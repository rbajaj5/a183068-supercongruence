"""Exact checks for HyperdeterminantFourierSupercongruence.md."""

from itertools import product


def hyperdeterminant(values: tuple[int, ...], p: int) -> int:
    a, b, c, d, e, f, g, h = values
    return (
        a * a * h * h
        + b * b * g * g
        + c * c * f * f
        + e * e * d * d
        - 2
        * (
            a * b * g * h
            + a * c * f * h
            + a * e * d * h
            + b * c * f * g
            + b * e * d * g
            + c * e * d * f
        )
        + 4 * (a * d * f * g + b * c * e * h)
    ) % p


def is_square(value: int, p: int) -> bool:
    assert value % p
    return pow(value, (p - 1) // 2, p) == 1


def zero_fiber(q: int) -> int:
    return q**7 + q**4 - q**3


def square_fiber(q: int) -> int:
    return q**3 * (q - 1) * (q + 1) ** 3


def nonsquare_fiber(q: int) -> int:
    return q**3 * (q - 1) ** 3 * (q + 1)


def epsilon_minus_one(q: int) -> int:
    return 1 if q % 4 == 1 else -1


def paired_product(q: int) -> int:
    return q**8 * (1 - 4 * epsilon_minus_one(q) * q * (q * q - 1) ** 2)


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def exhaustive_prime_field(p: int) -> None:
    counts = [0] * p
    for values in product(range(p), repeat=8):
        counts[hyperdeterminant(values, p)] += 1

    expected = [zero_fiber(p)]
    expected.extend(
        square_fiber(p) if is_square(value, p) else nonsquare_fiber(p)
        for value in range(1, p)
    )
    assert counts == expected
    assert sum(counts) == p**8


def main() -> None:
    exhaustive_primes = (3, 5, 7)
    for p in exhaustive_primes:
        exhaustive_prime_field(p)

    fiber_cases = 0
    valuation_cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for r in range(1, 7):
            q = p**r
            nonzero_total = (q - 1) // 2 * (
                square_fiber(q) + nonsquare_fiber(q)
            )
            assert zero_fiber(q) + nonzero_total == q**8
            fiber_cases += 1
            if r >= 2:
                difference = paired_product(p**r) - paired_product(p ** (r - 1))
                assert valuation(difference, p) == 8 * (r - 1)
                valuation_cases += 1

    print(
        "PASS:",
        len(exhaustive_primes),
        "exhaustive fields;",
        fiber_cases,
        "symbolic fiber cases;",
        valuation_cases,
        "exact valuation cases.",
    )


if __name__ == "__main__":
    main()
