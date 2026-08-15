"""Exact checks for CyclotomicRationalFramingTower.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


Profile = dict[int, int]


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def multiply(left: list[int], right: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[: degree + 1 - i]):
            if b:
                out[i + j] += a * b
    return out


def factor(exponent: int, step: int, degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for j in range(degree // step + 1):
        if exponent >= 0:
            if j > exponent:
                break
            value = comb(exponent, j) * (-1) ** j
        else:
            value = comb(-exponent + j - 1, j)
        out[j * step] = value
    return out


def coefficients(profile: Profile, exponent: int, degree: int) -> list[int]:
    out = [1] + [0] * degree
    for step, multiplicity in profile.items():
        out = multiply(out, factor(multiplicity * exponent, step, degree), degree)
    return out


def framed(profile: Profile, k: int, m: int, n: int) -> int:
    return coefficients(profile, m * n, k * n)[k * n]


def ghost_reduced(profile: Profile, prime: int, degree: int) -> list[Fraction]:
    log_coeff = [Fraction(0)] * (degree + 1)
    for step, multiplicity in profile.items():
        for j in range(1, degree // step + 1):
            log_coeff[step * j] -= Fraction(multiplicity, j)
    out = log_coeff[:]
    for n in range(prime, degree + 1, prime):
        out[n] -= log_coeff[n // prime] / prime
    return out


def depleted(profile: Profile, prime: int, degree: int) -> list[Fraction]:
    out = [Fraction(0)] * (degree + 1)
    for step, multiplicity in profile.items():
        for j in range(1, degree // step + 1):
            if j % prime:
                out[step * j] -= Fraction(multiplicity, j)
    return out


def check_depletion() -> int:
    checks = 0
    profiles = (
        {1: -1, 2: 1, 3: -1, 6: 1},
        {1: 1, 3: -1},
        {1: 2, 2: -3, 5: 1},
        {2: -2, 7: 3},
    )
    for profile in profiles:
        for prime in (3, 5, 7, 11):
            if any(step % prime == 0 for step in profile):
                continue
            left = ghost_reduced(profile, prime, 100)
            right = depleted(profile, prime, 100)
            for index in range(101):
                assert left[index] == right[index]
                if index and index % prime == 0:
                    assert right[index] == 0
                checks += 1
    return checks


def check_towers() -> int:
    checks = 0
    profiles = (
        {1: -1, 2: 1, 3: -1, 6: 1},  # A228960
        {1: 1, 3: -1},  # A350383
        {1: 2, 2: -3, 5: 1},
        {2: -2, 7: 3},
    )
    for profile in profiles:
        for prime in (3, 5, 7, 11):
            if any(step % prime == 0 for step in profile):
                continue
            for k in (1, 2, 3):
                for m in (-2, -1, 1, 2):
                    for n in (1, 2, 3):
                        for depth in (1, 2):
                            upper = n * prime**depth
                            lower = n * prime ** (depth - 1)
                            difference = framed(profile, k, m, upper)
                            difference -= framed(profile, k, m, lower)
                            assert valuation(difference, prime) >= 2 * depth
                            checks += 1
    return checks


def check_named_values() -> int:
    checks = 0
    a228 = {1: -1, 2: 1, 3: -1, 6: 1}
    a350 = {1: 1, 3: -1}
    # A228960 has offset 1.  The leading 1 below is the natural n=0
    # extension, followed by the OEIS values a(1), a(2), ... .
    expected_228 = [1, 1, 1, 4, 17, 51, 136, 393]
    expected_350 = [1, -1, 1, 2, -15, 49, -98, 48]
    for n, expected in enumerate(expected_228):
        assert framed(a228, 1, 1, n) == expected
        checks += 1
    for n, expected in enumerate(expected_350):
        assert framed(a350, 1, 1, n) == expected
        checks += 1
    return checks


def check_excluded_boundaries() -> int:
    a228 = {1: -1, 2: 1, 3: -1, 6: 1}
    a350 = {1: 1, 3: -1}
    # The step-dividing prime 3 genuinely fails at the first adjacent level
    # for both records.
    assert valuation(framed(a228, 1, 1, 3) - framed(a228, 1, 1, 1), 3) == 1
    assert valuation(framed(a350, 1, 1, 3) - framed(a350, 1, 1, 1), 3) == 1
    # Exclusion is only sufficient, not an assertion that every excluded
    # instance fails: A228960 happens to agree at the first binary level.
    assert framed(a228, 1, 1, 2) == framed(a228, 1, 1, 1)
    return 3


def main() -> None:
    depletion = check_depletion()
    towers = check_towers()
    named = check_named_values()
    boundaries = check_excluded_boundaries()
    total = depletion + towers + named + boundaries
    print("cyclotomic rational-framing checks passed")
    print(f"depleted-logarithm checks: {depletion}")
    print(f"tower checks: {towers}")
    print(f"named-value checks: {named}")
    print(f"excluded-prime boundary checks: {boundaries}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
