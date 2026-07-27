# Fourier convolution towers for the \(2\times2\times2\) hyperdeterminant

## Status

This note uses finite Fourier inversion to determine the complete
distribution of sums of Cayley hyperdeterminants. It extends the
single-tensor fiber theorem and paired Fourier product in the preceding
note to every convolution power.

The Fourier and Gauss-sum identities are standard. The resulting formulas
for hyperdeterminant convolution fibers, the sharp supercongruence family,
and the explicit mixing estimate are new deductions within this
repository. Literature priority is preliminary.

## 1. The two-point nonzero spectrum

Let \(q\) be odd, let \(\chi\) be the quadratic character of
\(\mathbf F_q^\times\), and let

\[
\psi:(\mathbf F_q,+)\longrightarrow\mathbf C^\times
\]

be nontrivial. For a \(2\times2\times2\) tensor \(T\), write
\(\Delta(T)\) for Cayley's hyperdeterminant and put

\[
\mathcal H_q(a)
=
\sum_T\psi(a\Delta(T))
\qquad(a\in\mathbf F_q).
\tag{1}
\]

The one-tensor fiber calculation gives

\[
\mathcal H_q(0)=q^8
\tag{2}
\]

and, for \(a\neq0\),

\[
\boxed{
\mathcal H_q(a)
=
q^4\left(1+c_q\chi(a)G_q\right),
\qquad
c_q=2(q^2-1),
}
\tag{3}
\]

where

\[
G_q=\sum_{t\neq0}\chi(t)\psi(t),
\qquad
G_q^2=\varepsilon_q q,
\qquad
\varepsilon_q=\chi(-1).
\tag{4}
\]

Thus the nonzero additive Fourier spectrum has only two values. This is the
finite-field analogue of diagonalizing a translation-invariant operator:
convolution becomes multiplication of the coefficients (3).

## 2. Complete convolution fibers

For \(m\geq1\) and \(t\in\mathbf F_q\), define

\[
C_{m,t}(q)
=
\#\left\{
(T_1,\ldots,T_m):
\Delta(T_1)+\cdots+\Delta(T_m)=t
\right\}.
\tag{5}
\]

Put

\[
X_q=4\varepsilon_q q(q^2-1)^2
\tag{6}
\]

and define the even and odd binomial polynomials

\[
A_m(X)
=
\sum_{j\geq0}\binom m{2j}X^j,
\qquad
B_m(X)
=
\sum_{j\geq0}\binom m{2j+1}X^j.
\tag{7}
\]

### Theorem 1 (all additive convolution fibers)

For every odd prime power \(q\) and every \(m\geq1\),

\[
\boxed{
C_{m,0}(q)
=
q^{8m-1}
+(q-1)q^{4m-1}A_m(X_q).
}
\tag{8}
\]

For \(t\neq0\),

\[
\boxed{
\begin{aligned}
C_{m,t}(q)
={}&
q^{8m-1}\\
&+
q^{4m-1}
\left(
-A_m(X_q)
+2\chi(t)q(q^2-1)B_m(X_q)
\right).
\end{aligned}
}
\tag{9}
\]

In particular, every convolution power again has exactly three fiber
classes: zero, nonzero square, and nonsquare.

### Proof

Fourier inversion on the additive group of \(\mathbf F_q\) gives

\[
C_{m,t}(q)
=
\frac1q
\sum_{a\in\mathbf F_q}
\psi(-at)\mathcal H_q(a)^m.
\tag{10}
\]

The term \(a=0\) is \(q^{8m-1}\). If \(t=0\), expand (3). The sum over
\(a\neq0\) kills every odd power of \(\chi(a)\), while each even power sums
to \(q-1\). Since

\[
c_q^{2j}G_q^{2j}=X_q^j,
\]

equation (8) follows.

Now suppose \(t\neq0\). For even powers,

\[
\sum_{a\neq0}\psi(-at)=-1.
\tag{11}
\]

For odd powers,

\[
\sum_{a\neq0}\chi(a)\psi(-at)=\chi(-t)G_q.
\tag{12}
\]

Using \(G_q^2=\varepsilon_q q\) and
\(\chi(-t)\varepsilon_q=\chi(t)\), the odd contribution becomes

\[
2\chi(t)q(q^2-1)B_m(X_q).
\]

This proves (9). \(\square\)

For \(m=1\), equations (8) and (9) recover the original zero,
square, and nonsquare fibers. For \(m=2\), equation (8) is the additive
energy of the hyperdeterminant map.

## 3. An infinite sharp supercongruence family

For \(\sigma\in\{0,1,-1\}\), let \(C_m^\sigma(q)\) denote (8) when
\(\sigma=0\), and (9) with \(\chi(t)=\sigma\) otherwise.

### Theorem 2 (convolution supercongruence)

Let \(p\) be an odd prime, \(m\geq1\), \(r\geq2\), and
\(\sigma\in\{0,1,-1\}\). Then

\[
\boxed{
v_p\left(
C_m^\sigma(p^r)-C_m^\sigma(p^{r-1})
\right)
=(4m-1)(r-1).
}
\tag{13}
\]

Hence

\[
C_m^\sigma(p^r)
\equiv
C_m^\sigma(p^{r-1})
\pmod {p^{(4m-1)(r-1)}},
\tag{14}
\]

and the exponent is sharp.

### Proof

Both (8) and (9) have the form

\[
C_m^\sigma(q)=q^{4m-1}U_{m,\sigma}(q,\varepsilon_q),
\tag{15}
\]

where

\[
U_{m,\sigma}(0,\varepsilon)=-1
\tag{16}
\]

