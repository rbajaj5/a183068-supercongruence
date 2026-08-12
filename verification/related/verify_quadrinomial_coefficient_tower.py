"""Exact checks for the two supercongruences recorded on OEIS A005725.

The checks are regression tests for the proof packet, not substitutes for
the proofs.  Python integers are used throughout.
"""

from math import comb


ODD_PRIMES = (3, 5, 7, 11, 13, 17, 19)
WOLSTENHOLME_PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
ARGUMENT_CAP = 900
BASE_N_CAP = 40


def quadrinomial_coefficient(n: int) -> int:
    """Return [x^n](1+x+x^2+x^3)^n."""
    return sum(comb(n, k) * comb(n, 2 * k) for k in range(n // 2 + 1))


def ratio_coefficient(n: int) -> int:
    """Return [x^n]((1+x)/(1-x))^n."""
    return sum(comb(n, k) * comb(2 * n - k - 1, n - k) for k in range(n + 1))


def check_quadrinomial_tower() -> tuple[int, int]:
    cache: dict[int, int] = {}

    def value(n: int) -> int:
        if n not in cache:
            cache[n] = quadrinomial_coefficient(n)
        return cache[n]

    cases = 0
    sharp = 0
    for prime in ODD_PRIMES:
        for level in range(1, 4):
            modulus = prime ** (2 * level)
            for n in range(1, BASE_N_CAP + 1):
                if n * prime**level > ARGUMENT_CAP:
                    continue
                difference = value(n * prime**level) - value(
                    n * prime ** (level - 1)
                )
                assert difference % modulus == 0, (prime, level, n)
                if difference % (prime * modulus) != 0:
                    sharp += 1
                cases += 1
    assert cases == 433
    assert sharp > 0
    return cases, sharp


def check_ratio_prime_boundary() -> tuple[int, int]:
    cases = 0
    sharp = 0
    for prime in WOLSTENHOLME_PRIMES:
        difference = ratio_coefficient(prime) - 2
        assert difference % prime**3 == 0, prime
        if difference % prime**4 != 0:
            sharp += 1
        cases += 1
    assert cases == 12
    assert sharp > 0
    return cases, sharp


def main() -> None:
    tower_cases, tower_sharp = check_quadrinomial_tower()
    ratio_cases, ratio_sharp = check_ratio_prime_boundary()
    print(
        f"quadrinomial tower: {tower_cases} cases "
        f"({tower_sharp} exact-exponent witnesses)"
    )
    print(
        f"ratio prime boundary: {ratio_cases} cases "
        f"({ratio_sharp} exact-exponent witnesses)"
    )
    print("all A005725 checks passed")


if __name__ == "__main__":
    main()
