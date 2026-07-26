"""Exact checks for LandauDepthSupercongruenceSynthesis.md.

This is evidence and regression testing, not a replacement for the proof.
All arithmetic is over Python integers and fractions.
"""

from functools import lru_cache
from fractions import Fraction
from math import factorial


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def landau_uv(u: int, v: int, y: Fraction) -> int:
    """Landau fiber for u copies of k and v copies of N-k."""
    return v + floor_fraction((u - v) * y)


def landau_uv_from_floors(u: int, v: int, y: Fraction) -> int:
    """Compute the same fiber directly from its numerator and bottom forms."""
    return (
        floor_fraction((u - v) * y)
        - u * floor_fraction(y)
        - v * floor_fraction(-y)
    )


def multinomial_equal_parts(m: int, k: int) -> int:
    return factorial(m * k) // factorial(k) ** m


@lru_cache(maxsize=None)
def f_uv(u: int, v: int, n: int, k: int) -> int:
    top = u * k + v * (n - k)
    return factorial(top) // (factorial(k) ** u * factorial(n - k) ** v)


@lru_cache(maxsize=None)
def a_uv(u: int, v: int, n: int) -> int:
    return sum(f_uv(u, v, n, k) for k in range(n + 1))


def vp(x: int, p: int) -> int:
    if x == 0:
        return 10**9
    answer = 0
    while x % p == 0:
        answer += 1
        x //= p
    return answer


def vp_factorial(n: int, p: int) -> int:
    answer = 0
    while n:
        n //= p
        answer += n
    return answer


def vp_f_uv(u: int, v: int, n: int, k: int, p: int) -> int:
    top = u * k + v * (n - k)
    return (
        vp_factorial(top, p)
        - u * vp_factorial(k, p)
        - v * vp_factorial(n - k, p)
    )


def apery_zeta2_fiber(y: Fraction) -> int:
    # binom(N,k)^2 binom(N+k,k), evaluated on the fiber x=0.
    binom_n_k = -floor_fraction(y) - floor_fraction(-y)
    binom_n_plus_k_k = floor_fraction(y) - floor_fraction(y)
    return 2 * binom_n_k + binom_n_plus_k_k


def apery_zeta3_fiber(y: Fraction) -> int:
    # binom(N,k)^2 binom(N+k,k)^2.
    binom_n_k = -floor_fraction(y) - floor_fraction(-y)
    binom_n_plus_k_k = floor_fraction(y) - floor_fraction(y)
    return 2 * binom_n_k + 2 * binom_n_plus_k_k


def domb_fiber(y: Fraction) -> int:
    # binom(N,k)^2 binom(2k,k) binom(2N-2k,N-k).
    return (
        2 * (-floor_fraction(y) - floor_fraction(-y))
        + floor_fraction(2 * y)
        - 2 * floor_fraction(y)
        + floor_fraction(-2 * y)
        - 2 * floor_fraction(-y)
    )


def franel_fiber(q: int, y: Fraction) -> int:
    # binom(N,k)^q.
    return q * (-floor_fraction(y) - floor_fraction(-y))


def check_fibers() -> int:
    checks = 0
    for u in range(2, 9):
        for v in range(2, 9):
            values = []
            for denominator in range(2, 41):
                for numerator in range(1, denominator):
                    y = Fraction(numerator, denominator)
                    observed = landau_uv_from_floors(u, v, y)
                    expected = v + floor_fraction((u - v) * y)
                    assert observed == expected
                    values.append(observed)
                    checks += 1
            assert min(values) == min(u, v)
            assert landau_uv(u, v, Fraction(1, 2)) == (u + v) // 2

    for denominator in range(2, 60):
        for numerator in range(1, denominator):
            y = Fraction(numerator, denominator)
            assert apery_zeta2_fiber(y) == 2
            assert apery_zeta3_fiber(y) == 2
            assert domb_fiber(y) == (4 if y == Fraction(1, 2) else 3)
            for q in range(1, 6):
                assert franel_fiber(q, y) == q
            checks += 8
    return checks


def check_active_landau_levels() -> int:
    """Independently check Lemma 1 against Legendre valuations."""
    checks = 0
    for u in range(1, 7):
        for v in range(1, 7):
            depth = min(u, v)
            for p in (2, 3, 5, 7):
                for t in (1, 2, 3):
                    n = p**t
                    for k in range(1, n):
                        s = vp(k, p)
                        if s >= t:
                            continue
                        active_sum = 0
                        first_fraction = None
                        for i in range(s + 1, t + 1):
                            q = p**i
                            y = Fraction(k % q, q)
                            if first_fraction is None:
                                first_fraction = y
                            level = landau_uv_from_floors(u, v, y)
                            assert level >= depth
                            active_sum += level
                        assert active_sum >= depth * (t - s)
                        assert vp_f_uv(u, v, n, k, p) >= active_sum
                        if p == 2:
                            assert first_fraction == Fraction(1, 2)
                        checks += 1
    return checks


def epsilon(p: int) -> int:
    if p == 2:
        return 2
    if p == 3:
        return 1
    return 0


def deficit(p: int, depth: int) -> int:
    return max(0, depth + epsilon(p) - 3)


