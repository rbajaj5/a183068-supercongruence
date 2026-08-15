"""Exact checks for the enhanced A376458 pure-prime tower."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


PRIMES = (5, 7, 11)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def rational_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def fraction_mod(value: Fraction, modulus: int) -> int:
    return value.numerator * pow(value.denominator % modulus, -1, modulus) % modulus


def local_polynomial(value: Fraction) -> Fraction:
    return (1 - value) ** 3 * (1 + value)


def term(n: int, j: int) -> int:
    return (
        (-1) ** j
        * comb(n, j) ** 2
        * comb(n - 1, j)
        * comb(n + j - 1, j)
    )


def unit_quotient(prime: int, n: int, j: int) -> Fraction:
    out = Fraction(1)
    for h in range(1, prime * j):
        if h % prime:
            out *= local_polynomial(Fraction(prime * n, h))
    return out


def unit_power_sum(prime: int, exponent: int, power: int) -> Fraction:
    return sum(
        (Fraction(1, u**power) for u in range(1, prime**exponent) if u % prime),
        Fraction(),
    )


@lru_cache(maxsize=None)
def sequence(n: int) -> int:
    return sum(term(n, j) for j in range(n))


def check_exact_quotient_and_bounds() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in (1, 2):
            n = prime**exponent
            for j in range(1, min(n, 70)):
                quotient = unit_quotient(prime, n, j)
                assert Fraction(term(prime * n, prime * j), term(n, j)) == quotient
                q = valuation(j, prime)
                assert valuation(term(n, j), prime) >= 3 * (exponent - q)
                expected = exponent + 2 * q + 3 if q <= exponent else 3 * exponent + 3
                assert rational_valuation(quotient - 1, prime) >= expected
                checks += 3
    return checks


def check_outer_shell() -> int:
    checks = 0
    for prime in PRIMES:
        modulus = prime**3
        for a in range(1, prime):
            for b in range(prime):
                k = a + prime * b
                harmonic = sum(
                    (Fraction(1, h) for h in range(1, b + 1)), Fraction()
                )
                harmonic_two = sum(
                    (Fraction(1, h * h) for h in range(1, b + 1)), Fraction()
                )
                short_harmonic = sum(
                    (Fraction(1, h) for h in range(1, a)), Fraction()
                )
                linear = -Fraction(3 * b, a) - 2 * harmonic
                quadratic = (
                    Fraction(6 * b * b, a * a)
                    + Fraction(6 * b, a) * harmonic
                    + 2 * harmonic**2
                    - 2 * harmonic_two
                    - 2 * short_harmonic
                    - Fraction(1, a)
                )
                prediction = Fraction(1, a**3) * (
                    1 + prime * linear + prime**2 * quadratic
                )
                assert fraction_mod(
                    Fraction(term(prime**2, k), prime**6) - prediction,
                    modulus,
                ) == 0
                checks += 1
        for exponent in (2, 3):
            if prime**exponent > 400:
                continue
            n = prime**exponent
            normalized = sum(term(n, k) // n**3 for k in range(1, n) if k % prime)
            assert normalized % prime**3 == 0
            checks += 1
    return checks


def check_penultimate_shell() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in (2, 3):
            if prime**exponent > 400:
                continue
            n = prime**exponent
            tau = unit_power_sum(prime, exponent - 1, 2) / prime ** (exponent - 1)
            total = Fraction()
            for a in range(1, prime**2):
                if a % prime:
                    j = prime ** (exponent - 2) * a
                    quotient = unit_quotient(prime, n, j)
                    assert fraction_mod(
                        Fraction(term(n, j), prime**6) - Fraction(1, a**3), prime
                    ) == 0
                    normalized = (quotient - 1) / prime ** (3 * exponent - 1)
                    assert fraction_mod(normalized - tau * a * a, prime) == 0
                    total += term(n, j) * (quotient - 1)
                    checks += 2
            assert rational_valuation(total, prime) >= 3 * exponent + 6
            checks += 1
    return checks


def check_critical_shell() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in (1, 2):
            if prime == 5 and exponent == 1:
                continue
            n = prime**exponent
            tau = unit_power_sum(prime, exponent, 2) / prime**exponent
            total = Fraction()
            for a in range(1, prime):
                j = prime ** (exponent - 1) * a
                quotient = unit_quotient(prime, n, j)
                harmonic = sum((Fraction(1, h) for h in range(1, a)), Fraction())
                term_prediction = Fraction(1, a**3) * (
                    1 - Fraction(prime, a) - 2 * prime * harmonic
                )
                assert fraction_mod(
                    Fraction(term(n, j), prime**3) - term_prediction, prime**2
                ) == 0
                normalized = term(n, j) * (quotient - 1) / prime ** (
                    3 * exponent + 4
                )
                prediction = tau * (
                    Fraction(1, a)
                    - Fraction(3 * prime, a * a)
                    - Fraction(2 * prime, a) * harmonic
                )
                assert fraction_mod(normalized - prediction, prime**2) == 0
                total += term(n, j) * (quotient - 1)
                checks += 2
            assert rational_valuation(total, prime) >= 3 * exponent + 6
            checks += 1
    return checks


def check_harmonics_and_boundary() -> int:
    checks = 0
    for prime in (7, 11, 13, 17):
        h1 = sum((Fraction(1, a) for a in range(1, prime)), Fraction())
        h2 = sum((Fraction(1, a * a) for a in range(1, prime)), Fraction())
        double = sum(
            (
                sum((Fraction(1, h) for h in range(1, a)), Fraction()) / a
                for a in range(1, prime)
            ),
            Fraction(),
        )
        assert rational_valuation(h1, prime) >= 2
        assert rational_valuation(h2, prime) >= 1
        assert double == (h1 * h1 - h2) / 2
        assert rational_valuation(double, prime) >= 1
        checks += 4

    boundary = sequence(25) - sequence(5)
    expected = 2**2 * 3**2 * 5**9 * 67 * 97 * 7741 * 49223 * 129289
    assert boundary == expected
    assert valuation(boundary, 5) == 9
    checks += 2
    return checks


def check_tower() -> int:
    checks = 0
    minimum_slack = 10**9
    for prime in PRIMES:
        for level in (2, 3):
            if prime**level > 1500:
                continue
            difference = sequence(prime**level) - sequence(prime ** (level - 1))
            slack = valuation(difference, prime) - (3 * level + 3)
            assert slack >= 0, (prime, level, slack)
            minimum_slack = min(minimum_slack, slack)
            checks += 1
    assert minimum_slack == 0
    return checks


def main() -> None:
    quotient = check_exact_quotient_and_bounds()
    outer = check_outer_shell()
    penultimate = check_penultimate_shell()
    critical = check_critical_shell()
    harmonic = check_harmonics_and_boundary()
    tower = check_tower()
    total = quotient + outer + penultimate + critical + harmonic + tower
    print(f"exact quotient and bound checks: {quotient}")
    print(f"outer-shell checks: {outer}")
    print(f"penultimate-shell checks: {penultimate}")
    print(f"critical-shell checks: {critical}")
    print(f"harmonic and boundary checks: {harmonic}")
    print(f"enhanced A376458 tower checks: {tower}")
    print(f"all {total} checks passed")


if __name__ == "__main__":
    main()
