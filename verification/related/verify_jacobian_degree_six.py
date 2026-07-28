"""Exact checks for JacobianDegreeSixGenusThree.md.

The script works in F_7, F_(7^2), and F_(7^3).  Elements of an extension
field are encoded in base 7 against a monic irreducible polynomial.
"""

from array import array
from itertools import product


P = 13


def valuation(number: int, prime: int) -> int:
    assert number
    answer = 0
    while number % prime == 0:
        answer += 1
        number //= prime
    return answer


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def has_root(poly: tuple[int, ...], p: int) -> bool:
    return any(
        sum(coefficient * pow(x, degree, p) for degree, coefficient in enumerate(poly))
        % p
        == 0
        for x in range(p)
    )


def irreducible_polynomial(p: int, degree: int) -> tuple[int, ...]:
    if degree == 1:
        return (0, 1)
    # In degrees two and three, root-free is equivalent to irreducible.
    for lower in product(range(p), repeat=degree):
        candidate = tuple(lower) + (1,)
        if not has_root(candidate, p):
            return candidate
    raise AssertionError("no irreducible polynomial found")


class FiniteField:
    def __init__(self, p: int, degree: int):
        assert degree in (1, 2, 3)
        self.p = p
        self.degree = degree
        self.q = p**degree
        self.modulus = irreducible_polynomial(p, degree)
        self.digits = [self._decode(x) for x in range(self.q)]
        typecode = "H" if self.q < 2**16 else "I"
        self.add = [array(typecode, [0]) * self.q for _ in range(self.q)]
        self.mul = [array(typecode, [0]) * self.q for _ in range(self.q)]
        for x in range(self.q):
            for y in range(self.q):
                self.add[x][y] = self._encode(
                    tuple(
                        (a + b) % p
                        for a, b in zip(self.digits[x], self.digits[y])
                    )
                )
                self.mul[x][y] = self._multiply(
                    self.digits[x],
                    self.digits[y],
                )

    def _decode(self, x: int) -> tuple[int, ...]:
        answer = []
        for _ in range(self.degree):
            answer.append(x % self.p)
            x //= self.p
        return tuple(answer)

    def _encode(self, coefficients: tuple[int, ...] | list[int]) -> int:
        answer = 0
        place = 1
        for coefficient in coefficients:
            answer += coefficient % self.p * place
            place *= self.p
        return answer

    def _multiply(
        self,
        left: tuple[int, ...],
        right: tuple[int, ...],
    ) -> int:
        p = self.p
        product_coefficients = [0] * (2 * self.degree - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                product_coefficients[i + j] = (
                    product_coefficients[i + j] + x * y
                ) % p
        for degree in range(2 * self.degree - 2, self.degree - 1, -1):
            leading = product_coefficients[degree]
            if leading == 0:
                continue
            for i in range(self.degree):
                product_coefficients[degree - self.degree + i] = (
                    product_coefficients[degree - self.degree + i]
                    - leading * self.modulus[i]
                ) % p
        return self._encode(product_coefficients[: self.degree])


# A scalar multiple of the degree-six canonical tangent quartic.
TANGENT_TERMS = (
    (-25, 4, 0),
    (-20, 3, 1),
    (24, 3, 0),
    (-15, 2, 2),
    (18, 2, 1),
    (-10, 1, 3),
    (12, 1, 2),
    (-56, 1, 0),
    (-5, 0, 4),
    (6, 0, 3),
    (-28, 0, 1),
    (27, 0, 0),
)


def powers(x: int, bound: int, field: FiniteField) -> list[int]:
    answer = [1]
    for _ in range(bound):
        answer.append(field.mul[answer[-1]][x])
    return answer


def evaluate_terms(
    terms: tuple[tuple[int, int, int], ...],
    r: int,
    t: int,
    field: FiniteField,
) -> int:
    rp = powers(r, 4, field)
    tp = powers(t, 4, field)
    answer = 0
    for coefficient, i, j in terms:
        monomial = field.mul[rp[i]][tp[j]]
        term = field.mul[coefficient % field.p][monomial]
        answer = field.add[answer][term]
    return answer


def tangent(r: int, t: int, field: FiniteField) -> int:
    return evaluate_terms(TANGENT_TERMS, r, t, field)


def derivative_terms(
    terms: tuple[tuple[int, int, int], ...],
    variable: int,
) -> tuple[tuple[int, int, int], ...]:
    answer = []
    for coefficient, i, j in terms:
        exponent = (i, j)[variable]
        if exponent == 0:
            continue
        powers_ = [i, j]
        powers_[variable] -= 1
        answer.append((coefficient * exponent, powers_[0], powers_[1]))
    return tuple(answer)


R_DERIVATIVE = derivative_terms(TANGENT_TERMS, 0)
T_DERIVATIVE = derivative_terms(TANGENT_TERMS, 1)


def infinity(r: int, t: int, field: FiniteField) -> int:
    return evaluate_terms(
        tuple(term for term in TANGENT_TERMS if term[1] + term[2] == 4),
        r,
        t,
        field,
    )


def diagonal(r: int, field: FiniteField) -> int:
    return tangent(r, r, field)


def verify_smooth(field: FiniteField) -> None:
    q = field.q
    for r in range(q):
        for t in range(q):
            if tangent(r, t, field) != 0:
                continue
            assert (
                evaluate_terms(R_DERIVATIVE, r, t, field) != 0
                or evaluate_terms(T_DERIVATIVE, r, t, field) != 0
            )

    top = tuple(term for term in TANGENT_TERMS if term[1] + term[2] == 4)
    next_part = tuple(
        term for term in TANGENT_TERMS if term[1] + term[2] == 3
    )
    points = [(r, 1) for r in range(q)] + [(1, 0)]
    for r, t in points:
        if evaluate_terms(top, r, t, field) != 0:
            continue
        assert (
            evaluate_terms(derivative_terms(top, 0), r, t, field) != 0
            or evaluate_terms(derivative_terms(top, 1), r, t, field) != 0
            or evaluate_terms(next_part, r, t, field) != 0
        )


def geometric_packet(field: FiniteField) -> tuple[int, int, int, int, int]:
    q = field.q
    affine = 0
    bitangent = 0
    diagonal_count = 0
    for r in range(q):
        if diagonal(r, field) == 0:
            diagonal_count += 1
        for t in range(q):
            if tangent(r, t, field) != 0:
                continue
            affine += 1
            if r != t and tangent(t, r, field) == 0:
                bitangent += 1

    infinity_count = sum(infinity(r, 1, field) == 0 for r in range(q))
    infinity_count += infinity(1, 0, field) == 0
    projective = affine + infinity_count
    trace = q + 1 - projective
    correction = -2 + 2 * infinity_count + 2 * diagonal_count + bitangent
    return trace, infinity_count, diagonal_count, bitangent, correction


def newton_l_polynomial(p: int, traces: list[int]) -> list[int]:
    """Return the genus-three L-polynomial from traces at levels 1,2,3."""

    t1, t2, t3 = traces
    e2 = (t1 * t1 - t2) // 2
    e3 = (t1**3 - 3 * t1 * t2 + 2 * t3) // 6
    return [1, -t1, e2, -e3, p * e2, -(p**2) * t1, p**3]


def trace_recurrence(polynomial: list[int], initial: list[int], r: int) -> int:
    """Power sum recurrence attached to prod(1-alpha*T)."""

    traces = {index + 1: value for index, value in enumerate(initial)}
    # Newton supplies the missing initial traces through degree six.
    for n in range(4, 7):
        value = -n * polynomial[n]
        for j in range(1, n):
            value -= polynomial[j] * traces[n - j]
        traces[n] = value
    for n in range(7, r + 1):
        traces[n] = -sum(
            polynomial[j] * traces[n - j] for j in range(1, 7)
        )
    return traces[r]


def finite_correction(r: int) -> int:
    return (
        6
        + 4 * (r % 2 == 0)
        + 6 * (r % 3 == 0)
        + 4 * (r % 4 == 0)
        + 6 * (r % 6 == 0)
    )


def verify_symbolic_certificates() -> None:
    """Check smoothness and the finite-orbit factorization over F_13."""

    import warnings

    import sympy as sp
    from sympy.utilities.exceptions import SymPyDeprecationWarning

    warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)

    r, t, z = sp.symbols("r t z")
    homogeneous = sum(
        coefficient * r**i * t**j * z ** (4 - i - j)
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

    # There is no singular projective point at infinity.
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
    diagonal_poly = affine.subs(t, r)
    reversed_affine = affine.xreplace({r: t, t: r})
    resultant = sp.resultant(affine, reversed_affine, t)

    def degrees(poly: sp.Expr) -> list[int]:
        _, factors = sp.factor_list(poly, r, modulus=P)
        assert all(exponent == 1 for _, exponent in factors)
        return sorted(sp.degree(factor, r) for factor, _ in factors)

    assert degrees(top) == [1, 3]
    assert degrees(diagonal_poly) == [1, 1, 2]
    assert degrees(resultant) == [1, 1, 1, 1, 2, 4, 6]

    x = sp.symbols("x")
    characteristic = x**6 + 16 * x**4 - 26 * x**3 + 208 * x**2 + 2197
    _, rational_factors = sp.factor_list(characteristic, x)
    assert len(rational_factors) == 1
    assert sp.degree(rational_factors[0][0], x) == 6


def main() -> None:
    verify_symbolic_certificates()
    packets = []
    for degree in (1, 2, 3):
        field = FiniteField(P, degree)
        verify_smooth(field)
        packets.append(geometric_packet(field))

    traces = [packet[0] for packet in packets]
    polynomial = newton_l_polynomial(P, traces)
    assert polynomial[4] == P * polynomial[2]
    assert polynomial[5] == P**2 * polynomial[1]
    assert polynomial[6] == P**3
    assert all(
        trace_recurrence(polynomial, traces, r) == traces[r - 1]
        for r in (1, 2, 3)
    )
    for r, packet in enumerate(packets, start=1):
        assert packet[4] == finite_correction(r)

    variances = []
    corrected = []
    for r, packet in enumerate(packets, start=1):
        q = P**r
        trace, _, _, _, correction = packet
        variance = (q - 1) * (q * q + 2 * trace + correction)
        variances.append(variance)
        corrected.append(variance - (q - 1) * (2 * trace + correction))
        assert corrected[-1] == q**3 - q**2

    for r in (2, 3):
        assert valuation(corrected[r - 1] - corrected[r - 2], P) == 2 * r - 2

    # The raw obstruction has period twelve modulo 13 and never vanishes.
    packet_residues = [
        (
            2 * trace_recurrence(polynomial, traces, r)
            + finite_correction(r)
        )
        % P
        for r in range(1, 25)
    ]
    assert packet_residues[:12] == packet_residues[12:]
    assert packet_residues[:12] == [6, 11, 12, 11, 6, 5, 6, 0, 12, 0, 6, 4]
    assert all(
        packet_residues[r - 1] != packet_residues[r - 2]
        for r in range(2, 25)
    )

    for r in range(2, 13):
        current = P ** (3 * r) - P ** (2 * r)
        previous = P ** (3 * (r - 1)) - P ** (2 * (r - 1))
        assert valuation(current - previous, P) == 2 * r - 2

    print("PASS")
    print("irreducible moduli:", [
        irreducible_polynomial(P, degree) for degree in (1, 2, 3)
    ])
    print("packets (trace,I,D,H,c):", packets)
    print("L-polynomial coefficients:", polynomial)
    print("packet residues mod 13 by r mod 12:", packet_residues[:12])
    print("collision counts:", variances)
    print(
        "raw adjacent valuations:",
        [valuation(variances[r - 1] - variances[r - 2], P) for r in (2, 3)],
    )
    print("corrected counts:", corrected)


if __name__ == "__main__":
    main()
