"""Exact checks for the first two A365029 levels and the remaining target."""

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


def check_second_level() -> int:
    checks = 0
    for prime, max_n in ((5, 14), (7, 12), (11, 9), (13, 7)):
        modulus = prime**6
        for n in range(1, max_n + 1):
            assert (
                sequence_term(n * prime**2) - sequence_term(n * prime)
            ) % modulus == 0
            checks += 1
    return checks


def check_shifted_transfer() -> int:
    checks = 0
    for prime, max_r, max_n in ((5, 3, 12), (7, 3, 9), (11, 2, 8)):
        for r in range(1, max_r + 1):
            modulus = prime ** (3 * r)
            lower_n = prime ** (r - 1)
            for n in range(1, max_n + 1):
                n_low = n * lower_n
                for ell in range(n_low + 1):
                    assert (
                        summand(n_low * prime, ell * prime)
                        - summand(n_low, ell)
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


def harmonic(limit: int, modulus: int) -> int:
    return sum(pow(value, -1, modulus) for value in range(1, limit + 1))


def check_second_level_expansions() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        modulus = prime**2
        half = (prime - 1) // 2
        for n in range(1, 10):
            for ell in range(n):
                prefactor = n * comb(n + ell, ell)
                for v in range(prime):
                    h_v = harmonic(v, modulus)
                    for c in range(1, prime):
                        unit = prime * v + c
                        k = modulus * ell + unit
                        n_big = modulus * n

                        first = generalized_binom(n_big + k - 1, k)
                        assert first % modulus == 0
                        predicted_first = (
                            prefactor
                            * pow(c, -1, modulus)
                            * (
                                1
                                + prime
                                * (
                                    n * h_v
                                    - v * pow(c, -1, modulus)
                                )
                            )
                        ) % modulus
                        assert (first // modulus) % modulus == predicted_first

                        epsilon = 0 if c <= half else 1
                        digit = 2 * v + epsilon
                        carry, residue = divmod(digit, prime)
                        reduced = (
                            comb(2 * ell + carry, n)
                            if n <= 2 * ell + carry
                            else 0
                        )
                        predicted_second = (
                            reduced
                            * (1 + prime * n * harmonic(residue, modulus))
                        ) % modulus
                        actual_second = generalized_binom(
                            2 * k - 1, n_big
                        ) % modulus
                        assert actual_second == predicted_second
                        checks += 2
    return checks


def check_second_level_harmonic_identities() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        modulus = prime**2
        half = (prime - 1) // 2
        s2 = sum(pow(c, -2, modulus) for c in range(1, half + 1))
        s3 = sum(pow(c, -3, modulus) for c in range(1, half + 1))
        upper2 = sum(
            pow(c, -2, modulus) for c in range(half + 1, prime)
        )
        upper3 = sum(
            pow(c, -3, modulus) for c in range(half + 1, prime)
        )
        full2 = (s2 + upper2) % modulus
        full3 = (s3 + upper3) % modulus
        assert s2 % prime == upper2 % prime == 0
        assert full3 % prime == 0
        assert (full2 - 2 * s2 - 2 * prime * s3) % modulus == 0
        assert (upper2 - s2 - 2 * prime * s3) % modulus == 0
        assert (upper3 + s3) % prime == 0
        assert (
            half * full2 + s2 - 2 * prime * half * s3
        ) % modulus == 0
        assert (
            half * full2 + upper2 - 2 * prime * half * upper3
        ) % modulus == 0
        checks += 7
    return checks


def check_second_level_half_blocks() -> int:
    checks = 0
    for prime, max_n in ((5, 10), (7, 8), (11, 6), (13, 5)):
        q = prime**2
        for n in range(1, max_n + 1):
            n_big = n * q
            for ell in range(n):
                lower = 0
                upper = 0
                for unit in range(1, q):
                    if unit % prime == 0:
                        continue
                    k = q * ell + unit
                    first = generalized_binom(n_big + k - 1, k)
                    assert first % q == 0
                    term = (
                        (first // q) ** 2
                        * generalized_binom(2 * k - 1, n_big)
                    )
                    if 2 * unit < q:
                        lower += term
                    else:
                        upper += term
                assert lower % q == 0
                assert upper % q == 0
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
        "second-level theorem": check_second_level(),
        "shifted transfer": check_shifted_transfer(),
        "Lucas block formula": check_lucas_block_formula(),
        "half reciprocal squares": check_half_reciprocal_squares(),
        "second-level local expansions": check_second_level_expansions(),
        "second-level harmonic identities": (
            check_second_level_harmonic_identities()
        ),
        "second-level half blocks": check_second_level_half_blocks(),
        "higher-level block target": check_higher_level_block_target(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(f"all {sum(counts.values())} A365029 first-two-level checks passed")


if __name__ == "__main__":
    main()
