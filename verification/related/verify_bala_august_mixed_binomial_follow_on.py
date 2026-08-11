"""Exact checks for the August mixed-binomial follow-on.

The calculations certify formulas, sample theorem instances, and the two
displayed counterexamples.  They support the written proofs; they do not
replace the valuation argument or Coster's theorem.
"""

from __future__ import annotations

from math import comb

import verify_bala_august_coefficient_packet as august


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def integer_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(-top + bottom - 1, bottom)


def mixed_term(
    slopes: tuple[int, ...],
    bottom_weights: tuple[int, ...],
    n: int,
    k: int,
) -> int:
    out = 1
    for slope, weight in zip(slopes, bottom_weights, strict=True):
        out *= integer_binomial(slope * n, weight * k)
    return out


def mixed_sum(
    slopes: tuple[int, ...],
    bottom_weights: tuple[int, ...],
    cutoff: int,
    n: int,
    twist: int = 1,
) -> int:
    return sum(
        twist**k * mixed_term(slopes, bottom_weights, n, k)
        for k in range(cutoff * n + 1)
    )


def mixed_exponent(number_of_factors: int, prime: int, level: int) -> int:
    small_prime_loss = 1 if prime == 3 else 0
    return min(number_of_factors * level, 3 * level - small_prime_loss)


def a333473(n: int) -> int:
    if n == 0:
        return 1
    return sum(comb(n, k) * comb(n + 2 * k - 1, 2 * k) for k in range(n + 1))


def algebraic_family_lagrange(r: int, s: int, n: int) -> int:
    """Return [x^(r*n)] F(x)^(s*n) from the finite Lagrange sum."""
    if n == 0:
        return 1
    total = sum(
        comb(r * n, j) * comb(s * n + 2 * j - 1, r * n - 1)
        for j in range(r * n + 1)
    )
    assert (s * total) % r == 0
    return s * total // r


def schroeder_substitution_series(degree: int) -> list[int]:
    """Coefficients of F=1+x+xF^2 through the requested degree."""
    coefficients = [1]
    for n in range(1, degree + 1):
        coefficient = int(n == 1)
        coefficient += sum(
            coefficients[j] * coefficients[n - 1 - j] for j in range(n)
        )
        coefficients.append(coefficient)
    return coefficients


def power_series_coefficient(base: list[int], power: int, degree: int) -> int:
    out = [1] + [0] * degree
    factor = base[: degree + 1]
    while power:
        if power & 1:
            out = [
                sum(out[j] * factor[n - j] for j in range(n + 1))
                for n in range(degree + 1)
            ]
        power //= 2
        if power:
            factor = [
                sum(factor[j] * factor[n - j] for j in range(n + 1))
                for n in range(degree + 1)
            ]
    return out[degree]


def a333592(n: int) -> int:
    if n == 0:
        return 1
    return sum(comb(n + k - 1, k) ** 2 for k in range(n + 1))


def coster_block(n: int) -> int:
    if n == 0:
        return 1
    return sum(comb(n + k - 1, k) ** 2 for k in range(n))


def endpoint_square(n: int) -> int:
    if n == 0:
        return 0
    return comb(2 * n - 1, n) ** 2


def companion_positive(n: int) -> int:
    return sum(
        integer_binomial(-n, k)
        * integer_binomial(n, k)
        * integer_binomial(2 * k, n)
        * integer_binomial(n + k, k)
        for k in range(n + 1)
    )


def companion_negative(n: int) -> int:
    return sum(
        integer_binomial(n, k) ** 2
        * integer_binomial(2 * k, n)
        * integer_binomial(-n - k, k)
        for k in range(n + 1)
    )


def cutoff_companion_positive(n: int, cutoff: int) -> int:
    return sum(
        integer_binomial(-n, k) ** 2
        * integer_binomial(2 * k, n)
        * integer_binomial(n + k, k)
        for k in range(cutoff * n + 1)
    )


def cutoff_companion_negative(n: int, cutoff: int) -> int:
    return sum(
        integer_binomial(-n, k) ** 2
        * integer_binomial(2 * k, n)
        * integer_binomial(-n - k, k)
        for k in range(cutoff * n + 1)
    )


