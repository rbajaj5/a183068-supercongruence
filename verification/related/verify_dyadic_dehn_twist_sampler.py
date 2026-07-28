"""Exact checks for the dyadic Dehn-twist sampler and refresh chain."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def unit_from_coordinates(modulus: int, sign: int, exponent: int) -> int:
    factor = -1 if sign else 1
    return (factor * pow(5, exponent, modulus)) % modulus


def state_from_bits(bits: tuple[int, ...], level: int) -> tuple[int, int]:
    exponent_width = level - 2
    sign = bits[0]
    exponent = sum(
        bits[1 + index] << index for index in range(exponent_width)
    )
    translation_start = 1 + exponent_width
    translation = sum(
        bits[translation_start + index] << index
        for index in range(level)
    )
    modulus = 2**level
    return (
        unit_from_coordinates(modulus, sign, exponent),
        translation,
    )


def verify_binary_parametrization(max_level: int) -> None:
    for level in range(3, max_level + 1):
        dimension = 2 * level - 1
        states = {
            state_from_bits(
                tuple((mask >> index) & 1 for index in range(dimension)),
                level,
            )
            for mask in range(2**dimension)
        }
        assert len(states) == 2**dimension


def verify_four_element_lifts(max_level: int) -> None:
    for level in range(3, max_level):
        modulus = 2**level
        lifted_modulus = 2 ** (level + 1)
        for sign in (0, 1):
            for exponent in range(2 ** (level - 2)):
                for translation in range(modulus):
                    lower = (
                        unit_from_coordinates(modulus, sign, exponent),
                        translation,
                    )
                    lifts = {
                        (
                            unit_from_coordinates(
                                lifted_modulus,
                                sign,
                                exponent + exponent_bit * 2 ** (level - 2),
                            ),
                            translation + translation_bit * modulus,
                        )
                        for exponent_bit in (0, 1)
                        for translation_bit in (0, 1)
                    }
                    assert len(lifts) == 4
                    assert {
                        (unit % modulus, shift % modulus)
                        for unit, shift in lifts
                    } == {lower}


def walsh(mask: int, state: int) -> int:
    return -1 if (mask & state).bit_count() % 2 else 1


def verify_walsh_spectrum(dimensions: tuple[int, ...]) -> None:
    for dimension in dimensions:
        for mask in range(2**dimension):
            weight = mask.bit_count()
            for state in range(2**dimension):
                numerator = 0
                for coordinate in range(dimension):
                    cleared = state & ~(1 << coordinate)
                    set_bit = cleared | (1 << coordinate)
                    numerator += walsh(mask, cleared)
                    numerator += walsh(mask, set_bit)
                assert numerator == 2 * (dimension - weight) * walsh(
                    mask, state
                )
        assert sum(comb(dimension, weight) for weight in range(dimension + 1)) == (
            2**dimension
        )


def refresh_distribution(
    distribution: list[Fraction], dimension: int
) -> list[Fraction]:
    result = [Fraction(0) for _ in distribution]
    denominator = 2 * dimension
    for state, probability in enumerate(distribution):
        for coordinate in range(dimension):
            cleared = state & ~(1 << coordinate)
            set_bit = cleared | (1 << coordinate)
            result[cleared] += probability / denominator
            result[set_bit] += probability / denominator
    return result


def verify_chi_square(dimension: int, max_time: int) -> None:
    size = 2**dimension
    distribution = [Fraction(0) for _ in range(size)]
    distribution[0] = Fraction(1)
    uniform = Fraction(1, size)

    for time in range(max_time + 1):
        direct = sum(
            (probability - uniform) ** 2 / uniform
            for probability in distribution
        )
        spectral = sum(
            Fraction(comb(dimension, weight))
            * Fraction(dimension - weight, dimension) ** (2 * time)
            for weight in range(1, dimension + 1)
        )
        assert direct == spectral
        distribution = refresh_distribution(distribution, dimension)


def main() -> None:
    verify_binary_parametrization(8)
    verify_four_element_lifts(8)
    verify_walsh_spectrum((5, 7))
    verify_chi_square(5, 8)
    print("checked binary affine coordinates through modulus 2^8")
    print("checked every four-element lift fiber through modulus 2^8")
    print("checked Walsh eigenfunctions in dimensions 5 and 7")
    print("checked the chi-square identity by exact rational arithmetic")
    print("PASS")


if __name__ == "__main__":
    main()
