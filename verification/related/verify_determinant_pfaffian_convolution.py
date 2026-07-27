"""Exact checks for determinant and Pfaffian convolution towers."""

from fractions import Fraction

from verify_finite_field_determinant_bias import (
    character_sum_formula as determinant_sum,
    exponent as determinant_exponent,
)
from verify_finite_field_pfaffian_bias import (
    character_sum_formula as pfaffian_sum,
    exponent as pfaffian_exponent,
)


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def one_sample_fibers(
    q: int, dimension: int, character_sum: int
) -> list[int]:
    total = q**dimension
    zero = (total + (q - 1) * character_sum) // q
    nonzero = (total - character_sum) // q
    return [zero] + [nonzero] * (q - 1)


def convolution_fiber(
    q: int,
    dimension: int,
    character_sum: int,
    length: int,
    is_zero: bool,
) -> int:
    total = q ** (dimension * length)
    power = character_sum**length
    if is_zero:
        return (total + (q - 1) * power) // q
    return (total - power) // q


def cyclic_convolution(left: list[int], right: list[int]) -> list[int]:
    q = len(left)
    assert len(right) == q
    result = [0] * q
    for first, first_count in enumerate(left):
        for second, second_count in enumerate(right):
            result[(first + second) % q] += first_count * second_count
    return result


def total_variation(counts: list[int], total: int) -> Fraction:
    q = len(counts)
    return Fraction(
        sum(abs(q * count - total) for count in counts),
        2 * q * total,
    )


def verify_convolutions_and_mixing() -> None:
    cases = 0
    for family in ("determinant", "pfaffian"):
        for size in range(2, 6):
            if family == "determinant":
                dimension = size * size
                sum_function = determinant_sum
            else:
                dimension = size * (2 * size - 1)
                sum_function = pfaffian_sum
            for q in (2, 3, 5, 7):
                character_sum = sum_function(size, q)
                one_step = one_sample_fibers(
                    q, dimension, character_sum
                )
                current = [1] + [0] * (q - 1)
                for length in range(1, 9):
                    current = cyclic_convolution(current, one_step)
                    expected_zero = convolution_fiber(
                        q,
                        dimension,
                        character_sum,
                        length,
                        True,
                    )
                    expected_nonzero = convolution_fiber(
                        q,
                        dimension,
                        character_sum,
                        length,
                        False,
                    )
                    assert current == (
                        [expected_zero]
                        + [expected_nonzero] * (q - 1)
                    )
                    total = q ** (dimension * length)
                    assert sum(current) == total
                    beta = Fraction(character_sum, q**dimension)
                    assert total_variation(current, total) == (
                        Fraction(q - 1, q) * abs(beta) ** length
                    )
                    cases += 1
    print("exact convolution and mixing cases:", cases)


def verify_supercongruences() -> None:
    determinant_cases = 0
    pfaffian_cases = 0
    for p in (2, 3, 5, 7, 11):
        for r in range(2, 6):
            for length in range(1, 7):
                for n in range(2, 9):
                    dimension = n * n
                    expected = (
                        length * determinant_exponent(n) - 1
                    ) * (r - 1)
                    for is_zero in (False, True):
                        upper = convolution_fiber(
                            p**r,
                            dimension,
                            determinant_sum(n, p**r),
                            length,
                            is_zero,
                        )
                        lower = convolution_fiber(
                            p ** (r - 1),
                            dimension,
                            determinant_sum(n, p ** (r - 1)),
                            length,
                            is_zero,
                        )
                        assert valuation(upper - lower, p) == expected
                        determinant_cases += 1
                for m in range(2, 8):
                    dimension = m * (2 * m - 1)
                    expected = (
                        length * pfaffian_exponent(m) - 1
                    ) * (r - 1)
                    for is_zero in (False, True):
                        upper = convolution_fiber(
                            p**r,
                            dimension,
                            pfaffian_sum(m, p**r),
                            length,
                            is_zero,
                        )
                        lower = convolution_fiber(
                            p ** (r - 1),
                            dimension,
                            pfaffian_sum(m, p ** (r - 1)),
                            length,
                            is_zero,
                        )
                        assert valuation(upper - lower, p) == expected
                        pfaffian_cases += 1
    print("determinant sharp valuations:", determinant_cases)
    print("Pfaffian sharp valuations:", pfaffian_cases)


def main() -> None:
    verify_convolutions_and_mixing()
    verify_supercongruences()
    print("PASS")


if __name__ == "__main__":
    main()
