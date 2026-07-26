# Supercongruence towers through a p-adic Arzelà--Ascoli lens

**Status:** elementary compactness framework. The vertical convergence
theorems below are complete. For A183068, a Banach-contraction argument proves
that the scale-invariant tower limit cannot extend continuously to all of
$\mathbb Z_p$; a viable compact interpolation target is the unit shell
$\mathbb Z_p^\times$.

Supercongruences compare a sequence at adjacent $p$-power scales. This gives
one direction of regularity automatically. Arzelà--Ascoli becomes relevant
only after that scale control is combined with equicontinuity in the input
variable.

The distinction is:

```text
vertical control:   r changes, x is fixed;
horizontal control: x changes p-adically, r is uniform;
defect compactness: the normalized vertical errors form a precompact family.
```

This note makes those three statements precise.

## 1. Uniform convergence supplied by a supercongruence

Let $K$ be a complete discretely valued field, let $\mathcal O_K$ be its
valuation ring, let $\varpi$ be a uniformizer, and normalize the valuation by
$v(\varpi)=1$. Let $X$ be any set.

### Theorem 1 (vertical tower)

Suppose that $F_r:X\to\mathcal O_K$ and that integers $e_r$ satisfy
$e_r\to\infty$ and

```math
v\!\left(F_{r+1}(x)-F_r(x)\right)\ge e_r
\qquad(x\in X).
\tag{1}
```

Then $(F_r)$ is uniformly Cauchy and converges uniformly to a function
$F:X\to\mathcal O_K$. More precisely,

```math
v\!\left(F(x)-F_r(x)\right)
\ge \inf_{j\ge r}e_j
\qquad(x\in X).
\tag{2}
```

If $(e_r)$ is increasing, the right side of (2) is $e_r$.

### Proof

For $s>r$, the ultrametric inequality gives

```math
v\!\left(F_s(x)-F_r(x)\right)
\ge
\min_{r\le j<s}
v\!\left(F_{j+1}(x)-F_j(x)\right)
\ge
\min_{r\le j<s}e_j.
```

The lower bound is independent of $x$ and tends to infinity with $r$.
Completeness of $\mathcal O_K$ gives the pointwise limit, and the same bound
gives uniform convergence and (2). $\square$

This is stronger than an Arzelà--Ascoli conclusion in the scale direction:
it produces convergence of the full sequence, not merely a convergent
subsequence, and it does not require $X$ to be compact.

## 2. The horizontal hypothesis needed on $\mathbb Z_p$

Now take $X=\mathbb Z_p$. A convenient uniform equicontinuity condition is the
existence of a function $\omega:\mathbb N\to\mathbb N$ with
$\omega(h)\to\infty$ such that

```math
x\equiv y\pmod {p^h}
\quad\Longrightarrow\quad
F_r(x)\equiv F_r(y)\pmod {\varpi^{\omega(h)}}
\qquad\text{for every }r.
\tag{3}
```

### Corollary 2 (continuous interpolation)

Under (1) and (3), the uniform limit $F$ is continuous and obeys the same
modulus (3).

### Proof

Pass to the limit in (3). The subset $\varpi^{\omega(h)}\mathcal O_K$ is
closed, so the congruence is preserved. $\square$

For a sequence initially defined only on nonnegative integers, (3) also lets
each $F_r$ extend uniquely from the dense subset $\mathbb N_0\subset\mathbb
Z_p$ to a continuous function on $\mathbb Z_p$.

This is the first important boundary: a supercongruence in the scale variable
does **not** by itself imply (3). A Lucas congruence, a Dwork congruence, a
Mahler-coefficient estimate, or a direct Kummer-type argument may supply the
missing horizontal modulus, but it must be proved separately.

## 3. Where Arzelà--Ascoli enters: normalized defects

Assume now that $K/\mathbb Q_p$ is finite and that $X$ is a compact metric
space. Then $\mathcal O_K$ is compact. Define the normalized defect

```math
G_r(x)=
\frac{F_{r+1}(x)-F_r(x)}{\varpi^{e_r}}
\in\mathcal O_K.
\tag{4}
```

### Theorem 3 (defect compactness)

If the family $(G_r)$ is equicontinuous, then it has a uniformly convergent
subsequence in $C(X,\mathcal O_K)$.

### Proof

The values lie in the compact space $\mathcal O_K$, and the family is
equicontinuous on compact $X$. The metric Arzelà--Ascoli theorem therefore
makes $(G_r)$ relatively compact in the uniform topology. $\square$

