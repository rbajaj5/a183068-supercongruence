"""Exact regression checks for the Gaussian Frobenius-twist deduction."""

from math import factorial


Gaussian = tuple[int, int]


def a183068_term(n: int, k: int) -> int:
    return factorial(2 * n + 2 * k) // (
        factorial(k) ** 4 * factorial(n - k) ** 2
    )


def i_power(exponent: int) -> Gaussian:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[exponent % 4]


def minus_one_power(exponent: int) -> Gaussian:
    return (1 if exponent % 2 == 0 else -1, 0)


def twisted_sum(n: int, modulus: int, power) -> Gaussian:
    real = 0
    imaginary = 0
    for k in range(n + 1):
        coefficient = a183068_term(n, k) % modulus
        weight_real, weight_imaginary = power(k)
        real = (real + weight_real * coefficient) % modulus
        imaginary = (imaginary + weight_imaginary * coefficient) % modulus
    return real, imaginary


def verify_odd_frobenius() -> int:
    checks = 0
    for prime in (3, 5, 7, 11, 13):
        for r in (1, 2):
            modulus = prime ** (2 * r)
            for n in range(1, 5):
                current = twisted_sum(n * prime**r, modulus, i_power)
                previous = twisted_sum(
                    n * prime ** (r - 1), modulus, i_power
                )
                if prime % 4 == 3:
                    previous = (previous[0], -previous[1] % modulus)
                assert current == previous
                checks += 1
    return checks


def verify_binary_cross_twist() -> int:
    checks = 0
    for r in (1, 2, 3):
        modulus = 2 ** (2 * r)
        for n in range(1, 5):
            current = twisted_sum(n * 2**r, modulus, i_power)
            previous = twisted_sum(
                n * 2 ** (r - 1), modulus, minus_one_power
            )
            assert current == previous
            checks += 1
    return checks


def main() -> None:
    odd_checks = verify_odd_frobenius()
    binary_checks = verify_binary_cross_twist()
    print(f"odd-prime Gaussian Frobenius checks: {odd_checks}")
    print(f"binary ramified cross-twist checks: {binary_checks}")


if __name__ == "__main__":
    main()
