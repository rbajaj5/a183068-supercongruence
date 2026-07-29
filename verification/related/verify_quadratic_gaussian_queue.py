"""Exact checks for the two quadratic polynomial Frobenius towers.

The proof is in related-results/QuadraticGaussianQueueTheorem.md.
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


def apery_coefficient(n: int, k: int) -> int:
    return (math.comb(n, k) * math.comb(n + k, k)) ** 2


def negative_binomial_coefficient(n: int, k: int) -> int:
    return math.comb(n + k - 1, k) ** 2


def generalized_negative_binomial_coefficient(
    v_parameter: int,
) -> Coefficient:
    return lambda n, k: math.comb(v_parameter * n + k - 1, k) ** 2


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


def gaussian_value(
    coefficient: Coefficient, n: int, upper_multiplier: int = 1
) -> GaussianInteger:
    real = 0
    imag = 0
    for k in range(upper_multiplier * n + 1):
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


def alternating_value(
    coefficient: Coefficient, n: int, upper_multiplier: int = 1
) -> int:
    return sum(
        (-1) ** k * coefficient(n, k)
        for k in range(upper_multiplier * n + 1)
    )


def gaussian_difference(
    coefficient: Coefficient,
    prime: int,
    r: int,
    n: int,
    upper_multiplier: int = 1,
) -> GaussianInteger:
    upper = gaussian_value(coefficient, n * prime**r, upper_multiplier)
    lower_n = n * prime ** (r - 1)
    if prime == 2:
        lower = (
            alternating_value(coefficient, lower_n, upper_multiplier),
            0,
        )
    else:
        lower = gaussian_value(coefficient, lower_n, upper_multiplier)
        if prime % 4 == 3:
            lower = lower[0], -lower[1]
    return upper[0] - lower[0], upper[1] - lower[1]


def grid() -> Iterable[tuple[int, int, int]]:
    for prime in (2, 3, 5, 7, 11):
        for r, n_max in ((1, 6), (2, 3), (3, 1)):
            for n in range(1, n_max + 1):
                yield prime, r, n


def run_family(
    name: str,
    coefficient: Coefficient,
    upper_multiplier: int = 1,
) -> tuple[int, int]:
    coefficient_checks = 0
    gaussian_checks = 0
    coefficient_equalities: list[tuple[int, int, int, int, int]] = []
    gaussian_equalities: list[tuple[int, int, int, int]] = []

    for prime, r, n in grid():
        required = 2 * r
        upper_n = upper_multiplier * n * prime**r
        for k in range(upper_n + 1):
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
                coefficient_equalities.append((prime, r, n, k, actual))
            coefficient_checks += 1

        real, imag = gaussian_difference(
            coefficient, prime, r, n, upper_multiplier
        )
        actual = min(valuation(real, prime), valuation(imag, prime))
        assert actual >= required, (
            name,
            prime,
            r,
            n,
            actual,
            required,
        )
        if actual == required:
            gaussian_equalities.append((prime, r, n, actual))
        gaussian_checks += 1

    assert coefficient_equalities
    assert gaussian_equalities
    print(f"{name} coefficient checks: {coefficient_checks}")
    print(f"{name} Gaussian checks: {gaussian_checks}")
    print(f"  coefficient equalities: {coefficient_equalities[:6]}")
    print(f"  Gaussian equalities: {gaussian_equalities[:6]}")
    return coefficient_checks, gaussian_checks


def main() -> None:
    total_coefficients = 0
    total_gaussian = 0
    for name, coefficient in (
        ("A005259", apery_coefficient),
        ("A333592", negative_binomial_coefficient),
    ):
        coefficient_checks, gaussian_checks = run_family(name, coefficient)
        total_coefficients += coefficient_checks
        total_gaussian += gaussian_checks

    generalized_checks = 0
    for u_parameter in range(1, 4):
        for v_parameter in range(1, 4):
            coefficient = generalized_negative_binomial_coefficient(
                v_parameter
            )
            for prime in (2, 3, 5, 7):
                for r, n_max in ((1, 3), (2, 1)):
                    for n in range(1, n_max + 1):
                        required = 2 * r
                        upper_n = u_parameter * n * prime**r
                        for k in range(upper_n + 1):
                            actual = valuation(
                                coefficient_difference(
                                    coefficient, prime, r, n, k
                                ),
                                prime,
                            )
                            assert actual >= required, (
                                u_parameter,
                                v_parameter,
                                prime,
                                r,
                                n,
                                k,
                                actual,
                                required,
                            )
                            generalized_checks += 1

                        real, imag = gaussian_difference(
                            coefficient,
                            prime,
                            r,
                            n,
                            u_parameter,
                        )
                        actual = min(
                            valuation(real, prime),
                            valuation(imag, prime),
                        )
                        assert actual >= required, (
                            u_parameter,
                            v_parameter,
                            prime,
                            r,
                            n,
                            actual,
                            required,
                        )
                        generalized_checks += 1

    print(f"total coefficient checks: {total_coefficients}")
    print(f"total Gaussian checks: {total_gaussian}")
    print(f"generalized A333592-family checks: {generalized_checks}")


if __name__ == "__main__":
    main()
