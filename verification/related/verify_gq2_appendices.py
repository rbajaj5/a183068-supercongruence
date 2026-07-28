#!/usr/bin/env python3
"""Independent exact checks for Roe--Turturean Appendices C and D.

This script checks only finite or symbolic calculations.  It is not a
verification of the paper's profinite classification theorem.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product


Permutation = tuple[int, ...]


def identity(n: int) -> Permutation:
    return tuple(range(n))


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left * right, with right applied first."""
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(g: Permutation) -> Permutation:
    result = [0] * len(g)
    for i, image in enumerate(g):
        result[image] = i
    return tuple(result)


def power(g: Permutation, exponent: int) -> Permutation:
    if exponent < 0:
        return power(inverse(g), -exponent)
    result = identity(len(g))
    base = g
    while exponent:
        if exponent & 1:
            result = compose(result, base)
        base = compose(base, base)
        exponent >>= 1
    return result


def conjugate(x: Permutation, g: Permutation) -> Permutation:
    """The paper's right-conjugation convention x^g = g^-1 x g."""
    return compose(compose(inverse(g), x), g)


def commutator(x: Permutation, y: Permutation) -> Permutation:
    """The paper's convention [x,y] = x^-1 y^-1 x y."""
    return compose(compose(compose(inverse(x), inverse(y)), x), y)


def generated_subgroup(generators: tuple[Permutation, ...]) -> set[Permutation]:
    n = len(generators[0])
    one = identity(n)
    subgroup = {one}
    frontier = [one]
    steps = generators + tuple(inverse(g) for g in generators)
    while frontier:
        current = frontier.pop()
        for step in steps:
            candidate = compose(current, step)
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return subgroup


OMEGA_TWO_EXPONENT = 40_491_355_905


def tame_relation(sigma: Permutation, tau: Permutation) -> bool:
    return conjugate(tau, sigma) == power(tau, 2)


def wild_relation(
    sigma: Permutation,
    tau: Permutation,
    x0: Permutation,
    x1: Permutation,
) -> bool:
    sigma2 = power(sigma, OMEGA_TWO_EXPONENT)
    g0 = power(sigma2, 2)
    u0 = power(compose(x0, tau), OMEGA_TWO_EXPONENT)
    u1 = power(compose(x1, tau), OMEGA_TWO_EXPONENT)
    d0 = compose(u0, inverse(x0))
    z0 = conjugate(x0, sigma2)
    c0 = commutator(d0, z0)
    dg = conjugate(d0, g0)
    hc = commutator(dg, d0)
    h0 = identity(len(sigma))
    for factor in (
        conjugate(x0, g0),
        x0,
        dg,
        d0,
        power(d0, 2),
        hc,
    ):
        h0 = compose(h0, factor)
    relator = compose(
        compose(compose(h0, inverse(u1)), conjugate(x1, sigma)),
        c0,
    )
    return relator == identity(len(sigma))


def symmetric_group(n: int) -> tuple[Permutation, ...]:
    return tuple(permutations(range(n)))


def double_transpositions_s4() -> tuple[Permutation, ...]:
    one = identity(4)
    values = [one]
    for pairing in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))):
        p = list(one)
        for a, b in pairing:
            p[a], p[b] = p[b], p[a]
        values.append(tuple(p))
    return tuple(values)


def count_admissible_surjections(
    group: tuple[Permutation, ...],
    o2: tuple[Permutation, ...],
) -> tuple[int, int]:
    admissible = 0
    surjective = 0
    order = len(group)
    for sigma, tau, x0, x1 in product(group, group, o2, o2):
        if not tame_relation(sigma, tau):
            continue
        if not wild_relation(sigma, tau, x0, x1):
            continue
        admissible += 1
        if len(generated_subgroup((sigma, tau, x0, x1))) == order:
            surjective += 1
    return admissible, surjective


