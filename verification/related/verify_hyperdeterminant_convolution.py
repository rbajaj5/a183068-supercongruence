"""Exact checks for the hyperdeterminant Fourier convolution tower."""

from fractions import Fraction

from verify_hyperdeterminant_fourier import (
    epsilon_minus_one,
    nonsquare_fiber,
    square_fiber,
    valuation,
    zero_fiber,
)


def even_binomial_polynomial(m: int, value: int) -> int:
    coefficients = [1]
    for _ in range(m):
        coefficients = [
            (coefficients[index] if index < len(coefficients) else 0)
            + (
                coefficients[index - 1]
                if index > 0
                else 0
            )
            for index in range(len(coefficients) + 1)
        ]
    return sum(
        coefficients[2 * j] * value**j
        for j in range((m // 2) + 1)
    )


def odd_binomial_polynomial(m: int, value: int) -> int:
    coefficients = [1]
    for _ in range(m):
        coefficients = [
            (coefficients[index] if index < len(coefficients) else 0)
            + (
                coefficients[index - 1]
                if index > 0
                else 0
            )
            for index in range(len(coefficients) + 1)
        ]
    return sum(
        coefficients[2 * j + 1] * value**j
        for j in range(((m - 1) // 2) + 1)
    )


def convolution_fiber(q: int, m: int, character_class: int) -> int:
    assert character_class in (-1, 0, 1)
    epsilon = epsilon_minus_one(q)
    x_value = 4 * epsilon * q * (q * q - 1) ** 2
    even = even_binomial_polynomial(m, x_value)
    odd = odd_binomial_polynomial(m, x_value)
    if character_class == 0:
        return q ** (8 * m - 1) + (
            (q - 1) * q ** (4 * m - 1) * even
        )
    return q ** (8 * m - 1) + q ** (4 * m - 1) * (
        -even
        + 2
        * character_class
        * q
        * (q * q - 1)
        * odd
    )


def cyclic_convolution(left: list[int], right: list[int]) -> list[int]:
    q = len(left)
    assert len(right) == q
    result = [0] * q
    for first, first_count in enumerate(left):
        for second, second_count in enumerate(right):
            result[(first + second) % q] += first_count * second_count
    return result


def is_square(value: int, p: int) -> bool:
    assert value % p
    return pow(value, (p - 1) // 2, p) == 1


def verify_prime_field_convolutions() -> None:
    cases = 0
    for q in (3, 5, 7):
        one_step = [zero_fiber(q)]
        one_step.extend(
            square_fiber(q) if is_square(value, q)
            else nonsquare_fiber(q)
            for value in range(1, q)
        )
        current = [1] + [0] * (q - 1)
        for m in range(1, 9):
            current = cyclic_convolution(current, one_step)
            expected = [convolution_fiber(q, m, 0)]
            expected.extend(
                convolution_fiber(
                    q, m, 1 if is_square(value, q) else -1
                )
                for value in range(1, q)
            )
            assert current == expected
            assert sum(current) == q ** (8 * m)
            cases += q
    print("exact prime-field convolution fibers:", cases)


def verify_supercongruence() -> None:
    cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for r in range(2, 7):
            for m in range(1, 9):
                for character_class in (-1, 0, 1):
                    difference = (
                        convolution_fiber(p**r, m, character_class)
                        - convolution_fiber(
                            p ** (r - 1), m, character_class
                        )
                    )
                    assert valuation(difference, p) == (
                        (4 * m - 1) * (r - 1)
                    )
                    cases += 1
    print("sharp adjacent-extension valuations:", cases)


def total_variation(
    counts: list[int], total: int
) -> Fraction:
    q = len(counts)
    return Fraction(
        sum(abs(q * count - total) for count in counts),
        2 * q * total,
    )


def verify_mixing_bound() -> None:
    cases = 0
    for q in (3, 5, 7, 11):
        one_step = [zero_fiber(q)]
        one_step.extend(
            square_fiber(q) if is_square(value, q)
            else nonsquare_fiber(q)
            for value in range(1, q)
        )
        current = [1] + [0] * (q - 1)
        c_value = 2 * (q * q - 1)
        # Uniform rational upper bound for rho_q^2:
        # |1 + cG|^2 <= 2(1 + c^2 q).
        rho_squared_bound = Fraction(
            2 * (1 + c_value * c_value * q),
            q**8,
        )
        for m in range(1, 9):
            current = cyclic_convolution(current, one_step)
            tv = total_variation(current, q ** (8 * m))
            # Square (20) and use the rational bound above.
            assert 4 * tv * tv <= (
                (q - 1) * rho_squared_bound**m
            )
            cases += 1
    print("total-variation bounds:", cases)


def main() -> None:
    verify_prime_field_convolutions()
    verify_supercongruence()
    verify_mixing_bound()
    print("PASS")


if __name__ == "__main__":
    main()
