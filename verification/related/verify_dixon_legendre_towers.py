"""Exact checks for the Dixon--Legendre half-binomial tower.

The script is a regression certificate, not a proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def vp_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def vp_fraction(value: Fraction, prime: int) -> int:
    return vp_int(value.numerator, prime) - vp_int(value.denominator, prime)


def generalized_binomial(top: Fraction, lower: int) -> Fraction:
    out = Fraction(1)
    for j in range(lower):
        out *= top - j
    for j in range(1, lower + 1):
        out /= j
    return out


def dixon_sum(parameter: int, n: int) -> int:
    if n == 0:
        return 1
    return sum(
        comb((parameter - 1) * n - k - 1, n - k)
        * comb(parameter * n, k) ** 2
        for k in range(n + 1)
    )


def dixon_binomial_form(parameter: int, n: int) -> Fraction:
    if n == 0:
        return Fraction(1)
    return (
        comb(parameter * n, 2 * n)
        * generalized_binomial(Fraction((parameter + 2) * n, 2), n)
        * comb(2 * n, n)
        / generalized_binomial(Fraction(parameter * n, 2), n)
    )


def dixon_hypergeometric_form(parameter: int, n: int) -> Fraction:
    """The reversed finite 3F2 before applying Dixon's evaluation."""
    if n == 0:
        return Fraction(1)
    total = Fraction(0)
    term = Fraction(1)
    total += term
    a_top = (parameter - 2) * n
    bottom = (parameter - 1) * n + 1
    for j in range(n):
        term *= Fraction((a_top + j) * (-n + j) ** 2, (bottom + j) ** 2 * (j + 1))
        total += term
    return comb(parameter * n, n) ** 2 * total


def half_binomial(parameter: int, n: int) -> Fraction:
    return generalized_binomial(Fraction(parameter * n, 2), n)


def unit_product(parameter: int, n: int, prime: int) -> Fraction:
    out = Fraction(1)
    for j in range(1, n):
        if j % prime:
            out *= 1 - Fraction(parameter * n, 2 * j)
    return out


def unit_harmonics(n: int, prime: int) -> tuple[Fraction, Fraction]:
    first = Fraction(0)
    second = Fraction(0)
    for j in range(1, n):
        if j % prime:
            first += Fraction(1, j)
            second += Fraction(1, j * j)
    return first, second


def check_named_initial_values() -> int:
    expected = {
        3: [1, 10, 300, 11440, 485100, 21841260],
        5: [1, 28, 2646, 316540, 42031990, 5921058528],
    }
    checks = 0
    for parameter, values in expected.items():
        for n, value in enumerate(values):
            assert dixon_sum(parameter, n) == value
            checks += 1
    return checks


def check_exact_forms() -> int:
    checks = 0
    for parameter in range(3, 11):
        for n in range(0, 13):
            value = dixon_sum(parameter, n)
            binomial = dixon_binomial_form(parameter, n)
            hypergeometric = dixon_hypergeometric_form(parameter, n)
            assert binomial.denominator == 1
            assert value == binomial.numerator
            assert hypergeometric == value
            checks += 3
    return checks


def check_half_binomial_factorization() -> int:
    checks = 0
    for parameter in range(2, 11):
        for prime in (5, 7, 11):
            for m in range(1, 8):
                n = prime * m
                ratio = half_binomial(parameter, n) / half_binomial(parameter, m)
                assert ratio == unit_product(parameter, n, prime)
                checks += 1
    return checks


def check_harmonics() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for exponent in (1, 2):
            block = prime**exponent
            for multiplier in range(1, 6):
                first, second = unit_harmonics(multiplier * block, prime)
                assert vp_fraction(first, prime) >= 2 * exponent
                assert vp_fraction(second, prime) >= exponent
                checks += 2
    return checks


def check_half_binomial_tower() -> int:
    checks = 0
    for parameter in range(2, 11):
        for prime in (5, 7, 11):
            for r in (1, 2):
                for n in range(1, 5):
                    high = half_binomial(parameter, n * prime**r)
                    low = half_binomial(parameter, n * prime ** (r - 1))
                    assert vp_fraction(high / low - 1, prime) >= 3 * r
                    checks += 1
    return checks


def check_family_tower() -> int:
    checks = 0
    for parameter in range(3, 10):
        for prime in (5, 7, 11):
            for r in (1, 2):
                for n in range(1, 5):
                    high = dixon_sum(parameter, n * prime**r)
                    low = dixon_sum(parameter, n * prime ** (r - 1))
                    assert (high - low) % prime ** (3 * r) == 0
                    checks += 1
    return checks


def check_small_prime_boundaries() -> int:
    checks = 0
    for parameter in (3, 5):
        delta_two = dixon_sum(parameter, 2) - dixon_sum(parameter, 1)
        delta_three = dixon_sum(parameter, 3) - dixon_sum(parameter, 1)
        assert vp_int(delta_two, 2) == 1
        assert vp_int(delta_three, 3) == 2
        checks += 2
    return checks


def main() -> None:
    sections = {
        "named initial values": check_named_initial_values(),
        "three exact forms": check_exact_forms(),
        "half-binomial factorizations": check_half_binomial_factorization(),
        "unit-block harmonics": check_harmonics(),
        "half-binomial towers": check_half_binomial_tower(),
        "Dixon--Legendre family towers": check_family_tower(),
        "small-prime boundaries": check_small_prime_boundaries(),
    }
    print(f"Dixon--Legendre tower checks passed: {sum(sections.values())}")
    for name, count in sections.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
