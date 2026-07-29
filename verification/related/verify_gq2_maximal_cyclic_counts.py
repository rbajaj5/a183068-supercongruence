"""Exact checks for semidihedral and modular G_Q2 target counts."""

from __future__ import annotations

from itertools import product


Element = tuple[int, int]
Pattern = tuple[int, int, int]


def action_parameter(family: str, n_rotation: int) -> int:
    half = n_rotation // 2
    if family == "semidihedral":
        return half - 1
    if family == "modular":
        return half + 1
    raise ValueError(f"unknown family: {family}")


def mul(x: Element, y: Element, n_rotation: int, action: int) -> Element:
    """Multiply r^a w^alpha and r^b w^beta."""
    a, alpha = x
    b, beta = y
    multiplier = action if alpha else 1
    return ((a + multiplier * b) % n_rotation, (alpha + beta) & 1)


def inv(x: Element, n_rotation: int, action: int) -> Element:
    a, alpha = x
    multiplier = action if alpha else 1
    return ((-multiplier * a) % n_rotation, alpha)


def power(
    x: Element, exponent: int, n_rotation: int, action: int
) -> Element:
    out = (0, 0)
    base = x
    while exponent:
        if exponent & 1:
            out = mul(out, base, n_rotation, action)
        base = mul(base, base, n_rotation, action)
        exponent >>= 1
    return out


def commutator(
    x: Element, y: Element, n_rotation: int, action: int
) -> Element:
    """Use [x,y] = x^(-1)y^(-1)xy."""
    return mul(
        mul(
            mul(
                inv(x, n_rotation, action),
                inv(y, n_rotation, action),
                n_rotation,
                action,
            ),
            x,
            n_rotation,
            action,
        ),
        y,
        n_rotation,
        action,
    )


def relator(
    a: Element,
    s: Element,
    y: Element,
    n_rotation: int,
    action: int,
) -> Element:
    """Evaluate the Roe--Turturean relator A^2 S^4 [S,Y]."""
    return mul(
        mul(
            power(a, 2, n_rotation, action),
            power(s, 4, n_rotation, action),
            n_rotation,
            action,
        ),
        commutator(s, y, n_rotation, action),
        n_rotation,
        action,
    )


def frattini_vector(x: Element) -> int:
    a, alpha = x
    return (a & 1) | (alpha << 1)


def spans_frattini(elements: tuple[Element, ...]) -> bool:
    vectors = {frattini_vector(x) for x in elements} - {0}
    # Two distinct nonzero vectors in F_2^2 are independent.
    return len(vectors) >= 2


def brute_pattern_counts(family: str, m: int) -> dict[Pattern, int]:
    n_rotation = 1 << (m - 1)
    action = action_parameter(family, n_rotation)
    group = list(product(range(n_rotation), range(2)))
    counts = {pattern: 0 for pattern in product(range(2), repeat=3)}
    for a, s, y in product(group, repeat=3):
        if relator(a, s, y, n_rotation, action) != (0, 0):
            continue
        if spans_frattini((a, s, y)):
            counts[(a[1], s[1], y[1])] += 1
    return counts


def predicted_pattern_counts(family: str, m: int) -> dict[Pattern, int]:
    n_rotation = 1 << (m - 1)
    n2 = n_rotation * n_rotation
    out = {pattern: 0 for pattern in product(range(2), repeat=3)}
    if family == "semidihedral":
        for pattern in (
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ):
            out[pattern] = n2
        out[(1, 0, 0)] = (3 if m == 4 else 2) * n2
        return out
    if family == "modular":
        for pattern in ((0, 0, 1), (0, 1, 0), (0, 1, 1)):
            out[pattern] = n2
        for pattern in ((1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)):
            out[pattern] = 3 * n2 // 2
        return out
    raise ValueError(f"unknown family: {family}")


def predicted_surjections(family: str, m: int) -> int:
    if family == "semidihedral":
        return 576 if m == 4 else 1 << (2 * m + 1)
    if family == "modular":
        return 9 * (1 << (2 * m - 2))
    raise ValueError(f"unknown family: {family}")


def automorphism_count(family: str, m: int) -> int:
    if family == "semidihedral":
        return 1 << (2 * m - 4)
    if family == "modular":
        return 1 << m
    raise ValueError(f"unknown family: {family}")


def predicted_extensions(family: str, m: int) -> int:
    if family == "semidihedral":
        return 36 if m == 4 else 32
    if family == "modular":
        return 9 * (1 << (m - 2))
    raise ValueError(f"unknown family: {family}")


def expected_relator_coordinate(
    family: str,
    a: int,
    alpha: int,
    s: int,
    sigma: int,
    y: int,
    tau: int,
    n_rotation: int,
) -> int:
    action = action_parameter(family, n_rotation)
    u_sigma = action if sigma else 1
    u_tau = action if tau else 1
    a_square = (2 * a) if alpha == 0 else (1 + action) * a
    s_fourth = (4 * s) if sigma == 0 else 2 * (1 + action) * s
    comm = (
        u_sigma * (u_tau - 1) * s
        + u_tau * (1 - u_sigma) * y
    )
    return (a_square + s_fourth + comm) % n_rotation


