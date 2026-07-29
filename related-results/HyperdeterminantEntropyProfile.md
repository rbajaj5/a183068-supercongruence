# Entropy profile of finite-field hyperdeterminant values

## Status

This note extracts exact information-theoretic consequences from the
hyperdeterminant fiber counts and additive Fourier coefficient proved in
[the companion Fourier note](HyperdeterminantFourierSupercongruence.md).
It gives the complete Rényi profile, an arithmetic sufficient statistic for
all Rényi divergences from uniformity, an asymptotically sharp
relative-entropy/total-variation comparison, and an exact collision-entropy
law for additive convolution powers.

The entropy identities are elementary consequences of the exact fibers,
Parseval, and standard properties of Rényi divergence. They are recorded as
reusable structure, not as independent literature-priority claims.

All logarithms are natural. Divide by \(\log 2\) to express the entropies in
bits.

## 1. The three-level value law

Let \(q\) be an odd prime power, let \(T\) be uniform on
\(M_2(\mathbf F_q)^2\), and put

\[
X_q:=\Delta(T)\in\mathbf F_q.
\]

Write \(P_q\) for the law of \(X_q\). The exact fibers give

\[
p_0:=P_q(0)=\frac{q^4+q-1}{q^5},
\tag{1}
\]

and, for \(u\ne0\),

\[
P_q(u)=
\begin{cases}
p_+:=\dfrac{(q-1)(q+1)^3}{q^5},&\chi(u)=1,\\[2mm]
p_-:=\dfrac{(q-1)^3(q+1)}{q^5},&\chi(u)=-1.
\end{cases}
\tag{2}
\]

There are \((q-1)/2\) values of each nonzero type, and

\[
p_+>p_0>p_-.
\tag{3}
\]

Thus \(P_q\) has full support but only three distinct probability levels.

## 2. Arithmetic localization of every Rényi divergence

Let

\[
C_q\in\{0,+,-\}
\]

record whether \(X_q\) is zero, a nonzero square, or a nonsquare. Its law is

\[
\overline P_q=
\left(
p_0,\,
\frac{q-1}{2}p_+,\,
\frac{q-1}{2}p_-
\right).
\tag{4}
\]

If \(U_q\) is uniform on \(\mathbf F_q\), the corresponding class law is

\[
\overline U_q=
\left(
\frac1q,\,
\frac{q-1}{2q},\,
\frac{q-1}{2q}
\right).
\tag{5}
\]

### Theorem 1 (the quadratic-character class is sufficient)

For every Rényi order \(0<\alpha\leq\infty\), including the
Kullback--Leibler limit \(\alpha=1\),

\[
\boxed{
D_\alpha(P_q\Vert U_q)
=
D_\alpha(\overline P_q\Vert\overline U_q).
}
\tag{6}
\]

### Proof

The likelihood ratio \(P_q(u)/U_q(u)=qP_q(u)\) is constant on each of the
three classes. For \(0<\alpha<\infty\), \(\alpha\ne1\), the contribution of
a class of size \(n\), with point mass \(p\), to the Rényi sum is

\[
n p^\alpha (1/q)^{1-\alpha}
=(np)^\alpha(n/q)^{1-\alpha}.
\]

This is exactly the contribution of the collapsed class. The limits
\(\alpha=1,\infty\) follow from the same constant-likelihood-ratio
observation. \(\square\)

Consequently, no divergence from uniformity is hidden inside either
quadratic-character class. All of it lives on the three-point arithmetic
quotient.

The Shannon chain rule gives the complementary identity

\[
\boxed{
H(P_q)
=H(\overline P_q)
+(1-p_0)\log\frac{q-1}{2}.
}
\tag{7}
\]

This is the entropy version of the Gauss-packet splitting in the Fourier
note.

## 3. The complete Rényi profile

For \(0<\alpha<\infty\), \(\alpha\ne1\),

\[
\boxed{
H_\alpha(P_q)
=
\frac{1}{1-\alpha}
\log\left(
p_0^\alpha
+\frac{q-1}{2}\bigl(p_+^\alpha+p_-^\alpha\bigr)
\right).
}
\tag{8}
\]

The limiting cases are

\[
H_0(P_q)=\log q,
\tag{9}
\]

\[
H(P_q)
=-p_0\log p_0
-\frac{q-1}{2}
\left(p_+\log p_+ +p_-\log p_-\right),
\tag{10}
\]

