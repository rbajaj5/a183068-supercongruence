"""Exact checks for the dyadic affine splitting proxy.

The proof is symbolic and appears in
related-results/GQ2AffineSplittingProxy.md.  This script checks finite
2-power shadows of every displayed algebraic identity, the parity splitting
criterion, and the Yablo truncation comparison.
"""

from __future__ import annotations

from itertools import product
from random import Random


def q_mod(n: int, bits: int) -> int:
    """Return (5^n - 1) / 4 modulo 2^bits."""

    modulus = 1 << bits
    lifted = pow(5, n, 4 * modulus)
    assert (lifted - 1) % 4 == 0
    return ((lifted - 1) // 4) % modulus


def mul_h(
    left: tuple[int, int], right: tuple[int, int], bits: int
) -> tuple[int, int]:
    """Multiplication in (Z/2^bits) semidirect C_(2^bits)."""

    modulus = 1 << bits
    x, n = left
    y, m = right
    return (
        (x + pow(5, n, modulus) * y) % modulus,
        (n + m) % modulus,
    )


def tau(z: int, value: tuple[int, int], bits: int) -> tuple[int, int]:
    modulus = 1 << bits
    x, n = value
    return ((-x + z * q_mod(n, bits)) % modulus, n)


def verify_q_cocycle() -> int:
    checks = 0
    for bits in range(1, 9):
        modulus = 1 << bits
        for n, m in product(range(modulus), repeat=2):
            lhs = q_mod((n + m) % modulus, bits)
            rhs = (
                q_mod(n, bits)
                + pow(5, n, modulus) * q_mod(m, bits)
            ) % modulus
            assert lhs == rhs
            checks += 1

    rng = Random(20260727)
    for bits in range(9, 33):
        modulus = 1 << bits
        for _ in range(1000):
            n = rng.randrange(modulus)
            m = rng.randrange(modulus)
            lhs = q_mod((n + m) % modulus, bits)
            rhs = (
                q_mod(n, bits)
                + pow(5, n, modulus) * q_mod(m, bits)
            ) % modulus
            assert lhs == rhs
            checks += 1
    return checks


def verify_tau() -> int:
    checks = 0
    for bits in range(1, 6):
        modulus = 1 << bits
        states = list(product(range(modulus), repeat=2))
        for z in (0, 1):
            for value in states:
                assert tau(z, tau(z, value, bits), bits) == value
                checks += 1
            for left, right in product(states, repeat=2):
                lhs = tau(z, mul_h(left, right, bits), bits)
                rhs = mul_h(tau(z, left, bits), tau(z, right, bits), bits)
                assert lhs == rhs
                checks += 1
    return checks


def verify_splitting_parity() -> int:
    checks = 0
    for bits in range(1, 10):
        modulus = 1 << bits
        attainable = {
            (2 * b + 4 * c) % modulus
            for b, c in product(range(modulus), repeat=2)
        }
        expected = {z for z in range(modulus) if z % 2 == 0}
        assert attainable == expected
        for z in range(modulus):
            assert (z in attainable) == (z % 2 == 0)
            checks += 1
    return checks


def verify_sign_cohomology() -> int:
    # A = Z/4 with the sign action.  Every x is a 1-cocycle because
    # x + (-x) = 0; coboundaries are (-y)-y = -2y.
    cocycles = {x for x in range(4) if (x - x) % 4 == 0}
    coboundaries = {(-2 * y) % 4 for y in range(4)}
    assert cocycles == {0, 1, 2, 3}
    assert coboundaries == {0, 2}
    quotient_cosets = {
        frozenset((x + b) % 4 for b in coboundaries) for x in cocycles
    }
    assert quotient_cosets == {frozenset({0, 2}), frozenset({1, 3})}
    return len(cocycles) + len(coboundaries)


def yablo_solutions(length: int) -> list[tuple[int, ...]]:
    solutions: list[tuple[int, ...]] = []
    for assignment in product((0, 1), repeat=length):
        if all(
            (assignment[n] == 1)
            == all(assignment[k] == 0 for k in range(n + 1, length))
            for n in range(length)
        ):
            solutions.append(assignment)
    return solutions


def verify_yablo_truncations() -> int:
    checks = 0
    previous: tuple[int, ...] | None = None
    for length in range(1, 17):
        solutions = yablo_solutions(length)
        expected = (0,) * (length - 1) + (1,)
        assert solutions == [expected]
        if previous is not None:
            assert expected[:-1] == (0,) * (length - 1)
            assert expected[:-1] != previous
            checks += 1
        previous = expected
        checks += 1
    return checks


def main() -> None:
    cocycle_checks = verify_q_cocycle()
    tau_checks = verify_tau()
    splitting_checks = verify_splitting_parity()
    cohomology_checks = verify_sign_cohomology()
    yablo_checks = verify_yablo_truncations()
    total = (
        cocycle_checks
        + tau_checks
        + splitting_checks
        + cohomology_checks
        + yablo_checks
    )
    print(
        "PASS: dyadic affine splitting proxy "
        f"({total} exact checks; "
        f"{cocycle_checks} cocycle, {tau_checks} automorphism, "
        f"{splitting_checks} splitting, {cohomology_checks} cohomology, "
        f"{yablo_checks} Yablo)"
    )


if __name__ == "__main__":
    main()
