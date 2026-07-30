"""Exact checks for the Straub p=5 boundary and three OEIS consequences.

The proof note is related-results/StraubPrimeFiveCoefficientPacket.md.
The computations are supporting regression tests, not a substitute for the proof.
"""

from __future__ import annotations

from math import comb
from random import Random


def multinomial(parts: list[int]) -> int:
    total = sum(parts)
    out = 1
    used = 0
    for part in parts:
        out *= comb(used + part, part)
        used += part
    assert used == total
    return out


def straub_coefficient(
    partition: tuple[int, ...], coordinates: tuple[int, ...], sign: int
) -> int:
    """Equation (20), restricted to positive coordinates."""

    assert sum(partition) == len(coordinates)
    assert sign in (-1, 1)
    out = 0
    for k in range(min(coordinates) + 1):
        cursor = 0
        term = sign**k
        for width in partition:
            block = coordinates[cursor : cursor + width]
            cursor += width
            term *= multinomial([value - k for value in block] + [k])
        out += term
    return out


def apery_zeta2_coefficient(n1: int, n2: int, n3: int) -> int:
    """Straub's B(n1,n2,n3), for nonnegative coordinates."""

    return sum(
        comb(n1, k)
        * comb(n1 + n2 - k, n1)
        * comb(n3, k)
        for k in range(min(n1, n2, n3) + 1)
    )


def apery_coefficient(n1: int, n2: int, n3: int, n4: int) -> int:
    """Straub's A(n1,n2,n3,n4), for nonnegative coordinates."""

    return sum(
        comb(n1, k)
        * comb(n3, k)
        * comb(n1 + n2 - k, n1)
        * comb(n3 + n4 - k, n3)
        for k in range(min(n1, n2, n3, n4) + 1)
    )


def a108625(n: int, m: int) -> int:
    return sum(
        comb(n, k) ** 2 * comb(n + m - k, m - k)
        for k in range(min(n, m) + 1)
    )


def a143007(n: int, m: int) -> int:
    return sum(
        comb(n, k) ** 2 * comb(n + m - k, m - k) ** 2
        for k in range(min(n, m) + 1)
    )


def a177316(n: int) -> int:
    if n == 0:
        return 1
    return sum(
        comb(n, k) ** 2 * comb(n + k - 1, k) ** 2
        for k in range(n + 1)
    )


def shifted_apery_coefficient(n: int) -> int:
    """Twice A(-n,n,-n,n), evaluated by its finite bilateral support."""

    if n == 0:
        return 1
    return 2 * sum(
        comb(n + k - 1, k) ** 2 * comb(n - 1, k - 1) ** 2
        for k in range(1, n + 1)
    )


def check_parameter_identifications() -> int:
    checks = 0
    for n in range(9):
        for m in range(9):
            assert a108625(n, m) == apery_zeta2_coefficient(n, m, n)
            assert a143007(n, m) == apery_coefficient(n, m, n, m)
            checks += 2
    for n in range(1, 21):
        assert a177316(n) == shifted_apery_coefficient(n)
        checks += 1
    return checks


def check_telescoping_identity() -> int:
    checks = 0
    for n in range(1, 21):
        terms = [
            comb(n, k) ** 2 * comb(n + k - 1, k) ** 2
            for k in range(n + 1)
        ] + [0]
        for k in range(n + 1):
            left = n**2 * (n**2 - 2 * k**2) * terms[k]
            right = (k + 1) ** 4 * terms[k + 1] - k**4 * terms[k]
            assert left == right
            checks += 1
    return checks


def check_reciprocal_square_boundary() -> int:
    checks = 0
    for level in range(1, 6):
        modulus = 5**level
        for sign in (1, -1):
            total = sum(
                (sign**k) * pow(k * k, -1, modulus)
                for k in range(1, modulus)
                if k % 5
            )
            assert total % modulus == 0
            checks += 1
    return checks


def check_prime_five_towers() -> int:
    checks = 0
    for level, bound in ((1, 8), (2, 3)):
        scale = 5**level
        previous = 5 ** (level - 1)
        modulus = 5 ** (3 * level)
        for n in range(1, bound + 1):
            for m in range(1, bound + 1):
                assert (
                    a108625(n * scale, m * scale)
                    - a108625(n * previous, m * previous)
                ) % modulus == 0
                assert (
                    a143007(n * scale, m * scale)
                    - a143007(n * previous, m * previous)
                ) % modulus == 0
                checks += 2
        for n in range(1, 2 * bound + 1):
            assert (
                a177316(n * scale) - a177316(n * previous)
            ) % modulus == 0
            checks += 1
    return checks


def check_general_prime_five_extension() -> int:
    rng = Random(14010854)
    partitions = ((1, 1), (2, 1), (1, 2), (2, 2), (1, 1, 1))
    checks = 0
    for level, trials, coordinate_bound in ((1, 60, 4), (2, 20, 2)):
        scale = 5**level
        previous = 5 ** (level - 1)
        modulus = 5 ** (3 * level)
        for _ in range(trials):
            partition = rng.choice(partitions)
            vector = tuple(
                rng.randint(1, coordinate_bound) for _ in range(sum(partition))
            )
            for sign in (-1, 1):
                upper = straub_coefficient(
                    partition, tuple(scale * value for value in vector), sign
                )
                lower = straub_coefficient(
                    partition, tuple(previous * value for value in vector), sign
                )
                assert (upper - lower) % modulus == 0
                checks += 1
    return checks


def main() -> None:
    counts = {
        "parameter identifications": check_parameter_identifications(),
        "telescoping identity": check_telescoping_identity(),
        "p=5 reciprocal-square boundary": check_reciprocal_square_boundary(),
        "p=5 OEIS towers": check_prime_five_towers(),
        "general p=5 coefficient towers": check_general_prime_five_extension(),
    }
    for label, count in counts.items():
        print(f"{label}: {count} checks")
    print(f"all {sum(counts.values())} Straub p=5 packet checks passed")


if __name__ == "__main__":
    main()
