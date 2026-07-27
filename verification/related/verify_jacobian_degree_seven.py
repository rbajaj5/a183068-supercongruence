"""Exact checks for JacobianDegreeSevenGenusSix.md.

Point counts use univariate root counting rather than a q^2 grid: for each
first coordinate r, the rational roots in t are the degree of
gcd(T(r,t), t^q-t).  This keeps the F_(5^6) calculation small.
"""

from itertools import product


P = 5
MODULI = {
    1: (0, 1),
    2: (1, 1, 1),
    3: (1, 1, 0, 1),
    4: (2, 0, 0, 0, 1),
    5: (1, 4, 0, 0, 0, 1),
    6: (2, 1, 0, 0, 0, 0, 1),
}


# Twice the divided-difference curve attached to
# rho(w) = -w + 4w^3 + 3w^5 - 7w^6.
TANGENT_TERMS = (
    (-12, 5, 0),
    (-10, 4, 1),
    (5, 4, 0),
    (-8, 3, 2),
    (4, 3, 1),
    (-6, 2, 3),
    (3, 2, 2),
    (6, 2, 0),
    (-4, 1, 4),
    (2, 1, 3),
    (4, 1, 1),
    (-2, 0, 5),
    (1, 0, 4),
    (2, 0, 2),
    (-1, 0, 0),
)


def valuation(number: int, prime: int) -> int:
    assert number
    answer = 0
    while number % prime == 0:
        answer += 1
        number //= prime
    return answer


def prime_factors(number: int) -> list[int]:
    answer = []
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            answer.append(divisor)
            while number % divisor == 0:
                number //= divisor
        divisor += 1
    if number > 1:
        answer.append(number)
    return answer


