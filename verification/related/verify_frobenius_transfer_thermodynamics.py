"""Exact valuation histogram for the degree-seven Frobenius automaton."""

from collections import Counter
from fractions import Fraction


PRIME = 5
PRECISION = 4
MODULUS = PRIME**PRECISION
PERIOD = 19_500
START = 16

DEGREE_SEVEN = [
    1,
    0,
    0,
    2,
    7,
    -16,
    -34,
    -80,
    175,
    250,
    0,
    0,
    15625,
]


def newton_traces(polynomial: list[int]) -> list[int]:
    degree = len(polynomial) - 1
    traces = [0]
    for n in range(1, degree + 1):
        value = -n * polynomial[n]
        value -= sum(
            polynomial[j] * traces[n - j] for j in range(1, n)
        )
        traces.append(value)
    return traces


def extend_traces_mod(
    polynomial: list[int], limit: int, modulus: int
) -> list[int]:
    degree = len(polynomial) - 1
    traces = [value % modulus for value in newton_traces(polynomial)]
    for n in range(degree + 1, limit + 1):
        traces.append(
            -sum(
                polynomial[j] * traces[n - j]
                for j in range(1, degree + 1)
            )
            % modulus
        )
    return traces


def correction(r: int) -> int:
    return (
        2 * (r % 2 == 0)
        + 16 * (r % 4 == 0)
        + 10 * (r % 5 == 0)
        + 10 * (r % 10 == 0)
    )


def truncated_valuation(residue: int) -> int:
    residue %= MODULUS
    if residue == 0:
        return PRECISION
    exponent = 0
    while residue % PRIME == 0:
        exponent += 1
        residue //= PRIME
    return exponent


def main() -> None:
    traces = extend_traces_mod(
        DEGREE_SEVEN, START + 2 * PERIOD + 1, MODULUS
    )

    def packet(r: int) -> int:
        return (2 * traces[r] + correction(r)) % MODULUS

    assert all(
        packet(r + PERIOD) == packet(r)
        for r in range(START - 1, START + PERIOD + 1)
    )

    histogram = Counter(
        truncated_valuation(packet(r - 1) - packet(r))
        for r in range(START + 1, START + PERIOD + 1)
    )
    expected = {0: 16_000, 1: 2_700, 2: 600, 3: 145, 4: 55}
    assert dict(sorted(histogram.items())) == expected

    thresholds = {
        h: sum(count for value, count in histogram.items() if value >= h)
        for h in range(1, PRECISION + 1)
    }
    assert thresholds == {1: 3_500, 2: 800, 3: 200, 4: 55}

    mean = Fraction(
        sum(value * count for value, count in histogram.items()), PERIOD
    )
    second_moment = Fraction(
        sum(value * value * count for value, count in histogram.items()),
        PERIOD,
    )
    variance = second_moment - mean * mean
    assert mean == Fraction(911, 3900)
    assert variance == Fraction(4_852_379, 15_210_000)

    print("valuation histogram:", dict(sorted(histogram.items())))
    print("threshold counts:", thresholds)
    print("mean:", mean)
    print("variance:", variance)
    print("PASS")


if __name__ == "__main__":
    main()
