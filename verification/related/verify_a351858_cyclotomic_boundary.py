"""Exact checks for A351858CyclotomicFamilyBoundary.md."""

from __future__ import annotations

from functools import lru_cache
from math import comb


PUBLISHED = (
    1,
    1,
    7,
    19,
    103,
    376,
    1825,
    7547,
    35175,
    153838,
    708132,
    3181091,
    14616481,
    66582283,
    306501377,
    1407473269,
    6497464679,
    29991098982,
    138844558150,
    643215119214,
    2985368996228,
    13868212710623,
    64508509024241,
    300324344452479,
    1399598738196897,
    6527698842078501,
)


def generalized_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(bottom - top - 1, bottom)


@lru_cache(maxsize=None)
def family(k: int, n: int) -> int:
    """[x^n] ((1-x^(k+1))^(k+1)/((1-x)(1-x^k)^k))^n."""
    answer = 0
    for first in range(n // (k + 1) + 1):
        first_coefficient = (-1) ** first * generalized_binomial(
            (k + 1) * n, first
        )
        remaining = n - (k + 1) * first
        for second in range(remaining // k + 1):
            last = remaining - k * second
            answer += (
                first_coefficient
                * (-1) ** second
                * generalized_binomial(-k * n, second)
                * generalized_binomial(-n, last)
                * (-1) ** last
            )
    return answer


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    answer = 0
    while value % prime == 0:
        answer += 1
        value //= prime
    return answer


def primes_through(limit: int) -> list[int]:
    answer = []
    for candidate in range(2, limit + 1):
        if all(candidate % divisor for divisor in range(2, int(candidate**0.5) + 1)):
            answer.append(candidate)
    return answer


def periodic_c(index: int) -> int:
    return 1 + 4 * (index % 2 == 0) - 9 * (index % 3 == 0)


def quadratic_coefficient_mod(total: int, prime: int, modulus: int) -> int:
    answer = 0
    for left in range(1, total):
        right = total - left
        if left % prime == 0:
            continue
        answer += (
            periodic_c(left)
            * periodic_c(right)
            * pow(left, -1, modulus)
            * pow(right, -1, modulus)
        )
    return answer % modulus


def inverse_square_prefix(bound: int, prime: int, modulus: int) -> int:
    return sum(
        pow(value, -2, modulus)
        for value in range(1, bound + 1)
        if value % prime
    ) % modulus


def residue_class_sums(prime: int, exponent: int) -> list[int]:
    modulus = prime**exponent
    return [
        sum(
            pow(value, -2, modulus)
            for value in range(1, modulus)
            if value % prime and value % 6 == residue
        )
        % modulus
        for residue in range(6)
    ]


def check_published_values() -> int:
    assert tuple(family(2, n) for n in range(len(PUBLISHED))) == PUBLISHED
    return len(PUBLISHED)


def check_factorization() -> int:
    checks = 0
    for k in range(1, 16):
        # Verify (sum_0^k x^j)^(k+1)/(sum_0^(k-1) x^j)^k after
        # cross multiplication with its cyclotomic expression.
        left = [1] * (k + 1)
        right = [1] * k

        def multiply(a: list[int], b: list[int]) -> list[int]:
            out = [0] * (len(a) + len(b) - 1)
            for i, x in enumerate(a):
                for j, y in enumerate(b):
                    out[i + j] += x * y
            return out

        def power(base: list[int], exponent: int) -> list[int]:
            out = [1]
            for _ in range(exponent):
                out = multiply(out, base)
            return out

        one_minus_xk = [0] * (k + 1)
        one_minus_xk[0] = 1
        one_minus_xk[k] = -1
        lhs = multiply(
            power(left, k + 1),
            multiply([1, -1], power(one_minus_xk, k)),
        )
        # (1-x^(k+1))^(k+1) * (sum_0^(k-1) x^j)^k
        cyclotomic = [0] * (k + 2)
        cyclotomic[0] = 1
        cyclotomic[k + 1] = -1
        rhs_cross = multiply(power(cyclotomic, k + 1), power(right, k))
        # Compare the original numerator times (1-x) with the cyclotomic
        # numerator times the original denominator.
        assert lhs == rhs_cross
        checks += 1
    return checks


def check_counterexample_families() -> int:
    checks = 0
    for prime in (p for p in primes_through(97) if p >= 5):
        first = family(prime - 1, prime)
        first_formula = comb(2 * prime - 1, prime) + prime**2 * (prime - 2)
        assert first == first_formula
        assert family(prime - 1, 1) == 1
        assert vp(first - 1, prime) == 2
        checks += 3

        second = family(prime, prime)
        second_formula = comb(2 * prime - 1, prime) + prime**2
        assert second == second_formula
        assert family(prime, 1) == 1
        assert vp(second - 1, prime) == 2
        checks += 3
    return checks


def check_small_witnesses() -> int:
    assert family(4, 5) == 201
    assert family(4, 5) - family(4, 1) == 200
    assert family(5, 5) == 151
    assert family(5, 5) - family(5, 1) == 150
    return 4


def check_sixth_interval_lemma() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19):
        for exponent in (1, 2, 3):
            modulus = prime**exponent
            one_third = inverse_square_prefix(modulus // 3, prime, modulus)
            one_sixth = inverse_square_prefix(modulus // 6, prime, modulus)
            assert (5 * one_third - one_sixth) % modulus == 0
            checks += 1

            classes = residue_class_sums(prime, exponent)
            if modulus % 6 == 1:
                a, b, d = classes[0], classes[2], classes[3]
                assert classes == [a, a, b, d, d, b]
            else:
                a, b, d = classes[0], classes[1], classes[2]
                assert classes == [a, b, d, d, b, a]
            assert (a + 5 * d) % modulus == 0
            assert (b - 4 * d) % modulus == 0
            checks += 3
    return checks


def check_autocorrelation_table() -> int:
    expected_positive = (
        (0, 0, 0, 0, 0, 0),
        (-4, -4, 5, -40, -40, 5),
        (-19, -19, -28, 17, 17, -28),
        (42, 42, 42, 42, 42, 42),
        (-11, -11, -2, -47, -47, -2),
        (-74, -74, -83, -38, -38, -83),
    )
    checks = 0
    patterns = {
        1: (-5, -5, 4, 1, 1, 4),
        -1: (-5, 4, 1, 1, 4, -5),
    }
    for epsilon in (1, -1):
        for remainder in range(6):
            row = tuple(
                sum(
                    periodic_c(residue + epsilon * offset)
                    * periodic_c(
                        epsilon * remainder
                        - residue
                        - epsilon * offset
                    )
                    for offset in range(remainder)
                )
                for residue in range(6)
            )
            if epsilon == 1:
                assert row == expected_positive[remainder]
            else:
                assert row == tuple(
                    expected_positive[remainder][(-residue) % 6]
                    for residue in range(6)
                )
            assert sum(x * y for x, y in zip(row, patterns[epsilon])) == 0
            checks += 2
    return checks


def check_quadratic_cartier() -> int:
    checks = 0
    sharp = 0
    for prime in (5, 7, 11, 13):
        for exponent in (1, 2, 3):
            required = prime**exponent
            modulus = prime ** (exponent + 1)
            for multiplier in range(1, 31):
                total = required * multiplier
                coefficient = quadratic_coefficient_mod(total, prime, modulus)
                assert coefficient % required == 0
                sharp += coefficient % modulus != 0
                checks += 1
    assert sharp > 0
    return checks


def check_named_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for prime in (5, 7, 11, 13):
        for level in (1, 2):
            for n in range(1, 9):
                if n * prime**level > 220:
                    continue
                high = family(2, n * prime**level)
                low = family(2, n * prime ** (level - 1))
                actual = vp(high - low, prime)
                assert actual >= 3 * level
                sharp += actual == 3 * level
                checks += 1
    assert sharp > 0
    return checks, sharp


def main() -> None:
    published = check_published_values()
    factorization = check_factorization()
    counterexamples = check_counterexample_families()
    small = check_small_witnesses()
    intervals = check_sixth_interval_lemma()
    autocorrelation = check_autocorrelation_table()
    cartier = check_quadratic_cartier()
    towers, sharp = check_named_towers()
    total = (
        published
        + factorization
        + counterexamples
        + small
        + intervals
        + autocorrelation
        + cartier
        + towers
    )
    print(f"published A351858 value checks: {published}")
    print(f"cyclotomic factorization checks: {factorization}")
    print(f"infinite-family coefficient/valuation checks: {counterexamples}")
    print(f"small explicit witness checks: {small}")
    print(f"sixth-interval and residue-class checks: {intervals}")
    print(f"autocorrelation-table checks: {autocorrelation}")
    print(f"quadratic Cartier checks: {cartier}")
    print(f"named cubic-tower checks: {towers} ({sharp} sharp)")
    print(f"all {total} A351858 boundary checks passed")


if __name__ == "__main__":
    main()
