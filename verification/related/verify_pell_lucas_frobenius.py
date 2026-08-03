"""Exact checks for the Pell--Lucas Frobenius tower.

The proof is in related-results/PellLucasFrobeniusTower.md.  These checks
guard the signs, exponents, and sample Pell data against transcription errors.
"""

from __future__ import annotations


def mul_pair(
    left: tuple[int, int], right: tuple[int, int], d: int
) -> tuple[int, int]:
    a, b = left
    c, e = right
    return a * c + d * b * e, a * e + b * c


def pow_pair_mod(
    base: tuple[int, int], exponent: int, d: int, modulus: int
) -> tuple[int, int]:
    result = (1, 0)
    current = (base[0] % modulus, base[1] % modulus)
    while exponent:
        if exponent & 1:
            result = mul_pair(result, current, d)
            result = result[0] % modulus, result[1] % modulus
        current = mul_pair(current, current, d)
        current = current[0] % modulus, current[1] % modulus
        exponent >>= 1
    return result


def pow_pair(base: tuple[int, int], exponent: int, d: int) -> tuple[int, int]:
    result = (1, 0)
    current = base
    while exponent:
        if exponent & 1:
            result = mul_pair(result, current, d)
        current = mul_pair(current, current, d)
        exponent >>= 1
    return result


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def legendre(d: int, prime: int) -> int:
    residue = pow(d % prime, (prime - 1) // 2, prime)
    assert residue in (1, prime - 1)
    return 1 if residue == 1 else -1


def local_quotient_depth(
    unit: tuple[int, int], d: int, prime: int, chi: int
) -> int:
    # q = epsilon^p epsilon^{-chi}; norm(epsilon)=1.
    epsilon_p = pow_pair(unit, prime, d)
    epsilon_minus_chi = (unit[0], -chi * unit[1])
    quotient = mul_pair(epsilon_p, epsilon_minus_chi, d)
    return min(
        valuation(quotient[0] - 1, prime),
        valuation(quotient[1], prime),
    )


def main() -> None:
    pell_units = (
        (2, (3, 2)),
        (3, (2, 1)),
        (5, (9, 4)),
        (6, (5, 2)),
    )
    primes = (3, 5, 7, 11, 13, 17, 19)
    checks = 0

    for d, unit in pell_units:
        assert unit[0] ** 2 - d * unit[1] ** 2 == 1
        for prime in primes:
            if d % prime == 0:
                continue
            chi = legendre(d, prime)
            depth = local_quotient_depth(unit, d, prime, chi)
            assert depth >= 1
            checks += 2

            for n in range(1, 7):
                n_depth = valuation(n, prime)
                for r in range(1, 5):
                    baseline_exponent = r + n_depth
                    refined_exponent = depth + r - 1 + n_depth
                    modulus = prime**refined_exponent
                    high = pow_pair_mod(unit, n * prime**r, d, modulus)
                    low = pow_pair_mod(unit, n * prime ** (r - 1), d, modulus)

                    assert (high[0] - low[0]) % prime**baseline_exponent == 0
                    assert (high[1] - chi * low[1]) % prime**baseline_exponent == 0
                    assert (high[0] - low[0]) % modulus == 0
                    assert (high[1] - chi * low[1]) % modulus == 0
                    checks += 4

    print(f"Pell--Lucas Frobenius checks passed: {checks}")


if __name__ == "__main__":
    main()

