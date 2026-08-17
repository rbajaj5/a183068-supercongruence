"""Exact checks for the A362676 one-step cubic congruence.

The script audits the finite transformation, the two carry formulas, the
residue-block cancellation, and the resulting r=1 theorem.  It is not a
replacement for the companion proof.
"""

from __future__ import annotations

from math import comb


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**9
    result = 0
    while n % p == 0:
        result += 1
        n //= p
    return result


def original_sum(n: int) -> int:
    return sum(
        4 ** (n - k) * comb(n, k) * comb(n - 1, k) * comb(2 * k, k)
        for k in range(n + 1)
    )


def convolution_term(n: int, k: int) -> int:
    return (
        comb(n + k - 1, k)
        * comb(2 * (n - k), n - k)
        * comb(2 * k, k)
    )


def convolution_sum(n: int) -> int:
    return sum(convolution_term(n, k) for k in range(n + 1))


def check_convolution(limit: int = 60) -> int:
    checks = 0
    for n in range(1, limit + 1):
        assert original_sum(n) == convolution_sum(n)
        checks += 1
    return checks


def check_local_formulas(prime_limit: int = 50) -> int:
    checks = 0
    for p in range(5, prime_limit):
        if not is_prime(p):
            continue
        modulus = p**3

        # Shifted Jacobsthal contraction, including inputs beyond one digit.
        for a in range(1, 2 * p + 3):
            for b in range(a):
                assert (comb(p * a - 1, p * b) - comb(a - 1, b)) % modulus == 0
                checks += 1

        h = (p - 1) // 2
        half_reciprocal = sum(pow(b * b, -1, p) for b in range(1, h + 1)) % p
        assert half_reciprocal == 0
        checks += 1

        for a in range(1, 2 * p + 3):
            for b in range(1, h + 1):
                carried = comb(2 * (a * p - b), a * p - b) // p
                expected = (
                    -a
                    * comb(2 * a, a)
                    * pow(b * comb(2 * b, b), -1, p)
                ) % p
                assert carried % p == expected
                checks += 1
    return checks


def check_blocks(prime_limit: int = 45, n_limit: int = 14) -> tuple[int, int]:
    checks = 0
    sharp = 0
    for p in range(5, prime_limit):
        if not is_prime(p):
            continue
        for n in range(1, n_limit + 1):
            big_n = n * p
            for j in range(n):
                block = sum(
                    convolution_term(big_n, j * p + b)
                    for b in range(1, p)
                )
                assert block % (p**3) == 0
                if valuation(block, p) == 3:
                    sharp += 1
                checks += 1
    return checks, sharp


def check_theorem(prime_limit: int = 45, n_limit: int = 14) -> tuple[int, int]:
    checks = 0
    sharp = 0
    for p in range(5, prime_limit):
        if not is_prime(p):
            continue
        for n in range(1, n_limit + 1):
            delta = convolution_sum(n * p) - convolution_sum(n)
            assert delta % (p**3) == 0
            if valuation(delta, p) == 3:
                sharp += 1
            checks += 1
    return checks, sharp


def main() -> None:
    convolution_checks = check_convolution()
    local_checks = check_local_formulas()
    block_checks, sharp_blocks = check_blocks()
    theorem_checks, sharp_theorems = check_theorem()

    print("A362676 one-step verification passed")
    print(f"exact convolution checks: {convolution_checks}")
    print(f"local congruence checks: {local_checks}")
    print(f"residue-block checks: {block_checks}")
    print(f"sharp residue blocks: {sharp_blocks}")
    print(f"direct theorem checks: {theorem_checks}")
    print(f"sharp theorem instances: {sharp_theorems}")


if __name__ == "__main__":
    main()