and, by (3),

\[
\boxed{
H_\infty(P_q)
=-\log p_+
=
\log\frac{q^5}{(q-1)(q+1)^3}.
}
\tag{11}
\]

Since the reference measure is uniform,

\[
D_\alpha(P_q\Vert U_q)=\log q-H_\alpha(P_q).
\tag{12}
\]

Thus (8) gives every Rényi divergence as well as every Rényi entropy.

## 4. Collision entropy and Fourier energy

The order-two collision probability has the closed form

\[
\boxed{
\operatorname{Col}(P_q)
:=\sum_{u\in\mathbf F_q}P_q(u)^2
=
\frac1q
\left[
1+\frac{q-1}{q^8}
\left(1+4q(q^2-1)^2\right)
\right].
}
\tag{13}
\]

Equivalently,

\[
\boxed{
\chi^2(P_q\Vert U_q)
=q\operatorname{Col}(P_q)-1
=
\frac{q-1}{q^8}
\left(1+4q(q^2-1)^2\right).
}
\tag{14}
\]

Therefore

\[
H_2(P_q)=-\log\operatorname{Col}(P_q),
\qquad
D_2(P_q\Vert U_q)
=\log\left(1+\chi^2(P_q\Vert U_q)\right).
\tag{15}
\]

### Fourier proof

For a fixed nontrivial additive character \(\psi\), put

\[
\phi_q(a):=\mathbf E\,\psi(aX_q).
\]

The Fourier formula from the companion note gives, for \(a\ne0\),

\[
\phi_q(a)
=q^{-4}\left(1+2(q^2-1)\chi(a)G_q(\chi,\psi)\right).
\tag{16}
\]

Parseval on \((\mathbf F_q,+)\) says

\[
\operatorname{Col}(P_q)
=\frac1q\sum_{a\in\mathbf F_q}|\phi_q(a)|^2.
\tag{17}
\]

The cross term cancels after summing \(\chi(a)\) over
\(\mathbf F_q^\times\), while
\(\lvert G_q(\chi,\psi)\rvert^2=q\). Substitution gives (13).

## 5. Shannon deficit, Pinsker, and sharp scale

The relative entropy from uniformity is exactly

\[
\boxed{
D(P_q\Vert U_q)
=
p_0\log(qp_0)
+\frac{q-1}{2}
\left[
p_+\log(qp_+)+p_-\log(qp_-)
\right].
}
\tag{18}
\]

As \(q\to\infty\) through odd prime powers,

\[
D(P_q\Vert U_q)
=
\frac{2}{q^2}
-\frac{2}{q^3}
+O(q^{-4}),
\tag{19}
\]

so

\[
H(P_q)
=
\log q-\frac{2}{q^2}
+\frac{2}{q^3}
+O(q^{-4}).
\tag{20}
\]

The total-variation distance is also exact:

\[
\boxed{
\lVert P_q-U_q\rVert_{\mathrm{TV}}
=
\frac{(q-1)(2q^3-2q+1)}{2q^5}
}
\tag{21}
\]

and hence

\[
\lVert P_q-U_q\rVert_{\mathrm{TV}}
=
\frac1q-\frac1{q^2}-\frac1{q^3}
+O(q^{-4}).
\tag{22}
\]

Pinsker's inequality gives

\[
\lVert P_q-U_q\rVert_{\mathrm{TV}}
\leq
\sqrt{\frac12D(P_q\Vert U_q)}.
\tag{23}
\]

Equations (19) and (22) show that the two sides of (23) are both
\(q^{-1}(1+o(1))\). Pinsker is therefore asymptotically sharp, including its
leading constant, for this arithmetic family.

The other two principal entropy deficits occur on different scales:

\[
\log q-H_2(P_q)
=\frac4{q^2}-\frac4{q^3}+O(q^{-4}),
\tag{24}
\]

\[
\log q-H_\infty(P_q)
=\frac2q-\frac2{q^2}+O(q^{-3}).
\tag{25}
\]

The min-entropy sees the largest individual square fiber at order \(q^{-1}\);
Shannon and collision entropy average that exceptional fiber across the
whole field and first deviate at order \(q^{-2}\).

## 6. Exact entropy growth under additive convolution

Let \(X_q^{(1)},\ldots,X_q^{(m)}\) be independent copies of \(X_q\), and put

