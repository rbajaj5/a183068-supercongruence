"""Exact checks for the two A376 Apéry-companion reductions."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def rational_valuation(value: Fraction, prime: int) -> int:
    if value == 0:
        return 10**9
    return valuation(value.numerator, prime) - valuation(value.denominator, prime)


def primes_through(limit: int) -> list[int]:
    out: list[int] = []
    for candidate in range(2, limit + 1):
        if all(candidate % p for p in out if p * p <= candidate):
            out.append(candidate)
    return out


def crystal_direct(m: int, k: int) -> int:
    return sum(
        comb(m, j) ** 2 * comb(m + k - j, k - j)
        for j in range(0, min(m, k) + 1)
    )


def shifted_row(m: int, k: int) -> int:
    return sum(
        comb(m, j) * comb(m + j, j) * comb(k, j)
        for j in range(0, min(m, k) + 1)
    )


def integer_binomial(n: int, k: int) -> int:
    """Straub's integer binomial coefficient, including negative indices."""

    if k >= 0:
        if n >= 0:
            return comb(n, k) if k <= n else 0
        return (-1) ** k * comb(k - n - 1, k)
    if n >= 0 or k > n:
        return 0
    return integer_binomial(n, n - k)


def straub_b(n1: int, n2: int, n3: int) -> int:
    """Straub's B(n1,n2,n3) on the finite supports used here."""

    radius = abs(n1) + abs(n2) + abs(n3) + 2
    return sum(
        integer_binomial(n1, j)
        * integer_binomial(n1 + n2 - j, n1)
        * integer_binomial(n3, j)
        for j in range(-radius, radius + 1)
    )


def a376458_original(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        (-1) ** (n + k)
        * comb(n, k)
        * comb(n + k, k)
        * crystal_direct(n - 1, n - k)
        for k in range(n + 1)
    )


def a376458_single(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        (-1) ** j
        * comb(n, j) ** 2
        * comb(n - 1, j)
        * comb(n + j - 1, j)
        for j in range(n)
    )


def q_coefficient(n: int, j: int) -> int:
    return sum(
        (-1) ** (n + k)
        * comb(n, k)
        * comb(n + k, k) ** 2
        * comb(k, j)
        for k in range(j, n + 1)
    )


def q_coefficient_finite_difference(n: int, j: int) -> int:
    return comb(n, j) * sum(
        (-1) ** ell * comb(n - j, ell) * comb(2 * n - ell, n) ** 2
        for ell in range(n - j + 1)
    )


def a376466_original(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        (-1) ** (n + k)
        * comb(n, k)
        * comb(n + k, k) ** 2
        * crystal_direct(n - 1, k)
        for k in range(n + 1)
    )


def a376466_pairing(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        comb(n - 1, j) * comb(n + j - 1, j) * q_coefficient(n, j)
        for j in range(n)
    )


def a376466_outer(n: int, k: int) -> int:
    return (-1) ** (n + k) * comb(n, k) * comb(n + k, k) ** 2


def harmonic_mod(power: int, prime: int, modulus: int) -> int:
    return sum(pow(j, -power, modulus) for j in range(1, prime)) % modulus


def multiple_harmonic_13(prime: int) -> int:
    total = 0
    prefix = 0
    for j in range(1, prime):
        total += prefix * pow(j, -3, prime)
        prefix += pow(j, -1, prime)
    return total % prime


def product_term(prime: int, j: int) -> Fraction:
    out = Fraction(prime**3, j**3) * (1 - Fraction(prime, j))
    for h in range(1, j):
        out *= (1 - Fraction(prime, h)) ** 3
        out *= 1 + Fraction(prime, h)
    return out


def a376458_term(n: int, j: int) -> int:
    return (
        (-1) ** j
        * comb(n, j) ** 2
        * comb(n - 1, j)
        * comb(n + j - 1, j)
    )


def unit_reciprocal_sum(prime: int, k: int, power: int) -> Fraction:
    return sum(
        (
            Fraction(1, h**power)
            for h in range(1, prime * k)
            if h % prime
        ),
        Fraction(),
    )


