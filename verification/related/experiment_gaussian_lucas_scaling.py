#!/usr/bin/env python3
"""Exact valuation experiments for Kalinin's rectangular Gaussian coefficient.

This is exploratory code, not part of the proof checker.  It measures

    Q(p^r A,p^r B;p^r C,p^r D)
      - Q(p^(r-1) A,p^(r-1) B;p^(r-1) C,p^(r-1) D)

in the inert p-adic completion and, for split primes, separately at the two
Gaussian primes above p.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from verify_gaussian_wolstenholme import (
    Gaussian,
    gadd,
    ginv,
    gmul,
    rectangular_binomial,
    vp_integer,
)


INFINITY = 10**9


@dataclass(frozen=True)
class ValuationResult:
    valuation: int
    certified_through: int

    @property
    def exact(self) -> bool:
        return self.valuation < self.certified_through

    def display(self) -> str:
        return (
            str(self.valuation)
            if self.exact
            else f">={self.certified_through}"
        )


def inert_difference_valuation(
    left: tuple[int, Gaussian],
    right: tuple[int, Gaussian],
    p: int,
    precision: int,
) -> ValuationResult:
    """Valuation of a difference from p-factored Gaussian residues."""
    left_valuation, left_unit = left
    right_valuation, right_unit = right
    if left_valuation != right_valuation:
        valuation = min(left_valuation, right_valuation)
        return ValuationResult(valuation, valuation + 1)

    modulus = p**precision
    real_difference = (left_unit[0] - right_unit[0]) % modulus
    imaginary_difference = (left_unit[1] - right_unit[1]) % modulus
    unit_valuation = min(
        vp_integer(real_difference, p),
        vp_integer(imaginary_difference, p),
        precision,
    )
    valuation = left_valuation + unit_valuation
    return ValuationResult(valuation, left_valuation + precision)


def inert_adjacent_scale(
    p: int,
    r: int,
    rectangle: tuple[int, int, int, int],
    precision: int = 18,
) -> ValuationResult:
    a, b, c, d = rectangle
    lower_scale = p ** (r - 1)
    upper_scale = p**r
    lower = rectangular_binomial(
        lower_scale * a,
        lower_scale * b,
        lower_scale * c,
        lower_scale * d,
        p,
        precision,
    )
    upper = rectangular_binomial(
        upper_scale * a,
        upper_scale * b,
        upper_scale * c,
        upper_scale * d,
        p,
        precision,
    )
    return inert_difference_valuation(upper, lower, p, precision)


def hensel_root_minus_one(p: int, precision: int, residue: int) -> int:
    """Lift a chosen root of x^2+1 modulo p to modulo p^precision."""
    root = residue % p
    assert (root * root + 1) % p == 0
    modulus = p
    for _ in range(1, precision):
        next_modulus = modulus * p
        for digit in range(p):
            candidate = root + digit * modulus
            if (candidate * candidate + 1) % next_modulus == 0:
                root = candidate
                break
        else:
            raise AssertionError("Hensel lift failed")
        modulus = next_modulus
    return root


def scalar_factor(value: int, p: int, modulus: int) -> tuple[int, int]:
    valuation = min(vp_integer(value, p), INFINITY)
    if valuation >= INFINITY:
        raise ValueError("zero factor encountered")
    unit = value // (p**valuation)
    return valuation, unit % modulus


def split_rectangular_binomial(
    a: int,
    b: int,
    c: int,
    d: int,
    p: int,
    root: int,
    precision: int,
) -> tuple[int, int]:
    """p-factored image of Q under the embedding i -> root in Q_p."""
    modulus = p**precision
    numerator_valuation = 0
    numerator_unit = 1
    for x in range(c):
        for y in range(d):
            valuation, unit = scalar_factor(
                (a - x) + (b - y) * root, p, modulus
            )
            numerator_valuation += valuation
            numerator_unit = numerator_unit * unit % modulus

    denominator_valuation = 0
    denominator_unit = 1
    for x in range(1, c + 1):
        for y in range(1, d + 1):
            valuation, unit = scalar_factor(x + y * root, p, modulus)
            denominator_valuation += valuation
            denominator_unit = denominator_unit * unit % modulus

    return (
        numerator_valuation - denominator_valuation,
        numerator_unit * pow(denominator_unit, -1, modulus) % modulus,
    )


def scalar_difference_valuation(
    left: tuple[int, int],
    right: tuple[int, int],
    p: int,
    precision: int,
) -> ValuationResult:
    left_valuation, left_unit = left
    right_valuation, right_unit = right
    if left_valuation != right_valuation:
        valuation = min(left_valuation, right_valuation)
        return ValuationResult(valuation, valuation + 1)
    modulus = p**precision
    difference = (left_unit - right_unit) % modulus
    unit_valuation = min(vp_integer(difference, p), precision)
    valuation = left_valuation + unit_valuation
    return ValuationResult(valuation, left_valuation + precision)


def split_adjacent_scale(
    p: int,
    gaussian_prime: Gaussian,
    r: int,
    rectangle: tuple[int, int, int, int],
    precision: int = 18,
) -> tuple[ValuationResult, ValuationResult]:
    """Return valuations at pi and conjugate(pi), in that order."""
    u, v = gaussian_prime
    assert u * u + v * v == p and v % p
    root_mod_p = -u * pow(v, -1, p) % p
    pi_root = hensel_root_minus_one(p, precision, root_mod_p)
    conjugate_root = hensel_root_minus_one(p, precision, -root_mod_p)

    a, b, c, d = rectangle
    lower_scale = p ** (r - 1)
    upper_scale = p**r
    results: list[ValuationResult] = []
    for root in (pi_root, conjugate_root):
        lower = split_rectangular_binomial(
            lower_scale * a,
            lower_scale * b,
            lower_scale * c,
            lower_scale * d,
            p,
            root,
            precision,
        )
        upper = split_rectangular_binomial(
            upper_scale * a,
            upper_scale * b,
            upper_scale * c,
            upper_scale * d,
            p,
            root,
            precision,
        )
        results.append(
            scalar_difference_valuation(upper, lower, p, precision)
        )
    return results[0], results[1]


def small_rectangles(bound: int) -> list[tuple[int, int, int, int]]:
    return [
        (a, b, c, d)
        for a in range(1, bound + 1)
        for b in range(1, bound + 1)
        for c in range(1, a + 1)
        for d in range(1, b + 1)
        if (a, b) != (c, d)
    ]


def minimum_result(
    results: list[
        tuple[tuple[int, int, int, int], ValuationResult]
    ],
) -> tuple[int, list[tuple[int, int, int, int]]]:
    minimum = min(result.valuation for _, result in results)
    witnesses = [
        rectangle
        for rectangle, result in results
        if result.valuation == minimum
    ]
    return minimum, witnesses


def check_level_one_leading_term(
    p: int = 7,
    bound: int = 3,
    precision: int = 5,
) -> tuple[int, Gaussian, Gaussian]:
    """Check the explicit leading-term formula modulo p."""
    modulus = p**precision
    reciprocal_sum_1 = (0, 0)
    reciprocal_sum_2 = (0, 0)
    for a in range(1, p + 1):
        for b in range(1, p + 1):
            if a == p and b == p:
                continue
            inverse = ginv(a, b, modulus)
            reciprocal_sum_1 = gadd(
                reciprocal_sum_1, inverse, modulus
            )
            reciprocal_sum_2 = gadd(
                reciprocal_sum_2,
                gmul(inverse, inverse, modulus),
                modulus,
            )

    alpha = (
        reciprocal_sum_1[0] // p**2 % p,
        reciprocal_sum_1[1] // p**2 % p,
    )
    beta = (
        reciprocal_sum_2[0] // p % p,
        reciprocal_sum_2[1] // p % p,
    )
    inverse_two = pow(2, -1, p)
    checks = 0

    for a, b, c, d in small_rectangles(bound):
        lower = rectangular_binomial(
            a, b, c, d, p, precision
        )
        upper = rectangular_binomial(
            p * a, p * b, p * c, p * d, p, precision
        )
        assert lower[0] == upper[0] == 0
        ratio = gmul(
            upper[1],
            ginv(lower[1][0], lower[1][1], modulus),
            modulus,
        )
        actual = (
            ((ratio[0] - 1) % modulus) // p**3 % p,
            (ratio[1] % modulus) // p**3 % p,
        )

        delta = ((a - c) % p, (b - d) % p)
        phi_1 = (c * d * delta[0] % p, c * d * delta[1] % p)
        phi_2 = gmul(phi_1, ((a - 1) % p, (b - 1) % p), p)
        predicted_first = gmul(alpha, phi_1, p)
        predicted_second = gmul(beta, phi_2, p)
        predicted = (
            (
                predicted_first[0]
                - inverse_two * predicted_second[0]
            )
            % p,
            (
                predicted_first[1]
                - inverse_two * predicted_second[1]
            )
            % p,
        )
        assert actual == predicted
        checks += 1

    return checks, alpha, beta


def check_three_adic_leading_term(bound: int = 3) -> int:
    """Check the sharp p=3 leading coefficient at level one."""
    p = 3
    precision = 8
    modulus = p**precision
    alpha = (1, 2)  # 1 - i modulo 3
    checks = 0

    for a, b, c, d in small_rectangles(bound):
        lower = rectangular_binomial(
            a, b, c, d, p, precision
        )
        upper = rectangular_binomial(
            p * a, p * b, p * c, p * d, p, precision
        )
        assert lower[0] == upper[0]
        ratio = gmul(
            upper[1],
            ginv(lower[1][0], lower[1][1], modulus),
            modulus,
        )
        actual = (
            ((ratio[0] - 1) % modulus) // p**2 % p,
            (ratio[1] % modulus) // p**2 % p,
        )
        delta = ((a - c) % p, (b - d) % p)
        phi_1 = (c * d * delta[0] % p, c * d * delta[1] % p)
        predicted = gmul(alpha, phi_1, p)
        assert actual == predicted
        checks += 1

    return checks


def run(deep: bool = False) -> None:
    precision = 18
    rectangles = small_rectangles(3)
    print(f"rectangles in the main grid: {len(rectangles)}")

    print("\nInert-prime theorem calibration (r=1)")
    for p in (7, 11, 19):
        results = [
            (rectangle, inert_adjacent_scale(p, 1, rectangle, precision))
            for rectangle in rectangles
        ]
        minimum, witnesses = minimum_result(results)
        print(
            f"p={p}: min v_p={minimum}; "
            f"equality witnesses={witnesses[:5]}"
        )

    boundary = inert_adjacent_scale(3, 1, (1, 2, 1, 1), precision)
    print(
        "\np=3 boundary (1,2,1,1): "
        f"v_3={boundary.display()}"
    )

    leading_checks, alpha, beta = check_level_one_leading_term()
    print(
        "\nLeading-term formula at p=7: "
        f"{leading_checks} checks; alpha={alpha}; beta={beta}"
    )
    print(
        "Leading-term formula at p=3: "
        f"{check_three_adic_leading_term()} checks; alpha=(1, 2)"
    )

    scaling_rectangles = [
        (1, 2, 1, 1),
        (2, 1, 1, 1),
        (2, 2, 1, 1),
        (2, 2, 1, 2),
        (2, 2, 2, 1),
    ]
    print("\nAdjacent inert scales")
    for p, maximum_r in ((7, 3), (11, 2), (19, 2)):
        for r in range(1, maximum_r + 1):
            results = [
                (
                    rectangle,
                    inert_adjacent_scale(p, r, rectangle, precision),
                )
                for rectangle in scaling_rectangles
            ]
            minimum, witnesses = minimum_result(results)
            displays = ", ".join(
                f"{rectangle}:{result.display()}"
                for rectangle, result in results
            )
            print(
                f"p={p}, r={r}: min={minimum}, "
                f"witnesses={witnesses}; {displays}"
            )

    print("\nSplit-prime adjacent scales")
    for p, gaussian_prime, maximum_r in (
        (5, (2, 1), 3),
        (13, (3, 2), 2),
        (17, (4, 1), 2),
    ):
        for r in range(1, maximum_r + 1):
            values = [
                (
                    rectangle,
                    split_adjacent_scale(
                        p,
                        gaussian_prime,
                        r,
                        rectangle,
                        precision,
                    ),
                )
                for rectangle in scaling_rectangles
            ]
            minimum_pi = min(pair[0].valuation for _, pair in values)
            minimum_conjugate = min(pair[1].valuation for _, pair in values)
            displays = ", ".join(
                f"{rectangle}:({pair[0].display()},{pair[1].display()})"
                for rectangle, pair in values
            )
            print(
                f"p={p}, pi={gaussian_prime}, r={r}: "
                f"min(v_pi,v_pi_bar)=({minimum_pi},{minimum_conjugate}); "
                f"{displays}"
            )

    if deep:
        print("\nDeep inert-prime calibrations")
        rectangle = (1, 2, 1, 1)
        for p, r in ((7, 4), (11, 3), (19, 3)):
            result = inert_adjacent_scale(
                p, r, rectangle, precision=14
            )
            print(
                f"p={p}, r={r}, rectangle={rectangle}: "
                f"v_p={result.display()}"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--deep",
        action="store_true",
        help="also run the expensive p=19, r=3 calibration",
    )
    run(parser.parse_args().deep)
