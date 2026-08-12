"""Exact checks for TaylorTruncationCoefficientReduction.md."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


CATALAN_NAMED = {
    1: (1, 2, 8, 41, 232, 1377, 8399, 52138),
    3: (1, 4, 34, 337, 3554, 38754, 431521, 4874377),
    4: (1, 5, 53, 647, 8373, 111880, 1525511, 21093476),
    5: (1, 6, 76, 1101, 16876, 266881, 4305247, 70414133),
}

SCHRODER_NAMED = {
    1: (1, 3, 21, 183, 1729, 17003, 171237, 1752047),
    2: (1, 5, 57, 761, 10817, 159005, 2386857, 36348401),
    3: (1, 7, 109, 1951, 36993, 724007, 14457421, 292732671),
}


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


def vp_integer(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def vp_fraction(value: Fraction, prime: int) -> int:
    return vp_integer(value.numerator, prime) - vp_integer(value.denominator, prime)


def catalan_prefactor(index: int) -> int:
    if index == 0:
        return 1
    return 2 if index % 3 == 0 else -1


@lru_cache(maxsize=None)
def schroder_prefactor(index: int) -> int:
    if index == 0:
        return 1
    if index == 1:
        return -2
    forcing = -2 if index == 2 else 0
    return (
        forcing
        - 2 * schroder_prefactor(index - 1)
        - 2 * schroder_prefactor(index - 2)
    )


@lru_cache(maxsize=None)
def catalan_reduced(power: int, n: int) -> int:
    if n == 0:
        return 1
    exponent = (power + 2) * n
    return sum(
        catalan_prefactor(n - j) * generalized_binomial(exponent, j)
        for j in range(n + 1)
    )


@lru_cache(maxsize=None)
def schroder_reduced(power: int, n: int) -> int:
    if n == 0:
        return 1
    exponent = (power + 1) * n
    total = 0
    for degree in range(n + 1):
        kernel = sum(
            generalized_binomial(exponent, left)
            * 2**left
            * generalized_binomial(n, degree - left)
            for left in range(degree + 1)
        )
        total += schroder_prefactor(n - degree) * kernel
    return total


def catalan_power_coefficient(exponent: int, degree: int) -> int:
    if degree == 0:
        return 1
    return generalized_binomial(exponent + 2 * degree, degree) - 2 * generalized_binomial(
        exponent + 2 * degree - 1, degree - 1
    )


def schroder_power_coefficient(exponent: int, degree: int) -> int:
    if degree == 0:
        return 1
    numerator = sum(
        generalized_binomial(exponent + degree - 1, j)
        * generalized_binomial(degree, degree - 1 - j)
        * 2 ** (j + 1)
        for j in range(degree)
    )
    answer = Fraction(exponent, degree) * numerator
    assert answer.denominator == 1
    return answer.numerator


def catalan_original(power: int, n: int) -> int:
    return sum(catalan_power_coefficient(power * n, k) for k in range(n + 1))


def schroder_original(power: int, n: int) -> int:
    return sum(schroder_power_coefficient(power * n, k) for k in range(n + 1))


def check_source_and_reduction() -> int:
    checks = 0
    for power, expected in CATALAN_NAMED.items():
        observed = tuple(catalan_reduced(power, n) for n in range(len(expected)))
        assert observed == expected
        checks += len(expected)
    for power, expected in SCHRODER_NAMED.items():
        observed = tuple(schroder_reduced(power, n) for n in range(len(expected)))
        assert observed == expected
        checks += len(expected)
    for power in range(-5, 8):
        for n in range(1, 13):
            assert catalan_reduced(power, n) == catalan_original(power, n)
            assert schroder_reduced(power, n) == schroder_original(power, n)
            checks += 2
    return checks


def check_prefactors() -> int:
    checks = 0
    for index in range(1, 100):
        assert catalan_prefactor(index) == (2 if index % 3 == 0 else -1)
        if index >= 3:
            assert schroder_prefactor(index) == (
                -2 * schroder_prefactor(index - 1)
                - 2 * schroder_prefactor(index - 2)
            )
        checks += 2
    for prime in (5, 7, 11, 13, 17, 19):
        for index in range(100):
            assert catalan_prefactor(prime * index) == catalan_prefactor(index)
            checks += 1
    return checks


def check_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for family in (catalan_reduced, schroder_reduced):
        for power in range(-4, 8):
            for prime in (5, 7, 11, 13):
                for n in (1, 2, 3):
                    for level in (1, 2):
                        high = family(power, n * prime**level)
                        low = family(power, n * prime ** (level - 1))
                        valuation = vp_integer(high - low, prime)
                        assert valuation >= 3 * level
                        sharp += valuation == 3 * level
                        checks += 1
    assert sharp > 0
    return checks, sharp


@lru_cache(maxsize=None)
def cartier_qv(prime: int, index: int) -> Fraction:
    target = prime * index
    return sum(
        (
            Fraction(
                catalan_prefactor(target - j) * (-1) ** (j + 1),
                j,
            )
            for j in range(1, target + 1)
            if j % prime
        ),
        Fraction(),
    )


@lru_cache(maxsize=None)
def full_q_log(index: int) -> Fraction:
    """Coefficient [y^index] Q_C(y) log(1+y)."""
    return sum(
        (
            Fraction(
                catalan_prefactor(index - j) * (-1) ** (j + 1),
                j,
            )
            for j in range(1, index + 1)
        ),
        Fraction(),
    )


def framed_bps(index: int) -> Fraction:
    """The rational coefficient b_index from equation (19)."""
    return index * full_q_log(index)


@lru_cache(maxsize=None)
def reduced_v_square(prime: int, index: int) -> Fraction:
    return sum(
        (
            Fraction((-1) ** (j + 1), j)
            * Fraction((-1) ** (index - j + 1), index - j)
            for j in range(1, index)
            if j % prime and (index - j) % prime
        ),
        Fraction(),
    )


@lru_cache(maxsize=None)
def cartier_qv_square(prime: int, index: int) -> Fraction:
    target = prime * index
    return sum(
        (
            catalan_prefactor(target - degree)
            * reduced_v_square(prime, degree)
            for degree in range(2, target + 1)
        ),
        Fraction(),
    )


def constant_term_obligation(prime: int, slope: int, m: int, degree: int) -> Fraction:
    coefficient = cartier_qv if degree == 1 else cartier_qv_square
    return sum(
        (
            generalized_binomial(slope * m, m - index)
            * coefficient(prime, index)
            for index in range(1, m + 1)
        ),
        Fraction(),
    )


def check_cartier_obligations() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for exponent in (0, 1):
            for unit in (1, 2, 3):
                if unit % prime == 0:
                    continue
                m = unit * prime**exponent
                for slope in range(-4, 9):
                    linear = constant_term_obligation(prime, slope, m, 1)
                    quadratic = constant_term_obligation(prime, slope, m, 2)
                    assert vp_fraction(linear, prime) >= 2 * (exponent + 1)
                    assert vp_fraction(quadratic, prime) >= exponent + 1
                    checks += 2
    return checks


def check_linear_gauss_reformulation() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19):
        for index in range(1, 81):
            coefficient = cartier_qv(prime, index)
            assert coefficient == (
                full_q_log(prime * index) - full_q_log(index) / prime
            )
            assert coefficient == (
                framed_bps(prime * index) - framed_bps(index)
            ) / (prime * index)
            exponent = vp_integer(index, prime) + 1
            assert vp_fraction(
                framed_bps(prime * index) - framed_bps(index), prime
            ) >= 3 * exponent
            checks += 3
    return checks


def main() -> None:
    source = check_source_and_reduction()
    prefactors = check_prefactors()
    towers, sharp = check_towers()
    cartier = check_cartier_obligations()
    gauss = check_linear_gauss_reformulation()
    total = source + prefactors + towers + cartier + gauss
    print(f"source/reduction checks: {source}")
    print(f"prefactor/Cartier-fixed checks: {prefactors}")
    print(f"cubic-tower evidence checks: {towers} ({sharp} sharp)")
    print(f"remaining-Cartier-obligation checks: {cartier}")
    print(f"linear cubic-Gauss reformulation checks: {gauss}")
    print(f"all {total} Taylor-truncation checks passed")


if __name__ == "__main__":
    main()
