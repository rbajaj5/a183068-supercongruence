"""Exact checks for the lattice-walk Frobenius congruence note.

The proof is symbolic.  These computations catch transcription, conjugation,
prime-splitting, ramified-valuation, and closed-walk interpretation errors.
"""

from __future__ import annotations

from itertools import product
from typing import Callable


Pair = tuple[int, int]
Matrix = list[list[Pair]]
Multiply = Callable[[Pair, Pair], Pair]
Conjugate = Callable[[Pair], Pair]


def add(x: Pair, y: Pair) -> Pair:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Pair, y: Pair) -> Pair:
    return x[0] - y[0], x[1] - y[1]


def gaussian_mul(x: Pair, y: Pair) -> Pair:
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c


def eisenstein_mul(x: Pair, y: Pair) -> Pair:
    """Multiply a+b*w and c+d*w using w^2+w+1=0."""
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def gaussian_conj(x: Pair) -> Pair:
    return x[0], -x[1]


def eisenstein_conj(x: Pair) -> Pair:
    # conjugate(w) = w^2 = -1-w
    return x[0] - x[1], -x[1]


def mat_mul(left: Matrix, right: Matrix, multiply: Multiply) -> Matrix:
    size = len(left)
    out = [[(0, 0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for k in range(size):
            for j in range(size):
                out[i][j] = add(out[i][j], multiply(left[i][k], right[k][j]))
    return out


def mat_pow(matrix: Matrix, exponent: int, multiply: Multiply) -> Matrix:
    size = len(matrix)
    out = [
        [(1, 0) if i == j else (0, 0) for j in range(size)]
        for i in range(size)
    ]
    base = matrix
    while exponent:
        if exponent & 1:
            out = mat_mul(out, base, multiply)
        base = mat_mul(base, base, multiply)
        exponent //= 2
    return out


def trace(matrix: Matrix) -> Pair:
    out = (0, 0)
    for i in range(len(matrix)):
        out = add(out, matrix[i][i])
    return out


def divisible_by_rational_power(x: Pair, p: int, r: int) -> bool:
    modulus = p**r
    return x[0] % modulus == 0 and x[1] % modulus == 0


def gaussian_ramified_valuation(x: Pair) -> int:
    """Return v_(1+i)(x), with a large sentinel for zero."""
    if x == (0, 0):
        return 10**9
    a, b = x
    valuation = 0
    while (a - b) % 2 == 0:
        a, b = (a + b) // 2, (b - a) // 2
        valuation += 1
    return valuation


def eisenstein_ramified_valuation(x: Pair) -> int:
    """Return v_(1-w)(x), with a large sentinel for zero."""
    if x == (0, 0):
        return 10**9
    a, b = x
    valuation = 0
    while (a + b) % 3 == 0:
        a, b = (2 * a - b) // 3, (a + b) // 3
        valuation += 1
    return valuation


def check_table(
    matrix: Matrix,
    multiply: Multiply,
    conjugate: Conjugate,
    split_modulus: int,
    ramified_prime: int,
    ramified_valuation: Callable[[Pair], int],
) -> int:
    checks = 0
    primes = (2, 3, 5, 7, 11, 13)
    for p in primes:
        for n in (1, 2, 3, 5):
            for r in (1, 2, 3):
                high = trace(mat_pow(matrix, n * p**r, multiply))
                low = trace(mat_pow(matrix, n * p ** (r - 1), multiply))

                if p == ramified_prime:
                    for image in (low, conjugate(low)):
                        assert ramified_valuation(sub(high, image)) >= r
                        checks += 1
                else:
                    image = low if p % split_modulus == 1 else conjugate(low)
                    assert divisible_by_rational_power(sub(high, image), p, r)
                    checks += 1
    return checks


def brute_closed_walk_sum(matrix: Matrix, length: int, multiply: Multiply) -> Pair:
    """Enumerate all marked closed walks and multiply their edge weights."""
    size = len(matrix)
    total = (0, 0)
    for vertices in product(range(size), repeat=length):
        weight = (1, 0)
        for step in range(length):
            source = vertices[step]
            target = vertices[(step + 1) % length]
            weight = multiply(weight, matrix[source][target])
        total = add(total, weight)
    return total


def check_closed_walk_interpretation() -> int:
    # A small orientation-weighted finite quotient.  Entries are Eisenstein
    # weights; zero entries simply make the corresponding walks contribute 0.
    matrix: Matrix = [
        [(0, 0), (1, 0), (0, 1)],
        [(1, 1), (0, 0), (1, 0)],
        [(0, -1), (1, 1), (0, 0)],
    ]
    checks = 0
    for length in range(1, 7):
        direct = brute_closed_walk_sum(matrix, length, eisenstein_mul)
        via_trace = trace(mat_pow(matrix, length, eisenstein_mul))
        assert direct == via_trace
        checks += 1
    return checks


def main() -> None:
    gaussian_matrix: Matrix = [
        [(1, 1), (1, 0), (0, 1)],
        [(0, -1), (2, -1), (1, 1)],
        [(1, 0), (-1, 1), (0, 1)],
    ]
    eisenstein_matrix: Matrix = [
        [(1, 1), (1, 0), (0, 1)],
        [(0, -1), (2, -1), (1, 1)],
        [(1, 0), (-1, 1), (0, 1)],
    ]

    checks = check_table(
        gaussian_matrix,
        gaussian_mul,
        gaussian_conj,
        split_modulus=4,
        ramified_prime=2,
        ramified_valuation=gaussian_ramified_valuation,
    )
    checks += check_table(
        eisenstein_matrix,
        eisenstein_mul,
        eisenstein_conj,
        split_modulus=3,
        ramified_prime=3,
        ramified_valuation=eisenstein_ramified_valuation,
    )
    checks += check_closed_walk_interpretation()

    print(f"lattice-walk Frobenius checks passed: {checks}")


if __name__ == "__main__":
    main()
