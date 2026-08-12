"""Exact checks for A263843ReversionCoefficientReduction.md."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


PUBLISHED_DERIVED = (
    1,
    4,
    62,
    1084,
    19982,
    379504,
    7347410,
    144168392,
    2856907662,
    57044977168,
    1145905776312,
    23131265652092,
)


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


@lru_cache(maxsize=None)
def framed(d: int, c: int, n: int) -> int:
    target = c * n
    return sum(
        generalized_binomial(3 * d * n, j)
        * (-1) ** (target - j)
        * generalized_binomial(-d * n, target - j)
        for j in range(target + 1)
    )


@lru_cache(maxsize=None)
def reversion_coefficient(c: int, s: int, n: int) -> int:
    if n == 0:
        return 1
    if s == 0:
        return 0
    d = c + s
    if d == 0:
        return -1 - 3 * (-1) ** (c * n - 1)
    answer = Fraction(s, d) * framed(d, c, n)
    assert answer.denominator == 1
    return answer.numerator


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def factorial_vp(n: int, prime: int) -> int:
    answer = 0
    while n:
        n //= prime
        answer += n
    return answer


def check_published_values() -> int:
    observed = tuple(reversion_coefficient(1, 1, n) for n in range(12))
    assert observed == PUBLISHED_DERIVED
    return len(observed)


def check_lagrange_and_integrality() -> int:
    checks = 0
    for c in range(1, 6):
        for s in range(-9, 10):
            for n in range(1, 16):
                value = reversion_coefficient(c, s, n)
                assert isinstance(value, int)
                if s == 0:
                    assert value == 0
                if c + s == 0:
                    assert value == -1 - 3 * (-1) ** (c * n - 1)
                checks += 1
    return checks


def check_refined_budget() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for level in range(1, 5):
            for e in range(4):
                assert 3 * level + 2 * e >= 3 * level + e
                for degree in range(3, 121):
                    assert (
                        degree * level
                        - factorial_vp(degree, prime)
                        + degree * e
                        >= 3 * level + e
                    )
                    checks += 1
    return checks


def check_odd_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    parameters = (
        (1, 1),
        (1, -1),
        (1, 4),       # 5 divides c+s
        (2, 3),       # 5 divides c+s
        (2, -7),      # 5 divides c+s
        (3, -1),
        (4, 7),       # 11 divides c+s
        (5, -2),
    )
    for c, s in parameters:
        for prime in (5, 7, 11):
            for n in (1, 2):
                for level in (1, 2):
                    high = reversion_coefficient(c, s, n * prime**level)
                    low = reversion_coefficient(c, s, n * prime ** (level - 1))
                    valuation = vp(high - low, prime)
                    assert valuation >= 3 * level
                    sharp += valuation == 3 * level
                    checks += 1
    assert sharp > 0
    return checks, sharp


def check_ternary_boundary() -> tuple[int, int]:
    proved = 0
    surviving = 0
    for c, s in ((1, 2), (1, -1), (2, 1), (2, -2), (4, 2), (5, -2)):
        assert (c + s) % 3 == 0
        for n in (1, 2, 4):
            for level in (1, 2):
                high = reversion_coefficient(c, s, n * 3**level)
                low = reversion_coefficient(c, s, n * 3 ** (level - 1))
                assert vp(high - low, 3) >= 3 * level
                proved += 1

    # Evidence only for the boundary not closed by the written proof.
    for c, s in ((1, 1), (1, 3), (2, -1), (3, 1), (4, -2)):
        assert (c + s) % 3 != 0
        for n in (1, 2, 4):
            for level in (1, 2):
                high = reversion_coefficient(c, s, n * 3**level)
                low = reversion_coefficient(c, s, n * 3 ** (level - 1))
                assert vp(high - low, 3) >= 3 * level
                surviving += 1
    return proved, surviving


def main() -> None:
    published = check_published_values()
    lagrange = check_lagrange_and_integrality()
    budget = check_refined_budget()
    towers, sharp = check_odd_towers()
    ternary_proved, ternary_open = check_ternary_boundary()
    total = published + lagrange + budget + towers + ternary_proved + ternary_open
    print(f"published derived-sequence checks: {published}")
    print(f"Lagrange/integrality checks: {lagrange}")
    print(f"refined valuation-budget checks: {budget}")
    print(f"p >= 5 tower checks: {towers} ({sharp} sharp)")
    print(f"proved ternary-subfamily checks: {ternary_proved}")
    print(f"surviving ternary-boundary evidence checks: {ternary_open}")
    print(f"all {total} A263843 reduction checks passed")


if __name__ == "__main__":
    main()
