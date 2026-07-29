"""Exact and numerical checks for HyperdeterminantEntropyProfile.md."""

from fractions import Fraction
from math import comb, isclose, log, sqrt


def zero_fiber(q: int) -> int:
    return q**7 + q**4 - q**3


def square_fiber(q: int) -> int:
    return q**3 * (q - 1) * (q + 1) ** 3


def nonsquare_fiber(q: int) -> int:
    return q**3 * (q - 1) ** 3 * (q + 1)


def point_probabilities(q: int) -> tuple[Fraction, Fraction, Fraction]:
    denominator = q**8
    return (
        Fraction(zero_fiber(q), denominator),
        Fraction(square_fiber(q), denominator),
        Fraction(nonsquare_fiber(q), denominator),
    )


def collision_direct(q: int) -> Fraction:
    p_zero, p_plus, p_minus = point_probabilities(q)
    half = (q - 1) // 2
    return p_zero**2 + half * (p_plus**2 + p_minus**2)


def collision_closed(q: int) -> Fraction:
    correction = Fraction(
        (q - 1) * (1 + 4 * q * (q * q - 1) ** 2),
        q**8,
    )
    return Fraction(1, q) * (1 + correction)


def chi_squared_closed(q: int) -> Fraction:
    return Fraction(
        (q - 1) * (1 + 4 * q * (q * q - 1) ** 2),
        q**8,
    )


def total_variation_direct(q: int) -> Fraction:
    uniform = Fraction(1, q)
    half = (q - 1) // 2
    p_zero, p_plus, p_minus = point_probabilities(q)
    l1 = (
        abs(p_zero - uniform)
        + half * abs(p_plus - uniform)
        + half * abs(p_minus - uniform)
    )
    return l1 / 2


def total_variation_closed(q: int) -> Fraction:
    return Fraction((q - 1) * (2 * q**3 - 2 * q + 1), 2 * q**5)


def shannon(probabilities: list[float]) -> float:
    return -sum(value * log(value) for value in probabilities if value)


def renyi(probabilities: list[float], alpha: float) -> float:
    if alpha == 1.0:
        return shannon(probabilities)
    return log(sum(value**alpha for value in probabilities)) / (1 - alpha)


def expanded_probabilities(q: int) -> list[float]:
    p_zero, p_plus, p_minus = point_probabilities(q)
    half = (q - 1) // 2
    return [float(p_zero)] + [float(p_plus)] * half + [float(p_minus)] * half


def class_probabilities(q: int) -> tuple[list[float], list[float]]:
    p_zero, p_plus, p_minus = point_probabilities(q)
    half = (q - 1) // 2
    law = [float(p_zero), float(half * p_plus), float(half * p_minus)]
    uniform = [1 / q, half / q, half / q]
    return law, uniform


def renyi_divergence(
    probabilities: list[float],
    reference: list[float],
    alpha: float,
) -> float:
    if alpha == 1.0:
        return sum(
            value * log(value / base)
            for value, base in zip(probabilities, reference)
            if value
        )
    total = sum(
        value**alpha * base ** (1 - alpha)
        for value, base in zip(probabilities, reference)
    )
    return log(total) / (alpha - 1)


def epsilon_minus_one(q: int) -> int:
    return 1 if q % 4 == 1 else -1


def convolution_energy(q: int, m: int) -> int:
    c_q = 2 * (q * q - 1)
    if epsilon_minus_one(q) == -1:
        return (1 + c_q * c_q * q) ** m
    return sum(
        comb(2 * m, 2 * j) * c_q ** (2 * j) * q**j
        for j in range(m + 1)
    )


def convolution_collision_closed(q: int, m: int) -> Fraction:
    correction = Fraction(
        (q - 1) * convolution_energy(q, m),
        q ** (8 * m),
    )
    return Fraction(1, q) * (1 + correction)


def cyclic_convolution(left: list[int], right: list[int]) -> list[int]:
    q = len(left)
    answer = [0] * q
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            answer[(i + j) % q] += first * second
    return answer