If every convergent subsequence has the same limit $G$, then the full defect
sequence converges uniformly to $G$. In that case,

```math
F_{r+1}(x)-F_r(x)
=
\varpi^{e_r}\bigl(G(x)+o(1)\bigr)
\tag{5}
```

uniformly in $x$. The profile $G$ is a next-order invariant: its zeros are
the inputs where the normalized leading defect vanishes. More concretely, if
$G_r\to G$, then for all sufficiently large $r$ the residue of $G_r(x)$
modulo $\varpi$ equals that of $G(x)$. Thus $G(x)$ is a unit exactly when the
bound $e_r$ is eventually sharp, while $G(x)\equiv0\pmod\varpi$ gives at
least one extra power for all sufficiently large $r$.

The finite-extension hypothesis matters. The closed unit ball of
$\mathbb C_p$ is not compact, so a family with values in $\mathcal O_{\mathbb
C_p}$ needs an additional pointwise relative-compactness hypothesis.

### Theorem 4 (Banach obstruction)

Let $H:\mathbb Z_p\to Y$ be continuous, where $Y$ is Hausdorff. If

```math
H(px)=H(x)\qquad(x\in\mathbb Z_p),
\tag{6}
```

then $H$ is constant.

### Proof

The map $S(x)=px$ is a strict contraction of $\mathbb Z_p$ with unique fixed
point $0$. For every $x$,

```math
H(x)=H(p^j x)\longrightarrow H(0)
```

because $p^j x\to0$. Hence $H(x)=H(0)$. $\square$

Thus Banach's fixed-point geometry supplies an obstruction here: a
nonconstant scale-invariant function cannot be continuous at the attracting
fixed point.

## 4. Application to A183068

For a fixed prime $p$, put

```math
F_r(n)=a(p^r n),
\qquad n\in\mathbb N_0.
```

The proved A183068 congruence gives

```math
v_p\!\left(F_r(n)-F_{r-1}(n)\right)\ge 2r
\qquad(r\ge1),
\tag{7}
```

uniformly in $n$. Theorem 1 therefore gives a uniform limit

```math
A_p(n)=\lim_{r\to\infty}a(p^r n)
\qquad(n\in\mathbb N_0)
\tag{8}
```

and the quantitative tail estimate

```math
v_p\!\left(A_p(n)-a(p^r n)\right)\ge2(r+1).
\tag{9}
```

The limit is scale invariant:

```math
A_p(pn)
=\lim_{r\to\infty}a(p^{r+1}n)
=A_p(n).
\tag{10}
```

It is also nonconstant. We have $A_p(0)=a(0)=1$. If $p\ne5$, then (9) at
$r=0$ gives

```math
A_p(1)\equiv a(1)=26\not\equiv1\pmod p.
```

For $p=5$, exact evaluation gives

```math
a(5)=35\,218\,238\,076,
\qquad
v_5(a(5)-1)=2.
```

The tail after $a(5)$ has valuation at least $4$, so
$v_5(A_5(1)-1)=2$. Thus $A_p(1)\ne A_p(0)$ for every prime $p$.

### Corollary 5 (no global continuous interpolation)

For every prime $p$, the function $A_p:\mathbb N_0\to\mathbb Z_p$ in (8) has
no continuous extension to $\mathbb Z_p$.

### Proof

Any extension would satisfy (10) on the dense subset $\mathbb N_0$ and hence
everywhere by continuity. Theorem 4 would make it constant, contradicting
$A_p(1)\ne A_p(0)$. $\square$

