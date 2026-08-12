"""Exact checks for A212334EnhancedPrimeCongruence.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def primes_through(limit: int) -> list[int]:
    primes: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % p for p in primes if p * p <= candidate):
            primes.append(candidate)
    return primes


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def apery_four(n: int) -> int:
    return sum((comb(n, k) * comb(n + k, k)) ** 2 for k in range(n + 1))


def a212334(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        comb(n, k) * comb(n - 1, k) * comb(n + k - 1, k) ** 2
        for k in range(n)
    )


def product_term(prime: int, k: int) -> Fraction:
    out = -Fraction(prime**3, k**3) * (1 - Fraction(prime, k))
    for j in range(1, k):
        out *= (1 - Fraction(prime**2, j**2)) ** 2
    return out


def harmonic(power: int, prime: int, modulus: int) -> int:
    return sum(pow(k, -power, modulus) for k in range(1, prime)) % modulus


def check_initial_values() -> int:
    expected = [1, 1, 9, 163, 3593, 87501, 2266155, 61211095]
    for n, value in enumerate(expected):
        assert a212334(n) == value
    return len(expected)


def check_prime_theorem() -> int:
    checks = 0
    for prime in primes_through(101):
        if prime < 5:
            continue
        value = a212334(prime)
        assert valuation(value - 1, prime) >= 5
        checks += 1
        for k in range(1, prime):
            direct = comb(prime, k) * comb(prime - 1, k)
            direct *= comb(prime + k - 1, k) ** 2
            assert product_term(prime, k) == direct
            checks += 1
        if prime >= 7:
            assert harmonic(3, prime, prime**2) == 0
            assert harmonic(4, prime, prime) == 0
            checks += 2
    assert a212334(5) - 1 == 87500 == 28 * 5**5
    checks += 1
    return checks


def check_apery_reduction() -> int:
    checks = 0
    for n in range(1, 24):
        assert 12 * a212334(n) == apery_four(n) + 7 * apery_four(n - 1)
        checks += 1

    for prime in (5, 7, 11):
        for depth in (1, 2):
            upper = prime**depth
            lower = prime ** (depth - 1)
            gamma = apery_four(upper) - apery_four(lower)
            delta = apery_four(upper - 1) - apery_four(lower - 1)

            # We do not assume the three conjectural relations here.  This
            # is the exact algebraic identity (10), with arbitrary alpha,
            # beta values sampled from the companion Apéry sequence.
            def apery_three(n: int) -> int:
                return sum(
                    comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1)
                )

            alpha = apery_three(upper) - apery_three(lower)
            beta = apery_three(upper - 1) - apery_three(lower - 1)
            left = 5 * (gamma + 7 * delta)
            right = (
                (5 * gamma - 14 * alpha)
                + 7 * (5 * delta - 2 * beta)
                + 14 * (alpha + beta)
            )
            assert left == right
            assert gamma + 7 * delta == 12 * (
                a212334(upper) - a212334(lower)
            )
            target = 5 if depth == 1 else 3 * depth + 3
            assert valuation(a212334(upper) - a212334(lower), prime) >= target
            checks += 3
    return checks


def main() -> None:
    initial = check_initial_values()
    prime = check_prime_theorem()
    reduction = check_apery_reduction()
    total = initial + prime + reduction
    print("A212334 enhanced-prime checks passed")
    print(f"initial-value checks: {initial}")
    print(f"prime-level checks: {prime}")
    print(f"Apéry-reduction checks: {reduction}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
