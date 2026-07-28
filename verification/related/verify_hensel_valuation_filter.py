"""Exact certificates for the weighted Hensel valuation filter."""

from collections import Counter
from fractions import Fraction

from verify_padic_valuation_expansion import (
    LOCAL_L,
    correction,
    extend_traces_mod,
)


P = 5
BASE_PERIOD = 780
CERTIFICATE_PRECISION = 8
CERTIFICATE_MODULUS = P**CERTIFICATE_PRECISION

# Each key is (common valuation, reduced polynomial coefficients in
# ascending order). The value is the complete list of phases with that
# certificate.
EXPECTED_PHASE_GROUPS = {
    (2, (0, 1)): (367,),
    (2, (0, 3)): (36,),
    (2, (0, 4)): (10, 350, 506),
    (2, (1,)): (33,),
    (2, (1, 1)): (287,),
    (2, (1, 2)): (500, 591),
    (2, (1, 4)): (194, 259, 673),
    (2, (2, 1)): (237, 640),
    (2, (2, 2)): (123, 157),
    (2, (2, 3)): (387,),
    (2, (2, 4)): (634,),
    (2, (3, 1)): (510,),
    (2, (3, 2)): (274,),
    (2, (3, 3)): (186,),
    (2, (3, 4)): (166, 233),
    (2, (4,)): (204, 657, 761),
    (2, (4, 1)): (560,),
    (2, (4, 2)): (188,),
    (2, (4, 3)): (537,),
    (3, (0, 3)): (672,),
    (3, (3,)): (189,),
    (4, (0, 4, 2)): (48,),
}

EXPECTED_ROOTS = {
    10: (2, ((0, 4),)),
    36: (2, ((0, 3),)),
    48: (4, ((0, 4), (3, 1))),
    123: (2, ((4, 2),)),
    157: (2, ((4, 2),)),
    166: (2, ((3, 4),)),
    186: (2, ((4, 3),)),
    188: (2, ((3, 2),)),
    194: (2, ((1, 4),)),
    233: (2, ((3, 4),)),
    237: (2, ((3, 1),)),
    259: (2, ((1, 4),)),
    274: (2, ((1, 2),)),
    287: (2, ((4, 1),)),
    350: (2, ((0, 4),)),
    367: (2, ((0, 1),)),
    387: (2, ((1, 3),)),
    500: (2, ((2, 2),)),
    506: (2, ((0, 4),)),
    510: (2, ((2, 1),)),
    537: (2, ((2, 3),)),
    560: (2, ((1, 1),)),
    591: (2, ((2, 2),)),
    634: (2, ((2, 4),)),
    640: (2, ((3, 1),)),
    672: (3, ((0, 3),)),
    673: (2, ((1, 4),)),
}


def valuation(value: int, precision: int) -> int:
    value %= P**precision
    if value == 0:
        return precision
    exponent = 0
    while value % P == 0:
        exponent += 1
        value //= P
    return exponent


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    result = 0
    power = 1
    for coefficient in coefficients:
        result += coefficient * power
        power *= value
    return result % P


def phase_map():
    limit = BASE_PERIOD * (P**4 + P + 2) + BASE_PERIOD + 2
    traces = extend_traces_mod(
        LOCAL_L, limit, CERTIFICATE_MODULUS
    )

    def packet(index: int) -> int:
        return (
            2 * traces[index] + correction(index)
        ) % CERTIFICATE_MODULUS

    def defect(index: int) -> int:
        return (
            packet(index - 1) - packet(index)
        ) % CERTIFICATE_MODULUS

    def phase_defect(phase: int, coordinate: int) -> int:
        return defect(phase + BASE_PERIOD * (coordinate + 1))

    return phase_defect


