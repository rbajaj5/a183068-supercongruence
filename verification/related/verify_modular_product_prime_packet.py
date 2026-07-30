"""Exact checks for ModularProductPrimeCoefficientPacket.md."""

from __future__ import annotations

from math import comb
from random import Random


def multiply(left: list[int], right: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right[: degree + 1 - i]):
                if b:
                    out[i + j] += a * b
    return out


def factor(exponent: int, sign: int, step: int, degree: int) -> list[int]:
    """Truncation of (1-sign*x^step)^exponent."""
    out = [0] * (degree + 1)
    for j in range(degree // step + 1):
        if exponent >= 0:
            if j > exponent:
                break
            value = comb(exponent, j) * (-sign) ** j
        else:
            value = comb(-exponent + j - 1, j) * sign**j
        out[j * step] = value
    return out


def euler_coefficient(
    degree: int,
    scale: int,
    colors: tuple[tuple[int, int, int], ...],
) -> int:
    """Coefficient for factors (1-sign*x^m)^(h*scale*m^d)."""
    poly = [1] + [0] * degree
    for m in range(1, degree + 1):
        for sign, h, power in colors:
            exponent = h * scale * m**power
            poly = multiply(poly, factor(exponent, sign, m, degree), degree)
    return poly[degree]


def prime_coefficient(h: list[int], prime: int) -> int:
    poly = [1] + [0] * prime
    for m in range(1, prime + 1):
        poly = multiply(poly, factor(prime * h[m], 1, m, prime), prime)
    return poly[prime]


def check_universal_first_coefficient() -> int:
    rng = Random(20260729)
    checks = 0
    for prime in (3, 5, 7, 11, 13):
        for _ in range(30):
            h = [0] + [rng.randint(-3, 3) for _ in range(prime)]
            actual = prime_coefficient(h, prime)
            predicted = -h[1] - prime * h[prime]
            assert (actual - predicted) % prime**2 == 0
            checks += 1
    return checks


def check_named_prime_claims() -> int:
    checks = 0
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    families = (
        (((1, -1, 0),), lambda p: p + 1),          # A008485
        (((1, 1, 0),), lambda p: -p - 1),          # A008705
        (((-1, 1, 0),), lambda p: p + 1),          # A270913
        (((-1, 1, 0), (1, -1, 0)), lambda p: 2*p + 2),  # A270919
    )
    for colors, expected in families:
        for prime in primes:
            actual = euler_coefficient(prime, prime, colors)
            assert (actual - expected(prime)) % prime**2 == 0
            checks += 1

    for prime in primes:
        actual = euler_coefficient(2 * prime, 2 * prime, ((1, 1, 0),))
        assert (actual - (prime - 1)) % prime**2 == 0
        checks += 1
    return checks


def check_towers() -> tuple[int, int]:
    complete = (
        ((1, -1, 1),),                 # A255672
        ((-1, 1, 1),),                 # A270922
        ((-1, 1, 1), (1, -1, 1)),      # A270924
    )
    partial = (
        ((1, -1, 2),),                 # A023871
        ((1, -1, 4),),                 # A023873
        ((-1, 1, 2), (1, -1, 2)),      # A206622
        ((1, 1, 4),),                  # A283271
    )
    complete_checks = 0
    partial_checks = 0
    for families, counter_name in (
        (complete, "complete"),
        (partial, "partial"),
    ):
        for colors in families:
            for prime in (3, 5):
                for r in (1, 2):
                    for n in (1, 2):
                        upper = n * prime**r
                        lower = n * prime ** (r - 1)
                        high_value = euler_coefficient(upper, upper, colors)
                        low_value = euler_coefficient(lower, lower, colors)
                        assert (high_value - low_value) % prime ** (2 * r) == 0
                        if counter_name == "complete":
                            complete_checks += 1
                        else:
                            partial_checks += 1
    return complete_checks, partial_checks


def main() -> None:
    universal = check_universal_first_coefficient()
    named = check_named_prime_claims()
    complete, partial = check_towers()
    print("Modular-product prime coefficient packet checks passed")
    print(f"universal first-coefficient checks: {universal}")
    print(f"named prime-level checks: {named}")
    print(f"complete tower checks: {complete}")
    print(f"partial baseline checks: {partial}")
    print(f"total exact checks: {universal + named + complete + partial}")


if __name__ == "__main__":
    main()
