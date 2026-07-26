# Pfaffian bias and a sharp finite-field supercongruence

## Status

This note proves an exact additive-character sum for the Pfaffian on
alternating matrices in every finite characteristic and extracts a sharp
adjacent-extension supercongruence.

Counts of alternating matrices by rank are classical. A targeted search found
the surrounding rank-enumeration and prehomogeneous-vector-space literature,
but not the exact adjacent-\(p^r\) valuation or the two-ended-polynomial
formulation below. Those aspects are recorded as apparently new, with
literature priority provisional.

## Setup

Let \(q\) be a prime power and let

\[
\psi:(\mathbf F_q,+)\longrightarrow\mathbf C^\times
\]

be a nontrivial additive character. Let
\(\operatorname{Alt}_{2m}(\mathbf F_q)\) denote the alternating
\(2m\)-by-\(2m\) matrices. This means skew-symmetric matrices with zero
diagonal in odd characteristic, and symmetric matrices with zero diagonal in
characteristic \(2\).

The Pfaffian is defined by its usual integral polynomial, so it is meaningful
in every characteristic. Define

\[
\mathcal P_m(q)
:=\sum_{A\in\operatorname{Alt}_{2m}(\mathbf F_q)}
\psi(\operatorname{Pf}(A)),
\qquad m\geq2,
\]

and set

\[
F_m:=m^2-m+1.
\]

## Exact character sum

### Theorem 1

For every prime power \(q\), every \(m\geq2\), and every nontrivial additive
character \(\psi\),

\[
\boxed{
\mathcal P_m(q)
=q^{m(2m-1)}
-q^{F_m}\prod_{j=2}^{m}(q^{2j-1}-1).
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\frac{\mathcal P_m(q)}{q^{m(2m-1)}}
=1-\prod_{j=2}^{m}(1-q^{-(2j-1)}).
}
\tag{2}
\]

### Proof

Write an alternating \(2m\)-by-\(2m\) matrix as

\[
A=
\begin{pmatrix}
B&v\\
-v^{\mathsf T}&0
\end{pmatrix},
\]

where \(B\) is alternating of size \(2m-1\). Expansion along the final row
shows that \(\operatorname{Pf}(A)\) is a linear functional of \(v\).
Its coefficients are the maximal principal Pfaffians of \(B\).

If \(\operatorname{rank}B=2m-2\), at least one such coefficient is nonzero.
The character sum over \(v\) is therefore zero. If
\(\operatorname{rank}B\leq2m-4\), all coefficients vanish and the sum over
\(v\) is \(q^{2m-1}\). Hence

\[
\mathcal P_m(q)
=q^{2m-1}
\#\{B\in\operatorname{Alt}_{2m-1}(\mathbf F_q):
\operatorname{rank}B\leq2m-4\}.
\tag{3}
\]

It remains to count the alternating forms of maximal rank \(2m-2\) on a
\((2m-1)\)-dimensional vector space \(V\). Such a form has a unique
one-dimensional radical \(L\). For each line \(L\subset V\), it is the
pullback of a nondegenerate alternating form on \(V/L\). Therefore their
number is

\[
\frac{q^{2m-1}-1}{q-1}
\frac{|\operatorname{GL}_{2m-2}(\mathbf F_q)|}
     {|\operatorname{Sp}_{2m-2}(\mathbf F_q)|}.
\tag{4}
\]

Using the standard orders of the two groups, (4) simplifies to

\[
q^{(m-1)(m-2)}
(q^{2m-1}-1)
\prod_{j=2}^{m-1}(q^{2j-1}-1).
\tag{5}
\]

There are \(q^{(2m-1)(m-1)}\) alternating matrices of size \(2m-1\).
Subtracting (5) from this total in (3), and observing that

\[
2m-1+(m-1)(m-2)=m^2-m+1=F_m,
\]

gives (1). Dividing by the total number \(q^{m(2m-1)}\) gives (2).
\(\square\)

## Non-asymptotic rank-deficiency bound

