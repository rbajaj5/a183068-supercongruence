"""Exact checks for BinomialQuotientCancellation.md.

The script is a transcription and regression checker.  The proof is in the
companion Markdown note.
"""

from __future__ import annotations

import math
from fractions import Fraction


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


def fraction_valuation(value: Fraction, p: int) -> int:
    return rational_valuation(value.numerator, value.denominator, p)


def integer_binomial(top: int, lower: int) -> int:
    """Integral extension of binomial(top, lower) to every integer top."""
    if top >= 0:
        return math.comb(top, lower) if top >= lower else 0
    return (-1) ** lower * math.comb(lower - top - 1, lower)


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


def unit_block(p: int, r: int, parameter: int) -> Fraction:
    modulus = p**r
    out = Fraction(1)
    for u in range(1, modulus):
        if u % p:
            out *= Fraction(u + parameter * modulus, u)
    return out


def check_universal_quotient_cancellation() -> tuple[int, int]:
    checks = 0
    equality_cases = 0
    parameters = range(-3, 6)
    for p in (3, 5, 7):
        for r in (2, 3):
            blocks = {t: unit_block(p, r, t) - 1 for t in parameters}
            required = 3 * r + (2 if p == 3 else 3)
            for a in parameters:
                for b in parameters:
                    difference = (
                        b * (b + 1) * blocks[a]
                        - a * (a + 1) * blocks[b]
                    )
                    got = fraction_valuation(difference, p)
                    assert got >= required
                    checks += 1
                    if got == required:
                        equality_cases += 1
    assert equality_cases > 0
    return checks, equality_cases


def a357509_family(j: int, k: int, n: int) -> int:
    return (
        k * k * (k - 1) * integer_binomial(j * n, n)
        - j * j * (j - 1) * integer_binomial(k * n, n)
    )


def check_a357509_family() -> tuple[int, int]:
    checks = 0
    equality_cases = 0
    for p in (5, 7, 11):
        for r in (2, 3):
            for j in range(-5, 9):
                for k in range(-5, 9):
                    difference = (
                        a357509_family(j, k, p**r)
                        - a357509_family(j, k, p ** (r - 1))
                    )
                    got = valuation(difference, p)
                    assert got >= 3 * r + 3
                    checks += 1
                    if got == 3 * r + 3:
                        equality_cases += 1
    assert equality_cases > 0
    return checks, equality_cases


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
    universal_checks, universal_equalities = check_universal_quotient_cancellation()
    a357509_checks, a357509_equalities = check_a357509_family()
    quotient_checks, family_checks, equality_cases = check_enhanced_family()
    total = (
        factorization_checks
        + tower_checks
        + universal_checks
        + a357509_checks
        + quotient_checks
        + family_checks
    )
    print("Binomial-quotient cancellation checks passed")
    print(f"A364506 factorizations: {factorization_checks}")
    print(f"A364506 tower instances: {tower_checks}")
    print(f"universal quotient-cancellation instances: {universal_checks}")
    print(f"sharp universal quotient instances: {universal_equalities}")
    print(f"A357509 two-parameter instances: {a357509_checks}")
    print(f"sharp A357509 instances: {a357509_equalities}")
    print(f"quotient-cancellation instances: {quotient_checks}")
    print(f"A357568-family instances: {family_checks}")
    print(f"sharp A357568-family instances: {equality_cases}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
