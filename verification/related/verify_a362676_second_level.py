"""Exact checks for the A362676 second-level reduction.

The proof companion checks the scaled-index transfer modulo p^6, the
explicit one-digit block expansion, the second-digit scaling table, and the
resulting two-digit superblock cancellation.
"""

from __future__ import annotations

from functools import cache
from math import comb


PRIMES = (5, 7, 11, 13, 17, 19)
N_LIMIT = 5


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def unit_ratio_mod(numerator: int, denominator: int, p: int, modulus: int) -> int:
    """Return a p-adic unit quotient modulo a power of p."""
    numerator_v = valuation(numerator, p)
    denominator_v = valuation(denominator, p)
    assert numerator_v == denominator_v
    numerator //= p**numerator_v
    denominator //= p**denominator_v
    return numerator * pow(denominator, -1, modulus) % modulus


@cache
def term(n: int, k: int) -> int:
    return (
        comb(n + k - 1, k)
        * comb(2 * (n - k), n - k)
        * comb(2 * k, k)
    )


@cache
def sequence(n: int) -> int:
    return sum(term(n, k) for k in range(n + 1))


def c_minus(n: int, a: int) -> int:
    return (
        n
        * (n - a)
        * comb(n + a, a)
        * comb(2 * a, a)
        * comb(2 * (n - a), n - a)
    )


def c_plus(n: int, a: int) -> int:
    return (
        n
        * (a + 1)
        * comb(n + a, a)
        * comb(2 * a + 2, a + 1)
        * comb(2 * (n - a - 1), n - a - 1)
    )


def d_minus(m: int, j: int) -> int:
    return (
        m
        * (m - j)
        * comb(m + j, j)
        * comb(2 * j, j)
        * comb(2 * (m - j), m - j)
    )


def d_plus(m: int, j: int) -> int:
    return (
        m
        * (j + 1)
        * comb(m + j, j)
        * comb(2 * j + 2, j + 1)
        * comb(2 * (m - j - 1), m - j - 1)
    )


def blocks(n: int, p: int) -> list[int]:
    """Return all one-digit unit blocks at N=n*p^2."""
    big_n = n * p * p
    return [
        sum(term(big_n, j * p + b) for b in range(1, p))
        for j in range(n * p)
    ]


def check_scaled_transfer() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for p in PRIMES:
        modulus = p**6
        for n in range(1, N_LIMIT + 1):
            lower_n = n * p
            upper_n = lower_n * p
            for k in range(lower_n + 1):
                delta = term(upper_n, p * k) - term(lower_n, k)
                assert delta % modulus == 0
                if delta and valuation(delta, p) == 6:
                    sharp += 1
                checks += 1
    return checks, sharp


def check_central_cubic_quotient() -> int:
    checks = 0
    for p in PRIMES:
        modulus = p**4
        q_one = unit_ratio_mod(comb(2 * p, p), 2, p, modulus)
        assert (q_one - 1) % (p**3) == 0
        kappa = (q_one - 1) // (p**3) % p

        for x in range(1, 2 * p + 2):
            quotient = unit_ratio_mod(
                comb(2 * p * x, p * x), comb(2 * x, x), p, modulus
            )
            expected = 1 + kappa * p**3 * x**3
            assert (quotient - expected) % modulus == 0
            checks += 1
    return checks


def check_carry_budget() -> int:
    """Audit the two base-level carries used in the unit-index proof."""
    checks = 0
    for p in PRIMES:
        for n in range(1, N_LIMIT + 1):
            lower_n = n * p
            for k in range(1, lower_n):
                if k % p == 0:
                    continue
                assert valuation(comb(lower_n + k - 1, k), p) >= 1
                central_v = valuation(comb(2 * k, k), p)
                central_v += valuation(
                    comb(2 * (lower_n - k), lower_n - k), p
                )
                assert central_v >= 1
                assert valuation(term(lower_n, k), p) >= 2
                checks += 1
    return checks


