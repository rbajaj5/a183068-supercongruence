"""Exact checks for the enhanced A112028 shifted-binomial tower."""

from fractions import Fraction
from functools import lru_cache
from math import comb


PRIMES = (7, 11, 13)


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


def unit_power_sum(prime: int, exponent: int, power: int) -> Fraction:
    return sum(
        (Fraction(1, u**power) for u in range(1, prime**exponent) if u % prime),
        Fraction(),
    )


@lru_cache(maxsize=None)
def c(n: int) -> int:
    return sum(f(n, j) ** 3 for j in range(n))


def check_exact_quotient_and_bounds() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in range(1, 4):
            n = prime**exponent
            for j in range(1, min(n, 120)):
                quotient = unit_quotient(prime, n, j)
                t = valuation(j, prime)
                assert Fraction(f(prime * n, prime * j), f(n, j)) == quotient
                assert valuation(f(n, j), prime) == exponent - t
                assert rational_valuation(quotient - 1, prime) >= exponent + 2 * t + 3
                difference = f(n, j) ** 3 * (quotient**3 - 1)
                assert rational_valuation(difference, prime) >= 4 * exponent - t + 3
                checks += 4
    return checks


def check_unit_shell() -> int:
    checks = 0
    for prime in PRIMES:
        modulus = prime**3
        for a in range(1, prime):
            for b in range(prime):
                k = a + prime * b
                harmonic = sum(
                    (Fraction(1, j) for j in range(1, b + 1)), Fraction()
                )
                harmonic_two = sum(
                    (Fraction(1, j * j) for j in range(1, b + 1)), Fraction()
                )
                short_harmonic = sum(
                    (Fraction(1, j) for j in range(1, a)), Fraction()
                )
                first = harmonic - Fraction(b, a)
                second = (
                    (harmonic**2 - harmonic_two) / 2
                    + short_harmonic
                    - Fraction(b, a) * harmonic
                    + Fraction(b * b, a * a)
                )
                predicted = Fraction(1, a) * (
                    1 + prime * first + prime**2 * second
                )
                assert fraction_mod(
                    Fraction(f(prime**2, k), prime**2) - predicted, modulus
                ) == 0
                checks += 1

        for exponent in (2, 3):
            n = prime**exponent
            normalized = sum(
                (f(n, k) // n) ** 3 for k in range(1, n) if k % prime
            )
            assert normalized % prime**3 == 0
            checks += 1
    return checks


def check_penultimate_shell() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in (2, 3):
            n = prime**exponent
            tau = unit_power_sum(prime, exponent - 1, 2) / prime ** (exponent - 1)
            total = Fraction()
            for a in range(1, prime**2):
                if a % prime:
                    j = prime ** (exponent - 2) * a
                    quotient = unit_quotient(prime, n, j)
                    assert fraction_mod(
                        Fraction(f(n, j), prime**2) - Fraction(1, a), prime
                    ) == 0
                    normalized_quotient = (quotient**3 - 1) / prime ** (
                        3 * exponent - 1
                    )
                    assert fraction_mod(
                        normalized_quotient + Fraction(3, 2) * tau * a * a,
                        prime,
                    ) == 0
                    total += f(n, j) ** 3 * (quotient**3 - 1)
                    checks += 2
            assert rational_valuation(total, prime) >= 3 * exponent + 6
            checks += 1
    return checks


def check_critical_expansions() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in range(1, 4):
            n = prime**exponent
            tau = unit_power_sum(prime, exponent, 2) / prime**exponent
            assert rational_valuation(tau, prime) >= 0
            total = Fraction()
            for a in range(1, prime):
                j = prime ** (exponent - 1) * a
                quotient = unit_quotient(prime, n, j)
                predicted = (
                    -Fraction(3, 2)
                    * prime ** (3 * exponent + 1)
                    * tau
                    * a
                    * (a + prime)
                )
                modulus = prime ** (3 * exponent + 3)
                assert fraction_mod(quotient**3 - 1 - predicted, modulus) == 0

                harmonic = sum((Fraction(1, j) for j in range(1, a)), Fraction())
                binomial_prediction = Fraction(1, a) * (1 + prime * harmonic)
                assert fraction_mod(
                    Fraction(f(n, j), prime) - binomial_prediction, prime**2
                ) == 0
                total += f(n, j) ** 3 * (quotient**3 - 1)
                checks += 2

            assert rational_valuation(total, prime) >= 3 * exponent + 6
            checks += 1
    return checks


def check_harmonic_cancellation() -> int:
    checks = 0
    for prime in PRIMES:
        h1 = sum((Fraction(1, a) for a in range(1, prime)), Fraction())
        h2 = sum((Fraction(1, a * a) for a in range(1, prime)), Fraction())
        double = sum(
            (
                sum((Fraction(1, j) for j in range(1, a)), Fraction())
                / a
                for a in range(1, prime)
            ),
            Fraction(),
        )
        assert rational_valuation(h1, prime) >= 2
        assert rational_valuation(h2, prime) >= 1
        assert double == (h1 * h1 - h2) / 2
        assert rational_valuation(double, prime) >= 1
        checks += 4
    return checks


def check_tower() -> int:
    checks = 0
    minimum_slack = 10**9
    for prime in PRIMES:
        for level in (2, 3):
            if prime**level > 1500:
                continue
            difference = c(prime**level) - c(prime ** (level - 1))
            slack = valuation(difference, prime) - (3 * level + 3)
            assert slack >= 0, (prime, level, slack)
            minimum_slack = min(minimum_slack, slack)
            checks += 1
    assert minimum_slack == 0
    return checks


def main() -> None:
    quotient = check_exact_quotient_and_bounds()
    unit = check_unit_shell()
    penultimate = check_penultimate_shell()
    critical = check_critical_expansions()
    harmonic = check_harmonic_cancellation()
    tower = check_tower()
    total = quotient + unit + penultimate + critical + harmonic + tower
    print(f"exact quotient and bound checks: {quotient}")
    print(f"unit-shell checks: {unit}")
    print(f"penultimate-shell checks: {penultimate}")
    print(f"critical-expansion checks: {critical}")
    print(f"harmonic-cancellation checks: {harmonic}")
    print(f"enhanced A112028 tower checks: {tower}")
    print(f"all {total} checks passed")


if __name__ == "__main__":
    main()
