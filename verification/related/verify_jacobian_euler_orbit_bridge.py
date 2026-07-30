"""Exact checks for the Jacobian collision/Euler-orbit bridge.

The checker supports the proof note.  It is not a substitute for the
displayed Möbius-inversion argument.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb, factorial, gcd
from random import Random


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def ghosts_from_orbits(orbits: list[int]) -> list[int]:
    """Return a_n = sum_{d|n} d b_d, with index zero unused."""
    limit = len(orbits) - 1
    ghosts = [0] * (limit + 1)
    for n in range(1, limit + 1):
        ghosts[n] = sum(d * orbits[d] for d in divisors(n))
    return ghosts


def orbit_numerators(ghosts: list[int]) -> list[int]:
    """Return n*b_n by Möbius inversion, with index zero unused."""
    limit = len(ghosts) - 1
    return [
        0,
        *[
            sum(mobius(e) * ghosts[n // e] for e in divisors(n))
            for n in range(1, limit + 1)
        ],
    ]


def generalized_binom(a: int, k: int) -> int:
    if k < 0:
        return 0
    if a >= 0:
        return comb(a, k) if k <= a else 0
    return (-1) ** k * comb(-a + k - 1, k)


@lru_cache(maxsize=None)
def a183068(n: int) -> int:
    return sum(
        factorial(2 * n + 2 * k)
        // (factorial(k) ** 4 * factorial(n - k) ** 2)
        for k in range(n + 1)
    )


@lru_cache(maxsize=None)
def coefficient_family(n: int, alpha: int = 1, beta: int = -1) -> int:
    """[x^n] ((1+x)^alpha (1-x)^beta)^n."""
    if n == 0:
        return 1
    return sum(
        generalized_binom(alpha * n, j)
        * generalized_binom(beta * n, n - j)
        * (-1) ** (n - j)
        for j in range(n + 1)
    )


@lru_cache(maxsize=None)
def catalan_truncation(n: int) -> int:
    """A333093: the nth Taylor truncation of C(x)^n at x=1."""
    if n == 0:
        return 1
    return sum(
        n * comb(n + 2 * k, k) // (n + 2 * k)
        for k in range(n + 1)
    )


@lru_cache(maxsize=None)
def apery(n: int) -> int:
    """A005259, the zeta(3) Apéry numbers."""
    return sum((comb(n, k) * comb(n + k, k)) ** 2 for k in range(n + 1))


@lru_cache(maxsize=None)
def franel_four(n: int) -> int:
    """A005260, the fourth-order Franel numbers."""
    return sum(comb(n, k) ** 4 for k in range(n + 1))


def cubic_collision_ghost(n: int, q: int) -> int:
    """Off-diagonal collisions of the degree-three map over F_(q^n)."""
    Q = q**n
    if q == 3:
        return Q * Q * (Q - 1)
    return (Q - 1) * (Q * Q + 2)


def check_mobius_dictionary(limit: int = 48) -> int:
    rng = Random(20260730)
    checks = 0
    for _ in range(24):
        orbits = [0] + [rng.randint(-20, 40) for _ in range(limit)]
        ghosts = ghosts_from_orbits(orbits)
        numerators = orbit_numerators(ghosts)
        for n in range(1, limit + 1):
            assert numerators[n] == n * orbits[n]
            checks += 1
        for p in (2, 3, 5, 7):
            power = p
            r = 1
            while power <= limit:
                for m in range(1, limit // power + 1):
                    if gcd(m, p) != 1:
                        continue
                    difference = ghosts[m * power] - ghosts[m * power // p]
                    expected = power * sum(
                        e * orbits[e * power] for e in divisors(m)
                    )
                    assert difference == expected
                    assert difference % power == 0
                    checks += 2
                power *= p
                r += 1
    return checks


def check_sequence_orbits(
    sequence,
    limit: int,
    primes: tuple[int, ...],
    excess_per_level: int,
    require_nonnegative: bool = False,
) -> int:
    ghosts = [0] + [sequence(n) for n in range(1, limit + 1)]
    numerators = orbit_numerators(ghosts)
    checks = 0
    for n in range(1, limit + 1):
        assert numerators[n] % n == 0
        if require_nonnegative:
            assert numerators[n] // n >= 0
        checks += 1
    for p in primes:
        power = p
        r = 1
        while power <= limit:
            for m in range(1, limit // power + 1):
                if gcd(m, p) != 1:
                    continue
                b = numerators[m * power] // (m * power)
                assert valuation(b, p) >= excess_per_level * r
                checks += 1
            power *= p
            r += 1
    return checks


def check_named_sequences() -> int:
    checks = 0
    # A183068 has a p^(2r) tower, hence one excess power per level.
    checks += check_sequence_orbits(
        a183068, limit=25, primes=(2, 3, 5, 7, 11, 13, 17, 19, 23), excess_per_level=1
    )
    # The proved coefficient family has a p^(3r) tower for p >= 5.
    checks += check_sequence_orbits(
        coefficient_family, limit=49, primes=(5, 7, 11, 13), excess_per_level=2
    )
    # A333093 remains conjectural; these are regression checks only.
    checks += check_sequence_orbits(
        catalan_truncation,
        limit=49,
        primes=(5, 7, 11, 13),
        excess_per_level=2,
        require_nonnegative=True,
    )
    # These two sequences are proved realizable by Zhang and have published
    # cubic supercongruences.  Their Euler exponents are actual primitive
    # orbit multiplicities, not merely formal signed exponents.
    checks += check_sequence_orbits(
        apery,
        limit=49,
        primes=(5, 7, 11, 13),
        excess_per_level=2,
        require_nonnegative=True,
    )
    checks += check_sequence_orbits(
        franel_four,
        limit=49,
        primes=(5, 7, 11, 13),
        excess_per_level=2,
        require_nonnegative=True,
    )
    return checks


def check_cubic_collision_scheme() -> int:
    checks = 0
    for q in (5, 7, 11):
        limit = q
        ghosts = [0] + [cubic_collision_ghost(n, q) for n in range(1, limit + 1)]
        numerators = orbit_numerators(ghosts)
        for n in range(1, limit + 1):
            assert numerators[n] % n == 0
            assert numerators[n] // n >= 0
            checks += 2
        difference = ghosts[q] - ghosts[1]
        assert valuation(difference, q) == 1
        assert valuation(numerators[q] // q, q) == 0
        checks += 2

    ghosts3 = [0] + [cubic_collision_ghost(n, 3) for n in range(1, 4)]
    assert valuation(ghosts3[3] - ghosts3[1], 3) == 2
    checks += 1
    return checks


def main() -> None:
    dictionary_checks = check_mobius_dictionary()
    sequence_checks = check_named_sequences()
    collision_checks = check_cubic_collision_scheme()
    total = dictionary_checks + sequence_checks + collision_checks
    print(f"Euler/Mobius dictionary checks: {dictionary_checks}")
    print(f"Named-sequence orbit checks: {sequence_checks}")
    print(f"Jacobian collision checks: {collision_checks}")
    print(f"All {total} exact checks passed.")


if __name__ == "__main__":
    main()
