"""Exact checks for the Gaussian angular X-ray spectrum."""

from __future__ import annotations

from collections import Counter
from random import Random


Vector = tuple[int, int]


def primes_through(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = [False] * (
                (limit - prime * prime) // prime + 1
            )
    return [prime for prime, is_prime in enumerate(sieve) if is_prime]


def norm(vector: Vector, prime: int) -> int:
    x, y = vector
    return (x * x + y * y) % prime


def dot(left: Vector, right: Vector, prime: int) -> int:
    return (left[0] * right[0] + left[1] * right[1]) % prime


def canonical_direction(vector: Vector, prime: int) -> Vector:
    x, y = vector
    if x % prime:
        inverse = pow(x, -1, prime)
        return 1, y * inverse % prime
    assert y % prime
    return 0, 1


def add_scaled(base: Vector, direction: Vector, scale: int, prime: int) -> Vector:
    return (
        (base[0] + scale * direction[0]) % prime,
        (base[1] + scale * direction[1]) % prime,
    )


def verify_prime(prime: int) -> tuple[int, int]:
    squares = {value * value % prime for value in range(1, prime)}
    unit_circle = {
        (x, y)
        for x in range(prime)
        for y in range(prime)
        if norm((x, y), prime) == 1
    }
    directions = {
        canonical_direction(vector, prime)
        for vector in unit_circle
    }

    assert len(unit_circle) == prime + 1
    assert len(directions) == (prime + 1) // 2

    all_directions = {
        (1, slope)
        for slope in range(prime)
    } | {(0, 1)}
    assert directions == {
        direction
        for direction in all_directions
        if norm(direction, prime) in squares
    }

    spectrum = Counter()
    spectral_checks = 0
    for x in range(prime):
        for y in range(prime):
            frequency = (x, y)
            eigenvalue = sum(
                dot(frequency, direction, prime) == 0
                for direction in directions
            )
            if frequency == (0, 0):
                expected = len(directions)
                packet = "constant"
            elif norm(frequency, prime) in squares:
                expected = 1
                packet = "square"
            else:
                expected = 0
                packet = "nonsquare"
            assert eigenvalue == expected
            spectrum[packet] += 1
            spectral_checks += 1

    assert spectrum == {
        "constant": 1,
        "square": (prime * prime - 1) // 2,
        "nonsquare": (prime * prime - 1) // 2,
    }

    incidence_checks = 0
    for seed in range(5):
        random = Random((prime << 8) + seed)
        selected_lines = []
        for direction in sorted(directions):
            base = (random.randrange(prime), random.randrange(prime))
            selected_lines.append(
                {
                    add_scaled(base, direction, scale, prime)
                    for scale in range(prime)
                }
            )

        for index, line in enumerate(selected_lines):
            assert len(line) == prime
            for other in selected_lines[index + 1 :]:
                assert len(line & other) == 1

        multiplicity = Counter(
            point
            for line in selected_lines
            for point in line
        )
        direction_count = len(directions)
        assert sum(multiplicity.values()) == direction_count * prime
        assert sum(value * value for value in multiplicity.values()) == (
            direction_count * direction_count
            + direction_count * (prime - 1)
        )
        support = len(multiplicity)
        assert support * (direction_count + prime - 1) >= (
            direction_count * prime * prime
        )
        incidence_checks += 1

    return spectral_checks, incidence_checks


def main() -> None:
    spectral_checks = 0
    incidence_checks = 0
    primes = [
        prime
        for prime in primes_through(43)
        if prime % 4 == 3
    ]
    for prime in primes:
        spectral, incidence = verify_prime(prime)
        spectral_checks += spectral
        incidence_checks += incidence

    print(f"inert primes checked: {len(primes)}")
    print(f"spectral packets checked: {spectral_checks}")
    print(f"translated line families checked: {incidence_checks}")


if __name__ == "__main__":
    main()
