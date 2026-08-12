"""Exact checks for A245926AlgebraicCoefficientTower.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


PUBLISHED = (
    1,
    5,
    51,
    587,
    7123,
    89055,
    1135005,
    14660805,
    191253843,
    2513963567,
    33244446601,
    441772827105,
    5894323986301,
    78912561223553,
    1059543126891027,
    14261959492731387,
    192392702881384275,
    2600355510685245087,
    35206018016510388345,
    477377227987055971905,
)


def recurrence_values(limit: int) -> list[int]:
    """A245926 from the exact algebraic-series recurrence on its OEIS page."""
    values = [1]
    if limit == 0:
        return values
    values.append(5)
    for n in range(2, limit + 1):
        numerator = (
            (4 * n - 3) * (28 * n * n - 42 * n + 9) * values[-1]
            - (n - 1) * (2 * n - 3) * (4 * n - 1) * values[-2]
        )
        denominator = n * (2 * n - 1) * (4 * n - 5)
        assert numerator % denominator == 0
        values.append(numerator // denominator)
    return values


def coefficient_value(n: int) -> int:
    """[x^n] (1-x^3)^n (1-x^2)^(2n) (1-x)^(-5n)."""
    if n == 0:
        return 1
    answer = 0
    for a in range(n // 3 + 1):
        for b in range((n - 3 * a) // 2 + 1):
            degree = n - 3 * a - 2 * b
            answer += (
                (-1) ** (a + b)
                * comb(n, a)
                * comb(2 * n, b)
                * comb(5 * n + degree - 1, degree)
            )
    return answer


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        value //= prime
        answer += 1
    return answer


def factorial_vp(n: int, prime: int) -> int:
    answer = 0
    while n:
        n //= prime
        answer += n
    return answer


def check_published_and_coefficient_identity() -> int:
    values = recurrence_values(60)
    assert tuple(values[: len(PUBLISHED)]) == PUBLISHED
    checks = len(PUBLISHED)
    for n in range(61):
        assert coefficient_value(n) == values[n]
        checks += 1
    return checks


def check_kernel_factorizations() -> int:
    # (1+x+x^2)(1+x)^2/(1-x)^2
    # = (1-x^3)(1-x^2)^2/(1-x)^5.
    for x in range(-30, 31):
        if x == 1:
            continue
        left = Fraction((1 + x + x * x) * (1 + x) ** 2, (1 - x) ** 2)
        right = Fraction((1 - x**3) * (1 - x**2) ** 2, (1 - x) ** 5)
        assert left == right
    return 60


def check_reversion_identities() -> int:
    checks = 0
    # The rational identities in (9), (13), and (14), evaluated away from
    # their poles.  Since the proof displays their symbolic derivations,
    # these exact evaluations guard transcription independently.
    for v in range(1, 80):
        if v == 1:
            continue
        z = Fraction(v - 1, v * (3 * v + 1))
        discriminant = 1 - 14 * z + z * z
        signed_root = -Fraction(3 * v * v - 6 * v - 1, v * (3 * v + 1))
        assert signed_root * signed_root == discriminant
        b_squared = Fraction(v * (3 * v + 1) ** 2, (1 + 6 * v - 3 * v * v) ** 2)
        target = Fraction(1 - z + signed_root, 2 * discriminant)
        assert b_squared == target
        assert 3 * z * v * v + (z - 1) * v + 1 == 0
        checks += 3
    return checks


def check_support_and_budget() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23):
        for d in (1, 2, 3):
            for j in range(1, 5 * prime + 1):
                if j % prime:
                    assert (d * j) % prime
                    checks += 1
        for r in range(1, 6):
            for h in range(2, 150):
                assert h * r - factorial_vp(h, prime) >= 2 * r
                checks += 1
    return checks


def check_towers() -> int:
    values = recurrence_values(3 * 13**2)
    checks = 0
    for prime in (5, 7, 11, 13):
        for n in (1, 2, 3):
            for r in (1, 2):
                high = n * prime**r
                low = n * prime ** (r - 1)
                assert (values[high] - values[low]) % prime ** (2 * r) == 0
                checks += 1

    # Smaller level-three tests keep the exact recurrence inexpensive.
    values = recurrence_values(2 * 7**3)
    for prime in (5, 7):
        for n in (1, 2):
            high = n * prime**3
            low = n * prime**2
            assert (values[high] - values[low]) % prime**6 == 0
            checks += 1
    return checks


def check_small_prime_boundary() -> int:
    values = recurrence_values(3)
    assert values[2] - values[1] == 46
    assert vp(values[2] - values[1], 2) == 1
    assert values[3] - values[1] == 582
    assert vp(values[3] - values[1], 3) == 1
    return 2


def main() -> None:
    identity = check_published_and_coefficient_identity()
    factorization = check_kernel_factorizations()
    reversion = check_reversion_identities()
    lemmas = check_support_and_budget()
    towers = check_towers()
    boundary = check_small_prime_boundary()
    total = identity + factorization + reversion + lemmas + towers + boundary
    print(f"published/coefficient identity checks: {identity}")
    print(f"kernel factorization checks: {factorization}")
    print(f"reversion rational-identity checks: {reversion}")
    print(f"support/factorial-budget checks: {lemmas}")
    print(f"adjacent tower checks: {towers}")
    print(f"small-prime boundary checks: {boundary}")
    print(f"all {total} A245926 checks passed")


if __name__ == "__main__":
    main()
