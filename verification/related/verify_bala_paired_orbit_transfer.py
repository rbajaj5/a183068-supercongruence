"""Exact orbit-transfer tests for OEIS A376459--A376466.

These computations isolate a proof target; they are not a proof.
"""

from __future__ import annotations

import functools
import math


INFINITY = 10**9
SEQUENCES = tuple(range(459, 467))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return INFINITY
    value = abs(value)
    result = 0
    while value % prime == 0:
        result += 1
        value //= prime
    return result


@functools.cache
def crystal_ball(n: int, k: int) -> int:
    if n < 0 or k < 0:
        return 0
    return sum(
        math.comb(n, i) ** 2 * math.comb(n + k - i, k - i)
        for i in range(min(n, k) + 1)
    )


@functools.cache
def summands(sequence: int, n: int) -> tuple[int, ...]:
    result: list[int] = []
    for k in range(n + 1):
        left = math.comb(n, k)
        right = math.comb(n + k, k)
        h_forward = crystal_ball(n, k)
        h_reverse = crystal_ball(n, n - k)
        h_shifted = crystal_ball(n - 1, k)

        values = {
            459: (-1) ** (n + k) * left * right * h_reverse,
            460: (-1) ** (n + k) * left * right**2 * h_forward,
            461: left**2 * right * h_forward,
            462: left**2 * right * h_reverse,
            463: left**2 * right**2 * h_forward,
            464: left**2 * right**2 * h_reverse,
            465: left**2 * right**2 * h_shifted,
            466: (-1) ** (n + k) * left * right**2 * h_shifted,
        }
        result.append(values[sequence])
    return tuple(result)


def sequence_value(sequence: int, n: int) -> int:
    return sum(summands(sequence, n))


def stratum_sum(sequence: int, n: int, prime: int, level: int) -> int:
    terms = summands(sequence, n)
    return sum(
        terms[k]
        for k in range(1, n + 1)
        if valuation(k, prime) == level
    )


def test_grid() -> tuple[tuple[int, int, int], ...]:
    cases: list[tuple[int, int, int]] = []
    for prime in (5, 7, 11):
        cases.extend((prime, 1, n) for n in range(1, 4))
    for prime in (5, 7):
        cases.extend((prime, 2, n) for n in range(1, 3))
    cases.append((5, 3, 1))
    return tuple(cases)


def gaussian_twist(terms: tuple[int, ...]) -> tuple[int, int]:
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


def gaussian_adjacent_valuation(
    sequence: int, prime: int, r: int, n: int
) -> int:
    upper = gaussian_twist(summands(sequence, n * prime**r))
    lower = gaussian_twist(summands(sequence, n * prime ** (r - 1)))
    if prime % 4 == 3:
        lower = lower[0], -lower[1]
    return min(
        valuation(upper[0] - lower[0], prime),
        valuation(upper[1] - lower[1], prime),
    )


def orbit_transfer_checks() -> int:
    checks = 0
    for sequence in SEQUENCES:
        for prime, r, n in test_grid():
            upper_n = n * prime**r
            lower_n = upper_n // prime
            target = 3 * r

            unit = stratum_sum(sequence, upper_n, prime, 0)
            assert valuation(unit, prime) >= target
            checks += 1

            upper_zero = summands(sequence, upper_n)[0]
            lower_zero = summands(sequence, lower_n)[0]
            assert valuation(upper_zero - lower_zero, prime) >= target
            checks += 1

            # Include the top stratum v_p(k) = r. Omitting it would leave
            # the telescoping certificate incomplete even though the
            # adjacent sequence congruence is also checked below.
            for level in range(1, valuation(upper_n, prime) + 1):
                transfer = stratum_sum(
                    sequence, upper_n, prime, level
                ) - stratum_sum(sequence, lower_n, prime, level - 1)
                assert valuation(transfer, prime) >= target
                checks += 1

            adjacent = sequence_value(sequence, upper_n) - sequence_value(
                sequence, lower_n
            )
            assert valuation(adjacent, prime) >= target
            checks += 1
    return checks


def partition_depth_checks() -> int:
    checks = 0
    expected = {
        459: (1, 3, 3),
        460: (1, 2, 3),
        461: (2, 2, 3),
        462: (2, 2, 3),
        463: (2, 2, 3),
        464: (2, 2, 3),
        465: (2, 2, 3),
        466: (1, 2, 3),
    }
    for sequence in SEQUENCES:
        for prime in (5, 7, 11, 13):
            terms = summands(sequence, prime)
            individual_depth = min(
                valuation(terms[k], prime) for k in range(1, prime)
            )
            paired_depth = min(
                valuation(terms[k] + terms[prime - k], prime)
                for k in range(1, (prime + 1) // 2)
            )
            unit_depth = valuation(sum(terms[1:prime]), prime)
            required = expected[sequence]
            assert individual_depth == required[0]
            assert paired_depth == required[1]
            assert unit_depth >= required[2]
            checks += 1
    return checks


def gaussian_boundary_checks() -> int:
    checks = 0
    depth = {
        459: 1,
        460: 1,
        461: 2,
        462: 2,
        463: 2,
        464: 2,
        465: 2,
        466: 1,
    }
    cases = ((5, 1, 1), (7, 1, 1), (11, 1, 1), (5, 2, 1))
    for sequence in SEQUENCES:
        for prime, r, n in cases:
            actual = gaussian_adjacent_valuation(sequence, prime, r, n)
            assert actual == depth[sequence] * r
            checks += 1
    return checks


def main() -> None:
    orbit_checks = orbit_transfer_checks()
    partition_checks = partition_depth_checks()
    gaussian_checks = gaussian_boundary_checks()
    total = orbit_checks + partition_checks + gaussian_checks

    assert orbit_checks == 496
    assert partition_checks == 32
    assert gaussian_checks == 32
    assert total == 560

    print(f"Orbit and transfer checks: {orbit_checks}")
    print(f"Partition-depth checks: {partition_checks}")
    print(f"Gaussian-boundary checks: {gaussian_checks}")
    print(f"Total: {total} exact checks passed.")


if __name__ == "__main__":
    main()
