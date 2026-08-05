"""Exact checks for the Ehrhart-to-Newton determinant cutoff deduction.

These checks validate the centered-simplex sharpness example, the numerical
cutoff table, and the affine-matroid corollary. They do not prove the external
sharp Ehrhart-volume theorem.
"""

from fractions import Fraction
from itertools import combinations
from itertools import product
import random


def determinant(matrix: list[list[int]]) -> int:
    """Bareiss determinant over the integers."""
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign = -sign
        value = work[column][column]
        for row in range(column + 1, size):
            for entry in range(column + 1, size):
                work[row][entry] = (
                    work[row][entry] * value
                    - work[row][column] * work[column][entry]
                ) // previous
        previous = value
    return sign * work[-1][-1]


def centered_simplex_vertices(dimension: int) -> list[tuple[int, ...]]:
    base = (-1,) * dimension
    vertices = [base]
    for coordinate in range(dimension):
        vertex = list(base)
        vertex[coordinate] += dimension + 1
        vertices.append(tuple(vertex))
    return vertices


def in_centered_simplex(point: tuple[int, ...], *, interior: bool) -> bool:
    if interior:
        return all(value > -1 for value in point) and sum(point) < 1
    return all(value >= -1 for value in point) and sum(point) <= 1


def matrix_rank(matrix: list[list[int]], modulus: int | None = None) -> int:
    if not matrix:
        return 0
    if modulus is None:
        work = [[Fraction(value) for value in row] for row in matrix]
    else:
        work = [[value % modulus for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, rows) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if modulus is None:
            inverse = 1 / work[rank][column]
        else:
            inverse = pow(int(work[rank][column]), -1, modulus)
        work[rank] = [value * inverse for value in work[rank]]
        if modulus is not None:
            work[rank] = [int(value) % modulus for value in work[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                left - factor * right
                for left, right in zip(work[row], work[rank], strict=True)
            ]
            if modulus is not None:
                work[row] = [int(value) % modulus for value in work[row]]
        rank += 1
        if rank == rows:
            break
    return rank


def affine_rank(points: tuple[tuple[int, ...], ...], modulus: int | None = None) -> int:
    if len(points) <= 1:
        return 0
    base = points[0]
    differences = [
        [point[coordinate] - base[coordinate] for coordinate in range(len(base))]
        for point in points[1:]
    ]
    return matrix_rank(differences, modulus)


def next_prime(value: int) -> int:
    candidate = value + 1
    while True:
        if candidate >= 2 and all(
            candidate % divisor
            for divisor in range(2, int(candidate**0.5) + 1)
        ):
            return candidate
        candidate += 1


def check_affine_matroids() -> int:
    rng = random.Random(20260805)
    checks = 0
    for dimension in range(1, 7):
        points = tuple(
            point
            for point in product(range(-1, dimension + 1), repeat=dimension)
            if in_centered_simplex(point, interior=False)
        )
        prime = next_prime((dimension + 1) ** dimension)
        subsets: list[tuple[tuple[int, ...], ...]] = []
        if dimension <= 3:
            for size in range(1, dimension + 2):
                subsets.extend(combinations(points, size))
        else:
            for _ in range(5000):
                size = rng.randint(1, dimension + 1)
                subsets.append(tuple(rng.sample(points, size)))
        for subset in subsets:
            assert affine_rank(subset) == affine_rank(subset, prime)
            checks += 1
    return checks


def main() -> None:
    expected = {1: 2, 2: 9, 3: 64, 4: 625, 5: 7776, 6: 117649}
    checked_points = 0
    for dimension, cutoff in expected.items():
        vertices = centered_simplex_vertices(dimension)
        base = vertices[0]
        edge_matrix = [
            [vertices[column + 1][row] - base[row] for column in range(dimension)]
            for row in range(dimension)
        ]
        assert determinant(edge_matrix) == cutoff == (dimension + 1) ** dimension
        assert all(sum(vertex[i] for vertex in vertices) == 0 for i in range(dimension))

        interior = []
        for point in product(range(-1, dimension + 1), repeat=dimension):
            checked_points += 1
            if in_centered_simplex(point, interior=True):
                interior.append(point)
        assert interior == [(0,) * dimension]

    matroid_checks = check_affine_matroids()

    print(f"centered-simplex dimensions checked: {len(expected)}")
    print(f"integer points tested: {checked_points}")
    print(f"affine-matroid subsets checked: {matroid_checks}")
    print("sharp determinant and cutoff checks passed")


if __name__ == "__main__":
    main()
