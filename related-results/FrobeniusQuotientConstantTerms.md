# Frobenius quotients of constant-term sequences

**Status:** elementary theorem, an explicit A183068 corollary, and two exact
Dwork-boundary certificates. No novelty claim is made.

This note isolates the valid algebraic part of a proposed Dwork explanation
for the Cooper level-11 first-order law. It also records exactly what remains
unproved.

## 1. The universal first-order identity

Let

```math
\Lambda\in
\mathbb Z[x_1^{\pm1},\ldots,x_d^{\pm1}]
```

and write

```math
A(n)=\mathrm{CT}\!\left(\Lambda^n\right).
\qquad\text{(1)}
```

For a prime $p$, define the Frobenius quotient

```math
R_p(\mathbf x)=
\frac{\Lambda(\mathbf x)^p-\Lambda(\mathbf x^p)}p.
\qquad\text{(2)}
```

Here $\mathbf x^p=(x_1^p,\ldots,x_d^p)$. The freshman's dream modulo
$p$ shows coefficientwise that

```math
R_p\in
\mathbb Z[x_1^{\pm1},\ldots,x_d^{\pm1}].
\qquad\text{(3)}
```

### Theorem 1

For every $n\ge1$,

```math
A(pn)\equiv
A(n)+pn\mathrm{CT}\!\left(
 \Lambda(\mathbf x^p)^{n-1}R_p(\mathbf x)
\right)
\pmod {p^2}.
\qquad\text{(4)}
```

### Proof

The definition (2) gives the exact identity

```math
\Lambda(\mathbf x)^p=\Lambda(\mathbf x^p)+pR_p(\mathbf x).
```

Raise both sides to the $n$-th power. Every term with at least two copies of
$pR_p$ is divisible coefficientwise by $p^2$, so

```math
\Lambda(\mathbf x)^{pn}
\equiv
\Lambda(\mathbf x^p)^n+
pn\Lambda(\mathbf x^p)^{n-1}R_p(\mathbf x)
\pmod {p^2}.
```

Finally,

```math
\mathrm{CT}\!\left(f(\mathbf x^p)\right)
=\mathrm{CT}(f(\mathbf x)),
```

because multiplication of every exponent by $p$ fixes zero and sends no
nonzero exponent to zero. Taking constant terms proves (4). $\square$

For $n=1$, no truncation is needed:

```math
\frac{A(p)-A(1)}p
=\mathrm{CT}(R_p).
\qquad\text{(5)}
```

Thus the first Frobenius obstruction of any fixed Laurent-polynomial
constant-term sequence has an explicit integral representative.

## 2. The extra condition behind a factorized defect

Equation (4) implies

```math
\frac{A(pn)-A(n)}p
\equiv
n\mathrm{CT}\!\left(
 \Lambda(\mathbf x^p)^{n-1}R_p
\right)
\pmod p.
\qquad\text{(6)}
```

The more special law

```math
\frac{A(pn)-A(n)}p
\equiv
nA(n-1)\mathrm{CT}(R_p)
\pmod p
\qquad\text{(7)}
```

would follow from the rank-one pairing condition

```math
\mathrm{CT}\!\left(
 \Lambda(\mathbf x^p)^m R_p
\right)
\equiv
A(m)\mathrm{CT}(R_p)
\pmod p
\qquad(m\ge0).
\qquad\text{(8)}
```

Condition (8) is sufficient for (7). It is equivalent to the corresponding
instance of (7) only when $p\nmid m+1$; one may not cancel the factor
$n=m+1$ modulo $p$ in general.

If

```math
\psi_p\!\left(\sum_{\mathbf w}c_{\mathbf w}\mathbf x^{\mathbf w}\right)
=
\sum_{\mathbf w}c_{p\mathbf w}\mathbf x^{\mathbf w},
```

then constant-term adjunction rewrites (8) as

```math
\mathrm{CT}\!\left(\Lambda^m\psi_p(R_p)\right)
\equiv
A(m)\mathrm{CT}(R_p)
\pmod p.
\qquad\text{(9)}
```

This makes the missing assertion precise: $\psi_p(R_p)$ must act as a scalar
when paired against every power of $\Lambda$.

## 3. What the standard Dwork theorem does not supply automatically

Samol--van Straten and Mellit--Vlasenko prove D3 congruences for
$A(n)=\mathrm{CT}(\Lambda^n)$ when the Newton polytope of $\Lambda$
has the origin as its unique interior lattice point. Those congruences are a
powerful $p$-adic compatibility statement, but the cited theorem does not
state the rank-one pairing (8).

