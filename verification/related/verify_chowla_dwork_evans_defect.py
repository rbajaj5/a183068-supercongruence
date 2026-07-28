"""Exact checks of the Chowla--Dwork--Evans split-prime defect law."""

from math import comb, isqrt


LIMIT = 20_000


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            count = (limit - start) // candidate + 1
            sieve[start : limit + 1 : candidate] = b"\x00" * count
    return [number for number in range(2, limit + 1) if sieve[number]]


def primary_real_coordinate(prime: int) -> int:
    """Return signed a with p=a^2+b^2, a odd, b even, and a=1 mod 4."""

    for positive_a in range(1, isqrt(prime) + 1, 2):
        b_squared = prime - positive_a * positive_a
        b = isqrt(b_squared)
        if b * b == b_squared and b % 2 == 0:
            if positive_a % 4 == 1:
                return positive_a
            return -positive_a
    raise AssertionError(f"no primary sum-of-squares coordinate for {prime}")


def verify_prime(prime: int) -> tuple[int, bool]:
    a = primary_real_coordinate(prime)
    modulus = prime * prime
    binomial = comb((prime - 1) // 2, (prime - 1) // 4)

    power_residue = pow(2, prime - 1, modulus)
    fermat_quotient_mod_p = (power_residue - 1) // prime

    first_factor = (
        1 + (power_residue - 1) * pow(2, -1, modulus)
    ) % modulus
    second_factor = (
        2 * a - prime * pow(2 * a, -1, modulus)
    ) % modulus
    published_rhs = first_factor * second_factor % modulus
    assert binomial % modulus == published_rhs

    assert (binomial - 2 * a) % prime == 0
    defect = ((binomial - 2 * a) // prime) % prime
    predicted_defect = (
        a * fermat_quotient_mod_p - pow(2 * a, -1, prime)
    ) % prime
    assert defect == predicted_defect

    exceptional_criterion = (
        2 * a * a * fermat_quotient_mod_p - 1
    ) % prime == 0
    assert (defect == 0) == exceptional_criterion
    return a, defect == 0


def main() -> None:
    checked = 0
    exceptional: list[tuple[int, int]] = []
    for prime in primes_up_to(LIMIT - 1):
        if prime % 4 != 1:
            continue
        a, vanishes = verify_prime(prime)
        checked += 1
        if vanishes:
            exceptional.append((prime, a))

    assert checked == 1125
    assert exceptional == [(5, 1)]
    print(f"split primes checked below {LIMIT}: {checked}")
    print(f"vanishing normalized defects: {exceptional}")


if __name__ == "__main__":
    main()

