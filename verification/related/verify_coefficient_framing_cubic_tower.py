"""Exact checks for CoefficientFramingCubicTower.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


PRIMES = (3, 5, 7, 11, 13)


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


def coefficient(alpha: int, beta: int, n: int) -> int:
    """[x^n] ((1+x)^alpha (1-x)^beta)^n."""
    return sum(
        generalized_binomial(alpha * n, k)
        * (-1) ** (n - k)
        * generalized_binomial(beta * n, n - k)
        for k in range(n + 1)
    )


def coefficient_at_slope(alpha: int, beta: int, slope: int, n: int) -> int:
    """[x^(slope*n)] (1+x)^(alpha*n) (1-x)^(beta*n)."""
    degree = slope * n
    return sum(
        generalized_binomial(alpha * n, k)
        * (-1) ** (degree - k)
        * generalized_binomial(beta * n, degree - k)
        for k in range(degree + 1)
    )


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def rational_valuation(value: Fraction, prime: int) -> int:
    return valuation(value.numerator, prime) - valuation(
        value.denominator, prime
    )


def reduced_harmonic(total: int, prime: int, alternating: bool) -> Fraction:
    return sum(
        (
            Fraction((-1) ** (j + 1), j)
            if alternating
            else Fraction(1, j)
        )
        for j in range(1, total)
        if j % prime
    )


def l_coefficient(index: int, alpha: int, beta: int, prime: int) -> Fraction:
    if index <= 0 or index % prime == 0:
        return Fraction(0)
    return Fraction(alpha * (-1) ** (index + 1) - beta, index)


def l_square_coefficient(
    total: int, alpha: int, beta: int, prime: int
) -> Fraction:
    return sum(
        l_coefficient(j, alpha, beta, prime)
        * l_coefficient(total - j, alpha, beta, prime)
        for j in range(1, total)
    )


def check_source_identifications() -> int:
    expected = {
        (1, -1): (2, 8, 38, 192, 1002),  # A002003
        (-1, -2): (1, 5, 19, 85, 376),  # A348410
        (-2, -4): (2, 14, 92, 654, 4752),  # A351857
        (-1, -3): (2, 12, 74, 484, 3252),  # A352373
        (4, -3): (7, 97, 1519, 25089, 427007),  # A370101
        (4, -4): (8, 128, 2312, 44032, 864008),  # A370102
    }
    checks = 0
    for parameters, values in expected.items():
        actual = tuple(
            coefficient(*parameters, n) for n in range(1, len(values) + 1)
        )
        assert actual == values
        checks += len(values)
    return checks


def check_harmonic_lemma() -> int:
    checks = 0
    for prime in PRIMES:
        epsilon = int(prime == 3)
        for exponent in (1, 2):
            for unit in (1, 2, 4):
                if unit % prime == 0:
                    continue
                total = unit * prime**exponent
                ordinary = reduced_harmonic(total, prime, False)
                assert rational_valuation(ordinary, prime) >= (
                    2 * exponent - epsilon
                )
                checks += 1
                if total % 2 == 0:
                    alternating = reduced_harmonic(total, prime, True)
                    assert rational_valuation(alternating, prime) >= (
                        2 * exponent - epsilon
                    )
                    checks += 1
    return checks


def check_quadratic_cartier_lemma() -> int:
    checks = 0
    for prime in PRIMES:
        epsilon = int(prime == 3)
        for alpha in range(-3, 4):
            for beta in range(-3, 4):
                for m in range(1, 13):
                    total = prime * m
                    value = l_square_coefficient(
                        total, alpha, beta, prime
                    )
                    assert rational_valuation(value, prime) >= (
                        valuation(total, prime) - epsilon
                    )
                    checks += 1
    return checks


def check_cubic_tower() -> int:
    checks = 0
    parameter_pairs = tuple(
        (alpha, beta)
        for alpha in range(-4, 5)
        for beta in range(-4, 5)
    )
    for prime in PRIMES:
        loss = int(prime == 3)
        for alpha, beta in parameter_pairs:
            for n in (1, 2, 3):
                for level in (1, 2):
                    upper = coefficient(alpha, beta, n * prime**level)
                    lower = coefficient(
                        alpha, beta, n * prime ** (level - 1)
                    )
                    assert valuation(upper - lower, prime) >= (
                        3 * level - loss
                    )
                    checks += 1
    return checks


def check_integral_coefficient_slopes() -> int:
    checks = 0
    parameter_pairs = (
        (-3, -2),
        (-2, 1),
        (-1, -4),
        (1, -2),
        (2, 3),
        (4, -1),
    )
    for prime in (3, 5, 7):
        loss = int(prime == 3)
        for alpha, beta in parameter_pairs:
            for slope in range(4):
                for n in (1, 2):
                    for level in (1, 2):
                        upper = coefficient_at_slope(
                            alpha, beta, slope, n * prime**level
                        )
                        lower = coefficient_at_slope(
                            alpha, beta, slope, n * prime ** (level - 1)
                        )
                        assert valuation(upper - lower, prime) >= (
                            3 * level - loss
                        )
                        checks += 1
    return checks


def check_named_towers_at_level_three() -> int:
    checks = 0
    named = (
        (1, -1),
        (-1, -2),
        (-2, -4),
        (-1, -3),
        (4, -3),
        (4, -4),
    )
    for prime in (3, 5, 7):
        loss = int(prime == 3)
        for alpha, beta in named:
            upper = coefficient(alpha, beta, prime**3)
            lower = coefficient(alpha, beta, prime**2)
            assert valuation(upper - lower, prime) >= 9 - loss
            checks += 1
    return checks


def check_sharp_boundaries() -> int:
    examples = (
        # (alpha, beta, prime, level, n, exact valuation)
        (-3, -1, 3, 1, 1, 2),
        (-3, -1, 3, 2, 1, 5),
        (-3, -1, 3, 3, 1, 8),
        (1, -1, 5, 1, 1, 3),
        (1, -1, 5, 2, 1, 6),
    )
    for alpha, beta, prime, level, n, expected in examples:
        difference = coefficient(alpha, beta, n * prime**level)
        difference -= coefficient(
            alpha, beta, n * prime ** (level - 1)
        )
        assert valuation(difference, prime) == expected
    return len(examples)


def main() -> None:
    counts = {
        "source identifications": check_source_identifications(),
        "reduced harmonic lemma": check_harmonic_lemma(),
        "quadratic Cartier lemma": check_quadratic_cartier_lemma(),
        "cubic tower grid": check_cubic_tower(),
        "integral coefficient slopes": check_integral_coefficient_slopes(),
        "named level-three checks": check_named_towers_at_level_three(),
        "sharp boundaries": check_sharp_boundaries(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(
        "all "
        f"{sum(counts.values())} "
        "coefficient-framing cubic-tower checks passed"
    )


if __name__ == "__main__":
    main()
