#!/usr/bin/env python3
"""Exact checks for the affine-depth filtration of the ramified block."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

from verify_gaussian_product_isometry import (
    GaussianRational,
    anisotropic_weights,
    critical_shell_weights,
    first_log_coefficient,
    gadd,
    gdiv,
    gpow,
    gsub,
    mixed_block,
    neighborhood_weights,
    vpi,
    weighted_first_log_coefficient,
    weighted_product,
)


def weighted_log_coefficient(
    r: int,
    k: int,
    weights: list[GaussianRational],
) -> GaussianRational:
    reciprocal_sum: GaussianRational = (Fraction(0), Fraction(0))
    for xi, weight in zip(mixed_block(r), weights, strict=True):
        reciprocal_sum = gadd(
            reciprocal_sum,
            gdiv(gpow(weight, k), gpow(xi, k)),
        )
    scale = Fraction((-1) ** (k + 1) * 2 ** (r * k), k)
    return scale * reciprocal_sum[0], scale * reciprocal_sum[1]


def candidate_masks(r: int) -> list[int]:
    size = len(mixed_block(r))
    if r == 2:
        return list(range(1 << size))
    masks = [0, (1 << size) - 1]
    masks.extend(1 << index for index in range(size))
    masks.extend(
        (1 << left) | (1 << right)
        for left, right in combinations(range(size), 2)
    )
    return masks


def depth_witnesses(r: int) -> dict[int, int]:
    normalization = gpow(
        (Fraction(1), Fraction(1)),
        6 * r - 3,
    )
    targets = set(range(2 * r - 1))
    witnesses: dict[int, int] = {}
    for mask in candidate_masks(r):
        weights = critical_shell_weights(r, mask)
        coefficient = weighted_first_log_coefficient(r, weights)
        if coefficient == (Fraction(0), Fraction(0)):
            continue
        defect = gdiv(coefficient, normalization)
        depth = vpi(defect)
        if depth in targets and depth not in witnesses:
            witnesses[depth] = mask
            if witnesses.keys() == targets:
                break
    assert witnesses.keys() == targets
    return witnesses


def main() -> None:
    square_checks = 0
    tail_checks = 0
    for r in range(2, 6):
        unit_weights = [
            (Fraction(1), Fraction(0)) for _ in mixed_block(r)
        ]
        square = weighted_log_coefficient(r, 2, unit_weights)
        assert vpi(square) >= 8 * r - 4
        square_checks += 1
        for k in range(2, 13):
            coefficient = weighted_log_coefficient(r, k, unit_weights)
            assert vpi(coefficient) >= 8 * r - 4
            tail_checks += 1

    points: list[GaussianRational] = [
        (Fraction(a), Fraction(b))
        for a in range(-2, 3)
        for b in range(-2, 3)
    ]

    depth_checks = 0
    pair_checks = 0
    weighted_tail_checks = 0
    neighborhood_tail_checks = 0
    for r in (2, 3):
        normalization = gpow(
            (Fraction(1), Fraction(1)),
            6 * r - 3,
        )
        assert vpi(first_log_coefficient(r)) == 6 * r - 3
        for depth, mask in depth_witnesses(r).items():
            weights = critical_shell_weights(r, mask)
            coefficient = weighted_first_log_coefficient(r, weights)
            defect = gdiv(coefficient, normalization)
            assert vpi(defect) == depth
            depth_checks += 1

            for k in range(2, 13):
                higher = weighted_log_coefficient(r, k, weights)
                assert vpi(higher) >= 8 * r - 4
                weighted_tail_checks += 1

            values = {
                point: weighted_product(r, point, weights)
                for point in points
            }
            for left, right in combinations(points, 2):
                source_difference = gsub(left, right)
                image_difference = gsub(values[left], values[right])
                assert vpi(image_difference) == (
                    6 * r - 3 + depth + vpi(source_difference)
                )
                pair_checks += 1

        for weight_builder in (neighborhood_weights, anisotropic_weights):
            for pattern in (0, 1):
                weights = weight_builder(r, pattern)
                for k in range(2, 13):
                    higher = weighted_log_coefficient(r, k, weights)
                    assert vpi(higher) >= 8 * r - 4
                    neighborhood_tail_checks += 1

    print(
        "Gaussian reciprocal-square improvement: "
        f"{square_checks} exact scale checks passed"
    )
    print(
        "Gaussian unweighted higher tail: "
        f"{tail_checks} exact coefficient checks passed"
    )
    print(
        "Gaussian affine depths: "
        f"{depth_checks} certified depth witnesses passed"
    )
    print(
        "Gaussian weighted higher tail: "
        f"{weighted_tail_checks} exact coefficient checks passed"
    )
    print(
        "Gaussian neighborhood higher tails: "
        f"{neighborhood_tail_checks} exact coefficient checks passed"
    )
    print(
        "Gaussian depth-stratified isometry: "
        f"{pair_checks} exact pair checks passed"
    )


if __name__ == "__main__":
    main()
