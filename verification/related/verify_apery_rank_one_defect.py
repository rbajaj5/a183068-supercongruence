"""Exact checks for AperyRankOneDefectPacket.md.

The three enhanced defect relations remain conjectural.  This script checks
finite instances and the exact algebraic reductions; it is not their proof.
"""

from __future__ import annotations

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


def zeta2_apery(n: int) -> int:
    return sum(comb(n, k) ** 2 * comb(n + k, k) for k in range(n + 1))


def zeta3_apery(n: int) -> int:
    return sum(
        comb(n, k) ** 2 * comb(n + k, k) ** 2 for k in range(n + 1)
    )


def enhanced_exponent(r: int) -> int:
    return 5 if r == 1 else 3 * r + 3


def source_sequences(n: int) -> tuple[int, ...]:
    z_n = zeta2_apery(n)
    z_before = zeta2_apery(n - 1)
    w_n = zeta3_apery(n)
    w_before = zeta3_apery(n - 1)
    return (
        (z_n + z_before) // 2,
        z_n**3 * z_before,
        5 * w_n - 14 * z_n,
        5 * w_before - 2 * z_before,
        5 * w_before + 2 * z_n,
        3**42 * w_n**25 - 5**25 * z_n**42,
        w_before**5 * z_n**6,
    )


def check_packet() -> tuple[int, int, int]:
    cases = [(p, 1) for p in (5, 7, 11, 13, 17, 19, 23, 29, 31)]
    cases += [(p, 2) for p in (5, 7, 11, 13)]
    cases += [(5, 3), (7, 3)]

    relation_checks = 0
    source_checks = 0
    rank_one_checks = 0

    for prime, r in cases:
        high_index = prime**r
        low_index = prime ** (r - 1)
        z_high = zeta2_apery(high_index)
        z_low = zeta2_apery(low_index)
        zm_high = zeta2_apery(high_index - 1)
        zm_low = zeta2_apery(low_index - 1)
        w_high = zeta3_apery(high_index)
        w_low = zeta3_apery(low_index)
        wm_high = zeta3_apery(high_index - 1)
        wm_low = zeta3_apery(low_index - 1)

        alpha = z_high - z_low
        beta = zm_high - zm_low
        gamma = w_high - w_low
        delta = wm_high - wm_low
        defects = (alpha, beta, gamma, delta)

        assert all(valuation(value, prime) >= 3 * r for value in defects)
        relation_checks += 4

        exponent = enhanced_exponent(r)
        modulus = prime**exponent
        relations = (
            alpha + beta,
            5 * gamma - 14 * alpha,
            5 * delta - 2 * beta,
        )
        assert all(value % modulus == 0 for value in relations)
        relation_checks += 3

        high_sources = source_sequences(high_index)
        low_sources = source_sequences(low_index)
        for high, low in zip(high_sources, low_sources, strict=True):
            assert (high - low) % modulus == 0
            source_checks += 1

        if prime != 5:
            q = alpha * pow(5, -1, modulus) % modulus
            predicted = (5 * q, -5 * q, 14 * q, -2 * q)
            assert all(
                (observed - expected) % modulus == 0
                for observed, expected in zip(defects, predicted, strict=True)
            )
            rank_one_checks += 4

    return relation_checks, source_checks, rank_one_checks


def check_isolated_binary_and_ternary_boundaries() -> int:
    # A357506 explicitly includes p=3 at the first level.
    assert (
        zeta2_apery(3) ** 3 * zeta2_apery(2) - 27
    ) % 3**5 == 0

    # The five-record packet is not asserted at p=2.
    high = source_sequences(2)
    low = source_sequences(1)
    assert any((a - b) % 2**5 for a, b in zip(high, low, strict=True))
    return 2


def main() -> None:
    relation_checks, source_checks, rank_one_checks = check_packet()
    boundary_checks = check_isolated_binary_and_ternary_boundaries()
    total = (
        relation_checks + source_checks + rank_one_checks + boundary_checks
    )
    print("Apéry rank-one defect packet checks passed")
    print(f"baseline and three-relation checks: {relation_checks}")
    print(f"linear and nonlinear source checks: {source_checks}")
    print(f"rank-one coordinate checks: {rank_one_checks}")
    print(f"small-prime boundary checks: {boundary_checks}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
