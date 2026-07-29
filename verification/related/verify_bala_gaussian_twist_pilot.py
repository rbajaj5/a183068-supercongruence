"""Exact Gaussian-twist checks for three entries in the Bala--OEIS census.

These computations are triage and regression checks, not proofs.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Iterable

GaussianInteger = tuple[int, int]
SummandFamily = Callable[[int], Iterable[int]]


def gaussian_twist(terms: Iterable[int]) -> GaussianInteger:
    real = 0
    imag = 0
    for k, term in enumerate(terms):
        residue = k % 4
        if residue == 0:
            real += term
        elif residue == 1:
            imag += term
        elif residue == 2:
            real -= term
        else:
            imag -= term
    return real, imag


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


def gaussian_valuation(value: GaussianInteger, prime: int) -> int:
    return min(valuation(value[0], prime), valuation(value[1], prime))


def fourth_power_franel(n: int) -> Iterable[int]:
    return (math.comb(n, k) ** 4 for k in range(n + 1))


def apery(n: int) -> Iterable[int]:
    return (
        (math.comb(n, k) * math.comb(n + k, k)) ** 2
        for k in range(n + 1)
    )


def negative_binomial_square(n: int) -> Iterable[int]:
    if n == 0:
        return iter((1,))
    return (math.comb(n + k - 1, k) ** 2 for k in range(n + 1))


def adjacent_difference(
    family: SummandFamily, prime: int, r: int, n: int
) -> GaussianInteger:
    upper = gaussian_twist(family(n * prime**r))
    lower = gaussian_twist(family(n * prime ** (r - 1)))
    if prime % 4 == 3:
        lower = lower[0], -lower[1]
    return upper[0] - lower[0], upper[1] - lower[1]


def test_grid() -> Iterable[tuple[int, int, int]]:
    for prime in (3, 5, 7, 11, 13):
        for r, n_max in ((1, 8), (2, 4), (3, 1)):
            for n in range(1, n_max + 1):
                yield prime, r, n


def run_family(
    name: str,
    family: SummandFamily,
    required_exponent: Callable[[int, int], int],
) -> tuple[int, list[tuple[int, int, int, int]]]:
    checks = 0
    equality_witnesses: list[tuple[int, int, int, int]] = []
    for prime, r, n in test_grid():
        actual = gaussian_valuation(
            adjacent_difference(family, prime, r, n), prime
        )
        required = required_exponent(prime, r)
        assert actual >= required, (name, prime, r, n, actual, required)
        if actual == required:
            equality_witnesses.append((prime, r, n, actual))
        checks += 1
    assert equality_witnesses
    return checks, equality_witnesses


def main() -> None:
    families = (
        (
            "A005260",
            fourth_power_franel,
            lambda prime, r: 3 * r - (1 if prime == 3 else 0),
        ),
        ("A005259", apery, lambda _prime, r: 2 * r),
        ("A333592", negative_binomial_square, lambda _prime, r: 2 * r),
    )

    total = 0
    witnesses: dict[str, list[tuple[int, int, int, int]]] = {}
    for name, family, bound in families:
        checks, equality = run_family(name, family, bound)
        total += checks
        witnesses[name] = equality
        print(f"{name}: {checks} exact lower-bound checks passed")
        print(f"  first equality witnesses: {equality[:5]}")

    # Exact counterexamples to blindly copying a cubic untwisted exponent.
    assert gaussian_valuation(adjacent_difference(fourth_power_franel, 3, 1, 2), 3) == 2
    assert gaussian_valuation(adjacent_difference(apery, 5, 1, 1), 5) == 2
    assert (
        gaussian_valuation(
            adjacent_difference(negative_binomial_square, 5, 1, 1), 5
        )
        == 2
    )

    assert total == 195
    print(f"Total: {total} exact Gaussian-twist checks passed")
    print("All three stronger-bound counterexamples verified exactly.")


if __name__ == "__main__":
    main()
