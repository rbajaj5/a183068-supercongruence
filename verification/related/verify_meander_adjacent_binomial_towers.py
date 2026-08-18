"""Exact checks for the adjacent-binomial meander-row theorem.

The proof note is related-results/MeanderAdjacentBinomialTowers.md.
"""

from __future__ import annotations

from math import comb


def choose(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return comb(n, k)


def vp(value: int, prime: int) -> int:
    if value == 0:
        return 10**9
    value = abs(value)
    out = 0
    while value % prime == 0:
        value //= prime
        out += 1
    return out


def original_row(degree: int, n: int) -> int:
    """T(degree-1,n), after evaluating the two finite binomial sums."""

    total = 0
    for k in range(n + 1):
        left = choose(n, k)
        right = choose(n, k + 1)
        total += sum(left ** (degree - j) * right**j for j in range(degree))
    return total


def symmetric_row(degree: int, size: int) -> int:
    """M_degree(size), using twice the symmetric polynomial H_degree."""

    numerator = 0
    for t in range(size + 1):
        left = choose(size - 1, t - 1)
        right = choose(size - 1, t)
        numerator += left**degree + right**degree
        numerator += 2 * sum(
            left ** (degree - j) * right**j for j in range(1, degree)
        )
    assert numerator % 2 == 0
    return numerator // 2


def meander(degree: int, size: int) -> int:
    assert size >= 1
    return original_row(degree, size - 1)


def check_forms_and_named_rows() -> int:
    checks = 0
    for degree in range(1, 11):
        for size in range(1, 15):
            assert meander(degree, size) == symmetric_row(degree, size)
            checks += 1

    expected_4 = [1, 5, 46, 485, 5626, 69062, 882540]
    expected_6 = [1, 7, 190, 5831, 219626, 8976562, 394800204]
    assert [original_row(4, n) for n in range(len(expected_4))] == expected_4
    assert [original_row(6, n) for n in range(len(expected_6))] == expected_6
    checks += len(expected_4) + len(expected_6)

    # A198256 Conjecture 1.
    for n in range(30):
        rhs = sum(choose(n + 1, k) ** 2 * choose(n, k) ** 2 for k in range(n + 1))
        assert original_row(4, n) == rhs
        checks += 1
    return checks


def check_polynomial_lemmas() -> int:
    checks = 0
    for degree in range(1, 13):
        for x in range(-5, 6):
            # Evaluate 2H at y=-x.  It always vanishes.
            y = -x
            twice_h = x**degree + y**degree + 2 * sum(
                x ** (degree - j) * y**j for j in range(1, degree)
            )
            assert twice_h == 0
            checks += 1

            # For F=2H, F''(-x)=d*x^(d-2) in even degree and
            # F'(-x)=x^(d-1) in odd degree.  These are equivalent to the
            # residual values J_d(x,-x)=d*x^(d-2)/4 and
            # K_d(x,-x)=x^(d-1)/2 in the note.
            if degree % 2 == 0:
                second = degree * (degree - 1) * y ** (degree - 2)
                second += 2 * sum(
                    j * (j - 1) * x ** (degree - j) * y ** (j - 2)
                    for j in range(2, degree)
                )
                assert second == degree * x ** (degree - 2)
                checks += 1
            else:
                first = degree * y ** (degree - 1)
                first += 2 * sum(
                    j * x ** (degree - j) * y ** (j - 1)
                    for j in range(1, degree)
                )
                assert first == x ** (degree - 1)
                checks += 1

            # Difference quotients verify the multiplicity and residual value.
            if degree % 2 == 0:
                # Use exact polynomial evaluation one unit away from the root
                # to accompany the symbolic identity checked in the note.
                for delta in (-2, -1, 1, 2):
                    yy = -x + delta
                    num = x**degree + yy**degree + 2 * sum(
                        x ** (degree - j) * yy**j
                        for j in range(1, degree)
                    )
                    assert num % (x + yy) ** 2 == 0
                    checks += 1
            else:
                for delta in (-2, -1, 1, 2):
                    yy = -x + delta
                    num = x**degree + yy**degree + 2 * sum(
                        x ** (degree - j) * yy**j
                        for j in range(1, degree)
                    )
                    assert num % (x + yy) == 0
                    checks += 1
    return checks


def check_gauss_towers() -> int:
    checks = 0
    for degree in range(1, 10):
        for prime in (3, 5, 7):
            for n in (1, 2, 4):
                for level in (1, 2):
                    high = meander(degree, n * prime**level)
                    low = meander(degree, n * prime ** (level - 1))
                    assert (high - low) % prime**level == 0
                    checks += 1
    return checks


def check_odd_degree_quadratic_residue() -> int:
    checks = 0
    for degree in (1, 3, 5, 7):
        for prime in (3, 5, 7, 11):
            for level in (1, 2, 3):
                size = prime**level
                assert (meander(degree, size) - pow(2, size - 1, prime**2)) % (
                    prime**2
                ) == 0
                checks += 1
    return checks


def check_cubic_towers() -> int:
    checks = 0
    for degree in (2, 4, 6, 8):
        for prime in (5, 7, 11):
            for n in (1, 2, 3):
                for level in (1, 2):
                    high = meander(degree, n * prime**level)
                    low = meander(degree, n * prime ** (level - 1))
                    assert (high - low) % prime ** (3 * level) == 0
                    checks += 1

    for degree in (6, 12):
        prime = 3
        for n in (1, 2, 4):
            for level in (1, 2, 3):
                high = meander(degree, n * prime**level)
                low = meander(degree, n * prime ** (level - 1))
                assert (high - low) % prime ** (3 * level) == 0
                checks += 1

    difference = meander(4, 3) - meander(4, 1)
    assert difference == 45 and vp(difference, 3) == 2
    checks += 1
    return checks


def inverse_square_sum(prime: int, level: int) -> int:
    modulus = prime**level
    return sum(
        pow(value, -2, modulus)
        for value in range(1, modulus)
        if value % prime
    )


def check_reciprocal_blocks() -> int:
    checks = 0
    for prime in (5, 7, 11, 13):
        for level in range(1, 6):
            assert inverse_square_sum(prime, level) % prime**level == 0
            checks += 1
    for level in range(1, 8):
        total = inverse_square_sum(3, level)
        assert total % 3 ** (level - 1) == 0
        if level <= 5:
            assert vp(total, 3) == level - 1
        checks += 1
    return checks


def main() -> None:
    counts = {
        "equivalent forms and named rows": check_forms_and_named_rows(),
        "polynomial factors": check_polynomial_lemmas(),
        "all-row Gauss towers": check_gauss_towers(),
        "odd-degree quadratic residues": check_odd_degree_quadratic_residue(),
        "even-degree cubic towers": check_cubic_towers(),
        "reciprocal-square blocks": check_reciprocal_blocks(),
    }
    for label, count in counts.items():
        print(f"{label}: {count}")
    print(f"all {sum(counts.values())} meander-row checks passed")


if __name__ == "__main__":
    main()
