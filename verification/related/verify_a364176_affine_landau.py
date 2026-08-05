"""Exact checks for the A364176 affine-Landau theorem.

The script is a regression certificate, not a proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def vp_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def vp_fraction(value: Fraction, prime: int) -> int:
    return vp_int(value.numerator, prime) - vp_int(value.denominator, prime)


def gamma_ratio_value(n: int) -> Fraction:
    if n % 2 == 0:
        m = n // 2
        return Fraction(
            factorial(30 * m) * factorial(5 * m) * factorial(4 * m),
            factorial(15 * m)
            * factorial(12 * m)
            * factorial(10 * m)
            * factorial(2 * m),
        )
    m = (n - 1) // 2
    return Fraction(
        2 ** (20 * m + 10) * factorial(15 * m + 7) * factorial(4 * m + 2),
        factorial(5 * m + 2)
        * factorial(12 * m + 6)
        * factorial(2 * m + 1),
    )


def odd_core(m: int) -> Fraction:
    return Fraction(
        factorial(15 * m + 7) * factorial(4 * m + 2),
        factorial(5 * m + 2)
        * factorial(12 * m + 6)
        * factorial(2 * m + 1),
    )


def floor_defect(m: int, d: int) -> int:
    return (
        (15 * m + 7) // d
        + (4 * m + 2) // d
        - (5 * m + 2) // d
        - (12 * m + 6) // d
        - (2 * m + 1) // d
    )


def reduced_floor_defect(q: int, alpha: Fraction) -> int:
    y = Fraction(2 * q, 5) + alpha / 5
    return (
        2 * q
        + (3 * alpha // 2)
        + (2 * y // 1)
        - (6 * y // 1)
        - (y // 1)
    )


def table_value(q: int, alpha: Fraction) -> int:
    intervals = {
        0: (
            (Fraction(2, 3), Fraction(5, 6), True),
            (Fraction(4, 3), Fraction(5, 3), True),
        ),
        1: ((Fraction(2, 3), Fraction(2), True),),
        2: (
            (Fraction(0), Fraction(1, 6), False),
            (Fraction(2, 3), Fraction(1), True),
            (Fraction(4, 3), Fraction(11, 6), True),
        ),
        3: ((Fraction(4, 3), Fraction(2), True),),
        4: (
            (Fraction(0), Fraction(1, 3), False),
            (Fraction(2, 3), Fraction(7, 6), True),
            (Fraction(4, 3), Fraction(2), True),
        ),
    }
    return int(
        any(
            (left <= alpha if closed_left else left < alpha) and alpha < right
            for left, right, closed_left in intervals[q]
        )
    )


def legendre_core_valuation(m: int, prime: int) -> int:
    total = 0
    power = prime
    while power <= 15 * m + 7:
        total += floor_defect(m, power)
        power *= prime
    return total


def check_initial_values() -> int:
    expected = (
        1,
        7168,
        168043980,
        4488240824320,
        126694219977836700,
        3688258943632086663168,
        109504706026534324525391988,
        3295939064766794222800490987520,
        100204869963549181630558779565943580,
        3070025447039504554088467623457608171520,
        94632263448378916462441320194245442445186480,
    )
    assert tuple(gamma_ratio_value(n) for n in range(len(expected))) == expected
    return len(expected)


def check_floor_reduction() -> int:
    checks = 0
    for d in range(2, 501):
        for m in range(d):
            q, residue = divmod(5 * m + 2, d)
            assert 0 <= q <= 4
            alpha = Fraction(2 * residue + 1, d)
            assert 0 < alpha < 2
            direct = floor_defect(m, d)
            reduced = reduced_floor_defect(q, alpha)
            assert direct == reduced == table_value(q, alpha)
            assert direct in (0, 1)
            assert floor_defect(m + d, d) == direct
            checks += 4
    return checks


def check_integrality_and_legendre() -> int:
    checks = 0
    for n in range(151):
        assert gamma_ratio_value(n).denominator == 1
        checks += 1
    for m in range(81):
        core = odd_core(m)
        assert core.denominator == 1
        checks += 1
        for prime in (2, 3, 5, 7, 11, 13, 17, 19):
            assert vp_fraction(core, prime) == legendre_core_valuation(m, prime)
            checks += 1
    return checks


def check_cubic_tower() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for r, n_max in ((1, 5), (2, 2)):
            for n in range(1, n_max + 1):
                high = gamma_ratio_value(n * prime**r)
                low = gamma_ratio_value(n * prime ** (r - 1))
                assert high.denominator == low.denominator == 1
                assert vp_fraction(high - low, prime) >= 3 * r
                checks += 1
    return checks


def main() -> None:
    sections = {
        "OEIS initial values": check_initial_values(),
        "affine floor reduction": check_floor_reduction(),
        "integrality and Legendre identity": check_integrality_and_legendre(),
        "A364176 cubic towers": check_cubic_tower(),
    }
    print(f"A364176 checks passed: {sum(sections.values())}")
    for name, count in sections.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
