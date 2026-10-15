"""Exact checks for BoberHalfIndexIntegralityTowers.md.

The proof is in the Markdown note.  This script reconstructs the odd-index
factorial ratios from the Bober coefficient vectors and checks the two
binary digit-sum certificates without relying on precomputed sequence terms.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import factorial

from verify_bober_sporadic_packet import FRACTIONAL, evaluate_gamma_ratio, vp


FIRST_DIGIT_CERTIFICATE = {
    "A295456",
    "A295458",
    "A295460",
    "A295465",
    "A295468",
}

SECOND_DIGIT_CERTIFICATE = {
    "A295470",
    "A295471",
    "A295475",
    "A295477",
    "A295479",
    "A295481",
}

EXPECTED_LAMBDA = {
    "A295456": 10,
    "A295458": 10,
    "A295460": 12,
    "A295465": 8,
    "A295468": 8,
    "A295470": 2,
    "A295471": 2,
    "A295475": 6,
    "A295477": 4,
    "A295479": 6,
    "A295481": 6,
}


def signed_vectors(name: str) -> tuple[list[int], list[int]]:
    numerators, denominators, indices = FRACTIONAL[name]
    assert 2 in indices
    return numerators, denominators


def odd_core_terms(
    numerators: list[int], denominators: list[int]
) -> tuple[int, list[tuple[int, int, int]]]:
    """Return lambda and (slope, intercept, exponent) for N=2m+1.

    The gamma duplication formula gives B(2m+1) = 2^(lambda*(2m+1)) R(m),
    where R is the signed product of the factorials encoded by the triples.
    """

    terms: list[tuple[int, int, int]] = []
    odd_slope_sum = 0
    odd_count = 0
    for exponent, coefficients in ((1, numerators), (-1, denominators)):
        for coefficient in coefficients:
            if coefficient % 2 == 0:
                terms.append((coefficient, coefficient // 2, exponent))
            else:
                half = (coefficient + 1) // 2
                terms.append((2 * coefficient, coefficient + 1, exponent))
                terms.append((coefficient, half, -exponent))
                odd_slope_sum += exponent * coefficient
                odd_count += exponent
    assert odd_count == 0
    return -odd_slope_sum, terms


def compact_digit_expression(
    terms: list[tuple[int, int, int]],
) -> dict[tuple[int, int], int]:
    """Coefficients in v_2(R), modulo s_2(2x)=s_2(x)."""

    expression: defaultdict[tuple[int, int], int] = defaultdict(int)
    for slope, intercept, exponent in terms:
        while slope % 2 == 0 and intercept % 2 == 0:
            slope //= 2
            intercept //= 2
        expression[(slope, intercept)] -= exponent
    return {argument: value for argument, value in expression.items() if value}


def expected_digit_expression(name: str) -> dict[tuple[int, int], int]:
    if name in FIRST_DIGIT_CERTIFICATE:
        # N=2m+1: s_2(3N)+s_2(5N)-s_2(15N).
        return {(6, 3): 1, (10, 5): 1, (30, 15): -1}
    assert name in SECOND_DIGIT_CERTIFICATE
    # N=2m+1: s_2(N).
    return {(2, 1): 1}


def core_value(terms: list[tuple[int, int, int]], m: int) -> Fraction:
    value = Fraction(1)
    for slope, intercept, exponent in terms:
        value *= Fraction(factorial(slope * m + intercept)) ** exponent
    return value


def original_landau(
    numerators: list[int], denominators: list[int], numerator: int, denominator: int
) -> int:
    return sum(a * numerator // denominator for a in numerators) - sum(
        a * numerator // denominator for a in denominators
    )


def affine_defect(terms: list[tuple[int, int, int]], m: int, d: int) -> int:
    return sum(exponent * ((slope * m + intercept) // d) for slope, intercept, exponent in terms)


def check_symbolic_certificates() -> int:
    checks = 0
    names = FIRST_DIGIT_CERTIFICATE | SECOND_DIGIT_CERTIFICATE
    assert names == {name for name, (_, _, indices) in FRACTIONAL.items() if 2 in indices}
    checks += 1
    for name in sorted(names):
        numerators, denominators = signed_vectors(name)
        assert sum(numerators) == sum(denominators)
        assert sum(a % 2 for a in numerators) == sum(a % 2 for a in denominators)
        lam, terms = odd_core_terms(numerators, denominators)
        assert lam == EXPECTED_LAMBDA[name] > 0
        assert sum(exponent * slope for slope, _, exponent in terms) == 0
        assert sum(exponent * intercept for _, intercept, exponent in terms) == 0
        assert compact_digit_expression(terms) == expected_digit_expression(name)
        checks += 6
    return checks


def check_odd_prime_landau_transfer() -> int:
    checks = 0
    for name in sorted(FIRST_DIGIT_CERTIFICATE | SECOND_DIGIT_CERTIFICATE):
        numerators, denominators = signed_vectors(name)
        _, terms = odd_core_terms(numerators, denominators)
        for d in range(3, 102, 2):
            for m in range(2 * d):
                t = m + (d + 1) // 2
                assert affine_defect(terms, m, d) == original_landau(
                    numerators, denominators, t, d
                )
                checks += 1
    return checks


def check_exact_values_and_valuations() -> int:
    checks = 0
    for name in sorted(FIRST_DIGIT_CERTIFICATE | SECOND_DIGIT_CERTIFICATE):
        numerators, denominators = signed_vectors(name)
        lam, terms = odd_core_terms(numerators, denominators)
        fractional_terms = defaultdict(int)
        for coefficient in numerators:
            fractional_terms[Fraction(coefficient, 2)] += 1
        for coefficient in denominators:
            fractional_terms[Fraction(coefficient, 2)] -= 1
        fractional_terms = {key: value for key, value in fractional_terms.items() if value}

        for m in range(41):
            n = 2 * m + 1
            core = core_value(terms, m)
            value = evaluate_gamma_ratio(fractional_terms, n)
            assert value == (2 ** (lam * n)) * core
            assert core.denominator == 1
            assert value.denominator == 1
            expected_v2 = sum(
                coefficient * (slope * m + intercept).bit_count()
                for (slope, intercept), coefficient in expected_digit_expression(name).items()
            )
            assert vp(core, 2) == expected_v2 >= 0
            checks += 4
    return checks


def check_towers() -> int:
    checks = 0
    for name in sorted(FIRST_DIGIT_CERTIFICATE | SECOND_DIGIT_CERTIFICATE):
        numerators, denominators = signed_vectors(name)
        terms = defaultdict(int)
        for coefficient in numerators:
            terms[Fraction(coefficient, 2)] += 1
        for coefficient in denominators:
            terms[Fraction(coefficient, 2)] -= 1
        terms = {key: value for key, value in terms.items() if value}
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
        "symbolic certificates": check_symbolic_certificates(),
        "odd-prime Landau transfer": check_odd_prime_landau_transfer(),
        "exact values and valuations": check_exact_values_and_valuations(),
        "cubic towers": check_towers(),
    }
    print(f"Bober half-index checks passed: {sum(sections.values())}")
    for name, count in sections.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
