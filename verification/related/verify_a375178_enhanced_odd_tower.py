"""Exact checks for the enhanced A375178 odd-power tower."""

from fractions import Fraction
from functools import lru_cache
from math import comb


PRIMES = (7, 11, 13, 17, 19)
ODD_POWERS = (3, 5, 7, 9)


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


def f(n: int, j: int) -> int:
    return comb(n + j - 1, j)


def unit_quotient(prime: int, n: int, j: int) -> Fraction:
    out = Fraction(1)
    for h in range(1, prime * j):
        if h % prime:
            out *= 1 + Fraction(prime * n, h)
    return out


def unit_square_sum(prime: int, exponent: int) -> Fraction:
    return sum(
        (Fraction(1, u * u) for u in range(1, prime**exponent) if u % prime),
        Fraction(),
    )


@lru_cache(maxsize=None)
def b(n: int, power: int) -> int:
    return sum(f(n, j) ** power for j in range(n))


def check_scaled_bounds() -> int:
    checks = 0
    for power in ODD_POWERS:
        for prime in PRIMES:
            if prime < power + 4:
                continue
            for exponent in (1, 2):
                n = prime**exponent
                for j in range(1, min(n, 100)):
                    t = valuation(j, prime)
                    quotient = unit_quotient(prime, n, j)
                    assert Fraction(f(prime * n, prime * j), f(n, j)) == quotient
                    assert rational_valuation(quotient - 1, prime) >= (
                        exponent + 2 * t + 3
                    )
                    difference = f(n, j) ** power * (quotient**power - 1)
                    assert rational_valuation(difference, prime) >= (
                        (power + 1) * exponent - (power - 2) * t + 3
                    )
                    checks += 3
    return checks


def check_critical_shell() -> int:
    checks = 0
    for power in ODD_POWERS:
        for prime in PRIMES:
            if prime < power + 4:
                continue
            m = power - 2
            harmonic_sum = Fraction()
            for a in range(1, prime):
                harmonic = sum((Fraction(1, j) for j in range(1, a)), Fraction())
                harmonic_sum += harmonic / a**m
            assert rational_valuation(harmonic_sum, prime) >= 1
            checks += 1

            for exponent in (1, 2):
                n = prime**exponent
                tau = unit_square_sum(prime, exponent) / prime**exponent
                total = Fraction()
                for a in range(1, prime):
                    j = prime ** (exponent - 1) * a
                    quotient = unit_quotient(prime, n, j)
                    harmonic = sum(
                        (Fraction(1, index) for index in range(1, a)), Fraction()
                    )
                    assert fraction_mod(
                        Fraction(f(n, j), prime)
                        - Fraction(1, a) * (1 + prime * harmonic),
                        prime**2,
                    ) == 0
                    predicted = (
                        -Fraction(power, 2)
                        * prime ** (3 * exponent + 1)
                        * tau
                        * a
                        * (a + prime)
                    )
                    assert fraction_mod(
                        quotient**power - 1 - predicted,
                        prime ** (3 * exponent + 3),
                    ) == 0
                    total += f(n, j) ** power * (quotient**power - 1)
                    checks += 2
                assert rational_valuation(total, prime) >= (
                    3 * exponent + power + 3
                )
                checks += 1
    return checks


def check_unit_boundary() -> int:
    checks = 0
    power = 5
    for prime in PRIMES:
        if prime < power + 4:
            continue
        n = prime**2
        normalized = sum(
            (f(n, k) // n) ** power for k in range(1, n) if k % prime
        )
        assert normalized % prime == 0
        checks += 1
    return checks


def check_towers() -> int:
    checks = 0
    sharp_by_power = {power: False for power in ODD_POWERS}
    for power in ODD_POWERS:
        for prime in PRIMES:
            if prime < power + 4:
                continue
            for level in (2, 3):
                if prime**level > 1500:
                    continue
                difference = b(prime**level, power) - b(
                    prime ** (level - 1), power
                )
                slack = valuation(difference, prime) - (3 * level + power)
                assert slack >= 0, (power, prime, level, slack)
                sharp_by_power[power] |= slack == 0
                checks += 1
    assert all(sharp_by_power.values())
    return checks


def main() -> None:
    scaled = check_scaled_bounds()
    critical = check_critical_shell()
    unit = check_unit_boundary()
    towers = check_towers()
    total = scaled + critical + unit + towers
    print(f"scaled quotient and valuation checks: {scaled}")
    print(f"critical-shell and harmonic checks: {critical}")
    print(f"unit-boundary checks: {unit}")
    print(f"enhanced odd-power tower checks: {towers}")
    print(f"all {total} checks passed")


if __name__ == "__main__":
    main()
