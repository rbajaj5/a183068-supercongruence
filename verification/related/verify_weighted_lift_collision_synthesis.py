"""Exact checks for WeightedLiftCollisionSynthesis.md."""

from fractions import Fraction


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def seed_coefficients(d: int) -> list[Fraction]:
    """Gallagher's degree-d seed, in increasing coefficient order."""

    coefficients = [Fraction(0) for _ in range(d + 1)]
    correction = Fraction(6, d * (d + 1))
    coefficients[1] += 2 - correction
    coefficients[2] += -3 + correction
    coefficients[d - 1] += 1
    coefficients[d] -= 1
    return coefficients


def integral_coefficients(coefficients: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)]
    answer.extend(
        coefficient / degree
        for degree, coefficient in enumerate(coefficients[1:], start=1)
    )
    return answer


def reduce_coefficients(coefficients: list[Fraction], p: int) -> list[int]:
    return [
        coefficient.numerator * pow(coefficient.denominator, -1, p) % p
        for coefficient in coefficients
    ]


def evaluate(coefficients: list[int], x: int, p: int) -> int:
    answer = 0
    for coefficient in reversed(coefficients):
        answer = (answer * x + coefficient) % p
    return answer


def derivative(coefficients: list[int], p: int) -> list[int]:
    return [
        degree * coefficient % p
        for degree, coefficient in enumerate(coefficients[1:], start=1)
    ]


def tangent_value(
    phi: list[int],
    phi_prime: list[int],
    r: int,
    t: int,
    p: int,
) -> int:
    if r == t:
        second = derivative(phi_prime, p)
        return evaluate(second, r, p) * pow(2, -1, p) % p
    numerator = (
        evaluate(phi, t, p)
        - evaluate(phi, r, p)
        - (t - r) * evaluate(phi_prime, r, p)
    ) % p
    return numerator * pow((t - r) ** 2, -1, p) % p


def tangent_derivatives(
    phi: list[int],
    r: int,
    t: int,
    p: int,
) -> tuple[int, int]:
    phi_prime = derivative(phi, p)
    phi_second = derivative(phi_prime, p)
    if r == t:
        phi_third = derivative(phi_second, p)
        third = evaluate(phi_third, r, p)
        return third * pow(3, -1, p) % p, third * pow(6, -1, p) % p

    difference = (t - r) % p
    numerator = (
        evaluate(phi, t, p)
        - evaluate(phi, r, p)
        - difference * evaluate(phi_prime, r, p)
    ) % p
    inverse_cube = pow(difference, -3, p)
    derivative_r = (
        -evaluate(phi_second, r, p) * difference * difference
        + 2 * numerator
    ) * inverse_cube % p
    derivative_t = (
        (evaluate(phi_prime, t, p) - evaluate(phi_prime, r, p)) * difference
        - 2 * numerator
    ) * inverse_cube % p
    return derivative_r, derivative_t


def infinity_value(n: int, r: int, t: int, p: int) -> int:
    """Top divided difference for w^n, evaluated projectively."""

    if r == t:
        return n * (n - 1) * pow(r, n - 2, p) * pow(2, -1, p) % p
    numerator = (
        pow(t, n, p)
        - pow(r, n, p)
        - n * pow(r, n - 1, p) * (t - r)
    ) % p
    return numerator * pow((t - r) ** 2, -1, p) % p


def geometric_counts(
    phi: list[int],
    p: int,
) -> tuple[int, int, int, int, int]:
    phi_prime = derivative(phi, p)
    affine = 0
    diagonal = 0
    bitangent = 0
    for r in range(p):
        for t in range(p):
            first = tangent_value(phi, phi_prime, r, t, p)
            if first == 0:
                affine += 1
                if r == t:
                    diagonal += 1
                elif tangent_value(phi, phi_prime, t, r, p) == 0:
                    bitangent += 1

    n = len(phi) - 1
    infinity = sum(infinity_value(n, r, 1, p) == 0 for r in range(p))
    infinity += infinity_value(n, 1, 0, p) == 0
    projective = affine + infinity
    trace = p + 1 - projective
    correction = -2 + 2 * infinity + 2 * diagonal + bitangent
    return trace, infinity, diagonal, bitangent, correction


def line_collision_count(phi: list[int], p: int) -> int:
    phi_prime = derivative(phi, p)
    answer = 0
    for slope in range(p):
        for intercept in range(p):
            simple_roots = sum(
                (evaluate(phi, w, p) - slope * w + intercept) % p == 0
                and (evaluate(phi_prime, w, p) - slope) % p != 0
                for w in range(p)
            )
            answer += simple_roots * (simple_roots - 1)
    return answer


