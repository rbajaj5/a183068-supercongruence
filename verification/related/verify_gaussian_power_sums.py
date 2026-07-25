"""Exact checks for the Gaussian power-sum conjectures."""

from __future__ import annotations

import argparse


Gaussian = tuple[int, int]


def gaussian_multiply(left: Gaussian, right: Gaussian, modulus: int) -> Gaussian:
    a, b = left
    c, d = right
    return (a * c - b * d) % modulus, (a * d + b * c) % modulus


def gaussian_power(base: Gaussian, exponent: int, modulus: int) -> Gaussian:
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = gaussian_multiply(result, base, modulus)
        base = gaussian_multiply(base, base, modulus)
        exponent //= 2
    return result


def valuation(value: int, prime: int, cap: int = 100) -> int:
    if value == 0:
        return cap
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def expected_small_prime_valuation(prime: int, n: int) -> int:
    residue = n % 4
    if residue == 0:
        return 0
    base = 2 if prime == 3 and residue >= 2 else residue
    return base + sum(valuation(n - j, prime) for j in range(residue))


def verify_small_prime_formula(prime: int, limit: int, precision: int = 24) -> int:
    modulus = prime**precision
    bases = [
        (a, b)
        for a in range(1, prime)
        for b in range(1, prime)
    ]
    powers = [(1, 0)] * len(bases)
    for n in range(1, limit + 1):
        powers = [
            gaussian_multiply(power, base, modulus)
            for power, base in zip(powers, bases)
        ]
        real = sum(value[0] for value in powers) % modulus
        imaginary = sum(value[1] for value in powers) % modulus
        actual = min(
            valuation(real, prime, precision),
            valuation(imaginary, prime, precision),
        )
        expected = expected_small_prime_valuation(prime, n)
        assert actual == expected, (prime, n, actual, expected)
    return limit


def exact_gaussian_sum(prime: int, exponent: int) -> Gaussian:
    def multiply(left: Gaussian, right: Gaussian) -> Gaussian:
        a, b = left
        c, d = right
        return a * c - b * d, a * d + b * c

    def power(base: Gaussian, n: int) -> Gaussian:
        result = (1, 0)
        while n:
            if n & 1:
                result = multiply(result, base)
            base = multiply(base, base)
            n //= 2
        return result

    values = [
        power((a, b), exponent)
        for a in range(1, prime)
        for b in range(1, prime)
    ]
    return sum(value[0] for value in values), sum(value[1] for value in values)


def verify_counterexamples() -> int:
    certificates = (
        (7, 30, 5),
        (7, 42, 4),
        (11, 90, 4),
    )
    for prime, exponent, expected in certificates:
        real, imaginary = exact_gaussian_sum(prime, exponent)
        actual = min(
            valuation(real, prime),
            valuation(imaginary, prime),
        )
        assert actual == expected

    real, imaginary = exact_gaussian_sum(7, 30)
    assert real == 0
    assert imaginary == -6264101156848215194673755568
    assert (imaginary // 7**5) % 7 == 2
    return len(certificates)


def verify_conjecture_one_failure() -> int:
    prime = 37
    exponent = 32
    precision = 5
    modulus = prime**precision
    real = 0
    imaginary = 0
    for a in range(1, prime):
        for b in range(1, prime):
            value = gaussian_power((a, b), exponent, modulus)
            real = (real + value[0]) % modulus
            imaginary = (imaginary + value[1]) % modulus
    assert min(
        valuation(real, prime, precision),
        valuation(imaginary, prime, precision),
    ) == 2
    return 1


def verify_affine_orbits() -> int:
    points = {
        (a, b)
        for a in range(1, 5)
        for b in range(1, 5)
    }

    def quarter_turn(value: Gaussian) -> Gaussian:
        a, b = value
        return 5 - b, a

    orbits: list[list[Gaussian]] = []
    while points:
        value = next(iter(points))
        orbit = []
        for _ in range(4):
            orbit.append(value)
            points.remove(value)
            value = quarter_turn(value)
        assert value == orbit[0]
        orbits.append(orbit)
    assert len(orbits) == 4

    representatives = ((4, 4), (2, 4), (2, 1), (2, 3))
    fourth_powers = [
        gaussian_power(value, 4, 5)
        for value in representatives
    ]
    assert fourth_powers == [(1, 0), (3, 1), (3, 4), (1, 0)]
    assert (
        sum(value[0] for value in fourth_powers) % 5,
        sum(value[1] for value in fourth_powers) % 5,
    ) == (3, 0)
    return len(orbits)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()
    limit = 1_000_000 if args.extended else 100_000

    checks_3 = verify_small_prime_formula(3, limit)
    checks_5 = verify_small_prime_formula(5, limit)
    counterexamples = verify_counterexamples()
    conjecture_one_failures = verify_conjecture_one_failure()
    orbits = verify_affine_orbits()

    print(f"p=3 formula checks: {checks_3}")
    print(f"p=5 formula checks: {checks_5}")
    print(f"inert-prime counterexamples: {counterexamples}")
    print(f"printed mod-4-law counterexamples: {conjecture_one_failures}")
    print(f"affine quarter-turn orbits: {orbits}")


if __name__ == "__main__":
    main()
