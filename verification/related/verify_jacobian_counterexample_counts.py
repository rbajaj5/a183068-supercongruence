"""Exact checks for JacobianCounterexampleFiniteFieldCounts.md."""

from collections import Counter


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def variance_formula(q: int, characteristic: int) -> int:
    if characteristic == 3:
        return q * q * (q - 1)
    return (q - 1) * (q * q + 2)


def expected_distribution(q: int, characteristic: int) -> tuple[int, ...]:
    variance = variance_formula(q, characteristic)
    return (
        variance // 3,
        q**3 - variance // 2,
        0,
        variance // 6,
    )


def assert_counting_identities(q: int, characteristic: int) -> None:
    n0, n1, n2, n3 = expected_distribution(q, characteristic)
    assert n2 == 0
    assert n0 + n1 + n3 == q**3
    assert n1 + 3 * n3 == q**3
    assert n0 == 2 * n3
    assert n0 + 4 * n3 == variance_formula(q, characteristic)

    if characteristic == 3:
        split = q * q * (q - 1) // 6
        linear_quadratic = q * q * (q - 1) // 2
        irreducible = q * q * (q - 1) // 3
        double_simple = q * q
        triple = 0
    else:
        split = (q - 1) * (q * q + 2) // 6
        linear_quadratic = q * q * (q - 1) // 2
        irreducible = (q - 1) * (q * q - 1) // 3
        double_simple = q * q - q + 1
        triple = q - 1

    assert split == n3
    assert irreducible + triple == n0
    assert linear_quadratic + double_simple == n1
    assert split + linear_quadratic + irreducible == q**3 - q**2
    assert double_simple + triple == q**2
    assert split - linear_quadratic + irreducible == 0
    expected_standard_trace = 0 if characteristic == 3 else q - 1
    assert 2 * split - irreducible == expected_standard_trace


def direct_prime_field(p: int) -> tuple[int, ...]:
    fibers: Counter[tuple[int, int, int]] = Counter()
    for x in range(p):
        x2 = x * x % p
        x3 = x2 * x % p
        for y in range(p):
            y2 = y * y % p
            xy = x * y % p
            u = (1 + xy) % p
            u2 = u * u % p
            u3 = u2 * u % p
            four_plus = (4 + 3 * xy) % p
            constant_p = y2 * u * four_plus % p
            constant_q = (y + 3 * x * y2 * four_plus) % p
            coefficient_q = 3 * x * u2 % p
            constant_r = (2 * x - 3 * x2 * y) % p
            coefficient_r = -x3 % p
            for z in range(p):
                target = (
                    (u3 * z + constant_p) % p,
                    (constant_q + coefficient_q * z) % p,
                    (constant_r + coefficient_r * z) % p,
                )
                fibers[target] += 1

    result = Counter(fibers.values())
    result[0] = p**3 - len(fibers)
    assert max(fibers.values()) == 3
    return tuple(result[j] for j in range(4))


class QuadraticField:
    """Small table implementation of F_p(alpha), alpha^2 = nonsquare."""

    def __init__(self, p: int):
        self.p = p
        self.q = p * p
        squares = {a * a % p for a in range(p)}
        self.nonsquare = next(a for a in range(2, p) if a not in squares)
        self.add = [[0] * self.q for _ in range(self.q)]
        self.mul = [[0] * self.q for _ in range(self.q)]
        for x in range(self.q):
            a, b = x % p, x // p
            for y in range(self.q):
                c, d = y % p, y // p
                self.add[x][y] = (a + c) % p + p * ((b + d) % p)
                self.mul[x][y] = (
                    (a * c + b * d * self.nonsquare) % p
                    + p * ((a * d + b * c) % p)
                )

    def neg(self, x: int) -> int:
        return (-x % self.p) + self.p * (-(x // self.p) % self.p)


def direct_quadratic_extension(p: int) -> tuple[int, ...]:
    field = QuadraticField(p)
    q, add, mul = field.q, field.add, field.mul
    c2, c3, c4 = 2 % p, 3 % p, 4 % p
    fibers: Counter[tuple[int, int, int]] = Counter()

    for x in range(q):
        x2 = mul[x][x]
        x3 = mul[x2][x]
        for y in range(q):
            y2 = mul[y][y]
            xy = mul[x][y]
            u = add[1][xy]
            u2 = mul[u][u]
            u3 = mul[u2][u]
            four_plus = add[c4][mul[c3][xy]]
            constant_p = mul[mul[y2][u]][four_plus]
            constant_q = add[y][mul[mul[mul[c3][x]][y2]][four_plus]]
            coefficient_q = mul[mul[c3][x]][u2]
            constant_r = add[mul[c2][x]][field.neg(mul[mul[c3][x2]][y])]
            coefficient_r = field.neg(x3)
            for z in range(q):
                target = (
                    add[mul[u3][z]][constant_p],
                    add[constant_q][mul[coefficient_q][z]],
                    add[constant_r][mul[coefficient_r][z]],
                )
                fibers[target] += 1

    result = Counter(fibers.values())
    result[0] = q**3 - len(fibers)
    assert max(fibers.values()) == 3
    return tuple(result[j] for j in range(4))


def verify_adjacent_valuations() -> int:
    cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        for r in range(2, 8):
            current = variance_formula(p**r, p)
            previous = variance_formula(p ** (r - 1), p)
            expected = 2 * r - 2 if p == 3 else r - 1
            assert valuation(current - previous, p) == expected

            collision_current = p ** (3 * r) + current
            collision_previous = p ** (3 * (r - 1)) + previous
            assert (
                valuation(collision_current - collision_previous, p)
                == expected
            )
            cases += 1
    return cases


def main() -> None:
    prime_cases = (3, 5, 7, 11, 13, 17, 19)
    for p in prime_cases:
        assert_counting_identities(p, p)
        assert direct_prime_field(p) == expected_distribution(p, p)

    quadratic_cases = (3, 5, 7, 11)
    for p in quadratic_cases:
        q = p * p
        assert_counting_identities(q, p)
        assert direct_quadratic_extension(p) == expected_distribution(q, p)

    symbolic_cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        for r in range(1, 8):
            assert_counting_identities(p**r, p)
            symbolic_cases += 1

    valuation_cases = verify_adjacent_valuations()
    print(
        "PASS:",
        len(prime_cases),
        "prime-field brute-force cases;",
        len(quadratic_cases),
        "quadratic-extension brute-force cases;",
        symbolic_cases,
        "counting-identity cases;",
        valuation_cases,
        "exact adjacent-valuation cases.",
    )


if __name__ == "__main__":
    main()
