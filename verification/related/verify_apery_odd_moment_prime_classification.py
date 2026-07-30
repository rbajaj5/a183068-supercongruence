"""Exact checks for AperyOddMomentPrimeClassification.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def moment(q: int, n: int) -> int:
    return sum(
        k**q * comb(n, k) ** 2 * comb(n + k, k) ** 2
        for k in range(n + 1)
    )


def moment_mod(q: int, n: int, modulus: int) -> int:
    return sum(
        pow(k, q, modulus)
        * pow(comb(n, k), 2, modulus)
        * pow(comb(n + k, k), 2, modulus)
        for k in range(n + 1)
    ) % modulus


def check_exact_product() -> int:
    checks = 0
    for prime in PRIMES:
        for k in range(1, prime):
            left = comb(prime - 1, k) * comb(prime - 1 + k, k)
            right = Fraction((-1) ** k * prime, k)
            right *= 1 - Fraction(prime, k)
            for j in range(1, k):
                right *= 1 - Fraction(prime * prime, j * j)
            assert right.denominator == 1
            assert left == right.numerator
            checks += 1
    return checks


def check_local_expansion() -> int:
    checks = 0
    for prime in PRIMES:
        modulus = prime**4
        for q in (1, 5, 7, 9, 11, 13, 15, 17, 19, 21):
            for k in range(1, prime):
                left = (
                    pow(k, q, modulus)
                    * pow(comb(prime - 1, k), 2, modulus)
                    * pow(comb(prime - 1 + k, k), 2, modulus)
                ) % modulus
                right = (
                    prime**2 * pow(k, q - 2, modulus)
                    - 2 * prime**3 * pow(k, q - 3, modulus)
                ) % modulus
                assert left == right
                checks += 1
    return checks


def power_sum(exponent: int, prime: int, modulus: int) -> int:
    return sum(pow(k, exponent, modulus) for k in range(1, prime)) % modulus


def check_master_congruence() -> int:
    checks = 0
    for prime in PRIMES:
        modulus = prime**4
        for q in (1, 5, 7, 9, 11, 13, 15, 17, 19, 21):
            left = moment_mod(q, prime - 1, modulus)
            right = (
                prime**2 * power_sum(q - 2, prime, modulus)
                - 2 * prime**3 * power_sum(q - 3, prime, modulus)
            ) % modulus
            assert left == right
            checks += 1
    return checks


def check_a357510() -> int:
    checks = 0
    for prime in PRIMES[1:]:
        assert moment_mod(1, prime - 1, prime**4) == 0
        checks += 1
    assert valuation(moment(1, 2), 3) == 3
    return checks + 1


def exceptional(m: int, prime: int) -> bool:
    return (2 * m - 2) % (prime - 1) == 0 and (2 * m - 5) % prime != 0


def check_odd_moment_residue() -> int:
    checks = 0
    for m in range(2, 31):
        q = 2 * m + 1
        for prime in PRIMES:
            modulus = prime**4
            value = moment_mod(q, prime - 1, modulus)
            assert value % prime**3 == 0
            actual = (value // prime**3) % prime
            delta = int((2 * m - 2) % (prime - 1) == 0)
            expected = (
                delta * (5 - 2 * m) * pow(2, -1, prime)
            ) % prime
            assert actual == expected
            assert (actual != 0) == exceptional(m, prime)
            checks += 1
    return checks


def check_exception_table() -> int:
    expected = {
        2: {3},
        3: {3, 5},
        4: {7},
        5: {3},
        6: {3, 11},
        7: {5, 7, 13},
        8: {3},
        9: {3, 5, 17},
        10: {7, 19},
    }
    checks = 0
    for m, target in expected.items():
        bound = 2 * m - 1
        candidates = {
            p for p in PRIMES if p <= bound and exceptional(m, p)
        }
        assert candidates == target
        checks += 1
    return checks


def check_named_boundary() -> int:
    checks = 0
    for prime in PRIMES[1:]:
        assert moment_mod(5, prime - 1, prime**4) == 0
        checks += 1
    assert moment_mod(19, 4, 5**4) == 5**3
    checks += 1
    return checks


def main() -> None:
    counts = {
        "exact product": check_exact_product(),
        "local expansion": check_local_expansion(),
        "master congruence": check_master_congruence(),
        "A357510 theorem": check_a357510(),
        "odd-moment residue": check_odd_moment_residue(),
        "exception table": check_exception_table(),
        "named boundary": check_named_boundary(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(
        "all "
        f"{sum(counts.values())} "
        "Apéry odd-moment prime-classification checks passed"
    )


if __name__ == "__main__":
    main()
