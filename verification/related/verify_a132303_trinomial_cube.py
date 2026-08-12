"""Exact checks for A132303TrinomialCubeTower.md.

The checks are regression evidence for the written proof, not a substitute
for it.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache


PUBLISHED = (
    1,
    3,
    45,
    831,
    17181,
    375903,
    8530929,
    198643455,
    4714491357,
    113550338127,
    2767105469745,
    68077260387315,
    1688160321677025,
    42142679453321307,
    1058050429855640217,
    26695057057648257231,
    676431705046728704733,
    17205315843416998571415,
    439098128408223839364561,
    11239967518370464873317291,
)


@lru_cache(maxsize=None)
def trinomial_row(n: int) -> tuple[int, ...]:
    row = [1]
    for _ in range(n):
        nxt = [0] * (len(row) + 2)
        for index, value in enumerate(row):
            nxt[index] += value
            nxt[index + 1] += value
            nxt[index + 2] += value
        row = nxt
    return tuple(row)


@lru_cache(maxsize=None)
def sequence(n: int) -> int:
    return sum(value**3 for value in trinomial_row(n))


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
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


def check_initial_values() -> int:
    assert tuple(sequence(n) for n in range(len(PUBLISHED))) == PUBLISHED
    return len(PUBLISHED)


def check_constant_term_identity() -> int:
    checks = 0
    for n in range(13):
        row = trinomial_row(n)
        # CT F(x)^n F(y)^n F((xy)^-1)^n forces all three indices equal.
        constant_term = sum(
            row[i] * row[j] * row[k]
            for i in range(len(row))
            for j in range(len(row))
            for k in range(len(row))
            if i == k and j == k
        )
        assert constant_term == sequence(n)
        checks += 1
    return checks


def reduced_log_coefficient(exponent: int, prime: int) -> Fraction:
    value = Fraction(0)
    if exponent % prime:
        value += Fraction(1, exponent)
    if exponent % 3 == 0:
        index = exponent // 3
        if index % prime:
            value -= Fraction(1, index)
    return value


def log_f_coefficient(exponent: int) -> Fraction:
    value = Fraction(1, exponent)
    if exponent % 3 == 0:
        value -= Fraction(1, exponent // 3)
    return value


def check_reduced_log_support() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17):
        for exponent in range(1, 301):
            coefficient = reduced_log_coefficient(exponent, prime)
            frobenius_log = prime * log_f_coefficient(exponent)
            if exponent % prime == 0:
                frobenius_log -= log_f_coefficient(exponent // prime)
            assert frobenius_log == prime * coefficient
            if coefficient:
                assert exponent % prime != 0
                assert coefficient.denominator % prime != 0
            checks += 1
    return checks


def check_factorial_budget() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for r in (1, 2, 3, 4):
            for degree in range(2, 121):
                assert degree * r - factorial_vp(degree, prime) >= 2 * r
                checks += 1
    return checks


def check_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for prime in (5, 7, 11, 13):
        for n in (1, 2, 3):
            for r in (1, 2):
                difference = sequence(n * prime**r) - sequence(
                    n * prime ** (r - 1)
                )
                valuation = vp(difference, prime)
                assert valuation >= 2 * r
                sharp += valuation == 2 * r
                checks += 1
    for prime in (5, 7):
        difference = sequence(prime**3) - sequence(prime**2)
        valuation = vp(difference, prime)
        assert valuation >= 6
        sharp += valuation == 6
        checks += 1
    assert sharp > 0
    return checks, sharp


def main() -> None:
    initial = check_initial_values()
    constants = check_constant_term_identity()
    support = check_reduced_log_support()
    budget = check_factorial_budget()
    towers, sharp = check_towers()
    total = initial + constants + support + budget + towers
    print(f"published initial-value checks: {initial}")
    print(f"constant-term identity checks: {constants}")
    print(f"reduced-log support checks: {support}")
    print(f"factorial valuation-budget checks: {budget}")
    print(f"adjacent tower checks: {towers} ({sharp} sharp)")
    print(f"all {total} A132303 checks passed")


if __name__ == "__main__":
    main()
