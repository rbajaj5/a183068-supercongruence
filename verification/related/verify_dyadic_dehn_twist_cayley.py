"""Finite spectral checks for the dyadic Dehn-twist Cayley walk."""

from __future__ import annotations

from math import cos, pi

import numpy as np


def transition_matrix(m: int) -> tuple[np.ndarray, list[tuple[int, int]]]:
    modulus = 1 << m
    units = [u for u in range(modulus) if u % 2]
    states = [(u, b) for u in units for b in range(modulus)]
    index = {state: j for j, state in enumerate(states)}
    inv5 = pow(5, -1, modulus)
    matrix = np.zeros((len(states), len(states)), dtype=float)

    for row, (u, b) in enumerate(states):
        moves = [
            ((u, b), 0.5),
            ((u, (b + u) % modulus), 0.1),
            ((u, (b - u) % modulus), 0.1),
            (((5 * u) % modulus, b), 0.1),
            (((inv5 * u) % modulus, b), 0.1),
            (((-u) % modulus, b), 0.1),
        ]
        for state, probability in moves:
            matrix[row, index[state]] += probability

    return matrix, states


def unit_character(m: int, states: list[tuple[int, int]]) -> np.ndarray:
    modulus = 1 << m
    order = 1 << (m - 2)
    exponents: dict[int, int] = {}
    value = 1
    for exponent in range(order):
        exponents[value] = exponent
        value = (5 * value) % modulus

    values: list[complex] = []
    for u, _ in states:
        sign_free = u if u in exponents else (-u) % modulus
        exponent = exponents[sign_free]
        values.append(np.exp(2j * pi * exponent / order))
    return np.asarray(values)


def check_level(m: int) -> tuple[int, float, float, float]:
    matrix, states = transition_matrix(m)
    size = len(states)

    assert np.max(np.abs(matrix.sum(axis=1) - 1.0)) < 1e-13
    assert np.max(np.abs(matrix - matrix.T)) < 1e-13

    eigenvalues = np.linalg.eigvalsh(matrix)
    assert eigenvalues[0] >= -1e-12
    assert abs(eigenvalues[-1] - 1.0) < 1e-12
    assert eigenvalues[-2] < 1.0 - 1e-12

    gap = 1.0 - eigenvalues[-2]
    lower = (1.0 - cos(2.0 * pi / (1 << m))) / 5.0
    upper = (1.0 - cos(2.0 * pi / (1 << (m - 2)))) / 5.0
    assert gap + 1e-12 >= lower
    assert gap <= upper + 1e-12

    character = unit_character(m, states)
    predicted = 1.0 - upper
    residual = np.max(np.abs(matrix @ character - predicted * character))
    assert residual < 1e-12

    return size, gap, lower, upper


def main() -> None:
    print("Dyadic Dehn-twist Cayley-walk checks")
    for m in range(4, 6):
        size, gap, lower, upper = check_level(m)
        print(
            f"  m={m}: |G_m|={size}, gap={gap:.12g}, "
            f"bounds=[{lower:.12g}, {upper:.12g}]"
        )
    print("PASS")


if __name__ == "__main__":
    main()
