#!/usr/bin/env python3
"""Exact bounded search for the Gaussian Erdos--Moser equation."""

from __future__ import annotations

import argparse
from math import comb


def gaussian_power(base: int, exponent: int) -> tuple[int, int]:
    real, imaginary = 1, 0
    for _ in range(exponent):
        real, imaginary = (
            base * (real - imaginary),
            base * (real + imaginary),
        )
    return real, imaginary


def search(limit: int) -> list[tuple[int, int]]:
    power_sums = [0] * (limit + 1)
    solutions: list[tuple[int, int]] = []
    for n in range(1, limit):
        power = 1
        for exponent in range(limit + 1):
            power_sums[exponent] += power
            power *= n
        m = n + 1
        for k in range(1, limit + 1):
            real = 0
            imaginary = 0
            for j in range(k + 1):
                term = comb(k, j) * power_sums[k - j] * power_sums[j]
                residue = j % 4
                if residue == 0:
                    real += term
                elif residue == 1:
                    imaginary += term
                elif residue == 2:
                    real -= term
                else:
                    imaginary -= term
            if (real, imaginary) == gaussian_power(m, k):
                solutions.append((k, m))
    return solutions


def run() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=180)
    args = parser.parse_args()
    solutions = search(args.limit)
    assert solutions == [(2, 3)]
    print(
        f"Gaussian Erdos--Moser search through k,m <= {args.limit}: "
        f"{solutions}"
    )


if __name__ == "__main__":
    run()
