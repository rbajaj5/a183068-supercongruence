"""Exact checks for G_Q2 surjections onto generalized quaternion 2-groups."""

from __future__ import annotations

from itertools import product


Element = tuple[int, int]
Pattern = tuple[int, int, int]


def mul(x: Element, y: Element, n_rotation: int) -> Element:
    """Multiply r^a w^alpha and r^b w^beta in Q_(2^m)."""
    a, alpha = x
    b, beta = y
    signed_b = -b if alpha else b
    central_square = (n_rotation // 2) if alpha and beta else 0
    return (
        (a + signed_b + central_square) % n_rotation,
        (alpha + beta) & 1,
    )


def inv(x: Element, n_rotation: int) -> Element:
    a, alpha = x
    if alpha:
        return ((a + n_rotation // 2) % n_rotation, 1)
    return ((-a) % n_rotation, 0)


def power(x: Element, exponent: int, n_rotation: int) -> Element:
    out = (0, 0)
    for _ in range(exponent):
        out = mul(out, x, n_rotation)
    return out


def commutator(x: Element, y: Element, n_rotation: int) -> Element:
    """Use [x,y] = x^(-1)y^(-1)xy."""
    return mul(
        mul(
            mul(inv(x, n_rotation), inv(y, n_rotation), n_rotation),
            x,
            n_rotation,
        ),
        y,
        n_rotation,
    )


def relator(a: Element, s: Element, y: Element, n_rotation: int) -> Element:
    """Evaluate A^2 S^4 [S,Y]."""
    return mul(
        mul(power(a, 2, n_rotation), power(s, 4, n_rotation), n_rotation),
        commutator(s, y, n_rotation),
        n_rotation,
    )


def frattini_vector(x: Element) -> int:
    a, alpha = x
    return (a & 1) | (alpha << 1)


def spans_frattini(elements: tuple[Element, ...]) -> bool:
    vectors = {frattini_vector(x) for x in elements} - {0}
    # Two distinct nonzero vectors in F_2^2 are independent.
    return len(vectors) >= 2


def brute_pattern_counts(n_rotation: int) -> dict[Pattern, int]:
    group = list(product(range(n_rotation), range(2)))
    counts = {pattern: 0 for pattern in product(range(2), repeat=3)}
    for a, s, y in product(group, repeat=3):
        if relator(a, s, y, n_rotation) != (0, 0):
            continue
        if not spans_frattini((a, s, y)):
            continue
        counts[(a[1], s[1], y[1])] += 1
    return counts


def predicted_pattern_counts(m: int) -> dict[Pattern, int]:
    n_rotation = 1 << (m - 1)
    n2 = n_rotation * n_rotation
    out = {pattern: 0 for pattern in product(range(2), repeat=3)}

    for pattern in ((0, 0, 1), (0, 1, 0), (0, 1, 1)):
        out[pattern] = n2

    if m == 3:
        out[(1, 0, 0)] = 0
        for pattern in ((1, 0, 1), (1, 1, 0), (1, 1, 1)):
            out[pattern] = 2 * n2
    elif m == 4:
        out[(1, 0, 0)] = 4 * n2
        for pattern in ((1, 0, 1), (1, 1, 0), (1, 1, 1)):
            out[pattern] = n2
    else:
        out[(1, 0, 0)] = 2 * n2
        for pattern in ((1, 0, 1), (1, 1, 0), (1, 1, 1)):
            out[pattern] = n2

    return out


def predicted_surjections(m: int) -> int:
    if m == 3:
        return 144
    if m == 4:
        return 640
    return 1 << (2 * m + 1)


def automorphism_count(m: int) -> int:
    # Q_8 is exceptional: Aut(Q_8) is isomorphic to S_4.
    if m == 3:
        return 24
    return 1 << (2 * m - 3)


def predicted_extensions(m: int) -> int:
    if m == 3:
        return 6
    if m == 4:
        return 20
    return 16


def expected_relator_coordinate(
    a: int,
    alpha: int,
    s: int,
    sigma: int,
    y: int,
    tau: int,
    n_rotation: int,
) -> int:
    a_square = 2 * a if alpha == 0 else n_rotation // 2
    s_fourth = 4 * s if sigma == 0 else 0
    comm = (
        ((-1) ** sigma) * (((-1) ** tau) - 1) * s
        + ((-1) ** tau) * (1 - ((-1) ** sigma)) * y
    )
    return (a_square + s_fourth + comm) % n_rotation


def check_relator_formula(max_m: int = 12) -> int:
    checks = 0
    for m in range(3, max_m + 1):
        n_rotation = 1 << (m - 1)
        sample_coordinates = range(min(n_rotation, 16))
        for a, s, y in product(sample_coordinates, repeat=3):
            for alpha, sigma, tau in product(range(2), repeat=3):
                observed = relator(
                    (a, alpha), (s, sigma), (y, tau), n_rotation
                )[0]
                expected = expected_relator_coordinate(
                    a, alpha, s, sigma, y, tau, n_rotation
                )
                assert observed == expected
                checks += 1
    return checks


def check_inverse_law(max_m: int = 12) -> int:
    checks = 0
    for m in range(3, max_m + 1):
        n_rotation = 1 << (m - 1)
        for x in product(range(n_rotation), range(2)):
            assert mul(x, inv(x, n_rotation), n_rotation) == (0, 0)
            assert mul(inv(x, n_rotation), x, n_rotation) == (0, 0)
            checks += 2
    return checks


def check_exhaustive(max_m: int = 7) -> int:
    total_patterns = 0
    for m in range(3, max_m + 1):
        n_rotation = 1 << (m - 1)
        observed = brute_pattern_counts(n_rotation)
        expected = predicted_pattern_counts(m)
        assert observed == expected, (m, observed, expected)
        assert sum(observed.values()) == predicted_surjections(m)
        total_patterns += len(observed)
    return total_patterns


def check_extension_counts(max_m: int = 16) -> int:
    checks = 0
    for m in range(3, max_m + 1):
        surjections = predicted_surjections(m)
        automorphisms = automorphism_count(m)
        assert surjections % automorphisms == 0
        assert surjections // automorphisms == predicted_extensions(m)
        checks += 1
    return checks


def main() -> None:
    inverse_checks = check_inverse_law()
    relator_checks = check_relator_formula()
    pattern_checks = check_exhaustive()
    extension_checks = check_extension_counts()
    print("G_Q2 generalized-quaternion target counts")
    print(f"group inverse identities: {inverse_checks}")
    print(f"relator-coordinate identities: {relator_checks}")
    print(f"exhaustive reflection-pattern subtotals: {pattern_checks}")
    print("all triples exhaustively checked through Q_128")
    print(f"closed extension counts checked: {extension_checks}")
    print("all exact generalized-quaternion target checks passed")


if __name__ == "__main__":
    main()
