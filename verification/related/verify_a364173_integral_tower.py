"""Exact checks for the A364173 integrality and tower theorem.

The script is a regression certificate, not a proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def vp_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def vp_fraction(value: Fraction, prime: int) -> int:
    return vp_int(value.numerator, prime) - vp_int(value.denominator, prime)


def generalized_binomial(top: Fraction, lower: int) -> Fraction:
    out = Fraction(1)
    for j in range(lower):
        out *= top - j
    for j in range(1, lower + 1):
        out /= j
    return out


def half_binomial(parameter: int, n: int) -> Fraction:
    return generalized_binomial(Fraction(parameter * n, 2), n)


def sequence_value(n: int) -> Fraction:
    return (
        Fraction(comb(9 * n, 4 * n) * comb(5 * n, 2 * n) * comb(2 * n, n) ** 2)
        / half_binomial(9, n)
        / half_binomial(7, n)
        / half_binomial(5, n)
    )


def even_factorial_value(m: int) -> int:
    return (
        factorial(18 * m)
        * factorial(4 * m)
        * factorial(3 * m)
        // (
            factorial(9 * m)
            * factorial(8 * m)
            * factorial(6 * m)
            * factorial(2 * m)
        )
    )


def odd_factorial_value(m: int) -> Fraction:
    return Fraction(
        4 ** (6 * m + 3) * factorial(4 * m + 2) * factorial(9 * m + 4),
        factorial(3 * m + 1) * factorial(8 * m + 4) * factorial(2 * m + 1),
    )


def floor_defect(m: int, q: int) -> int:
    return (
        (9 * m + 4) // q
        + (4 * m + 2) // q
        - (8 * m + 4) // q
        - (3 * m + 1) // q
        - (2 * m + 1) // q
    )


def half_transfer(parameter: int, n: int, prime: int) -> Fraction:
    assert n % prime == 0
    return half_binomial(parameter, n) / half_binomial(parameter, n // prime)


def check_initial_values() -> int:
    expected = [
        1,
        128,
        43758,
        17039360,
        7012604550,
        2976412336128,
        1288415796384780,
        565399665327996928,
    ]
    for n, value in enumerate(expected):
        actual = sequence_value(n)
        assert actual.denominator == 1
        assert actual.numerator == value
    return len(expected)


def check_parity_forms() -> int:
    checks = 0
    for m in range(0, 30):
        assert sequence_value(2 * m) == even_factorial_value(m)
        assert sequence_value(2 * m + 1) == odd_factorial_value(m)
        checks += 2
    return checks


def check_floor_lemma() -> int:
    checks = 0
    for q in range(2, 401):
        for m in range(0, 3 * q + 7):
            assert floor_defect(m, q) >= 0
            assert floor_defect(m + q, q) == floor_defect(m, q)
            checks += 2
    return checks


def check_integrality() -> int:
    checks = 0
    for n in range(0, 151):
        assert sequence_value(n).denominator == 1
        checks += 1
    return checks


def check_adjacent_factors() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for r in (1, 2):
            for n in range(1, 6):
                high = n * prime**r
                low = high // prime
                for parameter in (5, 7, 9):
                    ratio = half_transfer(parameter, high, prime)
                    assert vp_fraction(ratio - 1, prime) >= 3 * r
                    checks += 1
                ordinary = (
                    Fraction(comb(9 * high, 4 * high), comb(9 * low, 4 * low)),
                    Fraction(comb(5 * high, 2 * high), comb(5 * low, 2 * low)),
                    Fraction(comb(2 * high, high), comb(2 * low, low)),
                )
                for ratio in ordinary:
                    assert vp_fraction(ratio - 1, prime) >= 3 * r
                    checks += 1
    return checks


def check_tower() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for r in (1, 2):
            for n in range(1, 6):
                high = sequence_value(n * prime**r)
                low = sequence_value(n * prime ** (r - 1))
                assert high.denominator == low.denominator == 1
                assert (high.numerator - low.numerator) % prime ** (3 * r) == 0
                checks += 1
    return checks


def check_small_prime_boundaries() -> int:
    at_one = sequence_value(1).numerator
    delta_two = sequence_value(2).numerator - at_one
    delta_three = sequence_value(3).numerator - at_one
    assert vp_int(delta_two, 2) == 1
    assert vp_int(delta_three, 3) == 2
    return 2


def main() -> None:
    sections = {
        "OEIS initial values": check_initial_values(),
        "even/odd factorial forms": check_parity_forms(),
        "floor-defect lemma": check_floor_lemma(),
        "integrality": check_integrality(),
        "adjacent factor transfers": check_adjacent_factors(),
        "A364173 towers": check_tower(),
        "small-prime boundaries": check_small_prime_boundaries(),
    }
    print(f"A364173 checks passed: {sum(sections.values())}")
    for name, count in sections.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
