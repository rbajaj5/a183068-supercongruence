"""Exact checks for the candidate p=3 cubic theorem for sequence (eta)."""

from __future__ import annotations

import math


def binom(n: int, k: int) -> int:
    """Polynomially extended binomial coefficient for integer n and k >= 0."""
    if k < 0:
        return 0
    if n >= 0:
        return math.comb(n, k) if k <= n else 0
    return (-1) ** k * math.comb(k - n - 1, k)


def eta_term(n: int, k: int) -> int:
    bracket = binom(4 * n - 5 * k - 1, 3 * n) + binom(
        4 * n - 5 * k, 3 * n
    )
    return (-1) ** k * binom(n, k) ** 3 * bracket


def eta_formula(n: int) -> int:
    return sum(eta_term(n, k) for k in range(n + 1))


def eta_recurrence(limit: int) -> list[int]:
    """The customary normalization, one half of eta_formula."""
    values = [1]
    previous = 0
    current = 1
    for n in range(limit):
        numerator = (
            (2 * n + 1) * (11 * n * n + 11 * n + 5) * current
            - 125 * n**3 * previous
        )
        denominator = (n + 1) ** 3
        assert numerator % denominator == 0
        following = numerator // denominator
        values.append(following)
        previous, current = current, following
    return values


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def check_formula() -> int:
    recurrence = eta_recurrence(100)
    for n, value in enumerate(recurrence):
        assert eta_formula(n) == 2 * value
    return len(recurrence)


def check_termwise() -> tuple[int, int]:
    discarded = 0
    scaled = 0
    for r in range(1, 5):
        power = 3**r
        for m in range(1, 31):
            n = m * power
            if n > 900:
                continue
            modulus = 3 ** (3 * r)
            for k in range(n + 1):
                if k % 3:
                    assert eta_term(n, k) % modulus == 0
                    discarded += 1
                else:
                    difference = eta_term(n, k) - eta_term(n // 3, k // 3)
                    assert difference % modulus == 0
                    scaled += 1
    return discarded, scaled


def check_aggregate(limit: int = 10_000) -> tuple[int, int]:
    values = eta_recurrence(limit)
    checks = 0
    minimum_slack = 10**9
    power = 3
    r = 1
    while power <= limit:
        for m in range(1, limit // power + 1):
            difference = values[m * power] - values[m * power // 3]
            slack = valuation(difference, 3) - 3 * r
            assert slack >= 0
            minimum_slack = min(minimum_slack, slack)
            checks += 1
        r += 1
        power *= 3
    return checks, minimum_slack


def main() -> None:
    formula_checks = check_formula()
    discarded, scaled = check_termwise()
    aggregate, slack = check_aggregate()
    print(f"formula/recurrence identities: {formula_checks}")
    print(f"discarded term checks:         {discarded}")
    print(f"scaled term checks:            {scaled}")
    print(f"aggregate congruences:         {aggregate}")
    print(f"minimum aggregate slack:       {slack}")
    print("all eta p=3 checks passed")


if __name__ == "__main__":
    main()
