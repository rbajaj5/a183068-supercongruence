"""Exact checks for compatible lift towers and square-zero defects."""

from __future__ import annotations

from itertools import product


Matrix = tuple[tuple[int, int], tuple[int, int]]


def identity() -> Matrix:
    return ((1, 0), (0, 1))


def add(left: Matrix, right: Matrix, modulus: int) -> Matrix:
    return tuple(
        tuple((left[i][j] + right[i][j]) % modulus for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def subtract(left: Matrix, right: Matrix, modulus: int) -> Matrix:
    return tuple(
        tuple((left[i][j] - right[i][j]) % modulus for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def multiply(left: Matrix, right: Matrix, modulus: int) -> Matrix:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(2)) % modulus
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def scalar_multiply(scalar: int, matrix: Matrix, modulus: int) -> Matrix:
    return tuple(
        tuple(scalar * matrix[i][j] % modulus for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def inverse(matrix: Matrix, modulus: int) -> Matrix:
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = (a * d - b * c) % modulus
    determinant_inverse = pow(determinant, -1, modulus)
    return (
        (
            determinant_inverse * d % modulus,
            -determinant_inverse * b % modulus,
        ),
        (
            -determinant_inverse * c % modulus,
            determinant_inverse * a % modulus,
        ),
    )


def power(matrix: Matrix, exponent: int, modulus: int) -> Matrix:
    result = identity()
    base = matrix
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus)
        base = multiply(base, base, modulus)
        exponent >>= 1
    return result


def matrix_from_seed(seed: int, modulus: int) -> Matrix:
    return (
        ((seed + 1) % modulus, (2 * seed + 1) % modulus),
        ((seed * seed + 1) % modulus, (3 * seed + 2) % modulus),
    )


def near_identity(matrix: Matrix, prime: int, modulus: int) -> Matrix:
    return add(identity(), scalar_multiply(prime, matrix, modulus), modulus)


def normalized_near_identity(matrix: Matrix, prime: int) -> Matrix:
    return tuple(
        tuple(
            ((matrix[i][j] - (1 if i == j else 0)) // prime) % prime
            for j in range(2)
        )
        for i in range(2)
    )  # type: ignore[return-value]


def conjugate(action: Matrix, value: Matrix, prime: int) -> Matrix:
    return multiply(
        multiply(action, value, prime), inverse(action, prime), prime
    )


def check_compatible_tower() -> int:
    generator: Matrix = ((0, -1), (1, 0))
    checks = 0
    previous: list[Matrix] | None = None
    for level in range(1, 7):
        modulus = 3**level
        representation = [power(generator, exponent, modulus) for exponent in range(4)]
        for left, right in product(range(4), repeat=2):
            assert multiply(
                representation[left], representation[right], modulus
            ) == representation[(left + right) % 4]
            checks += 1
        if previous is not None:
            lower_modulus = 3 ** (level - 1)
            assert all(
                tuple(
                    tuple(entry % lower_modulus for entry in row)
                    for row in matrix
                )
                == previous[index]
                for index, matrix in enumerate(representation)
            )
        previous = representation
    return checks


def check_square_zero_defects() -> int:
    prime = 3
    modulus = prime * prime
    generator: Matrix = ((0, -1), (1, 0))
    exact = [power(generator, exponent, modulus) for exponent in range(4)]
    residual = [
        tuple(tuple(entry % prime for entry in row) for row in matrix)
        for matrix in exact
    ]
    checks = 0

    for seed in range(1, 41):
        perturbations = [((0, 0), (0, 0))] + [
            matrix_from_seed(seed + 5 * group_element, prime)
            for group_element in range(1, 4)
        ]
        lifts = [
            multiply(
                near_identity(perturbations[g], prime, modulus),
                exact[g],
                modulus,
            )
            for g in range(4)
        ]

        defect: dict[tuple[int, int], Matrix] = {}
        for g, h in product(range(4), repeat=2):
            raw = multiply(
                multiply(lifts[g], lifts[h], modulus),
                inverse(lifts[(g + h) % 4], modulus),
                modulus,
            )
            defect[g, h] = normalized_near_identity(raw, prime)

        for g, h, k in product(range(4), repeat=3):
            left = add(
                defect[g, h], defect[(g + h) % 4, k], prime
            )
            right = add(
                conjugate(residual[g], defect[h, k], prime),
                defect[g, (h + k) % 4],
                prime,
            )
            assert left == right
            checks += 1

        changes = [((0, 0), (0, 0))] + [
            matrix_from_seed(2 * seed + 7 * group_element, prime)
            for group_element in range(1, 4)
        ]
        changed_lifts = [
            multiply(
                near_identity(changes[g], prime, modulus),
                lifts[g],
                modulus,
            )
            for g in range(4)
        ]

        changed_defect: dict[tuple[int, int], Matrix] = {}
        for g, h in product(range(4), repeat=2):
            raw = multiply(
                multiply(changed_lifts[g], changed_lifts[h], modulus),
                inverse(changed_lifts[(g + h) % 4], modulus),
                modulus,
            )
            changed_defect[g, h] = normalized_near_identity(raw, prime)
            coboundary = subtract(
                add(
                    changes[g],
                    conjugate(residual[g], changes[h], prime),
                    prime,
                ),
                changes[(g + h) % 4],
                prime,
            )
            assert changed_defect[g, h] == add(
                defect[g, h], coboundary, prime
            )
            checks += 1

        corrected_lifts = [
            multiply(
                near_identity(
                    scalar_multiply(-1, perturbations[g], prime),
                    prime,
                    modulus,
                ),
                lifts[g],
                modulus,
            )
            for g in range(4)
        ]
        assert corrected_lifts == exact
        for g, h in product(range(4), repeat=2):
            assert multiply(
                corrected_lifts[g], corrected_lifts[h], modulus
            ) == corrected_lifts[(g + h) % 4]
            checks += 1

    return checks


def main() -> None:
    tower_checks = check_compatible_tower()
    defect_checks = check_square_zero_defects()
    print(f"checked {tower_checks} compatible finite-level identities")
    print(f"checked {defect_checks} square-zero defect identities")
    print("PASS")


if __name__ == "__main__":
    main()
