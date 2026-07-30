"""Exact checks for the crystalline-support/Frobenius-packet bridge."""

from __future__ import annotations

import random


def valuation(n: int, prime: int) -> int:
    if n == 0:
        raise ValueError("valuation of zero is not used")
    out = 0
    n = abs(n)
    while n % prime == 0:
        n //= prime
        out += 1
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    primes = 0
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            n //= trial
            primes += 1
            if n % trial == 0:
                return 0
            while n % trial == 0:
                n //= trial
        trial += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def ghost(primitive: list[int], n: int) -> int:
    return sum(d * primitive[d] for d in divisors(n))


def recover_primitive(ghosts: list[int], n: int) -> int:
    numerator = sum(mobius(d) * ghosts[n // d] for d in divisors(n))
    assert numerator % n == 0
    return numerator // n


def mu(pair: tuple[int, int], prime: int) -> tuple[int, int]:
    a, b = pair
    assert a > 0 and b == 0
    return a - 1, prime


def theta(pair: tuple[int, int], prime: int) -> tuple[int, int]:
    a, b = pair
    assert a < prime and b == 0
    return a + 1, prime


def nu(pair: tuple[int, int], prime: int) -> tuple[int, int]:
    a, b = pair
    assert a == 0
    return 1, prime - b


def zero_count(pair: tuple[int, int]) -> int:
    return sum(value == 0 for value in pair)


def check_local_moves() -> int:
    checks = 0
    for prime in (3, 5, 7, 11, 13):
        for a in range(1, prime + 1):
            before = (a, 0)
            after = mu(before, prime)
            expected = 0 if a == 1 else -1
            assert zero_count(after) - zero_count(before) == expected
            checks += 1

        for a in range(prime):
            before = (a, 0)
            after = theta(before, prime)
            expected = -2 if a == 0 else -1
            assert zero_count(after) - zero_count(before) == expected
            checks += 1

        for b in range(prime + 1):
            before = (0, b)
            after = nu(before, prime)
            if b == prime:
                expected = 0
            elif b == 0:
                expected = -2
            else:
                expected = -1
            assert zero_count(after) - zero_count(before) == expected
            checks += 1

        assert nu(mu((1, 0), prime), prime) == (1, 0)
        assert mu(nu((0, prime), prime), prime) == (0, prime)
        checks += 2
    return checks


def check_baseline_packets() -> int:
    rng = random.Random(260726305)
    limit = 180
    checks = 0
    primes = (2, 3, 5, 7, 11)

    for _ in range(24):
        primitive = [0] + [rng.randrange(0, 9) for _ in range(limit)]
        ghosts = [0] + [ghost(primitive, n) for n in range(1, limit + 1)]

        for n in range(1, limit + 1):
            assert recover_primitive(ghosts, n) == primitive[n]
            checks += 1

        for prime in primes:
            for m in range(1, 19):
                r = 1
                while m * prime**r <= limit:
                    top = m * prime**r
                    bottom = m * prime ** (r - 1)
                    modulus = prime ** (r + valuation(m, prime))
                    assert (ghosts[top] - ghosts[bottom]) % modulus == 0
                    checks += 1
                    r += 1
    return checks


def check_higher_dold_packets() -> int:
    rng = random.Random(183068)
    limit = 240
    checks = 0

    for prime in (2, 3, 5, 7):
        for depth in (1, 2, 3, 4):
            primitive = [0] * (limit + 1)
            for n in range(1, limit + 1):
                unit = rng.randrange(0, 10)
                exponent = valuation(n, prime)
                primitive[n] = unit * prime ** ((depth - 1) * exponent)

            ghosts = [0] + [ghost(primitive, n) for n in range(1, limit + 1)]
            for m in range(1, 31):
                if m % prime == 0:
                    continue
                r = 1
                while m * prime**r <= limit:
                    n = m * prime**r
                    assert primitive[n] % prime ** ((depth - 1) * r) == 0
                    assert (
                        ghosts[n] - ghosts[m * prime ** (r - 1)]
                    ) % prime ** (depth * r) == 0
                    checks += 2
                    r += 1
    return checks


def main() -> None:
    local = check_local_moves()
    baseline = check_baseline_packets()
    higher = check_higher_dold_packets()
    total = local + baseline + higher
    print(
        "crystalline support bridge:",
        f"{local} local-move checks,",
        f"{baseline} baseline-orbit checks,",
        f"{higher} higher-Dold checks;",
        f"{total} total",
    )


if __name__ == "__main__":
    main()
