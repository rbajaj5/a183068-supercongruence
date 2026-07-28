# Controller-filtered periodic-orbit supercongruences

## Status

This note gives a reusable compiler from finite-state controller models to
prime-power congruences.  The arithmetic is the classical Dold, or necklace,
congruence for periodic points.  The contribution here is the explicit
filtered and multiobjective formulation:

- bounded controller memory is incorporated by a synchronous product;
- safety, capture, and Pareto labels are integer weights on primitive cycles;
- every such filtered count satisfies the same prime-power congruence;
- the normalized difference counts primitive prime-power cycles exactly.

No novelty is claimed for the underlying Dold congruence.  The relevant
periodic-point literature is surveyed by
[Byszewski--Graff--Ward](https://arxiv.org/abs/2007.04031).

## 1. Weighted periodic points

Let $X$ be a finite set and let

$$
T:X\longrightarrow X
$$

be any map.  Write $\mathcal C(T)$ for its primitive periodic orbits.  Let
$A$ be a free abelian group and assign an integer-vector weight

$$
w:\mathcal C(T)\longrightarrow A.
$$

For $x\in\mathrm{Fix}(T^n)$, let $C_x$ be its primitive orbit.  Define the
weighted fixed-point count

$$
G_n(w)=\sum_{x\in\mathrm{Fix}(T^n)}w(C_x)\in A.
\tag{1}
$$

For each $d\ge1$, put

$$
W_d(w)=
\sum_{\substack{C\in\mathcal C(T)\\ |C|=d}}w(C).
\tag{2}
$$

### Theorem 1: filtered Dold congruence

For every $n\ge1$,

$$
G_n(w)=\sum_{d\mid n}d\,W_d(w).
\tag{3}
$$

Consequently,

$$
\sum_{d\mid n}\mu(n/d)G_d(w)
=nW_n(w)\in nA.
\tag{4}
$$

In particular, for every prime $\ell$ and $r\ge1$,

$$
G_{\ell^r}(w)
\equiv G_{\ell^{r-1}}(w)\pmod{\ell^rA},
\tag{5}
$$

and the normalized defect has the exact interpretation

$$
\frac{G_{\ell^r}(w)-G_{\ell^{r-1}}(w)}{\ell^r}
=W_{\ell^r}(w).
\tag{6}
$$

### Proof

A primitive orbit $C$ of length $d$ contributes its $d$ points to
$\mathrm{Fix}(T^n)$ exactly when $d\mid n$.  Each of those points has weight
$w(C)$, giving (3).  Möbius inversion gives (4).  When $n=\ell^r$, subtracting
the formula for $\ell^{r-1}$ from the formula for $\ell^r$ cancels every
primitive orbit of smaller length and leaves exactly
$\ell^rW_{\ell^r}(w)$.  This proves (5)--(6). $\square$

Equation (6) is stronger than divisibility: the quotient is not an error
term but the aggregate weight of the newly visible primitive cycles.

## 2. Universal orbit assets and change of denomination

Let

$$
\mathcal U_T=
\bigoplus_{C\in\mathcal C(T)}\mathbb Z[C]
$$

be the free abelian group on the primitive orbits.  Define the universal
fixed-point portfolio

$$
\Pi_n=
\sum_{x\in\mathrm{Fix}(T^n)}[C_x]
=\sum_{d\mid n}d
\sum_{\substack{C\in\mathcal C(T)\\|C|=d}}[C].
\tag{7}
$$

Theorem 1 holds first in $\mathcal U_T$.  Every weight system is then a
homomorphism

$$
\varphi:\mathcal U_T\longrightarrow A,
$$

and

$$
G_n(w)=\varphi(\Pi_n).
\tag{8}
$$

### Corollary 2: change of denomination

For every homomorphism $\psi:A\to B$,

$$
G_n(\psi\circ w)=\psi\bigl(G_n(w)\bigr),
$$

and the Dold and prime-power congruences commute with $\psi$.

Thus the primitive cycle is the structural object, while survival score,
capture score, utility, or a monetary valuation is a later denomination.
One can retain a vector-valued outcome until the final decision and then
apply any integral linear utility or change of units without recounting the
orbits.

This is the exact sense in which assets and currencies decouple here.  It
does not cover nonlinear pricing rules, stochastic discount factors that
were omitted from the state, or division by a nonunit that destroys
integrality.

## 3. Compiling finite-memory controllers

Suppose a finite environment has state set $E$ and deterministic update
$F:E\to E$.  A controller or runtime monitor has a finite memory set $Q$ and
an update rule

$$
\delta:Q\times E\longrightarrow Q.
$$

The closed-loop system is the product map

$$
T(e,q)=\bigl(F(e),\delta(q,e)\bigr)
\tag{9}
$$

on $E\times Q$.  Several controllers driven by the same environment are
handled by the product

$$
E\times Q_1\times\cdots\times Q_m.
$$

Any outcome computed from a complete primitive cycle and unchanged by cyclic
rotation can be used as $w(C)$.  Examples include:

- whether a safety violation occurs anywhere on the cycle;
- whether a target is reached at least once;
- the minimum number of surviving agents;
- a vector containing all controller outcomes;
- the indicator that a controller is Pareto-undominated on that cycle.

### Corollary 3: finite-controller supercongruence

Every integer-vector count of periodic closed-loop states selected by such a
cycle label satisfies (4)--(6).

The proof is not probabilistic.  Bounded queue contents, delayed releases,
and a finite pseudorandom-generator state may all be included in the product
state.  Once that state is included, the replay is a deterministic finite
map and Theorem 1 applies.

## 4. Pareto-filtered cycles

Let $m$ controllers be evaluated jointly on each primitive environment
cycle.  Give controller $j$ the integer outcome vector

$$
v_j(C)\in\mathbb Z^k,
$$

with every coordinate oriented so that larger is better.  Define
$P_j(C)=1$ when no controller strictly dominates $j$ on $C$, and
$P_j(C)=0$ otherwise.  Taking

$$
w(C)=\bigl(P_1(C),\ldots,P_m(C)\bigr)
$$

in Theorem 1 gives

$$
G_{\ell^r}^{\mathrm{Pareto}}
\equiv
G_{\ell^{r-1}}^{\mathrm{Pareto}}
\pmod{\ell^r}
\tag{10}
$$

coordinatewise.

The motivating replay had outcome pairs

$$
\begin{array}{c|c}
\text{controller}&(\text{capture},\text{survivors})\\ \hline
\text{unshielded}&(1,21)\\
\text{current-state filter}&(1,23)\\
\text{queue-aware filter}&(0,24).
\end{array}
$$

For that one seed, the unshielded controller is dominated, while the other
two are incomparable.  This observation motivates the Pareto label; one
seed supplies no periodic-orbit count and therefore no evidence for (10).
The congruence begins only after a finite transition system and its complete
cycle counts have been specified.

### A separate stochastic local-to-global certificate

There is a different rigorous way to analyze a spatial queue or delay field.
Suppose a backlog height $h(t,x)$ on a lattice really obeys the hypotheses
in Chatterjee's surface-growth framework: its update is monotone,
equivariant under adding a constant height, Lipschitz in the noise, and
driven by independent Gaussian noise or a Lipschitz image of it.  Then
[Chatterjee's Theorem 1.2](https://arxiv.org/abs/2103.09199) says that
sublinear growth of the global height variance is equivalent to sublinear
growth of the expected squared height difference at two distinct sites.
Thus a local backlog-difference statistic can certify global
superconcentration under those assumptions.

This is a published probabilistic implication, not a new result here and not
a supercongruence.  It does not directly cover the motivating Hawkes replay:
the paper explicitly places Poisson-clock update models outside its stated
recursion.  A separate reduction would be required before applying the
theorem.

## 5. Directed graphs and automata

Let $B$ be the adjacency matrix of a finite directed multigraph.  Then

$$
H_n=\mathrm{tr}(B^n)
$$

counts rooted closed walks of length $n$.  Decomposing closed walks into
primitive cyclic words gives

$$
\sum_{d\mid n}\mu(n/d)H_d\in n\mathbb Z
\tag{11}
$$

and hence

$$
\mathrm{tr}(B^{\ell^r})
\equiv
\mathrm{tr}(B^{\ell^{r-1}})
\pmod{\ell^r}.
\tag{12}
$$

A finite-state safety filter is compiled into the graph by the ordinary
product construction.  Formula (12) then counts accepted rooted cycles.  In
this sense, regular safety specifications preserve the orbit
supercongruence automatically.

This is the precise formal-language bridge: the monitor changes the product
graph, not the orbit-counting proof.

Local uniqueness should not be confused with low global expressive power.
Vishnikin and Okhotin prove that categorial grammars assigning a unique
category to each symbol can nevertheless homomorphically encode every
context-free language.  Their
[theorem](https://arxiv.org/abs/2505.14559) is the $k=1$ endpoint of the
lexical-ambiguity parameter studied by Kanazawa, but the encoding replaces
each original symbol by a nonempty block over a new alphabet.  It therefore
does **not** say that every context-free language is directly generated by a
$1$-valued grammar over its original alphabet.

This is an expressivity result, not a learnability or supercongruence result.
Its warning for controller models is still useful: giving each event one
unambiguous local type does not by itself make the global trace language
simple.  The finite-state hypothesis in Theorem 1 is doing real work.

## 6. Schottky words: an explicit family

The symbolic engine in
[*Indra's Pearls*](https://www.cambridge.org/core/books/indras-pearls/5B33E99CB1E4F19D989150B59E416A5B)
uses reduced words in free generators to organize Schottky-group limit sets.
The resulting no-backtracking language gives an explicit instance of
Theorem 1.

Take $g$ generators and their inverses.  Let $B_g$ be the $2g$ by $2g$
matrix whose $(a,b)$ entry is one unless $b=a^{-1}$.  It counts reduced
transitions, including the final-to-initial condition for a cyclic word.
If $J$ is the all-ones matrix and $P$ exchanges each generator with its
inverse, then

$$
B_g=J-P.
$$

The eigenvalues are

$$
2g-1\quad(1\text{ time}),\qquad
-1\quad(g-1\text{ times}),\qquad
1\quad(g\text{ times}).
$$

Hence the number of rooted cyclically reduced words of length $n$ is

$$
C_g(n)=
\mathrm{tr}(B_g^n)
=(2g-1)^n+(g-1)(-1)^n+g.
\tag{13}
$$

### Corollary 4: Schottky-word supercongruence

For every prime $\ell$, $r\ge1$, and $g\ge2$,

$$
C_g(\ell^r)
\equiv C_g(\ell^{r-1})
\pmod{\ell^r}.
\tag{14}
$$

Moreover,

$$
\frac{C_g(\ell^r)-C_g(\ell^{r-1})}{\ell^r}
$$

is the number of primitive unrooted cyclic words of length $\ell^r$.
Each such orbit has $\ell^r$ rooted representatives, which is exactly the
normalization in (11).

A finite-state restriction on the generator words is handled by a product
automaton and still satisfies (12), although the closed formula (13) will
usually disappear.

Minsky's work on
[Kleinian groups and the complex of curves](https://arxiv.org/abs/math/9907070)
relates combinatorial end data to bounded geometry through subsurface
projections.  None of that geometric depth is used in (11)--(12).  The
present corollary stops at the finite symbolic skeleton; it makes no claim
about ending laminations, injectivity radii, or hyperbolic $3$-manifold
classification.

## 7. A Gold-style finite-data obstruction

Carroll's exposition of Gold learning defines identification in the limit
from positive data and uses Angluin's finite-telltale characterization to
separate learnable from unlearnable grammar classes.  See
[Sections 5--6 of Carroll's thesis](https://www.math.harvard.edu/media/gabriel_carroll.pdf).
That framework suggests the following elementary limitation on learning
orbit defects.

### Theorem 5: no finite observation horizon determines the next defect

For every observation horizon $N$, there are two finite labeled transition
systems whose rooted closed-trace counts agree for every length $n\le N$ but
whose normalized prime-power defects differ by one at some length
$m=\ell^r>N$.

### Proof

Choose a prime power $m=\ell^r>N$.  Start with any finite labeled transition
system $\mathcal A$.  Form $\mathcal A'$ by taking its disjoint union with
one directed cycle of length $m$.  The added component has no closed walk of
positive length below $m$, so

$$
H_n(\mathcal A')=H_n(\mathcal A)
\qquad(1\le n\le N).
\tag{15}
$$

At length $m$, every one of the $m$ new states roots one new closed walk.
There is no new closed walk at length $m/\ell$.  Consequently,

$$
\frac{
 \bigl(H_m(\mathcal A')-H_{m/\ell}(\mathcal A')\bigr)
 -
 \bigl(H_m(\mathcal A)-H_{m/\ell}(\mathcal A)\bigr)}
 {m}
=1.
\tag{16}
$$

Both systems are finite, and their labeled closed-trace languages are
rotation invariant and regular in the finite-automaton sense.  This proves
the claim. $\square$

The theorem says that bounded trace data cannot certify the next
prime-power defect unless the hypothesis class supplies an independent
size, state-complexity, or telltale bound.  It is deliberately weaker than
Gold identification in the limit: it rules out a uniform finite horizon,
not eventual learning from an infinite text.  It also differs from PAC
learning, which introduces a sampling distribution and an error tolerance.

The obstruction is exact rather than statistical.  The two candidates have
identical observations through $N$, yet the next normalized defect differs
by the smallest possible nonzero amount.

## 8. Boundaries

The theorem does **not** assert any of the following:

1. **Geometric Brownian motion.** A multiplicative stochastic differential
   equation is not used.
2. **Collatz dynamics.** No Collatz map or arithmetic stopping-time claim is
   present.
3. **A congruence for real Hawkes probabilities.** Real-valued transition
   probabilities need not satisfy integer divisibility.  The theorem applies
   to unweighted counts after a finite delay-generator state has been
   included, or to integral multiplicities.
4. **A stability theorem.** Periodic-orbit divisibility does not imply
   Lyapunov stability, mixing, capture, or safety.
5. **Superconcentration from the arithmetic congruence.** Chatterjee's
   surface-growth result requires a stochastic lattice recursion with
   monotonicity, shift equivariance, and Lipschitz noise dependence.  Those
   properties do not follow from orbit divisibility.
6. **A new Dold theorem.** The new content is an explicit controller-filter,
   universal-valuation, and Schottky-word packaging of classical orbit
   decomposition.

An unbounded queue or a truly continuous state space is outside the finite
theorem.  One must first prove a finite quotient is faithful for the
observable under study, or pass to an inverse limit with separate compactness
and continuity arguments.

## 9. Why this belongs in the program

The A183068 and Gaussian results compare arithmetic data at adjacent
prime-power levels by valuation estimates.  The present mechanism is
different: it compares periodic-point counts by orbit length.  Both produce
an adjacent-scale law

$$
a(\ell^r)\equiv a(\ell^{r-1})\pmod{\ell^r},
$$

but the proof certificates are different:

| Program branch | Certificate for divisibility |
| --- | --- |
| Factorial-ratio sequences | carries plus scaling congruences |
| Finite-field point counts | Frobenius orbit decomposition |
| Controller-filtered cycles | primitive transition-system orbits |

This note therefore extends the repository's compiler viewpoint without
pretending that control simulations are factorial ratios or Gaussian-prime
products.

## 10. Exact checks

The checker:

- enumerates every self-map on sets of size at most five;
- assigns signed vector weights to every primitive orbit;
- verifies the full Möbius relation and all tested prime-power defects;
- checks every binary adjacency matrix of size at most three;
- checks the closed Schottky trace formula and its prime-power defects;
- checks that integral changes of denomination commute with orbit counts;
- checks exhaustive and sampled environment/controller product maps; and
- reproduces the Pareto classification of the motivating replay;
- constructs the Gold-style indistinguishable pair for multiple horizons.

Run:

```text
python verification/related/verify_filtered_orbit_supercongruence.py
```

The current run passes **260,164 exact checks**.  These verify the formulas,
not literature priority and not any continuous or stochastic model.
