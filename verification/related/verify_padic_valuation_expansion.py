"""Certificates for the degree-seven p-adic precision-lifting theorem."""

from collections import Counter
from fractions import Fraction
from math import lcm


P = 5
CHI = [
    15625,
    0,
    0,
    250,
    175,
    -80,
    -34,
    -16,
    7,
    2,
    0,
    0,
    1,
]
LOCAL_L = [
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
UNIT_FACTOR_125 = [111, 44, 92, 2, 100, 105, 1]
NONUNIT_FACTOR_125 = [0, 0, 0, 0, 50, 20, 1]


def convolution(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def matrix_multiply(
    left: list[list[int]], right: list[list[int]], modulus: int
) -> list[list[int]]:
    return [
        [
            sum(
                left[i][k] * right[k][j] for k in range(len(right))
            )
            % modulus
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matrix_vector(
    matrix: list[list[int]], vector: list[int], modulus: int
) -> list[int]:
    return [
        sum(row[j] * vector[j] for j in range(len(vector))) % modulus
        for row in matrix
    ]


def matrix_power(
    matrix: list[list[int]], exponent: int, modulus: int
) -> list[list[int]]:
    result = [
        [int(i == j) for j in range(len(matrix))]
        for i in range(len(matrix))
    ]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, matrix, modulus)
        matrix = matrix_multiply(matrix, matrix, modulus)
        exponent //= 2
    return result


def companion(polynomial: list[int], modulus: int) -> list[list[int]]:
    degree = len(polynomial) - 1
    matrix = [[0] * degree for _ in range(degree)]
    for i in range(degree - 1):
        matrix[i][i + 1] = 1
    matrix[-1] = [(-polynomial[i]) % modulus for i in range(degree)]
    return matrix


def newton_traces(polynomial: list[int], modulus: int) -> list[int]:
    degree = len(polynomial) - 1
    traces = [0]
    for n in range(1, degree + 1):
        value = -n * polynomial[degree - n]
        value -= sum(
            polynomial[degree - j] * traces[n - j]
            for j in range(1, n)
        )
        traces.append(value % modulus)
    return traces


def vector_period(
    matrix: list[list[int]],
    vector: list[int],
    modulus: int,
    bound: int,
) -> int:
    current = vector[:]
    target = [entry % modulus for entry in vector]
    for period in range(1, bound + 1):
        current = matrix_vector(matrix, current, modulus)
        if current == target:
            return period
    raise AssertionError("period not found")


def full_newton_traces(polynomial: list[int]) -> list[int]:
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
    traces = [
        value % modulus for value in full_newton_traces(polynomial)
    ]
    for n in range(degree + 1, limit + 1):
        traces.append(
            -sum(
                polynomial[j] * traces[n - j]
                for j in range(1, degree + 1)
            )
            % modulus
        )
    return traces


def trace_state_cycle(
    polynomial: list[int], modulus: int
) -> tuple[int, int]:
    degree = len(polynomial) - 1
    traces = full_newton_traces(polynomial)
    state = tuple(value % modulus for value in traces[1:])
    seen = {state: 0}
    step = 0
    while True:
        next_value = -sum(
            polynomial[j] * state[-j] for j in range(1, degree + 1)
        )
        state = state[1:] + (next_value % modulus,)
        step += 1
        previous = seen.get(state)
        if previous is not None:
            return previous, step - previous
        seen[state] = step


def correction(r: int) -> int:
    return (
        2 * (r % 2 == 0)
        + 16 * (r % 4 == 0)
        + 10 * (r % 5 == 0)
        + 10 * (r % 10 == 0)
    )


def truncated_valuation(value: int, precision: int) -> int:
    value %= P**precision
    if value == 0:
        return precision
    exponent = 0
    while value % P == 0:
        exponent += 1
        value //= P
    return exponent


def packet_histogram(
    precision: int,
    trace_preperiod: int,
    trace_period: int,
) -> tuple[int, Counter[int]]:
    modulus = P**precision
    period = lcm(trace_period, 20)
    start = len(LOCAL_L) + trace_preperiod + 1
    traces = extend_traces_mod(
        LOCAL_L, start + 2 * period + 1, modulus
    )

    def packet(r: int) -> int:
        return (2 * traces[r] + correction(r)) % modulus

    assert all(
        packet(r + period) == packet(r)
        for r in range(start - 1, start + period + 1)
    )
    histogram = Counter(
        truncated_valuation(packet(r - 1) - packet(r), precision)
        for r in range(start + 1, start + period + 1)
    )
    return period, histogram


def verify_hensel_and_matrix_certificate() -> None:
    assert [
        coefficient % 125
        for coefficient in convolution(
            UNIT_FACTOR_125, NONUNIT_FACTOR_125
        )
    ] == [coefficient % 125 for coefficient in CHI]

    matrix_125 = companion(UNIT_FACTOR_125, 125)
    state_125 = newton_traces(UNIT_FACTOR_125, 125)[1:]
    assert state_125 == [20, 75, 119, 97, 80, 91]

    matrix_5 = [[entry % 5 for entry in row] for row in matrix_125]
    matrix_25 = [[entry % 25 for entry in row] for row in matrix_125]
    assert vector_period(matrix_5, state_125, 5, 500) == 39
    assert vector_period(matrix_25, state_125, 25, 1000) == 195

    power_195 = matrix_power(matrix_125, 195, 125)
    assert all(
        (power_195[i][j] - int(i == j)) % 5 == 0
        for i in range(6)
        for j in range(6)
    )
    difference = [
        (image - source) % 125
        for image, source in zip(
            matrix_vector(power_195, state_125, 125), state_125
        )
    ]
    assert difference == [100, 25, 100, 75, 0, 25]
    assert [entry // 25 for entry in difference] == [4, 1, 4, 3, 0, 1]


def verify_high_precision_histograms() -> None:
    expected_cycles = {
        5: (4, 24_375),
        6: (5, 121_875),
    }
    observed_cycles = {
        precision: trace_state_cycle(LOCAL_L, P**precision)
        for precision in expected_cycles
    }
    assert observed_cycles == expected_cycles

    period_5, histogram_5 = packet_histogram(5, *expected_cycles[5])
    period_6, histogram_6 = packet_histogram(6, *expected_cycles[6])
    assert period_5 == 97_500
    assert period_6 == 487_500
    assert dict(sorted(histogram_5.items())) == {
        0: 80_000,
        1: 13_500,
        2: 3_000,
        3: 725,
        4: 195,
        5: 80,
    }
    assert dict(sorted(histogram_6.items())) == {
        0: 400_000,
        1: 67_500,
        2: 15_000,
        3: 3_625,
        4: 975,
        5: 320,
        6: 80,
    }

    thresholds_6 = {
        h: sum(
            count
            for value, count in histogram_6.items()
            if value >= h
        )
        for h in range(1, 7)
    }
    assert thresholds_6 == {
        1: 87_500,
        2: 20_000,
        3: 5_000,
        4: 1_375,
        5: 400,
        6: 80,
    }
    assert Fraction(thresholds_6[5], period_6) == Fraction(4, 4875)
    assert Fraction(thresholds_6[6], period_6) == Fraction(4, 24375)

    mean = Fraction(
        sum(value * count for value, count in histogram_6.items()),
        period_6,
    )
    second = Fraction(
        sum(value * value * count for value, count in histogram_6.items()),
        period_6,
    )
    assert mean == Fraction(22_871, 97_500)
    assert second - mean * mean == Fraction(
        3_115_714_859, 9_506_250_000
    )

    print("trace-state cycles:", observed_cycles)
    print("precision-5 histogram:", dict(sorted(histogram_5.items())))
    print("precision-6 histogram:", dict(sorted(histogram_6.items())))


def verify_valuation_expansion() -> None:
    for value in range(1, 10_001):
        for precision in range(1, 9):
            lhs = truncated_valuation(value, precision)
            rhs = sum(value % (P**h) == 0 for h in range(1, precision + 1))
            assert lhs == rhs


def main() -> None:
    verify_hensel_and_matrix_certificate()
    verify_high_precision_histograms()
    verify_valuation_expansion()
    print("PASS")


if __name__ == "__main__":
    main()
