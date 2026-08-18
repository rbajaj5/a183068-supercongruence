"""Exact checks for the Peter Bala OEIS supercongruence queue.

Three results in BalaOeisSupercongruenceQueue.md are proved or reduced there.
The remaining A365029 and A375178 tower checks in this file are explicitly
computational evidence, not proofs.
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
def bala_power(n: int, exponent: int) -> int:
    """The generalized A375178 sum with arbitrary positive exponent."""
    return sum(
        generalized_binomial(n + k - 1, k) ** exponent
        for k in range(n)
    )


def bala_odd_power(n: int, m: int) -> int:
    """The A375178 family b_m(n), whose exponent is 2m+1."""
    return bala_power(n, 2 * m + 1)


def signed_dilation_value(n: int, dilation: int, m: int) -> int:
    """Return S_(A,m)(n) for the signed A375179/A375180 family."""
    exponent = 2 * m + 1
    return sum(
        (-1) ** (n + k + 1)
        * generalized_binomial(dilation * n, k) ** exponent
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


@lru_cache(maxsize=None)
def coster_signed_apery(n: int) -> int:
    """The generalized Apéry sum w_(0,2,-1)(n) used by Coster."""
    return sum(
        (-1) ** k * generalized_binomial(n + k, k) ** 2
        for k in range(n + 1)
    )


def a333593_central_tail(n: int) -> int:
    """The final summand separated from A333593."""
    return generalized_binomial(2 * n - 1, n) ** 2


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


def check_even_power_prime_level_theorem() -> tuple[int, int]:
    """Check B_q(p)=1 mod p^(q+1) for even q and p>=q+3."""
    checks = 0
    minimum_slack = 10**9
    for exponent in range(2, 13, 2):
        target = exponent + 1
        for prime in PRIMES:
            if prime < exponent + 3:
                continue
            difference = bala_power(prime, exponent) - 1
            slack = valuation(difference, prime) - target
            assert slack >= 0, (exponent, prime, slack)
            minimum_slack = min(minimum_slack, slack)
            checks += 1
    assert checks == 60
    assert minimum_slack == 0

    # The excluded p=5 boundary for both named fifth-power claims is sharp.
    assert valuation(bala_power(5, 3) - 1, 5) == 4
    assert valuation(bala_power(5, 4) - 1, 5) == 4
    return checks + 2, minimum_slack


def check_signed_dilation_prime_level_theorem() -> tuple[int, int]:
    """Check the arbitrary-dilation odd-power boundary theorem."""
    checks = 0
    minimum_slack = 10**9
    for dilation in range(-2, 6):
        for m in range(1, 7):
            target = 2 * m + 3
            for prime in PRIMES:
                if prime < 2 * m + 5:
                    continue
                difference = signed_dilation_value(prime, dilation, m) - 1
                slack = valuation(difference, prime) - target
                assert slack >= 0, (dilation, m, prime, slack)
                minimum_slack = min(minimum_slack, slack)
                checks += 1
    assert checks == 448
    assert minimum_slack == 0
    return checks, minimum_slack


def check_signed_dilation_named_sequences() -> int:
    """Match the initial A375179 and A375180 values printed by OEIS."""
    expected = {
        2: (0, 1, 63, 3160, 154175, 7623126, 385867944, 20012582304),
        3: (0, 1, 215, 45928, 10362231, 2450260001, 600869373182),
    }
    checks = 0
    for dilation, values in expected.items():
        for n, value in enumerate(values):
            assert signed_dilation_value(n, dilation, 1) == value, (
                dilation,
                n,
            )
            checks += 1
    assert checks == 15
    return checks


def check_coster_a375178_baseline() -> tuple[int, int]:
    """Check Coster's p^(3r) tower for all exponents q >= 2."""
    checks = 0
    minimum_slack = 10**9
    for exponent in range(2, 9):
        for prime in (5, 7, 11, 13):
            for level in (1, 2):
                for n in range(1, 9):
                    upper = n * prime**level
                    if upper > 300:
                        continue
                    lower = n * prime ** (level - 1)
                    difference = (
                        bala_power(upper, exponent)
                        - bala_power(lower, exponent)
                    )
                    slack = valuation(difference, prime) - 3 * level
                    assert slack >= 0, (
                        exponent,
                        prime,
                        level,
                        n,
                        slack,
                    )
                    minimum_slack = min(minimum_slack, slack)
                    checks += 1
    assert checks == 343
    assert minimum_slack == 0
    return checks, minimum_slack


def check_a333593_coster_reduction() -> tuple[int, int]:
    """Check the exact decomposition and both published tower components."""
    identity_checks = 0
    for n in range(1, 201):
        expected = (
            (-1) ** n * coster_signed_apery(n - 1)
            + a333593_central_tail(n)
        )
        assert a333593(n) == expected, n
        identity_checks += 1

    tower_checks = 0
    minimum_slack = 10**9
    for prime in TOWER_PRIMES:
        for level in range(1, 4):
            for n in range(1, 16):
                if n * prime**level > 500:
                    continue
                upper = n * prime**level
                lower = n * prime ** (level - 1)
                target = 3 * level

                apery_difference = (
                    coster_signed_apery(upper - 1)
                    - coster_signed_apery(lower - 1)
                )
                central_difference = (
                    a333593_central_tail(upper)
                    - a333593_central_tail(lower)
                )
                final_difference = a333593(upper) - a333593(lower)

                assert valuation(apery_difference, prime) >= target, (
                    "Coster component",
                    prime,
                    level,
                    n,
                )
                assert valuation(central_difference, prime) >= target, (
                    "central component",
                    prime,
                    level,
                    n,
                )
                slack = valuation(final_difference, prime) - target
                assert slack >= 0, (prime, level, n, slack)
                minimum_slack = min(minimum_slack, slack)
                tower_checks += 1
    assert identity_checks == 200
    assert tower_checks == 128
    assert minimum_slack == 0
    assertion_checks = identity_checks + 3 * tower_checks
    assert assertion_checks == 584
    return assertion_checks, minimum_slack


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
    even_checks, even_slack = check_even_power_prime_level_theorem()
    signed_checks, signed_slack = check_signed_dilation_prime_level_theorem()
    signed_identity_checks = check_signed_dilation_named_sequences()
    baseline_checks, baseline_slack = check_coster_a375178_baseline()
    a333_checks, a333_slack = check_a333593_coster_reduction()
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
        "proved even-power prime cases and named boundaries: "
        f"{even_checks} (minimum slack {even_slack})"
    )
    print(
        "proved signed arbitrary-dilation prime cases: "
        f"{signed_checks} (minimum slack {signed_slack}); "
        f"named identities {signed_identity_checks}"
    )
    print(
        "published Coster baseline cases: "
        f"{baseline_checks} (minimum slack {baseline_slack})"
    )
    print(
        "proved A333593 Coster-reduction checks: "
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
        f"{boundary_checks + prime_checks + even_checks + signed_checks + signed_identity_checks + baseline_checks + a333_checks + a365_checks + odd_checks} "
        "Bala-queue checks passed"
    )


if __name__ == "__main__":
    main()
