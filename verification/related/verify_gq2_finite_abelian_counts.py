"""Exact checks for the finite-abelian-target G_Q2 surjection formula."""

from __future__ import annotations

from itertools import product


def partitions(n: int, largest: int | None = None) -> list[tuple[int, ...]]:
    """Partitions of n in nonincreasing order."""
    if n == 0:
        return [()]
    if largest is None or largest > n:
        largest = n
    out: list[tuple[int, ...]] = []
    for first in range(largest, 0, -1):
        for rest in partitions(n - first, first):
            out.append((first, *rest))
    return out


def residual_parameters(lambdas: tuple[int, ...]) -> tuple[int, int, int, int]:
    """Return e, h, d and |2H| for the invariant factors."""
    e = sum(lam == 1 for lam in lambdas)
    h = sum(lam >= 2 for lam in lambdas)
    d = e + h
    twice_order = 1 << sum(max(lam - 1, 0) for lam in lambdas)
    return e, h, d, twice_order


def spanning_pair_count(d: int) -> int:
    if d > 2:
        return 0
    out = 1
    for i in range(d):
        out *= 4 - (1 << i)
    return out


def formula(lambdas: tuple[int, ...]) -> int:
    e, h, d, twice_order = residual_parameters(lambdas)
    pair = spanning_pair_count(d)
    quotient_pair = spanning_pair_count(d - 1) if d >= 1 else 0
    residual = pair + ((1 << e) - 1) * 4 * quotient_pair
    return twice_order * twice_order * (1 << h) * residual


def elements(lambdas: tuple[int, ...]) -> list[tuple[int, ...]]:
    return list(product(*(range(1 << lam) for lam in lambdas)))


def two_torsion(lambdas: tuple[int, ...]) -> list[tuple[int, ...]]:
    coordinates = []
    for lam in lambdas:
        coordinates.append((0, 1 << (lam - 1)))
    return list(product(*coordinates))


def mod_two_vector(x: tuple[int, ...], lambdas: tuple[int, ...]) -> int:
    """Coordinates of x in H/2H, packed as a bit vector."""
    out = 0
    for i, (coordinate, lam) in enumerate(zip(x, lambdas, strict=True)):
        # In Z/2^lam, reduction modulo 2H is parity.
        if coordinate & 1:
            out |= 1 << i
    return out


def gf2_rank(vectors: tuple[int, ...]) -> int:
    basis: dict[int, int] = {}
    for vector in vectors:
        x = vector
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def brute_count(lambdas: tuple[int, ...]) -> int:
    group = elements(lambdas)
    torsion = two_torsion(lambdas)
    d = len(lambdas)
    bars = {x: mod_two_vector(x, lambdas) for x in group}
    total = 0
    for z in torsion:
        bz = bars[z]
        for x in group:
            bx = bars[x]
            for y in group:
                if gf2_rank((bz, bx, bars[y])) == d:
                    total += 1
    return total


def check_all_types(max_log_order: int = 8) -> int:
    checked = 0
    for log_order in range(1, max_log_order + 1):
        for lambdas in partitions(log_order):
            observed = brute_count(lambdas)
            predicted = formula(lambdas)
            assert observed == predicted, (lambdas, observed, predicted)
            checked += 1
    return checked


def check_cyclic() -> None:
    assert formula((1,)) == 7
    for m in range(2, 17):
        assert formula((m,)) == 3 * (1 << (2 * m - 1))


def check_elementary() -> None:
    expected = {1: 7, 2: 42, 3: 168}
    for d, count in expected.items():
        assert formula((1,) * d) == count
    for d in range(4, 9):
        assert formula((1,) * d) == 0


def main() -> None:
    checked = check_all_types()
    check_cyclic()
    check_elementary()
    print("G_Q2 finite abelian target counts")
    print(f"exhaustively checked {checked} invariant-factor types through order 2^8")
    print("cyclic formulas checked through exponent 2^16")
    print("elementary-abelian rank boundary checked through rank 8")
    print("all exact finite-abelian-target checks passed")


if __name__ == "__main__":
    main()
