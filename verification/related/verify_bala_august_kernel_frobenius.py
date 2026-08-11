"""Coefficient checks for the Frobenius-fixed first-defect kernel.

The conjectural coefficient identity and its proved reductions are recorded in
``related-results/BalaAugustFirstDefectKernel.md``, Section 5.2.  This checker
uses exact rational arithmetic and reduces only at the final p-adic step.

Run with:
    python verification/related/verify_bala_august_kernel_frobenius.py
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def rational_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation(abs(value.numerator), prime) - valuation(
        value.denominator, prime
    )


def mod_prime(value: Fraction, prime: int) -> int:
    assert value.denominator % prime != 0
    return value.numerator * pow(value.denominator, -1, prime) % prime


class KernelCoefficients:
    def __init__(self, prime: int, a: int, b: int) -> None:
        self.prime = prime
        self.a = a
        self.b = b
        self._v_power: dict[tuple[int, int], Fraction] = {}
        self._h_l_power: dict[tuple[int, int, int], Fraction] = {}

    def v_power(self, power: int, degree: int) -> Fraction:
        """Coefficient of z^degree in V_p(z)^power."""

        key = (power, degree)
        if key in self._v_power:
            return self._v_power[key]
        if power == 0:
            result = Fraction(int(degree == 0))
        elif degree <= 0:
            result = Fraction(0)
        else:
            result = sum(
                (
                    Fraction(1, k) * self.v_power(power - 1, degree - k)
                    for k in range(1, degree + 1)
                    if k % self.prime != 0
                ),
                Fraction(0),
            )
        self._v_power[key] = result
        return result

    def l_power(self, power: int, x_degree: int, y_degree: int) -> Fraction:
        return sum(
            (
                comb(power, x_count)
                * self.a**x_count
                * self.b ** (power - x_count)
                * self.v_power(x_count, x_degree)
                * self.v_power(power - x_count, y_degree)
                for x_count in range(power + 1)
            ),
            Fraction(0),
        )

    def h_l_power(self, power: int, x_degree: int, y_degree: int) -> Fraction:
        """Coefficient in H(xy)(aV_p(x)+bV_p(y))^power."""

        key = (power, x_degree, y_degree)
        if key not in self._h_l_power:
            self._h_l_power[key] = sum(
                (
                    self.l_power(power, x_degree - diagonal, y_degree - diagonal)
                    for diagonal in range(min(x_degree, y_degree) + 1)
                ),
                Fraction(0),
            )
        return self._h_l_power[key]

    def primitives(
        self, maximum: int
    ) -> tuple[dict[tuple[int, int], Fraction], dict[tuple[int, int], Fraction]]:
        """Canonical P,Q with C_p(HL^2)/p = D_x P + D_y Q."""

        prime = self.prime
        first: dict[tuple[int, int], Fraction] = {}
        second: dict[tuple[int, int], Fraction] = {}
        for m in range(maximum + 1):
            for n in range(maximum + 1):
                coefficient = self.h_l_power(2, prime * m, prime * n) / prime
                if m == 0 and n == 0:
                    assert coefficient == 0
                elif m != 0 and valuation(m, prime) <= valuation(n, prime):
                    first[m, n] = coefficient / m
                else:
                    second[m, n] = coefficient / n
        return first, second

    def defect_kernel(
        self,
        c: int,
        maximum: int,
        first: dict[tuple[int, int], Fraction],
        second: dict[tuple[int, int], Fraction],
    ) -> dict[tuple[int, int], Fraction]:
        """Canonical coefficients of the first-defect kernel B."""

        prime = self.prime
        result: dict[tuple[int, int], Fraction] = {}
        for m in range(maximum + 1):
            for n in range(maximum + 1):
                first_times_log = -c * first.get((m, n), Fraction(0))
                first_times_log += self.a * sum(
                    (first.get((m - q, n), Fraction(0)) for q in range(1, m + 1)),
                    Fraction(0),
                )
                second_times_log = -c * second.get((m, n), Fraction(0))
                second_times_log += self.b * sum(
                    (second.get((m, n - q), Fraction(0)) for q in range(1, n + 1)),
                    Fraction(0),
                )
                coefficient = self.h_l_power(3, prime * m, prime * n) / 6
                coefficient -= (first_times_log + second_times_log) / 2
                assert coefficient.denominator % prime != 0
                result[m, n] = coefficient
        return result


def check_configuration(prime: int, a: int, b: int, c: int, window: int) -> int:
    engine = KernelCoefficients(prime, a, b)
    maximum = prime * window
    first, second = engine.primitives(maximum)
    kernel = engine.defect_kernel(c, maximum, first, second)
    checks = 0

    for m in range(window + 1):
        for n in range(window + 1):
            # Lifted reciprocal-square congruence.  This is exactly the
            # valuation needed to make the canonical primitives fixed.
            if m != 0 or n != 0:
                lifted_square = engine.h_l_power(
                    2, prime * prime * m, prime * prime * n
                ) - prime * engine.h_l_power(2, prime * m, prime * n)
                required = 3 + min(valuation(m, prime), valuation(n, prime))
                assert rational_valuation(lifted_square, prime) >= required
                checks += 1

            assert mod_prime(first.get((prime * m, prime * n), Fraction(0)), prime) == mod_prime(
                first.get((m, n), Fraction(0)), prime
            )
            assert mod_prime(second.get((prime * m, prime * n), Fraction(0)), prime) == mod_prime(
                second.get((m, n), Fraction(0)), prime
            )
            checks += 2

            # Stronger-than-needed observation: the canonical defect kernel
            # itself, not merely its period class, is Cartier-fixed modulo p.
            assert mod_prime(kernel[prime * m, prime * n], prime) == mod_prime(
                kernel[m, n], prime
            )
            checks += 1
    return checks


def main() -> None:
    configurations = (
        (5, 1, 2, 1, 7),
        (5, 1, 1, 1, 6),
        (5, 2, 3, 2, 6),
        (5, 4, 3, 5, 6),
        (7, 1, 2, 1, 6),
        (7, 2, 3, 2, 5),
        (7, 1, 2, 7, 5),
        (11, 1, 2, 1, 3),
    )
    total = 0
    for configuration in configurations:
        count = check_configuration(*configuration)
        print(f"{configuration}: {count} exact coefficient checks")
        total += count
    print(f"total: {total} exact coefficient checks")


if __name__ == "__main__":
    main()
