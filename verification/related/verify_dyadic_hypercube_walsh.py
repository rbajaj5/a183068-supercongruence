"""Exact checks for the Walsh analysis of the dyadic hypercube defect.

The proof is in related-results/DyadicHypercubeWalshAnalysis.md. These
finite checks are regression certificates, not substitutes for the proof.
"""

from __future__ import annotations

import itertools
from fractions import Fraction
from math import comb


Exponent = tuple[int, ...]


def add_exponents(left: Exponent, right: Exponent) -> Exponent:
    return tuple(a + b for a, b in zip(left, right, strict=True))


def matching_data(
    support: tuple[Exponent, ...], target: Exponent
) -> tuple[list[tuple[int, int]], int | None]:
    pairs = [
        (left, right)
        for left in range(len(support))
        for right in range(left + 1, len(support))
        if add_exponents(support[left], support[right]) == target
    ]
    diagonal = next(
        (
            index
            for index, exponent in enumerate(support)
            if tuple(2 * value for value in exponent) == target
        ),
        None,
    )
    flat = [index for pair in pairs for index in pair]
    assert len(flat) == len(set(flat))
    return pairs, diagonal


def exact_coordinate_defect(
    support: tuple[Exponent, ...],
    coefficients: tuple[int, ...],
    target: Exponent,
) -> int:
    square_coefficient = 0
    for left, left_exponent in enumerate(support):
        for right, right_exponent in enumerate(support):
            if add_exponents(left_exponent, right_exponent) == target:
                square_coefficient += coefficients[left] * coefficients[right]

    phi_coefficient = sum(
        coefficients[index]
        for index, exponent in enumerate(support)
        if tuple(2 * value for value in exponent) == target
    )
    numerator = square_coefficient - phi_coefficient
    assert numerator % 2 == 0
    return (numerator // 2) % 2


def matching_coordinate_defect(
    coefficients: tuple[int, ...],
    pairs: list[tuple[int, int]],
    diagonal: int | None,
) -> int:
    answer = 0 if diagonal is None else (coefficients[diagonal] // 2) % 2
    for left, right in pairs:
        answer ^= (coefficients[left] % 2) * (coefficients[right] % 2)
    return answer


def check_coordinate_counts() -> int:
    cases = (
        (
            tuple((index,) for index in range(5)),
            tuple((target,) for target in range(9)),
        ),
        (
            ((0, 0), (1, 0), (0, 1), (1, 1)),
            tuple((left, right) for left in range(3) for right in range(3)),
        ),
    )
    checks = 0
    for support, targets in cases:
        total = 4 ** len(support)
        for target in targets:
            pairs, diagonal = matching_data(support, target)
            zero_count = 0
            for coefficients in itertools.product(range(4), repeat=len(support)):
                direct = exact_coordinate_defect(
                    support, coefficients, target
                )
                matching = matching_coordinate_defect(
                    coefficients, pairs, diagonal
                )
                assert direct == matching
                zero_count += direct == 0
                checks += 1

            if diagonal is not None:
                expected = total // 2
            else:
                expected = total // 2 + total // (2 ** (len(pairs) + 1))
            assert zero_count == expected
            checks += 1

    print(f"coordinate-array checks: {checks}")
    return checks


def canonical_value(bits: tuple[int, ...], edges: int, diagonal: int) -> int:
    answer = 0
    for edge in range(edges):
        answer ^= bits[2 * edge] * bits[2 * edge + 1]
    if diagonal:
        answer ^= bits[-1]
    return answer


def character(bits: tuple[int, ...], subset: int) -> int:
    parity = 0
    for index, bit in enumerate(bits):
        if subset & (1 << index):
            parity ^= bit
    return -1 if parity else 1


def walsh_coefficients(edges: int, diagonal: int) -> list[Fraction]:
    dimension = 2 * edges + diagonal
    points = list(itertools.product((0, 1), repeat=dimension))
    return [
        Fraction(
            sum(
                (-1) ** canonical_value(point, edges, diagonal)
                * character(point, subset)
                for point in points
            ),
            2**dimension,
        )
        for subset in range(2**dimension)
    ]


def check_walsh_and_influences() -> int:
    checks = 0
    for edges in range(5):
        for diagonal in (0, 1):
            dimension = 2 * edges + diagonal
            coefficients = walsh_coefficients(edges, diagonal)
            nonzero = [value for value in coefficients if value]
            assert len(nonzero) == 4**edges
            assert all(abs(value) == Fraction(1, 2**edges) for value in nonzero)
            expected_bias = Fraction(0) if diagonal else Fraction(1, 2**edges)
            assert coefficients[0] == expected_bias
            checks += len(coefficients) + 3

            points = list(itertools.product((0, 1), repeat=dimension))
            influences: list[Fraction] = []
            for variable in range(dimension):
                changes = 0
                for point in points:
                    flipped = list(point)
                    flipped[variable] ^= 1
                    changes += canonical_value(
                        point, edges, diagonal
                    ) != canonical_value(tuple(flipped), edges, diagonal)
                influences.append(Fraction(changes, len(points)))
            assert influences[: 2 * edges] == [Fraction(1, 2)] * (2 * edges)
            if diagonal:
                assert influences[-1] == 1
            assert sum(influences) == edges + diagonal
            checks += dimension + 2

            actual_noise = [Fraction(0)] * (dimension + 1)
            for subset, coefficient in enumerate(coefficients):
                actual_noise[subset.bit_count()] += coefficient**2

            expected_noise = [Fraction(0)] * (dimension + 1)
            denominator = 4**edges
            for degree in range(2 * edges + 1):
                expected_noise[degree + diagonal] = Fraction(
                    comb(2 * edges, degree), denominator
                )
            assert actual_noise == expected_noise
            checks += dimension + 1

    print(f"Walsh, influence, and noise checks: {checks}")
    return checks


def face_bias(
    status: tuple[int, ...], edges: int, diagonal: int
) -> Fraction:
    free = [index for index, value in enumerate(status) if value == -1]
    signed_sum = 0
    for free_bits in itertools.product((0, 1), repeat=len(free)):
        point = list(status)
        for index, bit in zip(free, free_bits, strict=True):
            point[index] = bit
        signed_sum += (-1) ** canonical_value(tuple(point), edges, diagonal)
    return Fraction(signed_sum, 2 ** len(free))


def predicted_face_bias_magnitude(
    status: tuple[int, ...], edges: int, diagonal: int
) -> Fraction:
    intact = 0
    linear = 0
    for edge in range(edges):
        left = status[2 * edge]
        right = status[2 * edge + 1]
        if left == -1 and right == -1:
            intact += 1
        elif left == -1 and right == 1:
            linear += 1
        elif left == 1 and right == -1:
            linear += 1
    if diagonal and status[-1] == -1:
        linear += 1
    return Fraction(0) if linear else Fraction(1, 2**intact)


def check_affine_faces() -> int:
    checks = 0
    for edges in range(4):
        for diagonal in (0, 1):
            dimension = 2 * edges + diagonal
            for status in itertools.product((-1, 0, 1), repeat=dimension):
                actual = abs(face_bias(status, edges, diagonal))
                expected = predicted_face_bias_magnitude(
                    status, edges, diagonal
                )
                assert actual == expected
                checks += 1
    print(f"affine-face checks: {checks}")
    return checks


def main() -> None:
    coordinate = check_coordinate_counts()
    walsh = check_walsh_and_influences()
    faces = check_affine_faces()
    print(f"total exact checks: {coordinate + walsh + faces}")


if __name__ == "__main__":
    main()
