"""Exact checks for the A108628 tower and first half-index theorem."""

from __future__ import annotations

from math import comb


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def primes_through(limit: int) -> list[int]:
    out: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % p for p in out if p * p <= candidate):
            out.append(candidate)
    return out


def sequence_value(n: int) -> int:
    return sum(
        comb(n, k) * comb(n + 1, k) * comb(n + k + 1, k)
        for k in range(n + 1)
    )


def legendre_coefficient_value(n: int) -> int:
    return sum(
        comb(n + 1, j) ** 2 * comb(2 * n + 1 - j, n - j)
        for j in range(n + 1)
    )


def dixon_sum(n: int) -> int:
    return sum(
        (-1) ** (n - j) * comb(n + 1, j) ** 2 * comb(n - 1, j - 1)
        for j in range(1, n + 1)
    )


def dixon_closed(n: int) -> int:
    if n % 2 == 0:
        return 0
    m = (n - 1) // 2
    return 4 * (-1) ** m * comb(2 * m, m) * comb(3 * m + 2, m)


def factorial_valuation(n: int, prime: int) -> int:
    out = 0
    while n:
        n //= prime
        out += n
    return out


def binomial_valuation(n: int, k: int, prime: int) -> int:
    return (
        factorial_valuation(n, prime)
        - factorial_valuation(k, prime)
        - factorial_valuation(n - k, prime)
    )


def check_identities() -> int:
    expected = (1, 7, 55, 471, 4251, 39733, 380731, 3716695)
    assert tuple(sequence_value(n) for n in range(len(expected))) == expected
    checks = len(expected)
    for n in range(1, 101):
        assert sequence_value(n) == legendre_coefficient_value(n)
        assert dixon_sum(n) == dixon_closed(n)
        checks += 2
    return checks


def check_first_half_index() -> int:
    checks = 0
    for prime in primes_through(251):
        if prime % 4 != 1:
            continue
        n = (prime - 1) // 2
        assert sequence_value(n) % prime == 0
        assert dixon_sum(n) == 0
        for j in range(1, n + 1):
            assert (
                comb(prime - j, n - j)
                - (-1) ** (n - j) * comb(n - 1, j - 1)
            ) % prime == 0
            checks += 1
        checks += 2
    return checks


def check_dixon_valuation() -> int:
    checks = 0
    for prime in primes_through(251):
        if prime % 4 != 3:
            continue
        for exponent in (1, 3, 5, 7, 9):
            m = (prime**exponent - 3) // 4
            depth = binomial_valuation(2 * m, m, prime)
            depth += binomial_valuation(3 * m + 2, m, prime)
            assert depth == exponent - 1
            checks += 1
    return checks


def check_remaining_boundaries() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for exponent in (2, 3):
            n = (prime**exponent - 1) // 2
            value = sequence_value(n)
            comparison = dixon_closed(n)
            depth = valuation(value, prime)
            expected = exponent if prime % 4 == 1 or exponent % 2 == 0 else exponent - 1
            assert depth >= expected
            assert valuation(value - comparison, prime) >= exponent
            if prime % 4 == 3 and exponent % 2 == 1:
                assert valuation(comparison, prime) == exponent - 1
            else:
                assert comparison == 0
            checks += 3
    for level, bound in ((1, 16), (2, 4)):
        scale = 5**level
        lower = 5 ** (level - 1)
        modulus = 5 ** (3 * level)
        for n in range(1, bound + 1):
            assert (
                sequence_value(n * scale - 1) - sequence_value(n * lower - 1)
            ) % modulus == 0
            checks += 1
    return checks


def main() -> None:
    identities = check_identities()
    boundary = check_first_half_index()
    dixon_valuation = check_dixon_valuation()
    remaining = check_remaining_boundaries()
    print(f"A108628 identity checks: {identities}")
    print(f"proved first half-index checks: {boundary}")
    print(f"Dixon valuation checks: {dixon_valuation}")
    print(f"remaining-boundary/tower evidence: {remaining}")
    print("A108628 half-index checks passed")


if __name__ == "__main__":
    main()
