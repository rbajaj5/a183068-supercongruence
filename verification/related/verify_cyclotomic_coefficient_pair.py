"""Exact checks for the A228960/A350383 coefficientwise theorem.

The proof is in related-results/CyclotomicCoefficientPairTheorem.md.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Iterable

Coefficient = Callable[[int, int], int]
GaussianInteger = tuple[int, int]


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def a228960_coefficient(n: int, k: int) -> int:
    if k < 0 or 3 * k > n:
        return 0
    return math.comb(n, k) * math.comb(n, 3 * k)


def a350383_coefficient(n: int, k: int) -> int:
    if k < 0 or 3 * k > n:
        return 0
    if n == 0:
        return int(k == 0)
    return (
        (-1) ** (n - k)
        * math.comb(n + k - 1, k)
        * math.comb(n, 3 * k)
    )


def coefficient_difference(
    coefficient: Coefficient, prime: int, r: int, n: int, k: int
) -> int:
    upper_n = n * prime**r
    lower_n = n * prime ** (r - 1)
    upper = coefficient(upper_n, k)
    lower = (
        coefficient(lower_n, k // prime) if k % prime == 0 else 0
    )
    return upper - lower


def polynomial_value(
    coefficient: Coefficient, n: int, x: int
) -> int:
    return sum(
        coefficient(n, k) * x**k for k in range(n // 3 + 1)
    )


def gaussian_value(coefficient: Coefficient, n: int) -> GaussianInteger:
    real = 0
    imag = 0
    for k in range(n // 3 + 1):
        term = coefficient(n, k)
        if k % 4 == 0:
            real += term
        elif k % 4 == 1:
            imag += term
        elif k % 4 == 2:
            real -= term
        else:
            imag -= term
    return real, imag


def grid() -> Iterable[tuple[int, int, int]]:
    for prime in (5, 7, 11, 13):
        for r, n_max in ((1, 8), (2, 4), (3, 1)):
            for n in range(1, n_max + 1):
                yield prime, r, n


def run_family(name: str, coefficient: Coefficient) -> tuple[int, int, int]:
    coefficient_checks = 0
    aggregate_checks = 0
    gaussian_checks = 0
    equality_witnesses: list[tuple[int, int, int, int, int]] = []

    for prime, r, n in grid():
        required = 2 * r
        upper_n = n * prime**r
        lower_n = n * prime ** (r - 1)

        for k in range(upper_n // 3 + 1):
            actual = valuation(
                coefficient_difference(coefficient, prime, r, n, k),
                prime,
            )
            assert actual >= required, (
                name,
                prime,
                r,
                n,
                k,
                actual,
                required,
            )
            if actual == required:
                equality_witnesses.append((prime, r, n, k, actual))
            coefficient_checks += 1

        aggregate_difference = polynomial_value(
            coefficient, upper_n, 1
        ) - polynomial_value(coefficient, lower_n, 1)
        assert valuation(aggregate_difference, prime) >= required
        aggregate_checks += 1

        upper_real, upper_imag = gaussian_value(coefficient, upper_n)
        lower_real, lower_imag = gaussian_value(coefficient, lower_n)
        if prime % 4 == 3:
            lower_imag = -lower_imag
        real_difference = upper_real - lower_real
        imag_difference = upper_imag - lower_imag
        assert min(
            valuation(real_difference, prime),
            valuation(imag_difference, prime),
        ) >= required
        gaussian_checks += 1

    assert equality_witnesses
    print(f"{name} coefficient checks: {coefficient_checks}")
    print(f"{name} aggregate checks: {aggregate_checks}")
    print(f"{name} Gaussian checks: {gaussian_checks}")
    print(f"  equality witnesses: {equality_witnesses[:8]}")
    return coefficient_checks, aggregate_checks, gaussian_checks


def check_definitions_and_boundaries() -> None:
    assert [
        polynomial_value(a228960_coefficient, n, 1) for n in range(7)
    ] == [1, 1, 1, 4, 17, 51, 136]
    assert [
        polynomial_value(a350383_coefficient, n, 1) for n in range(7)
    ] == [1, -1, 1, 2, -15, 49, -98]

    # At p = 3, each family misses the proposed p^(2r) modulus already
    # at r = n = k = 1.
    for coefficient in (a228960_coefficient, a350383_coefficient):
        difference = coefficient_difference(coefficient, 3, 1, 1, 1)
        assert difference == 3
        assert valuation(difference, 3) == 1

    # The second family also fails at the ramified prime 2.
    binary_difference = coefficient_difference(
        a350383_coefficient, 2, 1, 1, 0
    )
    assert binary_difference == 2
    assert valuation(binary_difference, 2) == 1


def main() -> None:
    check_definitions_and_boundaries()
    totals = [0, 0, 0]
    for name, coefficient in (
        ("A228960", a228960_coefficient),
        ("A350383", a350383_coefficient),
    ):
        counts = run_family(name, coefficient)
        totals = [left + right for left, right in zip(totals, counts)]

    print(f"total coefficient checks: {totals[0]}")
    print(f"total aggregate checks: {totals[1]}")
    print(f"total Gaussian checks: {totals[2]}")
    print("small-prime boundary certificates: 3")


if __name__ == "__main__":
    main()
