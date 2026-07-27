"""Checks for the USAMO-to-Hamming supercongruence note."""

from fractions import Fraction
from math import comb, factorial


def chord_length(step: int, n: int) -> int:
    return min(step, n - step)


def triangulation_count(n: int) -> int:
    counts = [0] * n
    counts[1] = 1
    for span in range(2, n):
        total = 0
        for left in range(1, span):
            lengths = (
                chord_length(left, n),
                chord_length(span - left, n),
                chord_length(span, n),
            )
            if (
                lengths[0] == lengths[1]
                or lengths[0] == lengths[2]
                or lengths[1] == lengths[2]
            ):
                total += counts[left] * counts[span - left]
        counts[span] = total
    return counts[n - 1]


def predicted_triangulation_count(n: int) -> int:
    odd = n
    power = 1
    while odd % 2 == 0:
        odd //= 2
        power *= 2
    if odd == 1:
        return n // 2
    if odd == 3:
        return power
    if odd >= 5 and (odd - 1) & (odd - 2) == 0:
        return n
    return 0


def walsh_eigenvalue(dimension: int, weight: int) -> int:
    difference = dimension - 2 * weight
    return 1 + difference + (
        difference * difference - dimension
    ) // 2


def zero_sum_count(length: int, dimension: int) -> int:
    numerator = sum(
        comb(dimension, weight)
        * walsh_eigenvalue(dimension, weight) ** length
        for weight in range(dimension + 1)
    )
    assert numerator % 2**dimension == 0
    return numerator // 2**dimension


def cyclic_xor_convolution(
    left: list[int], right: list[int]
) -> list[int]:
    size = len(left)
    result = [0] * size
    for first, first_count in enumerate(left):
        for second, second_count in enumerate(right):
            result[first ^ second] += first_count * second_count
    return result


def binomial_coefficients(length: int) -> list[int]:
    differences = [
        zero_sum_count(length, dimension)
        for dimension in range(length + 1)
    ]
    answer = []
    while differences:
        answer.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]
    return answer


def evaluate_binomial_polynomial(
    coefficients: list[int], value: int
) -> int:
    return sum(
        coefficient * comb(value, degree)
        for degree, coefficient in enumerate(coefficients)
    )


def derivative_at_zero(coefficients: list[int]) -> Fraction:
    return sum(
        Fraction(
            (-1) ** (degree - 1) * coefficients[degree],
            degree,
        )
        for degree in range(1, len(coefficients))
    )


def valuation(number: int, prime: int) -> int:
    assert number
    answer = 0
    while number % prime == 0:
        answer += 1
        number //= prime
    return answer


def primes_through(limit: int) -> list[int]:
    answer = []
    for candidate in range(2, limit + 1):
        if all(
            candidate % divisor
            for divisor in range(2, int(candidate**0.5) + 1)
        ):
            answer.append(candidate)
    return answer


def verify_triangulations() -> None:
    for n in range(3, 257):
        assert triangulation_count(n) == (
            predicted_triangulation_count(n)
        )
    print("exact triangulation counts: 254")


def verify_walsh_spectrum() -> None:
    cases = 0
    for dimension in range(1, 11):
        ball = [
            value
            for value in range(1 << dimension)
            if value.bit_count() <= 2
        ]
        for frequency in range(1 << dimension):
            direct = sum(
                -1
                if (value & frequency).bit_count() % 2
                else 1
                for value in ball
            )
            assert direct == walsh_eigenvalue(
                dimension, frequency.bit_count()
            )
            cases += 1
    print("Walsh coefficients:", cases)


def verify_convolutions() -> None:
    cases = 0
    for dimension in range(0, 9):
        size = 1 << dimension
        ball = [
            1 if value.bit_count() <= 2 else 0
            for value in range(size)
        ]
        current = [1] + [0] * (size - 1)
        for length in range(1, 9):
            current = cyclic_xor_convolution(current, ball)
            assert current[0] == zero_sum_count(length, dimension)
            cases += 1
    print("direct XOR convolutions:", cases)


def verify_polynomials_and_towers() -> None:
    polynomial_cases = 0
    congruence_cases = 0
    sharp_cases = 0
    primes = primes_through(500)
    for length in range(1, 11):
        coefficients = binomial_coefficients(length)
        assert len(coefficients) == length + 1
        for dimension in range(0, 2 * length + 6):
            assert evaluate_binomial_polynomial(
                coefficients, dimension
            ) == zero_sum_count(length, dimension)
            polynomial_cases += 1
        if length == 1:
            continue
        derivative = derivative_at_zero(coefficients)
        obstruction = derivative * factorial(length)
        assert obstruction.denominator == 1
        for prime in primes:
            if prime <= length:
                continue
            for r in range(2, 5):
                difference = evaluate_binomial_polynomial(
                    coefficients, prime**r
                ) - evaluate_binomial_polynomial(
                    coefficients, prime ** (r - 1)
                )
                actual = valuation(difference, prime)
                assert actual >= r - 1
                congruence_cases += 1
                if int(obstruction) % prime:
                    assert actual == r - 1
                    sharp_cases += 1
    print("polynomial identities:", polynomial_cases)
    print("tower congruences:", congruence_cases)
    print("sharp generic towers:", sharp_cases)


def verify_first_exception() -> None:
    coefficients = binomial_coefficients(6)
    obstruction = derivative_at_zero(coefficients) * factorial(6)
    assert obstruction == 474120
    assert int(obstruction) % 439 == 0
    residues = []
    for r in range(2, 7):
        difference = evaluate_binomial_polynomial(
            coefficients, 439**r
        ) - evaluate_binomial_polynomial(
            coefficients, 439 ** (r - 1)
        )
        actual = valuation(difference, 439)
        assert actual == r
        residues.append(actual)
    print("p=439 exceptional valuations:", residues)


def main() -> None:
    verify_triangulations()
    verify_walsh_spectrum()
    verify_convolutions()
    verify_polynomials_and_towers()
    verify_first_exception()
    print("PASS")


if __name__ == "__main__":
    main()
