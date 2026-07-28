"""Exact checks for conjugacy shells in the dyadic affine quotient."""

from __future__ import annotations


def valuation_mod_power_of_two(value: int, precision: int) -> int:
    """Return v_2(value) for a nonzero residue modulo 2**precision."""
    modulus = 1 << precision
    value %= modulus
    if value == 0:
        raise ValueError("zero has no finite truncated valuation")
    result = 0
    while value % 2 == 0:
        value //= 2
        result += 1
    return result


def units(precision: int) -> range:
    return range(1, 1 << precision, 2)


def conjugate_translation(
    unit: int, offset: int, translation: int, precision: int
) -> int:
    """Conjugate T_translation by M(unit, offset)."""
    modulus = 1 << precision
    inverse_unit = pow(unit, -1, modulus)

    # (u,a)(1,b)(u,a)^(-1), using (u,a)(v,c)=(uv,a+uc).
    first_unit = unit
    first_offset = (offset + unit * translation) % modulus
    inverse_offset = (-inverse_unit * offset) % modulus
    result_unit = first_unit * inverse_unit % modulus
    result_offset = (first_offset + first_unit * inverse_offset) % modulus
    assert result_unit == 1
    assert result_offset == unit * translation % modulus
    return result_offset


def check_conjugacy_shells() -> int:
    checks = 0
    for precision in range(2, 9):
        modulus = 1 << precision
        unit_values = tuple(units(precision))

        assert {conjugate_translation(u, 0, 0, precision) for u in unit_values} == {
            0
        }
        checks += len(unit_values)

        for depth in range(precision):
            representative = 1 << depth
            orbit = {
                conjugate_translation(unit, offset, representative, precision)
                for unit in unit_values
                for offset in (0, 1, modulus // 2)
            }
            shell = {
                value
                for value in range(1, modulus)
                if valuation_mod_power_of_two(value, precision) == depth
            }
            assert orbit == shell
            assert len(orbit) == 1 << (precision - depth - 1)

            centralizing_units = {
                unit
                for unit in unit_values
                if unit * representative % modulus == representative
            }
            assert len(centralizing_units) == 1 << depth
            centralizer_size = modulus * len(centralizing_units)
            assert centralizer_size == 1 << (precision + depth)
            group_size = modulus * len(unit_values)
            assert group_size // centralizer_size == len(orbit)
            checks += 3 * len(unit_values)
    return checks


def direct_moment(precision: int, exponent: int) -> int:
    modulus = 1 << precision
    return sum(
        1 << (exponent * valuation_mod_power_of_two(value, precision))
        for value in range(1, modulus)
    )


def formula_moment(precision: int, exponent: int) -> int:
    return sum(
        (1 << (precision - depth - 1)) * (1 << (exponent * depth))
        for depth in range(precision)
    )


def check_depth_moments() -> int:
    checks = 0
    for exponent in range(9):
        previous = None
        for precision in range(1, 17):
            direct = direct_moment(precision, exponent)
            formula = formula_moment(precision, exponent)
            assert direct == formula
            if previous is not None:
                assert direct - 2 * previous == 1 << (exponent * (precision - 1))
            previous = direct
            checks += 1
    return checks


def main() -> None:
    conjugacy_checks = check_conjugacy_shells()
    moment_checks = check_depth_moments()
    print(f"checked {conjugacy_checks} finite affine conjugacy identities")
    print(f"checked {moment_checks} exact depth-moment identities")
    print("PASS")


if __name__ == "__main__":
    main()
