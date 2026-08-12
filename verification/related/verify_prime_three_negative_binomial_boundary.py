"""Exact checks for PrimeThreeNegativeBinomialBoundary.md."""

from __future__ import annotations

import random
from fractions import Fraction
from math import comb

from verify_bala_august_kernel_frobenius import (
    KernelCoefficients,
    mod_prime,
    rational_valuation,
)
from verify_mixed_negative_binomial_cubic_tower import (
    prefix_sum,
    prefix_sum_mod,
    valuation,
)


def fraction_mod_power(value: Fraction, modulus: int) -> int:
    assert value.denominator % 3 != 0
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def ternary_primitives(
    engine: KernelCoefficients, maximum: int
) -> tuple[dict[tuple[int, int], Fraction], dict[tuple[int, int], Fraction]]:
    """Canonical P,Q with C_3(HL^2) = D_x P + D_y Q."""

    first: dict[tuple[int, int], Fraction] = {}
    second: dict[tuple[int, int], Fraction] = {}
    for m in range(maximum + 1):
        for n in range(maximum + 1):
            coefficient = engine.h_l_power(2, 3 * m, 3 * n)
            if m == 0 and n == 0:
                assert coefficient == 0
            elif m != 0 and valuation(m, 3) <= (
                valuation(n, 3) if n else 10**9
            ):
                first[m, n] = coefficient / m
                assert first[m, n].denominator % 3 != 0
            else:
                second[m, n] = coefficient / n
                assert second[m, n].denominator % 3 != 0
    return first, second


def ternary_kernel(
    engine: KernelCoefficients,
    cutoff: int,
    maximum: int,
    first: dict[tuple[int, int], Fraction],
    second: dict[tuple[int, int], Fraction],
) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for m in range(maximum + 1):
        for n in range(maximum + 1):
            first_log = -cutoff * first.get((m, n), Fraction(0))
            first_log += engine.a * sum(
                (first.get((m - q, n), Fraction(0)) for q in range(1, m + 1)),
                Fraction(0),
            )
            second_log = -cutoff * second.get((m, n), Fraction(0))
            second_log += engine.b * sum(
                (second.get((m, n - q), Fraction(0)) for q in range(1, n + 1)),
                Fraction(0),
            )
            result[m, n] = engine.h_l_power(3, 3 * m, 3 * n) / 2
            result[m, n] -= (first_log + second_log) / 2
            assert result[m, n].denominator % 3 != 0
    return result


def residue_formula(a: int, b: int, cutoff: int, n: int) -> int:
    x_term = 0
    y_term = 0
    cross_term = 0
    for k in range(1, cutoff * n + 1):
        x_term += comb(a * n + k, k - 1) * comb(b * n + k - 1, k)
        y_term += comb(a * n + k - 1, k) * comb(b * n + k, k - 1)
        cross_term += comb(a * n + k - 1, k - 1) * comb(
            b * n + k - 1, k - 1
        )
    bracket = (
        a * a * x_term
        + a * b * cross_term
        + b * b * y_term
        + n * (a * x_term + b * y_term)
    )
    return (2 * n * n * bracket) % 3


def defect(a: int, b: int, cutoff: int, n: int, level: int) -> int:
    upper = n * 3**level
    return prefix_sum(a, b, cutoff, upper) - prefix_sum(
        a, b, cutoff, upper // 3
    )


def check_residue_formula() -> int:
    checks = 0
    for a in range(1, 13):
        for b in range(1, 13):
            for cutoff in range(1, 8):
                for n in range(1, 10):
                    difference = defect(a, b, cutoff, n, 1)
                    assert difference % 9 == 0
                    assert (difference // 9) % 3 == residue_formula(
                        a, b, cutoff, n
                    )
                    checks += 1
    return checks


def check_cubic_subclass() -> int:
    checks = 0
    for a in range(1, 16):
        for b in range(1, 16):
            for cutoff in range(1, 9):
                for n in range(1, 16):
                    if (n * a * b * (a + b)) % 3:
                        continue
                    assert residue_formula(a, b, cutoff, n) == 0
                    assert defect(a, b, cutoff, n, 1) % 27 == 0
                    checks += 1
    return checks


def check_sharp_boundary() -> int:
    assert prefix_sum(1, 1, 1, 1) == 2
    assert prefix_sum(1, 1, 1, 3) == 146
    assert valuation(144, 3) == 2

    assert prefix_sum(2, 2, 1, 1) == 5
    assert prefix_sum(2, 2, 1, 3) == 3614
    assert valuation(3614 - 5, 3) == 2

    assert prefix_sum(1, 1, 1, 2) == 14
    assert prefix_sum(1, 1, 1, 6) == 296438
    assert valuation(296438 - 14, 3) == 2

    assert prefix_sum(2, 2, 2, 2) == 1742
    assert prefix_sum(2, 2, 2, 6) == 2485268015414
    assert valuation(2485268015414 - 1742, 3) == 2

    first = defect(1, 1, 1, 1, 1)
    second = defect(1, 1, 1, 1, 2)
    assert valuation(second - 27 * first, 3) == 7
    return 14


def check_exact_renormalization_grid() -> int:
    checks = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for cutoff in range(1, 5):
                for n in range(1, 7):
                    previous = defect(a, b, cutoff, n, 1)
                    for level in (2, 3):
                        current = defect(a, b, cutoff, n, level)
                        assert (
                            current - 27 * previous
                        ) % 3 ** (3 * level + 1) == 0
                        previous = current
                        checks += 1
    return checks


