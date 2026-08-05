"""Exact checks for the group-ring Gauss torsion boundary.

The script is a regression certificate, not a proof.
"""

from __future__ import annotations

from collections.abc import Callable


Element = tuple[int, ...] | int


def group_ring_power_identity_coefficient(
    coefficients: dict[Element, int],
    exponent: int,
    identity: Element,
    multiply: Callable[[Element, Element], Element],
) -> int:
    state: dict[Element, int] = {identity: 1}
    for _ in range(exponent):
        following: dict[Element, int] = {}
        for left, left_coefficient in state.items():
            for right, right_coefficient in coefficients.items():
                product = multiply(left, right)
                following[product] = following.get(product, 0) + (
                    left_coefficient * right_coefficient
                )
        state = following
    return state.get(identity, 0)


def cyclic_multiply(order: int) -> Callable[[Element, Element], Element]:
    return lambda left, right: (int(left) + int(right)) % order


def permutation_multiply(left: Element, right: Element) -> Element:
    left_tuple = tuple(left)  # type: ignore[arg-type]
    right_tuple = tuple(right)  # type: ignore[arg-type]
    return tuple(left_tuple[right_tuple[index]] for index in range(len(left_tuple)))


def check_cyclic_positive_cases() -> int:
    checks = 0
    examples = (
        (3, {0: -2, 1: 3, 2: -1}, (2, 5, 7)),
        (4, {0: 1, 1: -2, 3: 2}, (3, 5, 7)),
        (6, {0: -1, 1: 2, 2: -2, 5: 1}, (5, 7)),
    )
    for order, coefficients, primes in examples:
        multiply = cyclic_multiply(order)
        for prime in primes:
            assert order % prime
            for r in (1, 2, 3):
                for n in range(1, 5):
                    high = group_ring_power_identity_coefficient(
                        coefficients, n * prime**r, 0, multiply
                    )
                    low = group_ring_power_identity_coefficient(
                        coefficients, n * prime ** (r - 1), 0, multiply
                    )
                    assert (high - low) % prime**r == 0
                    checks += 1
    return checks


def check_symmetric_group() -> int:
    identity = (0, 1, 2)
    transposition = (1, 0, 2)
    three_cycle = (1, 2, 0)
    coefficients: dict[Element, int] = {
        identity: -2,
        transposition: 3,
        three_cycle: -1,
    }
    checks = 0
    for prime in (5, 7):
        for r in (1, 2):
            for n in range(1, 5):
                high = group_ring_power_identity_coefficient(
                    coefficients, n * prime**r, identity, permutation_multiply
                )
                low = group_ring_power_identity_coefficient(
                    coefficients,
                    n * prime ** (r - 1),
                    identity,
                    permutation_multiply,
                )
                assert (high - low) % prime**r == 0
                checks += 1
    return checks


def check_torsion_obstructions() -> int:
    checks = 0
    for prime in (2, 3, 5, 7, 11, 13):
        multiply = cyclic_multiply(prime)
        coefficients: dict[Element, int] = {1: 1}
        at_one = group_ring_power_identity_coefficient(
            coefficients, 1, 0, multiply
        )
        at_prime = group_ring_power_identity_coefficient(
            coefficients, prime, 0, multiply
        )
        assert at_one == 0
        assert at_prime == 1
        assert (at_prime - at_one) % prime == 1
        checks += 3
    return checks


def main() -> None:
    sections = {
        "cyclic p-torsion-free cases": check_cyclic_positive_cases(),
        "noncommutative S3 cases": check_symmetric_group(),
        "prime-torsion obstructions": check_torsion_obstructions(),
    }
    print(f"group-ring Gauss checks passed: {sum(sections.values())}")
    for name, count in sections.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