\[
S_{q,m}:=X_q^{(1)}+\cdots+X_q^{(m)}.
\]

Write

\[
c_q:=2(q^2-1),
\qquad
\varepsilon(q):=\chi(-1),
\]

and define

\[
A_m(q,\varepsilon)=
\begin{cases}
(1+c_q^2q)^m,&\varepsilon=-1,\\[2mm]
\displaystyle
\sum_{j=0}^{m}\binom{2m}{2j}c_q^{2j}q^j,
&\varepsilon=1.
\end{cases}
\tag{26}
\]

### Theorem 2 (convolution collision law)

For every \(m\geq1\),

\[
\boxed{
\operatorname{Col}(S_{q,m})
=
\frac1q\left(
1+\frac{q-1}{q^{8m}}A_m(q,\varepsilon(q))
\right).
}
\tag{27}
\]

Consequently,

\[
H_2(S_{q,m})
=-\log\operatorname{Col}(S_{q,m}),
\tag{28}
\]

\[
H(S_{q,m})\geq H_2(S_{q,m}),
\tag{29}
\]

and Fourier inversion with Cauchy--Schwarz gives

\[
\boxed{
\lVert\mathcal L(S_{q,m})-U_q\rVert_{\mathrm{TV}}
\leq
\frac12
\sqrt{\frac{q-1}{q^{8m}}A_m(q,\varepsilon(q))}.
}
\tag{30}
\]

### Proof

The Fourier coefficient of the \(m\)-fold convolution is
\(\phi_q(a)^m\). Thus

\[
q\operatorname{Col}(S_{q,m})-1
=
\sum_{a\ne0}|\phi_q(a)|^{2m}.
\tag{31}
\]

If \(\varepsilon(q)=-1\), the Gauss sum is purely imaginary and

\[
|1\pm c_qG_q|^2=1+c_q^2q.
\]

If \(\varepsilon(q)=1\), the two quadratic classes contribute
\((1+c_q\sqrt q)^{2m}\) and \((1-c_q\sqrt q)^{2m}\). Their average is the
even-binomial sum in (26). There are \((q-1)/2\) frequencies in each class.
Substitution in (31) proves (27). Equations (28) and (29) are the definition
of collision entropy and monotonicity of Rényi entropy. Equation (30) is the
standard Parseval--Cauchy bound. \(\square\)

This supplies an exact entropy trajectory, not only a one-step
equidistribution estimate.

## 7. Relation to the hypercube hashing estimates

The binary affine/matroid hashing laws concern sparse Walsh supports in
\(\mathbf F_2^n\). The present law lives on the odd-characteristic output
group \((\mathbf F_q,+)\), and the hyperdeterminant phase appears to have a
dense transform on its eight tensor coordinates. Direct sparse-support
hashing therefore does not strengthen the adjacent-extension exponent.

The useful transfer is instead:

1. replace support size by Fourier energy;
2. use Parseval to obtain collision and Rényi-2 entropy exactly;
3. collapse the scaling-character classes to an arithmetic sufficient
   statistic; and
4. use relative entropy or Rényi divergence to compare the arithmetic law
   with uniform measure.

This suggests a broader entropy program for relative invariants: when a
scaling character has finite-index image and the fibers are uniform inside
its multiplicative classes, the cokernel class is a sufficient statistic for
the entire divergence profile.

## 8. Relation to Jerby's entropy argument

Section 7.4 of Yochay Jerby's
[work on variations of the Hardy \(Z\)-function](https://arxiv.org/abs/2511.18275)
uses relative entropy under a Girsanov change of measure and Pinsker's
inequality to show that removing an error drift does not alter bounded local
statistics in the limit.

Only the measure-comparison principle is used here: quantify a perturbation
by relative entropy, then convert that control to variation distance. The
zeta-zero ensemble, stochastic dynamics, and pair-correlation claims in that
paper are not inputs to any theorem in this note.

## Verification

The companion
[`verify_hyperdeterminant_entropy.py`](../verification/related/verify_hyperdeterminant_entropy.py)

- checks the exact Rényi-2 and chi-squared formulas over odd prime powers;
- checks arithmetic-class sufficiency numerically for several Rényi orders;
- verifies the exact total-variation formula and Pinsker inequality;
- verifies Rényi monotonicity and the min-entropy extremizer; and
- compares (27) against exact cyclic convolutions for \(q=3,5,7\) and
  \(1\leq m\leq4\).
