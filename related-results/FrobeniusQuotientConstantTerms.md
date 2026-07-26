# Frobenius quotients of constant-term sequences

**Status:** elementary theorem and an explicit A183068 corollary. No novelty
claim is made.

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
