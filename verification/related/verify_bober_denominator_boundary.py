"""Exact checks for the denominator-three/four Bober boundary theorem."""

from fractions import Fraction
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
BASE = runpy.run_path(ROOT / "verification/related/verify_bober_sporadic_packet.py")

VARIANTS = (
    ("A295456", (30, 5, 4), (15, 12, 10, 2), 3),
    ("A295458", (30, 5, 4), (15, 10, 8, 6), 3),
    ("A295460", (30, 3, 2), (15, 10, 6, 4), 4),
    ("A295477", (24, 1), (12, 8, 5), 4),
)


def digit_sum(value: int, base: int) -> int:
    total = 0
    while value:
        total += value % base
        value //= base
    return total


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def landau(positive: tuple[int, ...], negative: tuple[int, ...], x: Fraction) -> int:
    return sum(floor_fraction(c * x) for c in positive) - sum(
        floor_fraction(c * x) for c in negative
    )


def residue_representative(value: int, q: int) -> int:
    residue = value % q
    return q if residue == 0 else residue


def translated_landau(
    positive: tuple[int, ...], negative: tuple[int, ...], q: int, z: int, x: Fraction
) -> int:
    def term(c: int) -> int:
        return floor_fraction(c * x + 1 - Fraction(residue_representative(c * z, q), q))

    return sum(term(c) for c in positive) - sum(term(c) for c in negative)


def boundary_valuation(
    positive: tuple[int, ...], negative: tuple[int, ...], q: int, n: int
) -> int:
    def gamma_valuation(c: int) -> int:
        product = c * n
        residue = product % q
        if q == 3:
            if residue == 0:
                k = product // 3
                return (k - digit_sum(k, 3)) // 2
            if residue == 1:
                return -(product + 2) // 3
            return -(product + 1) // 3
        assert q == 4
        if residue == 0:
            k = product // 4
            return k - k.bit_count()
        if residue == 1:
            return -(product + 3) // 2
        if residue == 2:
            return -(product + 2) // 4
        return -(product + 1) // 2

    return sum(gamma_valuation(c) for c in positive) - sum(
        gamma_valuation(c) for c in negative
    )


def displayed_boundary_formula(name: str, n: int) -> int:
    if name == "A295456":
        if n % 3 == 0:
            return boundary_valuation((30, 5, 4), (15, 12, 10, 2), 3, n)
        return (
            3 * n
            - digit_sum(10 * n, 3)
            + digit_sum(5 * n, 3)
            + digit_sum(4 * n, 3)
        ) // 2
    if name == "A295458":
        if n % 3 == 0:
            return boundary_valuation((30, 5, 4), (15, 10, 8, 6), 3, n)
        return (
            9 * n
            - digit_sum(10 * n, 3)
            + digit_sum(5 * n, 3)
            + digit_sum(2 * n, 3)
        ) // 2
    if name == "A295460":
        if n % 4 == 0:
            return boundary_valuation((30, 3, 2), (15, 10, 6, 4), 4, n)
        if n % 2:
            return n + n.bit_count()
        return (
            6 * n
            - (15 * n // 2).bit_count()
            - (n // 2).bit_count()
            + (5 * n // 2).bit_count()
            + (3 * n // 2).bit_count()
            + n.bit_count()
        )
    assert name == "A295477"
    if n % 4 == 0:
        return boundary_valuation((24, 1), (12, 8, 5), 4, n)
    return (3 * n if n % 2 else 2 * n) + n.bit_count()


def check_translated_landau() -> int:
    checks = 0
    for name, positive, negative, q in VARIANTS:
        assert sum(positive) == sum(negative), name
        for z in range(q):
            assert landau(positive, negative, Fraction(-z, q)) == 0, (name, z)
            for denominator in range(1, 201):
                for numerator in range(denominator):
                    x = Fraction(numerator, denominator)
                    left = translated_landau(positive, negative, q, z, x)
                    right = landau(positive, negative, x - Fraction(z, q))
                    assert left == right
                    assert left >= 0
                    checks += 2
            checks += 1
    return checks


def check_valuations_and_integrality() -> int:
    checks = 0
    for name, positive, negative, q in VARIANTS:
        terms = BASE["terms_for_fractional"](list(positive), list(negative), q)
        for n in range(1, 81):
            value = BASE["evaluate_gamma_ratio"](terms, n)
            boundary_prime = 3 if q == 3 else 2
            exact_boundary = boundary_valuation(positive, negative, q, n)
            assert BASE["vp"](value, boundary_prime) == exact_boundary
            assert exact_boundary == displayed_boundary_formula(name, n)
            assert exact_boundary >= 0
            assert value.denominator == 1
            checks += 4

            for prime in (2, 3, 5, 7, 11, 13):
                if q % prime == 0:
                    continue
                total = 0
                power = prime
                while power <= max(positive) * n + q:
                    z = (n * pow(power, -1, q)) % q
                    total += translated_landau(
                        positive, negative, q, z, Fraction(n, q * power)
                    )
                    power *= prime
                assert BASE["vp"](value, prime) == total, (name, n, prime)
                checks += 1
    return checks


def check_towers() -> int:
    checks = 0
    for name, positive, negative, q in VARIANTS:
        terms = BASE["terms_for_fractional"](list(positive), list(negative), q)
        for prime in (5, 7, 11):
            for level in (1, 2):
                for n in (1, 2):
                    high = BASE["evaluate_gamma_ratio"](terms, n * prime**level)
                    low = BASE["evaluate_gamma_ratio"](
                        terms, n * prime ** (level - 1)
                    )
                    assert BASE["vp"](high - low, prime) >= 3 * level
                    checks += 1
    return checks


def main() -> None:
    sections = {
        "translated Landau identities": check_translated_landau(),
        "boundary valuations and integrality": check_valuations_and_integrality(),
        "adjacent cubic towers": check_towers(),
    }
    for label, count in sections.items():
        print(f"{label}: {count}")
    print(f"all {sum(sections.values())} checks passed")


if __name__ == "__main__":
    main()
