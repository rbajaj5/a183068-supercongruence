"""Exact checks for three Catalan ballot-power supercongruences.

This script supplies computational evidence only.  It checks the quotient's
integrality before testing each congruence.
"""

from math import comb


ODD_EXPONENTS = (3, 5, 7)
OFFICIAL_PRIMES = (5, 7, 11, 13, 17, 19)
ARGUMENT_CAP = 1000
BASE_N_CAP = 50


def valuation(value: int, prime: int) -> int:
    """Return the prime-adic valuation of a nonzero integer."""
    if value == 0:
        raise ValueError("the tested adjacent difference unexpectedly vanished")
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def ballot_power_quotient(n: int, exponent: int) -> int:
    """Return B_exponent(n), asserting that the displayed quotient is integral."""
    denominator = comb(2 * n - 1, n - 1)
    previous = 0
    numerator = 0
    for k in range(n):
        current = comb(2 * n - 1, k)
        numerator += (current - previous) ** exponent
        previous = current
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0, (n, exponent, remainder)
    return quotient


def cached_family(exponent: int):
    cache: dict[int, int] = {}

    def value(n: int) -> int:
        if n not in cache:
            cache[n] = ballot_power_quotient(n, exponent)
        return cache[n]

    return value


def check_official_conjecture(exponent: int) -> tuple[int, int]:
    """Check the OEIS p^(3r) conjecture and return cases and minimum slack."""
    family = cached_family(exponent)
    cases = 0
    minimum_slack: int | None = None
    for prime in OFFICIAL_PRIMES:
        for level in range(1, 4):
            for n in range(1, BASE_N_CAP + 1):
                if n * prime**level > ARGUMENT_CAP:
                    continue
                difference = family(n * prime**level) - family(
                    n * prime ** (level - 1)
                )
                slack = valuation(difference, prime) - 3 * level
                assert slack >= 0, (exponent, prime, level, n, slack)
                minimum_slack = (
                    slack if minimum_slack is None else min(minimum_slack, slack)
                )
                cases += 1
    assert cases == 388
    assert minimum_slack == 0
    return cases, minimum_slack


def check_small_prime_refinement(exponent: int) -> tuple[int, int]:
    """Check the proposed sharp losses at 2 and 3."""
    family = cached_family(exponent)
    cases = 0
    minimum_slack: int | None = None
    for prime in (2, 3):
        for level in range(1, 5):
            target = 1 if (prime, level) == (2, 1) else 3 * level - 1
            for n in range(1, BASE_N_CAP + 1):
                if n * prime**level > ARGUMENT_CAP:
                    continue
                difference = family(n * prime**level) - family(
                    n * prime ** (level - 1)
                )
                slack = valuation(difference, prime) - target
                assert slack >= 0, (exponent, prime, level, n, slack)
                minimum_slack = (
                    slack if minimum_slack is None else min(minimum_slack, slack)
                )
                cases += 1
    assert cases == 349
    assert minimum_slack == 0
    return cases, minimum_slack


def main() -> None:
    official_total = 0
    small_prime_total = 0
    for exponent in ODD_EXPONENTS:
        official_cases, official_slack = check_official_conjecture(exponent)
        small_cases, small_slack = check_small_prime_refinement(exponent)
        official_total += official_cases
        small_prime_total += small_cases
        print(
            f"m={exponent}: official {official_cases} cases "
            f"(minimum slack {official_slack}); "
            f"small-prime {small_cases} cases "
            f"(minimum slack {small_slack})"
        )
    print(
        f"all {official_total} official and {small_prime_total} "
        "small-prime refinement checks passed"
    )


if __name__ == "__main__":
    main()
