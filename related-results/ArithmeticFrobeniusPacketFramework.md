# Arithmetic Frobenius packets for the Bala supercongruence census

**Status:** the aggregation lemma, local-to-global lemma, closure calculus, and
arbitrary-depth valuation budget below are complete elementary results.  The
classification covers the repository's reproducible 110-record Bala census.
This framework does **not** claim to prove all 110 conjectures, and priority
for the packaging is provisional.

## 1. The synthesis

The conjectures in the Bala--OEIS census do not share one formula.  They do
share a local shape:

1. choose a number field $K$ containing the coefficients and twists;
2. localize at a prime ideal $\mathfrak p$ above the rational prime $p$;
3. compare adjacent $p$-power levels through a local Frobenius or an
   explicitly proved ramified transition;
4. prove a valuation bound for the resulting defect; and
5. combine the prime-ideal statements when a rational congruence is wanted.

We call the resulting collection of local certificates an **arithmetic
Frobenius packet**.  This is repository vocabulary, not a claim that the
phrase is standard in the literature.

Let $\mathcal O_K$ be the ring of integers of $K$, let $K_{\mathfrak p}$
be the completion, and let $\mathcal O_{\mathfrak p}$ be its valuation
ring.  For every $\mathfrak p\mid p$, a packet records:

- the local field $K_{\mathfrak p}$ and valuation ring
  $\mathcal O_{\mathfrak p}$;
- its normalized valuation $v_{\mathfrak p}$;
- the ramification index $e_{\mathfrak p}$ and residue degree
  $f_{\mathfrak p}$;
- an integral algebra or module $M_{\mathfrak p}$;
- a chosen semilinear transition
  $\Phi_{\mathfrak p}:M_{\mathfrak p}\to M_{\mathfrak p}$; and
- an exponent function $E_{\mathfrak p}(r)$ for which

```math
A_r-\Phi_{\mathfrak p}(A_{r-1})
\in \mathfrak p^{\,E_{\mathfrak p}(r)}M_{\mathfrak p}.
```

At an unramified prime, $\Phi_{\mathfrak p}$ normally lifts the
$p$-power Frobenius of the residue field.  Such a lift is part of the
certificate; it is not silently assumed to exist on every coefficient
algebra.  At a ramified prime, the transition may instead be a separately
proved cross-twist or normalized block map.

This adjacent-level congruence, rather than a particular factorial formula,
is the common
object.

## 2. Local-to-global reconstruction

### Theorem 1: prime-ideal assembly

Let $p$ be a rational prime.  In $\mathcal O_K$, write

```math
p\mathcal O_K
  =\prod_{\mathfrak p\mid p}\mathfrak p^{e_{\mathfrak p}}.
```

If $x,y\in\mathcal O_K$ satisfy

```math
x-y\in\mathfrak p^{\,e_{\mathfrak p}E}
\qquad\text{for every }\mathfrak p\mid p,
```

then

```math
x\equiv y\pmod {p^E\mathcal O_K}.
```

If $x,y\in\mathbb Z$, this implies the ordinary integer congruence
$x\equiv y\pmod {p^E}$.

#### Proof

Distinct prime ideals are coprime, so the factorization above gives

```math
p^E\mathcal O_K
  =\prod_{\mathfrak p\mid p}
     \mathfrak p^{\,e_{\mathfrak p}E}.
```

Membership in every factor is therefore membership in their product.  The
last assertion follows by intersecting $p^E\mathcal O_K$ with
$\mathbb Z$. $\square$

This theorem explains why a split-prime statement needs both local factors.
A one-sided congruence at a selected prime ideal is useful local arithmetic,
but it does not by itself imply a rational congruence modulo $p^E$.

## 3. The aggregation principle

Termwise proofs, block proofs, and constant-term proofs can all be expressed
as fiberwise statements.

### Theorem 2: fiberwise Frobenius aggregation

For $r\ge1$, let a finite index set $I_r$ be the disjoint union of a
discarded set $D_r$ and fibers $L_{r,j}$ indexed by $j\in I_{r-1}$.
Let $F_r:I_r\to M_{\mathfrak p}$, and suppose

```math
\sum_{x\in D_r}F_r(x)
  \equiv0\pmod{\mathfrak p^E}
```

and, for every $j\in I_{r-1}$,

```math
\sum_{x\in L_{r,j}}F_r(x)
  \equiv\Phi_{\mathfrak p}(F_{r-1}(j))
  \pmod{\mathfrak p^E}.
```

If $\Phi_{\mathfrak p}$ is additive, then

