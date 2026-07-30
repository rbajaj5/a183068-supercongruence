"""Exact checks for MultinomialPowerFrobeniusTowers.md.

The computations are regression evidence for the written proof, not a
substitute for it.
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial
from typing import Iterator


def compositions(total: int, parts: int) -> Iterator[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


@lru_cache(maxsize=None)
def multinomial(items: tuple[int, ...]) -> int:
    value = factorial(sum(items))
    for item in items:
        value //= factorial(item)
    return value


@lru_cache(maxsize=None)
def power_sum(total: int, parts: int, exponent: int) -> int:
    return sum(
        multinomial(items) ** exponent
        for items in compositions(total, parts)
    )


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def check_initial_values() -> int:
    expected = [1, 3, 27, 381, 6219, 111753, 2151549, 43497891]
    observed = [power_sum(n, 3, 3) for n in range(len(expected))]
    assert observed == expected
    return len(expected)


def check_coefficientwise_transfer() -> int:
    checks = 0
    regimes = (
        (5, (3, 4, 5)),
        (7, (3, 4)),
        (3, (3, 6)),
        (2, (4, 8)),
    )
    for prime, exponents in regimes:
        for parts in (2, 3, 4):
            for exponent in exponents:
                for r in (1, 2):
                    for n in (1, 2):
                        lower_total = n * prime ** (r - 1)
                        modulus = prime ** (3 * r)
                        for lower in compositions(lower_total, parts):
                            upper = tuple(prime * item for item in lower)
                            difference = (
                                multinomial(upper) ** exponent
                                - multinomial(lower) ** exponent
                            )
                            assert difference % modulus == 0
                            checks += 1
    return checks


def check_discarded_coefficients() -> int:
    checks = 0
    regimes = (
        (5, 3),
        (5, 5),
        (3, 3),
        (3, 6),
        (2, 4),
        (2, 8),
    )
    for prime, exponent in regimes:
        for parts in (2, 3, 4):
            for r in (1, 2):
                total = prime**r
                modulus = prime ** (3 * r)
                for items in compositions(total, parts):
                    if all(item % prime == 0 for item in items):
                        continue
                    assert multinomial(items) ** exponent % modulus == 0
                    checks += 1
    return checks


def check_scalar_towers() -> int:
    checks = 0
    cases = (
        (5, 3),
        (5, 4),
        (7, 3),
        (3, 3),
        (3, 6),
        (2, 4),
        (2, 8),
    )
    for prime, exponent in cases:
        for parts in (2, 3, 4):
            for r in (1, 2):
                for n in (1, 2):
                    upper = power_sum(n * prime**r, parts, exponent)
                    lower = power_sum(n * prime ** (r - 1), parts, exponent)
                    assert (upper - lower) % prime ** (3 * r) == 0
                    checks += 1
    return checks


def check_a141057_boundaries() -> int:
    checks = 0
    for prime in (3, 5, 7, 11):
        for r in (1, 2):
            upper = power_sum(prime**r, 3, 3)
            lower = power_sum(prime ** (r - 1), 3, 3)
            assert (upper - lower) % prime ** (3 * r) == 0
            checks += 1

    binary_difference = power_sum(4, 3, 3) - power_sum(2, 3, 3)
    assert binary_difference == 6192
    assert vp(binary_difference, 2) == 4
    checks += 2
    return checks


def main() -> None:
    sections = {
        "initial values": check_initial_values(),
        "powered transfers": check_coefficientwise_transfer(),
        "discarded coefficients": check_discarded_coefficients(),
        "scalar towers": check_scalar_towers(),
        "A141057 boundaries": check_a141057_boundaries(),
    }
    print("Multinomial-power Frobenius checks passed")
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"total exact checks: {sum(sections.values())}")


if __name__ == "__main__":
    main()
