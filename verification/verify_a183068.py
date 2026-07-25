"""Exact regression checks for the A183068 supercongruence.

This script is evidence, not a replacement for the proof in ../PROOF.md.
It uses only Python integers and the standard library.
"""

from functools import cache
from math import comb


@cache
def a(n: int) -> int:
    """Return A183068(n) using an exact recurrence between summands."""
    if n < 0:
        raise ValueError("n must be nonnegative")

    term = comb(2 * n, n)
    total = term

    for k in range(n):
        numerator = (
            term
            * (2 * n + 2 * k + 2)
            * (2 * n + 2 * k + 1)
            * (n - k) ** 2
        )
        denominator = (k + 1) ** 4
        term, remainder = divmod(numerator, denominator)
        assert remainder == 0
        total += term

    return total


def cases() -> list[tuple[int, int, int]]:
    """The 80 base checks and 25 additional r=3 checks."""
    result = [
        (p, r, n)
        for p in (2, 3, 5, 7, 11)
        for r in (1, 2)
        for n in range(1, 9)
    ]
    result.extend(
        (p, 3, n)
        for p in (2, 3, 5)
        for n in range(1, 9)
    )
    result.append((7, 3, 1))
    assert len(result) == 105
    return result


def main() -> None:
    known = (1, 26, 3246, 606500, 137915470, 35218238076)
    assert tuple(a(n) for n in range(len(known))) == known

    for p, r, n in cases():
        difference = a(n * p**r) - a(n * p ** (r - 1))
        assert difference % p ** (2 * r) == 0, (p, r, n)

    print("known OEIS terms: 6")
    print("supercongruence cases: 105")
    print("all exact checks passed")


if __name__ == "__main__":
    main()

