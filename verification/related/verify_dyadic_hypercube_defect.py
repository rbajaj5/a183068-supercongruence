"""Exact checks for the dyadic hypercube defect theorem.

The proof is in related-results/DyadicHypercubeDefect.md. These checks are
finite certificates and regression tests, not substitutes for the proof.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EULER_CHECKER = ROOT / "verification/related/verify_euler_product_gaussian_tower.py"
SPEC = importlib.util.spec_from_file_location("euler_tower", EULER_CHECKER)
assert SPEC is not None and SPEC.loader is not None
EULER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EULER)


Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]


def clean(polynomial: Polynomial) -> Polynomial:
    return {monomial: value for monomial, value in polynomial.items() if value}


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    answer = dict(left)
    for monomial, value in right.items():
        answer[monomial] = answer.get(monomial, 0) + value
    return clean(answer)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for alpha, a_value in left.items():
        for beta, b_value in right.items():
            monomial = tuple(a + b for a, b in zip(alpha, beta, strict=True))
            answer[monomial] = answer.get(monomial, 0) + a_value * b_value
    return clean(answer)


def phi(polynomial: Polynomial) -> Polynomial:
    return {
        tuple(2 * exponent for exponent in monomial): value
        for monomial, value in polynomial.items()
    }


def q_exact(polynomial: Polynomial) -> Polynomial:
    numerator = add(
        multiply(polynomial, polynomial),
        {monomial: -value for monomial, value in phi(polynomial).items()},
    )
    assert all(value % 2 == 0 for value in numerator.values())
    return clean({monomial: value // 2 for monomial, value in numerator.items()})


def mod_two(polynomial: Polynomial) -> Polynomial:
    return clean({monomial: value % 2 for monomial, value in polynomial.items()})


def q_hypercube(polynomial: Polynomial) -> Polynomial:
    ordered = sorted(polynomial)
    answer: Polynomial = {}
    for monomial in ordered:
        high_bit = (polynomial[monomial] // 2) % 2
        doubled = tuple(2 * exponent for exponent in monomial)
        answer[doubled] = answer.get(doubled, 0) + high_bit
    for index, alpha in enumerate(ordered):
        for beta in ordered[index + 1 :]:
            value = (polynomial[alpha] % 2) * (polynomial[beta] % 2)
            monomial = tuple(a + b for a, b in zip(alpha, beta, strict=True))
            answer[monomial] = answer.get(monomial, 0) + value
    return mod_two(answer)


def truncate_series(
    base_index: int,
    degree: int,
    rules: tuple,
    target: int,
) -> list[dict[tuple[int, ...], int]]:
    colors = len(rules)
    coefficients: list[dict[tuple[int, ...], int]] = [
        {} for _ in range(target + 1)
    ]
    coefficients[0][(0,) * colors] = 1
    for color, rule in enumerate(rules):
        for part_size in range(1, target + 1):
            multiplier = rule(part_size)
            if multiplier == 0:
                continue
            exponent = base_index * multiplier * part_size**degree
            coefficients = EULER.multiply_factor(
                coefficients,
                part_size,
                exponent,
                color,
                colors,
                target,
            )
    return coefficients


def flatten_series(
    coefficients: list[dict[tuple[int, ...], int]],
) -> Polynomial:
    answer: Polynomial = {}
    for x_degree, polynomial in enumerate(coefficients):
        for color_degree, value in polynomial.items():
            answer[(x_degree, *color_degree)] = value
    return clean(answer)


def x_coefficient(polynomial: Polynomial, x_degree: int) -> Polynomial:
    return clean(
        {
            monomial[1:]: value
            for monomial, value in polynomial.items()
            if monomial[0] == x_degree
        }
    )


def truncate_x(polynomial: Polynomial, target: int) -> Polynomial:
    return clean(
        {
            monomial: value
            for monomial, value in polynomial.items()
            if monomial[0] <= target
        }
    )


def logarithmic_defect_series(
    base_index: int,
    degree: int,
    rules: tuple,
    target: int,
) -> Polynomial:
    colors = len(rules)
    answer: Polynomial = {}
    for color, rule in enumerate(rules):
        for part_size in range(1, target + 1):
            exponent = base_index * rule(part_size) * part_size**degree
            if exponent % 2 == 0:
                continue
            for multiple in range(1, target // part_size + 1):
                color_degree = [0] * colors
                color_degree[color] = multiple
                monomial = (part_size * multiple, *color_degree)
                answer[monomial] = answer.get(monomial, 0) + 1
    return mod_two(answer)


def check_universal_quadratic_identity() -> int:
    monomials = ((0, 0), (1, 0), (0, 1))
    polynomials: list[Polynomial] = []
    for values in itertools.product(range(-2, 3), repeat=len(monomials)):
        polynomials.append(clean(dict(zip(monomials, values, strict=True))))

    checks = 0
    for polynomial in polynomials:
        assert mod_two(q_exact(polynomial)) == q_hypercube(polynomial)
        checks += 1

    sample = polynomials[::17]
    for left in sample:
        for right in sample:
            lhs = mod_two(q_exact(add(left, right)))
            rhs = mod_two(
                add(add(q_exact(left), q_exact(right)), multiply(left, right))
            )
            assert lhs == rhs
            checks += 1
    print(f"universal quadratic checks: {checks}")
    return checks


def check_euler_defect_identity() -> int:
    cases = (
        (1, (EULER.constant(-1),)),
        (1, (EULER.constant(1),)),
        (2, (EULER.constant(-1),)),
        (2, (EULER.patterned,)),
        (3, (EULER.odd_only(2),)),
        (1, (EULER.constant(1), EULER.odd_only(-2))),
    )
    checks = 0
    for degree, rules in cases:
        for n in (1, 2, 3):
            series = flatten_series(truncate_series(n, degree, rules, 2 * n))
            defect_from_q = x_coefficient(q_exact(series), 2 * n)
            difference = EULER.frobenius_difference(2, 1, n, degree, rules)
            assert all(value % 2 == 0 for value in difference.values())
            normalized = clean(
                {monomial: value // 2 for monomial, value in difference.items()}
            )
            assert defect_from_q == normalized
            assert mod_two(defect_from_q) == mod_two(normalized)
            logarithmic = logarithmic_defect_series(
                n, degree, rules, 2 * n
            )
            closed_form = mod_two(
                truncate_x(
                    multiply(mod_two(phi(series)), logarithmic),
                    2 * n,
                )
            )
            assert truncate_x(mod_two(q_exact(series)), 2 * n) == closed_form
            if n % 2 == 0:
                assert not closed_form
            checks += len(normalized) + len(closed_form)
    print(f"exact Euler defect coefficients: {checks}")
    return checks


def check_binary_tower() -> int:
    cases = (
        (1, (EULER.constant(-2),)),
        (1, (EULER.constant(1),)),
        (2, (EULER.constant(-1),)),
        (2, (EULER.patterned,)),
        (3, (EULER.odd_only(2),)),
        (1, (EULER.constant(1), EULER.odd_only(-2))),
        (2, (EULER.constant(-1), EULER.odd_only(3))),
    )
    checks = 0
    sharp: list[tuple[int, int, int, int]] = []
    for degree, rules in cases:
        for level, n in ((1, 1), (1, 2), (2, 1), (3, 1)):
            difference = EULER.frobenius_difference(
                2, level, n, degree, rules
            )
            actual = EULER.polynomial_valuation(difference, 2)
            target = 2 * level - 1
            assert actual >= target
            if actual == target:
                sharp.append((degree, len(rules), level, n))
            checks += len(difference)

    boundary = EULER.frobenius_difference(
        2, 1, 1, 1, (EULER.constant(-1),)
    )
    assert boundary[(2,)] == 2
    assert (1, 1, 1, 1) in sharp
    print(f"binary tower coefficients: {checks}")
    print(f"sharp parameter sets: {sharp}")
    return checks


def main() -> None:
    universal = check_universal_quadratic_identity()
    euler = check_euler_defect_identity()
    tower = check_binary_tower()
    print(f"total exact checks: {universal + euler + tower}")


if __name__ == "__main__":
    main()
