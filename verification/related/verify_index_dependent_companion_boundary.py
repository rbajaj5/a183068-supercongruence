"""Exact checks for the index-dependent companion prime boundary."""

from __future__ import annotations

from math import comb


def integer_binomial(top: int, bottom: int) -> int:
    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(-top + bottom - 1, bottom)


def finite_term(n: int, k: int) -> int:
    return (
        integer_binomial(-n, k)
        * integer_binomial(n, k)
        * integer_binomial(2 * k, n)
        * integer_binomial(n + k, k)
    )


def cutoff_term(n: int, k: int) -> int:
    return (
        integer_binomial(-n, k) ** 2
        * integer_binomial(2 * k, n)
        * integer_binomial(n + k, k)
    )


def finite_sum(n: int) -> int:
    return sum(finite_term(n, k) for k in range(n + 1))


def cutoff_sum(n: int, cutoff: int) -> int:
    return sum(cutoff_term(n, k) for k in range(cutoff * n + 1))


def check_half_residues() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31):
        half = (prime - 1) // 2
        left = sum(pow(s, -2, prime) for s in range(1, half + 1)) % prime
        right = sum(pow(s, -2, prime) for s in range(half + 1, prime)) % prime
        assert left == right == 0
        checks += 2
    return checks


def check_unit_block_formulas() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17):
        half = (prime - 1) // 2
        for n in range(1, 9):
            for q in range(0, 3 * n):
                cutoff_block = 0
                for s in range(1, prime):
                    k = prime * q + s
                    term = cutoff_term(prime * n, k)
                    assert term % prime**2 == 0
                    cutoff_block += term // prime**2

                    negative_lead = (
                        (-1) ** (q + s)
                        * n
                        * pow(s, -1, prime)
                        * comb(n + q, q)
                    ) % prime
                    assert (
                        integer_binomial(-prime * n, k) // prime
                        - negative_lead
                    ) % prime == 0
                    checks += 2

                expected_cutoff = n * n * comb(n + q, q) ** 3
                expected_cutoff *= (
                    comb(2 * q, n)
                    * sum(pow(s, -2, prime) for s in range(1, half + 1))
                    + comb(2 * q + 1, n)
                    * sum(pow(s, -2, prime) for s in range(half + 1, prime))
                )
                assert (cutoff_block - expected_cutoff) % prime == 0
                assert cutoff_block % prime == 0
                checks += 2

                if q < n:
                    finite_block = sum(
                        finite_term(prime * n, prime * q + s) // prime**2
                        for s in range(1, prime)
                    )
                    sign = -1 if q % 2 == 0 else 1
                    expected_finite = sign * n * n
                    expected_finite *= comb(n - 1, q) * comb(n + q, q)
                    expected_finite *= (
                        comb(2 * q, n)
                        * sum(pow(s, -2, prime) for s in range(1, half + 1))
                        + comb(2 * q + 1, n)
                        * sum(pow(s, -2, prime) for s in range(half + 1, prime))
                    )
                    assert (finite_block - expected_finite) % prime == 0
                    assert finite_block % prime == 0
                    checks += 2
    return checks


def check_scaled_transfer() -> int:
    checks = 0
    grids = {
        5: ((1, 2, 3), (1, 2, 3)),
        7: ((1, 2), (1, 2, 3)),
        11: ((1, 2), (1, 2)),
        13: ((1, 2), (1, 2)),
    }
    for prime, (multipliers, levels) in grids.items():
        for level in levels:
            high_scale = prime**level
            low_scale = high_scale // prime
            modulus = prime ** (3 * level)
            for n in multipliers:
                high_n = n * high_scale
                low_n = n * low_scale
                for q in range(0, 3 * low_n + 1):
                    assert (
                        cutoff_term(high_n, prime * q)
                        - cutoff_term(low_n, q)
                    ) % modulus == 0
                    checks += 1
                    if q <= low_n:
                        assert (
                            finite_term(high_n, prime * q)
                            - finite_term(low_n, q)
                        ) % modulus == 0
                        checks += 1
    return checks


def check_quadratic_substitution() -> int:
    """Check the coefficient identities (14)--(16) independently."""

    checks = 0
    for n in range(1, 41):
        finite_coefficient = sum(
            integer_binomial(-n, k)
            * integer_binomial(n, k)
            * integer_binomial(n + k, k)
            * integer_binomial(2 * k, n)
            for k in range(n + 1)
        )
        assert finite_coefficient == finite_sum(n)
        checks += 1

        for cutoff in (1, 2, 3, 4):
            cutoff_coefficient = sum(
                integer_binomial(-n, k) ** 2
                * integer_binomial(n + k, k)
                * integer_binomial(2 * k, n)
                for k in range(cutoff * n + 1)
            )
            assert cutoff_coefficient == cutoff_sum(n, cutoff)
            checks += 1
    return checks


def check_prime_boundary() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19):
        modulus = prime**3
        for n in range(1, 9):
            assert (finite_sum(prime * n) - finite_sum(n)) % modulus == 0
            checks += 1
            for cutoff in (1, 2, 3):
                assert (
                    cutoff_sum(prime * n, cutoff) - cutoff_sum(n, cutoff)
                ) % modulus == 0
                checks += 1
    return checks


def main() -> None:
    results = {
        "half-residue identities": check_half_residues(),
        "unit-block formulas": check_unit_block_formulas(),
        "all-level scaled transfer": check_scaled_transfer(),
        "quadratic-substitution identities": check_quadratic_substitution(),
        "prime-boundary towers": check_prime_boundary(),
    }
    for name, count in results.items():
        print(f"{name}: {count} exact checks")
    print(f"total: {sum(results.values())} exact checks")


if __name__ == "__main__":
    main()
