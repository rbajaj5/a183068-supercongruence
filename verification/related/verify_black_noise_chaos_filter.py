"""Exact checks for the Walsh-chaos adjacent-scale congruence.

The checker has four independent parts:

1. arbitrary lacunary polynomials over the Gaussian integers;
2. random complement-odd Gaussian-valued observables on Boolean cubes; and
3. the exact Y-game winner and majority reduction; and
4. signed left-right crossing contrasts on small triangular-lattice patches.

No floating-point arithmetic is used.
"""

from __future__ import annotations

from collections import deque
import random
import sys


Gaussian = tuple[int, int]


def gadd(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] + w[0], z[1] + w[1]


def gsub(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] - w[0], z[1] - w[1]


def gmul(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def gpow(z: Gaussian, exponent: int) -> Gaussian:
    out = (1, 0)
    base = z
    while exponent:
        if exponent & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        exponent >>= 1
    return out


def gscale(n: int, z: Gaussian) -> Gaussian:
    return n * z[0], n * z[1]


def divide_by_gaussian_prime(z: Gaussian, prime: Gaussian) -> Gaussian | None:
    """Return z / prime when it is Gaussian-integral, and None otherwise."""

    a, b = prime
    norm = a * a + b * b
    real = z[0] * a + z[1] * b
    imag = z[1] * a - z[0] * b
    if real % norm or imag % norm:
        return None
    return real // norm, imag // norm


def gaussian_valuation(z: Gaussian, prime: Gaussian) -> int:
    if z == (0, 0):
        return 10**9
    valuation = 0
    while True:
        quotient = divide_by_gaussian_prime(z, prime)
        if quotient is None:
            return valuation
        valuation += 1
        z = quotient


def divide_by_prime_power(
    z: Gaussian, prime: Gaussian, exponent: int
) -> Gaussian:
    for _ in range(exponent):
        quotient = divide_by_gaussian_prime(z, prime)
        assert quotient is not None
        z = quotient
    return z


def polynomial_value(coefficients: dict[int, Gaussian], z: Gaussian) -> Gaussian:
    total = (0, 0)
    for degree, coefficient in coefficients.items():
        total = gadd(total, gmul(coefficient, gpow(z, degree)))
    return total


def lacunary_defect(
    coefficients: dict[int, Gaussian],
    prime: Gaussian,
    r: int,
    d: int,
) -> Gaussian:
    high = polynomial_value(coefficients, gpow(prime, r))
    low = polynomial_value(coefficients, gpow(prime, r - 1))
    return gsub(high, gmul(gpow(prime, d), low))


def fwht(values: list[Gaussian]) -> list[Gaussian]:
    out = values[:]
    block = 1
    while block < len(out):
        for start in range(0, len(out), 2 * block):
            for offset in range(block):
                left = out[start + offset]
                right = out[start + offset + block]
                out[start + offset] = gadd(left, right)
                out[start + offset + block] = gsub(left, right)
        block *= 2
    return out


def walsh_mass_polynomial(values: list[Gaussian]) -> dict[int, Gaussian]:
    transform = fwht(values)
    masses: dict[int, int] = {}
    for subset, coefficient in enumerate(transform):
        degree = subset.bit_count()
        norm = coefficient[0] ** 2 + coefficient[1] ** 2
        masses[degree] = masses.get(degree, 0) + norm
    return {degree: (mass, 0) for degree, mass in masses.items() if mass}


def random_complement_odd_values(
    dimension: int, rng: random.Random
) -> list[Gaussian]:
    size = 1 << dimension
    full_mask = size - 1
    values: list[Gaussian | None] = [None] * size
    for mask in range(size):
        complement = full_mask ^ mask
        if values[mask] is not None:
            continue
        value = (rng.randint(-4, 4), rng.randint(-4, 4))
        values[mask] = value
        values[complement] = (-value[0], -value[1])
    return [value for value in values if value is not None]


def triangular_crossing(bits: list[int], width: int, height: int) -> int:
    """Indicator of an open left-right crossing of a triangular patch."""

    def index(x: int, y: int) -> int:
        return y * width + x

    opened = {site for site, bit in enumerate(bits) if bit}
    queue = deque(
        index(0, y) for y in range(height) if index(0, y) in opened
    )
    seen = set(queue)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
    while queue:
        site = queue.popleft()
        x, y = site % width, site // width
        if x == width - 1:
            return 1
        for dx, dy in directions:
            xx, yy = x + dx, y + dy
            if 0 <= xx < width and 0 <= yy < height:
                neighbor = index(xx, yy)
                if neighbor in opened and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
    return 0


def crossing_contrast(width: int, height: int) -> list[Gaussian]:
    dimension = width * height
    values: list[Gaussian] = []
    for mask in range(1 << dimension):
        bits = [(mask >> site) & 1 for site in range(dimension)]
        complement = [1 - bit for bit in bits]
        contrast = triangular_crossing(bits, width, height) - triangular_crossing(
            complement, width, height
        )
        values.append((contrast, 0))
    return values


def y_cells(side: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, side - 1 - a - b)
        for a in range(side)
        for b in range(side - a)
    ]


