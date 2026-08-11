"""Exact checks for Bala's August coefficient packet.

These calculations test identities, boundaries, and sample towers.  The
general results are established by the proofs in the accompanying note.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd


PRIMES = (5, 7, 11, 13)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def integer_binomial(top: int, bottom: int) -> int:
    """Generalized binomial coefficient for an integer upper argument."""

    if bottom < 0:
        return 0
    if top >= 0:
        return comb(top, bottom) if bottom <= top else 0
    return (-1) ** bottom * comb(-top + bottom - 1, bottom)


def triangle_term(row: int, column: int) -> int:
    """A119258(row, column) from (1+2x)^row/(1+x)."""

    assert 0 <= column <= row
    return sum(
        (-1) ** (column - j) * (2**j) * comb(row, j)
        for j in range(column + 1)
    )


def rational_ray_coefficient(a: int, b: int, n: int) -> int:
    """[z^(bn)] (1+z)^(an) (1-z)^(-(a-b)n)."""

    degree = b * n
    left_power = a * n
    right_power = -(a - b) * n
    return sum(
        integer_binomial(left_power, j)
        * integer_binomial(right_power, degree - j)
        * (-1) ** (degree - j)
        for j in range(degree + 1)
    )


def partial_negative_binomial(c: int, n: int) -> int:
    if n == 0:
        return 1
    return sum(comb(n + j - 1, j) * 2**j for j in range(c * n + 1))


def coefficient_framing(alpha: int, beta: int, n: int) -> int:
    return sum(
        integer_binomial(alpha * n, j)
        * integer_binomial(beta * n, n - j)
        * (-1) ** (n - j)
        for j in range(n + 1)
    )


def poly_add(left: list[int], right: list[int], right_scale: int = 1) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += right_scale * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def poly_power(base: list[int], exponent: int) -> list[int]:
    out = [1]
    factor = base
    while exponent:
        if exponent & 1:
            out = poly_multiply(out, factor)
        exponent >>= 1
        if exponent:
            factor = poly_multiply(factor, factor)
    return out


def chebyshev_numerator(n: int) -> list[int]:
    """P_n with T_n((1+x)/(1-x)) = P_n(x)/(1-x)^n."""

    assert n >= 0
    if n == 0:
        return [1]
    previous = [1]
    current = [1, 1]
    for _ in range(1, n):
        first = [2 * value for value in poly_multiply([1, 1], current)]
        second = poly_multiply([1, -2, 1], previous)
        previous, current = current, poly_add(first, second, right_scale=-1)
    return current


def chebyshev_coefficient_direct(r: int, s: int, n: int) -> int:
    degree = r * n
    numerator = poly_power(chebyshev_numerator(n), s)
    denominator_power = n * s
    total = 0
    for j, value in enumerate(numerator[: degree + 1]):
        tail = degree - j
        total += value * comb(denominator_power + tail - 1, tail)
    return total


def ratio_coefficient(power: int, degree: int) -> int:
    """[t^degree] ((1+t)/(1-t))^power."""

    return sum(
        integer_binomial(power, j)
        * integer_binomial(-power, degree - j)
        * (-1) ** (degree - j)
        for j in range(degree + 1)
    )


def chebyshev_coefficient_split(r: int, s: int, n: int) -> int:
    numerator = sum(
        comb(s, j) * ratio_coefficient((2 * j - s) * n, 2 * r * n)
        for j in range(s + 1)
    )
    assert numerator % (2**s) == 0
    return numerator // (2**s)


def negative_binomial_sum(n: int) -> int:
    return sum(
        comb(n + k - 1, k) * comb(2 * n + k - 1, k)
        for k in range(n + 1)
    )


def bernoulli_number(index: int) -> Fraction:
    values = [Fraction(0)] * (index + 1)
    for m in range(index + 1):
        values[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            values[j - 1] = j * (values[j - 1] - values[j])
    return values[0]


def fraction_mod(value: Fraction, modulus: int) -> int:
    assert gcd(value.denominator, modulus) == 1
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def check_formula_identities() -> int:
    checks = 0
    for a in range(2, 8):
        for b in range(1, a):
            for n in range(1, 8):
                assert triangle_term(a * n, b * n) == rational_ray_coefficient(a, b, n)
                checks += 1
    for c in range(1, 7):
        for n in range(1, 10):
            assert partial_negative_binomial(c, n) == triangle_term((c + 1) * n, c * n)
            checks += 1
    for r in range(1, 5):
        for s in range(1, 5):
            for n in range(1, 7):
                assert chebyshev_coefficient_direct(r, s, n) == chebyshev_coefficient_split(
                    r, s, n
                )
                checks += 1
    return checks


def check_named_sequences() -> int:
    checks = 0
    a119259 = (1, 3, 17, 111, 769, 5503, 40193)
    a333562 = (1, 15, 769, 47103, 3080193, 208470015)
    a103885 = (1, 2, 16, 146, 1408, 14002, 142000)
    for n, expected in enumerate(a119259):
        assert partial_negative_binomial(1, n) == expected
        checks += 1
    for n, expected in enumerate(a333562):
        assert partial_negative_binomial(3, n) == expected
        checks += 1
    for n, expected in enumerate(a103885):
        if n == 0:
            observed = 1
        else:
            observed = coefficient_framing(2, -2, n) // 2
            assert observed == chebyshev_coefficient_direct(1, 1, n)
        assert observed == expected
        checks += 1
    for n in range(1, 20):
        source = partial_negative_binomial(1, n)
        a333564 = (source - (-1) ** n) // 2
        a333565 = 2 * source - (-1) ** n
        assert 2 * a333564 + (-1) ** n == source
        assert a333565 == 4 * a333564 + (-1) ** n
        checks += 2
    return checks


def check_ray_towers() -> int:
    checks = 0
    for a in range(2, 7):
        for b in range(1, a):
            for prime in PRIMES:
                for n in range(1, 4):
                    for level in (1, 2):
                        large = triangle_term(a * n * prime**level, b * n * prime**level)
                        small = triangle_term(
                            a * n * prime ** (level - 1),
                            b * n * prime ** (level - 1),
                        )
                        assert (large - small) % prime ** (3 * level) == 0
                        checks += 1
    return checks


def check_chebyshev_towers() -> int:
    checks = 0
    for r in range(1, 5):
        for s in range(1, 5):
            for prime in (5, 7, 11):
                if r % prime == 0:
                    continue
                for n in (1, 2):
                    for level in (1, 2):
                        large = chebyshev_coefficient_split(r, s, n * prime**level)
                        small = chebyshev_coefficient_split(r, s, n * prime ** (level - 1))
                        assert (large - small) % prime ** (3 * level) == 0
                        checks += 1
    return checks


def check_bernoulli_defect() -> int:
    checks = 0
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        modulus = prime**4
        predicted = (
            3 + 2 * prime**3 * fraction_mod(bernoulli_number(prime - 3), modulus)
        ) % modulus
        assert negative_binomial_sum(prime) % modulus == predicted
        checks += 1

    assert negative_binomial_sum(7) == 162_602_583
    assert valuation(negative_binomial_sum(7) - negative_binomial_sum(1), 7) == 3
    assert valuation(negative_binomial_sum(49) - negative_binomial_sum(7), 7) == 6
    checks += 3
    return checks


def check_corrected_negative_binomial_grid() -> int:
    checks = 0
    for prime in (5, 7, 11):
        for n in (1, 2, 3):
            for level in (1, 2):
                large = negative_binomial_sum(n * prime**level)
                small = negative_binomial_sum(n * prime ** (level - 1))
                assert (large - small) % prime ** (3 * level) == 0
                checks += 1
    return checks


def main() -> None:
    sections = {
        "formula identities": check_formula_identities(),
        "named sequences": check_named_sequences(),
        "A119258 ray towers": check_ray_towers(),
        "Chebyshev towers": check_chebyshev_towers(),
        "Bernoulli defect": check_bernoulli_defect(),
        "corrected negative-binomial grid": check_corrected_negative_binomial_grid(),
    }
    for name, count in sections.items():
        print(f"{name}: {count}")
    print(f"Bala August coefficient checks passed: {sum(sections.values())}")


if __name__ == "__main__":
    main()
