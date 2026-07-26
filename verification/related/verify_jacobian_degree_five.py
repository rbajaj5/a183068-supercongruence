"""Exact checks for JacobianDegreeFiveEllipticFrobenius.md."""

from collections import Counter


# The first two target coordinates have been multiplied by 393660 and
# 196830, respectively.  The third has been multiplied by 27.  These are
# invertible coordinate changes in every characteristic used below.
A_TERMS = (
    (-314928, 9, 5, 3),
    (1294704, 8, 6, 2),
    (-1574640, 8, 4, 3),
    (-1774224, 7, 7, 1),
    (5528736, 7, 5, 2),
    (-3149280, 7, 3, 3),
    (810448, 6, 8, 0),
    (-6281712, 6, 6, 1),
    (8518365, 6, 4, 2),
    (-3149280, 6, 2, 3),
    (2278016, 5, 7, 0),
    (-6549174, 5, 5, 1),
    (4680180, 5, 3, 2),
    (-1574640, 5, 1, 3),
    (1082509, 4, 6, 0),
    (781650, 4, 4, 1),
    (-1202850, 4, 2, 2),
    (-314928, 4, 0, 3),
    (-2070578, 3, 5, 0),
    (4373352, 3, 3, 1),
    (-2248236, 3, 1, 2),
    (-961417, 2, 4, 0),
    (-94608, 2, 2, 1),
    (-649539, 2, 0, 2),
    (2485204, 1, 3, 0),
    (-2707506, 1, 1, 1),
    (1761102, 0, 2, 0),
    (-1062882, 0, 0, 1),
)

B_TERMS = (
    (-196830, 9, 4, 3),
    (809190, 8, 5, 2),
    (-787320, 8, 3, 3),
    (-1108890, 7, 6, 1),
    (2646270, 7, 4, 2),
    (-1180980, 7, 2, 3),
    (506530, 6, 7, 0),
    (-2817180, 6, 5, 1),
    (2690010, 6, 3, 2),
    (-787320, 6, 1, 3),
    (917230, 5, 6, 0),
    (-1309770, 5, 4, 1),
    (284310, 5, 2, 2),
    (-196830, 5, 0, 3),
    (-217560, 4, 5, 0),
    (1688040, 4, 3, 1),
    (-962280, 4, 1, 2),
    (-1017860, 3, 4, 0),
    (852849, 3, 2, 1),
    (-393660, 3, 0, 2),
    (554401, 2, 3, 0),
    (-1164942, 2, 1, 1),
    (1213731, 1, 2, 0),
    (-728271, 1, 0, 1),
    (72900, 0, 1, 0),
)


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def tangent_first(r: int, t: int, add: list[list[int]], mul: list[list[int]], p: int) -> int:
    def scale(c: int, x: int) -> int:
        return mul[c % p][x]

    r2, t2 = mul[r][r], mul[t][t]
    r3, t3 = mul[r2][r], mul[t2][t]
    terms = (
        scale(-16, r3),
        scale(-12, mul[r2][t]),
        scale(15, r2),
        scale(-8, mul[r][t2]),
        scale(10, mul[r][t]),
        scale(-36, r),
        scale(-4, t3),
        scale(5, t2),
        scale(-18, t),
        17 % p,
    )
    answer = 0
    for term in terms:
        answer = add[answer][term]
    return answer


def infinity_polynomial(x: int, add: list[list[int]], mul: list[list[int]], p: int) -> int:
    x2, x3 = mul[x][x], mul[mul[x][x]][x]
    answer = add[mul[4 % p][x3]][mul[3 % p][x2]]
    answer = add[answer][mul[2 % p][x]]
    return add[answer][1]


def diagonal_polynomial(x: int, add: list[list[int]], mul: list[list[int]], p: int) -> int:
    x2, x3 = mul[x][x], mul[mul[x][x]][x]
    answer = add[mul[40 % p][x3]][mul[(-30) % p][x2]]
    answer = add[answer][mul[54 % p][x]]
    return add[answer][(-17) % p]


