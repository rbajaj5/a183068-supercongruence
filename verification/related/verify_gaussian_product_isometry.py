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


def gpow(value: GaussianRational, exponent: int) -> GaussianRational:
    result: GaussianRational = (Fraction(1), Fraction(0))
    base = value
    while exponent:
        if exponent & 1:
            result = gmul(result, base)
        base = gmul(base, base)
        exponent //= 2
    return result


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


def weighted_product(
    r: int,
    z: GaussianRational,
    weights: list[GaussianRational],
) -> GaussianRational:
    scale = Fraction(2**r)
    result: GaussianRational = (Fraction(1), Fraction(0))
    block = mixed_block(r)
    assert len(weights) == len(block)
    for xi, weight in zip(block, weights, strict=True):
        increment = gdiv(
            gmul(weight, (scale * z[0], scale * z[1])),
            xi,
        )
        result = gmul(result, gadd((Fraction(1), Fraction(0)), increment))
    return result


def weighted_first_log_coefficient(
    r: int,
    weights: list[GaussianRational],
) -> GaussianRational:
    reciprocal_sum: GaussianRational = (Fraction(0), Fraction(0))
    block = mixed_block(r)
    assert len(weights) == len(block)
    for xi, weight in zip(block, weights, strict=True):
        reciprocal_sum = gadd(reciprocal_sum, gdiv(weight, xi))
    scale = Fraction(2**r)
    return scale * reciprocal_sum[0], scale * reciprocal_sum[1]


def neighborhood_weights(r: int, pattern: int) -> list[GaussianRational]:
    pi_power = gpow((Fraction(1), Fraction(1)), 4 * r - 1)
    weights: list[GaussianRational] = []
    for a_fraction, b_fraction in mixed_block(r):
        a = int(a_fraction)
        b = int(b_fraction)
        if pattern == 0:
            perturbation = (
                Fraction((a + 2 * b) % 5 - 2),
                Fraction((2 * a - b) % 5 - 2),
            )
        else:
            perturbation = (
                Fraction(1 if (a + b) % 2 == 0 else -1),
                Fraction(1 if a % 2 else 0),
            )
        weights.append(
            gadd(
                (Fraction(1), Fraction(0)),
                gmul(pi_power, perturbation),
            )
        )
    return weights


def anisotropic_weights(r: int, pattern: int) -> list[GaussianRational]:
    weights: list[GaussianRational] = []
    for a_fraction, b_fraction in mixed_block(r):
        xi = (a_fraction, b_fraction)
        a = int(a_fraction)
        b = int(b_fraction)
        pi_power = gpow(
            (Fraction(1), Fraction(1)),
            4 * r - 2 + vpi(xi),
        )
        if pattern == 0:
            perturbation = (
                Fraction((a + 2 * b) % 5 - 2),
                Fraction((2 * a - b) % 5 - 2),
            )
        else:
            perturbation = (
                Fraction(1 if (a + b) % 2 == 0 else -1),
                Fraction(1 if a % 2 else 0),
            )
        weights.append(
            gadd(
                (Fraction(1), Fraction(0)),
                gmul(pi_power, perturbation),
            )
        )
    return weights


def coordinate_boundary_weights(
    r: int,
    index: int,
) -> tuple[list[GaussianRational], GaussianRational]:
    block = mixed_block(r)
    weights = [(Fraction(1), Fraction(0)) for _ in block]
    xi = block[index]
    coefficient = first_log_coefficient(r)
    numerator = gmul(coefficient, xi)
    scale = Fraction(2**r)
    perturbation = (-numerator[0] / scale, -numerator[1] / scale)
    assert vpi(perturbation) == 4 * r - 3 + vpi(xi)
    weights[index] = gadd(weights[index], perturbation)
    return weights, perturbation


def main() -> None:
    points: list[GaussianRational] = [
        (Fraction(a), Fraction(b))
        for a in range(-2, 3)
        for b in range(-2, 3)
    ]

    pair_checks = 0
    neighborhood_checks = 0
    anisotropic_checks = 0
    boundary_checks = 0
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

        for pattern in (0, 1):
            weights = neighborhood_weights(r, pattern)
            weighted_coefficient = weighted_first_log_coefficient(r, weights)
            assert vpi(weighted_coefficient) == 6 * r - 3
            assert vpi(gsub(weighted_coefficient, coefficient)) >= 6 * r - 2

            weighted_values = {
                point: weighted_product(r, point, weights) for point in points
            }
            assert weighted_values[(Fraction(0), Fraction(0))] == (
                Fraction(1),
                Fraction(0),
            )
            for left, right in combinations(points, 2):
                source_difference = gsub(left, right)
                image_difference = gsub(
                    weighted_values[left], weighted_values[right]
                )
                assert vpi(image_difference) == 6 * r - 3 + vpi(
                    source_difference
                )
                normalized_difference = gdiv(
                    image_difference, weighted_coefficient
                )
                assert vpi(normalized_difference) == vpi(source_difference)
                neighborhood_checks += 1

        for pattern in (0, 1):
            weights = anisotropic_weights(r, pattern)
            weighted_coefficient = weighted_first_log_coefficient(r, weights)
            assert vpi(weighted_coefficient) == 6 * r - 3
            assert vpi(gsub(weighted_coefficient, coefficient)) >= 6 * r - 2

            weighted_values = {
                point: weighted_product(r, point, weights) for point in points
            }
            for left, right in combinations(points, 2):
                source_difference = gsub(left, right)
                image_difference = gsub(
                    weighted_values[left], weighted_values[right]
                )
                assert vpi(image_difference) == 6 * r - 3 + vpi(
                    source_difference
                )
                normalized_difference = gdiv(
                    image_difference, weighted_coefficient
                )
                assert vpi(normalized_difference) == vpi(source_difference)
                anisotropic_checks += 1

        block = mixed_block(r)
        odd_odd_index = next(
            index for index, xi in enumerate(block) if vpi(xi) == 1
        )
        unit_index = next(
            index for index, xi in enumerate(block) if vpi(xi) == 0
        )
        for index in (odd_odd_index, unit_index):
            boundary_weights, _ = coordinate_boundary_weights(r, index)
            boundary_coefficient = weighted_first_log_coefficient(
                r, boundary_weights
            )
            assert boundary_coefficient == (Fraction(0), Fraction(0))
            boundary_checks += 1

    print(
        "Gaussian product isometry: "
        f"{pair_checks} exact pair checks across r=2,3 passed"
    )
    print(
        "Gaussian parameter neighborhood: "
        f"{neighborhood_checks} exact pair checks across r=2,3 passed"
    )
    print(
        "Gaussian anisotropic chamber: "
        f"{anisotropic_checks} exact pair checks across r=2,3 passed"
    )
    print(
        "Gaussian coordinate radii: "
        f"{boundary_checks} sharp boundary checks passed"
    )


if __name__ == "__main__":
    main()
