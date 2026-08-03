"""Exact checks for BoberSporadicFactorialRatioPacket.md.

Finite checks catch transcription errors and search for counterexamples.
The Markdown note contains the general proofs.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial, prod


# Numerator and denominator coefficient vectors from A295431/a295431.txt.
BOBER_52 = (
    ("A295431", ([12, 1], [6, 4, 3])),
    ("A295432", ([12, 3, 2], [6, 6, 4, 1])),
    ("A295433", ([12, 1], [8, 3, 2])),
    ("A295434", ([12, 3], [8, 6, 1])),
    ("A295435", ([12, 3], [6, 5, 4])),
    ("A295436", ([12, 5], [10, 4, 3])),
    ("A295437", ([18, 1], [9, 6, 4])),
    ("A295438", ([9, 2], [6, 4, 1])),
    ("A295439", ([9, 4], [8, 3, 2])),
    ("A295440", ([18, 4, 3], [9, 8, 6, 2])),
    ("A295441", ([9, 1], [5, 3, 2])),
    ("A295442", ([18, 5, 3], [10, 9, 6, 1])),
    ("A295443", ([18, 4], [12, 9, 1])),
    ("A295444", ([12, 2], [9, 4, 1])),
    ("A295445", ([18, 2], [9, 6, 5])),
    ("A295446", ([10, 6], [9, 5, 2])),
    ("A295447", ([14, 3], [9, 7, 1])),
    ("A295448", ([18, 3, 2], [9, 7, 6, 1])),
    ("A295449", ([12, 2], [7, 4, 3])),
    ("A295450", ([14, 6, 4], [12, 7, 3, 2])),
    ("A295451", ([14, 1], [7, 5, 3])),
    ("A295452", ([10, 6, 1], [7, 5, 3, 2])),
    ("A295453", ([15, 1], [9, 5, 2])),
    ("A295454", ([30, 9, 5], [18, 15, 10, 1])),
    ("A295455", ([15, 4], [12, 5, 2])),
    ("A295456", ([30, 5, 4], [15, 12, 10, 2])),
    ("A295457", ([15, 4], [8, 6, 5])),
    ("A295458", ([30, 5, 4], [15, 10, 8, 6])),
    ("A295459", ([15, 2], [10, 4, 3])),
    ("A295460", ([30, 3, 2], [15, 10, 6, 4])),
    ("A295461", ([30, 1], [15, 10, 6])),
    ("A295462", ([15, 2], [10, 6, 1])),
    ("A295463", ([15, 7], [14, 5, 3])),
    ("A295464", ([30, 5, 3], [15, 10, 7, 6])),
    ("A295465", ([30, 5, 3], [15, 12, 10, 1])),
    ("A295466", ([15, 6, 1], [12, 5, 3, 2])),
    ("A295467", ([15, 1], [8, 5, 3])),
    ("A295468", ([30, 5, 3, 2], [15, 10, 8, 6, 1])),
    ("A295469", ([20, 3], [12, 10, 1])),
    ("A295470", ([20, 6, 1], [12, 10, 3, 2])),
    ("A295471", ([20, 1], [10, 8, 3])),
    ("A295472", ([20, 3, 2], [10, 8, 6, 1])),
    ("A295473", ([20, 1], [10, 7, 4])),
    ("A295474", ([20, 7, 2], [14, 10, 4, 1])),
    ("A295475", ([20, 3], [10, 9, 4])),
    ("A295476", ([20, 9, 6], [18, 10, 4, 3])),
    ("A295477", ([24, 1], [12, 8, 5])),
    ("A295478", ([24, 5, 2], [12, 10, 8, 1])),
    ("A295479", ([24, 4, 1], [12, 8, 7, 2])),
    ("A295480", ([24, 7, 4], [14, 12, 8, 1])),
    ("A295481", ([24, 4, 3], [12, 9, 8, 2])),
    ("A295482", ([24, 9, 6, 4], [18, 12, 8, 3, 2])),
)


# Fractional indices in approved OEIS comments visible on August 3, 2026.
FRACTIONAL = {
    "A295456": ([30, 5, 4], [15, 12, 10, 2], (2, 3)),
    "A295458": ([30, 5, 4], [15, 10, 8, 6], (2, 3)),
    "A295460": ([30, 3, 2], [15, 10, 6, 4], (2, 4)),
    "A295465": ([30, 5, 3], [15, 12, 10, 1], (2,)),
    "A295468": ([30, 5, 3, 2], [15, 10, 8, 6, 1], (2,)),
    "A295470": ([20, 6, 1], [12, 10, 3, 2], (2,)),
    "A295471": ([20, 1], [10, 8, 3], (2,)),
    "A295475": ([20, 3], [10, 9, 4], (2,)),
    "A295477": ([24, 1], [12, 8, 5], (2, 4)),
    "A295479": ([24, 4, 1], [12, 8, 7, 2], (2,)),
    "A295481": ([24, 4, 3], [12, 9, 8, 2], (2,)),
}


def factorial_ratio(numerators: list[int], denominators: list[int], n: int) -> int:
    top = prod(factorial(a * n) for a in numerators)
    bottom = prod(factorial(b * n) for b in denominators)
    assert top % bottom == 0
    return top // bottom


def laurent_binomial(numerators: list[int], denominators: list[int], n: int) -> Fraction:
    coefficients: defaultdict[int, int] = defaultdict(int)
    for a in numerators:
        coefficients[a] += 1
    for b in denominators:
        coefficients[b] -= 1
    maximum = max(coefficients)
    out = Fraction(1)
    for k in range(2, maximum + 1):
        exponent = sum(coefficients[m] for m in range(k, maximum + 1))
        out *= Fraction(comb(k * n, n)) ** exponent
    return out


def terms_for_fractional(
    numerators: list[int], denominators: list[int], q: int
) -> dict[Fraction, int]:
    terms: defaultdict[Fraction, int] = defaultdict(int)
    for a in numerators:
        terms[Fraction(a, q)] += 1
    for b in denominators:
        terms[Fraction(b, q)] -= 1
    return {slope: exponent for slope, exponent in terms.items() if exponent}


def rational_binomial(top: Fraction, bottom: int, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(bottom * n):
        out *= (top * n - j) / (j + 1)
    return out


def decompose_gamma_ratio(
    terms: dict[Fraction, int],
) -> tuple[dict[int, int], list[tuple[Fraction, int, int]]]:
    integer_factors: defaultdict[int, int] = defaultdict(int)
    classes: defaultdict[Fraction, tuple[list[Fraction], list[Fraction]]] = (
        defaultdict(lambda: ([], []))
    )
    for slope, exponent in terms.items():
        if slope.denominator == 1:
            integer_factors[int(slope)] += exponent
            continue
        residue = slope - int(slope)
        target = classes[residue][0 if exponent > 0 else 1]
        target.extend([slope] * abs(exponent))

    binomials: list[tuple[Fraction, int, int]] = []
    for positive, negative in classes.values():
        assert len(positive) == len(negative)
        for alpha, beta in zip(positive, negative, strict=True):
            if alpha > beta:
                distance = int(alpha - beta)
                binomials.append((alpha, distance, 1))
                integer_factors[distance] += 1
            elif beta > alpha:
                distance = int(beta - alpha)
                binomials.append((beta, distance, -1))
                integer_factors[distance] -= 1
    return dict(integer_factors), binomials


def evaluate_gamma_ratio(terms: dict[Fraction, int], n: int) -> Fraction:
    integer_factors, binomials = decompose_gamma_ratio(terms)
    out = Fraction(1)
    for slope, exponent in integer_factors.items():
        out *= Fraction(factorial(slope * n)) ** exponent
    for top, bottom, exponent in binomials:
        out *= rational_binomial(top, bottom, n) ** exponent
    return out


def vp_integer(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def vp(value: Fraction, p: int) -> int:
    return vp_integer(value.numerator, p) - vp_integer(value.denominator, p)


def check_bober_52() -> int:
    checks = 0
    assert len(BOBER_52) == 52
    assert [name for name, _ in BOBER_52] == [
        f"A{number}" for number in range(295431, 295483)
    ]
    checks += 2

    for name, (numerators, denominators) in BOBER_52:
        assert sum(numerators) == sum(denominators), name
        checks += 1
        for n in (1, 2):
            exact = factorial_ratio(numerators, denominators, n)
            factored = laurent_binomial(numerators, denominators, n)
            assert factored.denominator == 1
            assert factored.numerator == exact
            checks += 2
        for p in (5, 7):
            for r in (1, 2):
                high = factorial_ratio(numerators, denominators, p**r)
                low = factorial_ratio(numerators, denominators, p ** (r - 1))
                assert (high - low) % (p ** (3 * r)) == 0, (name, p, r)
                checks += 1
    return checks


def check_fractional_packet() -> int:
    checks = 0
    variants = 0
    for name, (numerators, denominators, denominators_q) in FRACTIONAL.items():
        for q in denominators_q:
            variants += 1
            terms = terms_for_fractional(numerators, denominators, q)
            assert sum(slope * exponent for slope, exponent in terms.items()) == 0
            checks += 1

            residues: defaultdict[Fraction, int] = defaultdict(int)
            for slope, exponent in terms.items():
                residue = slope - int(slope)
                if residue:
                    residues[residue] += exponent
            assert all(total == 0 for total in residues.values()), (name, q, residues)
            checks += len(residues)

            for n in range(31):
                value = evaluate_gamma_ratio(terms, n)
                assert value.denominator == 1, (name, q, n, value)
                checks += 1

            for p in (5, 7, 11):
                for r in (1, 2):
                    for n in (1, 2):
                        high = evaluate_gamma_ratio(terms, n * p**r)
                        low = evaluate_gamma_ratio(terms, n * p ** (r - 1))
                        assert vp(high - low, p) >= 3 * r, (name, q, p, r, n)
                        checks += 1

    assert variants == 15
    checks += 1
    return checks


def main() -> None:
    ordinary = check_bober_52()
    fractional = check_fractional_packet()
    print(f"Bober 52 checks passed: {ordinary}")
    print(f"fractional-index checks passed: {fractional}")
    print(f"all Bober packet checks passed: {ordinary + fractional}")


if __name__ == "__main__":
    main()
