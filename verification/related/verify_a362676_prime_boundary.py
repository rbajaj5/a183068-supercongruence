"""Exact checks for the A362676 prime-boundary proof.

The script audits the finite identities and congruences used in the proof.
It is not a replacement for the proof in the companion note.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd


def harmonic(n: int, power: int = 1) -> Fraction:
    return sum((Fraction(1, k**power) for k in range(1, n + 1)), Fraction())


def odd_harmonic(n: int) -> Fraction:
    return sum((Fraction(1, 2 * k - 1) for k in range(1, n + 1)), Fraction())


def mod_fraction(value: Fraction, modulus: int) -> int:
    assert gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def central_weight(k: int) -> Fraction:
    return Fraction(comb(2 * k, k), 4**k)


def a362676(n: int) -> int:
    return sum(
        4 ** (n - k) * comb(n, k) * comb(n - 1, k) * comb(2 * k, k)
        for k in range(n + 1)
    )


def check_exact_identities(limit: int = 40) -> int:
    checks = 0
    for n in range(1, limit + 1):
        h = harmonic(n)
        h2 = harmonic(n, 2)

        alternating = sum(
            (Fraction((-1) ** k * comb(n, k), k) for k in range(1, n + 1)),
            Fraction(),
        )
        assert alternating == -h
        checks += 1

        odd_block = sum(
            (
                Fraction((-1) ** k * comb(n, k), k) * odd_harmonic(k)
                for k in range(1, n + 1)
            ),
            Fraction(),
        )
        reciprocal_block = Fraction(1, 2) * sum(
            (Fraction(4**k, k * k * comb(2 * k, k)) for k in range(1, n + 1)),
            Fraction(),
        )
        assert odd_block == -reciprocal_block
        checks += 1

        square_block = sum(
            (Fraction((-1) ** k * comb(n, k), k * k) for k in range(1, n + 1)),
            Fraction(),
        )
        assert square_block == -(h * h + h2) / 2
        checks += 1

        mixed_block = sum(
            (
                Fraction((-1) ** k * comb(n, k), k) * harmonic(k - 1)
                for k in range(1, n + 1)
            ),
            Fraction(),
        )
        assert mixed_block == (h * h - h2) / 2
        checks += 1
    return checks


def check_prime_congruences(limit: int = 200) -> tuple[int, int]:
    checks = 0
    sharp = 0
    for p in range(5, limit):
        if not is_prime(p):
            continue
        h = (p - 1) // 2
        q = (2 ** (p - 1) - 1) // p
        hp = harmonic(h)

        assert mod_fraction(hp + 2 * q - p * q * q, p * p) == 0
        checks += 1

        s1 = sum(
            (central_weight(k) / k for k in range(1, p)), Fraction()
        )
        assert mod_fraction(s1 + hp, p * p) == 0
        assert mod_fraction(s1 - (2 * q - p * q * q), p * p) == 0
        checks += 2

        s2 = sum(
            (
                central_weight(k)
                / k
                * (2 * harmonic(k - 1) + Fraction(1, k))
                for k in range(1, p)
            ),
            Fraction(),
        )
        assert mod_fraction(s2 - hp * hp / 2, p) == 0
        assert mod_fraction(s2 - 2 * q * q, p) == 0
        checks += 2

        delta = a362676(p) - 4
        assert delta % (p**3) == 0
        if delta % (p**4) != 0:
            sharp += 1
        checks += 1
    return checks, sharp


def main() -> None:
    identity_checks = check_exact_identities()
    prime_checks, sharp = check_prime_congruences()
    print("A362676 prime-boundary verification passed")
    print(f"exact rational identity checks: {identity_checks}")
    print(f"exact prime congruence checks: {prime_checks}")
    print(f"sharp modulo-p^3 instances: {sharp}")


if __name__ == "__main__":
    main()