def trim(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def add_poly(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    length = max(len(left), len(right))
    return trim(
        tuple(
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(length)
        )
    )


def mul_poly(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    values = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            values[i + j] += a * b
    return trim(tuple(values))


def reduce_cubic(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    """Reduce modulo X^3 + 2 X^2 + 1."""
    values = list(poly)
    while len(values) > 3:
        degree = len(values) - 1
        coefficient = values.pop()
        if coefficient:
            # X^degree = -2 X^(degree-1) - X^(degree-3).
            values[degree - 1] -= 2 * coefficient
            values[degree - 3] -= coefficient
    while len(values) < 3:
        values.append(Fraction(0))
    return tuple(values)


def mul_cubic(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return reduce_cubic(mul_poly(left, right))


def determinant_3(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def norm_cubic(element: tuple[Fraction, ...]) -> Fraction:
    basis = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    columns = tuple(mul_cubic(element, vector) for vector in basis)
    matrix = tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
    return determinant_3(matrix)


def invert_cubic(element: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    # Solve element * (a + bX + cX^2) = 1 by exact Gaussian elimination.
    basis = (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    columns = tuple(mul_cubic(element, vector) for vector in basis)
    rows = [
        [columns[j][i] for j in range(3)] + [Fraction(int(i == 0))]
        for i in range(3)
    ]
    for col in range(3):
        pivot = next(row for row in range(col, 3) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [value / scale for value in rows[col]]
        for row in range(3):
            if row == col:
                continue
            scale = rows[row][col]
            rows[row] = [
                rows[row][j] - scale * rows[col][j] for j in range(4)
            ]
    return tuple(rows[i][3] for i in range(3))


def hensel_root_mod_power_of_two(bits: int) -> int:
    root = 1
    modulus = 2
    for _ in range(1, bits):
        next_modulus = modulus * 2
        candidates = (root, root + modulus)
        root = next(
            candidate
            for candidate in candidates
            if (candidate**3 + 2 * candidate**2 + 1) % next_modulus == 0
        )
        modulus = next_modulus
    return root


def check_orientation_algebra() -> None:
    one = (Fraction(1), Fraction(0), Fraction(0))
    x = (Fraction(0), Fraction(1), Fraction(0))
    x2 = mul_cubic(x, x)
    denominator = add_poly(add_poly(x2, x), one)
    minus_x3 = tuple(-value for value in mul_cubic(x2, x))
    s = mul_cubic(minus_x3, invert_cubic(denominator))
    y = tuple(-value for value in x2)

    root16 = hensel_root_mod_power_of_two(4)
    denominator16 = (root16 * root16 + root16 + 1) % 16
    s16 = (
        (-pow(root16, 3, 16)) * pow(denominator16, -1, 16)
    ) % 16

    assert root16 == 5
    assert s16 == 13
    assert norm_cubic(x) == -1
    assert norm_cubic(s) == Fraction(1, 4)
    assert norm_cubic(y) == -1
    print(
        "Appendix C.10: X=5 mod 16, S=13 mod 16, "
        "Norm(X)=-1, Norm(S)=1/4, Norm(Y)=-1"
    )


def check_small_targets() -> None:
    s3 = symmetric_group(3)
    s4 = symmetric_group(4)
    s3_counts = count_admissible_surjections(s3, (identity(3),))
    s4_counts = count_admissible_surjections(s4, double_transpositions_s4())
    assert s3_counts[1] == 6
    assert s4_counts[1] == 72
    print(
        "Appendix D.2: "
        f"{s3_counts[0]} admissible quadruples, {s3_counts[1]} surjective"
    )
    print(
        "Appendix D.3: "
        f"{s4_counts[0]} admissible quadruples, {s4_counts[1]} surjective"
    )


def main() -> None:
    check_orientation_algebra()
    check_small_targets()
    print("All exact Appendix C--D checks passed.")


if __name__ == "__main__":
    main()
