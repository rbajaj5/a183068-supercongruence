"""Checks for the all-level A365029 digit reduction."""

from fractions import Fraction
from math import comb


def generalized_binomial(n: int, k: int) -> int:
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


def first_binomial(n: int, ell: int, q: int, u: int) -> int:
    k = q * ell + u
    return generalized_binomial(n * q + k - 1, k)


def second_binomial(n: int, ell: int, q: int, u: int) -> int:
    k = q * ell + u
    return generalized_binomial(2 * k - 1, n * q)


def unit_product(n: int, k: int, q: int, prime: int) -> Fraction:
    out = Fraction(1)
    for j in range(1, k):
        if j % prime:
            out *= 1 + Fraction(n * q, j)
    return out


def fraction_mod(value: Fraction, modulus: int) -> int:
    return value.numerator * pow(value.denominator % modulus, -1, modulus) % modulus


def normalized_term(n: int, ell: int, q: int, u: int) -> int:
    first = first_binomial(n, ell, q, u)
    assert first % q == 0
    return (first // q) ** 2 * second_binomial(n, ell, q, u)


def reduced_term(n: int, ell: int, prime: int, level: int, u: int) -> int:
    q = prime**level
    k = q * ell + u
    b = (k - 1) // prime
    d = (2 * k - 1) // prime
    return (
        n**2
        * pow(u, -2, q)
        * comb(n * prime ** (level - 1) + b, b) ** 2
        * generalized_binomial(d, n * prime ** (level - 1))
    ) % q


def check_exact_factorization() -> int:
    checks = 0
    for prime, max_level in ((5, 3), (7, 3), (11, 2)):
        for level in range(1, max_level + 1):
            q = prime**level
            for n in range(1, 4):
                for ell in range(n):
                    for u in range(1, q):
                        if u % prime == 0:
                            continue
                        k = q * ell + u
                        b = (k - 1) // prime
                        exact = (
                            Fraction(n, k)
                            * comb(n * prime ** (level - 1) + b, b)
                            * unit_product(n, k, q, prime)
                        )
                        assert Fraction(first_binomial(n, ell, q, u), q) == exact
                        assert fraction_mod(unit_product(n, k, q, prime) - 1, q) == 0
                        checks += 2
    return checks


def check_recursive_congruences() -> int:
    checks = 0
    for prime, max_level in ((5, 4), (7, 3), (11, 2)):
        for level in range(1, max_level + 1):
            q = prime**level
            for n in range(1, 6):
                for ell in range(n):
                    direct = 0
                    reduced = 0
                    lower = 0
                    upper = 0
                    residue_sums = [0] * prime
                    for u in range(1, q):
                        if u % prime == 0:
                            continue
                        k = q * ell + u
                        d = (2 * k - 1) // prime
                        assert (
                            second_binomial(n, ell, q, u)
                            - generalized_binomial(d, n * prime ** (level - 1))
                        ) % q == 0
                        actual = normalized_term(n, ell, q, u) % q
                        predicted = reduced_term(n, ell, prime, level, u)
                        assert actual == predicted
                        direct = (direct + actual) % q
                        reduced = (reduced + predicted) % q
                        residue_sums[u % prime] = (
                            residue_sums[u % prime] + actual
                        ) % q
                        if 2 * u < q:
                            lower = (lower + actual) % q
                        else:
                            upper = (upper + actual) % q
                        checks += 2
                    assert direct == reduced == lower == upper == 0
                    # Complete last-digit cancellation is essential in a
                    # nontrivial block: some fixed residue remains a unit.
                    if n == 1 and ell == 0 and level >= 2:
                        assert any(value % prime for value in residue_sums[1:])
                    checks += 5
    return checks


def main() -> None:
    exact = check_exact_factorization()
    recursive = check_recursive_congruences()
    print(f"exact factorization and unit-product checks: {exact}")
    print(f"recursive, half-block, and digit-boundary checks: {recursive}")
    print(f"all {exact + recursive} checks passed")


if __name__ == "__main__":
    main()
