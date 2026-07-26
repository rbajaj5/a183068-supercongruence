#!/usr/bin/env python3
"""Exact checks for the ramified Gaussian product-isometry theorem.

For

    F_r(Z) = product_{xi in U_r} (1 + 2^r Z / xi),

the theorem predicts

    v_{1+i}(F_r(Z) - F_r(W))
      = 6r - 3 + v_{1+i}(Z - W).

All arithmetic below is exact in Q(i).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


GaussianRational = tuple[Fraction, Fraction]


def gadd(left: GaussianRational, right: GaussianRational) -> GaussianRational:
    return left[0] + right[0], left[1] + right[1]


def gsub(left: GaussianRational, right: GaussianRational) -> GaussianRational:
    return left[0] - right[0], left[1] - right[1]


def gmul(left: GaussianRational, right: GaussianRational) -> GaussianRational:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def ginv(value: GaussianRational) -> GaussianRational:
    a, b = value
    norm = a * a + b * b
    assert norm
    return a / norm, -b / norm


def gdiv(left: GaussianRational, right: GaussianRational) -> GaussianRational:
    return gmul(left, ginv(right))


def v2_integer(value: int) -> int:
    value = abs(value)
    assert value
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def v2_fraction(value: Fraction) -> int:
    assert value
    return v2_integer(value.numerator) - v2_integer(value.denominator)


def vpi(value: GaussianRational) -> int:
    """The (1+i)-valuation, computed from the rational norm."""
    a, b = value
    norm = a * a + b * b
    assert norm
    return v2_fraction(norm)


def mixed_block(r: int) -> list[GaussianRational]:
    scale = 2**r
    return [
        (Fraction(a), Fraction(b))
        for a in range(1, scale + 1)
        for b in range(1, scale + 1)
        if a % 2 or b % 2
    ]


def normalized_product(r: int, z: GaussianRational) -> GaussianRational:
    scale = Fraction(2**r)
    result: GaussianRational = (Fraction(1), Fraction(0))
    for xi in mixed_block(r):
        translated = gadd(xi, (scale * z[0], scale * z[1]))
        result = gmul(result, gdiv(translated, xi))
    return result


def first_log_coefficient(r: int) -> GaussianRational:
    reciprocal_sum: GaussianRational = (Fraction(0), Fraction(0))
    for xi in mixed_block(r):
        reciprocal_sum = gadd(reciprocal_sum, ginv(xi))
    scale = Fraction(2**r)
    return scale * reciprocal_sum[0], scale * reciprocal_sum[1]


def main() -> None:
    points: list[GaussianRational] = [
        (Fraction(a), Fraction(b))
        for a in range(-2, 3)
        for b in range(-2, 3)
    ]

    pair_checks = 0
    for r in (2, 3):
        coefficient = first_log_coefficient(r)
        assert vpi(coefficient) == 6 * r - 3

        values = {point: normalized_product(r, point) for point in points}
        assert values[(Fraction(0), Fraction(0))] == (
            Fraction(1),
            Fraction(0),
        )

        for left, right in combinations(points, 2):
            source_difference = gsub(left, right)
            image_difference = gsub(values[left], values[right])
            assert vpi(image_difference) == 6 * r - 3 + vpi(
                source_difference
            )

            normalized_difference = gdiv(image_difference, coefficient)
            assert vpi(normalized_difference) == vpi(source_difference)
            pair_checks += 1

    print(
        "Gaussian product isometry: "
        f"{pair_checks} exact pair checks across r=2,3 passed"
    )


if __name__ == "__main__":
    main()
