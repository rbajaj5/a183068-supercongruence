"""Exact checks for the Peter Bala OEIS supercongruence queue.

Two families in BalaOeisSupercongruenceQueue.md are proved there.  The
remaining tower checks in this file are explicitly computational evidence,
not proofs.
"""

from functools import lru_cache
from math import comb


PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
TOWER_PRIMES = (5, 7, 11, 13, 17, 19)


def generalized_binomial(n: int, k: int) -> int:
    """Return the integral generalized binomial coefficient."""
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


def valuation(value: int, prime: int) -> int:
    """Return v_prime(value), with a large sentinel for zero."""
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


@lru_cache(maxsize=None)
def a365029_family(n: int, exponent_a: int, exponent_b: int) -> int:
    """The two-parameter family containing A365029 at (A,B)=(2,1)."""
    return sum(
        generalized_binomial(n + k - 1, k) ** exponent_a
        * generalized_binomial(2 * k - 1, n) ** exponent_b
        for k in range(n + 1)
    )


@lru_cache(maxsize=None)
def bala_odd_power(n: int, m: int) -> int:
    """The A375178 family b_m(n), whose exponent is 2m+1."""
    exponent = 2 * m + 1
    return sum(
        generalized_binomial(n + k - 1, k) ** exponent
        for k in range(n)
    )


@lru_cache(maxsize=None)
def a333593(n: int) -> int:
    """The signed negative-binomial square sum A333593."""
    return sum(
        (-1) ** (n + k)
        * generalized_binomial(n + k - 1, k) ** 2
        for k in range(n + 1)
    )


def check_a365029_boundary_theorem() -> tuple[int, int]:
    """Check a_{A,B}(p-1)=1 mod p^(A+B)."""
    checks = 0
    minimum_slack = 10**9
    for prime in PRIMES:
        for exponent_a in range(1, 7):
            for exponent_b in range(1, 6):
                difference = (
                    a365029_family(prime - 1, exponent_a, exponent_b) - 1
                )
                slack = (
                    valuation(difference, prime)
                    - exponent_a
                    - exponent_b
                )
                assert slack >= 0, (
                    prime,
                    exponent_a,
                    exponent_b,
                    slack,
                )
                minimum_slack = min(minimum_slack, slack)
                checks += 1
    assert checks == 390
    assert minimum_slack == 0
    return checks, minimum_slack


def check_a375178_prime_level_theorem() -> tuple[int, int]:
    """Check b_m(p)=1 mod p^(2m+3) in the proved range."""
    checks = 0
    minimum_slack = 10**9
    for m in range(1, 7):
        target = 2 * m + 3
        for prime in PRIMES:
            if prime < 2 * m + 5:
                continue
            difference = bala_odd_power(prime, m) - 1
            slack = valuation(difference, prime) - target
            assert slack >= 0, (m, prime, slack)
            minimum_slack = min(minimum_slack, slack)
            checks += 1
    assert checks == 56
    assert minimum_slack == 0
    return checks, minimum_slack


def check_a333593_tower_evidence() -> tuple[int, int]:
    """Check Bala's still-open A333593 p^(3r) tower."""
    checks = 0
    minimum_slack = 10**9
    for prime in TOWER_PRIMES:
        for level in range(1, 4):
            for n in range(1, 16):
                if n * prime**level > 500:
                    continue
                difference = a333593(n * prime**level) - a333593(
                    n * prime ** (level - 1)
                )
                slack = valuation(difference, prime) - 3 * level
                assert slack >= 0, (prime, level, n, slack)
                minimum_slack = min(minimum_slack, slack)
                checks += 1
    assert checks == 128
    assert minimum_slack == 0
    return checks, minimum_slack


def check_a365029_tower_evidence() -> tuple[int, int]:
    """Check the still-open A365029 p^(3r) tower."""
    checks = 0
    minimum_slack = 10**9
    for prime in TOWER_PRIMES:
        for level in range(1, 4):
            for n in range(1, 16):
                if n * prime**level > 500:
                    continue
                difference = a365029_family(
                    n * prime**level, 2, 1
                ) - a365029_family(n * prime ** (level - 1), 2, 1)
                slack = valuation(difference, prime) - 3 * level
                assert slack >= 0, (prime, level, n, slack)
                minimum_slack = min(minimum_slack, slack)
                checks += 1
    assert checks == 128
    assert minimum_slack == 0
    return checks, minimum_slack


def check_a375178_tower_evidence() -> tuple[int, int]:
    """Check the still-open higher-level b_m tower for m=1,...,4."""
    checks = 0
    minimum_slack = 10**9
    for m in range(1, 5):
        for prime in TOWER_PRIMES:
            if prime < 2 * m + 5:
                continue
            for level in (2, 3):
                if prime**level > 500:
                    continue
                difference = bala_odd_power(
                    prime**level, m
                ) - bala_odd_power(prime ** (level - 1), m)
                target = 3 * level + 2 * m + 1
                slack = valuation(difference, prime) - target
                assert slack >= 0, (m, prime, level, slack)
                minimum_slack = min(minimum_slack, slack)
                checks += 1
    assert checks == 17
    assert minimum_slack == 0
    return checks, minimum_slack


def main() -> None:
    boundary_checks, boundary_slack = check_a365029_boundary_theorem()
    prime_checks, prime_slack = check_a375178_prime_level_theorem()
    a333_checks, a333_slack = check_a333593_tower_evidence()
    a365_checks, a365_slack = check_a365029_tower_evidence()
    odd_checks, odd_slack = check_a375178_tower_evidence()

    print(
        "proved A365029-family boundary cases: "
        f"{boundary_checks} (minimum slack {boundary_slack})"
    )
    print(
        "proved A375178-family prime cases: "
        f"{prime_checks} (minimum slack {prime_slack})"
    )
    print(
        "open A333593 tower evidence: "
        f"{a333_checks} (minimum slack {a333_slack})"
    )
    print(
        "open A365029 tower evidence: "
        f"{a365_checks} (minimum slack {a365_slack})"
    )
    print(
        "open A375178-family tower evidence: "
        f"{odd_checks} (minimum slack {odd_slack})"
    )
    print(
        "all "
        f"{boundary_checks + prime_checks + a333_checks + a365_checks + odd_checks} "
        "Bala-queue checks passed"
    )


if __name__ == "__main__":
    main()