def y_adjacency(side: int) -> list[list[int]]:
    cells = y_cells(side)
    neighbors: list[list[int]] = [[] for _ in cells]
    for left, u in enumerate(cells):
        for right, v in enumerate(cells):
            if sum(abs(x - y) for x, y in zip(u, v, strict=True)) == 2:
                neighbors[left].append(right)
    return neighbors


def has_y(
    bits: list[int],
    side: int,
    color: int,
    adjacency: list[list[int]] | None = None,
) -> bool:
    cells = y_cells(side)
    if adjacency is None:
        adjacency = y_adjacency(side)
    unseen = {index for index, bit in enumerate(bits) if bit == color}
    while unseen:
        start = unseen.pop()
        stack = [start]
        touches = [False, False, False]
        while stack:
            index = stack.pop()
            for coordinate, value in enumerate(cells[index]):
                touches[coordinate] |= value == 0
            for neighbor in adjacency[index]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        if all(touches):
            return True
    return False


def y_majority_reduce(bits: list[int], side: int) -> list[int]:
    assert side >= 2
    values = dict(zip(y_cells(side), bits, strict=True))
    reduced: list[int] = []
    for a, b, c in y_cells(side - 1):
        total = (
            values[a + 1, b, c]
            + values[a, b + 1, c]
            + values[a, b, c + 1]
        )
        reduced.append(int(total >= 2))
    return reduced


def check_y_game() -> int:
    expected_masses = {
        1: {1: 4},
        2: {1: 48, 3: 16},
        3: {1: 2496, 3: 1408, 5: 192},
        4: {1: 549568, 3: 377600, 5: 107136, 7: 14080, 9: 192},
        5: {
            1: 501212928,
            3: 377104896,
            5: 151252224,
            7: 38476800,
            9: 5370112,
            11: 317952,
            13: 6912,
        },
    }
    checks = 0
    for side, expected in expected_masses.items():
        cells = y_cells(side)
        adjacency = y_adjacency(side)
        dimension = len(cells)
        full_mask = (1 << dimension) - 1
        values: list[Gaussian] = []
        for mask in range(1 << dimension):
            bits = [(mask >> index) & 1 for index in range(dimension)]
            positive = has_y(bits, side, 1, adjacency)
            negative = has_y(bits, side, 0, adjacency)
            assert positive != negative
            winner = 1 if positive else -1
            values.append((winner, 0))
            checks += 1

            complement = full_mask ^ mask
            if complement < len(values):
                assert values[complement] == (-winner, 0)
                checks += 1

            if side >= 2:
                reduced = y_majority_reduce(bits, side)
                reduced_positive = has_y(reduced, side - 1, 1)
                assert reduced_positive == positive
                checks += 1

        polynomial = walsh_mass_polynomial(values)
        observed = {
            degree: coefficient[0]
            for degree, coefficient in polynomial.items()
        }
        assert observed == expected
        assert all(degree % 2 for degree in observed)
        checks += len(observed) + 1

        for prime in ((1, 1), (2, 1), (3, 0)):
            for r in range(1, 7):
                defect = lacunary_defect(polynomial, prime, r, d=1)
                assert gaussian_valuation(defect, prime) >= 3 * r - 2
                checks += 1
                if r >= 2:
                    normalized = divide_by_prime_power(
                        defect, prime, 3 * r - 2
                    )
                    cubic_mass = polynomial.get(3, (0, 0))
                    expected_residue = (-cubic_mass[0], -cubic_mass[1])
                    assert gaussian_valuation(
                        gsub(normalized, expected_residue), prime
                    ) >= 1
                    checks += 1
    return checks


