"""Exact checks for the conditional ordinary A376466 cubic-tower reduction.

The proof note is related-results/A376466OrdinaryTower.md.  These checks are
transcription and boundary tests.  In particular, they do not prove the open
quadratic Cartier-kernel descent recorded as Lemma 2 in the note.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from verify_a376_apery_companions import (
    a376466_outer,
    a376466_pairing,
    shifted_row,
    valuation,
)


PRIMES = (5, 7, 11)


def rational_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def unit_harmonic(limit: int, prime: int, power: int) -> Fraction:
    return sum(
        (Fraction(1, h**power) for h in range(1, limit + 1) if h % prime),
        Fraction(),
    )


def reduced_outer(n: int, k: int) -> int:
    """The outer kernel after extracting n/k from binom(n,k)."""

    return (
        (-1) ** (n + k)
        * comb(n - 1, k - 1)
        * comb(n + k, k) ** 2
    )


def descended_outer(n: int, q: int) -> int:
    if not 0 <= q < n:
        return 0
    return (
        (-1) ** (n + q - 1)
        * comb(n - 1, q)
        * comb(n + q, q) ** 2
    )


def cartier_kernel(n: int, q: int) -> int:
    if not 0 <= q < n:
        return 0
    return descended_outer(n, q) * shifted_row(n - 1, q)


def full_term(n: int, k: int) -> int:
    return a376466_outer(n, k) * shifted_row(n - 1, k)


def check_reciprocal_blocks() -> int:
    checks = 0
    for prime in PRIMES:
        for exponent in range(1, 5):
            block = prime**exponent
            for left in range(4):
                for power, target in ((1, 2 * exponent), (2, exponent)):
                    value = sum(
                        (
                            Fraction(1, k**power)
                            for k in range(left * block + 1, (left + 1) * block)
                            if k % prime
                        ),
                        Fraction(),
                    )
                    assert rational_valuation(value, prime) >= target
                    checks += 1
    return checks


def check_first_order_factorization() -> int:
    checks = 0
    for prime in PRIMES:
        for level in (1, 2):
            for n in range(1, 5):
                high_n = n * prime**level
                low_n = high_n // prime
                for k in range(1, high_n + 1):
                    if k % prime == 0:
                        continue
                    q = k // prime
                    harmonic = unit_harmonic(k, prime, 1)

                    high_outer = reduced_outer(high_n, k)
                    low_outer = descended_outer(low_n, q)
                    outer_model = low_outer * (
                        1 + Fraction(high_n, k) + high_n * harmonic
                    )
                    assert rational_valuation(high_outer - outer_model, prime) >= 2 * level
                    checks += 1

                    high_row = shifted_row(high_n - 1, k)
                    low_row = shifted_row(low_n - 1, q)
                    row_model = low_row * (1 - high_n * harmonic)
                    assert rational_valuation(high_row - row_model, prime) >= 2 * level
                    checks += 1

                    high_kernel = high_outer * high_row
                    low_kernel = cartier_kernel(low_n, q)
                    kernel_model = low_kernel * (1 + Fraction(high_n, k))
                    assert rational_valuation(high_kernel - kernel_model, prime) >= 2 * level
                    checks += 1
    return checks


def check_cartier_descent() -> int:
    checks = 0
    for prime in PRIMES:
        for level in (1, 2):
            for n in range(1, 5):
                high_n = n * prime**level
                low_n = high_n // prime
                for q in range(high_n):
                    difference = cartier_kernel(high_n, q) - cartier_kernel(
                        low_n, q // prime
                    )
                    assert valuation(difference, prime) >= 2 * level
                    checks += 1
    return checks


def check_shells_and_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    cases = [(p, 1, n) for p in (5, 7, 11, 13, 17, 19) for n in range(1, 7)]
    cases += [(p, 2, n) for p in (5, 7) for n in range(1, 4)]
    cases += [(5, 3, 1)]

    for prime, level, n in cases:
        high_n = n * prime**level
        low_n = high_n // prime
        modulus = prime ** (3 * level)

        scaled = sum(
            full_term(high_n, prime * q) - full_term(low_n, q)
            for q in range(low_n + 1)
        )
        unit = sum(full_term(high_n, k) for k in range(1, high_n) if k % prime)
        assert scaled % modulus == 0
        assert unit % modulus == 0
        checks += 2

        first_moment = sum(
            (
                Fraction(cartier_kernel(low_n, k // prime), k)
                for k in range(1, high_n)
                if k % prime
            ),
            Fraction(),
        )
        second_moment = sum(
            (
                Fraction(cartier_kernel(low_n, k // prime), k * k)
                for k in range(1, high_n)
                if k % prime
            ),
            Fraction(),
        )
        assert rational_valuation(first_moment, prime) >= 2 * level
        assert rational_valuation(second_moment, prime) >= level
        checks += 2

        difference = a376466_pairing(high_n) - a376466_pairing(low_n)
        depth = valuation(difference, prime)
        assert depth >= 3 * level
        sharp += int(depth == 3 * level)
        checks += 1

    return checks, sharp


def main() -> None:
    reciprocal = check_reciprocal_blocks()
    first_order = check_first_order_factorization()
    descent = check_cartier_descent()
    towers, sharp = check_shells_and_towers()
    total = reciprocal + first_order + descent + towers
    print(f"reciprocal block checks: {reciprocal}")
    print(f"first-order factorization checks: {first_order}")
    print(f"Cartier-kernel descent checks: {descent}")
    print(f"shell and tower checks: {towers} ({sharp} sharp)")
    print(f"all {total} conditional A376466 ordinary-tower checks passed")


if __name__ == "__main__":
    main()