```math
\sum_{x\in I_r}F_r(x)
  \equiv
  \Phi_{\mathfrak p}
  \left(\sum_{j\in I_{r-1}}F_{r-1}(j)\right)
  \pmod{\mathfrak p^E}.
```

#### Proof

Sum the fiber congruence over $j$, use the disjoint decomposition of $I_r$,
and then use the discarded-set congruence and additivity of
$\Phi_{\mathfrak p}$. $\square$

The fibers may be singletons.  That recovers the familiar split into
$p\nmid k$ and $k=p\ell$.  Nontrivial fibers allow cancellation that is
invisible term by term, while coefficient extraction and constant-term
operators can be incorporated as additive maps after the aggregate
congruence.

## 4. One valuation budget

The existing Landau-depth theorem uses a cubic transfer law.  The following
version allows an arbitrary transfer depth.

Assume a level-$r$ summand has two estimates:

- **vanishing depth $d$:** a stratum of valuation $s<r$ contributes at
  least $d(r-s)$ powers of the uniformizer;
- **transfer depth $\kappa$ with loss $\varepsilon$:** scaling a
  stratum-$s$ object changes it by at least
  $\kappa(s+1)-\varepsilon$ powers.

For a shallow lifted stratum $0\le s<r-1$, the available budget is

```math
d(r-1-s)+\kappa(s+1)-\varepsilon.
```

The discarded and deep-stratum budgets are respectively

```math
dr
\qquad\text{and}\qquad
\kappa r-\varepsilon.
```

### Theorem 3: arbitrary-depth budget

Put $m=\min(d,\kappa)$ and

```math
\delta(d,\kappa,\varepsilon)=
\begin{cases}
\max(0,d+\varepsilon-\kappa),&d\le\kappa,\\
\varepsilon,&d>\kappa.
\end{cases}
```

The minimum of all these budgets is

```math
mr-\delta(d,\kappa,\varepsilon).
```

Consequently, whenever the fiber hypotheses of Theorem 2 are established at
these termwise precisions, the aggregate tower holds to the displayed
precision.  If that exponent is nonpositive, the assertion is only the
corresponding vacuous ideal containment.

#### Proof

The shallow expression is

```math
dr+(\kappa-d)(s+1)-\varepsilon.
```

If $d\le\kappa$, it is minimized at $s=0$.  Comparing that value with
the discarded budget $dr$ gives
$dr-\max(0,d+\varepsilon-\kappa)$.  The deep budget is no smaller:
this is immediate when $\varepsilon\le\kappa-d$, and otherwise its
difference from the displayed bound is $(\kappa-d)(r-1)$.

If $d>\kappa$, the shallow expression is minimized at $s=r-2$, but the deep
budget is smaller by $d-\kappa$.  It is therefore
$\kappa r-\varepsilon$, as claimed. $\square$

For the Ljunggren--Jacobsthal--Kazandzidis transfer,
$\kappa=3$ and

```math
\varepsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\ge5.
\end{cases}
```

When $d\le3$, the deficit formula becomes exactly

```math
\max(0,d+\varepsilon_p-3)
```

from the repository's
[Landau-depth theorem](LandauDepthSupercongruenceSynthesis.md).  The new
formulation also describes shallower transfer laws and makes the bottleneck
$\min(d,\kappa)$ explicit.

### Boundary compensation

Theorem 3 gives the automatic exponent.  A local bonus can restore a lost
power:

- an extra carry at the first active binary level;
- parity of a repeated multinomial component;
- cancellation across a whole residue fiber;
- multiplicity in a polynomial or Euler-product factor; or
- removal of a local divisor before comparing unit blocks.

Such a bonus must be proved in the relevant local packet.  It is not licensed
by the framework alone.

## 5. Closure calculus

The five census routes interact because Frobenius packets are stable under
basic algebraic operations.

### Theorem 4: packet closure

Let $R$ be an algebra over $\mathcal O_{\mathfrak p}$ and let
$\Phi:R\to R$ be a ring endomorphism.  Suppose

```math
x_r\equiv\Phi(x_{r-1})\pmod{\mathfrak p^E},
\qquad
y_r\equiv\Phi(y_{r-1})\pmod{\mathfrak p^F}.
```

Then:

1. $x_r+y_r$ has precision $\min(E,F)$;
2. $x_ry_r$ has precision $\min(E,F)$;
3. every polynomial in integral $\Phi$-fixed coefficients preserves the
   minimum input precision; and
4. every integral linear map commuting with $\Phi$, including an eligible
   coefficient or constant-term extraction, preserves the input precision.

#### Proof

Addition and commuting linear maps are immediate.  For products, use