def check_y_game_side_six() -> int:
    """Run the optional 2^21-coloring exact side-six spectrum.

    This uses NumPy only in the opt-in extended run. The default repository
    checker remains standard-library-only.
    """

    try:
        import numpy as np
    except ImportError as error:
        raise RuntimeError(
            "the --extended Y-game run requires NumPy"
        ) from error

    winners = np.array([-1, 1], dtype=np.int8)
    for side in range(2, 7):
        large_cells = y_cells(side)
        index = {cell: position for position, cell in enumerate(large_cells)}
        masks = np.arange(1 << len(large_cells), dtype=np.uint32)
        reduced = np.zeros(masks.shape, dtype=np.uint32)
        for target, (a, b, c) in enumerate(y_cells(side - 1)):
            i = index[a + 1, b, c]
            j = index[a, b + 1, c]
            k = index[a, b, c + 1]
            majority = (
                ((masks >> i) & 1)
                + ((masks >> j) & 1)
                + ((masks >> k) & 1)
                >= 2
            )
            reduced |= majority.astype(np.uint32) << target
        winners = winners[reduced]

    assert winners.size == 1 << 21
    assert np.array_equal(winners, -winners[::-1])
    checks = 2

    rng = random.Random(6006)
    adjacency = y_adjacency(6)
    for _ in range(2_000):
        mask = rng.randrange(1 << 21)
        bits = [(mask >> index) & 1 for index in range(21)]
        positive = has_y(bits, 6, 1, adjacency)
        assert winners[mask] == (1 if positive else -1)
        checks += 1

    transform = winners.astype(np.int64)
    block = 1
    while block < transform.size:
        view = transform.reshape(-1, 2 * block)
        left = view[:, :block].copy()
        right = view[:, block:].copy()
        view[:, :block] = left + right
        view[:, block:] = left - right
        block *= 2

    masks = np.arange(transform.size, dtype=np.uint32)
    byte_counts = np.array([value.bit_count() for value in range(256)])
    degrees = byte_counts[masks.view(np.uint8).reshape(-1, 4)].sum(axis=1)
    squares = transform * transform
    observed = {
        degree: int(squares[degrees == degree].sum(dtype=np.int64))
        for degree in range(22)
        if np.any(transform[degrees == degree])
    }
    expected = {
        1: 1869439264128,
        3: 1473803873408,
        5: 722690237952,
        7: 256856418816,
        9: 63332709632,
        11: 10667093760,
        13: 1171385856,
        15: 82137600,
        17: 3330432,
        19: 59520,
    }
    assert observed == expected
    assert sum(observed.values()) == 1 << 42
    checks += len(observed) + 1

    polynomial = {
        degree: (coefficient, 0)
        for degree, coefficient in observed.items()
    }
    for prime in ((1, 1), (2, 1), (3, 0)):
        for r in range(1, 7):
            defect = lacunary_defect(polynomial, prime, r, d=1)
            assert gaussian_valuation(defect, prime) >= 3 * r - 2
            checks += 1
            if r >= 2:
                normalized = divide_by_prime_power(
                    defect, prime, 3 * r - 2
                )
                cubic_mass = polynomial[3]
                assert gaussian_valuation(
                    gadd(normalized, cubic_mass), prime
                ) >= 1
                checks += 1
    return checks