class FiniteField:
    """Table implementation of F_p or F_p(alpha), alpha^2 = nonsquare."""

    def __init__(self, p: int, degree: int = 1):
        assert degree in (1, 2)
        self.p = p
        self.degree = degree
        self.q = p**degree
        self.add = [[0] * self.q for _ in range(self.q)]
        self.mul = [[0] * self.q for _ in range(self.q)]
        if degree == 1:
            for x in range(p):
                for y in range(p):
                    self.add[x][y] = (x + y) % p
                    self.mul[x][y] = x * y % p
            return

        squares = {a * a % p for a in range(p)}
        nonsquare = next(a for a in range(2, p) if a not in squares)
        for x in range(self.q):
            a, b = x % p, x // p
            for y in range(self.q):
                c, d = y % p, y // p
                self.add[x][y] = (a + c) % p + p * ((b + d) % p)
                self.mul[x][y] = (
                    (a * c + b * d * nonsquare) % p
                    + p * ((a * d + b * c) % p)
                )

    def neg(self, x: int) -> int:
        if self.degree == 1:
            return -x % self.p
        return (-x % self.p) + self.p * (-(x // self.p) % self.p)


def powers(x: int, bound: int, field: FiniteField) -> list[int]:
    answer = [1]
    for _ in range(bound):
        answer.append(field.mul[answer[-1]][x])
    return answer


def evaluate_terms(
    terms: tuple[tuple[int, int, int, int], ...],
    xp: list[int],
    yp: list[int],
    zp: list[int],
    field: FiniteField,
) -> int:
    answer = 0
    for coefficient, i, j, k in terms:
        monomial = field.mul[field.mul[xp[i]][yp[j]]][zp[k]]
        answer = field.add[answer][field.mul[coefficient % field.p][monomial]]
    return answer


def direct_collision_count(field: FiniteField) -> int:
    q, p, add, mul = field.q, field.p, field.add, field.mul
    fibers: Counter[tuple[int, int, int]] = Counter()
    for x in range(q):
        xp = powers(x, 9, field)
        for y in range(q):
            yp = powers(y, 8, field)
            for z in range(q):
                zp = powers(z, 3, field)
                a = evaluate_terms(A_TERMS, xp, yp, zp, field)
                b = evaluate_terms(B_TERMS, xp, yp, zp, field)
                c = add[
                    add[mul[27 % p][x]][mul[(-37) % p][mul[xp[2]][y]]]
                ][mul[27 % p][mul[xp[3]][z]]]
                fibers[(a, b, c)] += 1
    return sum(m * (m - 1) for m in fibers.values())


def geometric_packet(field: FiniteField) -> tuple[int, int, int, int, int]:
    q, p, add, mul = field.q, field.p, field.add, field.mul
    affine_curve = 0
    bitangencies = 0
    for r in range(q):
        for t in range(q):
            first = tangent_first(r, t, add, mul, p)
            if first == 0:
                affine_curve += 1
                if r != t and tangent_first(t, r, add, mul, p) == 0:
                    bitangencies += 1

    infinity = sum(
        infinity_polynomial(x, add, mul, p) == 0 for x in range(q)
    )
    diagonal = sum(
        diagonal_polynomial(x, add, mul, p) == 0 for x in range(q)
    )
    projective_curve = affine_curve + infinity
    trace = q + 1 - projective_curve
    correction = -2 + 2 * infinity + 2 * diagonal + bitangencies
    return trace, infinity, diagonal, bitangencies, correction


def collision_formula(field: FiniteField) -> int:
    trace, _, _, _, correction = geometric_packet(field)
    q = field.q
    # In characteristic 17 the curved C=0 sheet is one-to-one rather than
    # two-to-one, reducing the boundary contribution by q(q-1).
    boundary_exception = q if field.p == 17 else 0
    return (q - 1) * (
        q * q - boundary_exception + 2 * trace + correction
    )


def elliptic_count(field: FiniteField) -> int:
    """Count Y^2 = X^3 - 2594700 X - 2076643440, including infinity."""

    q, p, add, mul = field.q, field.p, field.add, field.mul
    answer = 1
    for x in range(q):
        x3 = mul[mul[x][x]][x]
        right = add[
            add[x3][mul[(-2594700) % p][x]]
        ][(-2076643440) % p]
        answer += sum(mul[y][y] == right for y in range(q))
    return answer


# Polynomial arithmetic over F_p, with coefficients in increasing order.
def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim([x % p for x in a])
    b = trim([x % p for x in b])
    quotient = [0] * max(1, len(a) - len(b) + 1)
    inverse = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        degree = len(a) - len(b)
        coefficient = a[-1] * inverse % p
        quotient[degree] = coefficient
        for i, value in enumerate(b):
            a[degree + i] = (a[degree + i] - coefficient * value) % p
        trim(a)
    return trim(quotient), trim(a)


def poly_mul_mod(a: list[int], b: list[int], modulus: list[int], p: int) -> list[int]:
    product = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            product[i + j] = (product[i + j] + x * y) % p
    return poly_divmod(product, modulus, p)[1]


def poly_pow_mod(base: list[int], exponent: int, modulus: list[int], p: int) -> list[int]:
    answer = [1]
    while exponent:
        if exponent & 1:
            answer = poly_mul_mod(answer, base, modulus, p)
        base = poly_mul_mod(base, base, modulus, p)
        exponent //= 2
    return answer


def poly_gcd(a: list[int], b: list[int], p: int) -> list[int]:
    a, b = trim(a), trim(b)
    while b != [0]:
        a, b = b, poly_divmod(a, b, p)[1]
    inverse = pow(a[-1], -1, p)
    return [(coefficient * inverse) % p for coefficient in a]


def factor_degree_counts(poly: list[int], p: int) -> dict[int, int]:
    """Number of distinct irreducible factors of every degree."""

    poly = trim([coefficient % p for coefficient in poly])
    degree = len(poly) - 1
    roots_in_extension: dict[int, int] = {}
    irreducibles: dict[int, int] = {}
    for d in range(1, degree + 1):
        x_power = poly_pow_mod([0, 1], p**d, poly, p)
        difference = x_power[:]
        if len(difference) < 2:
            difference += [0] * (2 - len(difference))
        difference[1] = (difference[1] - 1) % p
        roots_in_extension[d] = len(poly_gcd(poly, difference, p)) - 1
        accounted = sum(
            e * irreducibles[e]
            for e in irreducibles
            if d % e == 0
        )
        irreducibles[d] = (roots_in_extension[d] - accounted) // d
    return {d: count for d, count in irreducibles.items() if count}


def roots_at_level(factors: dict[int, int], r: int) -> int:
    return sum(degree * count for degree, count in factors.items() if r % degree == 0)


INFINITY_POLY = [1, 2, 3, 4]
DIAGONAL_POLY = [-17, 54, -30, 40]
BITANGENCY_POLY = [
    13550,
    -29679,
    47269,
    -34600,
    33280,
    -9600,
    6400,
]


def verify_towers() -> tuple[int, int, int]:
    formula_cases = 0
    obstruction_cases = 0
    corrected_cases = 0
    for p in (7, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53):
        factors_i = factor_degree_counts(INFINITY_POLY, p)
        factors_d = factor_degree_counts(DIAGONAL_POLY, p)
        factors_h = factor_degree_counts(BITANGENCY_POLY, p)

        field = FiniteField(p)
        trace_1, _, _, _, _ = geometric_packet(field)
        traces = {0: 2, 1: trace_1}

        previous_corrected = None
        previous_variance = None
        for r in range(1, 9):
            if r >= 2:
                traces[r] = trace_1 * traces[r - 1] - p * traces[r - 2]
            q = p**r
            correction = (
                -2
                + 2 * roots_at_level(factors_i, r)
                + 2 * roots_at_level(factors_d, r)
                + roots_at_level(factors_h, r)
            )
            packet = 2 * traces[r] + correction - (q if p == 17 else 0)
            variance = (q - 1) * (q * q + packet)
            corrected = variance - (q - 1) * packet
            assert corrected == q**3 - q**2
            formula_cases += 1

            if r >= 2:
                assert valuation(corrected - previous_corrected, p) == 2 * r - 2
                corrected_cases += 1
                previous_q = p ** (r - 1)
                previous_packet = (
                    2 * traces[r - 1]
                    - 2
                    + 2 * roots_at_level(factors_i, r - 1)
                    + 2 * roots_at_level(factors_d, r - 1)
                    + roots_at_level(factors_h, r - 1)
                    - (previous_q if p == 17 else 0)
                )
                expected_mod_p = (-packet + previous_packet) % p
                assert (variance - previous_variance) % p == expected_mod_p
                obstruction_cases += 1

            previous_variance = variance
            previous_corrected = corrected
    return formula_cases, obstruction_cases, corrected_cases


def main() -> None:
    prime_cases = (7, 11, 13, 17, 19, 23, 29, 31)
    for p in prime_cases:
        field = FiniteField(p)
        assert direct_collision_count(field) == collision_formula(field)

    quadratic_cases = (7,)
    for p in quadratic_cases:
        field = FiniteField(p, 2)
        assert direct_collision_count(field) == collision_formula(field)

    good_curve_primes = (7, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53)
    curve_cases = 0
    for p in good_curve_primes:
        field = FiniteField(p)
        trace, _, _, _, _ = geometric_packet(field)
        assert elliptic_count(field) == p + 1 - trace
        curve_cases += 1
    field = FiniteField(7, 2)
    trace, _, _, _, _ = geometric_packet(field)
    assert elliptic_count(field) == 7**2 + 1 - trace
    curve_cases += 1

    formula_cases, obstruction_cases, corrected_cases = verify_towers()
    print(
        "PASS:",
        len(prime_cases),
        "prime-field collision cases;",
        len(quadratic_cases),
        "quadratic-extension collision case;",
        curve_cases,
        "plane-cubic/Jacobian cases;",
        formula_cases,
        "tower formulas;",
        obstruction_cases,
        "raw-obstruction residues;",
        corrected_cases,
        "corrected exact valuations.",
    )


if __name__ == "__main__":
    main()