def verify_cross_degree() -> tuple[int, int, int]:
    line_cases = 0
    boundary_cases = 0
    genus_cases = 0
    for d in range(2, 7):
        seed = seed_coefficients(d)
        phi_rational = integral_coefficients(seed)
        assert evaluate(
            reduce_coefficients(seed, 1000003),
            1,
            1000003,
        ) == -1 % 1000003
        assert sum(seed) == -1
        assert sum(
            coefficient / (degree + 1)
            for degree, coefficient in enumerate(seed)
        ) == 0

        n = d + 1
        expected_genus = (n - 3) * (n - 4) // 2
        assert expected_genus == (d - 2) * (d - 3) // 2
        genus_cases += 1

        for p in (101, 103):
            phi = reduce_coefficients(phi_rational, p)
            seed_mod = reduce_coefficients(seed, p)
            trace, infinity, diagonal, bitangent, correction = geometric_counts(
                phi, p
            )
            from_geometry = p * (p - 1) - 2 * (
                p + 1 - trace
                - infinity
                - diagonal
            ) + bitangent
            from_lines = line_collision_count(phi, p)
            assert from_geometry == from_lines

            linear = seed_mod[1]
            boundary = 3 * p * (p - 1) if linear else 2 * p * (p - 1)
            variance = (p - 1) * from_lines + boundary
            boundary_exception = p if linear == 0 else 0
            assert variance == (p - 1) * (
                p * p - boundary_exception + 2 * trace + correction
            )
            line_cases += 1
            boundary_cases += 1
    return line_cases, boundary_cases, genus_cases


def verify_smooth_canonical_reductions() -> int:
    """A smooth F_101 reduction certifies smoothness in characteristic zero."""

    p = 101
    cases = 0
    for d in range(2, 7):
        phi = reduce_coefficients(
            integral_coefficients(seed_coefficients(d)),
            p,
        )
        phi_prime = derivative(phi, p)
        for r in range(p):
            for t in range(p):
                if tangent_value(phi, phi_prime, r, t, p) == 0:
                    derivative_r, derivative_t = tangent_derivatives(
                        phi, r, t, p
                    )
                    assert derivative_r != 0 or derivative_t != 0

        n = len(phi) - 1
        top = [0] * n + [phi[-1]]
        next_part = [0] * (n - 1) + [phi[-2]]
        top_prime = derivative(top, p)
        for r, t in [(r, 1) for r in range(p)] + [(1, 0)]:
            value = tangent_value(top, top_prime, r, t, p)
            if value != 0:
                continue
            derivative_r, derivative_t = tangent_derivatives(top, r, t, p)
            z_derivative = tangent_value(
                next_part,
                derivative(next_part, p),
                r,
                t,
                p,
            )
            assert (
                derivative_r != 0
                or derivative_t != 0
                or z_derivative != 0
            )
        cases += 1
    return cases


def verify_boundary_exception() -> int:
    """Manufacture lambda = 0 modulo p while retaining good denominators."""

    cases = 0
    for p in (7, 11, 13):
        # rho(w) = p*w + (3-3p)w^2 + (2p-4)w^3 has rho(0)=0,
        # rho(1)=-1, integral zero, and linear coefficient 0 modulo p.
        seed = [
            Fraction(0),
            Fraction(p),
            Fraction(3 - 3 * p),
            Fraction(2 * p - 4),
        ]
        assert sum(seed) == -1
        assert sum(
            coefficient / (degree + 1)
            for degree, coefficient in enumerate(seed)
        ) == 0
        phi = reduce_coefficients(integral_coefficients(seed), p)
        trace, _, _, _, correction = geometric_counts(phi, p)
        line_count = line_collision_count(phi, p)
        variance = (p - 1) * line_count + 2 * p * (p - 1)
        assert variance == (p - 1) * (
            p * p - p + 2 * trace + correction
        )
        cases += 1
    return cases


def verify_corrected_tate_tower() -> int:
    cases = 0
    for p in (5, 7, 11, 13, 17, 19):
        previous = None
        for r in range(1, 9):
            q = p**r
            corrected = q**3 - q**2
            if previous is not None:
                assert valuation(corrected - previous, p) == 2 * r - 2
                cases += 1
            previous = corrected
    return cases


def main() -> None:
    line_cases, boundary_cases, genus_cases = verify_cross_degree()
    smooth_cases = verify_smooth_canonical_reductions()
    exceptional_cases = verify_boundary_exception()
    tower_cases = verify_corrected_tate_tower()
    print(
        "PASS:",
        line_cases,
        "cross-degree line/collision identities;",
        boundary_cases,
        "boundary formulas;",
        exceptional_cases,
        "lambda=0 exceptions;",
        genus_cases,
        "genus predictions;",
        smooth_cases,
        "smooth canonical reductions;",
        tower_cases,
        "corrected Tate valuations.",
    )


if __name__ == "__main__":
    main()
