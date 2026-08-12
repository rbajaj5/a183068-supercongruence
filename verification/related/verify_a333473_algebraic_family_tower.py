"""Exact checks for the full A333473 algebraic-family quadratic tower."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def lagrange_term(r_slope: int, s_slope: int, n: int, j: int) -> Fraction:
    """The normalized summand T_{R,S}(N,j)."""

    upper = s_slope * n + 2 * j
    if upper < r_slope * n:
        return Fraction(0)
    return (
        Fraction(s_slope * n, upper)
        * comb(r_slope * n, j)
        * comb(upper, r_slope * n)
    )


def algebraic_family(r_slope: int, s_slope: int, n: int) -> int:
    value = sum(
        (lagrange_term(r_slope, s_slope, n, j) for j in range(r_slope * n + 1)),
        Fraction(0),
    )
    assert value.denominator == 1
    return value.numerator


def schroeder_series(degree: int) -> list[int]:
    coefficients = [1]
    for n in range(1, degree + 1):
        coefficient = int(n == 1)
        coefficient += sum(
            coefficients[j] * coefficients[n - 1 - j] for j in range(n)
        )
        coefficients.append(coefficient)
    return coefficients


def power_coefficient(base: list[int], power: int, degree: int) -> int:
    out = [1] + [0] * degree
    factor = base[: degree + 1]
    while power:
        if power & 1:
            out = [
                sum(out[j] * factor[n - j] for j in range(n + 1))
                for n in range(degree + 1)
            ]
        power //= 2
        if power:
            factor = [
                sum(factor[j] * factor[n - j] for j in range(n + 1))
                for n in range(degree + 1)
            ]
    return out[degree]


def check_lagrange_identity() -> int:
    checks = 0
    for r_slope in range(1, 5):
        for s_slope in range(1, 5):
            for n in range(1, 6):
                degree = r_slope * n
                direct = power_coefficient(
                    schroeder_series(degree), s_slope * n, degree
                )
                assert algebraic_family(r_slope, s_slope, n) == direct
                checks += 1
    return checks


def check_local_integrality() -> int:
    checks = 0
    for r_slope in range(1, 9):
        for s_slope in range(1, 9):
            for n in range(1, 9):
                for j in range(r_slope * n + 1):
                    assert lagrange_term(r_slope, s_slope, n, j).denominator == 1
                    checks += 1
    return checks


def check_coefficientwise_transfer() -> int:
    checks = 0
    for prime in (3, 5, 7, 11):
        for level in (1, 2, 3):
            modulus = prime ** (2 * level)
            for r_slope in range(1, 6):
                for s_slope in range(1, 6):
                    for base in range(1, 4):
                        n = base * prime**level
                        if n > 180:
                            continue
                        for j in range(r_slope * n + 1):
                            upper = lagrange_term(r_slope, s_slope, n, j)
                            lower = Fraction(0)
                            if j % prime == 0:
                                lower = lagrange_term(
                                    r_slope, s_slope, n // prime, j // prime
                                )
                            difference = upper - lower
                            assert difference.denominator == 1
                            assert difference.numerator % modulus == 0
                            checks += 1
    return checks


def main() -> None:
    results = {
        "Lagrange identity": check_lagrange_identity(),
        "summand integrality": check_local_integrality(),
        "coefficientwise quadratic transfer": check_coefficientwise_transfer(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
