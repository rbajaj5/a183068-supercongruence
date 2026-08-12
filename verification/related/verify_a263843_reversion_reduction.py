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


def fraction_mod_prime(value: Fraction, prime: int) -> int:
    """Reduce a p-integral rational number modulo p."""

    numerator = value.numerator
    denominator = value.denominator
    assert denominator % prime != 0, value
    return numerator * pow(denominator, -1, prime) % prime


def reduced_harmonic(total: int, alternating: bool = False) -> Fraction:
    answer = Fraction(0)
    for index in range(1, total):
        if index % 3 == 0:
            continue
        sign = (-1) ** (index + 1) if alternating else 1
        answer += Fraction(sign, index)
    return answer


def w_coefficient(index: int) -> Fraction:
    if index <= 0 or index % 3 == 0:
        return Fraction(0)
    return Fraction(3 * (-1) ** (index + 1) + 1, index)


def phi_coefficient(d: int, m: int, degree: int) -> int:
    """Return [x^degree] (1+x)^(3dm) (1-x)^(-dm)."""

    return sum(
        generalized_binomial(3 * d * m, left)
        * (-1) ** (degree - left)
        * generalized_binomial(-d * m, degree - left)
        for left in range(degree + 1)
    )


def prefix_coefficient(d: int, c: int, m: int) -> int:
    """The coefficient T_{d,c}(m) in equation (25)."""

    return sum(phi_coefficient(d, m, degree) for degree in range(c * m))


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


def check_ternary_cartier_residues() -> int:
    checks = 0
    for m in range(1, 97):
        total = 3 * m
        harmonic = reduced_harmonic(total)
        alternating = reduced_harmonic(total, alternating=True)
        quadratic = Fraction(2, total) * (
            (1 + 9 * (-1) ** total) * harmonic
            + 3 * (1 + (-1) ** total) * alternating
        )
        normalized = quadratic / m
        assert fraction_mod_prime(normalized, 3) == 1
        checks += 1

    # C_3(W^3) == x/(1-x)^2 modulo 3.
    for m in range(1, 41):
        total = 3 * m
        cubic = Fraction(0)
        for left in range(1, total - 1):
            for middle in range(1, total - left):
                right = total - left - middle
                cubic += (
                    w_coefficient(left)
                    * w_coefficient(middle)
                    * w_coefficient(right)
                )
        assert fraction_mod_prime(cubic, 3) == m % 3
        checks += 1
    return checks


def check_frobenius_descent_lemma() -> int:
    checks = 0
    for d in (-5, -4, -2, -1, 1, 2, 4, 5):
        assert d % 3 != 0
        for c in (3, 6, 9):
            for m in range(1, 19):
                value = prefix_coefficient(d, c, m)
                assert value % 3 == 0
                if m % 3 == 0:
                    assert value % 3 == prefix_coefficient(d, c, m // 3) % 3
                checks += 1
    return checks


def check_leading_defect_formula() -> int:
    checks = 0
    inverse_two = pow(2, -1, 3)
    for level in (1, 2, 3):
        for n in (1, 2, 4):
            for d in (-2, -1, 1, 2):
                for c in range(1, 7):
                    high_index = n * 3**level
                    low_index = high_index // 3
                    difference = framed(d, c, high_index) - framed(
                        d, c, low_index
                    )
                    baseline = 3 ** (3 * level - 1)
                    assert difference % baseline == 0
                    observed = difference // baseline % 3
                    predicted = (
                        n**3
                        * inverse_two
                        * d**2
                        * (d + c)
                        * prefix_coefficient(d, c, low_index)
                    ) % 3
                    assert observed == predicted
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


def check_ternary_family() -> int:
    checks = 0
    for c in range(1, 7):
        for s in range(-8, 9):
            for n in (1, 2, 3, 4):
                for level in (1, 2):
                    high = reversion_coefficient(c, s, n * 3**level)
                    low = reversion_coefficient(c, s, n * 3 ** (level - 1))
                    assert vp(high - low, 3) >= 3 * level
                    checks += 1
    return checks


def main() -> None:
    published = check_published_values()
    lagrange = check_lagrange_and_integrality()
    budget = check_refined_budget()
    cartier = check_ternary_cartier_residues()
    descent = check_frobenius_descent_lemma()
    leading_defect = check_leading_defect_formula()
    towers, sharp = check_odd_towers()
    ternary = check_ternary_family()
    total = (
        published
        + lagrange
        + budget
        + cartier
        + descent
        + leading_defect
        + towers
        + ternary
    )
    print(f"published derived-sequence checks: {published}")
    print(f"Lagrange/integrality checks: {lagrange}")
    print(f"refined valuation-budget checks: {budget}")
    print(f"ternary Cartier-residue checks: {cartier}")
    print(f"Frobenius-descent coefficient checks: {descent}")
    print(f"leading-defect formula checks: {leading_defect}")
    print(f"p >= 5 tower checks: {towers} ({sharp} sharp)")
    print(f"full ternary-family checks: {ternary}")
    print(f"all {total} A263843 reduction checks passed")


if __name__ == "__main__":
    main()
