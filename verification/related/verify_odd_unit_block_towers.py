"""Exact checks for OddUnitBlockFrobeniusTowers.md.

The calculations are regression evidence for the written proof, not a
substitute for it.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def generalized_binomial(top: Fraction, lower: int) -> Fraction:
    answer = Fraction(1)
    for j in range(lower):
        answer *= top - j
    return answer / factorial(lower)


def coefficient_family(m: int, n: int) -> int:
    value = 4**n * generalized_binomial(Fraction(m * n - 1, 2), n)
    assert value.denominator == 1
    return value.numerator


def polynomial_coefficient(m: int, n: int) -> int:
    # [x^n] (1+x)^(mn) (1-x)^(-(m-2)n)
    if n == 0:
        return 1
    positive = m * n
    negative = (m - 2) * n
    answer = 0
    for j in range(n + 1):
        left = comb(positive, j)
        right = 1 if negative == 0 and n - j == 0 else 0
        if negative > 0:
            right = comb(negative + n - j - 1, n - j)
        answer += left * right
    return answer


def product_family(m: int, n: int) -> int:
    numerator = 2**n
    for j in range(n):
        numerator *= m * n - (2 * j + 1)
    assert numerator % factorial(n) == 0
    return numerator // factorial(n)


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def unit_product(bound: int, prime: int) -> int:
    answer = 1
    for k in range(1, bound + 1):
        if k % prime:
            answer *= k
    return answer


def correction_product(m: int, n: int, prime: int) -> Fraction:
    answer = Fraction(1)
    for t in range(1, 2 * n, 2):
        if t % prime:
            answer *= Fraction(t - m * n, t)
    # The number of extracted minus signs is even.
    return answer


def check_initial_values() -> int:
    expected_3 = [
        1,
        4,
        30,
        256,
        2310,
        21504,
        204204,
        1966080,
    ]
    expected_5 = [
        1,
        8,
        126,
        2240,
        41990,
        811008,
        15967980,
        318636032,
    ]
    assert [coefficient_family(3, n) for n in range(8)] == expected_3
    assert [coefficient_family(5, n) for n in range(8)] == expected_5
    return 16


def check_three_forms() -> int:
    checks = 0
    for m in range(2, 11):
        for n in range(0, 15):
            a = coefficient_family(m, n)
            assert a == polynomial_coefficient(m, n)
            assert a == product_family(m, n)
            checks += 2
    return checks


def check_odd_unit_harmonics() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for exponent in (1, 2, 3):
            modulus = prime**exponent
            odd_units = [
                t
                for t in range(1, 2 * modulus, 2)
                if t % prime
            ]
            first = sum(pow(t, -1, modulus**2) for t in odd_units)
            second = sum(pow(t, -2, modulus) for t in odd_units)
            assert first % modulus**2 == 0
            assert second % modulus == 0
            checks += 2

            for blocks in (2, 3, 5):
                values = [
                    t
                    for t in range(1, 2 * blocks * modulus, 2)
                    if t % prime
                ]
                first = sum(pow(t, -1, modulus**2) for t in values)
                second = sum(pow(t, -2, modulus) for t in values)
                assert first % modulus**2 == 0
                assert second % modulus == 0
                checks += 2
    return checks


def check_exact_factorization() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for m in range(2, 9):
            for lower in range(1, 9):
                upper = prime * lower
                lhs = Fraction(
                    coefficient_family(m, upper),
                    coefficient_family(m, lower),
                )
                jacobsthal = Fraction(
                    comb(2 * upper, upper),
                    comb(2 * lower, lower),
                )
                rhs = jacobsthal * correction_product(m, upper, prime)
                assert lhs == rhs
                checks += 1
    return checks


def check_family_tower() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for m in range(2, 11):
            for r in (1, 2, 3):
                # Keep the largest exact integers moderate while checking all
                # three adjacent levels.
                upper_n = 4 if r == 1 else (2 if r == 2 else 1)
                for n in range(1, upper_n + 1):
                    upper = coefficient_family(m, n * prime**r)
                    lower = coefficient_family(m, n * prime ** (r - 1))
                    assert (upper - lower) % prime ** (3 * r) == 0
                    checks += 1
    return checks


def check_small_prime_boundaries() -> int:
    checks = 0
    examples = (
        (3, 3, 1, 1, 2),
        (5, 3, 1, 1, 2),
        (3, 2, 1, 1, 1),
        (5, 2, 1, 1, 1),
    )
    for m, prime, n, r, expected in examples:
        difference = (
            coefficient_family(m, n * prime**r)
            - coefficient_family(m, n * prime ** (r - 1))
        )
        assert vp(difference, prime) == expected
        assert expected < 3 * r
        checks += 1
    return checks


def main() -> None:
    counts = {
        "initial values": check_initial_values(),
        "three exact forms": check_three_forms(),
        "odd-unit harmonics": check_odd_unit_harmonics(),
        "exact block factorizations": check_exact_factorization(),
        "family tower": check_family_tower(),
        "small-prime boundaries": check_small_prime_boundaries(),
    }
    total = sum(counts.values())
    print(f"odd-unit block tower checks passed: {total}")
    for label, count in counts.items():
        print(f"  {label}: {count}")


if __name__ == "__main__":
    main()