def check_blocks_and_residue_law() -> tuple[int, int, int, int, int, int]:
    block_checks = 0
    block_expansion_checks = 0
    scaling_table_checks = 0
    superblock_checks = 0
    residue_checks = 0
    theorem_checks = 0

    for p in PRIMES:
        h = (p - 1) // 2
        half_h2 = sum(pow(b * b, -1, p * p) for b in range(1, h + 1))
        half_h2 %= p * p
        assert half_h2 % p == 0
        alpha_p = half_h2 // p % p
        beta_p = sum(pow(b**3, -1, p) for b in range(1, h + 1)) % p
        mu_p = (-alpha_p - beta_p) % p

        for n in range(1, N_LIMIT + 1):
            current = blocks(n, p)
            middle_n = n * p
            for j, block in enumerate(current):
                assert block % (p**5) == 0
                block_checks += 1
                dm = d_minus(middle_n, j)
                dp = d_plus(middle_n, j)
                assert dm % (p**2) == 0
                assert dp % (p**2) == 0
                predicted = mu_p * p**3 * (dm - dp)
                assert (block - predicted) % (p**6) == 0
                block_expansion_checks += 1

            for a in range(n):
                superblock = sum(current[a * p : (a + 1) * p])
                assert superblock % (p**6) == 0
                superblock_checks += 1

                low = c_minus(n, a) % p
                high = c_plus(n, a) % p
                for c in range(p):
                    j = a * p + c
                    dm = d_minus(middle_n, j) // (p**2) % p
                    dp = d_plus(middle_n, j) // (p**2) % p
                    if c < h:
                        assert dm == low
                        assert dp == (-low) % p
                    elif c == h:
                        assert dm == low
                        assert dp == high
                    else:
                        assert dm == (-high) % p
                        assert dp == high
                    scaling_table_checks += 1

                    actual = current[a * p + c] // (p**5) % p
                    if c < h:
                        expected = 2 * mu_p * low
                    elif c == h:
                        expected = mu_p * (low - high)
                    else:
                        expected = -2 * mu_p * high
                    assert actual == expected % p
                    residue_checks += 1

            delta = sequence(n * p * p) - sequence(n * p)
            assert delta % (p**6) == 0
            theorem_checks += 1

    return (
        block_checks,
        block_expansion_checks,
        scaling_table_checks,
        superblock_checks,
        residue_checks,
        theorem_checks,
    )


def check_local_unit_term_expansions() -> int:
    """Audit equations (16) and (17) before the reciprocal sums are taken."""
    checks = 0
    for p in PRIMES:
        modulus = p**6
        h = (p - 1) // 2
        for n in range(1, N_LIMIT + 1):
            middle_n = n * p
            upper_n = middle_n * p
            for j in range(middle_n):
                dm = d_minus(middle_n, j)
                dp = d_plus(middle_n, j)
                for b in range(1, h + 1):
                    lower_denominator = (b + p * j) ** 2
                    lower_expected = (
                        -p**2
                        * dm
                        * pow(lower_denominator, -1, modulus)
                    )
                    assert (
                        term(upper_n, p * j + b) - lower_expected
                    ) % modulus == 0
                    checks += 1

                    upper_denominator = (b - p * (j + 1)) ** 2
                    upper_expected = (
                        p**2
                        * dp
                        * pow(upper_denominator, -1, modulus)
                    )
                    assert (
                        term(upper_n, p * (j + 1) - b) - upper_expected
                    ) % modulus == 0
                    checks += 1
    return checks


def check_exact_reduction() -> int:
    checks = 0
    for p in PRIMES:
        modulus = p**6
        for n in range(1, N_LIMIT + 1):
            upper_n = n * p * p
            lower_n = n * p
            unit_shell = sum(
                term(upper_n, k)
                for k in range(upper_n + 1)
                if k % p != 0
            )
            delta = sequence(upper_n) - sequence(lower_n)
            assert (delta - unit_shell) % modulus == 0

            scaled_error = sum(
                term(upper_n, p * k) - term(lower_n, k)
                for k in range(lower_n + 1)
            )
            assert delta == unit_shell + scaled_error
            assert scaled_error % modulus == 0
            checks += 1
    return checks


def main() -> None:
    transfer_checks, sharp_transfers = check_scaled_transfer()
    central_quotient_checks = check_central_cubic_quotient()
    carry_checks = check_carry_budget()
    local_term_checks = check_local_unit_term_expansions()
    (
        block_checks,
        block_expansion_checks,
        scaling_table_checks,
        superblock_checks,
        residue_checks,
        theorem_checks,
    ) = check_blocks_and_residue_law()
    reduction_checks = check_exact_reduction()

    print("A362676 second-level verification passed")
    print(f"scaled-index transfer checks: {transfer_checks}")
    print(f"sharp scaled-index transfers: {sharp_transfers}")
    print(f"central cubic-quotient checks: {central_quotient_checks}")
    print(f"two-carry budget checks: {carry_checks}")
    print(f"local unit-term expansion checks: {local_term_checks}")
    print(f"one-digit p^5 block checks: {block_checks}")
    print(f"explicit block-expansion checks: {block_expansion_checks}")
    print(f"second-digit scaling-table checks: {scaling_table_checks}")
    print(f"two-digit p^6 superblock checks: {superblock_checks}")
    print(f"piecewise residue-law checks: {residue_checks}")
    print(f"exact reduction checks: {reduction_checks}")
    print(f"direct r=2 theorem checks: {theorem_checks}")


if __name__ == "__main__":
    main()
