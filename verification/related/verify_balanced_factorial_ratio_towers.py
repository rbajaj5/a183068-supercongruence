"""Exact checks for balanced factorial-ratio cubic towers.

These checks support transcription and boundary testing.  The proof is the
Laurent-binomial factorization plus the Ljunggren--Jacobsthal congruence.
"""

from fractions import Fraction
from math import comb, factorial


def factorial_ratio(coefficients: dict[int, int], n: int) -> Fraction:
    value = Fraction(1)
    for m, exponent in coefficients.items():
        value *= Fraction(factorial(m * n)) ** exponent
    return value


def binomial_factorization(coefficients: dict[int, int], n: int) -> Fraction:
    maximum = max(coefficients)
    value = Fraction(1)
    for j in range(2, maximum + 1):
        exponent = sum(coefficients.get(m, 0) for m in range(j, maximum + 1))
        value *= Fraction(comb(j * n, n)) ** exponent
    return value


def a061164(n: int) -> int:
    value = factorial_ratio({20: 1, 10: -1, 7: -1, 4: -1, 1: 1}, n)
    assert value.denominator == 1
    return value.numerator


def main() -> None:
    checks = 0

    examples = (
        {3: 1, 2: -1, 1: -1},
        {5: 1, 3: -1, 2: -1},
        {6: 1, 3: -1, 2: -1, 1: -1},
        {20: 1, 10: -1, 7: -1, 4: -1, 1: 1},
        {8: 2, 6: -1, 5: -1, 4: -1, 1: -1},
    )
    for coefficients in examples:
        assert sum(m * c for m, c in coefficients.items()) == 0
        for n in range(1, 6):
            assert factorial_ratio(coefficients, n) == binomial_factorization(
                coefficients, n
            )
            checks += 1

    expected = (
        1,
        5_542_680,
        190_818_980_609_400,
        7_691_041_400_616_850_556_280,
        330_014_847_932_376_708_502_470_210_680,
        14_647_137_653_300_940_580_784_413_641_872_332_680,
    )
    for n, value in enumerate(expected):
        assert a061164(n) == value
        checks += 1

    for p in (5, 7, 11):
        for r in (1, 2):
            modulus = p ** (3 * r)
            for n in (1, 2, 3):
                assert (a061164(n * p**r) - a061164(n * p ** (r - 1))) % modulus == 0
                checks += 1

    # The short factorization displayed on the OEIS page.
    for n in range(1, 9):
        short = Fraction(comb(20 * n, 10 * n) * comb(10 * n, 3 * n), comb(4 * n, n))
        assert short.denominator == 1
        assert short.numerator == a061164(n)
        checks += 1

    print(f"balanced factorial-ratio checks passed: {checks}")


if __name__ == "__main__":
    main()
