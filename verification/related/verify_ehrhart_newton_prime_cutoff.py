"""Exact checks for the Ehrhart-to-Newton determinant cutoff deduction.

These checks validate the centered-simplex sharpness example and the numerical
cutoff table.  They do not prove the external sharp Ehrhart-volume theorem.
"""

from itertools import product


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

    print(f"centered-simplex dimensions checked: {len(expected)}")
    print(f"integer points tested: {checked_points}")
    print("sharp determinant and cutoff checks passed")


if __name__ == "__main__":
    main()