for either value of \(\varepsilon\). Therefore

\[
\begin{aligned}
&C_m^\sigma(p^r)-C_m^\sigma(p^{r-1})\\
&\quad=
p^{(4m-1)(r-1)}
\left(
p^{4m-1}U_{m,\sigma}(p^r,\varepsilon_{p^r})
-U_{m,\sigma}(p^{r-1},\varepsilon_{p^{r-1}})
\right).
\end{aligned}
\]

The parenthesized factor is \(1\) modulo \(p\), proving (13).
\(\square\)

The exponent grows linearly with the number \(m\) of independent tensor
outputs. This is not obtained by simply taking a power of the original
paired product: it comes from the lowest-degree term of the \(m\)-fold
Fourier convolution count.

## 4. Fourier mixing

Let \(\mu_q\) be the probability distribution of \(\Delta(T)\) for a
uniform tensor \(T\). Its nontrivial Fourier coefficients are

\[
\widehat\mu_q(a)
=
\frac{\mathcal H_q(a)}{q^8}
\qquad(a\neq0).
\tag{17}
\]

The distribution of a sum of \(m\) independent outputs is
\(\mu_q^{*m}\), whose Fourier coefficients are
\(\widehat\mu_q(a)^m\).

Put

\[
\rho_q
=
\max_{a\neq0}|\widehat\mu_q(a)|.
\tag{18}
\]

From (3) and \(|G_q|=\sqrt q\),

\[
\rho_q
\leq
q^{-4}
+2q^{-3/2}(1-q^{-2}).
\tag{19}
\]

### Corollary 3 (quantitative approach to uniformity)

If \(U_q\) is the uniform distribution on \(\mathbf F_q\), then

\[
\boxed{
\left\|\mu_q^{*m}-U_q\right\|_{\mathrm{TV}}
\leq
\frac12\sqrt{q-1}\,\rho_q^m.
}
\tag{20}
\]

### Proof

Parseval and Cauchy--Schwarz give

\[
\begin{aligned}
\left\|\mu_q^{*m}-U_q\right\|_{\mathrm{TV}}
&\leq
\frac12
\sqrt{
\sum_{a\neq0}
|\widehat\mu_q(a)|^{2m}
}\\
&\leq
\frac12\sqrt{q-1}\,\rho_q^m.
\end{aligned}
\]

Equation (19) follows directly from (3). \(\square\)

Thus independent addition amplifies the \(q^{-3/2}\) one-sample Fourier
decay exponentially in \(m\). This is a genuine finite-field mixing
statement. It is not, without a separate adversarial analysis, a claim that
the hyperdeterminant is a cryptographic extractor.

## 5. Restriction and Kakeya boundary

The transform in (1) is the one-dimensional Fourier transform of the
pushforward of counting measure by

\[
\Delta:\mathbf F_q^8\longrightarrow\mathbf F_q.
\]

It is not the ambient Fourier transform of a hyperdeterminant level set. For
that, one must study

\[
\widehat{1_{V_s}}(\xi)
=
\sum_{\substack{T\in\mathbf F_q^8\\\Delta(T)=s}}
\psi(\langle \xi,T\rangle),
\qquad
V_s=\{T:\Delta(T)=s\},
\tag{21}
\]

uniformly over nonzero \(\xi\in(\mathbf F_q^8)^\vee\). Bounds for (21),
stratified by the dual tensor orbits, are the honest next input for
finite-field restriction, additive-energy, and Kakeya-type questions. The
exact scalar spectrum above makes that problem unusually structured, but it
does not by itself prove an ambient restriction or Kakeya estimate.

This is the intended harmonic-analysis direction of the project. No
geometric-Langlands interpretation is needed for the results in this note.

## 6. The reusable Fourier compiler

The proof illustrates a general procedure.

1. Compute the nonzero fibers of a relative invariant.
2. Apply multiplicative Fourier analysis to the fiber classes.
3. Use additive Fourier inversion to obtain every convolution power.
4. Read ordinary mixing from the largest nontrivial Fourier coefficient.
5. Read the adjacent-extension supercongruence from the lowest nonzero
   degree of the resulting integer counting polynomial.

For determinant and Pfaffian the scaling character is surjective, so the
nonzero spectrum has one value. For the hyperdeterminant the scaling weight
is a square, so the spectrum has two values and the quadratic Gauss sum is
the extra eigenvalue packet. Higher-index scaling characters should produce
higher multiplicative-character packets.

## 7. Verification and literature boundary

The checker
[`verify_hyperdeterminant_convolution.py`](../verification/related/verify_hyperdeterminant_convolution.py)
verifies:

1. the full cyclic convolution of the exact fibers for \(q=3,5,7\);
2. formulas (8) and (9) for multiple convolution powers;
3. conservation of all \(q^{8m}\) tensor tuples;
4. the sharp valuation (13) on a prime, precision, and convolution grid;
   and
5. the total-variation estimate (20).

Run:

```text
python verification/related/verify_hyperdeterminant_convolution.py
```

Relevant references:

- T. Taniguchi and F. Thorne,
  [Orbital exponential sums for prehomogeneous vector
  spaces](https://arxiv.org/abs/1607.07827), for the surrounding
  relative-invariant Fourier-transform framework.
- [The \(2\times2\times2\) hyperdeterminant: Fourier splitting and a
  supercongruence](HyperdeterminantFourierSupercongruence.md), for the exact
  one-tensor fibers and coefficient (3).

A search for the combination of Cayley hyperdeterminant, additive
convolution fibers, and the displayed adjacent-extension exponent found no
direct match. The general Fourier method is classical; this remains only
preliminary priority evidence for the explicit family.
