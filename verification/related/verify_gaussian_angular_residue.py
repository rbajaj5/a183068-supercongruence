"""Exact checks for the cubic angular residue of Gaussian square power sums."""

from __future__ import annotations

import argparse
from math import comb
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from verification.related.verify_gaussian_power_sums import (
    Gaussian,
    gaussian_multiply,
    gaussian_power,
)


def primes_through(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = [False] * (
                (limit - prime * prime) // prime + 1
            )
    return [prime for prime, is_prime in enumerate(sieve) if is_prime]


def bernoulli_mod(index: int, prime: int) -> int:
    """Return B_index modulo prime, with B_1 = -1/2."""

    values = [1]
    for m in range(1, index + 1):
        subtotal = sum(
            comb(m + 1, k) * values[k]
            for k in range(m)
        )
        values.append((-subtotal * pow(m + 1, -1, prime)) % prime)
    return values[index]


def gaussian_sum(values: list[Gaussian], modulus: int) -> Gaussian:
    return (
        sum(value[0] for value in values) % modulus,
        sum(value[1] for value in values) % modulus,
    )


def scalar_multiply(value: Gaussian, scalar: int, modulus: int) -> Gaussian:
    return value[0] * scalar % modulus, value[1] * scalar % modulus


def verify_prime(prime: int) -> tuple[int, int]:
    modulus = prime**4
    bases = [
        (a, b)
        for a in range(1, prime)
        for b in range(1, prime)
    ]
    powers = [
        gaussian_power(base, prime - 1, modulus)
        for base in bases
    ]
    steps = [
        gaussian_power(base, 2 * (prime - 1), modulus)
        for base in bases
    ]

    first = gaussian_sum(powers, modulus)
    bernoulli = bernoulli_mod(prime - 3, prime)
    assert first[0] == 0
    assert first[1] % prime**3 == 0
    assert first[1] // prime**3 % prime == -bernoulli % prime

    checks = 0
    universal_roots = 0
    for r in range(1, 2 * prime, 2):
        actual = gaussian_sum(powers, modulus)
        coefficient = comb(r + 2, 3)
        expected_from_first = scalar_multiply(first, coefficient, modulus)
        expected_from_bernoulli = (
            0,
            (-prime**3 * coefficient * bernoulli) % modulus,
        )
        assert actual == expected_from_first, (
            prime,
            r,
            actual,
            expected_from_first,
        )
        assert actual == expected_from_bernoulli, (
            prime,
            r,
            actual,
            expected_from_bernoulli,
        )
        if r in {prime - 2, prime, 2 * prime - 1}:
            assert actual == (0, 0), (prime, r, actual)
            universal_roots += 1
        powers = [
            gaussian_multiply(power, step, modulus)
            for power, step in zip(powers, steps)
        ]
        checks += 1

    # The proven interval is genuinely nontrivial: the same cubic formula
    # already fails at the next odd multiplier for p = 7.
    if prime == 7:
        r = 2 * prime + 1
        actual = gaussian_sum(powers, modulus)
        coefficient = comb(r + 2, 3)
        expected = (
            0,
            (-prime**3 * coefficient * bernoulli) % modulus,
        )
        assert actual == (0, 2058)
        assert expected == (0, 1372)
        assert actual != expected

    return checks, universal_roots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    parser.add_argument(
        "--limit",
        type=int,
        help="override the prime bound (large bounds are cubic-time)",
    )
    args = parser.parse_args()
    limit = args.limit if args.limit is not None else (251 if args.extended else 199)

    primes = [
        prime
        for prime in primes_through(limit)
        if prime >= 7 and prime % 4 == 3
    ]
    residue_checks = 0
    universal_counterexamples = 0
    for prime in primes:
        checked, counterexamples = verify_prime(prime)
        residue_checks += checked
        universal_counterexamples += counterexamples

    print(f"inert primes checked: {len(primes)}")
    print(f"cubic angular residues checked: {residue_checks}")
    print(
        "universal r in {p-2,p,2p-1} counterexamples checked: "
        f"{universal_counterexamples}"
    )
    print("first-outside-range failure checked: p=7, r=15")


if __name__ == "__main__":
    main()