def check_termwise_transfer() -> int:
    """Check Theorems 2 and 3 before summing over the index."""
    checks = 0

    # Generic transfer, including depths 1, 2, and 3.
    for u in range(1, 7):
        for v in range(1, 7):
            depth = min(3, u, v)
            for p in (2, 3, 5):
                for r in (1, 2):
                    lower_n = p ** (r - 1)
                    modulus = p ** (depth * r - deficit(p, depth))
                    for ell in range(lower_n + 1):
                        difference = (
                            f_uv(u, v, p * lower_n, p * ell)
                            - f_uv(u, v, lower_n, ell)
                        )
                        assert difference % modulus == 0
                        checks += 1

    # The compensated quadratic family at p=2.
    for u in range(2, 9):
        for v in range(2, 9):
            if u + v < 6:
                continue
            for r in (1, 2, 3):
                lower_n = 2 ** (r - 1)
                modulus = 2 ** (2 * r)
                for ell in range(lower_n + 1):
                    difference = (
                        f_uv(u, v, 2 * lower_n, 2 * ell)
                        - f_uv(u, v, lower_n, ell)
                    )
                    assert difference % modulus == 0
                    checks += 1

    # The compensated cubic family at p=2 and p=3.
    for u in range(4, 9):
        for v in range(4, 9):
            if u + v < 10:
                continue
            for p in (2, 3):
                for r in (1, 2):
                    lower_n = p ** (r - 1)
                    modulus = p ** (3 * r)
                    for ell in range(lower_n + 1):
                        difference = (
                            f_uv(u, v, p * lower_n, p * ell)
                            - f_uv(u, v, lower_n, ell)
                        )
                        assert difference % modulus == 0
                        checks += 1

    return checks


def check_uniform_divisibility() -> int:
    checks = 0
    for m in range(3, 9):
        for k in range(1, 40):
            value = multinomial_equal_parts(m, k)
            if m >= 3:
                assert value % 3 == 0
            if m >= 4:
                assert value % 4 == 0
            checks += 1

    for u in range(4, 8):
        for v in range(4, 8):
            for n in range(1, 13):
                for k in range(n + 1):
                    value = f_uv(u, v, n, k)
                    assert value % 3 == 0
                    assert value % 4 == 0
                    checks += 2
    return checks


def check_quadratic_family() -> int:
    """Check the all-prime p^(2r) family u,v>=2 and u+v>=6."""
    checks = 0
    pairs = [
        (u, v)
        for u in range(2, 7)
        for v in range(2, 7)
        if u + v >= 6
    ]
    for u, v in pairs:
        for p in (2, 3, 5, 7):
            for r in (1, 2):
                for n in (1, 2):
                    left = a_uv(u, v, n * p**r)
                    right = a_uv(u, v, n * p ** (r - 1))
                    modulus = p ** (2 * r)
                    assert (left - right) % modulus == 0
                    checks += 1

        # The binary endgame used by the proof.
        for n in range(1, 12):
            for k in range(n + 1):
                assert (f_uv(u, v, 2 * n, 2 * k) - f_uv(u, v, n, k)) % 4 == 0
                checks += 1
    return checks


def check_cubic_family() -> int:
    """Check the all-prime p^(3r) subfamily u,v>=4 and u+v>=10."""
    checks = 0
    pairs = [
        (u, v)
        for u in range(4, 8)
        for v in range(4, 8)
        if u + v >= 10
    ]
    for u, v in pairs:
        assert min(landau_uv(u, v, Fraction(j, 3)) for j in (1, 2)) >= 4
        assert landau_uv(u, v, Fraction(1, 2)) >= 5
        for p in (2, 3, 5, 7):
            for r in (1, 2):
                # n=1 already reaches N=49 and very large exact integers.
                n = 1
                left = a_uv(u, v, n * p**r)
                right = a_uv(u, v, n * p ** (r - 1))
                modulus = p ** (3 * r)
                assert (left - right) % modulus == 0
                checks += 1
    return checks


def check_a183068_sharpness() -> int:
    """A183068 is (u,v)=(4,2): depth 2 and one binary bonus."""
    checks = 0
    assert min(
        landau_uv(4, 2, Fraction(j, 101)) for j in range(1, 101)
    ) == 2
    assert landau_uv(4, 2, Fraction(1, 2)) == 3
    for p in (2, 3, 5, 7, 11):
        difference = a_uv(4, 2, p) - a_uv(4, 2, 1)
        assert difference % p**2 == 0
        checks += 1
    return checks


def main() -> None:
    counts = {
        "fiber identities": check_fibers(),
        "active Landau levels": check_active_landau_levels(),
        "termwise transfer bounds": check_termwise_transfer(),
        "uniform small-prime divisibility": check_uniform_divisibility(),
        "quadratic-family congruences/endgames": check_quadratic_family(),
        "cubic-family congruences": check_cubic_family(),
        "A183068 spot checks": check_a183068_sharpness(),
    }
    print("Landau-depth exact checks passed")
    for label, count in counts.items():
        print(f"  {label}: {count}")
    print(f"  total: {sum(counts.values())}")


if __name__ == "__main__":
    main()
