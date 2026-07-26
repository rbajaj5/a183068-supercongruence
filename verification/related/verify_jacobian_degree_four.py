"""Exact checks for JacobianDegreeFourFrobeniusObstruction.md."""

from collections import Counter


A_TERMS = (
    (-243, 6, 4, 2),
    (-1944, 5, 5, 1),
    (-324, 5, 3, 2),
    (-3888, 4, 6, 0),
    (-2106, 4, 4, 1),
    (-162, 4, 2, 2),
    (-3240, 3, 5, 0),
    (-648, 3, 3, 1),
    (-36, 3, 1, 2),
    (-243, 2, 4, 0),
    (36, 2, 2, 1),
    (-3, 2, 0, 2),
    (396, 1, 3, 0),
    (48, 1, 1, 1),
    (87, 0, 2, 0),
    (6, 0, 0, 1),
)

B_TERMS = (
    (-54, 6, 3, 2),
    (-432, 5, 4, 1),
    (-54, 5, 2, 2),
    (-864, 4, 5, 0),
    (-324, 4, 3, 1),
    (-18, 4, 1, 2),
    (-432, 3, 4, 0),
    (-36, 3, 2, 1),
    (-2, 3, 0, 2),
    (90, 2, 3, 0),
    (20, 2, 1, 1),
    (58, 1, 2, 0),
    (4, 1, 0, 1),
    (1, 0, 1, 0),
)


def valuation(number: int, p: int) -> int:
    assert number
    answer = 0
    while number % p == 0:
        answer += 1
        number //= p
    return answer


