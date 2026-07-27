"""Exact checks for Frobenius obstruction automata."""

from math import gcd, lcm


DEGREE_SIX = [1, 0, 16, -26, 208, 0, 2197]
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
    """Return power sums through the degree by Newton's identities."""

    degree = len(polynomial) - 1
    traces = [0]
    for n in range(1, degree + 1):
        value = -n * polynomial[n]
        value -= sum(
            polynomial[j] * traces[n - j] for j in range(1, n)
        )
        traces.append(value)
    return traces


def extend_traces(polynomial: list[int], limit: int) -> list[int]:
    traces = newton_traces(polynomial)
    degree = len(polynomial) - 1
    for n in range(degree + 1, limit + 1):
        traces.append(
            -sum(
                polynomial[j] * traces[n - j]
                for j in range(1, degree + 1)
            )
        )
    return traces


def state_cycle(
    polynomial: list[int],
    modulus: int,
    reduced_order: bool = False,
) -> tuple[int, int, int]:
    """Return (preperiod, period, state dimension) after Newton startup."""

    degree = len(polynomial) - 1
    if reduced_order:
        nonzero = [
            j
            for j in range(1, degree + 1)
            if polynomial[j] % modulus
        ]
        order = max(nonzero, default=0)
    else:
        order = degree

    if order == 0:
        return 0, 1, 0

    traces = newton_traces(polynomial)
    state = tuple(value % modulus for value in traces[degree - order + 1 :])
    seen = {state: 0}

    for step in range(1, modulus**order + 2):
        next_value = -sum(
            polynomial[j] * state[-j] for j in range(1, order + 1)
        )
        state = state[1:] + (next_value % modulus,)
        previous = seen.get(state)
        if previous is not None:
            return previous, step - previous, order
        seen[state] = step

    raise AssertionError("finite-state orbit failed to repeat")


def correction_six(r: int) -> int:
    return (
        6
        + 4 * (r % 2 == 0)
        + 6 * (r % 3 == 0)
        + 4 * (r % 4 == 0)
        + 6 * (r % 6 == 0)
    )


def correction_seven(r: int) -> int:
    return (
        2 * (r % 2 == 0)
        + 16 * (r % 4 == 0)
        + 10 * (r % 5 == 0)
        + 10 * (r % 10 == 0)
    )


def minimal_period(values: list[int]) -> int:
    length = len(values)
    for candidate in range(1, length + 1):
        if length % candidate:
            continue
        if all(
            values[index] == values[index % candidate]
            for index in range(length)
        ):
            return candidate
    raise AssertionError("no period found")


def accepting_density(
    polynomial: list[int],
    correction,
    prime: int,
    precision: int,
    trace_period: int,
    trace_preperiod: int,
    finite_period: int,
) -> tuple[int, int, int]:
    modulus = prime**precision
    correction_period = minimal_period(
        [correction(r) % modulus for r in range(1, finite_period + 1)]
    )
    period = lcm(trace_period, correction_period)

    # State-cycle preperiod is measured after the degree-sized Newton
    # startup. This conservative start puts two consecutive packet values
    # inside the eventual cycle.
    start = len(polynomial) + trace_preperiod + 1
    traces = extend_traces(polynomial, start + 2 * period)

    def packet(r: int) -> int:
        return (2 * traces[r] + correction(r)) % modulus

    assert all(
        packet(r + period) == packet(r)
        for r in range(start, start + period + 1)
    )
    accepting = sum(
        packet(r) == packet(r - 1)
        for r in range(start + 1, start + period + 1)
    )
    divisor = gcd(accepting, period)
    return period, accepting // divisor, period // divisor


def valuation(value: int, prime: int) -> int:
    assert value
    exponent = 0
    while value % prime == 0:
        exponent += 1
        value //= prime
    return exponent


def verify_corrected_tower() -> None:
    for prime in (3, 5, 13, 17):
        values = {
            r: prime ** (3 * r) - prime ** (2 * r) for r in range(1, 9)
        }
        for r in range(2, 9):
            assert valuation(values[r] - values[r - 1], prime) == 2 * r - 2


def main() -> None:
    assert newton_traces(DEGREE_SIX)[1:] == [
        0,
        -32,
        78,
        -320,
        -2080,
        622,
    ]
    assert newton_traces(DEGREE_SEVEN)[1:7] == [
        0,
        0,
        -6,
        -28,
        80,
        216,
    ]

    preperiod, period, order = state_cycle(
        DEGREE_SIX, 13, reduced_order=True
    )
    assert (preperiod, period, order) == (0, 12, 2)
    preperiod, period, order = state_cycle(
        DEGREE_SEVEN, 5, reduced_order=True
    )
    assert (preperiod, period, order) == (0, 39, 6)
    assert period <= 5**order - 1

    six_cycles = [
        state_cycle(DEGREE_SIX, 13**precision)[:2]
        for precision in range(1, 5)
    ]
    seven_cycles = [
        state_cycle(DEGREE_SEVEN, 5**precision)[:2]
        for precision in range(1, 5)
    ]
    assert six_cycles == [(0, 12), (2, 156), (4, 2028), (6, 26364)]
    assert seven_cycles == [(0, 39), (1, 195), (2, 975), (3, 4875)]

    # The degree-six packet has no adjacent equality modulo 13.
    traces_six = extend_traces(DEGREE_SIX, 200)
    packet_six = [
        None,
        *[
            (2 * traces_six[r] + correction_six(r)) % 13
            for r in range(1, 201)
        ],
    ]
    assert all(
        packet_six[r] != packet_six[r - 1] for r in range(2, 201)
    )

    expected_seven = [
        (156, 7, 39),
        (780, 8, 195),
        (3900, 2, 195),
        (19500, 11, 3900),
    ]
    observed_seven = []
    for precision, (preperiod, trace_period) in enumerate(
        seven_cycles, start=1
    ):
        observed_seven.append(
            accepting_density(
                DEGREE_SEVEN,
                correction_seven,
                5,
                precision,
                trace_period,
                preperiod,
                20,
            )
        )
    assert observed_seven == expected_seven

    verify_corrected_tower()

    print("degree-six trace cycles:", six_cycles)
    print("degree-seven trace cycles:", seven_cycles)
    print("degree-seven fixed-precision data:", observed_seven)
    print("PASS")


if __name__ == "__main__":
    main()
