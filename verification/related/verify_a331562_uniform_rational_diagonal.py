"""Exact checks for the uniform rational diagonal of OEIS A331562."""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
from math import comb


Exponent = tuple[int, ...]
Polynomial = dict[Exponent, int]


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, 0) + coefficient
        if out[exponent] == 0:
            del out[exponent]
    return out


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        return {}
    dimension = len(next(iter(left)))
    out: Polynomial = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(left_exp[i] + right_exp[i] for i in range(dimension))
            out[exponent] = out.get(exponent, 0) + left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def poly_scale(poly: Polynomial, scalar: int) -> Polynomial:
    return {exponent: scalar * coefficient for exponent, coefficient in poly.items() if scalar * coefficient}


def constant(dimension: int, value: int) -> Polynomial:
    return {(0,) * dimension: value} if value else {}


def variable(dimension: int, index: int, coefficient: int = 1) -> Polynomial:
    exponent = [0] * dimension
    exponent[index] = 1
    return {tuple(exponent): coefficient}


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))
    return -1 if inversions % 2 else 1


def determinant(matrix: tuple[tuple[Polynomial, ...], ...]) -> Polynomial:
    dimension = len(matrix)
    out: Polynomial = {}
    for perm in permutations(range(dimension)):
        term = constant(dimension, permutation_sign(perm))
        for row, column in enumerate(perm):
            term = poly_mul(term, matrix[row][column])
        out = poly_add(out, term)
    return out


def adjacency(dimension: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(int(abs(row - column) <= 1) for column in range(dimension))
        for row in range(dimension)
    )


def determinant_polynomial(dimension: int, numerator: bool) -> Polynomial:
    adj = adjacency(dimension)
    rows = []
    for row in range(dimension):
        entries = []
        for column in range(dimension):
            entry = constant(dimension, int(row == column))
            matrix_value = adj[row][column] - (1 if numerator else 0)
            entry = poly_add(entry, variable(dimension, column, -matrix_value))
            entries.append(entry)
        rows.append(tuple(entries))
    return determinant(tuple(rows))


def continuant(dimension: int) -> Polynomial:
    if dimension == 0:
        return {(): 1}
    d0 = constant(dimension, 1)
    d1 = poly_add(d0, variable(dimension, 0, -1))
    if dimension == 1:
        return d1
    previous_previous, previous = d0, d1
    for index in range(1, dimension):
        first = poly_mul(poly_add(d0, variable(dimension, index, -1)), previous)
        cross = poly_mul(variable(dimension, index - 1), variable(dimension, index))
        current = poly_add(first, poly_scale(poly_mul(cross, previous_previous), -1))
        previous_previous, previous = previous, current
    return previous


def bounded_language_series(dimension: int, cap: int) -> Polynomial:
    """All admissible words whose individual letter counts are at most cap."""
    zero = (0,) * dimension
    by_last: dict[tuple[Exponent, int], int] = {}
    for last in range(dimension):
        exponent = list(zero)
        exponent[last] = 1
        by_last[(tuple(exponent), last)] = 1

    total: Polynomial = {zero: 1}
    frontier = by_last
    while frontier:
        next_frontier: dict[tuple[Exponent, int], int] = {}
        for (exponent, last), count in frontier.items():
            total[exponent] = total.get(exponent, 0) + count
            for new_last in range(max(0, last - 1), min(dimension, last + 2)):
                if exponent[new_last] == cap:
                    continue
                new_exponent = list(exponent)
                new_exponent[new_last] += 1
                key = (tuple(new_exponent), new_last)
                next_frontier[key] = next_frontier.get(key, 0) + count
        frontier = next_frontier
    return total


def truncated_product(left: Polynomial, right: Polynomial, cap: int) -> Polynomial:
    if not left or not right:
        return {}
    dimension = len(next(iter(left)))
    out: Polynomial = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(left_exp[i] + right_exp[i] for i in range(dimension))
            if max(exponent, default=0) > cap:
                continue
            out[exponent] = out.get(exponent, 0) + left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


@lru_cache(maxsize=None)
def words_with_last(counts: Exponent, last: int) -> int:
    if counts[last] == 0:
        return 0
    if sum(counts) == 1:
        return 1
    smaller = list(counts)
    smaller[last] -= 1
    return sum(
        words_with_last(tuple(smaller), previous)
        for previous in range(max(0, last - 1), min(len(counts), last + 2))
    )


def row_value(dimension: int, copies: int) -> int:
    if copies == 0:
        return 1
    counts = (copies,) * dimension
    return sum(words_with_last(counts, last) for last in range(dimension))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    out = 0
    while value % prime == 0:
        out += 1
        value //= prime
    return out


def check_determinants() -> int:
    checks = 0
    for dimension in range(1, 7):
        assert determinant_polynomial(dimension, numerator=False) == continuant(dimension)
        checks += 1
    return checks


def check_rational_identity() -> int:
    checks = 0
    for dimension, cap in ((1, 4), (2, 3), (3, 2), (4, 2)):
        denominator = determinant_polynomial(dimension, numerator=False)
        numerator = determinant_polynomial(dimension, numerator=True)
        series = bounded_language_series(dimension, cap)
        product_series = truncated_product(denominator, series, cap)
        for exponent in product(range(cap + 1), repeat=dimension):
            assert product_series.get(exponent, 0) == numerator.get(exponent, 0)
            checks += 1
    return checks


def check_rows() -> int:
    expected = {
        2: [1, 2, 6, 20, 70, 252],
        3: [1, 2, 12, 92, 780, 7002],
        4: [1, 2, 26, 506, 11482, 284002],
        5: [1, 2, 48, 2288, 135040, 8956752],
        6: [1, 2, 86, 10010, 1543862, 276285002],
    }
    checks = 0
    for dimension, values in expected.items():
        for copies, value in enumerate(values):
            assert row_value(dimension, copies) == value
            checks += 1
    for copies in range(8):
        assert row_value(2, copies) == comb(2 * copies, copies)
        checks += 1
    return checks


def check_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    cases = ((5, 5), (5, 7), (6, 5), (6, 7), (7, 5))
    for dimension, prime in cases:
        difference = row_value(dimension, prime) - row_value(dimension, 1)
        depth = valuation(difference, prime)
        assert depth >= 3
        sharp += int(depth == 3)
        checks += 1
    return checks, sharp


def main() -> None:
    determinant_checks = check_determinants()
    rational_checks = check_rational_identity()
    row_checks = check_rows()
    tower_checks, sharp = check_towers()
    print(f"A331562 determinant checks: {determinant_checks}")
    print(f"A331562 rational-identity checks: {rational_checks}")
    print(f"A331562 row checks: {row_checks}")
    print(f"A331562 prime-level tower checks: {tower_checks} ({sharp} sharp)")
    print("A331562 uniform rational-diagonal checks passed")


if __name__ == "__main__":
    main()