def modular_defect(
    a: int,
    b: int,
    cutoff: int,
    n: int,
    level: int,
    precision: int,
) -> int:
    modulus = 3**precision
    upper = n * 3**level
    return (
        prefix_sum_mod(a, b, cutoff, upper, 3, precision)
        - prefix_sum_mod(a, b, cutoff, upper // 3, 3, precision)
    ) % modulus


def check_modular_renormalization_grid() -> int:
    rng = random.Random(31_590_271)
    checks = 0
    for _ in range(1_000):
        a = rng.randint(1, 30)
        b = rng.randint(1, 30)
        cutoff = rng.randint(1, 8)
        n = rng.randint(1, 20)
        level = rng.randint(2, 5)
        if cutoff * n * 3**level > 150_000:
            continue
        precision = 3 * level + 1
        modulus = 3**precision
        current = modular_defect(a, b, cutoff, n, level, precision)
        previous = modular_defect(a, b, cutoff, n, level - 1, precision)
        assert (current - 27 * previous) % modulus == 0
        checks += 1
    return checks


def check_bala_sum_levels() -> int:
    checks = 0
    for cutoff in range(1, 5):
        for n in range(1, 9):
            for level in range(1, 5):
                assert defect(1, 2, cutoff, n, level) % 3 ** (3 * level) == 0
                checks += 1
    return checks


def check_ternary_kernel_configuration(
    a: int, b: int, cutoff: int, window: int
) -> int:
    engine = KernelCoefficients(3, a, b)
    maximum = 3 * window
    first, second = ternary_primitives(engine, maximum)
    kernel = ternary_kernel(engine, cutoff, maximum, first, second)
    checks = 0

    for m in range(window + 1):
        for n in range(window + 1):
            if m != 0 or n != 0:
                lifted_square = engine.h_l_power(2, 9 * m, 9 * n)
                lifted_square -= 3 * engine.h_l_power(2, 3 * m, 3 * n)
                vm = valuation(m, 3) if m else 10**9
                vn = valuation(n, 3) if n else 10**9
                assert rational_valuation(lifted_square, 3) >= 3 + min(vm, vn)
                checks += 1

            green = engine.h_l_power(2, 3 * m, 3 * n)
            expected_green = (
                a * a * max(m - n, 0)
                + b * b * max(n - m, 0)
                - 2 * a * b * min(m, n)
            )
            assert fraction_mod_power(green, 9) == expected_green % 9
            checks += 1

            assert fraction_mod_power(
                first.get((3 * m, 3 * n), Fraction(0))
                - first.get((m, n), Fraction(0)),
                9,
            ) == 0
            assert fraction_mod_power(
                second.get((3 * m, 3 * n), Fraction(0))
                - second.get((m, n), Fraction(0)),
                9,
            ) == 0
            checks += 2

            assert fraction_mod_power(
                kernel[3 * m, 3 * n] - kernel[m, n], 9
            ) == 0
            checks += 1

            kernel_times_log = sum(
                (
                    kernel.get((3 * m - q, 3 * n), Fraction(0))
                    * Fraction(a, q)
                    for q in range(1, 3 * m + 1)
                    if q % 3
                ),
                Fraction(0),
            )
            kernel_times_log += sum(
                (
                    kernel.get((3 * m, 3 * n - q), Fraction(0))
                    * Fraction(b, q)
                    for q in range(1, 3 * n + 1)
                    if q % 3
                ),
                Fraction(0),
            )
            assert fraction_mod_power(kernel_times_log, 3) == 0
            checks += 1

            cube_difference = engine.h_l_power(3, 9 * m, 9 * n)
            cube_difference -= engine.h_l_power(3, 3 * m, 3 * n)
            if m >= n:
                expected_cube = (
                    2 * a**3 * (m - n) + 3 * a * b * (a + b) * n
                )
            else:
                expected_cube = (
                    2 * b**3 * (n - m) + 3 * a * b * (a + b) * m
                )
            assert fraction_mod_power(cube_difference, 9) == expected_cube % 9
            checks += 1

            first_shifts = sum(
                (
                    first.get((3 * m - q, 3 * n), Fraction(0))
                    for q in range(1, 3 * m + 1)
                    if q % 3
                ),
                Fraction(0),
            )
            second_shifts = sum(
                (
                    second.get((3 * m, 3 * n - q), Fraction(0))
                    for q in range(1, 3 * n + 1)
                    if q % 3
                ),
                Fraction(0),
            )
            assert fraction_mod_power(
                cube_difference - a * first_shifts - b * second_shifts, 9
            ) == 0
            checks += 1
    return checks


def check_ternary_kernel() -> int:
    return sum(
        check_ternary_kernel_configuration(*configuration)
        for configuration in (
            (1, 1, 1, 7),
            (1, 2, 1, 7),
            (2, 3, 2, 6),
            (4, 5, 3, 5),
            (3, 6, 3, 5),
        )
    )


def main() -> None:
    sections = {
        "exact first-defect formula": check_residue_formula(),
        "proved cubic subclass": check_cubic_subclass(),
        "sharp boundaries": check_sharp_boundary(),
        "exact renormalization evidence": check_exact_renormalization_grid(),
        "modular renormalization evidence": check_modular_renormalization_grid(),
        "Bala-sum level evidence": check_bala_sum_levels(),
        "ternary kernel identities": check_ternary_kernel(),
    }
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"prime-three boundary checks passed: {sum(sections.values())}")


if __name__ == "__main__":
    main()