The normalized character sum is exactly the probability that a uniformly
random alternating matrix of odd size \(2m-1\) fails to have maximal rank:

\[
\frac{\mathcal P_m(q)}{q^{m(2m-1)}}
=\Pr(\operatorname{rank}B\leq2m-4).
\tag{6}
\]

Consequently,

\[
\boxed{
q^{-3}
\leq
\frac{\mathcal P_m(q)}{q^{m(2m-1)}}
\leq
\sum_{j=2}^{m}q^{-(2j-1)}
<
\frac{q^{-3}}{1-q^{-2}}.
}
\tag{7}
\]

Thus Pfaffian has additive Fourier bias of order \(q^{-3}\) as
\(q\to\infty\), uniformly in \(m\). As in the determinant case, this is an
exact statistical statement, not by itself a cryptographic extractor claim.

## Exact adjacent-extension valuation

### Theorem 2

For every prime \(p\), every \(m\geq2\), and every \(r\geq2\),

\[
\boxed{
v_p\!\left(
\mathcal P_m(p^r)-\mathcal P_m(p^{r-1})
\right)
=(m^2-m+1)(r-1).
}
\tag{8}
\]

In particular,

\[
\mathcal P_m(p^r)
\equiv
\mathcal P_m(p^{r-1})
\pmod {p^{(m^2-m+1)(r-1)}},
\tag{9}
\]

and the exponent is sharp.

### Proof

Equation (1) writes

\[
\mathcal P_m(X)=X^{F_m}D_m(X).
\]

The product in (1) has \(m-1\) factors, so its constant term is
\((-1)^{m-1}\). It follows that

\[
D_m(0)=(-1)^m,
\]

a unit modulo every prime. Thus

\[
\begin{aligned}
\mathcal P_m(p^r)-\mathcal P_m(p^{r-1})
&=p^{F_m(r-1)}
\left(p^{F_m}D_m(p^r)-D_m(p^{r-1})\right),
\end{aligned}
\]

and the parenthesized factor is \((-1)^{m+1}\) modulo \(p\). This proves
(8). \(\square\)

## Place in the program

Together with the determinant theorem, this gives a second exact instance of
the two-ended-polynomial principle:

| invariant | real/complex Fourier bias | exact \(p\)-adic exponent |
| --- | ---: | ---: |
| determinant on \(n\)-by-\(n\) matrices | \(q^{-2}\) | \(\frac{n^2-n+2}{2}(r-1)\) |
| Pfaffian on alternating \(2m\)-by-\(2m\) matrices | \(q^{-3}\) | \((m^2-m+1)(r-1)\) |

The Archimedean exponent is controlled by the highest surviving degree of the
counting polynomial. The \(p\)-adic exponent is controlled by its lowest
nonzero degree. This makes relative invariants of finite-field group actions
a systematic source of supercongruence candidates rather than an analogy.

## Literature boundary

The following are direct neighbors:

- [Pairs of quadratic forms over finite fields](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i2p8)
  records explicit alternating-matrix rank counts in arbitrary
  characteristic.
- T. Taniguchi and F. Thorne,
  [Orbital exponential sums for prehomogeneous vector spaces](https://arxiv.org/abs/1607.07827),
  develops exact finite-field Fourier transforms for several relative-
  invariant spaces.
- M. Rudelson and R. Vershynin,
  [Non-asymptotic theory of random matrices: extreme singular values](https://arxiv.org/abs/1003.2990),
  supplies the real/complex non-asymptotic comparison point.

A search for “Pfaffian additive-character sum,” “finite-field Pfaffian
exponential sum,” “Pfaffian Fourier transform,” and the exact displayed
adjacent-\(p^r\) valuation found no matching statement. That is not a proof of
priority.

## Verification

The companion
[`verify_finite_field_pfaffian_bias.py`](../verification/related/verify_finite_field_pfaffian_bias.py)

- enumerates every alternating matrix in five small prime-field cases and
  counts its Pfaffian residue;
- verifies the two equivalent count formulas;
- checks the sharp valuation (8) over a larger exact grid.
