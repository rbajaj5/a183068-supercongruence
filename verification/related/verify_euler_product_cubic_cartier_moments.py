"""Exact checks for EulerProductCubicCartierMoments.md.

The computation is evidence and transcription control.  The note states
explicitly which two moment estimates remain proof obligations.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


Spec = tuple[tuple[int, int, int], ...]


FAMILIES: tuple[tuple[str, Spec, tuple[int, ...]], ...] = (
    ("A023871", ((1, -1, 2),), (7, 11)),
    ("A023873", ((1, -1, 4),), (7, 11)),
    ("A206622", ((-1, 1, 2), (1, -1, 2)), (5, 7, 11)),
    ("A283271", ((1, 1, 4),), (7, 11)),
)


def valuation_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation_int(value.numerator, prime) - valuation_int(
        value.denominator, prime
    )


def multiply(left: list[int], right: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: degree + 1 - i]):
            if b:
                out[i + j] += a * b
    return out


def factor(exponent: int, epsilon: int, step: int, degree: int) -> list[int]:
    """Truncation of (1-epsilon*x^step)^exponent."""
    out = [0] * (degree + 1)
    for j in range(degree // step + 1):
        if exponent >= 0:
            if j > exponent:
                break
            value = comb(exponent, j) * (-epsilon) ** j
        else:
            value = comb(-exponent + j - 1, j) * epsilon**j
        out[j * step] = value
    return out


def product_power_coefficients(degree: int, scale: int, spec: Spec) -> list[int]:
    """Coefficients through degree for G_spec(x)^scale."""
    out = [1] + [0] * degree
    for part in range(1, degree + 1):
        for epsilon, h, power in spec:
            exponent = h * scale * part**power
            out = multiply(out, factor(exponent, epsilon, part, degree), degree)
    return out


def product_coefficient(degree: int, scale: int, spec: Spec) -> int:
    return product_power_coefficients(degree, scale, spec)[degree]


def ghost_coordinates(maximum: int, spec: Spec) -> list[int]:
    """b_n = n*[x^n] log G_spec(x)."""
    out = [0] * (maximum + 1)
    for part in range(1, maximum + 1):
        for epsilon, h, power in spec:
            weight = -h * part ** (power + 1)
            for quotient in range(1, maximum // part + 1):
                out[part * quotient] += weight * epsilon**quotient
    return out


def reduced_logarithm(maximum: int, prime: int, spec: Spec) -> list[Fraction]:
    ghosts = ghost_coordinates(maximum, spec)
    out = [Fraction(0)] * (maximum + 1)
    for n in range(1, maximum + 1):
        previous = ghosts[n // prime] if n % prime == 0 else 0
        out[n] = Fraction(ghosts[n] - previous, n)
        assert valuation(out[n], prime) >= 0
    return out


def convolve_fraction(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    out = [Fraction(0)] * (degree + 1)
    for i, a in enumerate(left[: degree + 1]):
        if not a:
            continue
        for j, b in enumerate(right[: degree + 1 - i]):
            if b:
                out[i + j] += a * b
    return out


def cartier_power(
    reduced_log: list[Fraction], prime: int, power: int, degree: int
) -> list[Fraction]:
    maximum = prime * degree
    current = [Fraction(1)] + [Fraction(0)] * maximum
    base = reduced_log[: maximum + 1]
    for _ in range(power):
        current = convolve_fraction(current, base, maximum)
    return [current[prime * n] for n in range(degree + 1)]


def coefficient_with_insertion(
    base: list[int], insertion: list[Fraction], degree: int
) -> Fraction:
    return sum(
        (Fraction(base[degree - j]) * insertion[j] for j in range(degree + 1)),
        Fraction(0),
    )


def check_exact_cartier_scaling() -> int:
    checks = 0
    for _, spec, primes in FAMILIES:
        degree_power = spec[0][2]
        for prime in primes:
            reduced = reduced_logarithm(30 * prime, prime, spec)
            for n in range(1, 31):
                assert reduced[prime * n] == prime**degree_power * reduced[n]
                checks += 1
    return checks


def check_quadratic_contraction() -> tuple[int, int]:
    passing = 0
    boundaries = 0
    for _, spec, primes in FAMILIES:
        for prime in primes:
            degree = 24
            reduced = reduced_logarithm(prime * degree, prime, spec)
            square = cartier_power(reduced, prime, 2, degree)
            for n in range(1, degree + 1):
                assert valuation(square[n], prime) >= 1
                passing += 1

    # The reciprocal-square family has the exact excluded-prime failure.
    reciprocal_square = ((1, -1, 2),)
    reduced = reduced_logarithm(5 * 8, 5, reciprocal_square)
    square = cartier_power(reduced, 5, 2, 8)
    assert valuation(square[1], 5) == 0
    boundaries += 1

    # Both fourth-degree signs already contract at five in the checked range.
    for spec in (((1, -1, 4),), ((1, 1, 4),)):
        reduced = reduced_logarithm(5 * 16, 5, spec)
        square = cartier_power(reduced, 5, 2, 16)
        for n in range(1, 17):
            assert valuation(square[n], 5) >= 1
            boundaries += 1
    return passing, boundaries


def moment_data(prime: int, n: int, framing: int, spec: Spec) -> tuple[int, int]:
    degree_power = spec[0][2]
    reduced = reduced_logarithm(prime * n, prime, spec)
    base = product_power_coefficients(n, framing * n, spec)
    first = coefficient_with_insertion(base, reduced[: n + 1], n)
    second_cartier = cartier_power(reduced, prime, 2, n)
    second = coefficient_with_insertion(base, second_cartier, n)
    e = valuation_int(n, prime)
    q = valuation_int(framing, prime)
    first_target = max(0, 2 * e + 2 - degree_power - q)
    second_target = max(0, e + 1 - 2 * q)
    assert valuation(first, prime) >= first_target
    assert valuation(second, prime) >= second_target
    return valuation(first, prime), valuation(second, prime)


def check_moment_bounds() -> int:
    checks = 0
    for _, spec, primes in FAMILIES:
        for prime in primes:
            candidates = (1, 2, prime, 2 * prime, prime * prime)
            for n in candidates:
                for framing in (-2, -1, 1, 2):
                    moment_data(prime, n, framing, spec)
                    checks += 2
    return checks


def check_two_term_reduction() -> int:
    checks = 0
    for _, spec, primes in FAMILIES:
        degree_power = spec[0][2]
        for prime in primes[:2]:
            for n in (1, 2, prime):
                for framing in (-1, 1, 2):
                    reduced = reduced_logarithm(prime * n, prime, spec)
                    base = product_power_coefficients(n, framing * n, spec)
                    first = coefficient_with_insertion(base, reduced[: n + 1], n)
                    second_cartier = cartier_power(reduced, prime, 2, n)
                    second = coefficient_with_insertion(base, second_cartier, n)
                    predicted = (
                        framing * prime ** (degree_power + 1) * n * first
                        + Fraction(framing**2 * prime**2 * n**2, 2) * second
                    )
                    upper = product_coefficient(prime * n, framing * prime * n, spec)
                    lower = product_coefficient(n, framing * n, spec)
                    actual = Fraction(upper - lower)
                    target = 3 * (valuation_int(n, prime) + 1)
                    assert valuation(actual - predicted, prime) >= target
                    checks += 1
    return checks


def check_prime_boundaries() -> int:
    checks = 0
    reciprocal_square = ((1, -1, 2),)
    for r, expected in ((1, 2), (2, 5)):
        upper_n = 5**r
        lower_n = 5 ** (r - 1)
        difference = product_coefficient(upper_n, upper_n, reciprocal_square)
        difference -= product_coefficient(lower_n, lower_n, reciprocal_square)
        assert valuation_int(difference, 5) == expected
        checks += 1

    for spec in (((1, -1, 4),), ((1, 1, 4),)):
        for prime in (5,):
            for r in (1, 2, 3):
                upper_n = prime**r
                lower_n = prime ** (r - 1)
                difference = product_coefficient(upper_n, upper_n, spec)
                difference -= product_coefficient(lower_n, lower_n, spec)
                assert valuation_int(difference, prime) >= 3 * r
                checks += 1

        difference = product_coefficient(3, 3, spec) - product_coefficient(1, 1, spec)
        assert valuation_int(difference, 3) == 2
        checks += 1
    return checks


def main() -> None:
    scaling = check_exact_cartier_scaling()
    contraction, boundaries = check_quadratic_contraction()
    moments = check_moment_bounds()
    reduction = check_two_term_reduction()
    prime_boundaries = check_prime_boundaries()
    total = scaling + contraction + boundaries + moments + reduction + prime_boundaries
    print("Euler-product cubic Cartier-moment checks passed")
    print(f"exact Cartier-scaling checks: {scaling}")
    print(f"quadratic-contraction checks: {contraction}")
    print(f"contraction boundary checks: {boundaries}")
    print(f"weighted-moment checks: {moments}")
    print(f"two-term reduction checks: {reduction}")
    print(f"prime-boundary checks: {prime_boundaries}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
