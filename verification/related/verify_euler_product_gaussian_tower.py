"""Exact checks for the colored Euler-product Frobenius theorem.

The proof is in related-results/EulerProductGaussianTower.md.  These checks
are finite certificates and regression tests, not substitutes for the proof.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from math import comb


Monomial = tuple[int, ...]
Polynomial = dict[Monomial, int]
ExponentRule = Callable[[int], int]
GaussianInteger = tuple[int, int]


def multiply_factor(
    coefficients: list[Polynomial],
    part_size: int,
    exponent: int,
    color: int,
    colors: int,
    target: int,
) -> list[Polynomial]:
    factor: list[int] = []
    for occupation in range(target // part_size + 1):
        if exponent >= 0:
            if occupation > exponent:
                break
            value = (-1) ** occupation * comb(exponent, occupation)
        else:
            value = comb(-exponent + occupation - 1, occupation)
        factor.append(value)

    result: list[Polynomial] = [{} for _ in range(target + 1)]
    for degree, polynomial in enumerate(coefficients):
        for monomial, old_value in polynomial.items():
            for occupation, factor_value in enumerate(factor):
                new_degree = degree + part_size * occupation
                if new_degree > target:
                    break
                new_monomial = list(monomial)
                new_monomial[color] += occupation
                key = tuple(new_monomial)
                result[new_degree][key] = (
                    result[new_degree].get(key, 0) + old_value * factor_value
                )
    return result


def euler_product_polynomial(
    target: int,
    degree: int,
    rules: Sequence[ExponentRule],
) -> Polynomial:
    """Return [x^target] prod_(color,m) (1-Z_color*x^m)^(N*h*m^d)."""

    colors = len(rules)
    coefficients: list[Polynomial] = [{} for _ in range(target + 1)]
    coefficients[0][(0,) * colors] = 1
    for color, rule in enumerate(rules):
        for part_size in range(1, target + 1):
            multiplier = rule(part_size)
            if multiplier == 0:
                continue
            exponent = target * multiplier * part_size**degree
            coefficients = multiply_factor(
                coefficients,
                part_size,
                exponent,
                color,
                colors,
                target,
            )
    return coefficients[target]


def frobenius_difference(
    prime: int,
    level: int,
    n: int,
    degree: int,
    rules: Sequence[ExponentRule],
) -> Polynomial:
    upper = euler_product_polynomial(n * prime**level, degree, rules)
    lower = euler_product_polynomial(n * prime ** (level - 1), degree, rules)
    answer = dict(upper)
    for monomial, value in lower.items():
        lifted = tuple(prime * exponent for exponent in monomial)
        answer[lifted] = answer.get(lifted, 0) - value
    return {monomial: value for monomial, value in answer.items() if value}


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def polynomial_valuation(polynomial: Polynomial, prime: int) -> int:
    return min((valuation(value, prime) for value in polynomial.values()), default=10**9)


def evaluate_one(polynomial: Polynomial) -> int:
    return sum(polynomial.values())


def evaluate_i(polynomial: Polynomial) -> GaussianInteger:
    if any(len(monomial) != 1 for monomial in polynomial):
        raise ValueError("Gaussian evaluation expects one color")
    real = 0
    imag = 0
    for (exponent,), value in polynomial.items():
        residue = exponent % 4
        if residue == 0:
            real += value
        elif residue == 1:
            imag += value
        elif residue == 2:
            real -= value
        else:
            imag -= value
    return real, imag


def gaussian_difference(
    prime: int,
    level: int,
    n: int,
    degree: int,
    rule: ExponentRule,
) -> GaussianInteger:
    upper = euler_product_polynomial(n * prime**level, degree, (rule,))
    lower = euler_product_polynomial(n * prime ** (level - 1), degree, (rule,))
    upper_value = evaluate_i(upper)

    real = 0
    imag = 0
    for (exponent,), value in lower.items():
        residue = (prime * exponent) % 4
        if residue == 0:
            real += value
        elif residue == 1:
            imag += value
        elif residue == 2:
            real -= value
        else:
            imag -= value
    return upper_value[0] - real, upper_value[1] - imag


def constant(value: int) -> ExponentRule:
    return lambda _part_size: value


def odd_only(value: int) -> ExponentRule:
    return lambda part_size: value if part_size % 2 else 0


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def ghost_polynomial(index: int) -> dict[int, int]:
    return {index // divisor: divisor**3 for divisor in divisors(index)}


def patterned(part_size: int) -> int:
    return (-2, 0, 1, 3)[part_size % 4]


def scalar_euler_product_value(
    target: int, degree: int, rule: ExponentRule
) -> int:
    """Return the uncolored specialization of the universal product."""
    coefficients = [0] * (target + 1)
    coefficients[0] = 1
    for part_size in range(1, target + 1):
        exponent = target * rule(part_size) * part_size**degree
        if exponent == 0:
            continue
        factor: list[int] = []
        for occupation in range(target // part_size + 1):
            if exponent >= 0:
                if occupation > exponent:
                    break
                value = (-1) ** occupation * comb(exponent, occupation)
            else:
                value = comb(-exponent + occupation - 1, occupation)
            factor.append(value)
        updated = [0] * (target + 1)
        for old_degree, old_value in enumerate(coefficients):
            if old_value == 0:
                continue
            for occupation, factor_value in enumerate(factor):
                new_degree = old_degree + part_size * occupation
                if new_degree > target:
                    break
                updated[new_degree] += old_value * factor_value
        coefficients = updated
    return coefficients[target]


def check_published_values() -> None:
    expected = (1, 1, 11, 73, 539, 3976, 30107, 229811, 1771803, 13749742)
    actual = [1]
    for target in range(1, len(expected)):
        polynomial = euler_product_polynomial(target, 2, (constant(-1),))
        actual.append(evaluate_one(polynomial))
    assert tuple(actual) == expected
    print(f"A380290 initial values: {len(expected)}")


def check_a281267_specialization() -> int:
    expected = (
        1,
        -1,
        -3,
        8,
        13,
        -51,
        -120,
        538,
        781,
        -5419,
        -3053,
        47673,
        5080,
        -427740,
        136462,
    )
    actual = [1]
    actual.extend(
        scalar_euler_product_value(target, 1, constant(1))
        for target in range(1, len(expected))
    )
    assert tuple(actual) == expected

    cache: dict[int, int] = {index: value for index, value in enumerate(actual)}

    def value(index: int) -> int:
        if index not in cache:
            cache[index] = scalar_euler_product_value(index, 1, constant(1))
        return cache[index]

    tower_checks = 0
    for prime in (3, 5, 7, 11):
        for level in (1, 2):
            modulus = prime ** (2 * level)
            for n in range(1, 6):
                if n * prime**level > 150:
                    continue
                difference = value(n * prime**level) - value(
                    n * prime ** (level - 1)
                )
                assert difference % modulus == 0, (prime, level, n)
                tower_checks += 1
    assert tower_checks == 34
    checks = len(expected) + tower_checks
    print(f"A281267 specialization checks: {checks}")
    return checks


def check_universal_theorem() -> int:
    checks = 0
    one_color_cases = (
        (1, constant(-2)),
        (1, constant(1)),
        (2, constant(-1)),
        (2, patterned),
        (3, odd_only(2)),
    )
    for degree, rule in one_color_cases:
        for prime in (3, 5, 7):
            for level, n in ((1, 1), (1, 2)):
                difference = frobenius_difference(
                    prime, level, n, degree, (rule,)
                )
                assert polynomial_valuation(difference, prime) >= 2 * level
                checks += len(difference)
        for prime in (3, 5):
            difference = frobenius_difference(prime, 2, 1, degree, (rule,))
            assert polynomial_valuation(difference, prime) >= 4
            checks += len(difference)

    two_color_cases = (
        (1, (constant(1), odd_only(-2))),
        (2, (constant(-1), odd_only(3))),
        (3, (patterned, odd_only(1))),
    )
    for degree, rules in two_color_cases:
        for prime in (3, 5):
            for level, n in ((1, 1), (1, 2), (2, 1)):
                difference = frobenius_difference(
                    prime, level, n, degree, rules
                )
                assert polynomial_valuation(difference, prime) >= 2 * level
                checks += len(difference)

    print(f"coefficientwise checks: {checks}")
    return checks


def check_gaussian_specialization() -> int:
    checks = 0
    equality_witnesses: list[tuple[int, int, int, GaussianInteger]] = []
    for prime in (3, 5, 7, 11):
        for level in (1, 2):
            if level == 2 and prime > 7:
                continue
            difference = gaussian_difference(
                prime, level, 1, 2, constant(-1)
            )
            actual = min(
                valuation(difference[0], prime),
                valuation(difference[1], prime),
            )
            assert actual >= 2 * level
            if actual == 2 * level:
                equality_witnesses.append((prime, level, actual, difference))
            checks += 1

    assert any(prime == 5 and level == 1 for prime, level, _, _ in equality_witnesses)
    assert any(prime == 3 and level == 2 for prime, level, _, _ in equality_witnesses)
    print(f"Gaussian checks: {checks}")
    print(f"Gaussian equality witnesses: {equality_witnesses[:5]}")
    return checks


def check_logarithmic_frobenius() -> int:
    checks = 0
    for prime in (3, 5, 7):
        for index in range(1, 21):
            valuation_index = 0
            unit = index
            while unit % prime == 0:
                unit //= prime
                valuation_index += 1

            left = ghost_polynomial(prime * index)
            for exponent, value in ghost_polynomial(index).items():
                lifted = prime * exponent
                left[lifted] = left.get(lifted, 0) - value
            expected = {
                exponent: prime ** (3 * (valuation_index + 1)) * value
                for exponent, value in ghost_polynomial(unit).items()
            }
            assert {key: value for key, value in left.items() if value} == expected
            checks += 1
    print(f"logarithmic Frobenius checks: {checks}")
    return checks


def check_boundaries() -> None:
    degree_zero = frobenius_difference(3, 1, 1, 0, (constant(-2),))
    assert degree_zero[(1,)] == 6
    assert valuation(degree_zero[(1,)], 3) == 1

    binary = frobenius_difference(2, 1, 1, 1, (constant(-1),))
    assert binary[(2,)] == 2
    assert valuation(binary[(2,)], 2) == 1
    print("boundary certificates: 2")


def main() -> None:
    check_published_values()
    a281267_checks = check_a281267_specialization()
    coefficient_checks = check_universal_theorem()
    logarithmic_checks = check_logarithmic_frobenius()
    gaussian_checks = check_gaussian_specialization()
    check_boundaries()
    print(
        "total exact checks: "
        f"{coefficient_checks + logarithmic_checks + gaussian_checks + 12 + a281267_checks}"
    )


if __name__ == "__main__":
    main()
