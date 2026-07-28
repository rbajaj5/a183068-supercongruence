"""Exact checks for the mixed dyadic affine obstruction.

These computations support transcription and finite-level debugging.  The
cohomology calculation itself is proved in the accompanying note.
"""

from __future__ import annotations


def q5(n: int, modulus: int) -> int:
    """Return (5^n - 1) / 4 modulo modulus without modular division."""
    total = 0
    power = 1
    for _ in range(n):
        total = (total + power) % modulus
        power = (5 * power) % modulus
    return total


def check_c2_cohomology() -> None:
    # A = Z/4Z with sign action.  Every element is a 1-cocycle because
    # (1+s)A = 0; coboundaries are (s-1)A = 2A.
    cocycles = {a for a in range(4) if (a + (-a)) % 4 == 0}
    coboundaries = {(-b - b) % 4 for b in range(4)}
    assert cocycles == {0, 1, 2, 3}
    assert coboundaries == {0, 2}
    assert len(cocycles) // len(coboundaries) == 2


def check_procyclic_cocycle(max_m: int = 10) -> int:
    checked = 0
    for m in range(3, max_m + 1):
        modulus = 1 << m
        gamma_order = 1 << (m - 2)

        assert pow(5, gamma_order, modulus) == 1
        if gamma_order > 1:
            assert pow(5, gamma_order // 2, modulus) != 1

        for n in range(gamma_order):
            qn = q5(n, modulus)
            assert (4 * qn - (pow(5, n, 4 * modulus) - 1)) % modulus == 0

            # phi_a(m,n) = (-m + a*q(n), n) is an involution.
            for a in (0, 1):
                for z in range(modulus):
                    first = (-z + a * qn) % modulus
                    second = (-first + a * qn) % modulus
                    assert second == z
                    checked += 1

        # q(n+n') = q(n) + 5^n q(n').  We do not reduce the exponents
        # modulo gamma_order: q modulo 2^m remembers more of n than the
        # action of 5 on Z/2^m does.
        for n in range(gamma_order):
            five_n = pow(5, n, modulus)
            for n_prime in range(gamma_order):
                lhs = q5(n + n_prime, modulus)
                rhs = (q5(n, modulus) + five_n * q5(n_prime, modulus)) % modulus
                assert lhs == rhs
                checked += 1
    return checked


def check_splitting_parity(max_m: int = 10) -> int:
    checked = 0
    for m in range(1, max_m + 1):
        modulus = 1 << m

        # A commuting pair of lifts exists iff a = 2b + 4c.  Exhaust the
        # smaller levels, then use the same exact parity criterion at all
        # remaining levels.
        if m <= 6:
            for a in range(modulus):
                count = sum(
                    1
                    for b in range(modulus)
                    for c in range(modulus)
                    if (a - 2 * b - 4 * c) % modulus == 0
                )
                expected = (1 << (m + 1)) if a % 2 == 0 else 0
                assert count == expected
                checked += modulus * modulus
        else:
            for a in range(modulus):
                assert (a % 2 == 0) == any(
                    (a - 2 * b) % modulus == 0 for b in range(modulus)
                )
                checked += modulus
    return checked


def main() -> None:
    check_c2_cohomology()
    cocycle_checks = check_procyclic_cocycle()
    splitting_checks = check_splitting_parity()
    print("C2 sign-cohomology quotient: 2 classes")
    print(f"Finite cocycle/involution checks: {cocycle_checks}")
    print(f"Finite splitting checks: {splitting_checks}")
    print("All mixed-obstruction checks passed.")


if __name__ == "__main__":
    main()