def is_square(value: int, q: int) -> bool:
    return pow(value, (q - 1) // 2, q) == 1


def value_counts_prime(q: int) -> list[int]:
    return [zero_fiber(q)] + [
        square_fiber(q) if is_square(value, q) else nonsquare_fiber(q)
        for value in range(1, q)
    ]


def convolution_collision_direct(q: int, m: int) -> Fraction:
    base = value_counts_prime(q)
    counts = [1] + [0] * (q - 1)
    for _ in range(m):
        counts = cyclic_convolution(counts, base)
    return Fraction(sum(value * value for value in counts), q ** (16 * m))


def main() -> None:
    odd_prime_powers = (3, 5, 7, 9, 11, 13, 17, 19, 25, 27, 49, 81, 121, 125)
    exact_checks = 0
    numerical_checks = 0

    for q in odd_prime_powers:
        p_zero, p_plus, p_minus = point_probabilities(q)
        half = (q - 1) // 2

        assert p_zero + half * (p_plus + p_minus) == 1
        exact_checks += 1
        assert p_plus > p_zero > p_minus
        exact_checks += 1
        assert collision_direct(q) == collision_closed(q)
        exact_checks += 1
        assert q * collision_direct(q) - 1 == chi_squared_closed(q)
        exact_checks += 1
        assert total_variation_direct(q) == total_variation_closed(q)
        exact_checks += 1

        expanded = expanded_probabilities(q)
        classes, uniform_classes = class_probabilities(q)
        uniform = [1 / q] * q

        chain_right = shannon(classes) + (1 - float(p_zero)) * log(half)
        assert isclose(shannon(expanded), chain_right, rel_tol=2e-13, abs_tol=2e-13)
        numerical_checks += 1

        orders = (0.5, 1.0, 2.0, 3.0, 10.0)
        entropies = [renyi(expanded, alpha) for alpha in orders]
        assert all(
            entropies[index] >= entropies[index + 1] - 2e-13
            for index in range(len(entropies) - 1)
        )
        numerical_checks += 1

        for alpha in orders:
            full = renyi_divergence(expanded, uniform, alpha)
            collapsed = renyi_divergence(classes, uniform_classes, alpha)
            assert isclose(full, collapsed, rel_tol=3e-12, abs_tol=3e-12)
            numerical_checks += 1

        min_entropy = -log(float(p_plus))
        assert isclose(
            min_entropy,
            log(q**5 / ((q - 1) * (q + 1) ** 3)),
            rel_tol=2e-13,
            abs_tol=2e-13,
        )
        numerical_checks += 1

        relative_entropy = renyi_divergence(expanded, uniform, 1.0)
        pinsker_bound = sqrt(relative_entropy / 2)
        assert float(total_variation_direct(q)) <= pinsker_bound + 2e-13
        numerical_checks += 1

    convolution_checks = 0
    for q in (3, 5, 7):
        for m in range(1, 5):
            assert (
                convolution_collision_direct(q, m)
                == convolution_collision_closed(q, m)
            )
            convolution_checks += 1

    asymptotic_q = 1009
    asymptotic_probabilities = expanded_probabilities(asymptotic_q)
    asymptotic_uniform = [1 / asymptotic_q] * asymptotic_q
    relative_entropy = renyi_divergence(
        asymptotic_probabilities,
        asymptotic_uniform,
        1.0,
    )
    assert abs(asymptotic_q**2 * relative_entropy - 2) < 0.01
    numerical_checks += 1
    assert abs(asymptotic_q * float(total_variation_direct(asymptotic_q)) - 1) < 0.01
    numerical_checks += 1

    print(
        "PASS:",
        exact_checks,
        "exact entropy checks;",
        numerical_checks,
        "Rényi/KL checks;",
        convolution_checks,
        "exact convolution checks.",
    )


if __name__ == "__main__":
    main()
