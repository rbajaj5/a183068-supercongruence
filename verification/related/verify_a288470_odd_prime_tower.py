"""Exact checks for the A288470 odd-prime supercongruence.

The proof is in related-results/A288470OddPrimeTower.md. These checks are
finite regression tests, not a replacement for the proof.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb


def vp(value: int, prime: int) -> int:
    """Return v_prime(value), using a large sentinel at zero."""
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def summand(n: int, k: int) -> int:
    return comb(n, k) * comb(2 * n, 2 * k)


@lru_cache(maxsize=None)
def sequence_value(n: int) -> int:
    return sum(summand(n, k) for k in range(n + 1))


def gaussian_value(n: int) -> tuple[int, int]:
    """Return the i^k twist using exact Gaussian integer arithmetic."""
    real = 0
    imag = 0
    powers = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for k in range(n + 1):
        coefficient = summand(n, k)
        unit_real, unit_imag = powers[k % 4]
        real += unit_real * coefficient
        imag += unit_imag * coefficient
    return real, imag


def check_towers() -> int:
    checked = 0
    grids = {
        1: ((3, 5, 7, 11, 13, 17, 19), range(1, 9)),
        2: ((3, 5, 7, 11, 13), range(1, 6)),
        3: ((3, 5, 7), range(1, 4)),
    }
    for r, (primes, multipliers) in grids.items():
        for p in primes:
            modulus = p ** (2 * r)
            for m in multipliers:
                high = sequence_value(m * p**r)
                low = sequence_value(m * p ** (r - 1))
                assert (high - low) % modulus == 0, (p, r, m)
                checked += 1
    return checked


def check_termwise_budgets() -> tuple[int, int]:
    vanish_checked = 0
    transfer_checked = 0
    for p in (3, 5, 7, 11):
        for r in (1, 2, 3):
            for m in range(1, 5):
                n = m * p**r
                modulus = p ** (2 * r)
                for k in range(n + 1):
                    if k % p:
                        assert summand(n, k) % modulus == 0, (
                            "vanish",
                            p,
                            r,
                            m,
                            k,
                        )
                        vanish_checked += 1
                    else:
                        ell = k // p
                        delta = summand(n, k) - summand(n // p, ell)
                        assert delta % modulus == 0, (
                            "transfer",
                            p,
                            r,
                            m,
                            k,
                        )
                        transfer_checked += 1
    return vanish_checked, transfer_checked


def check_gaussian_towers() -> int:
    checked = 0
    for p in (3, 5, 7, 11, 13):
        for r in (1, 2):
            modulus = p ** (2 * r)
            for m in range(1, 5):
                high_real, high_imag = gaussian_value(m * p**r)
                low_real, low_imag = gaussian_value(m * p ** (r - 1))
                if p % 4 == 3:
                    low_imag = -low_imag
                delta_real = high_real - low_real
                delta_imag = high_imag - low_imag
                assert delta_real % modulus == 0, ("gaussian-real", p, r, m)
                assert delta_imag % modulus == 0, ("gaussian-imag", p, r, m)
                checked += 1
    return checked


def check_binary_boundary() -> int:
    assert sequence_value(1) == 2
    assert sequence_value(2) == 14
    assert sequence_value(4) == 646
    delta = sequence_value(4) - sequence_value(2)
    assert delta == 632
    assert vp(delta, 2) == 3
    assert delta % 2**4 != 0
    return 1


def main() -> None:
    tower_count = check_towers()
    vanish_count, transfer_count = check_termwise_budgets()
    gaussian_count = check_gaussian_towers()
    boundary_count = check_binary_boundary()
    total = (
        tower_count
        + vanish_count
        + transfer_count
        + gaussian_count
        + boundary_count
    )
    print("A288470 odd-prime checks passed")
    print(f"tower instances: {tower_count}")
    print(f"vanishing summands: {vanish_count}")
    print(f"transferred summands: {transfer_count}")
    print(f"Gaussian twist instances: {gaussian_count}")
    print(f"binary boundary cases: {boundary_count}")
    print(f"total exact checks: {total}")


if __name__ == "__main__":
    main()
