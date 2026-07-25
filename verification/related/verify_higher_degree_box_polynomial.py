#!/usr/bin/env python3
"""Direct checks for HigherDegreeFiniteFieldBoxPolynomials.md."""

from __future__ import annotations

from itertools import product


Element = tuple[int, ...]
Polynomial = list[Element]


class FiniteField:
    def __init__(self, p: int, modulus: tuple[int, ...]) -> None:
        assert modulus[-1] == 1
        self.p = p
        self.modulus = modulus
        self.degree = len(modulus) - 1
        self.zero = (0,) * self.degree
        self.one = (1,) + (0,) * (self.degree - 1)

    def add(self, x: Element, y: Element) -> Element:
        return tuple((a + b) % self.p for a, b in zip(x, y))

    def neg(self, x: Element) -> Element:
        return tuple(-a % self.p for a in x)

    def mul(self, x: Element, y: Element) -> Element:
        raw = [0] * (2 * self.degree - 1)
        for j, a in enumerate(x):
            for k, b in enumerate(y):
                raw[j + k] = (raw[j + k] + a * b) % self.p
        for power in range(2 * self.degree - 2, self.degree - 1, -1):
            coefficient = raw[power] % self.p
            if coefficient:
                for j in range(self.degree):
                    raw[power - self.degree + j] -= (
                        coefficient * self.modulus[j]
                    )
                    raw[power - self.degree + j] %= self.p
        return tuple(raw[: self.degree])

    def elements_in_subspace(self, mask: int) -> list[Element]:
        indices = [j for j in range(self.degree) if mask & (1 << j)]
        elements: list[Element] = []
        for coefficients in product(range(self.p), repeat=len(indices)):
            value = [0] * self.degree
            for index, coefficient in zip(indices, coefficients):
                value[index] = coefficient
            elements.append(tuple(value))
        return elements


def polynomial_mul(
    field: FiniteField, left: Polynomial, right: Polynomial
) -> Polynomial:
    result = [field.zero] * (len(left) + len(right) - 1)
    for j, x in enumerate(left):
        for k, y in enumerate(right):
            result[j + k] = field.add(
                result[j + k], field.mul(x, y)
            )
    while len(result) > 1 and result[-1] == field.zero:
        result.pop()
    return result


def root_polynomial(field: FiniteField, roots: list[Element]) -> Polynomial:
    polynomial = [field.one]
    for root in roots:
        polynomial = polynomial_mul(
            field, polynomial, [field.neg(root), field.one]
        )
    return polynomial


def verify(field: FiniteField) -> None:
    full_mask = (1 << field.degree) - 1
    subspace_polynomials: dict[int, Polynomial] = {}
    for mask in range(full_mask + 1):
        subspace_polynomials[mask] = root_polynomial(
            field, field.elements_in_subspace(mask)
        )

    box = [
        tuple(coordinates)
        for coordinates in product(
            range(1, field.p), repeat=field.degree
        )
    ]
    box_polynomial = root_polynomial(field, box)

    positive = [field.one]
    negative = [field.one]
    for mask, polynomial in subspace_polynomials.items():
        codimension = field.degree - mask.bit_count()
        if codimension % 2:
            negative = polynomial_mul(field, negative, polynomial)
        else:
            positive = polynomial_mul(field, positive, polynomial)

    assert polynomial_mul(
        field, box_polynomial, negative
    ) == positive


def run() -> None:
    fields = [
        FiniteField(3, (1, 0, 1)),       # x^2 + 1
        FiniteField(3, (1, 2, 0, 1)),    # x^3 + 2x + 1
    ]
    for field in fields:
        verify(field)
        print(
            f"verified F_{field.p}^{field.degree}: "
            f"{(field.p - 1) ** field.degree} full-support roots"
        )


if __name__ == "__main__":
    run()
