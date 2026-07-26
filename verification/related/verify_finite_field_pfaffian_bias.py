"""Exact checks for FiniteFieldPfaffianBiasSupercongruence.md."""

from itertools import product
from math import prod


def pfaffian_mod(matrix: list[list[int]], p: int) -> int:
    size = len(matrix)
    if size == 0:
        return 1
    answer = 0
    for j in range(1, size):
        minor = [
            [matrix[row][col] for col in range(size) if col not in (0, j)]
            for row in range(size)
            if row not in (0, j)
        ]
        sign = 1 if j % 2 == 1 else -1
        answer += sign * matrix[0][j] * pfaffian_mod(minor, p)
    return answer % p


def alternating_matrix(values: tuple[int, ...], size: int, p: int) -> list[list[int]]:
    matrix = [[0] * size for _ in range(size)]
    index = 0
    for row in range(size):
        for col in range(row + 1, size):
            matrix[row][col] = values[index]
            matrix[col][row] = -values[index] % p
            index += 1
    return matrix


def exponent(m: int) -> int:
    return m * m - m + 1


def character_sum_formula(m: int, q: int) -> int:
    dimension = m * (2 * m - 1)
    return q**dimension - q ** exponent(m) * prod(
        q ** (2 * j - 1) - 1 for j in range(2, m + 1)
    )


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def brute_prime_field(m: int, p: int) -> None:
    size = 2 * m
    variables = size * (size - 1) // 2
    counts = [0] * p
    for values in product(range(p), repeat=variables):
        pfaffian = pfaffian_mod(alternating_matrix(values, size, p), p)
        counts[pfaffian] += 1
    assert len(set(counts[1:])) == 1
    exact_character_sum = counts[0] - counts[1]
    assert exact_character_sum == character_sum_formula(m, p)


def main() -> None:
    brute_cases = [(2, 2), (2, 3), (2, 5), (2, 7), (3, 2)]
    for m, p in brute_cases:
        brute_prime_field(m, p)

    formula_cases = 0
    valuation_cases = 0
    for m in range(2, 9):
        f = exponent(m)
        for p in (2, 3, 5, 7, 11):
            for r in range(1, 6):
                q = p**r
                odd_size = 2 * m - 1
                total_odd_alternating = q ** (odd_size * (odd_size - 1) // 2)
                maximal_rank = (
                    q ** ((m - 1) * (m - 2))
                    * (q ** (2 * m - 1) - 1)
                    * prod(q ** (2 * j - 1) - 1 for j in range(2, m))
                )
                conditioning_formula = q ** (2 * m - 1) * (
                    total_odd_alternating - maximal_rank
                )
                assert conditioning_formula == character_sum_formula(m, q)
                formula_cases += 1
                if r >= 2:
                    difference = character_sum_formula(m, p**r) - (
                        character_sum_formula(m, p ** (r - 1))
                    )
                    assert valuation(difference, p) == f * (r - 1)
                    valuation_cases += 1

    print(
        "PASS:",
        len(brute_cases),
        "brute-force field cases;",
        formula_cases,
        "polynomial cases;",
        valuation_cases,
        "exact valuation cases.",
    )


if __name__ == "__main__":
    main()
