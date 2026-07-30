"""Exact checks for the Zhang four-matrix counterexample."""

from fractions import Fraction
from itertools import product


Q = Fraction
ZERO = Q(0)
ONE = Q(1)


def matrix(
    a: Fraction, b: Fraction, c: Fraction, d: Fraction
) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    return ((a, b), (c, d))


I = matrix(ONE, ZERO, ZERO, ONE)


def madd(*matrices):
    return tuple(
        tuple(sum((m[i][j] for m in matrices), ZERO) for j in range(2))
        for i in range(2)
    )


def mscale(scalar, m):
    return tuple(tuple(scalar * entry for entry in row) for row in m)


def mmul(left, right):
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(2)), ZERO)
            for j in range(2)
        )
        for i in range(2)
    )


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(2)) for i in range(2))


def trace(m):
    return m[0][0] + m[1][1]


def determinant(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def phase_expression(a, b, c, d):
    anticommutator = madd(mmul(b, c), mmul(c, b))
    return madd(
        mmul(mmul(a, anticommutator), d),
        mmul(mmul(d, anticommutator), a),
    )


# Polynomials in t, stored in ascending coefficient order.
def ptrim(p):
    values = list(p)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def padd(*polynomials):
    degree = max(len(p) for p in polynomials)
    return ptrim(
        tuple(
            sum((p[i] if i < len(p) else ZERO for p in polynomials), ZERO)
            for i in range(degree)
        )
    )


def pscale(scalar, p):
    return ptrim(tuple(scalar * coefficient for coefficient in p))


def pmul(left, right):
    output = [ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] += a * b
    return ptrim(tuple(output))


def peval(p, value):
    output = ZERO
    for coefficient in reversed(p):
        output = output * value + coefficient
    return output


PZERO = (ZERO,)
T = (ZERO, ONE)


def pconstant(value):
    return (value,)


def pmat_from_rational(m):
    return tuple(tuple(pconstant(entry) for entry in row) for row in m)


def pmadd(*matrices):
    return tuple(
        tuple(padd(*(m[i][j] for m in matrices)) for j in range(2))
        for i in range(2)
    )


def pmmul(left, right):
    return tuple(
        tuple(
            padd(*(pmul(left[i][k], right[k][j]) for k in range(2)))
            for j in range(2)
        )
        for i in range(2)
    )


def pphase_expression(a, b, c, d):
    anticommutator = pmadd(pmmul(b, c), pmmul(c, b))
    return pmadd(
        pmmul(pmmul(a, anticommutator), d),
        pmmul(pmmul(d, anticommutator), a),
    )


def peval_matrix(m, value):
    return tuple(tuple(peval(entry, value) for entry in row) for row in m)


def perturb_polynomial(m):
    t_identity = ((T, PZERO), (PZERO, T))
    return pmadd(pmat_from_rational(m), t_identity)


def main() -> None:
    a = matrix(ONE, ZERO, ZERO, ZERO)
    b = matrix(ZERO, ZERO, ZERO, ONE)
    c = matrix(Q(1, 2), Q(-1, 2), Q(-1, 2), Q(1, 2))
    d = matrix(Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 2))
    projectors = (a, b, c, d)

    for projector in projectors:
        assert transpose(projector) == projector
        assert mmul(projector, projector) == projector
        assert trace(projector) == 1
        assert determinant(projector) == 0

    assert madd(a, b) == I
    assert madd(c, d) == I
    assert madd(*projectors) == mscale(2, I)

    anticommutator = madd(mmul(b, c), mmul(c, b))
    assert anticommutator == matrix(
        ZERO, Q(-1, 2), Q(-1, 2), ONE
    )

    x = phase_expression(*projectors)
    expected_x = matrix(Q(-1, 2), Q(-1, 4), Q(-1, 4), ZERO)
    assert x == expected_x
    assert trace(x) == Q(-1, 2)
    assert determinant(x) == Q(-1, 16)
    # The characteristic polynomial is z^2 + z/2 - 1/16.
    assert trace(x) ** 2 - 4 * determinant(x) == Q(1, 2)

    # The t=1/10 positive-definite counterexample.
    t0 = Q(1, 10)
    perturbed = tuple(madd(projector, mscale(t0, I)) for projector in projectors)
    for positive_definite in perturbed:
        assert positive_definite[0][0] > 0
        assert trace(positive_definite) == Q(6, 5)
        assert determinant(positive_definite) == Q(11, 100)

    assert madd(*perturbed) == mscale(Q(12, 5), I)
    x0 = phase_expression(*perturbed)
    assert x0 == matrix(
        Q(-627, 1250), Q(-3, 10), Q(-3, 10), Q(123, 1250)
    )
    assert trace(x0) == Q(-252, 625)
    assert trace(x0) ** 2 - 4 * determinant(x0) == Q(18, 25)
    # sqrt(2) > 132/125 proves the strict norm comparison.
    assert Q(132, 125) ** 2 < 2

    # Verify the full one-parameter perturbation identity over Q[t].
    pa, pb, pc, pd = tuple(perturb_polynomial(m) for m in projectors)
    px = pphase_expression(pa, pb, pc, pd)
    expected_px = (
        (
            (Q(-1, 2), Q(-1, 2), Q(4), Q(8), Q(4)),
            (Q(-1, 4), Q(-1, 2)),
        ),
        (
            (Q(-1, 4), Q(-1, 2)),
            (ZERO, Q(1, 2), Q(4), Q(8), Q(4)),
        ),
    )
    assert px == expected_px

    ptrace = padd(px[0][0], px[1][1])
    pdisc = padd(
        pmul(padd(px[0][0], pscale(-1, px[1][1])),
             padd(px[0][0], pscale(-1, px[1][1]))),
        pscale(4, pmul(px[0][1], px[1][0])),
    )
    y = (ONE, Q(2))
    assert pdisc == pscale(Q(1, 2), pmul(y, y))
    assert pscale(Q(1, 2), ptrace) == pscale(
        Q(1, 4),
        pmul(pmul(y, y), padd(pmul(y, y), pconstant(-2))),
    )

    for sample in (ZERO, Q(1, 20), Q(1, 10), Q(1, 8)):
        direct = phase_expression(
            *(madd(m, mscale(sample, I)) for m in projectors)
        )
        assert peval_matrix(px, sample) == direct

    # Bracket the unique positive threshold tau without floating point.
    def threshold_polynomial(value):
        return 16 * value**3 + 24 * value**2 + 8 * value

    lower = Q(1, 8)
    upper = Q(63, 500)
    assert threshold_polynomial(lower) ** 2 < 2
    assert threshold_polynomial(upper) ** 2 > 2

    # Finite sanity grid for the scalar AM--GM inequality.
    scalar_checks = 0
    for aa, bb, cc, dd in product(range(13), repeat=4):
        assert (aa + bb + cc + dd) ** 4 >= 256 * aa * bb * cc * dd
        scalar_checks += 1

    print("Zhang four-matrix counterexample checks passed")
    print("  4 exact rank-one projector checks")
    print("  exact PSD counterexample and characteristic polynomial")
    print("  exact t=1/10 positive-definite counterexample")
    print("  exact polynomial identity for the full perturbation family")
    print(f"  {scalar_checks} scalar AM--GM grid checks")


if __name__ == "__main__":
    main()
