# The representation and Frobenius packet behind A183068

**Status:** exact reformulations, a complete Hasse--Witt divisibility
calculation, and an archimedean asymptotic consequence. The matrix ranks in
the small-prime table are finite computations, not an all-prime theorem.
Nothing here replaces the elementary proof in [`PROOF.md`](../PROOF.md), and
no new supercongruence exponent is claimed.

This note applies the symmetry-adapted viewpoint used in the companion
[GOE determinant-factor project](https://github.com/rbajaj5/goe-determinant-factor-density)
to the constant-term model of A183068. In that project, multiplicity changes
a scalar orthogonal-polynomial problem into a block-Jacobi problem. Here,
three interior lattice points change a scalar unit-root model into a
three-dimensional Frobenius packet.

## 1. A183068 as a torus-invariant multiplicity

Let

```math
P(w,x,y,z)=
\frac{(1+w)^2}{w}(1+y)^2(1+x)
\left(
 1+\frac{(1+y)^2(1+z)^2}{xy^2z}
\right).
\qquad\text{(1)}
```

The optional structural calculation in [`PROOF.md`](../PROOF.md) gives

```math
a(n)=\mathrm{CT}_{w,x,y,z} P(w,x,y,z)^n.
\qquad\text{(2)}
```

All 99 Laurent coefficients of \(P\) are positive integers. Let

```math
T=({\mathbb C}^{\times})^4
```

and let \({\mathbb C}_{\lambda}\) denote the one-dimensional \(T\)-module of
weight \(\lambda\). If

```math
P=\sum_{\lambda}c_\lambda\,{\bf x}^{\lambda},
```

define

```math
V_P=\bigoplus_{\lambda}
{\mathbb C}_{\lambda}^{\,c_\lambda}.
\qquad\text{(3)}
```

Then \(P\) is exactly the character of \(V_P\). Tensor-product characters
multiply, and the constant term extracts the zero weight. Therefore

```math
\boxed{\quad
a(n)=\dim_{\mathbb C}\left((V_P^{\otimes n})^T\right).
\quad}
\qquad\text{(4)}
```

Thus the proved supercongruence can be restated without analogy:

```math
\dim\left((V_P^{\otimes np^r})^T\right)
\equiv
\dim\left((V_P^{\otimes np^{r-1}})^T\right)
\pmod {p^{2r}}.
\qquad\text{(5)}
```

The generating series \(\sum_{n\ge0}a(n)t^n\) is also the Hilbert series of
the invariant part of the tensor algebra \(T(V_P)^T\).

## 2. The exact weight-walk model

The dimension of \(V_P\) is

```math
D=P(1,1,1,1)=544.
```

Choose a basis vector of \(V_P\) uniformly and record its weight \(X\). In
other words,

```math
{\mathbb P}(X=\lambda)=\frac{c_\lambda}{544}.
```

For independent copies \(X_1,\ldots,X_n\), equation (4) is equivalently

```math
\boxed{\quad
\frac{a(n)}{544^n}
=
{\mathbb P}(X_1+\cdots+X_n=0).
\quad}
\qquad\text{(6)}
```

This is the probabilistic form of the torus-weight decomposition. The exact
drift in coordinates \((w,x,y,z)\) is

```math
{\mathbb E}X=
\left(0,-\frac {15}{34},\frac1{17},0\right),
\qquad\text{(7)}
```

and its covariance matrix is

```math
\Sigma=
\begin{pmatrix}
\frac12&0&0&0\\
0&\frac{353}{1156}&\frac{16}{289}&0\\
0&\frac{16}{289}&\frac{593}{578}&0\\
0&0&0&\frac8{17}
\end{pmatrix}.
\qquad\text{(8)}
```

The nonzero drift and the non-scalar covariance make the anisotropy
explicit. For every real linear functional \(\ell\), Kolmogorov's maximal
inequality gives the genuine archimedean estimate

```math
{\mathbb P}\left(
\max_{1\le k\le n}
\left|\ell\left(\sum_{j=1}^k(X_j-{\mathbb E}X)\right)\right|
\ge t
\right)
\le
\frac{n\,{\rm Var}(\ell(X))}{t^2}.
\qquad\text{(9)}
```

The zero-one law likewise applies to tail events of the infinite independent
weight sequence. These probability theorems control long weight paths; they
do **not** imply a \(p\)-adic congruence. This is the precise boundary of the
probabilistic analogy.

### The archimedean saddle

Put the positive torus variables in logarithmic coordinates. Since the
support spans the full lattice and the origin is interior to its Newton
polytope, \(\log P\) is strictly convex. Its unique zero-drift point is

```math
(w_*,x_*,y_*,z_*)=
\left(1,\,2+\sqrt6,\,\sqrt{\frac23},\,1\right).
\qquad\text{(10)}
```

At this point

```math
P(w_*,x_*,y_*,z_*)=196+80\sqrt6.
\qquad\text{(11)}
```

Indeed, logarithmic differentiation first gives \(w_*=z_*=1\).
The remaining two equations reduce to

```math
x=\frac{2(1+y)}y,
\qquad
y=\frac{x}{1+x}.
```

Their unique positive solution is (10). A second logarithmic
differentiation at that point gives the covariance below:

The covariance of the exponentially tilted zero-drift walk has determinant

```math
\det\Sigma_*=-\frac{88}{3}+12\sqrt6.
\qquad\text{(12)}
```

The support generates \(\mathbb Z^4\), so the lattice local central limit
theorem applies to the tilted walk. Undoing the exponential tilt gives

```math
\boxed{\quad
a(n)\sim
\frac{(196+80\sqrt6)^n}
{4\pi^2 n^2
 \sqrt{-88/3+12\sqrt6}}.
\quad}
\qquad\text{(13)}
```

This asymptotic is an archimedean companion to the \(p\)-adic theorem, not a
proof of it. Its constant simplifies to

```math
\frac{\sqrt3\,(2+\sqrt6)^{3/2}}{16\pi^2},
```

so (13) reproduces the asymptotic recorded by Václav Kotesovec on the
[OEIS A183068 entry](https://oeis.org/A183068). The weight-walk calculation
is a representation-theoretic derivation of that recorded formula, not a
priority claim for the asymptotic itself.

## 3. Frobenius quotients as cyclic tensor orbits

For a prime \(p\), set

```math
{\cal R}_p({\bf x})=
\frac{P({\bf x})^p-P({\bf x}^p)}p.
\qquad\text{(14)}
```

There is a direct representation interpretation. A cyclic group of order
\(p\) rotates the \(p\) tensor positions in a basis word of \(V_P^{\otimes
p}\). Constant words contribute the character \(P({\bf x}^p)\). Every
nonconstant orbit has size \(p\), and rotation preserves its total weight.
Consequently \({\cal R}_p\) is the weight enumerator of nonconstant cyclic
orbits of length \(p\).

In particular,

```math
\mathrm{CT}({\cal R}_p)
```

counts zero-weight nonconstant cyclic orbits. The \(n=1\) case of the proved
A183068 supercongruence says more than integrality:

```math
\mathrm{CT}({\cal R}_p)\equiv0\pmod p.
\qquad\text{(15)}
```

Thus the zero-weight primitive-necklace count carries a second factor of
\(p\) after the first factor used to form the orbit quotient.

## 4. The three-point Hasse--Witt packet

The Newton polytope computation in
[the Frobenius-quotient note](FrobeniusQuotientConstantTerms.md) finds the
three interior lattice points

```math
J=\{(0,0,-1,0),(0,0,0,0),(0,0,1,0)\}.
\qquad\text{(16)}
```

Following Vlasenko, define the \(3\) by \(3\) coefficient matrix

```math
(H_p)_{u,v}
=
[{\bf x}^{\,pv-u}]\,P({\bf x})^{p-1},
\qquad u,v\in J.
\qquad\text{(17)}
```

This is the ordinary Hasse--Witt matrix before reduction modulo \(p\).

Factor

```math
P(w,x,y,z)=C(w)G(x,y,z),
\qquad
C(w)=\frac{(1+w)^2}{w}.
\qquad\text{(18)}
```

Every point of \(J\) has \(w\)-coordinate zero, so coefficient extraction
separates:

```math
H_p(P)=
\mathrm{CT}_w(C(w)^{p-1})\,H_p(G)
=
\binom{2p-2}{p-1}H_p(G).
\qquad\text{(19)}
```

Kummer carry counting gives

```math
v_p\binom{2p-2}{p-1}=1,
\qquad
\frac1p\binom{2p-2}{p-1}\equiv-1\pmod p.
\qquad\text{(20)}
```

We therefore obtain a complete all-prime statement.

### Theorem 1

For every prime \(p\),

```math
H_p(P)\equiv0\pmod p.
\qquad\text{(21)}
```

The divided matrix

```math
\widehat H_p=\frac1pH_p(P)
\qquad\text{(22)}
```

is integral and satisfies

```math
\widehat H_p\equiv-H_p(G)\pmod p.
\qquad\text{(23)}
```

In particular, the usual invertible-Hasse--Witt or ordinary unit-root route
cannot start from this displayed constant-term representation. The relevant
information begins one divided \(p\)-adic layer lower. This explains why the
successful proof uses a valuation budget rather than an ordinary scalar
unit-root argument.

The first exact divided packets are:

| \(p\) | \(\widehat H_p\bmod p\) | rank |
| ---: | --- | ---: |
| \(2\) | \(\left(\begin{smallmatrix}0&0&0\\0&1&1\\0&0&0\end{smallmatrix}\right)\) | 1 |
| \(3\) | \(\left(\begin{smallmatrix}1&1&0\\0&2&2\\0&0&0\end{smallmatrix}\right)\) | 2 |
| \(5\) | \(\left(\begin{smallmatrix}4&0&1\\0&4&4\\0&0&0\end{smallmatrix}\right)\) | 2 |
| \(7\) | \(\left(\begin{smallmatrix}1&4&3\\0&6&6\\0&0&0\end{smallmatrix}\right)\) | 2 |

The rank drop at \(p=2\) is exact in this table. An all-odd-prime rank theorem
would require a separate proof and is not asserted here.

## 5. What Stiefel--Whitney classes do and do not add

The one-variable character in (18) is the character of

```math
W={\bf 1}^{\oplus2}\oplus L\oplus L^{-1}
```

for a torus line \(L\). If \(x=c_1(L)\), the underlying real bundle has

```math
w(W_{\mathbb R})
\equiv
(1+x)(1-x)
\equiv
1+x^2
\pmod2.
\qquad\text{(24)}
```

Thus the first surviving parity class of this factor is the degree-four
class \(w_4=x^2\); the degree-two contributions of \(L\) and \(L^{-1}\)
cancel. This is a useful geometric label for where binary parity lives.
It does not supply the integral valuation in (20), and it does not replace
the separate \(p=2\) argument in the A183068 proof.

The Stiefel--Whitney characteristic class and the Hasse--Witt matrix in
Section 4 are different constructions despite the shared name “Witt.”

## 6. Scalar versus matrix-valued structure

Multiplication by \(P\) is a finite-range transfer operator on the weight
lattice:

```math
a(n)=
\langle\delta_0,M_P^n\delta_0\rangle.
\qquad\text{(25)}
```

The displayed \(P\) is not reciprocal: its support is not centrally
symmetric and its coefficients do not satisfy
\(c_\lambda=c_{-\lambda}\). Hence \(M_P\) is not a self-adjoint scalar
Jacobi operator in the standard counting inner product.

The correct analogue of the GOE block decomposition is therefore:

- torus-character orthogonality instead of scalar radial orthogonality;
- a directed or biorthogonal transfer operator instead of a self-adjoint
  scalar Jacobi matrix; and
- the three-dimensional packet \(J\) instead of a single unit-root
  coordinate.

The common principle is exact: choose a basis adapted to the symmetry, and
the large coefficient problem becomes a small structured block. Here the
block also exposes the forced factor of \(p\) and the exceptional binary
rank drop.

## References

1. M. Vlasenko, *Higher Hasse--Witt matrices*,
   <https://arxiv.org/abs/1605.06440>.
2. A. Mellit and M. Vlasenko,
   *Dwork's congruences for the constant terms of powers of a Laurent
   polynomial*, <https://arxiv.org/abs/1306.5811>.
3. S. Sheffield, *18.175 Lecture 10: Zero-one laws and maximal
   inequalities*,
   <https://math.mit.edu/~sheffield/175/Lecture10.pdf>.
4. OEIS Foundation Inc., [A183068](https://oeis.org/A183068), including
   V. Kotesovec's recorded asymptotic.

The exact coefficient, covariance, reciprocity, and small-prime packet
calculations are reproduced by
[`verify_a183068_representation_packet.py`](../verification/related/verify_a183068_representation_packet.py).
