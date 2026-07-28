"""Exact finite checks for the affine-word grammar specialization."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def multiply(
    left: tuple[int, int], right: tuple[int, int], modulus: int
) -> tuple[int, int]:
    """Multiply M(u,b) M(v,c) = M(uv,b+uc)."""
    u, b = left
    v, c = right
    return (u * v % modulus, (b + u * c) % modulus)


def check_grammar(m: int) -> int:
    modulus = 1 << m
    units = [u for u in range(modulus) if u % 2]
    identity = (1, 0)
    normal_forms: set[tuple[int, int]] = set()
    checks = 0

    for u in units:
        unit = (u, 0)
        assert multiply(identity, unit, modulus) == unit
        for b in range(modulus):
            twist = (1, b)
            normal = multiply(twist, unit, modulus)
            assert normal == (u, b)
            normal_forms.add(normal)

            for c in range(modulus):
                twist_c = (1, c)
                assert multiply(twist, twist_c, modulus) == (
                    1,
                    (b + c) % modulus,
                )
                assert multiply(unit, twist_c, modulus) == multiply(
                    (1, u * c % modulus), unit, modulus
                )
                checks += 2

        for v in units:
            assert multiply(unit, (v, 0), modulus) == (u * v % modulus, 0)
            checks += 1

    assert len(normal_forms) == modulus * len(units)
    return checks


def check_twist_convolution(m: int) -> int:
    modulus = 1 << m
    units = [u for u in range(modulus) if u % 2]
    set_a = [a for a in range(modulus) if (a * a + 3 * a + 1) % 5 < 3]
    checks = 0

    def observable(state: tuple[int, int]) -> Fraction:
        u, b = state
        return Fraction((u + 2 * b + b * b) % 19, 18)

    for u in units:
        for y in range(modulus):
            group_average = sum(
                (
                    observable(
                        multiply((u, u * y % modulus), (1, -a), modulus)
                    )
                    for a in set_a
                ),
                Fraction(0),
            ) / len(set_a)
            convolution = sum(
                (
                    observable((u, u * ((y - a) % modulus) % modulus))
                    for a in set_a
                ),
                Fraction(0),
            ) / len(set_a)
            assert group_average == convolution
            checks += 1

    return checks


def fourier_coefficient_is_zero(values: list[Fraction], k: int) -> bool:
    """Decide exact vanishing at a 2-power root of unity."""
    modulus = len(values)
    common = gcd(modulus, k)
    order = modulus // common
    if order == 1:
        return sum(values, Fraction(0)) == 0

    coefficients = [Fraction(0) for _ in range(order)]
    primitive_exponent = k // common
    for y, value in enumerate(values):
        coefficients[(-primitive_exponent * y) % order] += value

    half = order // 2
    return all(
        coefficients[j] == coefficients[j + half] for j in range(half)
    )


def exact_periods(values: list[Fraction]) -> set[int]:
    modulus = len(values)
    return {
        c
        for c in range(modulus)
        if all(values[(y - c) % modulus] == values[y] for y in range(modulus))
    }


def predicted_periods(values: list[Fraction]) -> set[int]:
    modulus = len(values)
    support = [
        k
        for k in range(modulus)
        if not fourier_coefficient_is_zero(values, k)
    ]
    divisor = modulus
    for k in support:
        divisor = gcd(divisor, k)
    step = modulus // divisor
    return {c for c in range(modulus) if c % step == 0}


def check_period_certificate(m: int) -> int:
    modulus = 1 << m
    units = [u for u in range(modulus) if u % 2]
    set_a = [a for a in range(modulus) if (a * a + a + 1) % 7 < 4]
    checks = 0

    for u in units:
        base = [
            Fraction((3 * y * y + u * y + 5 * u) % 23, 22)
            for y in range(modulus)
        ]
        averaged = [
            sum((base[(y - a) % modulus] for a in set_a), Fraction(0))
            / len(set_a)
            for y in range(modulus)
        ]
        assert predicted_periods(base) == exact_periods(base)
        assert predicted_periods(averaged) == exact_periods(averaged)
        checks += 2

    constant = [Fraction(3, 7) for _ in range(modulus)]
    zero = [Fraction(0) for _ in range(modulus)]
    assert predicted_periods(constant) == set(range(modulus))
    assert predicted_periods(zero) == set(range(modulus))
    return checks + 2


def main() -> None:
    grammar_checks = 0
    convolution_checks = 0
    period_checks = 0
    for m in range(3, 8):
        grammar_checks += check_grammar(m)
        convolution_checks += check_twist_convolution(m)
        period_checks += check_period_certificate(m)
    print(f"checked {grammar_checks} exact affine rewriting identities")
    print(f"checked {convolution_checks} exact twist-convolution identities")
    print(f"checked {period_checks} exact cyclotomic period certificates")
    print("checked unique normal forms through modulus 2^7")
    print("PASS")


if __name__ == "__main__":
    main()
