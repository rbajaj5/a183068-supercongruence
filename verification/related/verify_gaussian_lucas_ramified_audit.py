#!/usr/bin/env python3
"""Adversarial finite audit for the GWL-TWO transcription.

This checker deliberately tests near-miss mutants and nested ranges. It is
finite evidence, not a proof of the ramified Gaussian theorem.
"""

from __future__ import annotations

from experiment_gaussian_lucas_scaling import (
    INFINITY,
    exact_gaussian_multiply,
    exact_rectangular_parts,
    one_plus_i_valuation,
    ramified_two_valuations,
    small_rectangles,
)


Gaussian = tuple[int, int]


def conjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def check_conjugation(bound: int = 3) -> int:
    """Check Q(b,a;d,c) = conjugate(Q(a,b;c,d)) exactly."""
    checks = 0
    for scale in (2, 4, 8):
        for a, b, c, d in small_rectangles(bound):
            numerator, denominator = exact_rectangular_parts(
                scale * a, scale * b, scale * c, scale * d
            )
            swapped_numerator, swapped_denominator = exact_rectangular_parts(
                scale * b, scale * a, scale * d, scale * c
            )
            left = exact_gaussian_multiply(
                swapped_numerator, conjugate(denominator)
            )
            right = exact_gaussian_multiply(
                conjugate(numerator), swapped_denominator
            )
            assert left == right
            checks += 1
    return checks


def check_analytic_domains() -> tuple[int, dict[str, int]]:
    """Check the exact depth used for log/exp and the mu_4 boundary."""
    minimum_depth = INFINITY
    checks = 0
    for r in range(2, 7):
        bound = 2**r
        for a in range(1, bound + 1):
            for b in range(1, bound + 1):
                if a % 2 == 0 and b % 2 == 0:
                    continue
                xi_depth = one_plus_i_valuation((a, b))
                quotient_depth = 2 * r - xi_depth
                assert quotient_depth >= 3
                minimum_depth = min(minimum_depth, quotient_depth)
                checks += 1

    torsion_depths = {
        "i-1": one_plus_i_valuation((-1, 1)),
        "-1-1": one_plus_i_valuation((-2, 0)),
        "-i-1": one_plus_i_valuation((-1, -1)),
    }
    assert torsion_depths == {"i-1": 1, "-1-1": 2, "-i-1": 1}
    assert minimum_depth == 3
    return checks, torsion_depths


def check_formula_and_mutants(
    bound: int, levels: tuple[int, ...]
) -> tuple[int, dict[str, int]]:
    """Verify the formula and count survivors of five near-miss mutants."""
    survivors = {
        "exponent_plus_one": 0,
        "exponent_minus_one": 0,
        "omit_CD": 0,
        "shift_imaginary_coefficient": 0,
        "difference_equals_ratio": 0,
    }
    checks = 0
    for r in levels:
        for a, b, c, d in small_rectangles(bound):
            lower, difference, ratio = ramified_two_valuations(
                r, (a, b, c, d)
            )
            leading = (c * d * (a - c), c * d * (b - d))
            excess = one_plus_i_valuation(leading)
            expected = 6 * r - 3 + excess
            assert ratio == expected

            g_excess = one_plus_i_valuation((a - c, b - d))
            shifted = (
                c * d * (a - c),
                c * d * (b - d + 1),
            )
            shifted_excess = one_plus_i_valuation(shifted)

            survivors["exponent_plus_one"] += ratio == expected + 1
            survivors["exponent_minus_one"] += ratio == expected - 1
            survivors["omit_CD"] += ratio == 6 * r - 3 + g_excess
            survivors["shift_imaginary_coefficient"] += (
                shifted_excess < INFINITY
                and ratio == 6 * r - 3 + shifted_excess
            )
            survivors["difference_equals_ratio"] += difference == expected

            assert difference == lower + ratio
            checks += 1

    return checks, survivors


def main() -> None:
    prefix_checks, _ = check_formula_and_mutants(3, (2, 3))
    extended_checks, survivors = check_formula_and_mutants(6, (2, 3))
    scale_four_checks, _ = check_formula_and_mutants(3, (4,))
    conjugation_checks = check_conjugation()
    domain_checks, torsion_depths = check_analytic_domains()

    killed = {
        name: count < extended_checks for name, count in survivors.items()
    }
    assert all(killed.values())

    print(
        "GWL-TWO nested ranges passed: "
        f"prefix={prefix_checks}, extended={extended_checks}, "
        f"scale-four={scale_four_checks}"
    )
    print(f"conjugation checks: {conjugation_checks}")
    print(
        f"analytic-domain checks: {domain_checks}; "
        f"minimum log depth=3; torsion depths={torsion_depths}"
    )
    print(
        f"near-miss mutation kill rate: {sum(killed.values())}/"
        f"{len(killed)}; survivors={survivors}"
    )


if __name__ == "__main__":
    main()
