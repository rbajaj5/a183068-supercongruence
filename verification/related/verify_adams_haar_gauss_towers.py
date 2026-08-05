"""Exact checks for the Adams--Haar representation-ring note.

The script is a regression and transcription checker.  The proofs are in
related-results/AdamsHaarRepresentationGaussTowers.md.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_pow(a: list[list[int]], exponent: int) -> list[list[int]]:
    size = len(a)
    result = [[int(i == j) for j in range(size)] for i in range(size)]
    base = a
    while exponent:
        if exponent & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        exponent >>= 1
    return result


def convolve(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, 0) + a * b
    return {k: v for k, v in out.items() if v}


def laurent_pow(poly: dict[int, int], exponent: int) -> dict[int, int]:
    result = {0: 1}
    base = poly
    while exponent:
        if exponent & 1:
            result = convolve(result, base)
        base = convolve(base, base)
        exponent >>= 1
    return result


def check_scalar_amplification() -> int:
    checks = 0
    for p in (2, 3, 5, 7):
        for r in range(1, 6):
            modulus = p**r
            for a in range(-4, 5):
                for c in range(-3, 4):
                    b = a**p + p * c
                    assert (a ** (p**r) - b ** (p ** (r - 1))) % modulus == 0
                    checks += 1
    return checks


def check_torus_constant_terms() -> int:
    checks = 0
    polynomials = (
        {-1: 1, 0: 1, 1: 1},
        {-2: 1, -1: -2, 0: 3, 1: 1},
        {-1: 2, 2: 1},
    )
    for poly in polynomials:
        for p in (2, 3, 5):
            for n in range(1, 4):
                for r in range(1, 4):
                    upper = laurent_pow(poly, n * p**r).get(0, 0)
                    lower = laurent_pow(poly, n * p ** (r - 1)).get(0, 0)
                    assert (upper - lower) % (p**r) == 0
                    checks += 1
    return checks


def s3_inner(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    # Conjugacy-class order: identity, transpositions, three-cycles.
    value = Fraction(sum(size * a * b for size, a, b in zip((1, 3, 2), left, right)), 6)
    assert value.denominator == 1
    return value.numerator


def check_s3_spectral_packet() -> int:
    irreducibles = (
        (1, 1, 1),   # trivial
        (1, -1, 1),  # sign
        (2, 0, -1),  # standard
    )
    character_v = tuple(a + b for a, b in zip(irreducibles[0], irreducibles[2]))

    # Column j records the decomposition of V tensor rho_j.
    fusion = [
        [
            s3_inner(tuple(character_v[k] * irreducibles[j][k] for k in range(3)), irreducibles[i])
            for j in range(3)
        ]
        for i in range(3)
    ]
    assert fusion == [[1, 0, 1], [0, 1, 1], [1, 1, 2]]

    values: list[int] = []
    checks = 1
    for exponent in range(31):
        spectral = Fraction(
            sum(size * value**exponent for size, value in zip((1, 3, 2), character_v)),
            6,
        )
        assert spectral.denominator == 1
        via_fusion = mat_pow(fusion, exponent)[0][0]
        assert spectral.numerator == via_fusion
        values.append(via_fusion)
        checks += 1

    # Eigenvalues are 3, 1, 0, so Cayley--Hamilton gives this recurrence.
    for n in range(28):
        assert values[n + 3] == 4 * values[n + 2] - 3 * values[n + 1]
        checks += 1

    for p in (5, 7, 11):  # precisely the tested primes away from |S_3|=6
        for n in range(1, 6):
            for r in range(1, 4):
                upper = Fraction(
                    sum(size * value ** (n * p**r) for size, value in zip((1, 3, 2), character_v)),
                    6,
                )
                lower = Fraction(
                    sum(
                        size * value ** (n * p ** (r - 1))
                        for size, value in zip((1, 3, 2), character_v)
                    ),
                    6,
                )
                assert upper.denominator == lower.denominator == 1
                assert (upper.numerator - lower.numerator) % (p**r) == 0
                checks += 1

    return checks


def su2_standard_invariants(tensor_power: int) -> int:
    if tensor_power % 2:
        return 0
    half = tensor_power // 2
    return comb(2 * half, half) // (half + 1)


def check_nonabelian_boundary() -> int:
    assert su2_standard_invariants(1) == 0
    assert su2_standard_invariants(2) == 1
    assert (su2_standard_invariants(2) - su2_standard_invariants(1)) % 2 == 1
    return 3


def main() -> None:
    checks = 0
    checks += check_scalar_amplification()
    checks += check_torus_constant_terms()
    checks += check_s3_spectral_packet()
    checks += check_nonabelian_boundary()
    print(f"Adams--Haar checks passed: {checks}")


if __name__ == "__main__":
    main()
