#!/usr/bin/env python3
"""Exact checks for GaussianWolstenholmeCitationNetwork.md."""

from __future__ import annotations

from math import comb


Gaussian = tuple[int, int]


def primes_through(limit: int) -> list[int]:
    primes: list[int] = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            primes.append(n)
    return primes


def gadd(x: Gaussian, y: Gaussian, modulus: int) -> Gaussian:
    return ((x[0] + y[0]) % modulus, (x[1] + y[1]) % modulus)


def gmul(x: Gaussian, y: Gaussian, modulus: int) -> Gaussian:
    a, b = x
    c, d = y
    return ((a * c - b * d) % modulus, (a * d + b * c) % modulus)


def gpow(x: Gaussian, exponent: int, modulus: int) -> Gaussian:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = gmul(result, x, modulus)
        x = gmul(x, x, modulus)
        exponent //= 2
    return result


def ginv(a: int, b: int, modulus: int) -> Gaussian:
    norm_inverse = pow((a * a + b * b) % modulus, -1, modulus)
    return (a * norm_inverse % modulus, -b * norm_inverse % modulus)


def domain(p: int) -> list[Gaussian]:
    return [
        (a, b)
        for a in range(1, p)
        for b in range(1, p)
        if (a * a + b * b) % p
    ]


def reciprocal_sum(p: int, k: int, power: int) -> Gaussian:
    modulus = p**power
    total = (0, 0)
    for a, b in domain(p):
        total = gadd(total, gpow(ginv(a, b, modulus), k, modulus), modulus)
    return total


def multiply_linear(
    coefficients: list[Gaussian], root: Gaussian, p: int
) -> list[Gaussian]:
    result = [(0, 0)] * (len(coefficients) + 1)
    minus_root = (-root[0] % p, -root[1] % p)
    for degree, coefficient in enumerate(coefficients):
        result[degree] = gadd(
            result[degree], gmul(coefficient, minus_root, p), p
        )
        result[degree + 1] = gadd(
            result[degree + 1], coefficient, p
        )
    return result


def direct_polynomial(p: int) -> list[Gaussian]:
    coefficients = [(1, 0)]
    for root in domain(p):
        coefficients = multiply_linear(coefficients, root, p)
    return coefficients


