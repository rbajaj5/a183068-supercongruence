"""Exact checks for the enhanced A219562 shifted-binomial tower."""

from fractions import Fraction
from functools import lru_cache
from math import comb


PRIMES = (5, 7, 11, 13)


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


def f(n: int, j: int) -> int:
    return comb(n + j - 1, j)


def unit_quotient(prime: int, n: int, j: int) -> Fraction:
    out = Fraction(1)
    for h in range(1, prime * j):
        if h % prime:
            out *= 1 + Fraction(prime * n, h)
    return out


@lru_cache(maxsize=None)
def b(n: int) -> int:
    return sum(f(n, j) ** 4 for j in range(n))


def check_exact_quotient_and_shell_bound() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in range(1, 4):
            n = prime**exponent
            for j in range(1, min(n, 180)):
                quotient = unit_quotient(prime, n, j)
                assert Fraction(f(prime * n, prime * j), f(n, j)) == quotient
                t = valuation(j, prime)
                assert valuation(f(n, j), prime) == exponent - t
                assert rational_valuation(quotient - 1, prime) >= exponent + 2 * t + 3
                difference = f(n, j) ** 4 * (quotient**4 - 1)
                assert rational_valuation(difference, prime) >= 5 * exponent - 2 * t + 3
                checks += 4
    return checks


def check_critical_shell() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in range(1, 4):
            modulus = prime ** (3 * exponent + 6)
            n = prime**exponent
            total = Fraction(0)
            for a in range(1, prime):
                j = prime ** (exponent - 1) * a
                quotient = unit_quotient(prime, n, j)
                total += f(n, j) ** 4 * (quotient**4 - 1)
            assert total.denominator % prime != 0
            assert total.numerator % modulus == 0, (prime, exponent)
            checks += 1
    return checks


def check_tower() -> int:
    checks = 0
    minimum_slack = 10**9
    for prime in PRIMES:
        for level in (2, 3):
            if prime**level > 1500:
                continue
            difference = b(prime**level) - b(prime ** (level - 1))
            slack = valuation(difference, prime) - (3 * level + 3)
            assert slack >= 0, (prime, level, slack)
            minimum_slack = min(minimum_slack, slack)
            checks += 1
    assert minimum_slack == 0
    return checks


def main() -> None:
    quotient_checks = check_exact_quotient_and_shell_bound()
    critical_checks = check_critical_shell()
    tower_checks = check_tower()
    print(f"exact quotient and shell checks: {quotient_checks}")
    print(f"critical-shell checks: {critical_checks}")
    print(f"enhanced A219562 tower checks: {tower_checks}")
    print(f"all {quotient_checks + critical_checks + tower_checks} checks passed")


if __name__ == "__main__":
    main()
