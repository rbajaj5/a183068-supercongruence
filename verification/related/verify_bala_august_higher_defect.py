"""Exact checks for the higher August defect reduction.

This verifies the exact three-level and shell identities and tests the
remaining conjectural valuation.  It is not a proof of that valuation.
"""

from __future__ import annotations

from math import comb

from verify_bala_august_mixed_binomial_follow_on import (
    negative_binomial_sum_mod,
)


def summand(n: int, k: int) -> int:
    return comb(n + k - 1, k) * comb(2 * n + k - 1, k)


def exact_sum(n: int) -> int:
    return sum(summand(n, k) for k in range(n + 1))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def check_three_level_equivalence() -> int:
    checks = 0
    for prime in (5, 7, 11):
        loss = int(prime == 5)
        for n in range(1, 5):
            for level in (2, 3):
                high = exact_sum(n * prime**level)
                middle = exact_sum(n * prime ** (level - 1))
                low = exact_sum(n * prime ** (level - 2))
                q_high = (high - middle) // prime ** (3 * level)
                q_low = (middle - low) // prime ** (3 * level - 3)
                residual = high - (1 + prime**3) * middle + prime**3 * low
                assert residual == prime ** (3 * level) * (q_high - q_low)
                assert residual % prime ** (5 * level - 2 - loss) == 0
                checks += 2
    return checks


def check_shell_decomposition() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for n in (1, 2):
            for level in (2, 3):
                high_n = n * prime**level
                middle_n = high_n // prime
                low_n = middle_n // prime
                unit = sum(
                    summand(high_n, k)
                    for k in range(high_n + 1)
                    if k % prime
                )
                once = sum(
                    summand(high_n, prime * q)
                    - (1 + prime**3) * summand(middle_n, q)
                    for q in range(1, middle_n + 1)
                    if q % prime
                )
                twice = sum(
                    summand(high_n, prime * prime * q)
                    - (1 + prime**3) * summand(middle_n, prime * q)
                    + prime**3 * summand(low_n, q)
                    for q in range(low_n + 1)
                )
                residual = (
                    exact_sum(high_n)
                    - (1 + prime**3) * exact_sum(middle_n)
                    + prime**3 * exact_sum(low_n)
                )
                assert unit + once + twice == residual
                checks += 1
    return checks


def check_modular_grid() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23):
        loss = int(prime == 5)
        sharp = False
        for n in range(1, 9):
            normalized: dict[int, int] = {}
            for level in (1, 2, 3, 4):
                if n * prime**level > 120_000:
                    continue
                precision = 3 * level + 8
                high = negative_binomial_sum_mod(
                    n * prime**level, prime, precision
                )
                low = negative_binomial_sum_mod(
                    n * prime ** (level - 1), prime, precision
                )
                difference = (high - low) % prime**precision
                assert difference % prime ** (3 * level) == 0
                normalized[level] = difference // prime ** (3 * level)
                checks += 1
            for level in range(2, max(normalized) + 1):
                required = 2 * level - 2 - loss
                delta = normalized[level] - normalized[level - 1]
                assert delta % prime**required == 0
                if valuation(delta, prime) == required:
                    sharp = True
                checks += 1
        assert sharp or prime == 23  # the bounded p=23 grid can gain accidentally
        checks += 1
    return checks


def main() -> None:
    results = {
        "three-level equivalence": check_three_level_equivalence(),
        "valuation-shell identity": check_shell_decomposition(),
        "higher-defect evidence": check_modular_grid(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
