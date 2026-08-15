"""Exact checks for the A079489 Lagrange-kernel reduction."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


def series_mul(left: list[Fraction], right: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: degree + 1 - i]):
            out[i + j] += a * b
    return out


def series_inverse(series: list[Fraction], degree: int) -> list[Fraction]:
    assert series[0] != 0
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = 1 / series[0]
    for n in range(1, degree + 1):
        out[n] = -sum(series[j] * out[n - j] for j in range(1, n + 1)) / series[0]
    return out


def series_pow(series: list[Fraction], exponent: int, degree: int) -> list[Fraction]:
    if exponent < 0:
        return series_pow(series_inverse(series, degree), -exponent, degree)
    out = [Fraction(1)] + [Fraction(0)] * degree
    base = series[: degree + 1]
    power = exponent
    while power:
        if power & 1:
            out = series_mul(out, base, degree)
        power >>= 1
        if power:
            base = series_mul(base, base, degree)
    return out


def series_compose(series: list[Fraction], inner: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    power = [Fraction(1)] + [Fraction(0)] * degree
    for coefficient in series:
        for index in range(degree + 1):
            out[index] += coefficient * power[index]
        power = series_mul(power, inner, degree)
    return out


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def a_series(degree: int) -> list[Fraction]:
    return [
        Fraction(2 ** (2 * n + 1) * catalan(n) - catalan(2 * n + 1))
        for n in range(degree + 1)
    ]


def b_series(degree: int) -> list[Fraction]:
    """Solve B(x)=1/A(x B(x)) by degree-contracting fixed iteration."""
    a = a_series(degree)
    b = [Fraction(1)] + [Fraction(0)] * degree
    x_b = [Fraction(0)] + b[:degree]
    for _ in range(degree + 1):
        composed = series_compose(a, x_b, degree)
        b = series_inverse(composed, degree)
        x_b = [Fraction(0)] + b[:degree]
    return b


def kernel(q: int, s: int, n: int) -> int:
    degree = s * n
    return sum(
        generalized_binomial(2 * q * n, j)
        * generalized_binomial(q * n + degree - j - 1, degree - j)
        for j in range(degree + 1)
    )


def direct_formula(r: int, s: int, n: int) -> Fraction:
    if r == 0:
        return Fraction(0)
    q = r + 2 * s
    if q == 0:
        return Fraction(4 * (-1) ** (s * n) - 2)
    return Fraction(r, q) * kernel(q, s, n)


def reverse_formula(r: int, s: int, n: int) -> Fraction:
    if r == 0:
        return Fraction(0)
    q = s - r
    if q == 0:
        return Fraction(2 * (-1) ** (s * n) - 1)
    return Fraction(-r, q) * kernel(q, s, n)


def valuation_fraction(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    numerator, denominator = value.numerator, value.denominator
    out = 0
    while numerator % prime == 0:
        numerator //= prime
        out += 1
    while denominator % prime == 0:
        denominator //= prime
        out -= 1
    return out


def check_algebraic_equation() -> int:
    checks = 0
    for degree in range(1, 18):
        a = a_series(degree)
        a2 = series_mul(a, a, degree)
        x_a2 = [Fraction(0)] + a2[:degree]
        one = [Fraction(1)] + [Fraction(0)] * degree
        numerator = series_pow([one[i] + x_a2[i] for i in range(degree + 1)], 2, degree)
        denominator = [one[i] - x_a2[i] for i in range(degree + 1)]
        rhs = series_mul(numerator, series_inverse(denominator, degree), degree)
        assert rhs == a
        checks += 1
    return checks


def check_lagrange_formulas() -> tuple[int, int]:
    degree = 12
    a = a_series(degree)
    b = b_series(degree)
    direct_checks = 0
    reverse_checks = 0
    for r in range(-5, 6):
        for s in range(1, 4):
            for n in range(1, 4):
                target = s * n
                if target > degree:
                    continue
                direct = series_pow(a, r * n, target)[target]
                reverse = series_pow(b, r * n, target)[target]
                assert direct == direct_formula(r, s, n)
                assert reverse == reverse_formula(r, s, n)
                assert direct.denominator == reverse.denominator == 1
                direct_checks += 1
                reverse_checks += 1
    return direct_checks, reverse_checks


def check_towers() -> tuple[int, int, int]:
    checks = 0
    normalized_checks = 0
    sharp = 0
    for r in range(-7, 8):
        for s in range(1, 4):
            for prime in (5, 7):
                for base in (1, 2):
                    high_direct = direct_formula(r, s, base * prime)
                    low_direct = direct_formula(r, s, base)
                    high_reverse = reverse_formula(r, s, base * prime)
                    low_reverse = reverse_formula(r, s, base)
                    direct_depth = valuation_fraction(high_direct - low_direct, prime)
                    reverse_depth = valuation_fraction(high_reverse - low_reverse, prime)
                    assert direct_depth >= 3
                    assert reverse_depth >= 3
                    sharp += int(direct_depth == 3) + int(reverse_depth == 3)
                    checks += 2

                    if r and r + 2 * s:
                        q = r + 2 * s
                        normalized = Fraction(r, q) * (
                            kernel(q, s, base * prime) - kernel(q, s, base)
                        )
                        assert valuation_fraction(normalized, prime) >= 3
                        normalized_checks += 1
                    if r and s - r:
                        q = s - r
                        normalized = Fraction(-r, q) * (
                            kernel(q, s, base * prime) - kernel(q, s, base)
                        )
                        assert valuation_fraction(normalized, prime) >= 3
                        normalized_checks += 1

    for r, s, prime in ((3, 1, 5), (-7, 1, 5), (5, 2, 5), (7, 1, 7)):
        for formula in (direct_formula, reverse_formula):
            difference = formula(r, s, prime * prime) - formula(r, s, prime)
            assert valuation_fraction(difference, prime) >= 6
            checks += 1
    return checks, normalized_checks, sharp


def main() -> None:
    algebraic_checks = check_algebraic_equation()
    direct_checks, reverse_checks = check_lagrange_formulas()
    tower_checks, normalized_checks, sharp = check_towers()
    print(f"A079489 algebraic-series checks: {algebraic_checks}")
    print(f"A079489 direct Lagrange checks: {direct_checks}")
    print(f"A079489 reverted Lagrange checks: {reverse_checks}")
    print(f"A079489 tower checks: {tower_checks} ({sharp} sharp first-level cases)")
    print(f"A079489 normalized-kernel checks: {normalized_checks}")
    print("A079489 Lagrange-kernel checks passed")


if __name__ == "__main__":
    main()
