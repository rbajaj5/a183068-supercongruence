"""Exact checks for G_Q2 surjections onto dihedral 2-groups."""

from __future__ import annotations

from itertools import product


Element = tuple[int, int]


def mul(x: Element, y: Element, n_rotation: int) -> Element:
    a, alpha = x
    b, beta = y
    signed_b = -b if alpha else b
    return ((a + signed_b) % n_rotation, (alpha + beta) & 1)


def inv(x: Element, n_rotation: int) -> Element:
    a, alpha = x
    return ((a if alpha else -a) % n_rotation, alpha)


def power(x: Element, exponent: int, n_rotation: int) -> Element:
    out = (0, 0)
    for _ in range(exponent):
        out = mul(out, x, n_rotation)
    return out


def commutator(x: Element, y: Element, n_rotation: int) -> Element:
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
    return mul(
        mul(power(a, 2, n_rotation), power(s, 4, n_rotation), n_rotation),
        commutator(s, y, n_rotation),
        n_rotation,
    )


def frattini_vector(x: Element) -> int:
    a, alpha = x
    return (a & 1) | (alpha << 1)


def spans_frattini(elements: tuple[Element, ...]) -> bool:
    vectors = {frattini_vector(x) for x in elements}
    nonzero = vectors - {0}
    # In F_2^2, two distinct nonzero vectors are automatically independent.
    return len(nonzero) >= 2


def brute_pattern_counts(n_rotation: int) -> dict[tuple[int, int, int], int]:
    group = list(product(range(n_rotation), range(2)))
    counts = {pattern: 0 for pattern in product(range(2), repeat=3)}
    for a, s, y in product(group, repeat=3):
        if relator(a, s, y, n_rotation) != (0, 0):
            continue
        if not spans_frattini((a, s, y)):
            continue
        counts[(a[1], s[1], y[1])] += 1
    return counts


def predicted_pattern_counts(n_rotation: int) -> dict[tuple[int, int, int], int]:
    n2 = n_rotation * n_rotation
    out = {pattern: 0 for pattern in product(range(2), repeat=3)}
    regular = (
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    )
    for pattern in regular:
        out[pattern] = n2
    out[(1, 0, 0)] = (3 if n_rotation == 4 else 2) * n2
    return out


def predicted_surjections(m: int) -> int:
    if m == 3:
        return 144
    return 1 << (2 * m + 1)


def automorphism_count(m: int) -> int:
    return 1 << (2 * m - 3)


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
                comm = (
                    ((-1) ** sigma) * (((-1) ** tau) - 1) * s
                    + ((-1) ** tau) * (1 - ((-1) ** sigma)) * y
                )
                expected = (
                    (2 * a if alpha == 0 else 0)
                    + (4 * s if sigma == 0 else 0)
                    + comm
                ) % n_rotation
                assert observed == expected
                checks += 1
    return checks


def check_exhaustive(max_m: int = 7) -> int:
    total_patterns = 0
    for m in range(3, max_m + 1):
        n_rotation = 1 << (m - 1)
        observed = brute_pattern_counts(n_rotation)
        expected = predicted_pattern_counts(n_rotation)
        assert observed == expected, (m, observed, expected)
        assert sum(observed.values()) == predicted_surjections(m)
        total_patterns += len(observed)
    return total_patterns


def check_extension_counts(max_m: int = 16) -> None:
    for m in range(3, max_m + 1):
        quotient = predicted_surjections(m) // automorphism_count(m)
        assert quotient == (18 if m == 3 else 16)


def main() -> None:
    relator_checks = check_relator_formula()
    pattern_checks = check_exhaustive()
    check_extension_counts()
    print("G_Q2 dihedral target counts")
    print(f"relator-coordinate identities: {relator_checks}")
    print(f"exhaustive reflection-pattern subtotals: {pattern_checks}")
    print("all triples exhaustively checked through D_128")
    print("closed extension counts checked through D_(2^16)")
    print("all exact dihedral-target checks passed")


if __name__ == "__main__":
    main()
