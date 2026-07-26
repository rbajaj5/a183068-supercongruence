# Finite-field determinant bias and an exact supercongruence

## Status

This is a self-contained proved note with an exact finite-field check for small
prime fields and an independent integer-arithmetic check of the resulting
valuation formula.

The finite-field rank count underlying Theorem 1 is classical infrastructure.
A targeted search did not locate the sharp adjacent-extension valuation in
Theorem 2 or the two-ended-polynomial formulation below. Those are therefore
recorded as apparently new formulations, with literature priority still
provisional rather than claimed as settled.

The point is structural. In non-asymptotic random-matrix theory over
\(\mathbb R\) or \(\mathbb C\), one studies proximity to singularity. Over a
finite field there is no ordered singular-value scale; exact rank deficiency
is the corresponding obstruction. Here that obstruction can be counted
exactly. The resulting polynomial has two useful ends:

- its highest-degree terms control ordinary Fourier bias;
- its lowest-degree term controls an exact \(p\)-adic supercongruence.

## The determinant character sum

Let \(q\) be a prime power, let \(\mathbf F_q\) be the field with \(q\)
elements, and let
\(\psi:(\mathbf F_q,+)\longrightarrow \mathbf C^\times\) be any nontrivial
additive character. For \(n\geq2\), define

\[
\mathcal S_n(q):=\sum_{M\in M_n(\mathbf F_q)}\psi(\det M).
\]

Set

\[
E_n:=n+\frac{(n-1)(n-2)}2=\frac{n^2-n+2}{2}.
\]

### Theorem 1

For every prime power \(q\), every \(n\geq2\), and every nontrivial additive
character \(\psi\),

\[
\boxed{\mathcal S_n(q)
=q^{n^2}-q^{E_n}\prod_{k=2}^{n}(q^k-1).}
\tag{1}
\]

Equivalently,

\[
\frac{\mathcal S_n(q)}{q^{n^2}}
=1-\prod_{k=2}^{n}(1-q^{-k}).
\tag{2}
\]

In particular, the answer is independent of the choice of \(\psi\).

### Proof

Condition on the first \(n-1\) rows of \(M\). If those rows are linearly
independent, determinant is a nonzero linear functional of the final row, so
the additive-character sum over that row is zero. If they are dependent,
determinant is zero for every final row, so the conditional sum is \(q^n\).

There are \(q^{n(n-1)}\) total \((n-1)\)-by-\(n\) matrices and

\[
\prod_{j=0}^{n-2}(q^n-q^j)
\]

of them have full row rank. Therefore

\[
\mathcal S_n(q)
=q^n\left(q^{n(n-1)}-\prod_{j=0}^{n-2}(q^n-q^j)\right).
\]

Factoring \(q^j\) from the \(j\)-th factor gives

\[
\prod_{j=0}^{n-2}(q^n-q^j)
=q^{(n-1)(n-2)/2}\prod_{k=2}^{n}(q^k-1),
\]

which proves (1). Dividing by \(q^{n^2}\) proves (2). \(\square\)

## The non-asymptotic bound

The normalized sum is exactly the probability that a uniformly random
\((n-1)\)-by-\(n\) matrix is rank deficient:

\[
\frac{\mathcal S_n(q)}{q^{n^2}}
=\Pr\bigl(\operatorname{rank}R<n-1\bigr).
\tag{3}
\]

Consequently,

\[
\boxed{
q^{-2}\leq\frac{\mathcal S_n(q)}{q^{n^2}}
\leq\sum_{k=2}^{n}q^{-k}
<\frac{q^{-2}}{1-q^{-1}}.}
\tag{4}
\]

Thus determinant has additive Fourier bias of order \(q^{-2}\) as
\(q\to\infty\), uniformly in \(n\). This is a precise finite-field
pseudorandomness statement, but not a claim that determinant is a
cryptographic extractor. For fixed \(q\), the bias does not tend to zero as
\(n\to\infty\).

## The \(p\)-adic theorem

Although (1) came from finite-field counting, its right side is an integer
polynomial in \(q\). Evaluating it at successive powers of one prime produces
an exact supercongruence.

### Theorem 2

Let \(p\) be a prime, \(n\geq2\), and \(r\geq2\). Then

\[
\boxed{
v_p\!\left(\mathcal S_n(p^r)-\mathcal S_n(p^{r-1})\right)
=E_n(r-1).}
\tag{5}
\]

Thus

\[
\mathcal S_n(p^r)\equiv\mathcal S_n(p^{r-1})
\pmod {p^{E_n(r-1)}},
\tag{6}
\]

and this modulus is best possible.

### Proof

Write \(\mathcal S_n(X)=X^{E_n}C_n(X)\). Since
\(\prod_{k=2}^{n}(X^k-1)\) has constant term \((-1)^{n-1}\), equation
(1) gives \(C_n(0)=(-1)^n\), a \(p\)-adic unit. Hence

\[
\mathcal S_n(p^r)-\mathcal S_n(p^{r-1})
=p^{E_n(r-1)}
\left(p^{E_n}C_n(p^r)-C_n(p^{r-1})\right).
\]

The parenthesized expression is congruent to
\(-C_n(0)=(-1)^{n+1}\) modulo \(p\), so it is a unit. This proves (5).
\(\square\)

## The two-ended polynomial principle

The ordinary size of \(\mathcal S_n(q)\) is controlled by cancellation among
the highest-degree terms of (1). Its leading surviving degree is \(n^2-2\),
giving the normalized \(q^{-2}\) bias.

The \(p\)-adic behavior is controlled at the opposite end. The lowest
nonzero degree is \(E_n=(n^2-n+2)/2\), with unit coefficient, giving (5).

This suggests a reusable search method: finite-field moment or character-sum
formulas having both high-degree cancellation and a delayed first nonzero
low-degree coefficient produce, respectively, a non-asymptotic
pseudorandomness bound and an adjacent-extension supercongruence.
Katz-style Frobenius trace formulas are a natural source of richer counting
polynomials to test.

## Relation to the literature

- Rudelson and Vershynin survey extreme singular values over
  \(\mathbb R\) and \(\mathbb C\). Exact finite-field rank deficiency replaces
  proximity to singularity here.
- Katz and Sarnak connect finite-field Frobenius families, character sums,
  and random-matrix symmetry. This theorem is an elementary character-sum
  model of that bridge; it does not use their monodromy machinery.

References:

- M. Rudelson and R. Vershynin,
  [Non-asymptotic theory of random matrices: extreme singular values](https://arxiv.org/abs/1003.2990).
- N. Katz and P. Sarnak,
  [Random Matrices, Frobenius Eigenvalues, and Monodromy](https://doi.org/10.1090/coll/045).
- J. Denef and A. Gyoja,
  [Character sums associated to prehomogeneous vector spaces](https://doi.org/10.1023/A:1000404921277).

The exact Yochay Jerby reference intended for finite-field random matrices
has not yet been identified, so this note makes no attribution on that point.

### Priority-search boundary

Searches by the structural fingerprints
“determinant additive-character sum over matrix space,” “finite-field
determinant exponential sum,” “prehomogeneous determinant Fourier transform,”
and the displayed adjacent-\(p^r\) valuation found the general character-sum
literature above but no exact match for (5). This is evidence for pursuing the
statement, not a proof of novelty.

## Verification

The companion script
[`verify_finite_field_determinant_bias.py`](../verification/related/verify_finite_field_determinant_bias.py)
performs:

1. brute-force determinant-residue counts over small prime fields;
2. exact integer checks of (1) and (5) on a larger parameter grid.
