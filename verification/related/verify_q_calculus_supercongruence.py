"""Exact checks for QCalculusCyclotomicSupercongruences.md.

The checker uses only the Python standard library.  Polynomials are reduced
modulo powers of cyclotomic polynomials while they are constructed, so the
tests do not depend on a computer-algebra system.

These computations are regression evidence, not a substitute for the proof.
"""

from functools import lru_cache
from math import factorial


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        )
    return trim(answer)


def subtract(left: list[int], right: list[int]) -> list[int]:
    return add(left, [-coefficient for coefficient in right])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def exact_divide(dividend: list[int], divisor: list[int]) -> list[int]:
    """Divide integer polynomials when the monic division is exact."""
    dividend = dividend[:]
    divisor = trim(divisor[:])
    assert divisor[-1] == 1
    if len(dividend) < len(divisor):
        raise AssertionError("nonzero polynomial is not divisible")
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor):
        coefficient = dividend[-1]
        degree = len(dividend) - len(divisor)
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            dividend[degree + index] -= coefficient * value
        trim(dividend)
    assert dividend == [0]
    return trim(quotient)


@lru_cache(maxsize=None)
def cyclotomic(number: int) -> tuple[int, ...]:
    """Return Phi_number(q), with coefficients in increasing degree."""
    polynomial = [-1] + [0] * (number - 1) + [1]
    for divisor in range(1, number):
        if number % divisor == 0:
            polynomial = exact_divide(polynomial, list(cyclotomic(divisor)))
    return tuple(polynomial)


def power(poly: list[int], exponent: int) -> list[int]:
    answer = [1]
    base = poly
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        base = multiply(base, base)
        exponent //= 2
    return answer


class PolynomialModulus:
    def __init__(self, polynomial: list[int]):
        self.polynomial = trim(polynomial)
        assert self.polynomial[-1] == 1
        self.degree = len(self.polynomial) - 1

    def reduce(self, poly: list[int]) -> list[int]:
        answer = trim(poly[:])
        while len(answer) > self.degree:
            coefficient = answer[-1]
            shift = len(answer) - len(self.polynomial)
            for index, value in enumerate(self.polynomial):
                answer[shift + index] -= coefficient * value
            trim(answer)
        return answer

    def add(self, left: list[int], right: list[int]) -> list[int]:
        return self.reduce(add(left, right))

    def subtract(self, left: list[int], right: list[int]) -> list[int]:
        return self.reduce(subtract(left, right))

    def multiply(self, left: list[int], right: list[int]) -> list[int]:
        return self.reduce(multiply(left, right))

    def q_power(self, exponent: int) -> list[int]:
        answer = [1]
        base = self.reduce([0, 1])
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, base)
            base = self.multiply(base, base)
            exponent //= 2
        return answer


class QMultinomialCalculator:
    def __init__(self, modulus: PolynomialModulus):
        self.modulus = modulus
        self.cache: dict[tuple[int, int, int], list[int]] = {}

    def q_binomial(self, n: int, k: int, base_power: int = 1) -> list[int]:
        if k < 0 or k > n:
            return [0]
        k = min(k, n - k)
        key = (n, k, base_power)
        if key in self.cache:
            return self.cache[key]
        if k == 0:
            answer = [1]
        else:
            answer = self.modulus.add(
                self.q_binomial(n - 1, k, base_power),
                self.modulus.multiply(
                    self.modulus.q_power(base_power * (n - k)),
                    self.q_binomial(n - 1, k - 1, base_power),
                ),
            )
        self.cache[key] = answer
        return answer

    def q_multinomial(
        self, parts: tuple[int, ...], base_power: int = 1
    ) -> list[int]:
        remaining = sum(parts)
        answer = [1]
        for part in parts:
            answer = self.modulus.multiply(
                answer,
                self.q_binomial(remaining, part, base_power),
            )
            remaining -= part
        return answer

    def a_uv(
        self, u: int, v: int, n: int, base_power: int = 1
    ) -> list[int]:
        answer = [0]
        for k in range(n + 1):
            parts = (k,) * u + (n - k,) * v
            answer = self.modulus.add(
                answer,
                self.q_multinomial(parts, base_power),
            )
        return answer


def multinomial(parts: tuple[int, ...]) -> int:
    answer = factorial(sum(parts))
    for part in parts:
        answer //= factorial(part)
    return answer


