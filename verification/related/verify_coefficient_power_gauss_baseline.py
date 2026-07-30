"""Exact checks for CoefficientPowerGaussBaseline.md.

The script is a regression certificate, not a proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
from random import Random


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def multiply(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > degree:
                break
            out[i + j] += a * b
    return out


def power(series: list[Fraction], exponent: int, degree: int) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * degree
    base = (series + [Fraction(0)] * (degree + 1))[: degree + 1]
    while exponent:
        if exponent & 1:
            out = multiply(out, base, degree)
        exponent //= 2
        if exponent:
            base = multiply(base, base, degree)
    return out


def compose(
    outer: list[Fraction], inner: list[Fraction], degree: int
) -> list[Fraction]:
    assert inner[0] == 0
    out = [Fraction(0) for _ in range(degree + 1)]
    term = [Fraction(1)] + [Fraction(0)] * degree
    for coefficient in outer[: degree + 1]:
        for j in range(degree + 1):
            out[j] += coefficient * term[j]
        term = multiply(term, inner, degree)
    return out


def a002897(n: int) -> int:
    return comb(2 * n, n) ** 3


def a008978(n: int) -> int:
    return factorial(5 * n) // factorial(n) ** 5


def a113424(n: int) -> int:
    return factorial(6 * n) // (
        factorial(3 * n) * factorial(2 * n) * factorial(n)
    )


PACKETS = {
    "A002897": (a002897, 8),
    "A008978": (a008978, 120),
    "A113424": (a113424, 60),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    out = 1
    prime = 2
    while prime * prime <= n:
        if n % prime:
            prime += 1
            continue
        n //= prime
        if n % prime == 0:
            return 0
        out = -out
        while n % prime == 0:
            n //= prime
        prime += 1
    return -out if n > 1 else out


def coefficient_root(function, scale: int, degree: int) -> list[Fraction]:
    root = [Fraction(1)]
    for n in range(1, degree + 1):
        trial = root + [Fraction(0)]
        known = power(trial, scale * n, n)[n]
        root.append(Fraction(function(n) - known, scale * n))
    return root


def exponential_companion(function, scale: int, degree: int) -> list[Fraction]:
    out = [Fraction(1)]
    for n in range(1, degree + 1):
        coefficient = sum(
            Fraction(function(k), scale) * out[n - k]
            for k in range(1, n + 1)
        ) / n
        out.append(coefficient)
    return out


def variable_power(series: list[Fraction], parameter: int, n: int) -> Fraction:
    return power(series, parameter * n, n)[n]


def check_integral_packets() -> tuple[int, dict[str, list[int]], dict[str, list[int]]]:
    checks = 0
    roots: dict[str, list[int]] = {}
    companions: dict[str, list[int]] = {}
    for name, (function, scale) in PACKETS.items():
        for n in range(1, 101):
            assert function(n) % scale == 0
            checks += 1

        root_q = coefficient_root(function, scale, 8)
        companion_q = exponential_companion(function, scale, 8)
        assert all(value.denominator == 1 for value in root_q)
        assert all(value.denominator == 1 for value in companion_q)
        root = [value.numerator for value in root_q]
        companion = [value.numerator for value in companion_q]
        roots[name] = root
        companions[name] = companion
        checks += 18

        for n in range(1, 61):
            numerator = sum(
                mobius(n // d) * (function(d) // scale)
                for d in divisors(n)
            )
            assert numerator % n == 0
            checks += 1

        for n in range(1, 9):
            assert variable_power(root_q, scale, n) == function(n)
            checks += 1

        e_power = power(companion_q, scale, 8)
        inner = [Fraction(0)] + e_power[:8]
        assert compose(root_q, inner, 8) == companion_q
        checks += 9

        for parameter in range(1, 7):
            for n in range(1, 8):
                left = (parameter + scale) * variable_power(
                    companion_q, parameter, n
                )
                right = parameter * variable_power(
                    root_q, parameter + scale, n
                )
                assert left == right
                checks += 1

    assert roots["A002897"][:7] == [1, 1, 6, 111, 2806, 84456, 2832589]
    assert roots["A008978"][:7] == [
        1,
        1,
        353,
        318986,
        408941594,
        633438203535,
        1105336091531052,
    ]
    assert companions["A008978"][:7] == [
        1,
        1,
        473,
        467606,
        637121154,
        1039792179805,
        1905441263652576,
    ]
    assert roots["A113424"][:7] == [
        1,
        1,
        56,
        7355,
        1290319,
        264117464,
        59508459679,
    ]
    checks += 4
    return checks, roots, companions


def check_normalized_gauss() -> int:
    checks = 0
    for function, scale in PACKETS.values():
        for prime in (2, 3, 5, 7, 11):
            for r in (1, 2):
                for n in range(1, 5):
                    high = function(n * prime**r) // scale
                    low = function(n * prime ** (r - 1)) // scale
                    assert (high - low) % prime**r == 0
                    checks += 1
    return checks


def check_lifting_lemma() -> int:
    checks = 0
    for prime in (2, 3, 5, 7):
        for exponent in range(0, 3):
            for unit_factor in range(1, 5):
                m = prime**exponent * unit_factor
                for weight in range(-6, 7):
                    difference = weight ** (prime * m) - weight**m
                    assert valuation(difference, prime) >= exponent + 1
                    checks += 1
    return checks


def check_universal_tower() -> tuple[int, int]:
    rng = Random(20260730)
    checks = 0
    sharp = 0
    series_family = [
        [Fraction(1), Fraction(1)],
        [Fraction(2), Fraction(-1), Fraction(3)],
    ]
    for _ in range(8):
        series_family.append(
            [Fraction(rng.randint(-3, 3)) for _ in range(70)]
        )

    for series in series_family:
        for parameter in range(1, 4):
            for prime in (2, 3, 5):
                for r in (1, 2):
                    for n in (1, 2):
                        high_index = n * prime**r
                        if high_index > 60:
                            continue
                        high = variable_power(series, parameter, high_index)
                        low = variable_power(
                            series, parameter, high_index // prime
                        )
                        assert high.denominator == low.denominator == 1
                        assert (high.numerator - low.numerator) % prime**r == 0
                        difference = high.numerator - low.numerator
                        if difference and valuation(difference, prime) == r:
                            sharp += 1
                        checks += 1
    assert sharp > 0
    return checks, sharp


def main() -> None:
    packet_checks, roots, companions = check_integral_packets()
    gauss_checks = check_normalized_gauss()
    lifting_checks = check_lifting_lemma()
    universal_checks, sharp_checks = check_universal_tower()
    total = packet_checks + gauss_checks + lifting_checks + universal_checks
    print("Coefficient-power Gauss baseline checks passed")
    print(f"integrality, root, and Lagrange checks: {packet_checks}")
    print(f"normalized factorial-ratio Gauss checks: {gauss_checks}")
    print(f"integer lifting checks: {lifting_checks}")
    print(f"universal variable-power towers: {universal_checks}")
    print(f"sharp universal witnesses: {sharp_checks}")
    print(f"A008978 F prefix: {roots['A008978'][:6]}")
    print(f"A008978 E prefix: {companions['A008978'][:6]}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
