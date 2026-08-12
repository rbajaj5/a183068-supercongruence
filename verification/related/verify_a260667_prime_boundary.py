"""Exact checks for the A260667 prime-boundary proof.

These checks are regression tests for the displayed proof, not substitutes
for it. Python integers and modular inverses are used throughout.
"""

from __future__ import annotations

from fractions import Fraction
from functools import cache
from math import comb


PRIMES = (
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
)


@cache
def apery_zeta2(n: int) -> int:
    return sum(comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1))


def s_polynomial(k: int, n: int) -> int:
    return sum(comb(k, j) * comb(n, j) * comb(n + j, j) for j in range(k + 1))


def a_direct(n: int) -> int:
    value = Fraction(
        sum((2 * k + 1) * s_polynomial(k, n) ** 2 for k in range(n)),
        n * n,
    )
    assert value.denominator == 1
    return value.numerator


def a_apery(n: int) -> int:
    current = apery_zeta2(n)
    previous = apery_zeta2(n - 1)
    value = Fraction(
        (n + 10) * current**2
        - (11 * n + 5) * current * previous
        - n * previous**2,
        25 * (n + 1),
    )
    assert value.denominator == 1
    return value.numerator


def harmonic(k: int, power: int, modulus: int) -> int:
    return sum(pow(j, -power, modulus) for j in range(1, k + 1)) % modulus


def check_formula_bridge() -> int:
    for n in range(1, 17):
        assert a_direct(n) == a_apery(n), n
    return 16


def check_prime_boundary() -> tuple[int, int]:
    sharp = 0
    for prime in PRIMES:
        difference = a_apery(prime - 1) - 1
        assert difference % prime**3 == 0, prime
        if difference % prime**4 != 0:
            sharp += 1
    assert sharp > 0
    return len(PRIMES), sharp


def check_local_expansion() -> int:
    cases = 0
    for prime in PRIMES[:12]:
        modulus = prime**3
        inverse_two = pow(2, -1, modulus)
        for k in range(prime - 1):
            h1 = harmonic(k, 1, modulus)
            h2 = harmonic(k, 2, modulus)
            predicted = (
                1
                - prime * h1
                + prime**2 * inverse_two * (h1 * h1 + h2)
            ) % modulus
            assert s_polynomial(k, prime - 1) % modulus == predicted, (prime, k)
            cases += 1
    return cases


def check_weighted_harmonics() -> int:
    cases = 0
    for prime in PRIMES:
        n = prime - 2
        modulus2 = prime**2
        weighted_linear = sum(
            (2 * k + 1) * harmonic(k, 1, modulus2) for k in range(n + 1)
        ) % modulus2
        assert weighted_linear == (-prime * (prime - 1) // 2) % modulus2

        weighted_quadratic = 0
        for k in range(n + 1):
            h1 = harmonic(k, 1, prime)
            h2 = harmonic(k, 2, prime)
            weighted_quadratic += (2 * k + 1) * (2 * h1 * h1 + h2)
        assert weighted_quadratic % prime == 1
        cases += 2
    return cases


def main() -> None:
    bridge = check_formula_bridge()
    boundary, sharp = check_prime_boundary()
    local = check_local_expansion()
    harmonic_cases = check_weighted_harmonics()
    total = bridge + boundary + local + harmonic_cases
    print(f"formula bridge: {bridge} exact values")
    print(f"prime boundary: {boundary} primes ({sharp} sharp modulo p^4)")
    print(f"local expansion: {local} (p,k) pairs")
    print(f"weighted harmonic identities: {harmonic_cases} congruences")
    print(f"all {total} A260667 checks passed")


if __name__ == "__main__":
    main()

