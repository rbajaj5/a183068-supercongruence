"""Exact checks for the first defect in Bala's negative-binomial tower.

The proof is the Cartier calculation in
``related-results/BalaAugustFirstDefectKernel.md``.  These computations
check the arithmetic consequences of the proved Cartier-moment stability;
they are not a substitute for the coefficient proof in that note.

Run with:
    python verification/related/verify_bala_august_first_defect.py
"""

from __future__ import annotations

from fractions import Fraction


def valuation_and_unit(value: int, prime: int) -> tuple[int, int]:
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent, value


def negative_binomial_sum_mod(n: int, prime: int, precision: int) -> int:
    """Return sum C(-n,k)C(-2n,k), 0 <= k <= n, modulo p^precision."""

    modulus = prime**precision
    unit = 1
    exponent = 0
    total = 1
    for k in range(1, n + 1):
        e1, u1 = valuation_and_unit(n + k - 1, prime)
        e2, u2 = valuation_and_unit(2 * n + k - 1, prime)
        ek, uk = valuation_and_unit(k, prime)
        exponent += e1 + e2 - 2 * ek
        assert exponent >= 0
        unit = unit * u1 * u2 * pow(uk, -2, modulus) % modulus
        if exponent < precision:
            total = (total + unit * prime**exponent) % modulus
    return total


def prefix_sum_mod(
    a: int, b: int, c: int, n: int, prime: int, precision: int
) -> int:
    """Return U_{a,b;c}(n) modulo p^precision."""

    modulus = prime**precision
    unit = 1
    exponent = 0
    total = 1
    for k in range(1, c * n + 1):
        e1, u1 = valuation_and_unit(a * n + k - 1, prime)
        e2, u2 = valuation_and_unit(b * n + k - 1, prime)
        ek, uk = valuation_and_unit(k, prime)
        exponent += e1 + e2 - 2 * ek
        assert exponent >= 0
        unit = unit * u1 * u2 * pow(uk, -2, modulus) % modulus
        if exponent < precision:
            total = (total + unit * prime**exponent) % modulus
    return total


def bernoulli_number(index: int) -> Fraction:
    values = [Fraction(0) for _ in range(index + 1)]
    for m in range(index + 1):
        values[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            values[j - 1] = j * (values[j - 1] - values[j])
    return values[0]


def fraction_mod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def normalized_defect(n: int, prime: int, level: int) -> int:
    precision = 3 * level + 1
    modulus = prime**precision
    large = negative_binomial_sum_mod(n * prime**level, prime, precision)
    small = negative_binomial_sum_mod(
        n * prime ** (level - 1), prime, precision
    )
    difference = (large - small) % modulus
    cubic = prime ** (3 * level)
    assert difference % cubic == 0
    return difference // cubic % prime


def check_level_stability() -> int:
    """Exact regression checks for the proved level-stability theorem."""

    checks = 0
    for prime, max_n, max_level in (
        (5, 20, 4),
        (7, 16, 4),
        (11, 12, 3),
        (13, 10, 3),
        (17, 8, 3),
        (19, 7, 3),
    ):
        for n in range(1, max_n + 1):
            values = [
                normalized_defect(n, prime, level)
                for level in range(1, max_level + 1)
            ]
            assert len(set(values)) == 1
            checks += max_level
    return checks


def check_bernoulli_boundary() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        expected = fraction_mod(2 * bernoulli_number(prime - 3), prime)
        for level in (1, 2, 3):
            assert normalized_defect(1, prime, level) == expected
            checks += 1
    return checks


def check_family_level_stability() -> int:
    """Broad regression grid for the family-level kernel-moment theorem."""

    checks = 0
    for prime in (5, 7, 11):
        for a in range(1, 5):
            for b in range(1, 5):
                for c in range(1, 4):
                    for n in range(1, 5):
                        values = []
                        for level in (1, 2):
                            precision = 3 * level + 1
                            modulus = prime**precision
                            large = prefix_sum_mod(
                                a,
                                b,
                                c,
                                n * prime**level,
                                prime,
                                precision,
                            )
                            small = prefix_sum_mod(
                                a,
                                b,
                                c,
                                n * prime ** (level - 1),
                                prime,
                                precision,
                            )
                            difference = (large - small) % modulus
                            cubic = prime ** (3 * level)
                            assert difference % cubic == 0
                            values.append(difference // cubic % prime)
                            checks += 1
                        assert values[0] == values[1]
    return checks


def check_extra_power_when_base_is_divisible() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for multiplier in range(1, 6):
            for level in (1, 2):
                n = prime * multiplier
                precision = 3 * level + 2
                modulus = prime**precision
                difference = (
                    negative_binomial_sum_mod(
                        n * prime**level, prime, precision
                    )
                    - negative_binomial_sum_mod(
                        n * prime ** (level - 1), prime, precision
                    )
                ) % modulus
                assert difference % prime ** (3 * level + 1) == 0
                checks += 1
    return checks


def main() -> None:
    results = {
        "level-stability evidence": check_level_stability(),
        "family-level stability evidence": check_family_level_stability(),
        "Bernoulli boundary": check_bernoulli_boundary(),
        "divisible-base bonus": check_extra_power_when_base_is_divisible(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