Consequently, applying that literature to a particular sequence still
requires:

1. an explicit Laurent polynomial for that exact sequence;
2. verification of the Newton-polytope hypothesis for that polynomial; and
3. a proof that D3, or an additional unit-root argument, yields (8).

A reference to the Newton-polytope criterion alone does not close the third
step.

### 3.1 The unique-interior hypothesis does not imply the rank-one pairing

There is a one-variable counterexample. Let

```math
\Lambda(x)=1+2x^{-1}+x.
```

Its Newton polytope is the interval $[-1,1]$, whose unique interior lattice
point is the origin. Thus the standard Dwork theorem applies. At $p=3$,
however,

```math
R_3=
2x^{-3}+4x^{-2}+6x^{-1}+4+3x+x^2.
```

Consequently,

```math
\mathrm{CT}(R_3)=4,
\qquad
\mathrm{CT}\!\left(\Lambda(x^3)R_3\right)=6,
\qquad
A(1)=1.
```

Modulo $3$, the two sides of (8) for $m=1$ are therefore $0$ and $1$.
This proves that the unique-interior Dwork congruences do not, by themselves,
imply the Cooper rank-one condition.

### 3.2 The displayed A183068 polynomial has three interior lattice points

The Laurent polynomial $P$ in [`PROOF.md`](../PROOF.md) also fails the
unique-interior hypothesis. Its Newton polytope is the product of the
$w$-interval $[-1,1]$ with a three-polytope $Q$ in coordinates $(x,y,z)$.
An exact facet description of $Q$ is

```math
\begin{gathered}
-x\le1,\quad -y\le2,\quad -z\le1,\quad z\le1,\quad y\le2,\\
x-z\le1,\quad x+z\le1,\quad 2x-y\le2.
\end{gathered}
```

Enumerating the lattice points satisfying all inequalities strictly gives

```math
(0,-1,0),\qquad(0,0,0),\qquad(0,1,0).
```

Hence the four-dimensional Newton polytope of $P$ has the three interior
lattice points

```math
(0,0,-1,0),\qquad
(0,0,0,0),\qquad
(0,0,1,0)
```

in $(w,x,y,z)$ coordinates. The Samol--van Straten and
Mellit--Vlasenko unique-interior theorem therefore cannot be invoked for this
particular representation. A different Laurent-polynomial representation
might still satisfy their hypothesis, but it would need to be exhibited and
checked.

## 4. Application to the Cooper level-11 target

Once a fixed constant-term model

```math
T(n)=\mathrm{CT}(\Lambda_{11}^n)
```

is specified, (5) gives

```math
q_p\equiv\mathrm{CT}(R_{p,11})\pmod p.
\qquad\text{(10)}
```

The 350-case first-order law recorded in
[the Cooper note](CooperLevel11RarePrimes.md) is therefore equivalent, away
from indices divisible by $p$, to the rank-one pairing (8) for
$\Lambda_{11}$. The public proof target is now exact rather than merely
described as a recurrence linearization.

## 5. An unconditional A183068 corollary

Let $P$ be the fixed Laurent polynomial in the optional structural section of
[`PROOF.md`](../PROOF.md), so that

```math
a(n)=\mathrm{CT}(P^n).
```

Define

```math
\mathcal R_p=
\frac{P(\mathbf x)^p-P(\mathbf x^p)}p.
```

The proved congruence $a(p)\equiv a(1)\pmod {p^2}$ and the exact identity
(5) give:

### Corollary 2

For every prime $p$,

```math
\mathrm{CT}(\mathcal R_p)\equiv0\pmod p.
\qquad\text{(11)}
```

This is a direct reformulation of the $n=1$ case of the A183068 theorem, not
an independent strengthening. Its value is structural: it translates the
elementary carry proof into a statement about the first Frobenius quotient
of a balanced Laurent polynomial.

## References

1. K. Samol and D. van Straten,
   *Dwork congruences and reflexive polytopes*,
   <https://arxiv.org/abs/0911.0797>.
2. A. Mellit and M. Vlasenko,
   *Dwork's congruences for the constant terms of powers of a Laurent
   polynomial*, <https://arxiv.org/abs/1306.5811>.
3. O. Gorodetsky,
   *New representations for all sporadic Apéry-like sequences, with
   applications to congruences*, <https://arxiv.org/abs/2102.11839>.

The exact finite certificates in Sections 3.1 and 3.2 are reproduced by
[`verify_dwork_boundaries.py`](../verification/related/verify_dwork_boundaries.py).
