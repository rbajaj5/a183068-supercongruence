"""Exact checks for A008793CubePlanePartitionTower.md."""

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
def cube_partitions(n: int) -> int:
    if n == 0:
        return 1
    return (
        hyperfactorial(n) ** 3
        * hyperfactorial(3 * n)
        // hyperfactorial(2 * n) ** 3
    )


def paired_product(n: int) -> Fraction:
    out = Fraction(2**n)
    for s in range(1, n):
        out *= Fraction(
            (s + n) * (3 * n - s), s * (2 * n - s)
        ) ** s
    return out


def residual_unit(prime: int, n: int) -> Fraction:
    out = Fraction(1)
    for s in range(1, prime * n):
        if s % prime:
            out *= Fraction(
                (s + prime * n) * (3 * prime * n - s),
                s * (2 * prime * n - s),
            ) ** s
    return out


def digit_sum(n: int) -> int:
    return n.bit_count()


def cumulative_digit_sum(n: int) -> int:
    return sum(digit_sum(k) for k in range(n))


def predicted_binary_valuation(n: int) -> int:
    return (
        3 * cumulative_digit_sum(n)
        + 3 * n
        - cumulative_digit_sum(3 * n)
    )


def main() -> None:
    initial = [
        1,
        2,
        20,
        980,
        232848,
        267227532,
        1478619421136,
        39405996318420160,
    ]
    initial_checks = 0
    for n, expected in enumerate(initial):
        assert cube_partitions(n) == expected
        initial_checks += 1

    pairing_checks = 0
    for n in range(1, 20):
        paired = paired_product(n)
        assert paired.denominator == 1
        assert paired.numerator == cube_partitions(n)
        pairing_checks += 1
        for prime in (2, 3, 5, 7):
            residual = residual_unit(prime, n)
            assert Fraction(cube_partitions(prime * n), cube_partitions(n) ** prime) == residual
            pairing_checks += 1

    odd_block_checks = 0
    for prime in (3, 5, 7, 11):
        epsilon = 1 if prime == 3 else 0
        for r in (1, 2, 3):
            q = prime**r
            for c in range(0, 7):
                block = sum(
                    (
                        Fraction(1, c * q + u)
                        for u in range(1, q)
                        if u % prime
                    ),
                    Fraction(0),
                )
                assert valuation_fraction(block, prime) >= 2 * r - epsilon
                odd_block_checks += 1

    binary_block_checks = 0
    for t in range(0, 8):
        q = 2 ** (t + 1)
        for c in range(0, 8):
            block = sum(
                (
                    Fraction(1, c * q + 2 * a + 1)
                    for a in range(2**t)
                ),
                Fraction(0),
            )
            assert valuation_fraction(block, 2) >= 2 * t
            binary_block_checks += 1

    binary_valuation_checks = 0
    for n in range(1, 65):
        actual = valuation_int(cube_partitions(n), 2)
        assert actual == predicted_binary_valuation(n)
        assert actual >= 1
        if 2 * n <= 64:
            assert valuation_int(cube_partitions(2 * n), 2) == 2 * actual
        binary_valuation_checks += 1

    residual_checks = 0
    for prime in (2, 3, 5, 7):
        for r in (1, 2, 3):
            for n in range(1, 7):
                lower = n * prime ** (r - 1)
                if prime * lower > 180:
                    continue
                residual = residual_unit(prime, lower)
                if prime == 2:
                    t = valuation_int(lower, 2)
                    assert valuation_fraction(residual - 1, 2) >= 4 * t + 2
                else:
                    assert valuation_fraction(residual - 1, prime) >= 4 * r
                residual_checks += 1

    tower_checks = 0
    equality_witnesses: list[tuple[int, int, int, int]] = []
    for prime in (2, 3, 5, 7, 11):
        for r in (1, 2, 3):
            for n in range(1, 9):
                high_index = n * prime**r
                if high_index > 180:
                    continue
                low_index = n * prime ** (r - 1)
                difference = cube_partitions(high_index) - cube_partitions(
                    low_index
                ) ** prime
                actual = valuation_int(difference, prime)
                assert actual >= 4 * r
                if actual == 4 * r:
                    equality_witnesses.append((prime, n, r, actual))
                tower_checks += 1

    total = (
        initial_checks
        + pairing_checks
        + odd_block_checks
        + binary_block_checks
        + binary_valuation_checks
        + residual_checks
        + tower_checks
    )
    print("A008793 cube-plane-partition checks passed")
    print(f"initial sequence checks: {initial_checks}")
    print(f"pairing and residual identities: {pairing_checks}")
    print(f"odd reciprocal-block checks: {odd_block_checks}")
    print(f"binary reciprocal-block checks: {binary_block_checks}")
    print(f"binary valuation checks: {binary_valuation_checks}")
    print(f"residual-unit checks: {residual_checks}")
    print(f"full tower checks: {tower_checks}")
    print(f"first sharp witnesses: {equality_witnesses[:12]}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
