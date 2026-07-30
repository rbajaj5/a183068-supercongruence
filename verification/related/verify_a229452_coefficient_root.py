"""Exact checks for A229452CoefficientRootBaseline.md."""

from __future__ import annotations

from math import factorial


def seed(m: int, n: int) -> int:
    return factorial(m * n) // (factorial(m) * factorial(n) ** m)


def valuation(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def exponent(prime: int, r: int) -> int:
    if prime == 2:
        return 3 * r - 2
    if prime == 3:
        return 3 * r - 1
    return 3 * r


def exponential_root(m: int, degree: int) -> list[int]:
    """E=exp(sum B(n)x^n/n), via n*e_n=sum B(k)e_(n-k)."""
    out = [1]
    for n in range(1, degree + 1):
        numerator = sum(seed(m, k) * out[n - k] for k in range(1, n + 1))
        assert numerator % n == 0
        out.append(numerator // n)
    return out


def multiply(a: list[int], b: list[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[: degree + 1 - i]):
                if y:
                    out[i + j] += x * y
    return out


def power_coefficient(series: list[int], power: int, degree: int) -> int:
    result = [1] + [0] * degree
    base = series[: degree + 1]
    e = power
    while e:
        if e & 1:
            result = multiply(result, base, degree)
        e //= 2
        if e:
            base = multiply(base, base, degree)
    return result[degree]


def inverse_series(series: list[int], degree: int) -> list[int]:
    assert series[0] in (1, -1)
    out = [series[0]]
    for n in range(1, degree + 1):
        value = -sum(series[k] * out[n - k] for k in range(1, n + 1))
        out.append(value * series[0])
    return out


def signed_power_coefficient(
    series: list[int], power: int, degree: int
) -> int:
    if power >= 0:
        return power_coefficient(series, power, degree)
    inverse = inverse_series(series, degree)
    return power_coefficient(inverse, -power, degree)


def canonical_root(e_series: list[int], degree: int) -> list[int]:
    """Solve E(x)=F(xE(x)) recursively."""
    y = [0] + e_series[:degree]
    powers = [[1] + [0] * degree]
    for _ in range(degree):
        powers.append(multiply(powers[-1], y, degree))
    f = [1]
    for n in range(1, degree + 1):
        known = sum(f[j] * powers[j][n] for j in range(n))
        coefficient_of_new = powers[n][n]
        assert coefficient_of_new == 1
        f.append(e_series[n] - known)
    return f


def main() -> None:
    seed_integrality = 0
    seed_scaling = 0
    series_integrality = 0
    bridge_checks = 0
    tower_checks = 0
    generalized_checks = 0
    cubic_evidence = 0

    for m in range(1, 9):
        for n in range(1, 25):
            assert seed(m, n) == factorial(m * n) // (
                factorial(m) * factorial(n) ** m
            )
            seed_integrality += 1

        e_series = exponential_root(m, 24)
        assert all(isinstance(value, int) for value in e_series)
        series_integrality += len(e_series) - 1

        f_series = canonical_root(e_series, 10)
        for n in range(1, 9):
            assert power_coefficient(f_series, n, n) == seed(m, n)
            assert 2 * power_coefficient(e_series, n, n) == power_coefficient(
                f_series, 2 * n, n
            )
            bridge_checks += 2

    for prime in (2, 3, 5, 7):
        for r in (1, 2, 3):
            for m in range(1, 8):
                for n in range(1, 6):
                    difference = seed(m, n * prime**r) - seed(
                        m, n * prime ** (r - 1)
                    )
                    assert valuation(difference, prime) >= exponent(prime, r)
                    seed_scaling += 1

    for m in range(1, 6):
        e_series = exponential_root(m, 100)
        for prime in (2, 3, 5, 7):
            for r in (1, 2):
                for n in (1, 2):
                    upper = n * prime**r
                    lower = n * prime ** (r - 1)
                    high = power_coefficient(e_series, upper, upper)
                    low = power_coefficient(e_series, lower, lower)
                    assert (high - low) % prime**r == 0
                    tower_checks += 1
                    if prime >= 5:
                        assert (high - low) % prime ** (3 * r) == 0
                        cubic_evidence += 1

    for m in range(1, 4):
        e_series = exponential_root(m, 40)
        for degree_scale in (1, 2, 3):
            for power_scale in (-2, -1, 1, 2):
                for prime in (2, 3, 5):
                    for n in (1, 2):
                        upper_n = n * prime
                        lower_n = n
                        high = signed_power_coefficient(
                            e_series,
                            power_scale * upper_n,
                            degree_scale * upper_n,
                        )
                        low = signed_power_coefficient(
                            e_series,
                            power_scale * lower_n,
                            degree_scale * lower_n,
                        )
                        assert (high - low) % prime == 0
                        generalized_checks += 1

    print("A229452 coefficient-root baseline checks passed")
    print(f"seed integrality checks: {seed_integrality}")
    print(f"strong seed-scaling checks: {seed_scaling}")
    print(f"integral exponential coefficients: {series_integrality}")
    print(f"Lagrange bridge checks: {bridge_checks}")
    print(f"proved baseline tower checks: {tower_checks}")
    print(f"generalized (m,R,S) tower checks: {generalized_checks}")
    print(f"open cubic evidence checks: {cubic_evidence}")
    print(
        "total exact checks: "
        f"{seed_integrality + seed_scaling + series_integrality + bridge_checks + tower_checks + generalized_checks + cubic_evidence}"
    )


if __name__ == "__main__":
    main()
