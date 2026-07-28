"""Exact checks for controller-filtered periodic-orbit congruences."""

from __future__ import annotations

from itertools import product
from math import isqrt
from random import Random


Vector = tuple[int, ...]


def add(left: Vector, right: Vector) -> Vector:
    return tuple(x + y for x, y in zip(left, right))


def scale(factor: int, value: Vector) -> Vector:
    return tuple(factor * x for x in value)


def sub(left: Vector, right: Vector) -> Vector:
    return tuple(x - y for x, y in zip(left, right))


def change_denomination(value: Vector) -> tuple[int, int]:
    x, y, z = value
    return (2 * x - y + 3 * z, -x + 4 * y)


def mobius(n: int) -> int:
    result = 1
    prime = 2
    remaining = n
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            result = -result
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        result = -result
    return result


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + list(reversed(large))


def iterate(mapping: tuple[int, ...], start: int, steps: int) -> int:
    value = start
    for _ in range(steps):
        value = mapping[value]
    return value


def primitive_cycles(mapping: tuple[int, ...]) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()
    size = len(mapping)
    for start in range(size):
        seen: dict[int, int] = {}
        path: list[int] = []
        value = start
        while value not in seen:
            seen[value] = len(path)
            path.append(value)
            value = mapping[value]
        cycle = path[seen[value] :]
        smallest = min(range(len(cycle)), key=lambda i: cycle[i])
        canonical = tuple(cycle[smallest:] + cycle[:smallest])
        cycles.add(canonical)
    return sorted(cycles)


def cycle_data(
    mapping: tuple[int, ...],
) -> tuple[list[tuple[int, ...]], dict[int, int], list[Vector]]:
    cycles = primitive_cycles(mapping)
    owner: dict[int, int] = {}
    weights: list[Vector] = []
    for index, cycle in enumerate(cycles):
        for state in cycle:
            owner[state] = index
        weights.append(
            (
                1 + sum(cycle),
                (-1 if len(cycle) % 2 else 1) * (1 + cycle[0]),
                len(cycle) * len(cycle),
            )
        )
    return cycles, owner, weights


def weighted_fixed_count(mapping: tuple[int, ...], steps: int) -> Vector:
    cycles, owner, weights = cycle_data(mapping)
    del cycles
    total = (0, 0, 0)
    for state in range(len(mapping)):
        if iterate(mapping, state, steps) == state:
            total = add(total, weights[owner[state]])
    return total


def denominated_fixed_count(
    mapping: tuple[int, ...], steps: int
) -> tuple[int, int]:
    cycles, owner, weights = cycle_data(mapping)
    del cycles
    total = (0, 0)
    for state in range(len(mapping)):
        if iterate(mapping, state, steps) == state:
            weight = change_denomination(weights[owner[state]])
            total = (total[0] + weight[0], total[1] + weight[1])
    return total


def aggregate_primitive_weights(
    mapping: tuple[int, ...], length: int
) -> Vector:
    cycles, _, weights = cycle_data(mapping)
    total = (0, 0, 0)
    for cycle, weight in zip(cycles, weights):
        if len(cycle) == length:
            total = add(total, weight)
    return total


def verify_mapping(mapping: tuple[int, ...], max_n: int = 18) -> int:
    counts = {
        n: weighted_fixed_count(mapping, n) for n in range(1, max_n + 1)
    }
    checks = 0
    for n in range(1, max_n + 1):
        assert denominated_fixed_count(mapping, n) == change_denomination(
            counts[n]
        )
        checks += 1
        mobius_sum = (0, 0, 0)
        for d in divisors(n):
            mobius_sum = add(
                mobius_sum, scale(mobius(n // d), counts[d])
            )
        expected = scale(n, aggregate_primitive_weights(mapping, n))
        assert mobius_sum == expected
        assert all(value % n == 0 for value in mobius_sum)
        checks += 1

    for prime in (2, 3, 5, 7):
        power = prime
        previous = counts[1]
        while power <= max_n:
            current = counts[power]
            defect = sub(current, previous)
            expected = scale(
                power, aggregate_primitive_weights(mapping, power)
            )
            assert defect == expected
            assert all(value % power == 0 for value in defect)
            previous = current
            power *= prime
            checks += 1
    return checks


def verify_all_small_maps() -> int:
    checks = 0
    maps = 0
    for size in range(1, 6):
        for mapping in product(range(size), repeat=size):
            checks += verify_mapping(mapping)
            maps += 1
    print(f"checked all {maps} self-maps on at most five states")
    return checks


def matmul(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(size))
            for j in range(size)
        )
        for i in range(size)
    )


def identity(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(1 if i == j else 0 for j in range(size)) for i in range(size)
    )


