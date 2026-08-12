"""Exact checks for the mixed-step coefficient tower containing A246437."""

from math import comb


PARAMETERS = (
    (1, 1, 1),
    (2, 1, 1),
    (3, 2, 1),
    (4, 3, 2),
    (2, 5, 3),
)
PRIMES = (5, 7, 11, 13)
ARGUMENT_CAP = 600
BASE_N_CAP = 30


def mixed_step_coefficient(n: int, u: int, v: int, c: int) -> int:
    """Return [x^(c*n)] ((1+x^u)/(1-x^v))^n for positive n."""
    total = 0
    for j in range(n + 1):
        remainder = c * n - u * j
        if remainder < 0 or remainder % v:
            continue
        k = remainder // v
        total += comb(n, j) * comb(n + k - 1, k)
    return total


def check_a246437_initial_values() -> int:
    expected = (
        1,
        0,
        2,
        3,
        10,
        25,
        71,
        196,
        554,
        1569,
        4477,
        12826,
        36895,
        106470,
        308114,
        893803,
    )
    actual = [1]
    actual.extend(mixed_step_coefficient(n, 3, 2, 1) for n in range(1, 16))
    assert tuple(actual) == expected
    return len(expected)


def check_towers() -> tuple[int, int]:
    caches: dict[tuple[int, int, int], dict[int, int]] = {
        parameters: {} for parameters in PARAMETERS
    }
    cases = 0
    sharp = 0
    for u, v, c in PARAMETERS:
        cache = caches[(u, v, c)]

        def value(n: int) -> int:
            if n not in cache:
                cache[n] = mixed_step_coefficient(n, u, v, c)
            return cache[n]

        for prime in PRIMES:
            if u % prime == 0 or v % prime == 0:
                continue
            for level in range(1, 4):
                modulus = prime ** (2 * level)
                for n in range(1, BASE_N_CAP + 1):
                    if n * prime**level > ARGUMENT_CAP:
                        continue
                    difference = value(n * prime**level) - value(
                        n * prime ** (level - 1)
                    )
                    assert difference % modulus == 0, (
                        u,
                        v,
                        c,
                        prime,
                        level,
                        n,
                    )
                    if difference % (prime * modulus) != 0:
                        sharp += 1
                    cases += 1
    assert cases == 782
    assert sharp > 0
    return cases, sharp


def main() -> None:
    initial = check_a246437_initial_values()
    cases, sharp = check_towers()
    print(f"A246437 initial values: {initial} exact matches")
    print(f"mixed-step towers: {cases} cases ({sharp} sharp witnesses)")
    print("all mixed-step coefficient checks passed")


if __name__ == "__main__":
    main()
