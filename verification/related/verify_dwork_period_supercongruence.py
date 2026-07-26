"""Exact checks for the Dwork-period multinomial supercongruence."""

from __future__ import annotations

import functools
import math


PRIMES = (2, 3, 5, 7)


def vp(value: int, prime: int) -> int:
    """Return the p-adic valuation of a nonzero integer."""
    assert value
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def digit_sum(value: int, prime: int) -> int:
    """Return the sum of the base-p digits of value."""
    answer = 0
    while value:
        answer += value % prime
        value //= prime
    return answer


@functools.cache
def equal_multinomial(degree: int, index: int) -> int:
    """Return (degree * index)! / index!^degree."""
    return math.factorial(degree * index) // math.factorial(index) ** degree


def epsilon(prime: int) -> int:
    if prime == 2:
        return 2
    if prime == 3:
        return 1
    return 0


def main() -> None:
    checked = 0
    for prime in PRIMES:
        for degree in range(2, 9):
            factorial_gain = vp(math.factorial(degree), prime)
            for index in range(1, 9):
                value = equal_multinomial(degree, index)
                legendre = (
                    degree * digit_sum(index, prime)
                    - digit_sum(degree * index, prime)
                ) // (prime - 1)
                assert vp(value, prime) == legendre
                assert legendre >= factorial_gain

                for scale in range(1, 3):
                    upper = equal_multinomial(
                        degree, index * prime**scale
                    )
                    lower = equal_multinomial(
                        degree, index * prime ** (scale - 1)
                    )
                    predicted = (
                        3 * (scale + vp(index, prime))
                        - epsilon(prime)
                        + digit_sum(index, prime) * factorial_gain
                    )
                    assert vp(upper - lower, prime) >= predicted
                    checked += 1

    print(
        "Dwork-period scaling:"
        f" {checked} exact adjacent-scale cases passed"
    )


if __name__ == "__main__":
    main()