def trace(matrix: tuple[tuple[int, ...], ...]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def verify_adjacency_matrices(max_n: int = 12) -> int:
    checks = 0
    matrices = 0
    for size in range(1, 4):
        for entries in product((0, 1), repeat=size * size):
            matrix = tuple(
                tuple(entries[size * i + j] for j in range(size))
                for i in range(size)
            )
            powers = identity(size)
            traces: dict[int, int] = {}
            for n in range(1, max_n + 1):
                powers = matmul(powers, matrix)
                traces[n] = trace(powers)
            for n in range(1, max_n + 1):
                numerator = sum(
                    mobius(n // d) * traces[d] for d in divisors(n)
                )
                assert numerator % n == 0
                assert numerator >= 0
                checks += 1
            for prime in (2, 3, 5, 7):
                power = prime
                previous = traces[1]
                while power <= max_n:
                    assert (traces[power] - previous) % power == 0
                    previous = traces[power]
                    power *= prime
                    checks += 1
            matrices += 1
    print(f"checked all {matrices} binary adjacency matrices of size <= 3")
    return checks


def verify_schottky_formula(max_n: int = 20) -> int:
    checks = 0
    for genus in range(2, 7):
        size = 2 * genus
        matrix = tuple(
            tuple(0 if target == (source ^ 1) else 1 for target in range(size))
            for source in range(size)
        )
        power = identity(size)
        traces: dict[int, int] = {}
        for n in range(1, max_n + 1):
            power = matmul(power, matrix)
            traces[n] = trace(power)
            expected = (
                (2 * genus - 1) ** n
                + (genus - 1) * ((-1) ** n)
                + genus
            )
            assert traces[n] == expected
            checks += 1
        for prime in (2, 3, 5, 7):
            prime_power = prime
            previous = traces[1]
            while prime_power <= max_n:
                assert (traces[prime_power] - previous) % prime_power == 0
                previous = traces[prime_power]
                prime_power *= prime
                checks += 1
    print("checked Schottky no-backtracking trace formula")
    return checks


def controller_product(
    environment: tuple[int, ...], update_bits: tuple[int, ...]
) -> tuple[int, ...]:
    size = len(environment)
    mapping: list[int] = []
    for env_state, memory in product(range(size), range(2)):
        next_env = environment[env_state]
        next_memory = update_bits[2 * env_state + memory]
        mapping.append(2 * next_env + next_memory)
    return tuple(mapping)


def verify_controller_products() -> int:
    checks = 0
    products_checked = 0
    for size in range(1, 4):
        for environment in product(range(size), repeat=size):
            for update_bits in product((0, 1), repeat=2 * size):
                closed_loop = controller_product(environment, update_bits)
                checks += verify_mapping(closed_loop, max_n=12)
                products_checked += 1

    rng = Random(91282)
    size = 4
    for _ in range(1000):
        environment = tuple(rng.randrange(size) for _ in range(size))
        update_bits = tuple(rng.randrange(2) for _ in range(2 * size))
        checks += verify_mapping(
            controller_product(environment, update_bits), max_n=18
        )
        products_checked += 1
    print(f"checked {products_checked} finite controller products")
    return checks


def pareto_undominated(outcomes: list[tuple[int, ...]]) -> list[bool]:
    result: list[bool] = []
    for j, outcome in enumerate(outcomes):
        dominated = False
        for i, competitor in enumerate(outcomes):
            if i == j:
                continue
            weakly_better = all(x >= y for x, y in zip(competitor, outcome))
            strictly_better = any(x > y for x, y in zip(competitor, outcome))
            if weakly_better and strictly_better:
                dominated = True
                break
        result.append(not dominated)
    return result


def verify_replay_pareto_table() -> int:
    outcomes = [(1, 21), (1, 23), (0, 24)]
    assert pareto_undominated(outcomes) == [False, True, True]
    return len(outcomes)


def next_power_of_two_above(n: int) -> int:
    power = 1
    while power <= n:
        power *= 2
    return power


def fixed_count(mapping: tuple[int, ...], steps: int) -> int:
    return sum(
        iterate(mapping, state, steps) == state
        for state in range(len(mapping))
    )


def verify_gold_horizon_obstruction() -> int:
    checks = 0
    base = (0,)
    for horizon in (1, 2, 3, 5, 8, 13, 21, 34):
        cycle_length = next_power_of_two_above(horizon)
        cycle = tuple(
            1 + ((offset + 1) % cycle_length)
            for offset in range(cycle_length)
        )
        extension = base + cycle
        for n in range(1, horizon + 1):
            assert fixed_count(extension, n) == fixed_count(base, n)
            checks += 1
        previous = cycle_length // 2
        defect_delta = (
            fixed_count(extension, cycle_length)
            - fixed_count(extension, previous)
            - fixed_count(base, cycle_length)
            + fixed_count(base, previous)
        )
        assert defect_delta == cycle_length
        assert defect_delta // cycle_length == 1
        checks += 2
    print("checked Gold-style finite-horizon obstruction")
    return checks


def main() -> None:
    map_checks = verify_all_small_maps()
    matrix_checks = verify_adjacency_matrices()
    schottky_checks = verify_schottky_formula()
    controller_checks = verify_controller_products()
    pareto_checks = verify_replay_pareto_table()
    gold_checks = verify_gold_horizon_obstruction()
    total = (
        map_checks
        + matrix_checks
        + schottky_checks
        + controller_checks
        + pareto_checks
        + gold_checks
    )
    print(
        "PASS: controller-filtered periodic-orbit supercongruences "
        f"({total} exact checks: {map_checks} maps, "
        f"{matrix_checks} matrices, {schottky_checks} Schottky, "
        f"{controller_checks} controllers, {pareto_checks} replay outcomes, "
        f"{gold_checks} Gold-style obstruction)"
    )


if __name__ == "__main__":
    main()