class FiniteField:
    """A small finite field with log-table multiplication."""

    def __init__(self, p: int, degree: int):
        self.p = p
        self.degree = degree
        self.q = p**degree
        self.modulus = MODULI[degree]
        self.digits = [self._decode(x) for x in range(self.q)]

        generator = self._primitive_element()
        self.exp = [0] * (self.q - 1)
        self.log = [-1] * self.q
        value = 1
        for exponent in range(self.q - 1):
            self.exp[exponent] = value
            self.log[value] = exponent
            value = self._raw_multiply(value, generator)
        assert value == 1
        assert all(self.log[x] >= 0 for x in range(1, self.q))

    def _decode(self, x: int) -> tuple[int, ...]:
        answer = []
        for _ in range(self.degree):
            answer.append(x % self.p)
            x //= self.p
        return tuple(answer)

    def _encode(self, coefficients: list[int] | tuple[int, ...]) -> int:
        answer = 0
        place = 1
        for coefficient in coefficients:
            answer += coefficient % self.p * place
            place *= self.p
        return answer

    def _raw_multiply(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        coefficients = [0] * (2 * self.degree - 1)
        for i, x in enumerate(self.digits[left]):
            for j, y in enumerate(self.digits[right]):
                coefficients[i + j] = (
                    coefficients[i + j] + x * y
                ) % self.p
        for degree in range(2 * self.degree - 2, self.degree - 1, -1):
            leading = coefficients[degree]
            if leading == 0:
                continue
            for i in range(self.degree):
                coefficients[degree - self.degree + i] = (
                    coefficients[degree - self.degree + i]
                    - leading * self.modulus[i]
                ) % self.p
        return self._encode(coefficients[: self.degree])

    def _raw_power(self, base: int, exponent: int) -> int:
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self._raw_multiply(answer, base)
            base = self._raw_multiply(base, base)
            exponent //= 2
        return answer

    def _primitive_element(self) -> int:
        factors = prime_factors(self.q - 1)
        for candidate in range(2, self.q):
            if all(
                self._raw_power(candidate, (self.q - 1) // factor) != 1
                for factor in factors
            ):
                return candidate
        raise AssertionError("no primitive element")

    def add(self, left: int, right: int) -> int:
        return self._encode(
            tuple(
                (x + y) % self.p
                for x, y in zip(self.digits[left], self.digits[right])
            )
        )

    def neg(self, value: int) -> int:
        return self._encode(tuple(-x % self.p for x in self.digits[value]))

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def mul(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        return self.exp[(self.log[left] + self.log[right]) % (self.q - 1)]

    def inv(self, value: int) -> int:
        assert value
        return self.exp[-self.log[value] % (self.q - 1)]


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_monic(poly: list[int], field: FiniteField) -> list[int]:
    poly = trim(poly)
    if poly == [0]:
        return poly
    inverse = field.inv(poly[-1])
    return [field.mul(coefficient, inverse) for coefficient in poly]


def poly_divmod(
    dividend: list[int],
    divisor: list[int],
    field: FiniteField,
) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:])
    divisor = trim(divisor[:])
    assert divisor != [0]
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = field.inv(divisor[-1])
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = field.mul(remainder[-1], inverse)
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[shift + i] = field.sub(
                remainder[shift + i],
                field.mul(coefficient, value),
            )
        trim(remainder)
    return trim(quotient), trim(remainder)


def poly_gcd(
    left: list[int],
    right: list[int],
    field: FiniteField,
) -> list[int]:
    left, right = trim(left[:]), trim(right[:])
    while right != [0]:
        left, right = right, poly_divmod(left, right, field)[1]
    return poly_monic(left, field)


def poly_mul_mod(
    left: list[int],
    right: list[int],
    modulus: list[int],
    field: FiniteField,
) -> list[int]:
    product_ = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        if x == 0:
            continue
        for j, y in enumerate(right):
            if y == 0:
                continue
            product_[i + j] = field.add(
                product_[i + j],
                field.mul(x, y),
            )
    return poly_divmod(product_, modulus, field)[1]


def poly_power_mod(
    base: list[int],
    exponent: int,
    modulus: list[int],
    field: FiniteField,
) -> list[int]:
    answer = [1]
    while exponent:
        if exponent & 1:
            answer = poly_mul_mod(answer, base, modulus, field)
        base = poly_mul_mod(base, base, modulus, field)
        exponent //= 2
    return answer


def rational_root_count(poly: list[int], field: FiniteField) -> int:
    poly = trim(poly)
    degree = len(poly) - 1
    if degree <= 0:
        return 0
    x_power = poly_power_mod([0, 1], field.q, poly, field)
    if len(x_power) < 2:
        x_power += [0] * (2 - len(x_power))
    x_power[1] = field.sub(x_power[1], 1)
    return len(poly_gcd(poly, x_power, field)) - 1


def powers(value: int, bound: int, field: FiniteField) -> list[int]:
    answer = [1]
    for _ in range(bound):
        answer.append(field.mul(answer[-1], value))
    return answer


def tangent_polynomial(
    fixed: int,
    field: FiniteField,
    reverse: bool = False,
) -> list[int]:
    fixed_powers = powers(fixed, 5, field)
    answer = [0] * 6
    for coefficient, i, j in TANGENT_TERMS:
        fixed_degree, variable_degree = (j, i) if reverse else (i, j)
        term = field.mul(coefficient % field.p, fixed_powers[fixed_degree])
        answer[variable_degree] = field.add(answer[variable_degree], term)
    return trim(answer)


def evaluate_tangent(r: int, t: int, field: FiniteField) -> int:
    rp = powers(r, 5, field)
    tp = powers(t, 5, field)
    answer = 0
    for coefficient, i, j in TANGENT_TERMS:
        term = field.mul(
            coefficient % field.p,
            field.mul(rp[i], tp[j]),
        )
        answer = field.add(answer, term)
    return answer


def geometric_packet(field: FiniteField) -> tuple[int, int, int, int, int]:
    affine = 0
    diagonal = 0
    bitangent = 0
    for r in range(field.q):
        forward = tangent_polynomial(r, field)
        affine += rational_root_count(forward, field)

        diagonal_here = evaluate_tangent(r, r, field) == 0
        diagonal += diagonal_here

        reverse = tangent_polynomial(r, field, reverse=True)
        common = poly_gcd(forward, reverse, field)
        bitangent += rational_root_count(common, field) - diagonal_here

    top_terms = tuple(
        term for term in TANGENT_TERMS if term[1] + term[2] == 5
    )
    infinity = 0
    for r in range(field.q):
        rp = powers(r, 5, field)
        value = 0
        for coefficient, i, j in top_terms:
            value = field.add(
                value,
                field.mul(coefficient % field.p, rp[i]),
            )
        infinity += value == 0
    infinity += (-12) % field.p == 0

    projective = affine + infinity
    trace = field.q + 1 - projective
    correction = -2 + 2 * infinity + 2 * diagonal + bitangent
    return trace, infinity, diagonal, bitangent, correction


def geometric_packet_brute(
    field: FiniteField,
) -> tuple[int, int, int, int, int]:
    affine = 0
    diagonal = 0
    bitangent = 0
    for r in range(field.q):
        for t in range(field.q):
            if evaluate_tangent(r, t, field) != 0:
                continue
            affine += 1
            if r == t:
                diagonal += 1
            elif evaluate_tangent(t, r, field) == 0:
                bitangent += 1

    top_terms = tuple(
        term for term in TANGENT_TERMS if term[1] + term[2] == 5
    )
    infinity = 0
    for r in range(field.q):
        rp = powers(r, 5, field)
        value = 0
        for coefficient, i, _ in top_terms:
            value = field.add(
                value,
                field.mul(coefficient % field.p, rp[i]),
            )
        infinity += value == 0
    infinity += (-12) % field.p == 0
    trace = field.q + 1 - affine - infinity
    correction = -2 + 2 * infinity + 2 * diagonal + bitangent
    return trace, infinity, diagonal, bitangent, correction


def newton_l_polynomial(p: int, traces: list[int]) -> list[int]:
    """Return the genus-six L-polynomial from traces at levels 1,...,6."""

    elementary = [1]
    for n in range(1, 7):
        numerator = sum(
            (-1) ** (j - 1) * elementary[n - j] * traces[j - 1]
            for j in range(1, n + 1)
        )
        assert numerator % n == 0
        elementary.append(numerator // n)

    coefficients = [(-1) ** n * elementary[n] for n in range(7)]
    coefficients.extend(
        p ** (n - 6) * coefficients[12 - n]
        for n in range(7, 13)
    )
    return coefficients


def trace_recurrence(
    polynomial: list[int],
    initial: list[int],
    r: int,
) -> int:
    traces = {index + 1: value for index, value in enumerate(initial)}
    for n in range(7, 13):
        value = -n * polynomial[n]
        for j in range(1, n):
            value -= polynomial[j] * traces[n - j]
        traces[n] = value
    for n in range(13, r + 1):
        traces[n] = -sum(
            polynomial[j] * traces[n - j] for j in range(1, 13)
        )
    return traces[r]


def finite_correction(r: int) -> int:
    return (
        2 * (r % 2 == 0)
        + 16 * (r % 4 == 0)
        + 10 * (r % 5 == 0)
        + 10 * (r % 10 == 0)
    )


def verify_symbolic_certificates() -> None:
    import warnings

    import sympy as sp
    from sympy.utilities.exceptions import SymPyDeprecationWarning

    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)
    r, t, z = sp.symbols("r t z")
    x = sp.symbols("x")
    for degree, coefficients in MODULI.items():
        modulus = sum(
            coefficient * x**i for i, coefficient in enumerate(coefficients)
        )
        if degree > 1:
            assert sp.Poly(modulus, x, modulus=P).is_irreducible

    homogeneous = sum(
        coefficient * r**i * t**j * z ** (5 - i - j)
        for coefficient, i, j in TANGENT_TERMS
    )
    affine = homogeneous.subs(z, 1)
    derivatives = [sp.diff(homogeneous, variable) for variable in (r, t, z)]
    basis = sp.groebner(
        [affine, derivatives[0].subs(z, 1), derivatives[1].subs(z, 1)],
        r,
        t,
        modulus=P,
    )
    assert len(basis.polys) == 1 and basis.polys[0].as_expr() == 1

    for substitutions, variable in (
        ({t: 1, z: 0}, r),
        ({r: 1, z: 0}, t),
    ):
        values = [
            sp.Poly(poly.subs(substitutions), variable, modulus=P)
            for poly in [homogeneous] + derivatives
        ]
        gcd = values[0]
        for value in values[1:]:
            gcd = sp.gcd(gcd, value)
        assert gcd.degree() == 0

    top = homogeneous.subs({t: 1, z: 0})
    diagonal = affine.subs(t, r)
    reversed_affine = affine.xreplace({r: t, t: r})
    resultant = sp.resultant(affine, reversed_affine, t)

    def degrees(poly: sp.Expr) -> list[int]:
        _, factors = sp.factor_list(poly, r, modulus=P)
        assert all(exponent == 1 for _, exponent in factors)
        return sorted(sp.degree(factor, r) for factor, _ in factors)

    assert degrees(top) == [1, 4]
    assert degrees(diagonal) == [5]
    assert degrees(resultant) == [2, 4, 4, 5, 10]

    characteristic = (
        x**12
        + 2 * x**9
        + 7 * x**8
        - 16 * x**7
        - 34 * x**6
        - 80 * x**5
        + 175 * x**4
        + 250 * x**3
        + 15625
    )
    _, rational_factors = sp.factor_list(characteristic, x)
    assert len(rational_factors) == 1
    assert sp.degree(rational_factors[0][0], x) == 12
    y = sp.symbols("y")
    real_factor = y**6 - 30 * y**4 + 2 * y**3 + 232 * y**2 - 46 * y - 354
    assert sp.Poly(real_factor, y, modulus=23).is_irreducible
    assert sp.resultant(real_factor, y**2 - 20, y) == 81076


def main() -> None:
    verify_symbolic_certificates()

    packets = []
    for degree in range(1, 7):
        field = FiniteField(P, degree)
        packet = geometric_packet(field)
        if degree <= 2:
            assert packet == geometric_packet_brute(field)
        assert packet[4] == finite_correction(degree)
        packets.append(packet)
        print("degree", degree, "packet", packet, flush=True)

    traces = [packet[0] for packet in packets]
    polynomial = newton_l_polynomial(P, traces)
    assert polynomial[12] == P**6
    for n in range(7):
        assert polynomial[12 - n] == P ** (6 - n) * polynomial[n]
    assert all(
        trace_recurrence(polynomial, traces, r) == traces[r - 1]
        for r in range(1, 7)
    )

    corrected = []
    raw = []
    for r, packet in enumerate(packets, start=1):
        q = P**r
        trace, _, _, _, correction = packet
        variance = (q - 1) * (q * q + 2 * trace + correction)
        raw.append(variance)
        packet_value = 2 * trace + correction
        corrected.append(variance - (q - 1) * packet_value)
        assert corrected[-1] == q**3 - q**2

    for r in range(2, 7):
        assert valuation(corrected[r - 1] - corrected[r - 2], P) == 2 * r - 2

    # Modulo 5 the trace recurrence has period 39.  The finite packet has
    # period 4 modulo 5, so the raw obstruction has period 156.
    trace_mod = [None] + [value % P for value in traces]
    for r in range(7, 158):
        trace_mod.append(
            -sum(polynomial[j] * trace_mod[r - j] for j in range(1, 7))
            % P
        )
    assert all(trace_mod[r + 39] == trace_mod[r] for r in range(1, 119))
    for divisor in (1, 3, 13):
        assert any(
            trace_mod[r + divisor] != trace_mod[r]
            for r in range(1, 40)
        )
    packet_mod = [
        None,
        *[
            (2 * trace_mod[r] + finite_correction(r)) % P
            for r in range(1, 158)
        ],
    ]
    divisible_classes = {
        1,
        10,
        16,
        30,
        32,
        33,
        36,
        38,
        42,
        48,
        49,
        55,
        64,
        69,
        71,
        75,
        77,
        81,
        84,
        87,
        92,
        98,
        103,
        118,
        123,
        131,
        137,
        150,
    }
    observed_classes = {
        r % 156
        for r in range(2, 158)
        if packet_mod[r] == packet_mod[r - 1]
    }
    assert observed_classes == divisible_classes

    print("L-polynomial coefficients:", polynomial)
    print("curve traces:", traces)
    print(
        "raw adjacent valuations:",
        [valuation(raw[r - 1] - raw[r - 2], P) for r in range(2, 7)],
    )
    print("raw mod-5 divisibility classes mod 156:", sorted(divisible_classes))
    print("corrected counts:", corrected)
    print("PASS")


if __name__ == "__main__":
    main()