```math
x_ry_r-\Phi(x_{r-1}y_{r-1})
=x_r\bigl(y_r-\Phi(y_{r-1})\bigr)
 +\Phi(y_{r-1})
  \bigl(x_r-\Phi(x_{r-1})\bigr).
```

Integrality gives the claimed minimum.  Polynomial closure follows by
addition and multiplication. $\square$

For a Teichmüller root of unity $\zeta$, Frobenius sends
$\zeta$ to $\zeta^p$.  Thus a coefficientwise packet evaluated at
$\zeta$ naturally compares a $\zeta$-twist at level $r$ with a
$\zeta^p$-twist at level $r-1$.  This is the algebraic source of the
split/inert tables.

## 6. Finite-field orbit packets

There is a useful model in which the packet is supplied by orbit
decomposition rather than by a factorial identity.

### Proposition 5: adjacent extension-degree congruence

Let $X$ be a finite-type scheme over $\mathbb F_q$, and put

```math
N_m=\#X(\mathbb F_{q^m}).
```

For every prime $\ell$ and all $n,r\ge1$,

```math
N_{n\ell^r}
\equiv N_{n\ell^{r-1}}
\pmod{\ell^{\,r+v_\ell(n)}}.
```

#### Proof

The points fixed by the $m$-th power of Frobenius are the union of
Frobenius orbits whose lengths divide $m$.  An orbit counted at
$m=n\ell^r$ but not at $n\ell^{r-1}$ has $\ell$-adic orbit-length
valuation exactly $v_\ell(n)+r$.  The difference of the two point counts
is a sum of the sizes of such orbits, proving the displayed congruence.
$\square$

This standard orbit argument is the finite-field baseline behind several
trace and zeta-function packets in the repository.  Stronger exponents
require additional cancellation or geometry; the orbit argument alone
supplies exactly the displayed divisibility.

### 6.1 Support before multiplicity

The orbit law has a useful order-theoretic refinement.  If
\(S\subseteq T\) are Frobenius-stable, locally finite supports, let \(b_d\)
be the number of length-\(d\) Frobenius orbits in \(T\setminus S\).  Their
relative support ghost is

```math
a_n=\#(T\setminus S)^{F^n}=\sum_{d\mid n}d\,b_d.
```

Thus every support inclusion produces a nonnegative Dold sequence and the
ordinary Gauss tower.  A stronger exponent \(h\) is not a formal consequence
of inclusion: it is equivalent to

```math
\ell^{(h-1)r}\mid b_{m\ell^r}
\qquad(\ell\nmid m).
```

The
[crystalline-locus support bridge](CrystallineLocusSupportFrobeniusBridge.md)
applies this distinction to the inclusion classification of Kansal, Levin,
and Savitt.  Their exceptional Barsotti--Tate/Steinberg pair also proves a
sharp limitation: equal semisimple supports give the zero ghost even though
the corresponding stack geometry and inclusion direction differ.  Support,
multiplicity, and stack structure are therefore three distinct layers.

## 7. Gaussian integers as the first complete local model

Take $K=\mathbb Q(i)$.

| Rational prime | Factorization in $\mathbb Z[i]$ | Frobenius behavior | Rational modulus $p^E$ requires |
| --- | --- | --- | --- |
| $p\equiv1\pmod4$ | $(p)=(\pi)(\bar\pi)$ | $i\mapsto i$ at both split completions | $v_\pi,v_{\bar\pi}\ge E$ |
| $p\equiv3\pmod4$ | $(p)$ remains prime | $i\mapsto-i$ in $\mathbb F_{p^2}$ | $v_p\ge E$ |
| $p=2$ | $(2)=-i(1+i)^2$ | ramified; no copied odd-prime rule | $v_{1+i}\ge2E$ |

This table unifies three repository results without pretending they have the
same proof:

- roots-of-unity finite sums use the split/inert Frobenius twist;
- inert rectangular Gaussian products use residue-block cancellation; and
- the ramified rectangular product uses an independent
  $(1+i)$-adic reciprocal-sum expansion.

### Proposition 6: split-prime divisor count

Let $p=\pi\bar\pi$ split, normalize $v_\pi(\pi)=1$, and let
$\iota_m\in\mathbb Z/p^m\mathbb Z$ be the image of $i$ under

```math
\mathbb Z[i]/\pi^m\cong\mathbb Z/p^m\mathbb Z.
```

For $a+ib\ne0$,

```math
v_\pi(a+ib)
=\sum_{m\ge1}
 \mathbf 1_{\,a+\iota_m b\equiv0\;(\mathrm{mod}\;p^m)}.
```

