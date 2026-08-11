"""Exact checks for PrimeThreeNegativeBinomialBoundary.md."""

from __future__ import annotations

import random
from math import comb

from verify_mixed_negative_binomial_cubic_tower import (
    prefix_sum,
    prefix_sum_mod,
    valuation,
)


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
            if (a + b) % 3:
                continue
            for cutoff in range(1, 9):
                for n in range(1, 16):
                    assert residue_formula(a, b, cutoff, n) == 0
                    assert defect(a, b, cutoff, n, 1) % 27 == 0
                    checks += 1
    return checks


def check_sharp_boundary() -> int:
    assert prefix_sum(1, 1, 1, 1) == 2
    assert prefix_sum(1, 1, 1, 3) == 146
    assert valuation(144, 3) == 2

    first = defect(1, 1, 1, 1, 1)
    second = defect(1, 1, 1, 1, 2)
    assert valuation(second - 27 * first, 3) == 7
    return 5


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


def main() -> None:
    sections = {
        "exact first-defect formula": check_residue_formula(),
        "proved cubic subclass": check_cubic_subclass(),
        "sharp boundaries": check_sharp_boundary(),
        "exact renormalization evidence": check_exact_renormalization_grid(),
        "modular renormalization evidence": check_modular_renormalization_grid(),
        "Bala-sum level evidence": check_bala_sum_levels(),
    }
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"prime-three boundary checks passed: {sum(sections.values())}")


if __name__ == "__main__":
    main()
