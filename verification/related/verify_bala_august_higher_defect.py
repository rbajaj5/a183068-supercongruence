"""Exact checks for the higher August normalized-defect theorem.

This verifies the exact three-level and shell identities, the two
coefficient filtrations in the second Cartier-connection lemma, its exact
covariant-Hessian factorization, and the resulting valuation on a modular
grid.  The checks support transcription/debugging; the note contains the
proof.
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


def minimum_index_valuation(m: int, n: int, prime: int) -> int:
    """The finite value min(v_p(m),v_p(n)) away from the origin."""

    assert m != 0 or n != 0
    return min(valuation(m, prime), valuation(n, prime))


def check_second_cartier_connection() -> int:
    """Check Lemma 5, equations (27)--(31), with exact rationals."""

    checks = 0
    configurations = ((5, 7), (7, 7), (11, 3), (13, 2))
    for prime, window in configurations:
        exponent = 1 if prime == 5 else 2
        engine = KernelCoefficients(prime, 1, 2)
        maximum = prime * window
        first, second = engine.primitives(maximum)
        kernel = engine.defect_kernel(1, maximum, first, second)

        a_x: dict[tuple[int, int], Fraction] = {}
        a_y: dict[tuple[int, int], Fraction] = {}
        residual: dict[tuple[int, int], Fraction] = {}

        for m in range(window + 1):
            for n in range(window + 1):
                coefficient = kernel[prime * m, prime * n] - kernel[m, n]
                residual[m, n] = coefficient
                if m == 0 and n == 0:
                    assert coefficient == 0
                    checks += 1
                    continue
                index_valuation = minimum_index_valuation(m, n, prime)
                assert rational_valuation(coefficient, prime) >= (
                    exponent + 2 * index_valuation
                )
                if m != 0 and valuation(m, prime) <= valuation(n, prime):
                    a_x[m, n] = coefficient / (prime**exponent * m * m)
                    reconstructed = prime**exponent * m * m * a_x[m, n]
                else:
                    a_y[m, n] = coefficient / (prime**exponent * n * n)
                    reconstructed = prime**exponent * n * n * a_y[m, n]
                assert reconstructed == coefficient
                checks += 2

        connection: dict[tuple[int, int], Fraction] = {}
        hessian: dict[tuple[int, int], Fraction] = {}
        tangent: dict[tuple[int, int], Fraction] = {}
        vector_x: dict[tuple[int, int], Fraction] = {}
        vector_y: dict[tuple[int, int], Fraction] = {}

        for m in range(window + 1):
            for n in range(window + 1):
                # [x^m y^n] C_p(B L_p), with L_p=V_p(x)+2V_p(y).
                c_mn = sum(
                    (
                        kernel[prime * m - q, prime * n] / q
                        for q in range(1, prime * m + 1)
                        if q % prime
                    ),
                    Fraction(0),
                )
                c_mn += 2 * sum(
                    (
                        kernel[prime * m, prime * n - q] / q
                        for q in range(1, prime * n + 1)
                        if q % prime
                    ),
                    Fraction(0),
                )
                connection[m, n] = c_mn

                # D_x^2 log G=sum(q x^q), D_y^2 log G=2 sum(q y^q).
                h_mn = sum(
                    (q * a_x.get((m - q, n), Fraction(0)) for q in range(1, m + 1)),
                    Fraction(0),
                )
                h_mn += 2 * sum(
                    (q * a_y.get((m, n - q), Fraction(0)) for q in range(1, n + 1)),
                    Fraction(0),
                )
                hessian[m, n] = h_mn
                j_mn = c_mn + prime ** (exponent - 1) * h_mn
                tangent[m, n] = j_mn

                if m == 0 and n == 0:
                    assert j_mn == 0
                    checks += 1
                    continue
                index_valuation = minimum_index_valuation(m, n, prime)
                assert rational_valuation(j_mn, prime) >= (
                    exponent - 1 + index_valuation
                )
                normalized = j_mn / prime ** (exponent - 1)
                if m != 0 and valuation(m, prime) <= valuation(n, prime):
                    vector_x[m, n] = normalized / m
                    reconstructed = prime ** (exponent - 1) * m * vector_x[m, n]
                else:
                    vector_y[m, n] = normalized / n
                    reconstructed = prime ** (exponent - 1) * n * vector_y[m, n]
                assert reconstructed == j_mn
                checks += 2

        # The two displayed decompositions are exact coefficient identities,
        # not merely valuation tests.
        for key in residual:
            m, n = key
            reconstructed_r = prime**exponent * (
                m * m * a_x.get(key, Fraction(0))
                + n * n * a_y.get(key, Fraction(0))
            )
            reconstructed_j = prime ** (exponent - 1) * (
                m * vector_x.get(key, Fraction(0))
                + n * vector_y.get(key, Fraction(0))
            )
            assert reconstructed_r == residual[key]
            assert reconstructed_j == tangent[key]
            checks += 2

        def dense(
            series: dict[tuple[int, int], Fraction], bound: int
        ) -> dict[tuple[int, int], Fraction]:
            return {
                (m, n): series.get((m, n), Fraction(0))
                for m in range(bound + 1)
                for n in range(bound + 1)
            }

        def multiply_axis(
            series: dict[tuple[int, int], Fraction],
            coefficients: dict[int, Fraction],
            bound: int,
            x_axis: bool,
        ) -> dict[tuple[int, int], Fraction]:
            product: dict[tuple[int, int], Fraction] = {}
            for m in range(bound + 1):
                for n in range(bound + 1):
                    product[m, n] = sum(
                        (
                            series.get(
                                (m - q, n) if x_axis else (m, n - q),
                                Fraction(0),
                            )
                            * coefficient
                            for q, coefficient in coefficients.items()
                            if q <= (m if x_axis else n)
                        ),
                        Fraction(0),
                    )
            return product

        # Check the exact moment identity (38), including both Hessian signs.
        # In this specialization l_x=-1+x/(1-x), l_y=-1+2y/(1-y).
        for moment_exponent in range(1, min(window, 4) + 1):
            bound = moment_exponent
            lx_squared = {0: Fraction(1)}
            lx_squared.update({q: Fraction(q - 3) for q in range(1, bound + 1)})
            ly_squared = {0: Fraction(1)}
            ly_squared.update({q: Fraction(4 * q - 8) for q in range(1, bound + 1)})
            lx = {0: Fraction(-1)}
            lx.update({q: Fraction(1) for q in range(1, bound + 1)})
            ly = {0: Fraction(-1)}
            ly.update({q: Fraction(2) for q in range(1, bound + 1)})

            quadratic = multiply_axis(a_x, lx_squared, bound, True)
            y_quadratic = multiply_axis(a_y, ly_squared, bound, False)
            x_vector = multiply_axis(vector_x, lx, bound, True)
            y_vector = multiply_axis(vector_y, ly, bound, False)
            final_series = {
                (m, n): quadratic[m, n]
                + y_quadratic[m, n]
                - x_vector[m, n]
                - y_vector[m, n]
                for m in range(bound + 1)
                for n in range(bound + 1)
            }

            left = kernel_moment(dense(residual, bound), bound, 1, 2, 1)
            left += prime * bound * kernel_moment(
                dense(connection, bound), bound, 1, 2, 1
            )
            right = prime**exponent * bound**2 * kernel_moment(
                final_series, bound, 1, 2, 1
            )
            assert left == right
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
        "second Cartier connection": check_second_cartier_connection(),
        "cubic-kernel contraction": check_cubic_kernel_contraction(),
        "higher-defect theorem": check_modular_grid(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
