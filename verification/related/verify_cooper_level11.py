"""Exact p-adic checks for Cooper's level-11 rare-prime conjecture."""

from __future__ import annotations

import argparse
import math


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit - 1) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (
                (limit - 1 - p * p) // p + 1
            )
    return [p for p in range(2, limit) if sieve[p]]


def vp_factorial(n: int, p: int) -> int:
    answer = 0
    while n:
        n //= p
        answer += n
    return answer


def vp(n: int, p: int) -> int:
    answer = 0
    while n and n % p == 0:
        n //= p
        answer += 1
    return answer


def t11_exact(limit: int) -> list[int]:
    values = [1]
    t_minus_two = 0
    t_minus_one = 0
    t = 1
    for n in range(limit):
        numerator = (
            (2 * n + 1) * (10 * n * n + 10 * n + 4) * t
            + n * (-56 * n * n - 8) * t_minus_one
            + 22 * n * (2 * n - 1) * (n - 1) * t_minus_two
        )
        denominator = (n + 1) ** 3
        assert numerator % denominator == 0
        following = numerator // denominator
        values.append(following)
        t_minus_two, t_minus_one, t = t_minus_one, t, following
    return values


def t11_padic_differences(p: int, max_n: int) -> list[int]:
    """Return T(p*n)-T(n) modulo p^2 without constructing full integers."""
    limit = p * max_n
    precision = 2 + 3 * vp_factorial(limit, p)
    modulus = p**precision
    t_minus_two = 0
    t_minus_one = 0
    t = 1
    small = {0: 1}
    differences: list[int] = []

    for n in range(limit):
        numerator = (
            (2 * n + 1) * (10 * n * n + 10 * n + 4) * t
            + n * (-56 * n * n - 8) * t_minus_one
            + 22 * n * (2 * n - 1) * (n - 1) * t_minus_two
        ) % modulus

        exponent = vp(n + 1, p)
        p_part = p ** (3 * exponent)
        unit = ((n + 1) // (p**exponent)) ** 3
        if exponent:
            assert numerator % p_part == 0
            precision -= 3 * exponent
            modulus //= p_part
            following = (numerator // p_part) * pow(unit, -1, modulus) % modulus
        else:
            following = numerator * pow(unit, -1, modulus) % modulus

        t_minus_two, t_minus_one, t = (
            t_minus_one % modulus,
            t % modulus,
            following,
        )
        index = n + 1
        if index <= max_n:
            small[index] = following % (p * p)
        if index % p == 0:
            j = index // p
            differences.append((following - small[j]) % (p * p))

    assert precision == 2
    return differences


def first_obstruction_scan(limit: int) -> list[int]:
    hits = []
    for p in primes_below(limit):
        if p == 2:
            continue
        if t11_padic_differences(p, 1)[0] == 0:
            hits.append(p)
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--extended",
        action="store_true",
        help="reproduce the longer checks reported in the research note",
    )
    args = parser.parse_args()

    exact = t11_exact(600)
    for p in (3, 5, 7, 59):
        differences = t11_padic_differences(p, 10)
        for n, difference in enumerate(differences, 1):
            assert difference == (exact[p * n] - exact[n]) % (p * p)

    scan_limit = 30_000 if args.extended else 10_000
    hits = first_obstruction_scan(scan_limit)
    assert hits == [59, 5581]

    ranges = ((59, 2_000), (5581, 100)) if args.extended else ((59, 250), (5581, 30))
    for p, max_n in ranges:
        differences = t11_padic_differences(p, max_n)
        assert all(value == 0 for value in differences)
        print(f"p={p}: T(p*n) == T(n) mod p^2 for 1 <= n <= {max_n}")

    print(f"odd-prime n=1 scan below {scan_limit}: {hits}")
    print("all Cooper level-11 checks passed")


if __name__ == "__main__":
    main()
