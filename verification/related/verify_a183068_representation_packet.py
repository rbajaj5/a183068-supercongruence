"""Exact checks for the A183068 representation and Frobenius packet."""

from fractions import Fraction
from math import comb

from verify_dwork_boundaries import a183068_polynomial, power


Vector = tuple[int, ...]
Laurent = dict[Vector, int]


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[entry % prime for entry in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work))
             if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], -1, prime)
        work[row] = [(entry * inverse) % prime for entry in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            factor = work[index][column]
            work[index] = [
                (left - factor * right) % prime
                for left, right in zip(work[index], work[row], strict=True)
            ]
        row += 1
    return row


def determinant_four(vectors: list[Vector]) -> int:
    """Laplace expansion for a 4 by 4 integer matrix."""
    total = 0
    for column in range(4):
        minor = [
            [vectors[row][other] for other in range(4) if other != column]
            for row in range(1, 4)
        ]
        minor_determinant = (
            minor[0][0]
            * (minor[1][1] * minor[2][2] - minor[1][2] * minor[2][1])
            - minor[0][1]
            * (minor[1][0] * minor[2][2] - minor[1][2] * minor[2][0])
            + minor[0][2]
            * (minor[1][0] * minor[2][1] - minor[1][1] * minor[2][0])
        )
        total += (-1) ** column * vectors[0][column] * minor_determinant
    return total


def reduced_three_variable_factor(polynomial: Laurent) -> Laurent:
    """Recover G from P=C(w)G using the coefficient of w^0 in C."""
    middle = {
        exponent[1:]: coefficient
        for exponent, coefficient in polynomial.items()
        if exponent[0] == 0
    }
    assert all(coefficient % 2 == 0 for coefficient in middle.values())
    return {
        exponent: coefficient // 2
        for exponent, coefficient in middle.items()
    }


def divided_packet(
    factor: Laurent,
    prime: int,
) -> tuple[list[list[int]], list[list[int]]]:
    interior = [(0, -1, 0), (0, 0, 0), (0, 1, 0)]
    factor_power = power(factor, prime - 1)
    central = comb(2 * prime - 2, prime - 1)
    packet = [
        [
            central * factor_power.get(
                tuple(
                    prime * right - left
                    for left, right in zip(u, v, strict=True)
                ),
                0,
            )
            for v in interior
        ]
        for u in interior
    ]
    assert all(entry % prime == 0 for row in packet for entry in row)
    divided = [
        [(entry // prime) % prime for entry in row]
        for row in packet
    ]
    return packet, divided


def binomial_or_zero(top: int, bottom: int) -> int:
    if bottom < 0 or bottom > top:
        return 0
    return comb(top, bottom)


def factor_packet_formula(prime: int) -> list[list[int]]:
    """Coefficient formula (25), reduced modulo prime."""
    indices = (-1, 0, 1)
    return [
        [
            sum(
                comb(prime - 1, k) ** 2
                * comb(2 * k, k)
                * binomial_or_zero(
                    2 * (prime - 1 + k),
                    prime * v - u + 2 * k,
                )
                for k in range(prime)
            )
            % prime
            for v in indices
        ]
        for u in indices
    ]


def check_character_and_walk() -> None:
    polynomial = a183068_polynomial()
    assert len(polynomial) == 99
    assert all(coefficient > 0 for coefficient in polynomial.values())
    dimension = sum(polynomial.values())
    assert dimension == 544

    mean_numerators = [
        sum(coefficient * exponent[index]
            for exponent, coefficient in polynomial.items())
        for index in range(4)
    ]
    assert [
        Fraction(value, dimension)
        for value in mean_numerators
    ] == [
        Fraction(0),
        Fraction(-15, 34),
        Fraction(1, 17),
        Fraction(0),
    ]

    second = [
        [
            sum(
                coefficient * exponent[left] * exponent[right]
                for exponent, coefficient in polynomial.items()
            )
            for right in range(4)
        ]
        for left in range(4)
    ]
    covariance = [
        [
            Fraction(second[left][right], dimension)
            - Fraction(
                mean_numerators[left] * mean_numerators[right],
                dimension * dimension,
            )
            for right in range(4)
        ]
        for left in range(4)
    ]
    assert covariance == [
        [Fraction(1, 2), 0, 0, 0],
        [0, Fraction(353, 1156), Fraction(16, 289), 0],
        [0, Fraction(16, 289), Fraction(593, 578), 0],
        [0, 0, 0, Fraction(8, 17)],
    ]

    support = set(polynomial)
    assert any(
        exponent != tuple(-entry for entry in exponent)
        and tuple(-entry for entry in exponent) not in support
        for exponent in support
    )
    lattice_basis = [
        (-1, 0, 0, 0),
        (-1, -1, -2, -1),
        (-1, -1, -2, 0),
        (-1, -1, -1, -1),
    ]
    assert all(vector in support for vector in lattice_basis)
    assert determinant_four(lattice_basis) == -1


def check_central_binomial_layer() -> None:
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        central = comb(2 * prime - 2, prime - 1)
        assert central % prime == 0
        assert central % (prime * prime) != 0
        assert (central // prime) % prime == (-1) % prime


def check_small_prime_packets() -> None:
    factor = reduced_three_variable_factor(a183068_polynomial())
    assert len(factor) == 33

    expected = {
        2: [[0, 0, 0], [0, 1, 1], [0, 0, 0]],
        3: [[1, 1, 0], [0, 2, 2], [0, 0, 0]],
        5: [[4, 0, 1], [0, 4, 4], [0, 0, 0]],
        7: [[1, 4, 3], [0, 6, 6], [0, 0, 0]],
    }
    for prime, target in expected.items():
        packet, divided = divided_packet(factor, prime)
        factor_packet = factor_packet_formula(prime)
        assert divided == [
            [(-entry) % prime for entry in row]
            for row in factor_packet
        ]
        assert divided == target
        assert all(
            entry % prime == 0
            for row in packet
            for entry in row
        )
        assert rank_mod(divided, prime) == (1 if prime == 2 else 2)

    for prime in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        packet = factor_packet_formula(prime)
        half = (prime - 1) // 2
        assert packet[0][0] == (-1) ** half % prime
        assert packet[1][1] == 1
        assert packet[2] == [0, 0, 0]
        assert rank_mod(packet, prime) == 2


def main() -> None:
    check_character_and_walk()
    check_central_binomial_layer()
    check_small_prime_packets()
    print("A183068 representation-packet checks passed")
    print("  character dimension: 544; Laurent weights: 99")
    print("  exact drift and anisotropic covariance: verified")
    print("  ordinary Hasse--Witt packet: zero mod p for all tested primes")
    print("  divided packet rank formula: p=2 gives 1; every odd p gives 2")


if __name__ == "__main__":
    main()
