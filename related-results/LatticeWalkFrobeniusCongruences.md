# Frobenius congruences for finite lattice-walk transfer matrices

## 1. Scope

There is a rigorous arithmetic bridge from lattice walks to congruences, but
it passes through **finite transfer matrices**, not through a claimed
self-avoiding-walk scaling limit.

- The square lattice is naturally modeled over the Gaussian integers
  $\mathbb Z[i]$.
- The triangular lattice, and the three directions underlying the honeycomb
  lattice, are naturally modeled over the Eisenstein integers
  $\mathbb Z[\omega]$, where $\omega^2+\omega+1=0$.
- A fixed-width transfer calculation has finitely many boundary states.
  Its weighted periodic counts are traces of powers of a finite matrix.
- Those trace sequences satisfy a Frobenius-twisted adjacent-scale
  congruence.

The unramified part is an application of the standard Gauss-congruence
formalism over number fields. The ramified statement below is included with
a self-contained proof because the usual number-field definition excludes
ramified primes.

This is an order-$r$ Gauss congruence, not a new order-$2r$
supercongruence. It belongs in this repository because it identifies a clean
transfer-matrix source of adjacent-scale congruences and gives an exact local
table at Gaussian and Eisenstein primes.

## 2. The local trace theorem

Let $R$ be the ring of integers of a number field, let
$\mathfrak p$ lie over the rational prime $p$, and work in the discrete
valuation ring $R_{\mathfrak p}$. Write $v_{\mathfrak p}$ for its
valuation. Suppose that a ring automorphism $\sigma$ satisfies

$$
  \sigma(x)\equiv x^p \pmod{\mathfrak p}
  \qquad(x\in R).
  \tag{1}
$$

This is the usual Frobenius automorphism when $\mathfrak p$ is unramified.
At a ramified prime, (1) is the only hypothesis needed below.

### Theorem 1 — uniformizer Gauss congruence

For every matrix $M\in\mathrm{Mat}_d(R)$, every $n,r\geq1$, and

$$
  a_N=\mathrm{tr}(M^N),
$$

one has

$$
  a_{np^r}\equiv
  \sigma\!\left(a_{np^{r-1}}\right)
  \pmod{\mathfrak p^r}.
  \tag{2}
$$

When $\mathfrak p$ is unramified, $p$ is a local uniformizer and (2) is
the familiar modulus $p^r$. At a ramified prime it is deliberately stated
in powers of the prime ideal, not powers of the rational prime.

### Proof

Set

$$
  F(t)=\det(I-tM)^{-1}\in 1+tR[[t]].
$$

Every such series has a unique Euler product

$$
  F(t)=\prod_{d\geq1}(1-x_dt^d)^{-1},
  \qquad x_d\in R.
  \tag{3}
$$

Taking logarithmic derivatives of the determinant and of (3) gives the
ghost-component identity

$$
  a_N=\sum_{d\mid N}d\,x_d^{N/d}.
  \tag{4}
$$

Write $n=p^v m$ with $p\nmid m$. The argument below, applied with total
level $r+v$, gives a congruence modulo $\mathfrak p^{r+v}$, which is
stronger than required. We may therefore assume $p\nmid n$. Write every
divisor of $np^r$ uniquely as $d_0p^j$, where $d_0\mid n$ and
$0\leq j\leq r$. Pair the terms
with $j<r$ in (4) with the corresponding terms in
$\sigma(a_{np^{r-1}})$. Their difference is

$$
 d_0p^j\left(
 x_{d_0p^j}^{(n/d_0)p^{r-j}} -
 \sigma(x_{d_0p^j})^{(n/d_0)p^{r-1-j}}
 \right).
\tag{5}
$$

We use the elementary lifting fact

$$
 u\equiv v\pmod{\mathfrak p^s}
 \quad\Longrightarrow\quad
 u^p\equiv v^p\pmod{\mathfrak p^{s+1}}
 \qquad(s\geq1).
 \tag{6}
$$

Indeed, expand $(v+(u-v))^p$. The middle binomial coefficients are
divisible by $p\in\mathfrak p$, and the final term has valuation at least
$p s\geq s+1$.

By (1), the parenthesized expression in (5) has
$\mathfrak p$-valuation at least $r-j$: first apply (1), raise to the
power $n/d_0$, and then apply (6) $r-j-1$ times. Since
$p^j\in\mathfrak p^j$, every term in (5) lies in
$\mathfrak p^r$. The unpaired $j=r$ terms contain $p^r$ and therefore
also lie in $\mathfrak p^r$. Summing proves (2). $\square$

## 3. Gaussian and Eisenstein local tables

Complex conjugation is denoted by a bar.

### Corollary 2 — Gaussian table

For $M\in\mathrm{Mat}_d(\mathbb Z[i])$:

$$
\begin{array}{c|c|c}
\text{rational prime} & \text{Frobenius action} & \text{congruence}\\
\hline
p\equiv1\pmod4 & z\mapsto z &
 a_{np^r}\equiv a_{np^{r-1}}\pmod{p^r}\\
p\equiv3\pmod4 & z\mapsto\bar z &
 a_{np^r}\equiv\overline{a_{np^{r-1}}}\pmod{p^r}\\
p=2 & z\mapsto z\ \text{or}\ z\mapsto\bar z &
 a_{n2^r}\equiv
 a_{n2^{r-1}}\equiv\overline{a_{n2^{r-1}}}
 \pmod{(1+i)^r}.
\end{array}
\tag{7}
$$

