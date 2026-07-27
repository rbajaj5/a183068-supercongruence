"""Exact 2-adic checks for the orientation exponents in Remark C.7."""

from __future__ import annotations


def polynomial(value: int) -> int:
    """The polynomial defining the distinguished 2-adic unit."""

    return value**3 + 2 * value**2 + 1


def hensel_root(precision: int) -> int:
    """Return the unique root modulo 2**precision that is odd modulo 2."""

    root = 1
    modulus = 2
    for _ in range(1, precision):
        next_modulus = 2 * modulus
        candidates = (root, root + modulus)
        roots = [
            candidate
            for candidate in candidates
            if polynomial(candidate) % next_modulus == 0
        ]
        assert len(roots) == 1
        root = roots[0]
        modulus = next_modulus
    return root % modulus


def exponent_classes(precision: int) -> list[tuple[int, int]]:
    """Compute the compatible discrete-log class at every precision."""

    root = hensel_root(precision)
    classes: list[tuple[int, int]] = []
    exponent = 1

    for level in range(3, precision + 1):
        modulus = 2**level
        order = 2 ** (level - 2)
        eta = -pow(3, -1, modulus) % modulus
        exponent %= order

        if pow(root, exponent, modulus) != eta:
            lifted = exponent + order // 2
            assert pow(root, lifted, modulus) == eta
            exponent = lifted

        assert pow(root, exponent, modulus) == eta
        assert pow(root, order, modulus) == 1
        if order > 1:
            assert pow(root, order // 2, modulus) != 1

        if classes:
            previous_level, previous = classes[-1]
            assert previous_level == level - 1
            assert exponent in {previous, previous + 2 ** (level - 3)}

        classes.append((level, exponent))

    return classes


def main() -> None:
    precision = 32
    root = hensel_root(precision)
    classes = exponent_classes(precision)

    assert root % 8 == 5
    assert polynomial(root) % (2**precision) == 0
    assert len({exponent for _, exponent in classes}) > 1

    print(f"root modulo 2^{precision}: {root}")
    print(f"checked {len(classes)} compatible exponent classes")
    print("last five classes:")
    for level, exponent in classes[-5:]:
        print(f"  k={level}: e={exponent} modulo 2^{level - 2}")
    print("all exact orientation-lift checks passed")


if __name__ == "__main__":
    main()
