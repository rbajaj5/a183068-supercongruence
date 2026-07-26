"""Exact certificates for the Dwork and p-adic continuity boundaries."""

from collections import defaultdict
from functools import reduce
from itertools import combinations, product
from math import factorial, gcd


Vector = tuple[int, ...]
Laurent = dict[Vector, int]


def multiply(left: Laurent, right: Laurent) -> Laurent:
    out: defaultdict[Vector, int] = defaultdict(int)
    for a, ca in left.items():
        for b, cb in right.items():
            out[tuple(x + y for x, y in zip(a, b))] += ca * cb
    return dict(out)


def power(base: Laurent, exponent: int) -> Laurent:
    dimension = len(next(iter(base)))
    out: Laurent = {(0,) * dimension: 1}
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def cross(a: Vector, b: Vector) -> Vector:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def subtract(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))


def dot(a: Vector, b: Vector) -> int:
    return sum(x * y for x, y in zip(a, b))


def supporting_facets(points: set[Vector]) -> set[tuple[int, int, int, int]]:
    """Return primitive inequalities n dot x <= c for a three-polytope."""
    facets: set[tuple[int, int, int, int]] = set()
    for a, b, c in combinations(sorted(points), 3):
        normal = cross(subtract(b, a), subtract(c, a))
        if normal == (0, 0, 0):
            continue
        constant = dot(normal, a)
        values = [dot(normal, point) - constant for point in points]
        if not (all(value <= 0 for value in values)
                or all(value >= 0 for value in values)):
            continue
        if all(value >= 0 for value in values):
            normal = tuple(-entry for entry in normal)
            constant = -constant
        divisor = reduce(
            gcd,
            [abs(entry) for entry in (*normal, constant) if entry],
        )
        primitive = tuple(entry // divisor for entry in normal)
        facets.add((*primitive, constant // divisor))
    return facets


def a183068_polynomial() -> Laurent:
    """Expand the factored Laurent polynomial from PROOF.md."""
    factors: list[Laurent] = [
        {(-1, 0, 0, 0): 1, (0, 0, 0, 0): 2, (1, 0, 0, 0): 1},
        {(0, 0, 0, 0): 1, (0, 0, 1, 0): 2, (0, 0, 2, 0): 1},
        {(0, 0, 0, 0): 1, (0, 1, 0, 0): 1},
    ]
    last: Laurent = {(0, 0, 0, 0): 1}
    for y, cy in enumerate((1, 2, 1)):
        for z, cz in enumerate((1, 2, 1)):
            last[(0, -1, y - 2, z - 1)] = cy * cz
    factors.append(last)

    out: Laurent = {(0, 0, 0, 0): 1}
    for factor in factors:
        out = multiply(out, factor)
    return out


def check_newton_polytope() -> None:
    polynomial = a183068_polynomial()
    assert len(polynomial) == 99
    points = {exponent[1:] for exponent in polynomial}

    expected_facets = {
        (-1, 0, 0, 1),
        (0, -1, 0, 2),
        (0, 0, -1, 1),
        (0, 0, 1, 1),
        (0, 1, 0, 2),
        (1, 0, -1, 1),
        (1, 0, 1, 1),
        (2, -1, 0, 2),
    }
    assert supporting_facets(points) == expected_facets

    interior: list[Vector] = []
    for point in product(range(-1, 2), range(-2, 3), range(-1, 2)):
        if all(dot(facet[:3], point) < facet[3]
               for facet in expected_facets):
            interior.append(point)
    assert interior == [(0, -1, 0), (0, 0, 0), (0, 1, 0)]


def check_rank_one_counterexample() -> None:
    """Unique interior point does not force the rank-one pairing."""
    lam: Laurent = {(-1,): 2, (0,): 1, (1,): 1}
    p = 3
    lam_p = power(lam, p)
    frobenius = {(p * exponent[0],): coefficient
                 for exponent, coefficient in lam.items()}
    keys = set(lam_p) | set(frobenius)
    quotient: Laurent = {}
    for exponent in keys:
        difference = lam_p.get(exponent, 0) - frobenius.get(exponent, 0)
        assert difference % p == 0
        if difference:
            quotient[exponent] = difference // p

    assert quotient == {
        (-3,): 2,
        (-2,): 4,
        (-1,): 6,
        (0,): 4,
        (1,): 3,
        (2,): 1,
    }
    pairing = multiply(frobenius, quotient).get((0,), 0)
    scalar_pairing = lam[(0,)] * quotient[(0,)]
    assert pairing == 6
    assert scalar_pairing == 4
    assert pairing % p != scalar_pairing % p


def a183068(n: int) -> int:
    return sum(
        factorial(2 * n + 2 * k)
        // (factorial(k) ** 4 * factorial(n - k) ** 2)
        for k in range(n + 1)
    )


def valuation(value: int, prime: int) -> int:
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def check_continuity_obstruction() -> None:
    assert a183068(0) == 1
    assert a183068(1) == 26
    a5 = a183068(5)
    assert a5 == 35_218_238_076
    assert valuation(a5 - 1, 5) == 2


def main() -> None:
    check_newton_polytope()
    check_rank_one_counterexample()
    check_continuity_obstruction()
    print("Dwork boundary certificates passed")
    print("  A183068 Newton-polytope interior lattice points: 3")
    print("  unique-interior rank-one counterexample: p=3, pairings 6 and 4")
    print("  A183068 p=5 continuity witness: v_5(a(5)-1)=2")


if __name__ == "__main__":
    main()
