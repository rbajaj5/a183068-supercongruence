"""Exact checks for FiniteFieldDeterminantBiasSupercongruence.md."""

from itertools import product
from math import prod


def det_mod(matrix: tuple[int, ...], n: int, p: int) -> int:
    rows = [list(matrix[i * n : (i + 1) * n]) for i in range(n)]
    determinant = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if rows[row][col] % p), None)
        if pivot is None:
            return 0
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            determinant = -determinant
        pivot_value = rows[col][col] % p
        determinant = determinant * pivot_value % p
        pivot_inverse = pow(pivot_value, -1, p)
        for row in range(col + 1, n):
            scale = rows[row][col] * pivot_inverse % p
            for j in range(col, n):
                rows[row][j] = (rows[row][j] - scale * rows[col][j]) % p
    return determinant % p


def exponent(n: int) -> int:
    return (n * n - n + 2) // 2


def character_sum_formula(n: int, q: int) -> int:
    e = exponent(n)
    return q ** (n * n) - q**e * prod(q**k - 1 for k in range(2, n + 1))


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def brute_prime_field(n: int, p: int) -> None:
    counts = [0] * p
    for entries in product(range(p), repeat=n * n):
        counts[det_mod(entries, n, p)] += 1
    assert len(set(counts[1:])) == 1
    exact_character_sum = counts[0] - counts[1]
    assert exact_character_sum == character_sum_formula(n, p)


def main() -> None:
    brute_cases = [(2, 2), (2, 3), (2, 5), (2, 7), (3, 2), (3, 3)]
    for n, p in brute_cases:
        brute_prime_field(n, p)

    formula_cases = 0
    valuation_cases = 0
    for n in range(2, 11):
        e = exponent(n)
        for p in (2, 3, 5, 7, 11):
            for r in range(1, 6):
                q = p**r
                count_formula = q**n * (
                    q ** (n * (n - 1))
                    - prod(q**n - q**j for j in range(n - 1))
                )
                assert count_formula == character_sum_formula(n, q)
                formula_cases += 1
                if r >= 2:
                    difference = character_sum_formula(n, p**r) - (
                        character_sum_formula(n, p ** (r - 1))
                    )
                    assert valuation(difference, p) == e * (r - 1)
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
