"""Exact checks for SymmetricBoxPlanePartitionTower.md."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial


def valuation_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def valuation_fraction(value: Fraction, prime: int) -> int:
    return valuation_int(value.numerator, prime) - valuation_int(
        value.denominator, prime
    )


@lru_cache(maxsize=None)
def hyperfactorial(n: int) -> int:
    out = 1
    for k in range(1, n):
        out *= factorial(k)
    return out


@lru_cache(maxsize=None)
def symmetric_box(n: int, c: int) -> int:
    if n == 0:
        return 1
    return (
        hyperfactorial(n) ** 2
        * hyperfactorial(c * n)
        * hyperfactorial((c + 2) * n)
        // (
            hyperfactorial(2 * n)
            * hyperfactorial((c + 1) * n) ** 2
        )
    )


def paired_product(n: int, c: int) -> Fraction:
    out = Fraction((c + 1) ** n)
    for s in range(1, n):
        out *= Fraction(
            s * (2 * n - s) + c * (c + 2) * n * n,
            s * (2 * n - s),
        ) ** s
    return out


def residual_unit(prime: int, n: int, c: int) -> Fraction:
    out = Fraction(1)
    for s in range(1, prime * n):
        if s % prime:
            out *= Fraction(
                s * (2 * prime * n - s)
                + c * (c + 2) * prime * prime * n * n,
                s * (2 * prime * n - s),
            ) ** s
    return out


def main() -> None:
    a008793 = [1, 2, 20, 980, 232848, 267227532]
    a352656 = [1, 3, 105, 41580, 184225041, 9095857138368]
    a352657 = [1, 4, 336, 572572, 19571505408, 13365232267026024]
    initial_checks = 0
    for n, expected in enumerate(a008793):
        assert symmetric_box(n, 1) == expected
        initial_checks += 1
    for n, expected in enumerate(a352656):
        assert symmetric_box(n, 2) == expected
        initial_checks += 1
    for n, expected in enumerate(a352657):
        assert symmetric_box(n, 3) == expected
        initial_checks += 1

    identity_checks = 0
    for c in range(1, 7):
        for n in range(1, 15):
            paired = paired_product(n, c)
            assert paired.denominator == 1
            assert paired.numerator == symmetric_box(n, c)
            identity_checks += 1
            for prime in (2, 3, 5, 7):
                residual = residual_unit(prime, n, c)
                assert Fraction(
                    symmetric_box(prime * n, c),
                    symmetric_box(n, c) ** prime,
                ) == residual
                identity_checks += 1

    odd_interval_checks = 0
    for prime in (3, 5, 7, 11):
        for r in (1, 2, 3):
            q = prime**r
            for n in range(1, 9):
                reciprocal_sum = sum(
                    (
                        Fraction(1, value)
                        for value in range(n * q + 1, 2 * n * q)
                        if value % prime
                    ),
                    Fraction(0),
                )
                assert valuation_fraction(reciprocal_sum, prime) >= 2 * r
                odd_interval_checks += 1

    binary_block_checks = 0
    for t in range(0, 8):
        width = 2 ** (t + 1)
        for d in range(0, 8):
            reciprocal_sum = sum(
                (
                    Fraction(1, d * width + 2 * a + 1)
                    for a in range(2**t)
                ),
                Fraction(0),
            )
            assert valuation_fraction(reciprocal_sum, 2) >= 2 * t
            binary_block_checks += 1

    binary_parity_checks = 0
    for c in (1, 3, 5, 7):
        for n in range(1, 33):
            value = symmetric_box(n, c)
            assert value % 2 == 0
            if 2 * n <= 32:
                assert valuation_int(symmetric_box(2 * n, c), 2) == 2 * valuation_int(
                    value, 2
                )
            binary_parity_checks += 1

    tower_checks = 0
    sharp_witnesses: list[tuple[int, int, int, int, int]] = []
    for c in range(1, 7):
        for prime in (2, 3, 5, 7, 11):
            for r in (1, 2, 3):
                for n in range(1, 7):
                    high_index = n * prime**r
                    if high_index > 120:
                        continue
                    low_index = n * prime ** (r - 1)
                    difference = symmetric_box(
                        high_index, c
                    ) - symmetric_box(low_index, c) ** prime
                    actual = valuation_int(difference, prime)
                    assert actual >= 4 * r
                    if actual == 4 * r:
                        sharp_witnesses.append((c, prime, n, r, actual))
                    tower_checks += 1

    total = (
        initial_checks
        + identity_checks
        + odd_interval_checks
        + binary_block_checks
        + binary_parity_checks
        + tower_checks
    )
    print("symmetric-box plane-partition checks passed")
    print(f"initial sequence checks: {initial_checks}")
    print(f"paired and residual identities: {identity_checks}")
    print(f"odd reciprocal-interval checks: {odd_interval_checks}")
    print(f"binary reciprocal-block checks: {binary_block_checks}")
    print(f"binary parity and doubling checks: {binary_parity_checks}")
    print(f"full tower checks: {tower_checks}")
    print(f"first sharp witnesses: {sharp_witnesses[:12]}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