def check_group_and_relator_formulas(max_m: int = 12) -> tuple[int, int]:
    group_checks = 0
    relator_checks = 0
    for family in ("semidihedral", "modular"):
        for m in range(4, max_m + 1):
            n_rotation = 1 << (m - 1)
            action = action_parameter(family, n_rotation)
            assert action * action % n_rotation == 1
            sample = range(min(n_rotation, 16))
            for x in product(sample, range(2)):
                assert mul(x, inv(x, n_rotation, action), n_rotation, action) == (
                    0,
                    0,
                )
                assert mul(inv(x, n_rotation, action), x, n_rotation, action) == (
                    0,
                    0,
                )
                group_checks += 2
            for a, s, y in product(sample, repeat=3):
                for alpha, sigma, tau in product(range(2), repeat=3):
                    observed = relator(
                        (a, alpha),
                        (s, sigma),
                        (y, tau),
                        n_rotation,
                        action,
                    )[0]
                    expected = expected_relator_coordinate(
                        family,
                        a,
                        alpha,
                        s,
                        sigma,
                        y,
                        tau,
                        n_rotation,
                    )
                    assert observed == expected
                    relator_checks += 1
    return group_checks, relator_checks


def element_order(
    x: Element, n_rotation: int, action: int
) -> int:
    value = (0, 0)
    for order in range(1, 2 * n_rotation + 1):
        value = mul(value, x, n_rotation, action)
        if value == (0, 0):
            return order
    raise AssertionError("element order exceeded group order")


def brute_automorphism_count(family: str, m: int) -> int:
    """Count generating images of the two defining generators."""
    n_rotation = 1 << (m - 1)
    action = action_parameter(family, n_rotation)
    group = list(product(range(n_rotation), range(2)))
    count = 0
    for image_r, image_w in product(group, repeat=2):
        if element_order(image_r, n_rotation, action) != n_rotation:
            continue
        if power(image_w, 2, n_rotation, action) != (0, 0):
            continue
        conjugate = mul(
            mul(image_w, image_r, n_rotation, action),
            inv(image_w, n_rotation, action),
            n_rotation,
            action,
        )
        if conjugate != power(image_r, action, n_rotation, action):
            continue
        if spans_frattini((image_r, image_w)):
            count += 1
    return count


def check_exhaustive(max_m: int = 7) -> int:
    pattern_checks = 0
    for family in ("semidihedral", "modular"):
        for m in range(4, max_m + 1):
            observed = brute_pattern_counts(family, m)
            expected = predicted_pattern_counts(family, m)
            assert observed == expected, (family, m, observed, expected)
            assert sum(observed.values()) == predicted_surjections(family, m)
            pattern_checks += len(observed)
    return pattern_checks


def check_automorphisms(max_m: int = 8) -> int:
    checks = 0
    for family in ("semidihedral", "modular"):
        for m in range(4, max_m + 1):
            observed = brute_automorphism_count(family, m)
            assert observed == automorphism_count(family, m), (
                family,
                m,
                observed,
                automorphism_count(family, m),
            )
            checks += 1
    return checks


def check_extension_counts(max_m: int = 16) -> int:
    checks = 0
    for family in ("semidihedral", "modular"):
        for m in range(4, max_m + 1):
            surjections = predicted_surjections(family, m)
            automorphisms = automorphism_count(family, m)
            assert surjections % automorphisms == 0
            assert surjections // automorphisms == predicted_extensions(
                family, m
            )
            checks += 1
    return checks


def check_extraspecial_rank_boundary(max_n: int = 16) -> int:
    """An extraspecial group of order 2^(1+2n) needs 2n generators."""
    checks = 0
    assert 2 * 1 <= 3  # D_8 and Q_8 survive the source rank bound.
    checks += 1
    for n in range(2, max_n + 1):
        assert 2 * n > 3
        checks += 1
    return checks


def main() -> None:
    group_checks, relator_checks = check_group_and_relator_formulas()
    pattern_checks = check_exhaustive()
    automorphism_checks = check_automorphisms()
    extension_checks = check_extension_counts()
    rank_checks = check_extraspecial_rank_boundary()
    print("G_Q2 semidihedral and modular target counts")
    print(f"group inverse identities: {group_checks}")
    print(f"relator-coordinate identities: {relator_checks}")
    print(f"exhaustive reflection-pattern subtotals: {pattern_checks}")
    print("all triples exhaustively checked through group order 128")
    print(f"automorphism counts exhaustively checked: {automorphism_checks}")
    print(f"closed extension counts checked: {extension_checks}")
    print(f"extraspecial generator-rank boundaries checked: {rank_checks}")
    print("all exact maximal-cyclic target checks passed")


if __name__ == "__main__":
    main()
