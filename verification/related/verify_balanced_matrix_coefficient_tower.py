"""Exact checks for the balanced-matrix coefficient theorem and A124435."""

from __future__ import annotations

from functools import lru_cache
from math import comb, factorial


Pair = tuple[int, int]  # a + b*tau, tau^2 = tau - 1


def pair_add(left: Pair, right: Pair) -> Pair:
    return left[0] + right[0], left[1] + right[1]


def pair_mul(left: Pair, right: Pair) -> Pair:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c + b * d


def pair_pow(base: Pair, exponent: int) -> Pair:
    out: Pair = (1, 0)
    while exponent:
        if exponent & 1:
            out = pair_mul(out, base)
        exponent >>= 1
        if exponent:
            base = pair_mul(base, base)
    return out


def multinomial(parts: tuple[int, ...]) -> int:
    total = sum(parts)
    out = factorial(total)
    for part in parts:
        out //= factorial(part)
    return out


@lru_cache(maxsize=None)
def a124435(n: int) -> int:
    return sum(
        (-1) ** (n - k)
        * comb(n, k)
        * comb(n + 2 * k, n)
        * comb(2 * k, k)
        for k in range(n + 1)
    )


def diagonal_sum(n: int) -> int:
    return sum(
        (-1) ** j * factorial(3 * n - 2 * j)
        // (factorial(j) * factorial(n - j) ** 3)
        for j in range(n + 1)
    )


def balanced_2(matrix: tuple[tuple[int, int], tuple[int, int]], n: int) -> int:
    out = 0
    for k in range(n + 1):
        out += (
            comb(n, k) ** 2
            * matrix[0][0] ** k
            * matrix[0][1] ** (n - k)
            * matrix[1][0] ** (n - k)
            * matrix[1][1] ** k
        )
    return out


def balanced_3_int(matrix: tuple[tuple[int, ...], ...], n: int) -> int:
    out = 0
    for b11 in range(n + 1):
        for b12 in range(n - b11 + 1):
            b13 = n - b11 - b12
            for b21 in range(n + 1):
                for b22 in range(n - b21 + 1):
                    b23 = n - b21 - b22
                    b31 = n - b11 - b21
                    b32 = n - b12 - b22
                    b33 = b11 + b12 + b21 + b22 - n
                    if min(b31, b32, b33) < 0:
                        continue
                    rows = (
                        (b11, b12, b13),
                        (b21, b22, b23),
                        (b31, b32, b33),
                    )
                    coefficient = 1
                    weight = 1
                    for i, row in enumerate(rows):
                        coefficient *= multinomial(row)
                        for j, exponent in enumerate(row):
                            weight *= matrix[i][j] ** exponent
                    out += coefficient * weight
    return out


def balanced_3_pair(matrix: tuple[tuple[Pair, ...], ...], n: int) -> Pair:
    out: Pair = (0, 0)
    for b11 in range(n + 1):
        for b12 in range(n - b11 + 1):
            b13 = n - b11 - b12
            for b21 in range(n + 1):
                for b22 in range(n - b21 + 1):
                    b23 = n - b21 - b22
                    b31 = n - b11 - b21
                    b32 = n - b12 - b22
                    b33 = b11 + b12 + b21 + b22 - n
                    if min(b31, b32, b33) < 0:
                        continue
                    rows = (
                        (b11, b12, b13),
                        (b21, b22, b23),
                        (b31, b32, b33),
                    )
                    coefficient = 1
                    weight: Pair = (1, 0)
                    for i, row in enumerate(rows):
                        coefficient *= multinomial(row)
                        for j, exponent in enumerate(row):
                            weight = pair_mul(weight, pair_pow(matrix[i][j], exponent))
                    out = pair_add(out, (coefficient * weight[0], coefficient * weight[1]))
    return out


def entrywise_power(matrix: tuple[tuple[int, ...], ...], p: int):
    return tuple(tuple(value**p for value in row) for row in matrix)


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def check_identities() -> int:
    expected = (1, 5, 67, 1109, 20251, 391355, 7847155)
    tau: Pair = (0, 1)
    tau_inverse: Pair = (1, -1)
    one: Pair = (1, 0)
    matrix = (
        (one, one, one),
        (one, one, tau),
        (one, tau_inverse, one),
    )
    checks = 0
    for n, value in enumerate(expected):
        assert a124435(n) == value
        assert diagonal_sum(n) == value
        assert balanced_3_pair(matrix, n) == (value, 0)
        checks += 3
    return checks


def check_generic_twists() -> int:
    checks = 0
    matrices_2 = (
        ((1, 2), (3, 4)),
        ((-1, 1), (2, 0)),
        ((2, -2), (1, 3)),
    )
    for matrix in matrices_2:
        for prime in (5, 7):
            for n in (1, 2, 3):
                for r in (1, 2):
                    current = balanced_2(matrix, n * prime**r)
                    previous = balanced_2(
                        entrywise_power(matrix, prime), n * prime ** (r - 1)
                    )
                    assert (current - previous) % prime ** (2 * r) == 0
                    checks += 1

    matrices_3 = (
        ((1, 0, 1), (2, -1, 1), (0, 1, 2)),
        ((1, 1, -1), (0, 2, 1), (2, 0, 1)),
    )
    for matrix in matrices_3:
        for prime in (5, 7):
            current = balanced_3_int(matrix, prime)
            previous = balanced_3_int(entrywise_power(matrix, prime), 1)
            assert (current - previous) % prime**2 == 0
            checks += 1
    return checks


def check_a124435_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for prime in (5, 7, 11, 13):
        for n in range(1, 5):
            for r in (1, 2):
                delta = a124435(n * prime**r) - a124435(
                    n * prime ** (r - 1)
                )
                valuation = vp(delta, prime)
                assert valuation >= 2 * r
                if valuation == 2 * r:
                    sharp += 1
                checks += 1
    assert vp(a124435(3) - a124435(1), 3) == 1
    return checks + 1, sharp


def main() -> None:
    identity_checks = check_identities()
    generic_checks = check_generic_twists()
    tower_checks, sharp = check_a124435_towers()
    print("Balanced-matrix coefficient theorem passed")
    print(f"A124435 identity checks: {identity_checks}")
    print(f"generic twisted-tower checks: {generic_checks}")
    print(f"A124435 tower and boundary checks: {tower_checks}")
    print(f"sharp A124435 instances: {sharp}")


if __name__ == "__main__":
    main()
