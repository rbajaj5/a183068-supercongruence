"""Exact checks for the higher August defect reduction.

This verifies the exact three-level and shell identities and tests the
remaining conjectural valuation.  It is not a proof of that valuation.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb

from verify_bala_august_mixed_binomial_follow_on import (
    negative_binomial_sum_mod,
)
from verify_bala_august_kernel_frobenius import (
    KernelCoefficients,
    rational_valuation,
)


def summand(n: int, k: int) -> int:
    return comb(n + k - 1, k) * comb(2 * n + k - 1, k)


def exact_sum(n: int) -> int:
    return sum(summand(n, k) for k in range(n + 1))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def check_three_level_equivalence() -> int:
    checks = 0
    for prime in (5, 7, 11):
        loss = int(prime == 5)
        for n in range(1, 5):
            for level in (2, 3):
                high = exact_sum(n * prime**level)
                middle = exact_sum(n * prime ** (level - 1))
                low = exact_sum(n * prime ** (level - 2))
                q_high = (high - middle) // prime ** (3 * level)
                q_low = (middle - low) // prime ** (3 * level - 3)
                residual = high - (1 + prime**3) * middle + prime**3 * low
                assert residual == prime ** (3 * level) * (q_high - q_low)
                assert residual % prime ** (5 * level - 2 - loss) == 0
                checks += 2
    return checks


def check_shell_decomposition() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for n in (1, 2):
            for level in (2, 3):
                high_n = n * prime**level
                middle_n = high_n // prime
                low_n = middle_n // prime
                unit = sum(
                    summand(high_n, k)
                    for k in range(high_n + 1)
                    if k % prime
                )
                once = sum(
                    summand(high_n, prime * q)
                    - (1 + prime**3) * summand(middle_n, q)
                    for q in range(1, middle_n + 1)
                    if q % prime
                )
                twice = sum(
                    summand(high_n, prime * prime * q)
                    - (1 + prime**3) * summand(middle_n, prime * q)
                    + prime**3 * summand(low_n, q)
                    for q in range(low_n + 1)
                )
                residual = (
                    exact_sum(high_n)
                    - (1 + prime**3) * exact_sum(middle_n)
                    + prime**3 * exact_sum(low_n)
                )
                assert unit + once + twice == residual
                checks += 1
    return checks


def jacobsthal_quotient(prime: int, a: int, b: int) -> Fraction:
    return Fraction(comb(prime * a, prime * b), comb(a, b))


def check_scaled_summand_factorization() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for middle in range(1, 9):
            for q in range(1, 9):
                left = Fraction(summand(prime * middle, prime * q), summand(middle, q))
                right = jacobsthal_quotient(
                    prime, middle + q, q
                ) * jacobsthal_quotient(prime, 2 * middle + q, q)
                assert left == right
                checks += 1
    return checks


def check_unit_reduction() -> int:
    checks = 0
    for prime in (5, 7):
        for unit in (1, 2, 3):
            assert unit % prime
            for shift in (1,):
                for level in (1, 2):
                    n = prime**shift * unit
                    direct = exact_sum(n * prime**level) - exact_sum(
                        n * prime ** (level - 1)
                    )
                    shifted = exact_sum(unit * prime ** (level + shift)) - exact_sum(
                        unit * prime ** (level + shift - 1)
                    )
                    assert direct == shifted
                    checks += 1
    return checks


def check_quartic_coefficient_lift() -> int:
    checks = 0
    configurations = (
        (5, 1, 2, 9),
        (5, 1, 1, 7),
        (7, 1, 2, 7),
        (7, 2, 3, 6),
        (11, 1, 2, 4),
        (13, 1, 2, 3),
    )
    for prime, a, b, window in configurations:
        engine = KernelCoefficients(prime, a, b)
        loss = int(prime == 5)
        for m in range(window + 1):
            for n in range(window + 1):
                if m == 0 and n == 0:
                    continue
                coefficient = engine.h_l_power(4, prime * m, prime * n)
                required = 1 - loss + min(valuation(m, prime), valuation(n, prime))
                assert rational_valuation(coefficient, prime) >= required
                lifted = engine.h_l_power(
                    4, prime * prime * m, prime * prime * n
                ) - prime * coefficient
                assert rational_valuation(lifted, prime) >= required + 1
                checks += 2
    return checks


def multiply_bivariate_mod(
    first: dict[tuple[int, int], int],
    second: dict[tuple[int, int], int],
    prime: int,
) -> dict[tuple[int, int], int]:
    result: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (m, n), a in first.items():
        for (u, v), b in second.items():
            result[m + u, n + v] = (result[m + u, n + v] + a * b) % prime
    return dict(result)


def check_finite_log_quartic_identity() -> int:
    checks = 0
    for prime in (7, 11, 13, 17, 19):
        one = {(0, 0): 1}
        finite_x = {(a, 0): pow(a, -1, prime) for a in range(1, prime)}
        finite_y = {(0, a): pow(a, -1, prime) for a in range(1, prime)}
        diagonal = {(a, a): 1 for a in range(prime)}
        for x_power in range(5):
            polynomial = one
            for _ in range(x_power):
                polynomial = multiply_bivariate_mod(polynomial, finite_x, prime)
            for _ in range(4 - x_power):
                polynomial = multiply_bivariate_mod(polynomial, finite_y, prime)
            polynomial = multiply_bivariate_mod(polynomial, diagonal, prime)
            cartier = {
                (m // prime, n // prime): value
                for (m, n), value in polynomial.items()
                if m % prime == 0 and n % prime == 0 and value % prime
            }
            assert not cartier
            checks += 1
    return checks


def kernel_moment(
    kernel: dict[tuple[int, int], Fraction],
    exponent: int,
    a: int,
    b: int,
    c: int,
) -> Fraction:
    result = Fraction(0)
    boundary = c * exponent
    for m in range(boundary + 1):
        x_shift = boundary - m
        x_coefficient = comb(a * exponent + x_shift - 1, x_shift)
        for n in range(boundary + 1):
            y_shift = boundary - n
            y_coefficient = comb(b * exponent + y_shift - 1, y_shift)
            result += kernel[m, n] * x_coefficient * y_coefficient
    return result


def check_cubic_kernel_contraction() -> int:
    checks = 0
    configurations = (
        (5, 1, 2, 1, 8),
        (7, 1, 2, 1, 6),
        (11, 1, 2, 1, 3),
        (13, 1, 2, 1, 2),
    )
    for prime, a, b, c, maximum_exponent in configurations:
        engine = KernelCoefficients(prime, a, b)
        maximum = prime * c * maximum_exponent
        first, second = engine.primitives(maximum)
        kernel = engine.defect_kernel(c, maximum, first, second)
        loss = int(prime == 5)
        for exponent in range(1, maximum_exponent + 1):
            high = kernel_moment(kernel, prime * exponent, a, b, c)
            low = kernel_moment(kernel, exponent, a, b, c)
            required = 2 * valuation(exponent, prime) + 2 - loss
            assert rational_valuation(high - low, prime) >= required
            checks += 1
    return checks


def check_modular_grid() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23):
        loss = int(prime == 5)
        sharp = False
        for n in range(1, 9):
            normalized: dict[int, int] = {}
            for level in (1, 2, 3, 4):
                if n * prime**level > 120_000:
                    continue
                precision = 3 * level + 8
                high = negative_binomial_sum_mod(
                    n * prime**level, prime, precision
                )
                low = negative_binomial_sum_mod(
                    n * prime ** (level - 1), prime, precision
                )
                difference = (high - low) % prime**precision
                assert difference % prime ** (3 * level) == 0
                normalized[level] = difference // prime ** (3 * level)
                checks += 1
            for level in range(2, max(normalized) + 1):
                required = 2 * level - 2 - loss
                delta = normalized[level] - normalized[level - 1]
                assert delta % prime**required == 0
                if valuation(delta, prime) == required:
                    sharp = True
                checks += 1
        assert sharp or prime == 23  # the bounded p=23 grid can gain accidentally
        checks += 1
    return checks


def main() -> None:
    results = {
        "three-level equivalence": check_three_level_equivalence(),
        "valuation-shell identity": check_shell_decomposition(),
        "scaled-summand factorization": check_scaled_summand_factorization(),
        "unit-index reduction": check_unit_reduction(),
        "finite-log quartic identity": check_finite_log_quartic_identity(),
        "quartic coefficient lift": check_quartic_coefficient_lift(),
        "cubic-kernel contraction evidence": check_cubic_kernel_contraction(),
        "higher-defect evidence": check_modular_grid(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
