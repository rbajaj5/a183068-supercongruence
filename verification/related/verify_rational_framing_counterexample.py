"""Exact checks for the counterexample to the rational-framing theorem.

The proof note is related-results/RationalFramingCounterexample.md.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def valuation(value: int | Fraction, prime: int) -> int:
    if isinstance(value, Fraction):
        return valuation(value.numerator, prime) - valuation(
            value.denominator, prime
        )
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        out += 1
        value //= prime
    return out


def seed(n: int) -> int:
    """Coefficient of z^n in z/(1-z)+16 z^4/(1-z^4)."""

    return 1 + 16 * (n % 4 == 0)


def framed(n: int) -> int:
    """[x^n] ((1-x)^(-1) (1-x^4)^(-4))^n."""

    return sum(
        comb(4 * n + j - 1, j)
        * comb(2 * n - 4 * j - 1, n - 4 * j)
        for j in range(n // 4 + 1)
    )


def check_two_sequence() -> int:
    checks = 0
    for prime in (2, 3, 5, 7, 11, 13):
        for level in range(1, 7):
            modulus = prime ** (2 * level)
            for multiplier in range(1, 101):
                assert (
                    seed(multiplier * prime**level)
                    - seed(multiplier * prime ** (level - 1))
                ) % modulus == 0
                checks += 1
    return checks


def check_weighted_harmonic_failure() -> int:
    weighted = sum(
        Fraction(seed(5 - k) * seed(k), k * k) for k in range(1, 5)
    )
    assert weighted == Fraction(2653, 144)
    assert valuation(weighted, 5) == 0
    assert weighted.numerator * pow(weighted.denominator, -1, 5) % 5 == 2
    return 3


def check_framing_failure() -> int:
    assert framed(1) == 1
    assert framed(5) == 226
    assert framed(5) - framed(1) == 225
    assert valuation(framed(5) - framed(1), 5) == 2
    assert (framed(5) - framed(1)) % 5**3 != 0
    return 5


def check_closed_formula() -> int:
    # Independent polynomial multiplication for the first small values.
    checks = 0
    for n in range(1, 13):
        coefficients = [1]
        base = [0] * (n + 1)
        for degree in range(n + 1):
            total = 0
            for j in range(degree // 4 + 1):
                total += comb(4 * n + j - 1, j) * comb(
                    n + degree - 4 * j - 1, degree - 4 * j
                )
            base[degree] = total
        assert base[n] == framed(n)
        checks += 1
    return checks


def main() -> None:
    counts = {
        "2-sequence": check_two_sequence(),
        "weighted theorem failure": check_weighted_harmonic_failure(),
        "framing theorem failure": check_framing_failure(),
        "closed coefficient formula": check_closed_formula(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(f"all {sum(counts.values())} rational-framing counterexample checks passed")


if __name__ == "__main__":
    main()

