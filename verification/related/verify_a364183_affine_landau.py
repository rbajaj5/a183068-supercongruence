"""Exact checks for the A364183 affine-Landau theorem."""

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


def vp(value: Fraction, prime: int) -> int:
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


def even_value(m: int) -> Fraction:
    return Fraction(
        factorial(24 * m) * factorial(4 * m) * factorial(m),
        factorial(12 * m)
        * factorial(8 * m)
        * factorial(7 * m)
        * factorial(2 * m),
    )


def odd_core(m: int) -> Fraction:
    return Fraction(
        factorial(24 * m + 12)
        * factorial(4 * m + 2)
        * factorial(2 * m + 2)
        * factorial(7 * m + 4),
        factorial(12 * m + 6)
        * factorial(8 * m + 4)
        * factorial(2 * m + 1)
        * factorial(m + 1)
        * factorial(14 * m + 8),
    )


def sequence_value(n: int) -> Fraction:
    if n % 2 == 0:
        return even_value(n // 2)
    m = (n - 1) // 2
    return 2 ** (12 * m + 6) * odd_core(m)


def floor_defect(m: int, d: int) -> int:
    return (
        (24 * m + 12) // d
        + (4 * m + 2) // d
        + (2 * m + 2) // d
        + (7 * m + 4) // d
        - (12 * m + 6) // d
        - (8 * m + 4) // d
        - (2 * m + 1) // d
        - (m + 1) // d
        - (14 * m + 8) // d
    )


def reduced_floor_defect(m: int, d: int) -> int:
    """The two-case residue formula used in the proof."""
    assert 0 <= m < d
    q, s = divmod(2 * m + 1, d)
    assert q in (0, 1)
    j = 12 * s // d
    h = (7 * s + 1) // d
    epsilon = (s + 1) // d
    c = j + j // 6 - j // 2 - j // 3
    if q == 0:
        assert s % 2 == 1
        return c + epsilon - (h + 1) // 2
    assert (d + s) % 2 == 1
    return -3 + c + (7 - h) // 2


def legendre_core_valuation(m: int, prime: int) -> int:
    total = 0
    power = prime
    while power <= 24 * m + 12:
        total += floor_defect(m, power)
        power *= prime
    return total


def half_factorization(n: int) -> Fraction:
    out = Fraction(1)
    for parameter in (14, 16, 18, 20, 22, 24):
        out *= half_binomial(parameter, n)
    for parameter in (3, 5, 6, 7, 8):
        out /= half_binomial(parameter, n)
    return out


def check_initial_and_parity() -> int:
    expected = (
        1,
        4224,
        76488984,
        1626105446400,
        36856530424884600,
        864687003650148532224,
    )
    assert tuple(sequence_value(n) for n in range(len(expected))) == expected
    checks = len(expected)
    for m in range(31):
        assert sequence_value(2 * m) == even_value(m)
        assert sequence_value(2 * m + 1) == 2 ** (12 * m + 6) * odd_core(m)
        checks += 2
    return checks


def check_floor_lemma() -> int:
    checks = 0
    for d in range(2, 1001):
        for m in range(d):
            defect = floor_defect(m, d)
            assert reduced_floor_defect(m, d) == defect
            assert defect in (0, 1, 2)
            assert (defect == 2) == (d == 2 * m + 2 and m >= 5)
            assert floor_defect(m + d, d) == defect
            checks += 4
    return checks


def check_integrality_and_legendre() -> int:
    checks = 0
    for n in range(101):
        assert sequence_value(n).denominator == 1
        checks += 1
    for m in range(51):
        assert odd_core(m).denominator == 1
        checks += 1
        for prime in (2, 3, 5, 7, 11, 13, 17, 19):
            assert vp(odd_core(m), prime) == legendre_core_valuation(m, prime)
            checks += 1
    return checks


def check_factorization_and_tower() -> int:
    checks = 0
    for n in range(1, 31):
        assert half_factorization(n) == sequence_value(n)
        checks += 1
    for prime in (5, 7, 11):
        for level in (1, 2):
            for n in range(1, 5):
                high = n * prime**level
                low = n * prime ** (level - 1)
                for parameter in (3, 5, 6, 7, 8, 14, 16, 18, 20, 22, 24):
                    ratio = half_binomial(parameter, high) / half_binomial(
                        parameter, low
                    )
                    assert vp(ratio - 1, prime) >= 3 * level
                    checks += 1
                difference = sequence_value(high) - sequence_value(low)
                assert vp(difference, prime) >= 3 * level
                checks += 1
    return checks


def main() -> None:
    sections = {
        "initial and parity identities": check_initial_and_parity(),
        "affine floor classification": check_floor_lemma(),
        "integrality and Legendre identities": check_integrality_and_legendre(),
        "half-binomial factorization and towers": check_factorization_and_tower(),
    }
    for label, count in sections.items():
        print(f"{label}: {count}")
    print(f"all {sum(sections.values())} checks passed")


if __name__ == "__main__":
    main()
