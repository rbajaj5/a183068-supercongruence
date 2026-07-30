"""Exact checks for CatalanBallotPrimeLevelTheorem.md.

The script verifies transcription and finite instances.  The Markdown note
contains the general proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
ODD_EXPONENTS = tuple(range(1, 20, 2))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def rational_valuation(value: Fraction, prime: int) -> int:
    return valuation(value.numerator, prime) - valuation(
        value.denominator, prime
    )


def ballot_entry(prime: int, k: int) -> int:
    previous = comb(2 * prime - 1, k - 1) if k else 0
    return comb(2 * prime - 1, k) - previous


def ballot_power_numerator(prime: int, exponent: int) -> int:
    return sum(
        ballot_entry(prime, k) ** exponent for k in range(prime)
    )


def harmonic(k: int, power: int = 1) -> Fraction:
    return sum(
        (Fraction(1, j**power) for j in range(1, k + 1)),
        start=Fraction(0),
    )


def alpha(k: int) -> Fraction:
    return -(2 * harmonic(k - 1) + Fraction(1, k))


def beta(k: int) -> Fraction:
    first = harmonic(k - 1)
    return (
        2 * first**2
        - 2 * harmonic(k - 1, 2)
        + 2 * first / k
    )


def check_local_expansion() -> int:
    checks = 0
    for prime in PRIMES:
        for k in range(1, prime):
            scaled = Fraction(ballot_entry(prime, k), 2 * (-1) ** k)
            approximation = 1 + prime * alpha(k) + prime**2 * beta(k)
            assert rational_valuation(scaled - approximation, prime) >= 3
            checks += 1
    return checks


def check_harmonic_identities() -> int:
    checks = 0
    for prime in PRIMES:
        a_sum = sum(
            (-1) ** k * harmonic(k - 1) ** 2
            for k in range(1, prime)
        )
        b_sum = sum(
            (-1) ** k * harmonic(k - 1) / k
            for k in range(1, prime)
        )
        c_sum = sum(
            Fraction((-1) ** k, k**2) for k in range(1, prime)
        )
        d_sum = sum(
            (-1) ** k * harmonic(k - 1, 2)
            for k in range(1, prime)
        )

        linear = sum(
            (-1) ** k * alpha(k) for k in range(1, prime)
        )
        assert linear == -harmonic(prime - 1)
        checks += 1

        assert 2 * (a_sum + b_sum) + c_sum == harmonic(prime - 1) ** 2
        checks += 1

        odd_inverse_squares = sum(
            Fraction(1, k**2) for k in range(1, prime) if k % 2
        )
        assert d_sum == odd_inverse_squares
        checks += 1

        assert rational_valuation(c_sum, prime) >= 1
        checks += 1
    return checks


def check_odd_power_theorem() -> int:
    checks = 0
    for prime in PRIMES:
        denominator = comb(2 * prime - 1, prime - 1)
        assert valuation(denominator - 1, prime) >= 3
        for exponent in ODD_EXPONENTS:
            numerator = ballot_power_numerator(prime, exponent)
            assert valuation(numerator - denominator, prime) >= 3
            checks += 1
    return checks


def check_named_consequences() -> int:
    checks = 0
    for prime in PRIMES:
        denominator = comb(2 * prime - 1, prime - 1)
        for exponent in (3, 5, 7):
            numerator = ballot_power_numerator(prime, exponent)
            quotient, remainder = divmod(numerator, denominator)
            assert remainder == 0
            assert valuation(quotient - 1, prime) >= 3
            checks += 1

        # A003161 uses the unnormalized cubic sum.
        cubic_sum = ballot_power_numerator(prime, 3)
        assert valuation(cubic_sum - 1, prime) >= 3
        checks += 1

        # A003162's odd bisection is the same cubic quotient as A183069.
        cubic_quotient = cubic_sum // denominator
        assert valuation(cubic_quotient - 1, prime) >= 3
        checks += 1
    return checks


def main() -> None:
    counts = {
        "local second-order expansions": check_local_expansion(),
        "harmonic identities": check_harmonic_identities(),
        "all-odd-exponent theorem": check_odd_power_theorem(),
        "named OEIS consequences": check_named_consequences(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(
        f"all {sum(counts.values())} Catalan-ballot prime-level checks passed"
    )


if __name__ == "__main__":
    main()
