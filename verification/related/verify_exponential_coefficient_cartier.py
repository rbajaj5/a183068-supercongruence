"""Exact checks for the universal exponential-coefficient Cartier defect."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def series_mul(left: list[Fraction], right: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: degree + 1 - i]):
            out[i + j] += a * b
    return out


def exp_from_log(logarithm: list[Fraction], degree: int) -> list[Fraction]:
    """Exponentiate a series with zero constant coefficient."""
    out = [Fraction(1)] + [Fraction(0)] * degree
    for n in range(1, degree + 1):
        out[n] = sum(
            Fraction(k) * logarithm[k] * out[n - k]
            for k in range(1, n + 1)
        ) / n
    return out


def source_log(source: list[int], degree: int) -> list[Fraction]:
    return [Fraction(0)] + [Fraction(source[m], m) for m in range(1, degree + 1)]


def euler_power(source: list[int], exponent: int, degree: int) -> list[Fraction]:
    logarithm = source_log(source, degree)
    return exp_from_log([Fraction(exponent) * value for value in logarithm], degree)


def delta(source: list[int], prime: int, degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    logarithm = source_log(source, degree)
    for m in range(1, degree + 1):
        out[m] += prime * logarithm[m]
        if m % prime == 0:
            out[m] -= logarithm[m // prime]
    return out


def cartier(series: list[Fraction], prime: int, degree: int) -> list[Fraction]:
    return [series[prime * m] for m in range(degree + 1)]


def coefficient(source: list[int], c: int, s: int, n: int) -> Fraction:
    degree = s * n
    return euler_power(source[: degree + 1], c * n, degree)[degree]


def cartier_difference(source: list[int], c: int, s: int, n: int, prime: int) -> Fraction:
    degree = s * n
    lifted_degree = prime * degree
    source = source[: lifted_degree + 1]
    base = euler_power(source, c * n, degree)
    defect_log = delta(source, prime, lifted_degree)
    defect_exp = exp_from_log(
        [Fraction(c * n) * value for value in defect_log], lifted_degree
    )
    theta = cartier(defect_exp, prime, degree)
    theta[0] -= 1
    return series_mul(base, theta, degree)[degree]


@lru_cache(maxsize=None)
def apery2(n: int) -> int:
    return sum(comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1))


def source_duchon(degree: int) -> list[int]:
    return [0] + [comb(5 * m, 2 * m) // 5 for m in range(1, degree + 1)]


def source_odd_apery(degree: int) -> list[int]:
    return [0] + [2 * apery2(m) if m % 2 else 0 for m in range(1, degree + 1)]


def source_trinomial(degree: int) -> list[int]:
    return [0] + [factorial(3 * m) // factorial(m) ** 3 for m in range(1, degree + 1)]


def valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    numerator, denominator = value.numerator, value.denominator
    out = 0
    while numerator % prime == 0:
        numerator //= prime
        out += 1
    while denominator % prime == 0:
        denominator //= prime
        out -= 1
    return out


def check_delta_formula() -> int:
    checks = 0
    for source in (
        [0] + [m * m - 3 * m + 7 for m in range(1, 31)],
        source_duchon(30),
        source_odd_apery(30),
        source_trinomial(30),
    ):
        for prime in (3, 5, 7):
            actual = delta(source, prime, 30)
            for m in range(1, 31):
                if m % prime:
                    expected = Fraction(prime * source[m], m)
                else:
                    expected = Fraction(source[m] - source[m // prime], m // prime)
                assert actual[m] == expected
                checks += 1
    return checks


def check_universal_identity() -> int:
    checks = 0
    sources = (
        [0] + [m * m + 1 for m in range(1, 41)],
        source_duchon(40),
        source_odd_apery(40),
        source_trinomial(40),
    )
    for source in sources:
        for c, s in ((1, 1), (2, 1), (-1, 2)):
            for prime in (3, 5):
                for n in (1, 2):
                    lhs = coefficient(source, c, s, prime * n) - coefficient(source, c, s, n)
                    rhs = cartier_difference(source, c, s, n, prime)
                    assert lhs == rhs
                    checks += 1
    return checks


def check_specializations() -> int:
    checks = 0
    duchon_expected = [1, 2, 23, 377, 7229, 151491, 3361598]
    a362722_expected = [1, 6, 72, 1266, 23232, 445506, 8740728]
    a362733_expected = [1, 6, 234, 10428, 492522, 24033006, 1197423396]

    degree = 12
    duchon_e = euler_power(source_duchon(degree), 1, degree)
    for n, expected in enumerate(duchon_expected):
        assert duchon_e[n] == expected
        checks += 1

    odd = source_odd_apery(degree)
    tri = source_trinomial(degree)
    for n, expected in enumerate(a362722_expected):
        actual = Fraction(1) if n == 0 else coefficient(odd, 1, 1, n)
        assert actual == expected
        checks += 1
    for n, expected in enumerate(a362733_expected):
        actual = Fraction(1) if n == 0 else coefficient(tri, 2, 1, n) / 2
        assert actual == expected
        checks += 1

    # One nonlinear A060941 iteration. Rational values are intentional.
    previous = [int(value) for value in duchon_e]
    next_expected = [
        Fraction(2),
        Fraction(31),
        Fraction(620),
        Fraction(13951),
        Fraction(1345389, 4),
        Fraction(42438173, 5),
        Fraction(4425312797, 20),
    ]
    for n, expected in enumerate(next_expected, 1):
        value = coefficient(previous, 1, 1, n)
        assert value == expected
        checks += 1
    return checks


def check_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for prime in (5, 7):
        degree = 2 * prime * prime
        duchon = source_duchon(degree)
        odd = source_odd_apery(degree)
        tri = source_trinomial(degree)
        first_level_cases = [
            (odd, 1, 1, 2),
            (tri, 2, 2, 3),
        ]
        if prime >= 7:
            first_level_cases.append((duchon, 1, 1, 3))
        for source, c, divisor, required in first_level_cases:
            high = coefficient(source, c, 1, prime)
            low = coefficient(source, c, 1, 1)
            difference = (high - low) / divisor
            depth = valuation(difference, prime)
            assert depth >= required
            sharp += int(depth == required)
            checks += 1

        # Second level for one representative of each source family.
        second_level_cases = [
            (odd, 1, 1, 4),
            (tri, 2, 2, 6),
        ]
        if prime >= 7:
            second_level_cases.append((duchon, 1, 1, 6))
        for source, c, divisor, required in second_level_cases:
            high = coefficient(source, c, 1, prime * prime)
            low = coefficient(source, c, 1, prime)
            depth = valuation((high - low) / divisor, prime)
            assert depth >= required
            sharp += int(depth == required)
            checks += 1

    # The ternary boundary claimed by A362733.
    tri = source_trinomial(18)
    for n in (1, 2):
        difference = (coefficient(tri, 2, 1, 3 * n) - coefficient(tri, 2, 1, n)) / 2
        depth = valuation(difference, 3)
        assert depth >= 3
        sharp += int(depth == 3)
        checks += 1
    return checks, sharp


def main() -> None:
    delta_checks = check_delta_formula()
    identity_checks = check_universal_identity()
    specialization_checks = check_specializations()
    tower_checks, sharp = check_towers()
    print(f"exponential Cartier delta checks: {delta_checks}")
    print(f"exponential Cartier identity checks: {identity_checks}")
    print(f"exponential Cartier specialization checks: {specialization_checks}")
    print(f"exponential coefficient tower checks: {tower_checks} ({sharp} sharp)")
    print("exponential-coefficient Cartier checks passed")


if __name__ == "__main__":
    main()
