"""Exact checks for MixedNegativeBinomialCubicTower.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rational_valuation(value: Fraction, prime: int) -> int:
    return valuation(value.numerator, prime) - valuation(
        value.denominator, prime
    )


def valuation_and_unit(value: int, prime: int) -> tuple[int, int]:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent, value


def prefix_sum(a: int, b: int, cutoff: int, n: int) -> int:
    return sum(
        comb(a * n + k - 1, k) * comb(b * n + k - 1, k)
        for k in range(cutoff * n + 1)
    )


def prefix_sum_mod(
    a: int,
    b: int,
    cutoff: int,
    n: int,
    prime: int,
    precision: int,
) -> int:
    modulus = prime**precision
    unit = 1
    exponent = 0
    total = 1
    for k in range(1, cutoff * n + 1):
        first_exponent, first_unit = valuation_and_unit(a * n + k - 1, prime)
        second_exponent, second_unit = valuation_and_unit(b * n + k - 1, prime)
        lower_exponent, lower_unit = valuation_and_unit(k, prime)
        exponent += first_exponent + second_exponent - 2 * lower_exponent
        assert exponent >= 0
        unit *= first_unit * second_unit
        unit *= pow(lower_unit, -2, modulus)
        unit %= modulus
        if exponent < precision:
            total += unit * prime**exponent
            total %= modulus
    return total


def square_cartier_coefficient(prime: int, m: int) -> Fraction:
    total = prime * m
    return sum(
        Fraction(1, j * (total - j))
        for j in range(1, total)
        if j % prime
    )


def cross_cartier_coefficient(prime: int, m: int, n: int) -> Fraction:
    return sum(
        Fraction(1, j * (j + prime * m))
        for j in range(max(1, 1 - prime * m), prime * n + 1)
        if j % prime
    )


def check_source_values() -> int:
    expected = (1, 3, 39, 705, 14343, 310878, 7012533, 162602583)
    checks = 0
    for n, value in enumerate(expected):
        actual = 1 if n == 0 else prefix_sum(1, 2, 1, n)
        assert actual == value
        checks += 1
    return checks


def check_square_bound() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for m in range(1, 31):
            coefficient = square_cartier_coefficient(prime, m)
            assert rational_valuation(coefficient, prime) >= (
                1 + valuation(m, prime)
            )
            checks += 1
    return checks


def check_cross_bound() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for m in range(-12, 13):
            for n in range(1, 13):
                coefficient = cross_cartier_coefficient(prime, m, n)
                if coefficient == 0:
                    checks += 1
                    continue
                minimum = min(valuation(m, prime), valuation(n, prime))
                assert rational_valuation(coefficient, prime) >= 1 + minimum
                checks += 1
    return checks


def check_exact_towers() -> int:
    checks = 0
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            for cutoff in (1, 2, 3):
                for prime in (5, 7, 11):
                    for n in (1, 2):
                        for level in (1, 2):
                            large_n = n * prime**level
                            small_n = large_n // prime
                            difference = prefix_sum(
                                a, b, cutoff, large_n
                            ) - prefix_sum(a, b, cutoff, small_n)
                            assert difference % prime ** (3 * level) == 0
                            checks += 1
    return checks


def check_modular_towers() -> int:
    configurations = (
        (1, 1, 1),
        (1, 2, 1),
        (2, 3, 2),
        (3, 5, 1),
        (4, 1, 3),
        (5, 7, 2),
    )
    checks = 0
    for a, b, cutoff in configurations:
        for prime in (5, 7, 11, 13):
            for n in (1, 2, 3, 4):
                for level in (1, 2, 3):
                    large_n = n * prime**level
                    if cutoff * large_n > 100_000:
                        continue
                    precision = 3 * level
                    modulus = prime**precision
                    difference = (
                        prefix_sum_mod(
                            a, b, cutoff, large_n, prime, precision
                        )
                        - prefix_sum_mod(
                            a,
                            b,
                            cutoff,
                            large_n // prime,
                            prime,
                            precision,
                        )
                    ) % modulus
                    assert difference == 0
                    checks += 1
    return checks


def main() -> None:
    sections = {
        "source values": check_source_values(),
        "square Cartier bound": check_square_bound(),
        "cross Cartier bound": check_cross_bound(),
        "exact cubic towers": check_exact_towers(),
        "modular cubic towers": check_modular_towers(),
    }
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"mixed negative-binomial checks passed: {sum(sections.values())}")


if __name__ == "__main__":
    main()
