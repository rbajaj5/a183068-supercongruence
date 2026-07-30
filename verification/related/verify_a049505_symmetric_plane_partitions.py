"""Exact checks for A049505SymmetricPlanePartitionCongruences.md."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def strip_prime(value: int, prime: int) -> tuple[int, int]:
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return value, out


def multiplicity(n: int, s: int) -> int:
    if s <= n:
        return (s + 1) // 2
    return n - s // 2


def exact_term(n: int) -> int:
    value = Fraction(1)
    for i in range(1, n + 1):
        value *= Fraction(
            factorial(2 * i - 2) * factorial(i + 2 * n - 1),
            factorial(i + n - 1) * factorial(2 * i + n - 2),
        )
    assert value.denominator == 1
    return value.numerator


def paired_exact(n: int) -> int:
    assert n % 2 == 1
    value = Fraction(2 ** ((n + 1) // 2))
    for s in range(1, n):
        value *= Fraction(
            (s + n) * (3 * n - s), s * (2 * n - s)
        ) ** multiplicity(n, s)
    assert value.denominator == 1
    return value.numerator


def term_mod_prime_power(n: int, prime: int, exponent: int) -> int:
    """Evaluate the paired product p-adically modulo prime**exponent."""
    assert n % 2 == 1
    modulus = prime**exponent
    value = pow(2, (n + 1) // 2, modulus)
    for s in range(1, n):
        numerator = (s + n) * (3 * n - s)
        denominator = s * (2 * n - s)
        num_unit, num_v = strip_prime(numerator, prime)
        den_unit, den_v = strip_prime(denominator, prime)
        assert num_v == den_v
        ratio = num_unit * pow(den_unit, -1, modulus) % modulus
        value = value * pow(ratio, multiplicity(n, s), modulus) % modulus
    return value


def main() -> None:
    initial = [
        1,
        2,
        10,
        112,
        2772,
        151008,
        18076916,
        4751252480,
        2740612658576,
    ]
    initial_checks = 0
    for n, expected in enumerate(initial):
        if n == 0:
            assert expected == 1
        else:
            assert exact_term(n) == expected
        initial_checks += 1

    pair_checks = 0
    for n in range(1, 18, 2):
        for s in range(1, 2 * n):
            brute = sum(
                1
                for i in range(1, n + 1)
                for j in range(i, n + 1)
                if i + j - 1 == s
            )
            assert multiplicity(n, s) == brute
            pair_checks += 1
        assert paired_exact(n) == exact_term(n)
        pair_checks += 1

    harmonic_checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        half = (prime - 1) // 2
        weighted = sum(
            ((t + 1) // 2) * pow(t, -2, prime)
            for t in range(1, prime)
        )
        odd_squares = sum(
            pow(t, -2, prime) for t in range(1, prime, 2)
        )
        half_squares = sum(
            pow(t, -2, prime) for t in range(1, half + 1)
        )
        assert weighted % prime == 0
        assert odd_squares % prime == 0
        assert half_squares % prime == 0
        harmonic_checks += 3

    master_checks = 0
    source_checks = 0
    for prime in (3, 5, 7, 11, 13):
        for r in (1, 2, 3):
            n = prime**r
            value = term_mod_prime_power(n, prime, 3)
            target = pow(2, (n + 1) // 2, prime**3)
            assert value == target
            master_checks += 1

        modulus = prime**3
        ap = term_mod_prime_power(prime, prime, 3)
        ap2 = term_mod_prime_power(prime**2, prime, 3)
        ap3 = term_mod_prime_power(prime**3, prime, 3)
        sign = -1 if ((prime * prime - 1) // 8) % 2 else 1
        assert ap == pow(2, (prime + 1) // 2, modulus)
        assert ap2 == sign * pow(ap, prime * prime - prime + 1, modulus) % modulus
        assert ap3 == pow(
            ap2, (prime**3 - prime**2 + 2) // 2, modulus
        )
        source_checks += 3

    assert exact_term(8) % 8 == pow(exact_term(4), 3, 8)
    source_checks += 1

    total = initial_checks + pair_checks + harmonic_checks + master_checks + source_checks
    print("A049505 symmetric-plane-partition checks passed")
    print(f"initial sequence checks: {initial_checks}")
    print(f"multiplicity and paired-product checks: {pair_checks}")
    print(f"harmonic cancellation checks: {harmonic_checks}")
    print(f"master prime-power checks: {master_checks}")
    print(f"source congruence checks: {source_checks}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
