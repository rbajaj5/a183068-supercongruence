"""Exact checks for A244973QuadraticFrobeniusReduction.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


PHI = {
    (0, 0): 1,
    (1, 0): 1,
    (0, 1): -1,
    (1, 1): 1,
    (1, 2): -1,
    (2, 1): 1,
    (2, 2): 1,
}


def a(n: int) -> int:
    return sum((-1) ** k * comb(n, k) ** 2 * comb(2 * k, k) for k in range(n + 1))


def signed_multinomial_square(n: int) -> int:
    total = 0
    nf = factorial(n)
    for i in range(n + 1):
        for j in range(n - i + 1):
            k = n - i - j
            multinomial = nf // (factorial(i) * factorial(j) * factorial(k))
            total += (-1) ** (i + j) * multinomial**2
    return total


def multiply(
    left: dict[tuple[int, int], int],
    right: dict[tuple[int, int], int],
) -> dict[tuple[int, int], int]:
    out: dict[tuple[int, int], int] = {}
    for (i, j), x in left.items():
        for (k, ell), y in right.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, 0) + x * y
    return {key: value for key, value in out.items() if value}


def phi_power(n: int) -> dict[tuple[int, int], int]:
    out = {(0, 0): 1}
    for _ in range(n):
        out = multiply(out, PHI)
    return out


def vertex_diagonal(n: int) -> int:
    return (-1) ** n * phi_power(n).get((n, n), 0)


def log_plus_coefficient(i: int, j: int) -> Fraction:
    """Coefficient in log(1+u+uv)."""
    if i >= 1 and 0 <= j <= i:
        return Fraction((-1) ** (i + 1) * comb(i, j), i)
    return Fraction(0)


def log_minus_coefficient(i: int, j: int) -> Fraction:
    """Coefficient in log(1-v+uv)."""
    if j >= 1 and 0 <= i <= j:
        return Fraction(-(-1) ** i * comb(j, i), j)
    return Fraction(0)


def log_phi_coefficient(i: int, j: int) -> Fraction:
    """Coefficient of u^i v^j in log((1+u+uv)(1-v+uv))."""
    return log_plus_coefficient(i, j) + log_minus_coefficient(i, j)


def reduced_log(p: int, degree: int) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for i in range(degree + 1):
        for j in range(degree + 1):
            if i == 0 and j == 0:
                continue
            value = log_phi_coefficient(i, j)
            if i % p == 0 and j % p == 0:
                value -= Fraction(1, p) * log_phi_coefficient(i // p, j // p)
            if value:
                out[i, j] = value
    return out


def valuation_fraction(value: Fraction, p: int) -> int:
    if value == 0:
        return 10**9
    numerator = abs(value.numerator)
    denominator = value.denominator
    answer = 0
    while numerator % p == 0:
        answer += 1
        numerator //= p
    while denominator % p == 0:
        answer -= 1
        denominator //= p
    return answer


def valuation_int(value: int, p: int) -> int:
    return valuation_fraction(Fraction(value), p)


def first_two_frobenius_terms(p: int, m: int) -> tuple[Fraction, Fraction]:
    """Return the signed h=1 and h=2 terms in equation (10)."""
    target = p * m
    log = reduced_log(p, target)
    coarse = phi_power(m)
    linear = Fraction(0)
    quadratic = Fraction(0)

    for (a_exp, b_exp), coefficient in coarse.items():
        x_exp = p * (m - a_exp)
        y_exp = p * (m - b_exp)
        if x_exp < 0 or y_exp < 0:
            continue
        linear += coefficient * log.get((x_exp, y_exp), Fraction(0))

        square_coefficient = Fraction(0)
        for (i, j), value in log.items():
            if i <= x_exp and j <= y_exp:
                square_coefficient += value * log.get(
                    (x_exp - i, y_exp - j), Fraction(0)
                )
        quadratic += coefficient * square_coefficient

    sign = (-1) ** m
    n = p * m
    return sign * n * linear, sign * Fraction(n * n, 2) * quadratic


def main() -> None:
    identity_checks = 0
    for n in range(11):
        expected = a(n)
        assert signed_multinomial_square(n) == expected
        assert vertex_diagonal(n) == expected
        identity_checks += 2

    coefficient_checks = 0
    for p in (7, 11, 13):
        log = reduced_log(p, 3 * p)
        for a_index in range(1, 4):
            for b_index in range(a_index + 1):
                plus = Fraction(
                    (-1) ** (a_index + 1)
                    * (comb(p * a_index, p * b_index) - comb(a_index, b_index)),
                    p * a_index,
                )
                minus = Fraction(
                    -(-1) ** b_index
                    * (comb(p * a_index, p * b_index) - comb(a_index, b_index)),
                    p * a_index,
                )
                plus_from_logs = log_plus_coefficient(
                    p * a_index, p * b_index
                ) - Fraction(1, p) * log_plus_coefficient(a_index, b_index)
                minus_from_logs = log_minus_coefficient(
                    p * b_index, p * a_index
                ) - Fraction(1, p) * log_minus_coefficient(b_index, a_index)
                assert plus == plus_from_logs
                assert minus == minus_from_logs
                assert log.get((p * a_index, p * b_index), Fraction(0)) == (
                    plus_from_logs
                    + (
                        minus_from_logs
                        if a_index == b_index
                        else Fraction(0)
                    )
                )
                if 0 < b_index < a_index:
                    assert valuation_fraction(plus, p) >= 2
                    assert valuation_fraction(minus, p) >= 2
                coefficient_checks += 2

    assert a(5) - a(1) == 50
    assert valuation_int(a(5) - a(1), 5) == 2

    tower_checks = 0
    sharp_checks = 0
    for p in (7, 11, 13):
        for n in range(1, 5):
            previous = a(n)
            for r in (1, 2):
                current = a(n * p**r)
                value = valuation_int(current - previous, p)
                assert value >= 3 * r
                assert value >= 3 + 2 * valuation_int(n * p ** (r - 1), p)
                sharp_checks += value == 3 * r
                tower_checks += 1
                previous = current

    dwork_checks = 0
    for p, m in ((7, 1), (7, 2), (7, 7), (11, 1), (11, 2)):
        linear, quadratic = first_two_frobenius_terms(p, m)
        target = 3 + 3 * valuation_int(m, p)
        difference = Fraction(a(p * m) - a(m))
        assert valuation_fraction(difference - linear - quadratic, p) >= target
        assert valuation_fraction(linear + quadratic, p) >= target
        dwork_checks += 2

    linear, quadratic = first_two_frobenius_terms(7, 7)
    assert valuation_fraction(linear, 7) == 5
    assert valuation_fraction(quadratic, 7) == 5
    assert valuation_fraction(linear + quadratic, 7) == 6
    dwork_checks += 3

    print(f"A244973 identity checks: {identity_checks}")
    print(f"reduced-log coefficient checks: {coefficient_checks}")
    print(f"A244973 tower checks: {tower_checks}")
    print(f"sharp tower checks: {sharp_checks}")
    print(f"two-term Dwork checks: {dwork_checks}")
    print("p=5 obstruction and p=7 linear-quadratic cancellation verified")


if __name__ == "__main__":
    main()