For $p\equiv1\pmod4$, apply Theorem 1 at both primes above $p$ and
intersect the two ideal congruences. For $p\equiv3\pmod4$, $p$ is inert
and conjugation is the residue-field Frobenius. At $p=2$, both identity and
conjugation satisfy (1) modulo $1+i$, so Theorem 1 applies to either lift.

### Corollary 3 — Eisenstein table

For $M\in\mathrm{Mat}_d(\mathbb Z[\omega])$:

$$
\begin{array}{c|c|c}
\text{rational prime} & \text{Frobenius action} & \text{congruence}\\
\hline
p\equiv1\pmod3 & z\mapsto z &
 a_{np^r}\equiv a_{np^{r-1}}\pmod{p^r}\\
p\equiv2\pmod3 & z\mapsto\bar z &
 a_{np^r}\equiv\overline{a_{np^{r-1}}}\pmod{p^r}\\
p=3 & z\mapsto z\ \text{or}\ z\mapsto\bar z &
 a_{n3^r}\equiv
 a_{n3^{r-1}}\equiv\overline{a_{n3^{r-1}}}
 \pmod{(1-\omega)^r}.
\end{array}
\tag{8}
$$

Thus the correct hexagonal analogue of the Gaussian split/inert table is
Eisenstein, with the ramified boundary moving from $1+i$ to
$1-\omega$.

## 4. Walk interpretation

Let $G$ be a finite directed multigraph and give each edge a weight in
$R$. If $M$ is its weighted adjacency matrix, then

$$
  \mathrm{tr}(M^N)
$$

is the total weight of all length-$N$ closed walks with a marked initial
vertex. Theorem 1 therefore gives a Frobenius congruence for every such
weighted closed-walk model.

More generally, fix a strip width and let the states record all connectivity
data along a transfer boundary. Any transfer-matrix enumeration whose
periodic length-$N$ partition function is

$$
  Z_N=\mathrm{tr}(T^N)
$$

inherits (2). This includes finite-state hard-core and self-avoidance
models once the boundary connectivity state is part of the state space.
The theorem is coefficient-ring agnostic: Gaussian direction weights are
natural on square-lattice models, while Eisenstein direction weights are
natural for triangular or honeycomb geometry.

This is a genuine but finite-width statement. The ordinary number of
$N$-step self-avoiding walks on the full infinite lattice is not, in
general, the trace of powers of one fixed finite matrix: remembering all
visited vertices requires unbounded state.

## 5. Why SLE is context, not a proof step

Duminil-Copin and Smirnov proved that the honeycomb-lattice connective
constant is

$$
  \sqrt{2+\sqrt2}.
$$

Their parafermionic observable uses complex turning weights and a local
discrete contour identity. That makes the Eisenstein/cyclotomic coefficient
language natural, but it does not produce a $p$-adic divisibility theorem.

The proposed convergence of planar self-avoiding walk to
$\mathrm{SLE}_{8/3}$ remains conjectural. Even if that scaling limit were
proved, it would describe large-scale probability and conformal geometry,
whereas (2) is an exact finite-level divisibility statement. A bridge
between them would require an additional theorem showing that a compatible
arithmetic transfer structure survives the growing-width limit.

The safe dependency diagram is therefore

$$
\begin{array}{c}
\text{finite boundary-state model}\\
\Downarrow\\
\text{finite transfer matrix}\\
\Downarrow\\
\text{Frobenius-twisted Gauss congruence}
\end{array}
\qquad
\text{not}
\qquad
\mathrm{SLE}_{8/3}\Longrightarrow\text{supercongruence}.
$$

## 6. Verification and status

The exact checker
[`verify_lattice_walk_frobenius.py`](../verification/related/verify_lattice_walk_frobenius.py)
implements arithmetic in $\mathbb Z[i]$ and $\mathbb Z[\omega]$, checks
the split, inert, and ramified rows of (7)--(8), checks both ramified
Frobenius lifts, and compares a weighted closed-walk enumeration with the
corresponding matrix trace.

Status:

- Theorem 1 and its two local tables: complete elementary proof.
- Finite transfer-matrix corollary: complete formal consequence.
- Application to the unrestricted planar SAW or to SLE: **not claimed**.
- Literature priority: the unramified theorem is standard
  Gauss-congruence infrastructure; no novelty claim is made for it. The
  ramified uniformizer formulation is recorded as a self-contained
  extension, with priority not established.

## References

- É. Delaygue and T. Rivoal,
  [*Abel's problem, Gauss and Cartier congruences over number fields*](https://arxiv.org/abs/2501.16281).
  Definition 1 gives the Frobenius-twisted number-field Gauss congruence at
  unramified primes.
- G. T. Minton,
  [*Linear recurrence sequences satisfying congruence conditions*](https://doi.org/10.1090/S0002-9939-2014-12168-X),
  *Proc. Amer. Math. Soc.* **142** (2014), 2337--2352.
- N. Clisby and I. Jensen,
  [*A new transfer-matrix algorithm for exact enumerations:
  self-avoiding polygons on the square lattice*](https://arxiv.org/abs/1111.5877).
- H. Duminil-Copin and S. Smirnov,
  [*The connective constant of the honeycomb lattice equals
  $\sqrt{2+\sqrt2}$*](https://arxiv.org/abs/1007.0575).
- G. F. Lawler, O. Schramm, and W. Werner,
  [*On the scaling limit of planar self-avoiding walk*](https://arxiv.org/abs/math/0204277).
