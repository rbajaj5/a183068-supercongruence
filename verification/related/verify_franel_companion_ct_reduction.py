"""Exact checks for the Franel-companion constant-term reduction.

The computation validates identities and searches finite parameter boxes.
It is not a proof of the conjectural cubic Cartier contraction.
"""

from __future__ import annotations

from collections import defaultdict
from math import comb


Laurent = dict[tuple[int, int], int]


def zbinom(n: int, k: int) -> int:
    """Generalized binomial coefficient for integer n and k >= 0."""
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


def w(a: int, m: int, n: int) -> int:
    return sum(
        (-4) ** (n - k)
        * comb(n, k)
        * zbinom(m * n + a * k, a * k)
        * comb(2 * k, k)
        for k in range(n + 1)
    )


def a362676(n: int) -> int:
    return sum(
        4 ** (n - k) * comb(n, k) * zbinom(n - 1, k) * comb(2 * k, k)
        for k in range(n + 1)
    )


def franel(n: int) -> int:
    return sum(comb(n, k) ** 3 for k in range(n + 1))


def multiply(left: Laurent, right: Laurent) -> Laurent:
    out: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (i, j), c in left.items():
        for (u, v), d in right.items():
            out[i + u, j + v] += c * d
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def power(base: Laurent, exponent: int) -> Laurent:
    out: Laurent = {(0, 0): 1}
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        exponent >>= 1
        if exponent:
            base = multiply(base, base)
    return out


def kernel(a: int, m: int) -> Laurent:
    """P_(a,m) as a finite Laurent dictionary; requires m >= 0."""
    assert a in (1, 2) and m >= 0
    y_factor = {(j, 0): comb(m, j) for j in range(m + 1)}
    bracket: defaultdict[tuple[int, int], int] = defaultdict(int)
    for i in range(a + 1):
        for j in range(3):
            bracket[i - a, j - 1] += comb(a, i) * comb(2, j)
    bracket[0, 0] -= 4
    return multiply(y_factor, dict(bracket))


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    result = 0
    while value % prime == 0:
        value //= prime
        result += 1
    return result


def check_constant_terms() -> int:
    checks = 0
    for a in (1, 2):
        for m in range(5):
            base = kernel(a, m)
            for n in range(7):
                assert power(base, n).get((0, 0), 0) == w(a, m, n)
                checks += 1
    return checks


def check_specializations() -> int:
    checks = 0
    for n in range(31):
        assert w(1, -1, n) == (-1) ** n * a362676(n)
        assert w(1, 0, n) == (-1) ** n * comb(2 * n, n)
        assert w(2, 0, n) == (-1) ** n * comb(2 * n, n)
        assert w(2, 1, n) == franel(n)
        checks += 4
    return checks


def check_towers() -> tuple[int, int, int]:
    checks = 0
    sharp = 0
    minimum_excess = 10**9
    for a in (1, 2):
        for m in range(-8, 9):
            for prime in (5, 7, 11, 13):
                for n in range(1, 5):
                    for r in (1, 2):
                        delta = w(a, m, n * prime**r) - w(
                            a, m, n * prime ** (r - 1)
                        )
                        valuation = vp(delta, prime)
                        assert valuation >= 3 * r, (a, m, prime, n, r, valuation)
                        if valuation == 3 * r:
                            sharp += 1
                        minimum_excess = min(minimum_excess, valuation - 3 * r)
                        checks += 1
    return checks, sharp, minimum_excess


def main() -> None:
    ct_checks = check_constant_terms()
    specialization_checks = check_specializations()
    tower_checks, sharp, minimum_excess = check_towers()
    print("Franel-companion constant-term reduction passed")
    print(f"independent Laurent constant-term checks: {ct_checks}")
    print(f"named-specialization checks: {specialization_checks}")
    print(f"exact conjectural tower checks: {tower_checks}")
    print(f"sharp tower instances: {sharp}")
    print(f"minimum valuation excess: {minimum_excess}")


if __name__ == "__main__":
    main()