def legendre(a: int, p: int) -> int:
    residue = a % p
    if residue == 0:
        return 0
    return 1 if pow(residue, (p - 1) // 2, p) == 1 else -1


def kappa_prime(p: int) -> int:
    return 3 + legendre(2, p) + 2 * legendre(-2, p) + 2 * legendre(6, p)


def kappa_level(p: int, r: int) -> int:
    if r % 2 == 0:
        return 8
    return kappa_prime(p)


def variance_formula(p: int, r: int) -> int:
    q = p**r
    return (q - 1) * (q * q + kappa_level(p, r))


def evaluate_prime_field(p: int) -> int:
    fibers: Counter[tuple[int, int, int]] = Counter()
    for x in range(p):
        xp = [1]
        for _ in range(6):
            xp.append(xp[-1] * x % p)
        for y in range(p):
            yp = [1]
            for _ in range(6):
                yp.append(yp[-1] * y % p)
            for z in range(p):
                zp = (1, z, z * z % p)
                a = sum(
                    coefficient * xp[i] * yp[j] * zp[k]
                    for coefficient, i, j, k in A_TERMS
                ) % p
                b = sum(
                    coefficient * xp[i] * yp[j] * zp[k]
                    for coefficient, i, j, k in B_TERMS
                ) % p
                c = (x - 4 * x * x * y - x * x * x * z) % p
                fibers[(a, b, c)] += 1
    return sum(m * (m - 1) for m in fibers.values())


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


def evaluate_terms(
    terms: tuple[tuple[int, int, int, int], ...],
    xp: list[int],
    yp: list[int],
    zp: tuple[int, int, int],
    field: QuadraticField,
) -> int:
    answer = 0
    for coefficient, i, j, k in terms:
        monomial = field.mul[field.mul[xp[i]][yp[j]]][zp[k]]
        term = field.mul[coefficient % field.p][monomial]
        answer = field.add[answer][term]
    return answer


def evaluate_quadratic_extension(p: int) -> int:
    field = QuadraticField(p)
    q, add, mul = field.q, field.add, field.mul
    fibers: Counter[tuple[int, int, int]] = Counter()

    for x in range(q):
        xp = [1]
        for _ in range(6):
            xp.append(mul[xp[-1]][x])
        for y in range(q):
            yp = [1]
            for _ in range(6):
                yp.append(mul[yp[-1]][y])
            for z in range(q):
                zp = (1, z, mul[z][z])
                a = evaluate_terms(A_TERMS, xp, yp, zp, field)
                b = evaluate_terms(B_TERMS, xp, yp, zp, field)
                c = add[
                    add[x][field.neg(mul[mul[xp[2]][y]][4 % p])]
                ][field.neg(mul[xp[3]][z])]
                fibers[(a, b, c)] += 1
    return sum(m * (m - 1) for m in fibers.values())


def verify_tangency_formula(p: int) -> None:
    tangent_first = {
        (r, s)
        for r in range(p)
        for s in range(p)
        if r != s and (3 * r * r + 2 * r * s + s * s - 1) % p == 0
    }
    tangent_second = {
        (r, s)
        for r in range(p)
        for s in range(p)
        if r != s and (r * r + 2 * r * s + 3 * s * s - 1) % p == 0
    }
    expected_first = p - 1 - legendre(-2, p) - legendre(6, p)
    assert len(tangent_first) == expected_first
    assert len(tangent_second) == expected_first
    assert len(tangent_first & tangent_second) == 1 + legendre(2, p)

    good = p * (p - 1) - len(tangent_first | tangent_second)
    expected_good = (
        p * p
        - 3 * p
        + 3
        + legendre(2, p)
        + 2 * legendre(-2, p)
        + 2 * legendre(6, p)
    )
    assert good == expected_good
    assert (p - 1) * good + 3 * p * (p - 1) == variance_formula(p, 1)


def verify_valuations() -> tuple[int, int, int]:
    adjacent_cases = 0
    two_step_cases = 0
    corrected_cases = 0
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 73):
        for r in range(2, 9):
            current = variance_formula(p, r)
            previous = variance_formula(p, r - 1)
            expected = r - 1 if p % 24 == 1 else 0
            assert valuation(current - previous, p) == expected
            adjacent_cases += 1

            corrected_current = current + kappa_level(p, r)
            corrected_previous = previous + kappa_level(p, r - 1)
            exceptional = p % 24 == 7 and r % 2 == 0
            expected_corrected = r if exceptional else r - 1
            assert (
                valuation(corrected_current - corrected_previous, p)
                == expected_corrected
            )
            corrected_cases += 1

            if r >= 3:
                two_back = variance_formula(p, r - 2)
                exceptional_two = p % 24 == 7 and r % 2 == 1
                expected_two = 2 * r - 4 if exceptional_two else r - 2
                assert valuation(current - two_back, p) == expected_two
                two_step_cases += 1
    return adjacent_cases, two_step_cases, corrected_cases


def verify_zeta_expansion() -> int:
    cases = 0
    for p in (5, 7, 11, 13, 17, 19, 23):
        epsilons = (
            (legendre(2, p), 1),
            (legendre(-2, p), 2),
            (legendre(6, p), 2),
        )
        for r in range(1, 8):
            q = p**r
            from_factors = 2 * q**3 - q**2 + 3 * q - 3
            from_factors += sum(
                weight * ((epsilon * p) ** r - epsilon**r)
                for epsilon, weight in epsilons
            )
            assert from_factors == q**3 + variance_formula(p, r)
            cases += 1
    return cases


def main() -> None:
    prime_cases = (5, 7, 11, 13, 17, 19, 23, 29, 31)
    for p in prime_cases:
        verify_tangency_formula(p)
        assert evaluate_prime_field(p) == variance_formula(p, 1)

    quadratic_cases = (5, 7, 11)
    for p in quadratic_cases:
        assert evaluate_quadratic_extension(p) == variance_formula(p, 2)

    adjacent, two_step, corrected = verify_valuations()
    zeta_cases = verify_zeta_expansion()
    print(
        "PASS:",
        len(prime_cases),
        "prime-field collision cases;",
        len(quadratic_cases),
        "quadratic-extension cases;",
        adjacent,
        "adjacent valuations;",
        two_step,
        "two-step valuations;",
        corrected,
        "corrected valuations.",
        zeta_cases,
        "zeta-expansion cases.",
    )


if __name__ == "__main__":
    main()
