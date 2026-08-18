"""Exact checks for A156554LegendreCoefficientTower.md.

These computations are regression evidence for the written proof, not a
substitute for it.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


PUBLISHED = (
    1,
    6,
    110,
    2562,
    66222,
    1815506,
    51697802,
    1511679210,
    45076309166,
    1364497268946,
    41800229045610,
    1292986222651646,
    40317756506959050,
    1265712901796074842,
    39965073938276694002,
    1268208750951634765562,
    40419340092267053380782,
    1293151592990764737265490,
)


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


@lru_cache(maxsize=None)
def framed_coefficient(a: int, b: int, c: int, s: int, n: int) -> int:
    """Coefficient in equation (1), using the binomial Legendre formula."""
    answer = 0
    for k in range(s * n + 1):
        target = c * n - k
        if target < 0:
            continue
        x_coefficient = sum(
            generalized_binomial(a * n, j)
            * (-1) ** (target - j)
            * generalized_binomial((b - s) * n, target - j)
            for j in range(target + 1)
        )
        answer += comb(s * n, k) ** 2 * x_coefficient
    return answer


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
    if value == 0:
        return 10**9
    return vp_integer(value.numerator, prime) - vp_integer(value.denominator, prime)


def factorial_vp(n: int, prime: int) -> int:
    answer = 0
    while n:
        n //= prime
        answer += n
    return answer


def polynomial_product(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def polynomial_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def polynomial_scale(polynomial: list[int], scalar: int) -> list[int]:
    return [scalar * coefficient for coefficient in polynomial]


def check_published_values() -> int:
    observed = tuple(framed_coefficient(0, 0, 1, 2, n) for n in range(18))
    assert observed == PUBLISHED
    return len(PUBLISHED)


def check_legendre_constant_term() -> int:
    checks = 0
    # Q_m(x)=(1-x)^m P_m((1+x)/(1-x)) obeys the transformed Legendre
    # recurrence.  Compute Q_m independently of the binomial-square formula.
    previous = [1]
    current = [1, 1]
    for m in range(13):
        recurrence_value = previous if m == 0 else current
        constant_term_value = [comb(m, k) ** 2 for k in range(m + 1)]
        assert recurrence_value == constant_term_value
        checks += 1
        if m == 0:
            continue
        numerator = polynomial_add(
            polynomial_scale(polynomial_product([1, 1], current), 2 * m + 1),
            polynomial_scale(polynomial_product([1, -2, 1], previous), -m),
        )
        assert all(coefficient % (m + 1) == 0 for coefficient in numerator)
        following = [coefficient // (m + 1) for coefficient in numerator]
        previous, current = current, following
    return checks


RAYS = ((1, 0), (0, 1), (1, -1))


def check_mixed_ray_exclusion() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for first in range(3):
            for second in range(first + 1, 3):
                u = RAYS[first]
                v = RAYS[second]
                for j in range(1, 3 * prime + 1):
                    if j % prime == 0:
                        continue
                    for k in range(1, 3 * prime + 1):
                        if k % prime == 0:
                            continue
                        exponent = (j * u[0] + k * v[0], j * u[1] + k * v[1])
                        assert exponent[0] % prime or exponent[1] % prime
                        checks += 1
    return checks


def reduced_coefficient(kind: str, exponent: int, prime: int) -> Fraction:
    if exponent <= 0 or exponent % prime == 0:
        return Fraction(0)
    if kind == "u":
        return Fraction(1, exponent)
    if kind == "v":
        return Fraction((-1) ** (exponent + 1), exponent)
    raise ValueError(kind)


def square_coefficient(
    alpha: int, beta: int, exponent: int, prime: int
) -> Fraction:
    return sum(
        (
            alpha * reduced_coefficient("u", j, prime)
            + beta * reduced_coefficient("v", j, prime)
        )
        * (
            alpha * reduced_coefficient("u", exponent - j, prime)
            + beta * reduced_coefficient("v", exponent - j, prime)
        )
        for j in range(1, exponent)
    )


def check_reciprocal_square() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for alpha, beta in ((1, 0), (0, 1), (1, 1), (2, -3), (-4, 1)):
            for m in range(1, 5 * prime + 1):
                coefficient = square_coefficient(alpha, beta, prime * m, prime)
                assert vp_fraction(coefficient, prime) >= 1 + vp_integer(m, prime)
                checks += 1
    return checks


def check_factorial_budget() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for level in range(1, 5):
            for degree in range(3, 121):
                assert degree * level - factorial_vp(degree, prime) >= 3 * level
                checks += 1
    return checks


def check_parameter_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    parameter_sets = (
        (0, 0, 1, 2),
        (1, 0, 1, 1),
        (-1, 0, 1, 2),
        (0, -1, 1, 2),
        (2, -2, 2, 1),
        (-2, 1, 1, 3),
        (1, 2, 2, 2),
    )
    for parameters in parameter_sets:
        for prime in (5, 7):
            for n in (1, 2):
                for level in (1, 2):
                    high = framed_coefficient(*parameters, n * prime**level)
                    low = framed_coefficient(*parameters, n * prime ** (level - 1))
                    valuation = vp_integer(high - low, prime)
                    assert valuation >= 3 * level
                    sharp += valuation == 3 * level
                    checks += 1

    # A named pure-prime third level without expanding the broader grid.
    high = framed_coefficient(0, 0, 1, 2, 5**3)
    low = framed_coefficient(0, 0, 1, 2, 5**2)
    valuation = vp_integer(high - low, 5)
    assert valuation >= 9
    sharp += valuation == 9
    checks += 1
    assert sharp > 0
    return checks, sharp


def main() -> None:
    published = check_published_values()
    legendre = check_legendre_constant_term()
    mixed = check_mixed_ray_exclusion()
    reciprocal = check_reciprocal_square()
    budget = check_factorial_budget()
    towers, sharp = check_parameter_towers()
    total = published + legendre + mixed + reciprocal + budget + towers
    print(f"published A156554 value checks: {published}")
    print(f"Legendre constant-term checks: {legendre}")
    print(f"mixed-ray Cartier exclusions: {mixed}")
    print(f"reciprocal-square valuation checks: {reciprocal}")
    print(f"factorial valuation-budget checks: {budget}")
    print(f"parameter-tower checks: {towers} ({sharp} sharp)")
    print(f"all {total} A156554 checks passed")


if __name__ == "__main__":
    main()
