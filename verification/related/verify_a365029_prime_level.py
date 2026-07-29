"""Exact checks for the prime-level A365029 theorem and its tower target."""

from __future__ import annotations

from math import comb


def generalized_binom(n: int, k: int) -> int:
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


def summand(n: int, k: int) -> int:
    return (
        generalized_binom(n + k - 1, k) ** 2
        * generalized_binom(2 * k - 1, n)
    )


def sequence_term(n: int) -> int:
    return sum(summand(n, k) for k in range(n + 1))


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def check_prime_level() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19):
        modulus = prime**3
        for n in range(1, 31):
            assert (sequence_term(n * prime) - sequence_term(n)) % modulus == 0
            checks += 1
    return checks


def check_shifted_transfer() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        modulus = prime**3
        for n in range(1, 41):
            for ell in range(n + 1):
                assert (
                    summand(n * prime, ell * prime) - summand(n, ell)
                ) % modulus == 0
                checks += 1
    return checks


def check_lucas_block_formula() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17):
        half = (prime - 1) // 2
        for n in range(1, 35):
            for ell in range(n):
                block = 0
                scale = n * n * comb(n + ell, ell) ** 2
                predicted = 0
                for unit in range(1, prime):
                    k = prime * ell + unit
                    first = generalized_binom(n * prime + k - 1, k)
                    assert first % prime == 0
                    second_reduction = comb(
                        2 * ell + (1 if unit > half else 0), n
                    )
                    local = (
                        scale
                        * pow(unit, -2, prime)
                        * second_reduction
                    ) % prime
                    actual = (
                        (first // prime) ** 2
                        * generalized_binom(2 * k - 1, n * prime)
                    ) % prime
                    assert actual == local
                    block = (block + actual) % prime
                    predicted = (predicted + local) % prime
                    checks += 1
                assert block == predicted == 0
                checks += 1
    return checks


def check_half_reciprocal_squares() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        half = (prime - 1) // 2
        lower = sum(pow(unit, -2, prime) for unit in range(1, half + 1))
        upper = sum(pow(unit, -2, prime) for unit in range(half + 1, prime))
        assert lower % prime == 0
        assert upper % prime == 0
        checks += 2
    return checks


def check_higher_level_block_target() -> int:
    checks = 0
    for prime, max_r, max_n in ((5, 3, 7), (7, 3, 6), (11, 2, 5)):
        for r in range(1, max_r + 1):
            q = prime**r
            modulus = q
            for n in range(1, max_n + 1):
                n_big = n * q
                for ell in range(n):
                    normalized = 0
                    for unit in range(1, q):
                        if unit % prime == 0:
                            continue
                        k = q * ell + unit
                        first = generalized_binom(n_big + k - 1, k)
                        assert first % q == 0
                        normalized += (
                            (first // q) ** 2
                            * generalized_binom(2 * k - 1, n_big)
                        )
                    assert normalized % modulus == 0
                    checks += 1
    return checks


def main() -> None:
    counts = {
        "prime-level theorem": check_prime_level(),
        "shifted transfer": check_shifted_transfer(),
        "Lucas block formula": check_lucas_block_formula(),
        "half reciprocal squares": check_half_reciprocal_squares(),
        "higher-level block target": check_higher_level_block_target(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(f"all {sum(counts.values())} A365029 checks passed")


if __name__ == "__main__":
    main()