Consequently, for a finite rectangular product, its $\pi$-valuation is the
sum of the numbers of lattice points lying on the displayed lifted null
lines.

#### Proof

The summand for $m$ is one exactly when
$a+ib\in\pi^m$.  Summing these nested divisibility indicators gives the
normalized discrete valuation.  Summing over the rectangle gives the second
statement. $\square$

This proposition explains the obstruction seen in raw split-prime
experiments: before a unit-block congruence is possible, the null-line
divisor must be extracted.  The proposition supplies that divisor exactly;
it does not by itself prove a cubic split-prime product theorem.

## 8. Routing all 110 Bala records

The counts below are inherited from the reproducible
[Gaussian generalization map](BalaGaussianGeneralizationMap.md).

| Route | Count | Packet certificate still needed |
| --- | ---: | --- |
| **T: finite-sum twist** | 40 | Landau/carry vanishing, local scaling, and the Frobenius action on the twist |
| **C: coefficient or constant term** | 37 | A Cartier, Dwork, or Hasse--Witt matrix congruence for a stated Laurent representation |
| **F: factorial or block product** | 14 | Local divisor extraction plus a unit-block transfer theorem |
| **M: modular or partition product** | 14 | Frobenius eigencomponents, often organized by characters or CM |
| **D: derived sequence** | 5 | Packets for the source sequences, followed by Theorem 4 |

Thus

```text
40 + 37 + 14 + 14 + 5 = 110.
```

The table is a decision procedure, not a mass proof:

1. identify the route;
2. specify $K$ and every $\mathfrak p\mid p$;
3. write the actual transition $\Phi_{\mathfrak p}$;
4. certify the valuation budget or Hasse--Witt precision;
5. discharge split and ramified boundary cases; and
6. assemble the desired rational statement with Theorem 1.

Theorem 4 makes the five derived entries the cheapest part of the queue once
their sources are certified.  Route T has the most reusable elementary
engine.  Routes C and M have the strongest connection to algebraic geometry,
but they require an actual constant-term or Frobenius-eigenspace
representation.  Route F is where the Gaussian split-prime null lines and
the ramified prime $1+i$ create genuinely different local problems.

## 9. Literature boundary

The framework is designed to connect, not replace, several established
theories:

- Mellit and Vlasenko prove prime-power Dwork congruences for constant terms
  of powers of Laurent polynomials and obtain $p$-adic analytic
  continuation: [arXiv:1306.5811](https://arxiv.org/abs/1306.5811).
- Vlasenko's higher Hasse--Witt matrices give congruences and unit-root
  Frobenius formulas for multivariate polynomial families:
  [arXiv:1605.06440](https://arxiv.org/abs/1605.06440).
- Varchenko and Zudilin prove Dwork-type congruences for Hasse--Witt matrices
  attached to tuples of Laurent polynomials:
  [arXiv:2108.12679](https://arxiv.org/abs/2108.12679).
- Straub proves two-term congruences modulo $p^{2r}$ for all 15 sporadic
  Apery-like sequences, using special constant-term representations in the
  remaining cases: [arXiv:2301.12248](https://arxiv.org/abs/2301.12248).

These sources justify the Frobenius and constant-term lanes.  They do not
automatically certify an arbitrary OEIS formula, a Gaussian split-prime
normalization, or the ramified $1+i$ case.

## 10. Immediate research program

The framework changes the queue from 110 isolated prompts into four concrete
certificate searches:

1. **Automate route T.**  Compute the Landau fiber depth, record the local
   transfer depth, and use Theorem 3 to predict the automatic exponent.
2. **Recognize route C.**  Search for Laurent-polynomial or diagonal
   representations and test the relevant Hasse--Witt rank.
3. **Factor route F locally.**  At split Gaussian primes, remove the null-line
   divisor from Proposition 6; at $1+i$, work in uniformizer valuation.
4. **Diagonalize route M.**  Separate character or CM eigenspaces before
   asking for a scalar congruence.

A sequence graduates from the framework to a theorem only when its local
certificates and exceptional primes are written out.  That is the main
quality-control gain of the synthesis.

## 11. Verification

Run

```text
python verification/related/verify_arithmetic_frobenius_packet_framework.py
```

The checker:

- exhausts the minimum calculation in Theorem 3 over a broad finite range;
- checks the 110-record census arithmetic;
- tests the closure calculus in exact modular arithmetic;
- checks the finite-field Frobenius-orbit congruence;
- verifies the Gaussian split/inert/ramified identities; and
- checks Proposition 6 for two split primes and thousands of lattice points.

The script is a transcription and regression check.  The proofs are the
arguments above.
