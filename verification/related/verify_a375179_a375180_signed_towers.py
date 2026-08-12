"""Exact checks for the signed odd-power towers A375179/A375180."""

from fractions import Fraction
from functools import lru_cache
from math import comb


PRIMES = (7, 11, 13, 17, 19)
ODD_POWERS = (3, 5, 7, 9)
SLOPES = (-4, -3, -2, -1, 1, 2, 3, 4)


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
    if value == 0:
        return 10**9
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def fraction_mod(value: Fraction, modulus: int) -> int:
    return value.numerator * pow(value.denominator % modulus, -1, modulus) % modulus


def generalized_binomial(n: int, k: int) -> int:
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


def f(slope: int, n: int, j: int) -> int:
    return generalized_binomial(slope * n + j - 1, j)


def unit_quotient(slope: int, prime: int, n: int, j: int) -> Fraction:
    out = Fraction(1)
    for h in range(1, prime * j):
        if h % prime:
            out *= 1 + Fraction(slope * prime * n, h)
    return out


def unit_square_sum(prime: int, exponent: int) -> Fraction:
    return sum(
        (Fraction(1, u * u) for u in range(1, prime**exponent) if u % prime),
        Fraction(),
    )


@lru_cache(maxsize=None)
def c(slope: int, n: int, power: int) -> int:
    return sum(f(slope, n, j) ** power for j in range(n))


@lru_cache(maxsize=None)
def signed(n: int, dilation: int, power: int) -> int:
    return sum(
        (-1) ** (n + k + 1) * comb(dilation * n, k) ** power
        for k in range(n)
    )


def check_conversion_and_lift() -> int:
    checks = 0
    for dilation in (1, 2, 3, 4):
        for power in ODD_POWERS:
            for n in range(1, 15):
                assert signed(n, dilation, power) == (-1) ** (n + 1) * c(
                    -dilation, n, power
                )
                checks += 1

    for slope in SLOPES:
        for prime in PRIMES:
            if slope % prime == 0:
                continue
            for exponent in (1, 2):
                n = prime**exponent
                for j in range(1, min(n, 80)):
                    t = valuation(j, prime)
                    quotient = unit_quotient(slope, prime, n, j)
                    assert Fraction(
                        f(slope, prime * n, prime * j), f(slope, n, j)
                    ) == quotient
                    assert valuation(f(slope, n, j), prime) == exponent - t
                    assert rational_valuation(quotient - 1, prime) >= (
                        exponent + 2 * t + 3
                    )
                    checks += 3
    return checks


def check_critical_shells() -> int:
    checks = 0
    for slope in SLOPES:
        for power in ODD_POWERS:
            for prime in PRIMES:
                if prime < power + 4 or slope % prime == 0:
                    continue
                for exponent in (1, 2):
                    n = prime**exponent
                    tau = unit_square_sum(prime, exponent) / n
                    total = Fraction()
                    for a in range(1, prime):
                        j = prime ** (exponent - 1) * a
                        quotient = Fraction(
                            f(slope, prime * n, prime * j), f(slope, n, j)
                        )
                        harmonic = sum(
                            (Fraction(1, h) for h in range(1, a)), Fraction()
                        )
                        assert fraction_mod(
                            Fraction(f(slope, n, j), prime)
                            - Fraction(slope, a) * (1 + slope * prime * harmonic),
                            prime**2,
                        ) == 0
                        predicted = (
                            -Fraction(power, 2)
                            * slope
                            * prime ** (3 * exponent + 1)
                            * tau
                            * a
                            * (a + slope * prime)
                        )
                        assert fraction_mod(
                            quotient**power - 1 - predicted,
                            prime ** (3 * exponent + 3),
                        ) == 0
                        total += f(slope, n, j) ** power * (
                            quotient**power - 1
                        )
                        checks += 2
                    assert rational_valuation(total, prime) >= (
                        3 * exponent + power + 3
                    )
                    checks += 1
    return checks


def check_shells_and_towers() -> int:
    checks = 0
    sharp_named = {
        (dilation, power): False
        for dilation in (2, 3)
        for power in ODD_POWERS
    }
    for slope in SLOPES:
        for power in ODD_POWERS:
            for prime in PRIMES:
                if prime < power + 4 or slope % prime == 0:
                    continue
                for level in (2, 3):
                    if prime**level > 700:
                        continue
                    difference = c(slope, prime**level, power) - c(
                        slope, prime ** (level - 1), power
                    )
                    slack = valuation(difference, prime) - (3 * level + power)
                    assert slack >= 0, (slope, power, prime, level, slack)
                    if -slope in (2, 3):
                        assert difference == (
                            signed(prime**level, -slope, power)
                            - signed(prime ** (level - 1), -slope, power)
                        )
                        sharp_named[-slope, power] |= slack == 0
                    checks += 1

                if power == 3 and prime <= 11:
                    exponent = 2
                    n = prime**exponent
                    shell = sum(
                        (
                            Fraction(f(slope, n, j) ** power)
                            * (
                                Fraction(
                                    f(slope, prime * n, prime * j),
                                    f(slope, n, j),
                                )
                                ** power
                                - 1
                            )
                            for j in range(1, n)
                            if valuation(j, prime) == 0
                        ),
                        Fraction(),
                    )
                    assert rational_valuation(shell, prime) >= (
                        3 * exponent + power + 3
                    )
                    checks += 1
    assert all(sharp_named.values())
    return checks


def main() -> None:
    conversion = check_conversion_and_lift()
    critical = check_critical_shells()
    towers = check_shells_and_towers()
    total = conversion + critical + towers
    print(f"conversion, exact-lift, and valuation checks: {conversion}")
    print(f"slope-dependent critical-shell checks: {critical}")
    print(f"penultimate-shell and full-tower checks: {towers}")
    print(f"all {total} checks passed")


if __name__ == "__main__":
    main()