def pair_energy(parts: tuple[int, ...]) -> int:
    return sum(
        parts[i] * parts[j]
        for i in range(len(parts))
        for j in range(i + 1, len(parts))
    )


def cyclotomic_exponent(parts: tuple[int, ...], order: int) -> int:
    return sum(parts) // order - sum(part // order for part in parts)


def landau_uv(u: int, v: int, numerator: int, denominator: int) -> int:
    return v + ((u - v) * numerator) // denominator


def check_cyclotomic_landau_identity() -> int:
    checks = 0
    for u in range(1, 8):
        for v in range(1, 8):
            for order in range(2, 15):
                for multiple in range(1, 5):
                    n = order * multiple
                    for k in range(1, n):
                        residue = k % order
                        if residue == 0:
                            continue
                        parts = (k,) * u + (n - k,) * v
                        observed = cyclotomic_exponent(parts, order)
                        expected = landau_uv(u, v, residue, order)
                        assert observed == expected
                        checks += 1
    return checks


def check_a183068_cyclotomic_filtration() -> int:
    checks = 0
    u, v = 4, 2
    for p in (2, 3, 5, 7):
        for t in (1, 2, 3):
            n = p**t
            for k in range(1, n):
                s = 0
                reduced = k
                while reduced % p == 0:
                    s += 1
                    reduced //= p
                for level in range(s + 1, t + 1):
                    order = p**level
                    residue = k % order
                    parts = (k,) * u + (n - k,) * v
                    observed = cyclotomic_exponent(parts, order)
                    expected = 2 + (2 * residue) // order
                    assert observed == expected
                    assert observed >= 2
                    if p == 2 and level == s + 1:
                        assert observed == 3
                    checks += 1
    return checks


def check_square_congruences() -> int:
    """Check A_uv(bN;q) = A_uv(N;q^(b^2)) mod Phi_b(q)^2."""
    checks = 0
    cases = []
    for scale in (2, 3, 4, 5):
        for u, v in ((2, 2), (2, 3), (3, 2), (4, 2)):
            for n in ((1, 2) if scale <= 3 else (1,)):
                cases.append((scale, u, v, n))

    for scale, u, v, n in cases:
        modulus = PolynomialModulus(power(list(cyclotomic(scale)), 2))
        calculator = QMultinomialCalculator(modulus)
        left = calculator.a_uv(u, v, scale * n)
        right = calculator.a_uv(u, v, n, scale * scale)
        assert modulus.subtract(left, right) == [0]
        checks += 1
    return checks


def check_corrected_cubic_congruences() -> int:
    """Check the explicit Straub correction modulo Phi_p(q)^3."""
    checks = 0
    for p in (5, 7):
        modulus = PolynomialModulus(power(list(cyclotomic(p)), 3))
        calculator = QMultinomialCalculator(modulus)
        q_to_p_minus_one = modulus.subtract(modulus.q_power(p), [1])
        correction_shape = modulus.multiply(
            q_to_p_minus_one, q_to_p_minus_one
        )

        for u, v in ((3, 3), (3, 4), (4, 3)):
            for n in (1, 2):
                left = calculator.a_uv(u, v, p * n)
                right = calculator.a_uv(u, v, n, p * p)
                defect = 0
                for k in range(n + 1):
                    parts = (k,) * u + (n - k,) * v
                    defect += multinomial(parts) * pair_energy(parts)
                coefficient = ((p * p - 1) // 24) * defect
                correction = [
                    coefficient * value for value in correction_shape
                ]

                # left = right - correction modulo Phi_p(q)^3.
                assert modulus.add(
                    modulus.subtract(left, right), correction
                ) == [0]
                checks += 1
    return checks


def main() -> None:
    landau_checks = check_cyclotomic_landau_identity()
    filtration_checks = check_a183068_cyclotomic_filtration()
    square_checks = check_square_congruences()
    cubic_checks = check_corrected_cubic_congruences()
    total = (
        landau_checks
        + filtration_checks
        + square_checks
        + cubic_checks
    )
    print(f"cyclotomic Landau identities: {landau_checks}")
    print(f"A183068 active cyclotomic levels: {filtration_checks}")
    print(f"square q-congruences: {square_checks}")
    print(f"corrected cubic q-congruences: {cubic_checks}")
    print(f"all {total} q-calculus checks passed")


if __name__ == "__main__":
    main()