def check_mixed_polynomial_theorem() -> int:
    configurations = (
        ((1,), (1,), 2),
        ((-1,), (2,), 1),
        ((1, -1), (1, 2), 1),
        ((-1, -2), (1, 1), 1),
        ((1, 2, 3), (1, 1, 1), 2),
        ((-1, 2, -3), (1, 2, 1), 1),
        ((1, -1, 2, -2), (1, 1, 2, 2), 1),
    )
    checks = 0
    for slopes, weights, cutoff in configurations:
        for prime in (3, 5, 7):
            if any(weight % prime == 0 for weight in weights):
                continue
            for n in (1, 2):
                for level in (1, 2):
                    large_n = n * prime**level
                    small_n = large_n // prime
                    exponent = mixed_exponent(len(slopes), prime, level)
                    modulus = prime**exponent
                    for k in range(cutoff * large_n + 1):
                        large = mixed_term(slopes, weights, large_n, k)
                        small = 0
                        if k % prime == 0:
                            small = mixed_term(slopes, weights, small_n, k // prime)
                        assert (large - small) % modulus == 0
                        checks += 1
    return checks


def check_a333473() -> int:
    expected = (1, 2, 12, 92, 752, 6352, 54768, 478928, 4231424)
    checks = 0
    for n, value in enumerate(expected):
        assert a333473(n) == value
        checks += 1
    for n in range(1, 30):
        assert a333473(n) == mixed_sum((1, -1), (1, 2), 1, n)
        checks += 1
    for prime in (3, 5, 7, 11, 13):
        for n in (1, 2, 3, 4):
            for level in (1, 2, 3):
                large_n = n * prime**level
                if large_n > 700:
                    continue
                difference = a333473(large_n) - a333473(large_n // prime)
                assert difference % prime ** (2 * level) == 0
                checks += 1
    return checks


def check_a333473_algebraic_family() -> int:
    checks = 0
    for r in (1, 2, 3):
        for s in (1, 2, 3):
            for n in range(1, 6):
                degree = r * n
                base = schroeder_substitution_series(degree)
                direct = power_series_coefficient(base, s * n, degree)
                assert algebraic_family_lagrange(r, s, n) == direct
                checks += 1

    for r in (1, 2, 3):
        for s in (1, 2, 3):
            for prime in (5, 7):
                for n in (1, 2):
                    for level in (1, 2):
                        large_n = n * prime**level
                        small_n = large_n // prime
                        difference = algebraic_family_lagrange(
                            r, s, large_n
                        ) - algebraic_family_lagrange(r, s, small_n)
                        assert difference % prime ** (2 * level) == 0
                        checks += 1
    return checks


def check_closed_denominator_boundaries() -> int:
    checks = 0
    for a, b, prime in ((6, 5, 5), (8, 7, 7), (12, 11, 11)):
        for n in (1, 2):
            for level in (1, 2):
                large = august.triangle_term(
                    a * n * prime**level, b * n * prime**level
                )
                small = august.triangle_term(
                    a * n * prime ** (level - 1),
                    b * n * prime ** (level - 1),
                )
                assert (large - small) % prime ** (3 * level) == 0
                checks += 1
    for prime in (5, 7):
        for coefficient_slope in (prime, 2 * prime):
            for power in (1, 2, 3):
                for level in (1, 2):
                    large = august.chebyshev_coefficient_split(
                        coefficient_slope, power, prime**level
                    )
                    small = august.chebyshev_coefficient_split(
                        coefficient_slope, power, prime ** (level - 1)
                    )
                    assert (large - small) % prime ** (3 * level) == 0
                    checks += 1
    return checks


def check_negative_binomial_status() -> int:
    checks = 0
    for prime in (3, 5, 7, 11, 13):
        for n in (1, 2, 3, 4):
            for level in (1, 2, 3):
                large_n = n * prime**level
                if large_n > 700:
                    continue
                large = august.negative_binomial_sum(large_n)
                small = august.negative_binomial_sum(large_n // prime)
                assert (large - small) % prime ** (3 * level) == 0
                checks += 1
    return checks


def check_a333592_coster_reduction() -> int:
    expected = (1, 2, 14, 146, 1742, 22252, 296438, 4063866)
    checks = 0
    for n, value in enumerate(expected):
        assert a333592(n) == value
        checks += 1
    for n in range(1, 50):
        assert a333592(n) == coster_block(n) + endpoint_square(n)
        checks += 1
    for prime in (5, 7, 11):
        for n in (1, 2, 3):
            for level in (1, 2):
                large_n = n * prime**level
                small_n = large_n // prime
                modulus = prime ** (3 * level)
                assert (a333592(large_n) - a333592(small_n)) % modulus == 0
                assert (coster_block(large_n) - coster_block(small_n)) % modulus == 0
                assert (endpoint_square(large_n) - endpoint_square(small_n)) % modulus == 0
                checks += 3
    return checks


def check_index_dependent_companions() -> int:
    checks = 0

    # Two exact counterexamples to a uniform cubic claim.
    difference = companion_negative(10) - companion_negative(2)
    assert companion_negative(2) == 48
    assert companion_negative(10) == -2_645_496_479_352
    assert valuation(difference, 5) == 2
    checks += 3

    difference = cutoff_companion_negative(5, 2) - cutoff_companion_negative(1, 2)
    assert cutoff_companion_negative(1, 2) == 20
    assert cutoff_companion_negative(5, 2) == 28_417_526_446_039_920
    assert valuation(difference, 5) == 2
    checks += 3

    # The positive-last-factor companions survive the same finite grid.
    for prime in (5, 7, 11):
        for n in (1, 2):
            for level in (1, 2):
                large_n = n * prime**level
                small_n = large_n // prime
                modulus = prime ** (3 * level)
                assert (companion_positive(large_n) - companion_positive(small_n)) % modulus == 0
                checks += 1
                for cutoff in (1, 2, 3):
                    large = cutoff_companion_positive(large_n, cutoff)
                    small = cutoff_companion_positive(small_n, cutoff)
                    assert (large - small) % modulus == 0
                    checks += 1
    return checks


def main() -> None:
    sections = {
        "mixed polynomial theorem": check_mixed_polynomial_theorem(),
        "A333473 quadratic tower": check_a333473(),
        "A333473 algebraic family": check_a333473_algebraic_family(),
        "closed slope boundaries": check_closed_denominator_boundaries(),
        "negative-binomial cubic evidence": check_negative_binomial_status(),
        "A333592 Coster reduction": check_a333592_coster_reduction(),
        "index-dependent companions": check_index_dependent_companions(),
    }
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"August mixed-binomial checks passed: {sum(sections.values())}")


if __name__ == "__main__":
    main()
