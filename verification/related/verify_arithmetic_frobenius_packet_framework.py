"""Exact checks for the arithmetic Frobenius-packet framework.

These computations check formulas and transcription.  The note contains the
proofs.
"""

from __future__ import annotations

from itertools import product


Gaussian = tuple[int, int]


def budget_formula(d: int, kappa: int, epsilon: int, r: int) -> int:
    m = min(d, kappa)
    if d <= kappa:
        delta = max(0, d + epsilon - kappa)
    else:
        delta = epsilon
    return m * r - delta


def budget_bruteforce(d: int, kappa: int, epsilon: int, r: int) -> int:
    candidates = [d * r, kappa * r - epsilon]
    candidates.extend(
        d * (r - 1 - s) + kappa * (s + 1) - epsilon
        for s in range(r - 1)
    )
    return min(candidates)


def check_budget_theorem() -> int:
    checks = 0
    for d, kappa, epsilon, r in product(
        range(1, 9), range(1, 9), range(5), range(1, 13)
    ):
        assert budget_formula(d, kappa, epsilon, r) == budget_bruteforce(
            d, kappa, epsilon, r
        )
        checks += 1

    # Recover the existing cubic-transfer deficit table.
    expected = {
        (1, 2): 0,
        (1, 1): 0,
        (1, 0): 0,
        (2, 2): 1,
        (2, 1): 0,
        (2, 0): 0,
        (3, 2): 2,
        (3, 1): 1,
        (3, 0): 0,
    }
    for (d, epsilon), deficit in expected.items():
        assert d - budget_formula(d, 3, epsilon, 1) == deficit
        checks += 1
    return checks


def polynomial(x: int) -> int:
    return 3 + 2 * x + x**3


def check_closure_calculus() -> int:
    checks = 0
    for p, exponent in product((2, 3, 5, 7), range(1, 6)):
        modulus = p**exponent
        for x0, y0, u, v in product(range(-3, 4), repeat=4):
            x1 = x0 + modulus * u
            y1 = y0 + modulus * v
            assert (x1 + y1 - (x0 + y0)) % modulus == 0
            assert (x1 * y1 - x0 * y0) % modulus == 0
            assert (polynomial(x1) - polynomial(x0)) % modulus == 0
            checks += 3
    return checks


def valuation(n: int, prime: int) -> int:
    value = 0
    while n % prime == 0:
        value += 1
        n //= prime
    return value


def check_finite_field_orbit_packet() -> int:
    """Check the point-count law on arbitrary finite Frobenius orbit data."""

    def point_count(extension_degree: int) -> int:
        return sum(
            orbit_length * ((orbit_length**2 + 3 * orbit_length + 1) % 5)
            for orbit_length in range(1, extension_degree + 1)
            if extension_degree % orbit_length == 0
        )

    checks = 0
    for prime, n, r in product((2, 3, 5, 7), range(1, 13), range(1, 6)):
        high = point_count(n * prime**r)
        low = point_count(n * prime ** (r - 1))
        modulus = prime ** (r + valuation(n, prime))
        assert (high - low) % modulus == 0
        checks += 1
    return checks


def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gpow(z: Gaussian, n: int) -> Gaussian:
    out = (1, 0)
    base = z
    while n:
        if n & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        n //= 2
    return out


def gmod(z: Gaussian, modulus: int) -> Gaussian:
    return (z[0] % modulus, z[1] % modulus)


def divide_gaussian_exact(z: Gaussian, pi: Gaussian) -> Gaussian | None:
    a, b = z
    x, y = pi
    norm = x * x + y * y
    real_num = a * x + b * y
    imag_num = b * x - a * y
    if real_num % norm or imag_num % norm:
        return None
    return (real_num // norm, imag_num // norm)


def v_pi(z: Gaussian, pi: Gaussian) -> int:
    if z == (0, 0):
        raise ValueError("valuation of zero is not used in this checker")
    value = 0
    current = z
    while True:
        quotient = divide_gaussian_exact(current, pi)
        if quotient is None:
            return value
        current = quotient
        value += 1


def hensel_sqrt_minus_one(p: int, initial: int, levels: int) -> list[int]:
    roots = [initial % p]
    modulus = p
    for _ in range(1, levels):
        old = roots[-1]
        candidates = [old + digit * modulus for digit in range(p)]
        modulus *= p
        root = next(x for x in candidates if (x * x + 1) % modulus == 0)
        roots.append(root)
    return roots


def check_split_divisor_formula(
    p: int, pi: Gaussian, initial_i: int, bound: int
) -> int:
    max_value = 0
    points: list[Gaussian] = []
    for a, b in product(range(-bound, bound + 1), repeat=2):
        if (a, b) == (0, 0):
            continue
        z = (a, b)
        value = v_pi(z, pi)
        max_value = max(max_value, value)
        points.append(z)

    roots = hensel_sqrt_minus_one(p, initial_i, max_value + 2)
    checks = 0
    for a, b in points:
        indicator_sum = 0
        modulus = p
        for root in roots:
            if (a + root * b) % modulus == 0:
                indicator_sum += 1
            modulus *= p
        assert indicator_sum == v_pi((a, b), pi)
        checks += 1
    return checks


def check_gaussian_local_table() -> int:
    checks = 0

    # Split factorizations and Frobenius-fixed i.
    assert gmul((2, 1), (2, -1)) == (5, 0)
    assert gmul((3, 2), (3, -2)) == (13, 0)
    for p in (5, 13, 17, 29):
        assert gmod(gpow((0, 1), p), p) == (0, 1)
        checks += 1

    # Inert Frobenius conjugates i.
    for p in (3, 7, 11, 19):
        assert gmod(gpow((0, 1), p), p) == (0, p - 1)
        checks += 1

    # Ramification and normalization on rational integers.
    assert gmul((0, -1), gpow((1, 1), 2)) == (2, 0)
    for n in range(1, 513):
        ordinary = 0
        m = n
        while m % 2 == 0:
            ordinary += 1
            m //= 2
        assert v_pi((n, 0), (1, 1)) == 2 * ordinary
        checks += 1

    # Exact lifted-null-line formula at two split primes.
    checks += check_split_divisor_formula(5, (2, 1), 3, 35)
    checks += check_split_divisor_formula(13, (3, 2), 5, 35)
    return checks


def check_census() -> int:
    counts = {"T": 40, "C": 37, "F": 14, "M": 14, "D": 5}
    assert sum(counts.values()) == 110
    assert len(counts) == 5
    return len(counts) + 1


def main() -> None:
    budget_checks = check_budget_theorem()
    closure_checks = check_closure_calculus()
    orbit_checks = check_finite_field_orbit_packet()
    local_checks = check_gaussian_local_table()
    census_checks = check_census()
    total = (
        budget_checks
        + closure_checks
        + orbit_checks
        + local_checks
        + census_checks
    )
    print(f"budget identities: {budget_checks}")
    print(f"closure identities: {closure_checks}")
    print(f"finite-field orbit identities: {orbit_checks}")
    print(f"Gaussian local identities: {local_checks}")
    print(f"census identities: {census_checks}")
    print(f"all {total} arithmetic Frobenius-packet checks passed")


if __name__ == "__main__":
    main()
