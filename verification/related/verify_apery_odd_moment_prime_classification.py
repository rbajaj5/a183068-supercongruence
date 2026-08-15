"""Exact checks for AperyOddMomentPrimeClassification.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd


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


def rational_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def reduced_kernel(n: int, k: int) -> int:
    return comb(n - 2, k - 1) * comb(n + k - 1, k - 1)


def reduced_sum(n: int) -> int:
    return sum(k * reduced_kernel(n, k) ** 2 for k in range(1, n))


def certificate_polynomial(n: int, k: int) -> int:
    return (
        6 * k**4
        - 4 * k**3 * n
        + 16 * k**3
        - 3 * k**2 * n**2
        - 6 * k**2 * n
        + 15 * k**2
        + 2 * k * n**3
        - 7 * k * n**2
        + 5 * k
        + 4 * n**3
        - 8 * n**2
        + 4 * n
    )


def certificate_multiplier(n: int, k: int) -> Fraction:
    return (
        Fraction(3 * (k - 1) ** 2, k)
        - 2 * n
        + Fraction(2 * n, k**2)
    )


def certificate_summand(n: int, k: int) -> Fraction:
    kernel = reduced_kernel(n, k)
    return Fraction(
        kernel**2 * certificate_polynomial(n, k),
        k**3 * (k + 1),
    )


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


def check_composite_factorization() -> int:
    checks = 0
    for n in range(2, 61):
        left = moment(5, n - 1)
        right = n**2 * (n - 1) ** 2 * reduced_sum(n)
        assert left == right
        checks += 1
        for k in range(1, n):
            kernel = reduced_kernel(n, k)
            assert kernel % k == 0
            assert (
                n * (n - 1) * kernel
                == k**2 * comb(n - 1, k) * comb(n + k - 1, k)
            )
            assert (
                n
                * (n - 1)
                * comb(n + k - 1, k - 1)
                == k * (k + 1) * comb(n + k - 1, k + 1)
            )
            checks += 3
            for divisor in range(2, n + k + 1):
                defect = (
                    (n - 2) // divisor
                    + (n + k - 1) // divisor
                    - k // divisor
                    - (k - 1) // divisor
                    - (n - k - 1) // divisor
                    - n // divisor
                )
                assert defect >= 0
                checks += 1
    return checks


def check_telescoping_certificate() -> int:
    checks = 0
    for n in range(2, 71):
        terms = [Fraction(0)] + [
            Fraction(k * reduced_kernel(n, k) ** 2)
            for k in range(1, n)
        ] + [Fraction(0)]
        total = Fraction(0)
        for k in range(1, n):
            left = 12 * terms[k] - (
                certificate_multiplier(n, k + 1) * terms[k + 1]
                - certificate_multiplier(n, k) * terms[k]
            )
            right = n**2 * certificate_summand(n, k)
            assert left == right
            total += certificate_summand(n, k)
            checks += 1
        assert 12 * reduced_sum(n) == n**2 * total
        checks += 1
    return checks


def check_local_integrality() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for n in range(prime, 141, prime):
            a = valuation(n, prime)
            for k in range(1, n):
                kernel_depth = valuation(reduced_kernel(n, k), prime)
                q = valuation(k, prime)
                s = valuation(k + 1, prime)
                assert kernel_depth >= q
                assert kernel_depth >= 2 * q - a
                assert kernel_depth >= s - a
                assert rational_valuation(certificate_summand(n, k), prime) >= 0
                checks += 4
            assert valuation(reduced_sum(n), prime) >= 2 * a
            checks += 1
    return checks


def check_full_composite_theorem() -> int:
    checks = 0
    for n in range(1, 301):
        if gcd(n, 6) != 1:
            continue
        assert moment_mod(5, n - 1, n**4) == 0
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
        "composite factorization": check_composite_factorization(),
        "telescoping certificate": check_telescoping_certificate(),
        "local certificate integrality": check_local_integrality(),
        "full composite theorem": check_full_composite_theorem(),
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