def check_lacunary_polynomials() -> int:
    rng = random.Random(20260729)
    checks = 0
    gaussian_primes = ((1, 1), (2, 1), (3, 0))
    for _ in range(120):
        d = rng.randint(0, 4)
        gap = rng.randint(1, 4)
        coefficients = {
            d + gap * step: (rng.randint(-8, 8), rng.randint(-8, 8))
            for step in range(rng.randint(2, 6))
        }
        for prime in gaussian_primes:
            for r in range(1, 6):
                defect = lacunary_defect(coefficients, prime, r, d)
                expected = (d + gap) * r - gap
                assert gaussian_valuation(defect, prime) >= expected
                checks += 1
    return checks


def check_random_observables() -> int:
    rng = random.Random(314159)
    checks = 0
    gaussian_primes = ((1, 1), (2, 1), (3, 0))
    for dimension in range(2, 8):
        for _ in range(12):
            values = random_complement_odd_values(dimension, rng)
            polynomial = walsh_mass_polynomial(values)
            assert all(degree % 2 == 1 for degree in polynomial)
            for prime in gaussian_primes:
                for r in range(1, 6):
                    defect = lacunary_defect(polynomial, prime, r, d=1)
                    assert gaussian_valuation(defect, prime) >= 3 * r - 2
                    checks += 1
                    if r >= 2:
                        normalized = divide_by_prime_power(
                            defect, prime, 3 * r - 2
                        )
                        cubic_mass = polynomial.get(3, (0, 0))
                        expected = (-cubic_mass[0], -cubic_mass[1])
                        assert gaussian_valuation(
                            gsub(normalized, expected), prime
                        ) >= 1
                        checks += 1
    return checks


def check_triangular_crossings() -> int:
    expected = {
        (2, 2): {1: 160, 3: 32},
        (3, 2): {1: 1816, 3: 592, 5: 24},
        (3, 3): {1: 124240, 3: 51584, 5: 5920, 7: 512, 9: 16},
        (4, 2): {1: 17312, 3: 8672, 5: 1120, 7: 32},
    }
    checks = 0
    for shape, expected_masses in expected.items():
        polynomial = walsh_mass_polynomial(crossing_contrast(*shape))
        observed = {degree: coefficient[0] for degree, coefficient in polynomial.items()}
        assert observed == expected_masses
        checks += len(observed)
        for prime in ((1, 1), (2, 1), (3, 0)):
            for r in range(1, 7):
                defect = lacunary_defect(polynomial, prime, r, d=1)
                assert gaussian_valuation(defect, prime) >= 3 * r - 2
                checks += 1
                if r >= 2:
                    normalized = divide_by_prime_power(
                        defect, prime, 3 * r - 2
                    )
                    cubic_mass = polynomial.get(3, (0, 0))
                    expected = (-cubic_mass[0], -cubic_mass[1])
                    assert gaussian_valuation(
                        gsub(normalized, expected), prime
                    ) >= 1
                    checks += 1
    return checks


def main() -> None:
    lacunary = check_lacunary_polynomials()
    observables = check_random_observables()
    y_game = check_y_game()
    crossings = check_triangular_crossings()
    total = lacunary + observables + y_game + crossings
    print(f"lacunary Gaussian-polynomial checks: {lacunary}")
    print(f"complement-odd Walsh checks: {observables}")
    print(f"Y-game renormalization checks: {y_game}")
    print(f"triangular-crossing checks: {crossings}")
    print(f"all {total} black-noise chaos-filter checks passed")
    if "--extended" in sys.argv[1:]:
        side_six = check_y_game_side_six()
        print(f"extended side-six Y-game checks: {side_six}")


if __name__ == "__main__":
    main()