def unit_block_factor(prime: int, n: int, k: int) -> Fraction:
    out = Fraction(1)
    for h in range(1, prime * k):
        if h % prime:
            x = Fraction(prime * n, h)
            out *= (1 - x) ** 3 * (1 + x)
    return out


def check_crystal_rows() -> int:
    checks = 0
    for m in range(0, 13):
        for k in range(0, 13):
            assert crystal_direct(m, k) == shifted_row(m, k)
            checks += 1
    return checks


def check_collapse_and_pairing() -> int:
    checks = 0
    expected_458 = [1, 1, -7, 1, 569, -3749, -45151, 806737, 1052729]
    expected_466 = [1, 3, 127, 9435, 866751, 89591753, 9988439203]
    for n in range(1, 18):
        original = a376458_original(n)
        collapsed = a376458_single(n)
        assert original == collapsed
        checks += 1
        for j in range(n + 1):
            transform = sum(
                (-1) ** (n + k)
                * comb(n, k)
                * comb(n + k, k)
                * comb(n - k, j)
                for k in range(n + 1)
            )
            assert transform == (-1) ** j * comb(n, j) ** 2
            checks += 1
    for n, expected in enumerate(expected_458):
        assert a376458_single(n) == expected
        checks += 1
    for n in range(1, 13):
        assert a376466_original(n) == a376466_pairing(n)
        checks += 1
        for j in range(n + 1):
            assert q_coefficient(n, j) == q_coefficient_finite_difference(n, j)
            checks += 1
    for n, expected in enumerate(expected_466):
        assert a376466_pairing(n) == expected
        checks += 1
    return checks


def check_prime_boundary() -> tuple[int, int]:
    checks = 0
    sharp = 0
    assert a376458_single(5) - a376458_single(1) == -3750
    assert valuation(-3750, 5) == 4
    checks += 2
    for prime in primes_through(101):
        if prime < 7:
            continue
        difference = a376458_single(prime) - 1
        depth = valuation(difference, prime)
        assert depth >= 5
        sharp += int(depth == 5)
        assert harmonic_mod(3, prime, prime**2) == 0
        assert harmonic_mod(4, prime, prime) == 0
        assert multiple_harmonic_13(prime) == 0
        checks += 4
        for j in range(1, prime):
            term = (
                (-1) ** j
                * comb(prime, j) ** 2
                * comb(prime - 1, j)
                * comb(prime + j - 1, j)
            )
            assert product_term(prime, j) == term
            checks += 1
    return checks, sharp


def check_ordinary_tower_lemma() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for k in range(1, 41):
            q = valuation(k, prime)
            s1 = unit_reciprocal_sum(prime, k, 1)
            s2 = unit_reciprocal_sum(prime, k, 2)
            assert rational_valuation(s1, prime) >= 2 * q + 2
            assert rational_valuation(s2, prime) >= q + 1
            checks += 2
        for n in range(1, 16):
            e = valuation(n, prime)
            for k in range(1, 16):
                q = valuation(k, prime)
                block = unit_block_factor(prime, n, k)
                expected = e + 2 * q + 3 if q <= e else 3 * e + 3
                assert rational_valuation(block - 1, prime) >= expected
                checks += 1
                if k < n:
                    high = a376458_term(prime * n, prime * k)
                    low = a376458_term(n, k)
                    assert Fraction(high, low) == block
                    assert valuation(high - low, prime) >= 3 * e + 3
                    checks += 2
            for j in range(1, prime * n):
                if j % prime:
                    assert valuation(a376458_term(prime * n, j), prime) >= 3 * e + 3
                    checks += 1
    return checks


def check_negative_row_reduction() -> int:
    checks = 0
    for n in range(1, 18):
        for k in range(18):
            assert shifted_row(n - 1, k) == straub_b(-n, k, -n)
            checks += 1

    for prime in (5, 7, 11):
        for n in range(1, 19):
            e = valuation(n, prime)
            for k in range(n + 1):
                high_row = shifted_row(prime * n - 1, prime * k)
                low_row = shifted_row(n - 1, k)
                q = valuation(k, prime) if k else 10**9
                row_depth = 3 * (min(e, q) + 1)
                assert (high_row - low_row) % prime**row_depth == 0
                checks += 1

    witness = a376466_outer(5, 1) * shifted_row(4, 1)
    assert valuation(witness, 5) == 1
    assert valuation(a376466_pairing(5) - a376466_pairing(1), 5) == 3
    checks += 2
    return checks


