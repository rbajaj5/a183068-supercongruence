"""Exact 2-adic checks for the orientation exponents in Remark C.7."""

from __future__ import annotations


def polynomial(value: int) -> int:
    """The polynomial defining the distinguished 2-adic unit."""

    return value**3 + 2 * value**2 + 1


def hensel_root(precision: int) -> int:
    """Return the unique root modulo 2**precision that is odd modulo 2."""

    root = 1
    modulus = 2
    for _ in range(1, precision):
        next_modulus = 2 * modulus
        candidates = (root, root + modulus)
        roots = [
            candidate
            for candidate in candidates
            if polynomial(candidate) % next_modulus == 0
        ]
        assert len(roots) == 1
        root = roots[0]
        modulus = next_modulus
    return root % modulus


def exponent_classes(precision: int) -> list[tuple[int, int]]:
    """Compute the compatible discrete-log class at every precision."""

    root = hensel_root(precision)
    classes: list[tuple[int, int]] = []
    exponent = 1

    for level in range(3, precision + 1):
        modulus = 2**level
        order = 2 ** (level - 2)
        eta = -pow(3, -1, modulus) % modulus
        exponent %= order

        if pow(root, exponent, modulus) != eta:
            lifted = exponent + order // 2
            assert pow(root, lifted, modulus) == eta
            exponent = lifted

        assert pow(root, exponent, modulus) == eta
        assert pow(root, order, modulus) == 1
        if order > 1:
            assert pow(root, order // 2, modulus) != 1

        if classes:
            previous_level, previous = classes[-1]
            assert previous_level == level - 1
            assert exponent in {previous, previous + 2 ** (level - 3)}

        classes.append((level, exponent))

    return classes


def multiply(
    left: tuple[tuple[int, int], tuple[int, int]],
    right: tuple[tuple[int, int], tuple[int, int]],
    modulus: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Multiply two 2-by-2 matrices modulo the supplied modulus."""

    return (
        (
            (left[0][0] * right[0][0] + left[0][1] * right[1][0])
            % modulus,
            (left[0][0] * right[0][1] + left[0][1] * right[1][1])
            % modulus,
        ),
        (
            (left[1][0] * right[0][0] + left[1][1] * right[1][0])
            % modulus,
            (left[1][0] * right[0][1] + left[1][1] * right[1][1])
            % modulus,
        ),
    )


def twist_matrix(
    parameter: int, modulus: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    """The action of a Dehn twist on the (S,Y) part of the abelianization."""

    return ((1, parameter % modulus), (0, 1))


def check_dehn_twists(precision: int) -> int:
    """Check composition, inverses, and exact dyadic depth at finite levels."""

    checks = 0
    identity = ((1, 0), (0, 1))

    for level in range(1, precision + 1):
        modulus = 2**level
        parameters = range(-8, 9)
        for left_parameter in parameters:
            for right_parameter in parameters:
                left = twist_matrix(left_parameter, modulus)
                right = twist_matrix(right_parameter, modulus)
                assert multiply(left, right, modulus) == twist_matrix(
                    left_parameter + right_parameter, modulus
                )
                checks += 1

        for parameter in parameters:
            matrix = twist_matrix(parameter, modulus)
            inverse = twist_matrix(-parameter, modulus)
            assert multiply(matrix, inverse, modulus) == identity
            checks += 1

    for depth in range(0, precision):
        for odd_unit in (-7, -5, -3, -1, 1, 3, 5, 7):
            parameter = (2**depth) * odd_unit
            assert twist_matrix(parameter, 2**depth) == identity
            assert twist_matrix(parameter, 2 ** (depth + 1)) != identity
            checks += 1

    return checks


def affine_product(
    left: tuple[int, int], right: tuple[int, int], modulus: int
) -> tuple[int, int]:
    """Multiply affine pairs (unit, translation) modulo a power of two."""

    unit, translation = left
    other_unit, other_translation = right
    return (
        (unit * other_unit) % modulus,
        (translation + unit * other_translation) % modulus,
    )


def affine_inverse(pair: tuple[int, int], modulus: int) -> tuple[int, int]:
    """Invert an affine pair modulo a power of two."""

    unit, translation = pair
    inverse_unit = pow(unit, -1, modulus)
    return (inverse_unit, (-inverse_unit * translation) % modulus)


def affine_commutator(
    left: tuple[int, int], right: tuple[int, int], modulus: int
) -> tuple[int, int]:
    """Use the convention [g,h] = g^-1 h^-1 g h."""

    return affine_product(
        affine_product(
            affine_product(
                affine_inverse(left, modulus),
                affine_inverse(right, modulus),
                modulus,
            ),
            left,
            modulus,
        ),
        right,
        modulus,
    )


def check_affine_shadow(precision: int) -> int:
    """Check the affine law, commutator formula, and central filtration."""

    checks = 0
    for level in range(1, precision + 1):
        modulus = 2**level
        units = range(1, modulus, 2)

        assert len(tuple(units)) * modulus == 2 ** (2 * level - 1)
        checks += 1

        for unit in units:
            inverse_unit = pow(unit, -1, modulus)
            for translation in range(modulus):
                scaling = (unit, 0)
                twist = (1, translation)
                conjugate = affine_product(
                    affine_product(scaling, twist, modulus),
                    affine_inverse(scaling, modulus),
                    modulus,
                )
                assert conjugate == (1, (unit * translation) % modulus)

                commutator = affine_commutator(scaling, twist, modulus)
                expected = (
                    1,
                    ((1 - inverse_unit) * translation) % modulus,
                )
                assert commutator == expected
                checks += 2

        commutator_parameters = {
            affine_commutator((unit, 0), (1, translation), modulus)[1]
            for unit in units
            for translation in range(modulus)
        }
        assert commutator_parameters == set(range(0, modulus, 2))
        checks += 1

        for depth in range(1, level):
            next_parameters = {
                affine_commutator((unit, 0), (1, translation), modulus)[1]
                for unit in units
                for translation in range(0, modulus, 2**depth)
            }
            assert next_parameters == set(
                range(0, modulus, 2 ** (depth + 1))
            )
            checks += 1

    return checks


def main() -> None:
    precision = 32
    root = hensel_root(precision)
    classes = exponent_classes(precision)
    twist_checks = check_dehn_twists(16)
    affine_checks = check_affine_shadow(9)

    assert root % 8 == 5
    assert polynomial(root) % (2**precision) == 0
    assert len({exponent for _, exponent in classes}) > 1

    print(f"root modulo 2^{precision}: {root}")
    print(f"checked {len(classes)} compatible exponent classes")
    print("last five classes:")
    for level, exponent in classes[-5:]:
        print(f"  k={level}: e={exponent} modulo 2^{level - 2}")
    print(f"checked {twist_checks} finite-level Dehn-twist identities")
    print(f"checked {affine_checks} finite-level affine identities")
    print("all exact orientation-lift checks passed")


if __name__ == "__main__":
    main()