The standard unique-interior Dwork theorem does not remove this obstruction.
It controls the ratios
$a(n)/a(\lfloor n/p\rfloor)$ through cross-multiplied congruences, not the
continuity of $n\mapsto a(n)$. Moreover, the displayed A183068 Laurent
polynomial has three interior lattice points, so it does not satisfy that
theorem's hypothesis. The exact polytope certificate is recorded in
[the Frobenius-quotient note](FrobeniusQuotientConstantTerms.md#32-the-displayed-a183068-polynomial-has-three-interior-lattice-points).

In particular, a horizontal estimate of the form

```math
n\equiv m\pmod {p^h}
\quad\Longrightarrow\quad
a(p^r n)\equiv a(p^r m)\pmod {p^{\omega(h)}}
\quad\text{uniformly in }r,
\qquad \omega(h)\to\infty,
\tag{11}
```

cannot hold on all of $\mathbb N_0$. A viable candidate compact domain is
$\mathbb Z_p^\times$, or more generally a fixed valuation shell
$p^j\mathbb Z_p^\times$. The scale-invariant limit is determined by its
values on the unit shell, and the contraction orbit no longer accumulates
inside that shell.

The first normalized defects are

```math
D_r(n)=
\frac{a(p^r n)-a(p^{r-1}n)}{p^{2r}}
\qquad(r\ge1).
\tag{12}
```

They are integral by the theorem. Proving a common horizontal modulus for
the $D_r$ on $\mathbb Z_p^\times$ would place them under Theorem 3 and
produce subsequential next-order profiles. They also obey the exact
renormalization relation

```math
D_r(pn)=p^2D_{r+1}(n).
\tag{13}
```

Consequently, if the defects converge to a continuous profile $D$, then
$D(pn)=p^2D(n)$. Unlike scale invariance, this positive-weight homogeneity is
compatible with continuity at the attracting fixed point and forces
$D(0)=0$.

Iterating (13) gives more without assuming convergence:

```math
D_r(p^h n)=p^{2h}D_{r+h}(n).
\tag{14}
```

### Corollary 6 (uniform contraction of the defects at zero)

For every $r\ge1$ and positive integer $n$,

```math
v_p(D_r(n))\ge2v_p(n),
\tag{15}
```

Moreover, $D_r(0)=0$. In particular, the family $(D_r)$ is uniformly
equicontinuous at $0$: if $n\equiv0\pmod {p^h}$, then
$D_r(n)\equiv0\pmod {p^{2h}}$ for every $r$.

### Proof

Write $n=p^h u$ and apply (14). The term $D_{r+h}(u)$ is integral by the
A183068 supercongruence. $\square$

## 5. Relation to the other results in this repository

### Landau-depth families

The same argument applies whenever the synthesis theorem gives a uniform
bound

```math
v_p\!\left(A(p^r n)-A(p^{r-1}n)\right)\ge dr-c_p(d).
```

It produces the vertical limit immediately. The Landau step function controls
the rate in $r$; it does not automatically control the $p$-adic modulus in
$n$.

### Cooper's level-11 sequence

The experimentally observed quantity

```math
D_p(n)=\frac{T(pn)-T(n)}p\pmod p
```

is a first normalized defect. The proposed law

```math
D_p(n)=nT(n-1)q_p
```

says that this defect lies in a one-dimensional family with coordinate
$q_p$. In compactness language, it is much stronger than precompactness: it
identifies the entire first defect profile. The different behavior seen at
the second scale warns that the next profile need not be a scalar iteration
of the first.

### Frobenius quotients

For constant-term sequences, the identity in
[Frobenius quotients of constant-term sequences](FrobeniusQuotientConstantTerms.md)
gives an explicit algebraic formula for the first defect. Arzelà--Ascoli
does not replace that formula; it supplies a route for taking limits of such
formulas once their horizontal dependence is controlled.

## 6. A concrete research protocol

For a new supercongruence family:

1. identify the renormalization law and check its attracting fixed points;
2. choose a compatible compact domain, such as $\mathbb Z_p^\times$ for a
   nonconstant scale-invariant limit;
3. define the scale functions $F_r$ and prove the vertical bound (1);
4. find a uniform horizontal modulus on the chosen domain;
5. normalize the defects as in (4);
6. prove equicontinuity of the normalized defects;
7. extract a limiting defect profile; and
8. use Frobenius, recurrence, or transfer identities to prove that the
   profile is unique and identify it.

Vertical convergence and horizontal continuity are independent mathematical
obligations. The fixed-point check prevents an impossible interpolation
problem from entering the queue. The later steps expose the next congruence
rather than merely rephrasing the original one.

## 7. What this framework does and does not claim

The framework gives:

- a uniform $p$-adic limit along every proved supercongruence tower;
- a fixed-point obstruction to impossible global interpolations;
- the unit shell as a viable candidate target for A183068 interpolation;
- a uniform quadratic contraction law for all normalized A183068 defects at
  the attracting fixed point; and
- a compactness mechanism for discovering next-order defect profiles.

It does not by itself give:

- a stronger exponent;
- the horizontal estimate on $\mathbb Z_p^\times$;
- uniqueness of a defect limit; or
- a cryptographic security property.

In particular, compactness and Lipschitz control can yield stable finite
approximations, but stability is not pseudorandomness.