def check_shell_split(n: int, prime: int, which: str) -> None:
    high_n = prime * n
    if which == "458":
        high_coefficients = [(-1) ** j * comb(high_n, j) ** 2 for j in range(high_n)]
        low_coefficients = [(-1) ** j * comb(n, j) ** 2 for j in range(n)]
        high_value = a376458_single(high_n)
        low_value = a376458_single(n)
    else:
        high_coefficients = [q_coefficient(high_n, j) for j in range(high_n)]
        low_coefficients = [q_coefficient(n, j) for j in range(n)]
        high_value = a376466_pairing(high_n)
        low_value = a376466_pairing(n)
    high_row = [comb(high_n - 1, j) * comb(high_n + j - 1, j) for j in range(high_n)]
    low_row = [comb(n - 1, j) * comb(n + j - 1, j) for j in range(n)]
    scaled = sum(
        high_row[prime * j] * high_coefficients[prime * j]
        - low_row[j] * low_coefficients[j]
        for j in range(n)
    )
    unit = sum(
        high_row[j] * high_coefficients[j]
        for j in range(high_n)
        if j % prime
    )
    assert high_value - low_value == scaled + unit


def check_towers() -> tuple[int, int]:
    checks = 0
    sharp = 0
    for prime in (5, 7, 11):
        for n in (1, 2, 3):
            check_shell_split(n, prime, "458")
            check_shell_split(n, prime, "466")
            checks += 2
            for sequence in (a376458_single, a376466_pairing):
                depth = valuation(sequence(n * prime) - sequence(n), prime)
                assert depth >= 3
                sharp += int(depth == 3)
                checks += 1
            shifted_difference = (
                a376466_pairing(n * prime - 1) - a376466_pairing(n - 1)
            )
            if n == 1:
                shifted_depth = valuation(shifted_difference, prime)
                assert shifted_depth >= 3
                sharp += int(shifted_depth == 3)
            else:
                # The published all-n shifted conjecture already fails
                # modulo p in these exact first-level examples.
                assert shifted_difference % prime != 0
            checks += 1
    for prime in (5, 7):
        for sequence in (a376458_single, a376466_pairing):
            depth = valuation(sequence(prime * prime) - sequence(prime), prime)
            assert depth >= 6
            sharp += int(depth == 6)
            checks += 1
        shifted_depth = valuation(
            a376466_pairing(prime * prime - 1) - a376466_pairing(prime - 1), prime
        )
        assert shifted_depth == 4
        checks += 1
        enhanced = valuation(a376458_single(prime * prime) - a376458_single(prime), prime)
        assert enhanced >= 9
        sharp += int(enhanced == 9)
        checks += 1
    counterexample = a376466_pairing(9) - a376466_pairing(1)
    assert counterexample == 18063466831218978
    assert counterexample % 5 == 3
    checks += 2
    return checks, sharp


def main() -> None:
    crystal = check_crystal_rows()
    identities = check_collapse_and_pairing()
    boundary, boundary_sharp = check_prime_boundary()
    ordinary_lemma = check_ordinary_tower_lemma()
    negative_row = check_negative_row_reduction()
    towers, tower_sharp = check_towers()
    print(f"A108625 row-identity checks: {crystal}")
    print(f"A376 collapse/pairing checks: {identities}")
    print(f"A376458 prime-boundary checks: {boundary} ({boundary_sharp} sharp)")
    print(f"A376458 ordinary-tower lemma checks: {ordinary_lemma}")
    print(f"A376466 negative-row reduction checks: {negative_row}")
    print(f"A376 companion tower checks: {towers} ({tower_sharp} sharp)")
    print("A376 Apéry-companion checks passed")


if __name__ == "__main__":
    main()