def verify_phase_certificate() -> None:
    phase_defect = phase_map()
    phase_certificate = {
        phase: (baseline, polynomial)
        for (baseline, polynomial), phases in EXPECTED_PHASE_GROUPS.items()
        for phase in phases
    }
    assert len(phase_certificate) == 32

    accepted = []
    for phase in range(1, BASE_PERIOD + 1):
        values_mod_25 = {
            phase_defect(phase, coordinate) % 25
            for coordinate in range(5)
        }
        assert len(values_mod_25) == 1
        if values_mod_25 == {0}:
            accepted.append(phase)

    assert accepted == sorted(phase_certificate)

    observed_roots = {}
    for phase in accepted:
        baseline, polynomial = phase_certificate[phase]
        sample = [
            phase_defect(phase, coordinate)
            for coordinate in range(P**baseline)
        ]
        assert min(
            valuation(value, CERTIFICATE_PRECISION)
            for value in sample
        ) == baseline
        assert all(value % (P**baseline) == 0 for value in sample)

        reduced = [
            polynomial_value(polynomial, coordinate)
            for coordinate in range(P)
        ]
        assert [
            phase_defect(phase, coordinate) // (P**baseline) % P
            for coordinate in range(P)
        ] == reduced
        assert all(
            phase_defect(phase, coordinate) // (P**baseline) % P
            == reduced[coordinate % P]
            for coordinate in range(P**baseline)
        )

        roots = []
        for coordinate, value in enumerate(reduced):
            if value != 0:
                continue
            derivatives = {
                (
                    (
                        phase_defect(phase, lift + P)
                        - phase_defect(phase, lift)
                    )
                    % CERTIFICATE_MODULUS
                )
                // (P ** (baseline + 1))
                % P
                for lift in range(coordinate, P**baseline, P)
            }
            assert len(derivatives) == 1
            derivative = derivatives.pop()
            assert derivative != 0
            roots.append((coordinate, derivative))
        if roots:
            observed_roots[phase] = (baseline, tuple(roots))

    assert observed_roots == EXPECTED_ROOTS
    inverse_limit_roots = sum(
        len(roots) for _, roots in observed_roots.values()
    )
    weighted_roots = sum(
        len(roots) * P ** (baseline - 2)
        for baseline, roots in observed_roots.values()
    )
    assert inverse_limit_roots == 28
    assert weighted_roots == 80

    assert polynomial_value((0, 4, 2), 0) == 0
    assert polynomial_value((0, 4, 2), 3) == 0
    assert polynomial_value((0, 4, 2), 1) != 0
    assert polynomial_value((0, 3), 0) == 0

    print(
        "phase certificate:",
        f"{len(accepted)} accepted phases,",
        f"{inverse_limit_roots} inverse-limit roots,",
        f"weighted count {weighted_roots}",
    )


def verify_precision_seven_partition() -> None:
    precision = 7
    modulus = P**precision
    trace_preperiod = 6
    trace_period = 39 * P ** (precision - 1)
    period = 156 * P ** (precision - 1)
    start = len(LOCAL_L) + trace_preperiod + 1
    traces = extend_traces_mod(
        LOCAL_L, start + period + 1, modulus
    )

    def packet(index: int) -> int:
        return (2 * traces[index] + correction(index)) % modulus

    assert [
        value % modulus
        for value in traces[start - 11 : start + 1]
    ] == [
        value % modulus
        for value in traces[
            start + trace_period - 11 : start + trace_period + 1
        ]
    ]
    assert packet(start) == packet(start + period)

    histogram = Counter(
        valuation(packet(index - 1) - packet(index), precision)
        for index in range(start + 1, start + period + 1)
    )
    expected = {
        0: 2_000_000,
        1: 337_500,
        2: 75_000,
        3: 18_125,
        4: 4_875,
        5: 1_600,
        6: 320,
        7: 80,
    }
    assert dict(sorted(histogram.items())) == expected
    assert sum(histogram.values()) == period
    assert trace_period == 609_375
    assert period == 2_437_500
    print("precision-7 histogram:", expected)


def verify_limit_law() -> None:
    probabilities = {
        0: Fraction(32, 39),
        1: Fraction(9, 65),
        2: Fraction(2, 65),
        3: Fraction(29, 3900),
        4: Fraction(1, 500),
    }
    tail_mass = Fraction(4, 4875)
    assert sum(probabilities.values(), Fraction()) + tail_mass == 1

    low_mean = sum(
        value * probability
        for value, probability in probabilities.items()
    )
    # For value = 5+t, use the exact sums of 5^(-t) and t 5^(-t).
    exact_tail_mean = Fraction(16, 39 * P**4) * (
        Fraction(5, 1) * Fraction(5, 4)
        + Fraction(5, 16)
    )
    mean = low_mean + exact_tail_mean

    low_second = sum(
        value * value * probability
        for value, probability in probabilities.items()
    )
    # With value = 5+t, sum (5+t)^2 / 5^t.
    sum_one = Fraction(5, 4)
    sum_t = Fraction(5, 16)
    sum_t_squared = Fraction(15, 32)
    exact_tail_second = Fraction(16, 39 * P**4) * (
        25 * sum_one + 10 * sum_t + sum_t_squared
    )
    second = low_second + exact_tail_second
    variance = second - mean * mean

    assert mean == Fraction(61, 260)
    assert second == Fraction(23, 60)
    assert variance == Fraction(66_577, 202_800)
    print("limit mean and variance:", mean, variance)


def main() -> None:
    verify_phase_certificate()
    verify_precision_seven_partition()
    verify_limit_law()
    print("PASS")


if __name__ == "__main__":
    main()
