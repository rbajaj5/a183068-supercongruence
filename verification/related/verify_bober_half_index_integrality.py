"""Exact checks for the uniform Bober half-index theorem."""

from fractions import Fraction
from math import factorial


PACKET = (
    ("A295456", (30, 5, 4), (15, 12, 10, 2)),
    ("A295458", (30, 5, 4), (15, 10, 8, 6)),
    ("A295460", (30, 3, 2), (15, 10, 6, 4)),
    ("A295465", (30, 5, 3), (15, 12, 10, 1)),
    ("A295468", (30, 5, 3, 2), (15, 10, 8, 6, 1)),
    ("A295470", (20, 6, 1), (12, 10, 3, 2)),
    ("A295471", (20, 1), (10, 8, 3)),
    ("A295475", (20, 3), (10, 9, 4)),
    ("A295477", (24, 1), (12, 8, 5)),
    ("A295479", (24, 4, 1), (12, 8, 7, 2)),
    ("A295481", (24, 4, 3), (12, 9, 8, 2)),
)


def vp_int(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def vp(value: Fraction, prime: int) -> int:
    return vp_int(value.numerator, prime) - vp_int(value.denominator, prime)


def half_factorial(slope: int, n: int) -> tuple[Fraction, int]:
    product = slope * n
    if product % 2 == 0:
        return Fraction(factorial(product // 2)), 0
    k = (product - 1) // 2
    return Fraction(factorial(2 * k + 2), 4 ** (k + 1) * factorial(k + 1)), 1


def half_value(positive: tuple[int, ...], negative: tuple[int, ...], n: int) -> Fraction:
    out = Fraction(1)
    pi_power = 0
    for slope in positive:
        value, exponent = half_factorial(slope, n)
        out *= value
        pi_power += exponent
    for slope in negative:
        value, exponent = half_factorial(slope, n)
        out /= value
        pi_power -= exponent
    assert pi_power == 0
    return out


def landau(positive: tuple[int, ...], negative: tuple[int, ...], x: Fraction) -> int:
    return sum(int(slope * x) for slope in positive) - sum(
        int(slope * x) for slope in negative
    )


def binary_digit_valuation(
    positive: tuple[int, ...], negative: tuple[int, ...], n: int
) -> int:
    k = sum(slope for slope in negative if slope % 2) - sum(
        slope for slope in positive if slope % 2
    )
    return (
        k * n
        - sum((slope * n // 2).bit_count() for slope in positive if slope % 2 == 0)
        + sum((slope * n // 2).bit_count() for slope in negative if slope % 2 == 0)
    )


def check_packet_hypotheses() -> int:
    checks = 0
    for name, positive, negative in PACKET:
        assert sum(positive) == sum(negative), name
        assert sum(slope % 2 for slope in positive) == sum(
            slope % 2 for slope in negative
        ), name
        assert landau(positive, negative, Fraction(1, 2)) == 0, name
        k = sum(slope for slope in negative if slope % 2) - sum(
            slope for slope in positive if slope % 2
        )
        assert k >= sum(slope % 2 == 0 for slope in positive), name
        for denominator in range(1, 401):
            for numerator in range(denominator):
                assert landau(positive, negative, Fraction(numerator, denominator)) >= 0
                checks += 1
        checks += 4
    return checks


def check_valuation_identities() -> int:
    checks = 0
    for name, positive, negative in PACKET:
        for n in range(1, 32, 2):
            value = half_value(positive, negative, n)
            for prime in (3, 5, 7, 11, 13):
                total = 0
                power = prime
                while power <= max(positive) * n + 1:
                    total += landau(
                        positive,
                        negative,
                        Fraction(n, 2 * power) + Fraction(1, 2),
                    )
                    power *= prime
                assert vp(value, prime) == total, (name, n, prime)
                checks += 1
            dyadic = binary_digit_valuation(positive, negative, n)
            assert vp(value, 2) == dyadic, (name, n)
            assert dyadic >= 0, (name, n)
            assert value.denominator == 1, (name, n)
            checks += 3
    return checks


def check_towers() -> int:
    checks = 0
    for name, positive, negative in PACKET:
        for prime in (5, 7):
            for level in (1, 2):
                for n in (1, 2):
                    high = half_value(positive, negative, n * prime**level)
                    low = half_value(positive, negative, n * prime ** (level - 1))
                    assert vp(high - low, prime) >= 3 * level, (name, prime, level, n)
                    checks += 1
    return checks


def main() -> None:
    sections = {
        "packet hypotheses and Landau values": check_packet_hypotheses(),
        "odd and dyadic valuation identities": check_valuation_identities(),
        "complete adjacent towers": check_towers(),
    }
    for label, count in sections.items():
        print(f"{label}: {count}")
    print(f"all {sum(sections.values())} checks passed")


if __name__ == "__main__":
    main()
