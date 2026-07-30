"""Exact checks for BinomialQuotientCancellation.md.

The script is a transcription and regression checker.  The proof is in the
companion Markdown note.
"""

from __future__ import annotations

import math


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def rational_valuation(num: int, den: int, p: int) -> int:
    return valuation(num, p) - valuation(den, p)


def t_a364506(row: int, n: int) -> int:
    num = (
        math.factorial(2 * n)
        * math.factorial(2 * row * n)
        * math.factorial((2 * row + 1) * n)
    )
    den = (
        math.factorial(n)
        * math.factorial(row * n) ** 2
        * math.factorial((row + 1) * n) ** 2
    )
    assert num % den == 0
    return num // den


def t_a364506_binomial(row: int, n: int) -> int:
    num = (
        math.comb(2 * n, n)
        * math.comb(2 * row * n, row * n)
        * math.comb((2 * row + 1) * n, row * n)
    )
    den = math.comb((row + 1) * n, row * n)
    assert num % den == 0
    return num // den


def check_a364506() -> tuple[int, int]:
    factorization_checks = 0
    tower_checks = 0

    for row in range(7):
        for n in range(1, 18):
            assert t_a364506(row, n) == t_a364506_binomial(row, n)
            factorization_checks += 1

    for p in (5, 7, 11):
        for row in range(6):
            for m in range(1, 5):
                for r in range(1, 4):
                    high = t_a364506(row, m * p**r)
                    low = t_a364506(row, m * p ** (r - 1))
                    assert (high - low) % p ** (3 * r) == 0
                    tower_checks += 1

    return factorization_checks, tower_checks


def quotient_relation_valuation(p: int, r: int) -> int:
    high = p**r
    low = p ** (r - 1)
    b2_high = math.comb(2 * high, high)
    b2_low = math.comb(2 * low, low)
    b3_high = math.comb(3 * high, high)
    b3_low = math.comb(3 * low, low)

    # (b3_high / b3_low - 1) - 3*(b2_high / b2_low - 1)
    num = (
        b3_high * b2_low
        - 3 * b2_high * b3_low
        + 2 * b3_low * b2_low
    )
    den = b3_low * b2_low
    return rational_valuation(num, den, p)


def a_family(k: int, n: int) -> int:
    return (
        9 * math.comb(2 * n, n) ** k
        - k * 2**k * math.comb(3 * n, n)
    )


def check_enhanced_family() -> tuple[int, int, int]:
    quotient_checks = 0
    family_checks = 0
    equality_cases = 0

    for p in (3, 5, 7, 11, 13):
        for r in range(2, 5):
            got = quotient_relation_valuation(p, r)
            required = 3 * r + (2 if p == 3 else 3)
            assert got >= required
            quotient_checks += 1

            for k in range(1, 13):
                difference = a_family(k, p**r) - a_family(k, p ** (r - 1))
                got_family = valuation(difference, p)
                required_family = 3 * r + 3
                assert got_family >= required_family
                family_checks += 1
                if got_family == required_family:
                    equality_cases += 1

    assert equality_cases > 0
    return quotient_checks, family_checks, equality_cases


def main() -> None:
    factorization_checks, tower_checks = check_a364506()
    quotient_checks, family_checks, equality_cases = check_enhanced_family()
    total = factorization_checks + tower_checks + quotient_checks + family_checks
    print("Binomial-quotient cancellation checks passed")
    print(f"A364506 factorizations: {factorization_checks}")
    print(f"A364506 tower instances: {tower_checks}")
    print(f"quotient-cancellation instances: {quotient_checks}")
    print(f"A357568-family instances: {family_checks}")
    print(f"sharp A357568-family instances: {equality_cases}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
