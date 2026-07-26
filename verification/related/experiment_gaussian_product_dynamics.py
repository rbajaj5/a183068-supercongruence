#!/usr/bin/env python3
"""Exact finite-quotient dynamics of the ramified Gaussian product.

For the normalized isometry

    G_r(Z) = (F_r(Z) - 1) / c_r,

this script studies translated maps

    T_{r,a}(Z) = G_r(Z) + a

on Z_2[i] / (1+i)^n.  Quotient classes are encoded by their unique first
``n`` digits in the uniformizer 1+i, so every computation is exact.
"""

from __future__ import annotations

from fractions import Fraction

from verify_gaussian_product_isometry import (
    GaussianRational,
    first_log_coefficient,
    gadd,
    gdiv,
    gmul,
    gsub,
    normalized_product,
)


ONE: GaussianRational = (Fraction(1), Fraction(0))
PI: GaussianRational = (Fraction(1), Fraction(1))


def divide_by_pi(value: GaussianRational) -> GaussianRational:
    """Divide exactly by 1+i."""
    a, b = value
    return (a + b) / 2, (b - a) / 2


def fraction_mod_two(value: Fraction) -> int:
    """Reduce a 2-adically integral rational with odd denominator modulo 2."""
    assert value.denominator % 2
    return value.numerator % 2


def residue_digit(value: GaussianRational) -> int:
    """Residue in Z_2[i]/(1+i), identified with F_2."""
    return (fraction_mod_two(value[0]) + fraction_mod_two(value[1])) % 2


def quotient_key(value: GaussianRational, precision: int) -> int:
    """Return the first ``precision`` uniformizer digits of ``value``."""
    key = 0
    current = value
    for position in range(precision):
        digit = residue_digit(current)
        key |= digit << position
        current = divide_by_pi(gsub(current, (Fraction(digit), Fraction(0))))
    return key


def quotient_representatives(precision: int) -> list[GaussianRational]:
    """Canonical representatives sum_j bit_j (1+i)^j."""
    powers: list[GaussianRational] = [ONE]
    for _ in range(1, precision):
        powers.append(gmul(powers[-1], PI))

    representatives: list[GaussianRational] = []
    for key in range(2**precision):
        value: GaussianRational = (Fraction(0), Fraction(0))
        for position, power in enumerate(powers):
            if key >> position & 1:
                value = gadd(value, power)
        assert quotient_key(value, precision) == key
        representatives.append(value)
    return representatives


def normalized_isometry(r: int, value: GaussianRational) -> GaussianRational:
    numerator = gsub(normalized_product(r, value), ONE)
    return gdiv(numerator, first_log_coefficient(r))


def permutation(
    r: int,
    translation: GaussianRational,
    precision: int,
) -> list[int]:
    representatives = quotient_representatives(precision)
    result = [
        quotient_key(
            gadd(normalized_isometry(r, value), translation),
            precision,
        )
        for value in representatives
    ]
    assert sorted(result) == list(range(2**precision))
    return result


def permutations_for_all_unit_translations(
    r: int,
    precision: int,
) -> list[list[int]]:
    representatives = quotient_representatives(precision)
    normalized_values = [
        normalized_isometry(r, value) for value in representatives
    ]
    mappings: list[list[int]] = []
    for key, translation in enumerate(representatives):
        if not key & 1:
            continue
        mapping = [
            quotient_key(gadd(value, translation), precision)
            for value in normalized_values
        ]
        assert sorted(mapping) == list(range(2**precision))
        mappings.append(mapping)
    return mappings


def cycle_lengths(mapping: list[int]) -> list[int]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = mapping[current]
        lengths.append(length)
    return sorted(lengths, reverse=True)


def main() -> None:
    translations: dict[str, GaussianRational] = {
        "1": ONE,
        "i": (Fraction(0), Fraction(1)),
        "1+pi": gadd(ONE, PI),
        "1+pi^2": gadd(ONE, gmul(PI, PI)),
    }

    for r, maximum_precision in ((2, 12), (3, 7)):
        print(f"r={r}")
        for name, translation in translations.items():
            profile: list[str] = []
            for precision in range(1, maximum_precision + 1):
                lengths = cycle_lengths(
                    permutation(r, translation, precision)
                )
                profile.append(
                    f"n={precision}:"
                    + ",".join(str(length) for length in lengths[:8])
                    + ("..." if len(lengths) > 8 else "")
                )
            print(f"  a={name}: " + " | ".join(profile))

    exhaustive_checks = 0
    for r, maximum_precision in ((2, 8), (3, 6)):
        for precision in range(1, maximum_precision + 1):
            expected_length = 2 ** ((precision + 1) // 2)
            expected_count = 2 ** (precision // 2)
            expected = [expected_length] * expected_count
            for mapping in permutations_for_all_unit_translations(
                r, precision
            ):
                assert cycle_lengths(mapping) == expected
                exhaustive_checks += 1
    print(
        "all-unit cycle-profile checks: "
        f"{exhaustive_checks} exact quotient maps passed"
    )


if __name__ == "__main__":
    main()
