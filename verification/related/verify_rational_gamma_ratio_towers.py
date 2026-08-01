"""Exact checks for RationalGammaRatioCubicTowers.md.

The checks catch transcription errors; the Markdown note contains the proof.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial


PRIMES = (5, 7, 11, 13)


def vp_int(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def vp(x: Fraction, p: int) -> int:
    return vp_int(x.numerator, p) - vp_int(x.denominator, p)


def rational_binomial(a: int, b: int, q: int, n: int) -> Fraction:
    """Return binomial(a*n/q, b*n) by its finite product."""
    top = Fraction(a * n, q)
    out = Fraction(1)
    for j in range(b * n):
        out *= (top - j) / (j + 1)
    return out


def reduced_product(a: int, b: int, q: int, n: int, p: int) -> Fraction:
    out = Fraction(1)
    for j in range(1, b * n):
        if j % p:
            out *= 1 - Fraction(a * n, q * j)
    return out


def check_rational_binomial_transfer() -> int:
    checks = 0
    for q in range(2, 8):
        for a in range(q + 1, 4 * q + 1):
            for b in range(1, a // q + 1):
                if a <= b * q:
                    continue
                for p in PRIMES:
                    if q % p == 0:
                        continue
                    for m in range(1, 8):
                        n = p * m
                        ratio = rational_binomial(a, b, q, n) / rational_binomial(
                            a, b, q, m
                        )
                        assert ratio == reduced_product(a, b, q, n, p)
                        assert vp(ratio - 1, p) >= 3 * vp_int(n, p)
                        checks += 2
    return checks


def a364175(n: int) -> Fraction:
    ordinary = Fraction(
        factorial(6 * n),
        factorial(3 * n) * factorial(2 * n) * factorial(n),
    )
    return ordinary / rational_binomial(5, 1, 3, n)


def check_a364175() -> int:
    known = (
        1,
        36,
        3564,
        408408,
        49697388,
        6249195036,
        802241960520,
    )
    assert tuple(a364175(n) for n in range(len(known))) == known
    checks = len(known)
    for p in PRIMES:
        for r in (1, 2):
            for n in range(1, 5):
                high = a364175(n * p**r)
                low = a364175(n * p ** (r - 1))
                assert high.denominator == low.denominator == 1
                assert vp(high - low, p) >= 3 * r
                checks += 1
    return checks


# Slope/exponent data copied from the live OEIS records on July 31, 2026.
PACKET: dict[str, dict[Fraction, int]] = {
    "A364172": {Fraction(6): 1, Fraction(1, 3): 1, Fraction(3): -1, Fraction(2): -1, Fraction(4, 3): -1},
    "A364173": {Fraction(9): 1, Fraction(2): 1, Fraction(3, 2): 1, Fraction(9, 2): -1, Fraction(4): -1, Fraction(3): -1, Fraction(1): -1},
    "A364174": {Fraction(9): 1, Fraction(5, 2): 1, Fraction(3, 2): 1, Fraction(5): -1, Fraction(9, 2): -1, Fraction(3): -1, Fraction(1, 2): -1},
    "A364175": {Fraction(6): 1, Fraction(2, 3): 1, Fraction(3): -1, Fraction(2): -1, Fraction(5, 3): -1},
    "A364176": {Fraction(15): 1, Fraction(5, 2): 1, Fraction(2): 1, Fraction(15, 2): -1, Fraction(6): -1, Fraction(5): -1, Fraction(1): -1},
    "A364177": {Fraction(15): 1, Fraction(5, 2): 1, Fraction(2): 1, Fraction(15, 2): -1, Fraction(5): -1, Fraction(4): -1, Fraction(3): -1},
    "A364178": {Fraction(10): 1, Fraction(3): 1, Fraction(1, 2): 1, Fraction(6): -1, Fraction(5): -1, Fraction(3, 2): -1, Fraction(1): -1},
    "A364179": {Fraction(10): 1, Fraction(1, 2): 1, Fraction(5): -1, Fraction(4): -1, Fraction(3, 2): -1},
    "A364180": {Fraction(10): 1, Fraction(1, 2): 1, Fraction(5): -1, Fraction(7, 2): -1, Fraction(2): -1},
    "A364181": {Fraction(10): 1, Fraction(3, 2): 1, Fraction(5): -1, Fraction(9, 2): -1, Fraction(2): -1},
    "A364182": {Fraction(12): 1, Fraction(1, 2): 1, Fraction(6): -1, Fraction(4): -1, Fraction(5, 2): -1},
    "A364183": {Fraction(12): 1, Fraction(2): 1, Fraction(1, 2): 1, Fraction(6): -1, Fraction(4): -1, Fraction(7, 2): -1, Fraction(1): -1},
    "A364184": {Fraction(12): 1, Fraction(2): 1, Fraction(3, 2): 1, Fraction(6): -1, Fraction(9, 2): -1, Fraction(4): -1, Fraction(1): -1},
}


def check_packet_hypotheses() -> int:
    checks = 0
    for name, terms in PACKET.items():
        assert sum(alpha * exponent for alpha, exponent in terms.items()) == 0, name
        checks += 1
        classes: defaultdict[Fraction, int] = defaultdict(int)
        for alpha, exponent in terms.items():
            residue = alpha - int(alpha)
            if residue:
                classes[residue] += exponent
        assert all(total == 0 for total in classes.values()), (name, classes)
        checks += len(classes)
    return checks


def decompose_gamma_ratio(
    terms: dict[Fraction, int],
) -> tuple[dict[int, int], list[tuple[Fraction, int, int]]]:
    """Pair nonintegral slopes and return integer factors and q-binomials."""
    integer_factors: defaultdict[int, int] = defaultdict(int)
    classes: defaultdict[Fraction, tuple[list[Fraction], list[Fraction]]] = (
        defaultdict(lambda: ([], []))
    )
    rational_binomials: list[tuple[Fraction, int, int]] = []
    for alpha, exponent in terms.items():
        if alpha.denominator == 1:
            integer_factors[int(alpha)] += exponent
            continue
        residue = alpha - int(alpha)
        target = classes[residue][0 if exponent > 0 else 1]
        target.extend([alpha] * abs(exponent))

    for positive, negative in classes.values():
        assert len(positive) == len(negative)
        for alpha, beta in zip(positive, negative, strict=True):
            if alpha > beta:
                distance = int(alpha - beta)
                rational_binomials.append((alpha, distance, 1))
                integer_factors[distance] += 1
            elif beta > alpha:
                distance = int(beta - alpha)
                rational_binomials.append((beta, distance, -1))
                integer_factors[distance] -= 1
    return dict(integer_factors), rational_binomials


def evaluate_gamma_ratio(terms: dict[Fraction, int], n: int) -> Fraction:
    integer_factors, rational_binomials = decompose_gamma_ratio(terms)
    out = Fraction(1)
    for slope, exponent in integer_factors.items():
        out *= Fraction(factorial(slope * n)) ** exponent
    for top, bottom, exponent in rational_binomials:
        out *= rational_binomial(
            top.numerator, bottom, top.denominator, n
        ) ** exponent
    return out


def add_term(terms: defaultdict[Fraction, int], slope: Fraction, exponent: int) -> None:
    if slope:
        terms[slope] += exponent


def a365025_terms(row: int) -> dict[Fraction, int]:
    terms: defaultdict[Fraction, int] = defaultdict(int)
    add_term(terms, Fraction(1, 2), 1)
    add_term(terms, Fraction(2 * row + 1), 1)
    add_term(terms, Fraction(4 * row + 1, 2), 1)
    add_term(terms, Fraction(1), -1)
    add_term(terms, Fraction(row), -2)
    add_term(terms, Fraction(2 * row + 1, 2), -2)
    return {slope: exponent for slope, exponent in terms.items() if exponent}


def a365025_sum(row: int, n: int) -> int:
    if n == 0:
        return 1
    return sum(
        (
            factorial((2 * row + 1) * n)
            // (
                factorial(row * n - j)
                * factorial((row + 1) * n + j)
            )
        )
        ** 2
        * factorial(n + j - 1)
        // (factorial(j) * factorial(n - 1))
        for j in range(row * n + 1)
    )


def generalized_integer_binomial(top: int, bottom: int) -> Fraction:
    out = Fraction(1)
    for j in range(bottom):
        out *= Fraction(top - j, j + 1)
    return out


def a364513_terms(row: int) -> dict[Fraction, int]:
    assert row >= 3
    terms: defaultdict[Fraction, int] = defaultdict(int)
    add_term(terms, Fraction(row + 2), 1)
    add_term(terms, Fraction(row, 2), 2)
    add_term(terms, Fraction(row + 2, 2), -1)
    add_term(terms, Fraction(row), -1)
    add_term(terms, Fraction(row - 2, 2), -1)
    add_term(terms, Fraction(1), -2)
    return {slope: exponent for slope, exponent in terms.items() if exponent}


def a364513_sum(row: int, n: int) -> Fraction:
    assert row >= 3 and n >= 1
    return sum(
        generalized_integer_binomial(row * n - 1, n - j) ** 2
        * generalized_integer_binomial((row - 2) * n + j - 2, j)
        for j in range(n + 1)
    )


def a364513_gamma(row: int, n: int) -> Fraction:
    return Fraction(row - 2, row) * evaluate_gamma_ratio(a364513_terms(row), n)


def check_packet_exact_values_and_towers() -> int:
    checks = 0
    for name, terms in PACKET.items():
        for n in range(13):
            # Finite evidence only: the proof does not infer global integrality.
            assert evaluate_gamma_ratio(terms, n).denominator == 1, (name, n)
            checks += 1
        for p in (5, 7):
            for r, n_max in ((1, 3), (2, 1)):
                for n in range(1, n_max + 1):
                    high = evaluate_gamma_ratio(terms, n * p**r)
                    low = evaluate_gamma_ratio(terms, n * p ** (r - 1))
                    assert vp(high - low, p) >= 3 * r, (name, p, r, n)
                    checks += 1
    return checks


def check_row_families() -> int:
    checks = 0
    for row in range(0, 8):
        terms = a365025_terms(row)
        for n in range(0, 9):
            assert evaluate_gamma_ratio(terms, n) == a365025_sum(row, n)
            checks += 1
        for p in (5, 7):
            for r, n_max in ((1, 2), (2, 1)):
                for n in range(1, n_max + 1):
                    high = evaluate_gamma_ratio(terms, n * p**r)
                    low = evaluate_gamma_ratio(terms, n * p ** (r - 1))
                    assert high.denominator == low.denominator == 1
                    assert vp(high - low, p) >= 3 * r
                    checks += 1

    for row in range(3, 9):
        terms = a364513_terms(row)
        for n in range(1, 10):
            value = a364513_gamma(row, n)
            assert value == a364513_sum(row, n)
            assert value.denominator == 1
            checks += 2
        for p in (5, 7):
            for r, n_max in ((1, 2), (2, 1)):
                for n in range(1, n_max + 1):
                    high = a364513_gamma(row, n * p**r)
                    low = a364513_gamma(row, n * p ** (r - 1))
                    assert vp(high - low, p) >= 3 * r
                    checks += 1
    return checks


def main() -> None:
    sections = {
        "rational-binomial identities/transfers": check_rational_binomial_transfer(),
        "A364175": check_a364175(),
        "packet hypotheses": check_packet_hypotheses(),
        "packet finite values/towers": check_packet_exact_values_and_towers(),
        "row-family identities/towers": check_row_families(),
    }
    total = sum(sections.values())
    print(f"Rational gamma-ratio checks passed: {total}")
    for label, count in sections.items():
        print(f"  {label}: {count}")


if __name__ == "__main__":
    main()
