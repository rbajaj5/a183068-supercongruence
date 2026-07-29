"""Exact checks for the binomial-power polynomial Frobenius theorem.

The proof is in related-results/BinomialPowerFrobeniusTheorem.md.
"""

from __future__ import annotations

import math
from collections.abc import Iterable

GaussianInteger = tuple[int, int]


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def exponent(prime: int, power: int, r: int) -> int:
    loss = 2 if prime == 2 else 1 if prime == 3 else 0
    return 3 * r - loss + valuation(power, prime)


def coefficient_difference(
    prime: int, power: int, r: int, n: int, k: int
) -> int:
    upper_n = n * prime**r
    lower_n = n * prime ** (r - 1)
    upper = math.comb(upper_n, k) ** power
    lower = 0
    if k % prime == 0:
        lower = math.comb(lower_n, k // prime) ** power
    return upper - lower


def gaussian_twist(n: int, power: int) -> GaussianInteger:
    real = 0
    imag = 0
    for k in range(n + 1):
        term = math.comb(n, k) ** power
        if k % 4 == 0:
            real += term
        elif k % 4 == 1:
            imag += term
        elif k % 4 == 2:
            real -= term
        else:
            imag -= term
    return real, imag


def alternating_sum(n: int, power: int) -> int:
    return sum(
        (-1) ** k * math.comb(n, k) ** power for k in range(n + 1)
    )


def gaussian_difference(
    prime: int, power: int, r: int, n: int
) -> GaussianInteger:
    upper = gaussian_twist(n * prime**r, power)
    lower_n = n * prime ** (r - 1)
    if prime == 2:
        return upper[0] - alternating_sum(lower_n, power), upper[1]
    lower = gaussian_twist(lower_n, power)
    if prime % 4 == 3:
        lower = lower[0], -lower[1]
    return upper[0] - lower[0], upper[1] - lower[1]


def grid() -> Iterable[tuple[int, int, int, int]]:
    for power in range(3, 9):
        for prime in (2, 3, 5, 7):
            for r, n_max in ((1, 5), (2, 3), (3, 1)):
                for n in range(1, n_max + 1):
                    yield prime, power, r, n
        yield 2, power, 4, 1


def main() -> None:
    coefficient_checks = 0
    gaussian_checks = 0
    coefficient_equalities: list[tuple[int, int, int, int, int, int]] = []
    gaussian_equalities: list[tuple[int, int, int, int, int]] = []
    binary_minimum_slack = {power: 10**9 for power in range(3, 9)}

    for prime, power, r, n in grid():
        required = exponent(prime, power, r)
        upper_n = n * prime**r
        for k in range(upper_n + 1):
            actual = valuation(
                coefficient_difference(prime, power, r, n, k), prime
            )
            assert actual >= required, (
                prime,
                power,
                r,
                n,
                k,
                actual,
                required,
            )
            if actual == required:
                coefficient_equalities.append(
                    (prime, power, r, n, k, actual)
                )
            if prime == 2:
                binary_minimum_slack[power] = min(
                    binary_minimum_slack[power], actual - required
                )
            coefficient_checks += 1

        real, imag = gaussian_difference(prime, power, r, n)
        actual = min(valuation(real, prime), valuation(imag, prime))
        assert actual >= required, (
            prime,
            power,
            r,
            n,
            actual,
            required,
        )
        if actual == required:
            gaussian_equalities.append((prime, power, r, n, actual))
        gaussian_checks += 1

    # The formula covers the first three binary multiplicity classes.
    for power, expected in ((3, 1), (6, 2), (4, 3)):
        required = exponent(2, power, 1)
        assert required == expected
    assert all(slack >= 0 for slack in binary_minimum_slack.values())

    # The p=3 loss is genuine for the fourth-power Gaussian specialization.
    real, imag = gaussian_difference(3, 4, 1, 2)
    assert min(valuation(real, 3), valuation(imag, 3)) == 2

    assert coefficient_equalities
    assert gaussian_equalities
    print(f"polynomial coefficient checks: {coefficient_checks}")
    print(f"Gaussian specialization checks: {gaussian_checks}")
    print(f"first coefficient equalities: {coefficient_equalities[:10]}")
    print(f"first Gaussian equalities: {gaussian_equalities[:10]}")
    print(f"binary minimum slack by power: {binary_minimum_slack}")
    print("binary and odd-prime multiplicity bonuses verified")
    print("exact p=3 obstruction to exponent 3r verified")


if __name__ == "__main__":
    main()
