"""Exact checks for GaussianBaseChangeJacobianCollisions.md."""

from math import gcd


def valuation(number: int, prime: int) -> int:
    assert number
    answer = 0
    while number % prime == 0:
        answer += 1
        number //= prime
    return answer


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def legendre(value: int, prime: int) -> int:
    residue = value % prime
    if residue == 0:
        return 0
    return 1 if pow(residue, (prime - 1) // 2, prime) == 1 else -1


def kappa(prime: int, extension_degree: int) -> int:
    return (
        3
        + legendre(2, prime) ** extension_degree
        + 2 * legendre(-2, prime) ** extension_degree
        + 2 * legendre(6, prime) ** extension_degree
    )


def collision(prime: int, extension_degree: int) -> int:
    q = prime**extension_degree
    return (q - 1) * (q * q + kappa(prime, extension_degree))


def complete_correction(prime: int, extension_degree: int) -> int:
    q = prime**extension_degree
    return collision(prime, extension_degree) - (
        q - 1
    ) * kappa(prime, extension_degree)


def orbit_lengths_after_power(length: int, power: int) -> tuple[int, int]:
    number = gcd(length, power)
    return number, length // number


def verify_prime_ideal_law() -> int:
    cases = 0
    for prime in (3, 5, 7, 11, 13):
        for ramification in (1, 2, 3):
            for residue_degree in (1, 2, 3):
                q = prime**residue_degree
                values = {
                    r: q ** (3 * r) - q ** (2 * r)
                    for r in range(1, 8)
                }
                for r in range(2, 8):
                    rational_valuation = valuation(
                        values[r] - values[r - 1], prime
                    )
                    ideal_valuation = ramification * rational_valuation
                    assert ideal_valuation == (
                        2 * ramification * residue_degree * (r - 1)
                    )
                    cases += 1
    return cases


def verify_orbit_powering() -> int:
    cases = 0
    for length in range(1, 50):
        points = list(range(length))
        for power in range(1, 12):
            unseen = set(points)
            cycles = []
            while unseen:
                start = min(unseen)
                cycle = []
                point = start
                while point not in cycle:
                    cycle.append(point)
                    unseen.remove(point)
                    point = (point + power) % length
                cycles.append(cycle)
            number, new_length = orbit_lengths_after_power(length, power)
            assert len(cycles) == number
            assert {len(cycle) for cycle in cycles} == {new_length}
            cases += 1
    return cases


def verify_gaussian_degree_four() -> tuple[int, int]:
    raw_cases = 0
    corrected_cases = 0
    primes = [p for p in range(5, 200) if is_prime(p)]

    for prime in primes:
        if prime % 4 == 1:
            # A split Gaussian prime has residue degree one.
            for r in range(2, 9):
                current = collision(prime, r)
                previous = collision(prime, r - 1)
                expected = r - 1 if prime % 24 == 1 else 0
                assert valuation(current - previous, prime) == expected
                raw_cases += 1

                corrected_current = complete_correction(prime, r)
                corrected_previous = complete_correction(prime, r - 1)
                assert (
                    valuation(
                        corrected_current - corrected_previous, prime
                    )
                    == 2 * r - 2
                )
                corrected_cases += 1
        else:
            # An inert Gaussian prime has residue degree two, so level r is
            # the rational extension degree 2r and every quadratic sign is 1.
            assert prime % 4 == 3
            for r in range(2, 9):
                assert kappa(prime, 2 * r) == 8
                current = collision(prime, 2 * r)
                previous = collision(prime, 2 * (r - 1))
                assert valuation(current - previous, prime) == 2 * r - 2
                raw_cases += 1

                corrected_current = complete_correction(prime, 2 * r)
                corrected_previous = complete_correction(
                    prime, 2 * (r - 1)
                )
                assert (
                    valuation(
                        corrected_current - corrected_previous, prime
                    )
                    == 4 * r - 4
                )
                corrected_cases += 1

    return raw_cases, corrected_cases


def main() -> None:
    prime_ideal_cases = verify_prime_ideal_law()
    orbit_cases = verify_orbit_powering()
    raw_cases, corrected_cases = verify_gaussian_degree_four()

    print(
        "PASS:",
        prime_ideal_cases,
        "prime-ideal valuation cases;",
        orbit_cases,
        "Frobenius orbit-powering cases;",
        raw_cases,
        "Gaussian split/inert raw cases;",
        corrected_cases,
        "complete-correction cases.",
    )


if __name__ == "__main__":
    main()
