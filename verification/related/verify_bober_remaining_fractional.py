"""Exact checks for BoberRemainingFractionalIntegralityTowers.md.

The Markdown note contains the proof.  This checker reconstructs the four
remaining gamma ratios, tests the coprime-modulus Landau transfer, and checks
the exact denominator-prime valuation formulas.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd

from verify_bober_sporadic_packet import (
    FRACTIONAL,
    evaluate_gamma_ratio,
    terms_for_fractional,
    vp,
)


TARGETS = {
    "A295456": 3,
    "A295458": 3,
    "A295460": 4,
    "A295477": 4,
}


def original_landau(
    numerators: list[int], denominators: list[int], t: int, d: int
) -> int:
    return sum(a * t // d for a in numerators) - sum(
        a * t // d for a in denominators
    )


def progression_defect(
    numerators: list[int], denominators: list[int], q: int, n: int, d: int
) -> int:
    """Legendre defect of the generalized q-factorials at modulus d."""

    m, residue = divmod(n, q)
    out = 0
    for exponent, coefficients in ((1, numerators), (-1, denominators)):
        for a in coefficients:
            k = a * m + (a * residue) // q
            rho = (a * residue) % q
            out += exponent * sum(
                (q * j + rho) % d == 0 for j in range(1, k + 1)
            )
    return out


def transfer_argument(q: int, n: int, d: int) -> int:
    m, residue = divmod(n, q)
    c = next(c for c in range(d) if (q * c - residue) % d == 0)
    return m + c


def factorial_valuation_ratio(
    positive: list[int], negative: list[int], prime: int
) -> int:
    value = Fraction(1)
    for argument in positive:
        value *= factorial(argument)
    for argument in negative:
        value /= factorial(argument)
    return vp(value, prime)


def denominator_prime_prediction(name: str, n: int) -> int:
    """The exact displayed valuation formula at 3 or 2."""

    if name == "A295456":
        return n + factorial_valuation_ratio([10 * n], [5 * n, 4 * n], 3)
    if name == "A295458":
        return 3 * n + factorial_valuation_ratio([10 * n], [5 * n, 2 * n], 3)
    if name == "A295460" and n % 2:
        return 2 * n - factorial_valuation_ratio([n], [], 2)
    if name == "A295460":
        s = n // 2
        return 3 * n + factorial_valuation_ratio(
            [15 * s, s], [5 * s, 3 * s, 2 * s], 2
        )
    assert name == "A295477"
    bonus = 2 * n if n % 2 else n
    return bonus + factorial_valuation_ratio([6 * n], [3 * n, 2 * n], 2)


def check_symbolic_hypotheses() -> int:
    checks = 0
    for name, q in TARGETS.items():
        numerators, denominators, indices = FRACTIONAL[name]
        assert q in indices
        assert sum(numerators) == sum(denominators)
        checks += 2
        for residue in range(1, q):
            assert sum(a % q == residue for a in numerators) == sum(
                a % q == residue for a in denominators
            )
            checks += 1
    return checks


def check_coprime_landau_transfer() -> int:
    checks = 0
    for name, q in TARGETS.items():
        numerators, denominators, _ = FRACTIONAL[name]
        for d in range(2, 102):
            if gcd(d, q) != 1:
                continue
            for n in range(1, 2 * q * d + 1):
                t = transfer_argument(q, n, d)
                assert progression_defect(
                    numerators, denominators, q, n, d
                ) == original_landau(numerators, denominators, t, d)
                checks += 1
    return checks


def check_values_and_boundary_valuations() -> int:
    checks = 0
    for name, q in TARGETS.items():
        numerators, denominators, _ = FRACTIONAL[name]
        terms = terms_for_fractional(numerators, denominators, q)
        prime = 3 if q == 3 else 2
        for n in range(101):
            value = evaluate_gamma_ratio(terms, n)
            assert value.denominator == 1
            checks += 1
            if n % q:
                predicted = denominator_prime_prediction(name, n)
                assert vp(value, prime) == predicted >= 0
                checks += 2
    return checks


def check_cubic_towers() -> int:
    checks = 0
    for name, q in TARGETS.items():
        numerators, denominators, _ = FRACTIONAL[name]
        terms = terms_for_fractional(numerators, denominators, q)
        for prime in (5, 7, 11):
            for r, maximum_n in ((1, 4), (2, 2)):
                for n in range(1, maximum_n + 1):
                    high = evaluate_gamma_ratio(terms, n * prime**r)
                    low = evaluate_gamma_ratio(terms, n * prime ** (r - 1))
                    assert high.denominator == low.denominator == 1
                    assert vp(high - low, prime) >= 3 * r
                    checks += 2
    return checks


def main() -> None:
    sections = {
        "symbolic hypotheses": check_symbolic_hypotheses(),
        "coprime-modulus Landau transfer": check_coprime_landau_transfer(),
        "exact values and boundary valuations": check_values_and_boundary_valuations(),
        "cubic towers": check_cubic_towers(),
    }
    print(f"Remaining Bober fractional checks passed: {sum(sections.values())}")
    for label, count in sections.items():
        print(f"  {label}: {count}")


if __name__ == "__main__":
    main()