def expected_polynomial(p: int) -> list[Gaussian]:
    degree = len(domain(p))
    coefficients = [(0, 0)] * (degree + 1)
    if p % 4 == 3:
        for j in range((p - 1) // 2 + 1):
            coefficients[2 * j * (p - 1)] = (1, 0)
    else:
        for j in range(p - 2):
            coefficients[j * (p - 1)] = (comb(j + 2, 2) % p, 0)
    return coefficients


def a_value(p: int, q: int) -> int:
    if p % 4 == 3:
        if q % (p - 1):
            return 0
        if q % (p * p - 1):
            return 2
        return 1
    return 0 if q % (p - 1) else 3


def expected_normalized_residue(p: int, k: int) -> Gaussian:
    r = (-k) % 4
    q = k + r
    coefficient = ((-1) ** r * comb(k + r - 1, r)) % p
    unit = gpow((pow(2, -1, p), pow(2, -1, p)), r, p)
    return gmul((coefficient * a_value(p, q) % p, 0), unit, p)


def normalized_direct_residue(p: int, k: int) -> Gaussian:
    r = (-k) % 4
    modulus_power = r + 1
    total = reciprocal_sum(p, k, modulus_power)
    scale = p**r
    assert total[0] % scale == 0
    assert total[1] % scale == 0
    return ((total[0] // scale) % p, (total[1] // scale) % p)


def vp_integer(value: int, p: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    valuation = 0
    while value % p == 0:
        value //= p
        valuation += 1
    return valuation


def factor_gaussian(
    value: Gaussian, p: int, modulus: int
) -> tuple[int, Gaussian]:
    valuation = min(vp_integer(value[0], p), vp_integer(value[1], p))
    scale = p**valuation
    return (
        valuation,
        (value[0] // scale % modulus, value[1] // scale % modulus),
    )


def factored_product(
    values: list[Gaussian], p: int, modulus: int
) -> tuple[int, Gaussian]:
    valuation = 0
    unit = (1, 0)
    for value in values:
        local_valuation, local_unit = factor_gaussian(value, p, modulus)
        valuation += local_valuation
        unit = gmul(unit, local_unit, modulus)
    return valuation, unit


def rectangular_binomial(
    a: int, b: int, c: int, d: int, p: int, precision: int = 5
) -> tuple[int, Gaussian]:
    modulus = p**precision
    numerator = [
        (a - x, b - y)
        for x in range(c)
        for y in range(d)
    ]
    denominator = [
        (x, y)
        for x in range(1, c + 1)
        for y in range(1, d + 1)
    ]
    numerator_valuation, numerator_unit = factored_product(
        numerator, p, modulus
    )
    denominator_valuation, denominator_unit = factored_product(
        denominator, p, modulus
    )
    inverse_denominator = ginv(
        denominator_unit[0], denominator_unit[1], modulus
    )
    return (
        numerator_valuation - denominator_valuation,
        gmul(numerator_unit, inverse_denominator, modulus),
    )


def congruent_factored(
    left: tuple[int, Gaussian],
    right: tuple[int, Gaussian],
    p: int,
    power: int,
) -> bool:
    left_valuation, left_unit = left
    right_valuation, right_unit = right
    if left_valuation >= power and right_valuation >= power:
        return True
    if left_valuation != right_valuation:
        return False
    required = power - left_valuation
    if required <= 0:
        return True
    modulus = p**required
    return (
        (left_unit[0] - right_unit[0]) % modulus == 0
        and (left_unit[1] - right_unit[1]) % modulus == 0
    )


def complete_block(p: int, z: Gaussian, precision: int = 4) -> Gaussian:
    modulus = p**precision
    result = (1, 0)
    for a in range(1, p + 1):
        for b in range(1, p + 1):
            if a == p and b == p:
                continue
            factor = (p * z[0] + a, p * z[1] + b)
            result = gmul(result, factor, modulus)
    return result


def run() -> None:
    polynomial_checks = 0
    for p in [3, 5, 7, 11, 13, 17, 19, 29]:
        assert direct_polynomial(p) == expected_polynomial(p)
        polynomial_checks += 1

    leading_residue_checks = 0
    for p in [q for q in primes_through(59) if q % 2]:
        for k in range(1, 4 * p + 1):
            assert normalized_direct_residue(
                p, k
            ) == expected_normalized_residue(p, k)
            leading_residue_checks += 1

    family_checks = 0
    for p in [q for q in primes_through(199) if q > 17]:
        k = p - 4 if p % 4 == 1 else 2 * p - 5
        residue = normalized_direct_residue(p, k)
        assert residue != (0, 0)
        family_checks += 1

    p = 19
    k = 33
    total = reciprocal_sum(p, k, 4)
    assert total == (14 * p**3, 5 * p**3)

    block_checks = 0
    for p in [7, 11, 19]:
        base_block = complete_block(p, (0, 0))
        for x in range(4):
            for y in range(4):
                shifted_block = complete_block(p, (x, y))
                assert (shifted_block[0] - base_block[0]) % p**3 == 0
                assert (shifted_block[1] - base_block[1]) % p**3 == 0
                block_checks += 1

    lucas_checks = 0
    for p in [7, 11]:
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, a + 1):
                    for d in range(1, b + 1):
                        small = rectangular_binomial(a, b, c, d, p)
                        scaled = rectangular_binomial(
                            p * a, p * b, p * c, p * d, p
                        )
                        assert congruent_factored(scaled, small, p, 3)
                        lucas_checks += 1

    p3_small = rectangular_binomial(1, 2, 1, 1, 3)
    p3_scaled = rectangular_binomial(3, 6, 3, 3, 3)
    assert not congruent_factored(p3_scaled, p3_small, 3, 3)
    assert congruent_factored(p3_scaled, p3_small, 3, 2)

    print(f"direct polynomial identities: {polynomial_checks}")
    print(f"normalized leading residues: {leading_residue_checks}")
    print(f"infinite-family samples: {family_checks}")
    print("smallest certificate: S_19^(33) = 19^3(14+5i) mod 19^4")
    print(f"translation-invariant residue blocks: {block_checks}")
    print(f"Gaussian Lucas rectangles: {lucas_checks}")
    print("p=3 Lucas boundary: mod 3^2 holds, mod 3^3 fails")


if __name__ == "__main__":
    run()
