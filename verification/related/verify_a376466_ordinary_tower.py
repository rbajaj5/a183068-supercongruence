"""Exact checks for the proved ordinary A376466 cubic tower.

The proof note is related-results/A376466OrdinaryTower.md.  These checks are
transcription and boundary tests for its finite-product expansions, exact
three-term recurrence, Cartier induction, reciprocal moments, and tower.
"""

from __future__ import annotations

from fractions import Fraction
from functools import cache
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


@cache
def cartier_kernel(n: int, q: int) -> int:
    if not 0 <= q < n:
        return 0
    return descended_outer(n, q) * shifted_row(n - 1, q)


def full_term(n: int, k: int) -> int:
    return a376466_outer(n, k) * shifted_row(n - 1, k)


def recurrence_coefficients(n: int, j: int) -> tuple[int, int, int]:
    """Coefficients C_+, C_0, C_- in equation (8e)."""

    middle = (j + 1) ** 2 + j**2 + n * (n - 1)
    plus = j * (j + 1) ** 5
    zero = middle * j * (n - 1 - j) * (n + j + 1) ** 2
    minus = (
        (n - j)
        * (n + j) ** 2
        * (n - 1 - j)
        * (n + j + 1) ** 2
    )
    return plus, zero, minus


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


def check_unit_reduction_identity() -> int:
    """Check that Lemma 1 implies Cartier descent on every unit digit."""

    checks = 0
    for prime in PRIMES:
        for level in (1, 2):
            for n in range(1, 5):
                high_n = n * prime**level
                low_n = high_n // prime
                modulus = prime ** (2 * level)
                for j in range(1, high_n):
                    if j % prime == 0:
                        continue
                    q = j // prime
                    assert Fraction(cartier_kernel(high_n, j)) == Fraction(
                        reduced_outer(high_n, j) * shifted_row(high_n - 1, j)
                    ) * (1 - Fraction(high_n, j))
                    model = cartier_kernel(low_n, q) * (
                        1 + Fraction(high_n, j)
                    ) * (1 - Fraction(high_n, j))
                    assert rational_valuation(
                        model - cartier_kernel(low_n, q), prime
                    ) >= 2 * level
                    assert (
                        cartier_kernel(high_n, j) - cartier_kernel(low_n, q)
                    ) % modulus == 0
                    checks += 1
    return checks


def check_recurrence_certificate() -> int:
    """Audit (8d)--(8i), including the simultaneous-induction budgets."""

    checks = 0
    for n in range(3, 41):
        for j in range(1, n - 1):
            row_previous = shifted_row(n - 1, j - 1)
            row_current = shifted_row(n - 1, j)
            row_next = shifted_row(n - 1, j + 1)
            middle = (j + 1) ** 2 + j**2 + n * (n - 1)
            assert (
                (j + 1) ** 2 * row_next
                - middle * row_current
                + j**2 * row_previous
                == 0
            )
            checks += 1

            plus, zero, minus = recurrence_coefficients(n, j)
            assert (
                plus * cartier_kernel(n, j + 1)
                + zero * cartier_kernel(n, j)
                + minus * cartier_kernel(n, j - 1)
                == 0
            )
            checks += 1

            polynomial = (
                -n**3
                - 3 * n**2 * j
                - n**2
                + n * j
                + n
                + 3 * j**3
                + 7 * j**2
                + 5 * j
                + 1
            )
            assert plus + zero + minus == -(n**3) * polynomial
            checks += 1

    cases = [
        (prime, level, n)
        for prime in PRIMES
        for level in (1, 2)
        for n in range(1, 5)
    ]
    cases += [(5, 3, 1)]
    for prime, level, n in cases:
        high_n = n * prime**level
        low_n = high_n // prime

        # This is the horizontal estimate (8g) after Cartier descent.
        for j in range(1, high_n):
            target = 2 * max(level - valuation(j, prime), 0)
            assert valuation(
                cartier_kernel(high_n, j) - cartier_kernel(high_n, j - 1),
                prime,
            ) >= target
            checks += 1

        # These are precisely the nontrivial t<R branches of (8i).
        for q in range(1, low_n):
            j = prime * q
            t = valuation(j, prime)
            if t >= level:
                continue
            plus, zero, minus = recurrence_coefficients(high_n, j)
            beta = Fraction(minus, zero)
            gamma = Fraction(plus + zero + minus, zero)
            assert rational_valuation(beta, prime) == 2 * t
            assert rational_valuation(gamma, prime) == 3 * level - t
            checks += 2

            previous = cartier_kernel(high_n, j - 1)
            current = cartier_kernel(high_n, j)
            following = cartier_kernel(high_n, j + 1)
            assert Fraction(current - following) == (
                -beta * (previous - following) - gamma * following
            )
            assert valuation(previous - following, prime) >= 2 * (level - t)
            assert valuation(current - following, prime) >= 2 * level
            assert valuation(
                current - cartier_kernel(low_n, q), prime
            ) >= 2 * level
            checks += 4

    return checks


def check_scaled_boundary() -> int:
    """Test the now-proved scaled congruence (8b), including level three."""

    checks = 0
    cases = [
        (prime, level, n)
        for prime in PRIMES
        for level in (1, 2)
        for n in range(1, 5)
    ]
    cases += [(5, 3, 1)]
    for prime, level, n in cases:
        high_n = n * prime**level
        low_n = high_n // prime
        modulus = prime ** (2 * level)
        for q in range(low_n):
            assert (
                cartier_kernel(high_n, prime * q) - cartier_kernel(low_n, q)
            ) % modulus == 0
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
    unit_reduction = check_unit_reduction_identity()
    recurrence = check_recurrence_certificate()
    scaled_boundary = check_scaled_boundary()
    towers, sharp = check_shells_and_towers()
    total = (
        reciprocal
        + first_order
        + descent
        + unit_reduction
        + recurrence
        + scaled_boundary
        + towers
    )
    print(f"reciprocal block checks: {reciprocal}")
    print(f"first-order factorization checks: {first_order}")
    print(f"Cartier-kernel descent checks: {descent}")
    print(f"unit-digit reduction checks: {unit_reduction}")
    print(f"recurrence-certificate checks: {recurrence}")
    print(f"scaled-boundary checks: {scaled_boundary}")
    print(f"shell and tower checks: {towers} ({sharp} sharp)")
    print(f"all {total} A376466 ordinary-tower checks passed")


if __name__ == "__main__":
    main()
