# Maximin residue-orbit experiment for the paired Apéry towers

**Status:** exact computational reduction target; not a proof

**Scope:** the unshifted congruences conjectured on OEIS A376459--A376466

## 1. The eight summand families

Write

```math
H(N,k)=\sum_{i=0}^{\min(N,k)}
\binom Ni^2\binom{N+k-i}{k-i}.
```

This is the crystal-ball triangle A108625 used in the eight OEIS records.
For $0\leq k\leq N$, let $F_j(N,k)$ be the displayed summand defining
A376$j$, for $459\leq j\leq466$. Explicitly:

```math
\begin{array}{c|l}
j&F_j(N,k)\\ \hline
459&(-1)^{N+k}\binom Nk\binom{N+k}kH(N,N-k)\\
460&(-1)^{N+k}\binom Nk\binom{N+k}k^2H(N,k)\\
461&\binom Nk^2\binom{N+k}kH(N,k)\\
462&\binom Nk^2\binom{N+k}kH(N,N-k)\\
463&\binom Nk^2\binom{N+k}k^2H(N,k)\\
464&\binom Nk^2\binom{N+k}k^2H(N,N-k)\\
465&\binom Nk^2\binom{N+k}k^2H(N-1,k)\\
466&(-1)^{N+k}\binom Nk\binom{N+k}k^2H(N-1,k).
\end{array}
```

Put $a_j(N)=\sum_{k=0}^N F_j(N,k)$.

## 2. The orbit-transfer target

Let $p\geq5$ be prime and write $N=np^r$, with $p\nmid n$. (The general
case follows by absorbing $v_p(n)$ into $r$.) Define

```math
S_{j,s}(N)=
\sum_{\substack{1\leq k\leq N\\v_p(k)=s}}F_j(N,k).
```

The exact data support the following single certificate for all eight
unshifted towers:

> **Orbit-transfer conjecture.** For $459\leq j\leq466$, $p\geq5$, and
> $n,r\geq1$ with $p\nmid n$,
>
> ```math
> \begin{aligned}
> v_p(S_{j,0}(N))&\geq3r,\\
> v_p\!\left(S_{j,s}(N)-S_{j,s-1}(N/p)\right)&\geq3r
> &&(s\geq1),\\
> v_p\!\left(F_j(N,0)-F_j(N/p,0)\right)&\geq3r.
> \end{aligned}
> \tag{1}
> ```

Only finitely many strata are nonempty. Summing (1) over all of them gives

```math
a_j(np^r)\equiv a_j(np^{r-1})\pmod {p^{3r}}.
\tag{2}
```

Thus (1), if proved, closes the **unshifted half** of all eight named
conjectures at once.  It does not address the separate shifted congruences
at $np^r-1$.

## 3. Why this is a maximin problem

At $N=p$, the weakest individual summand is generally only one or two
powers deep. Pairing $k$ with $p-k$ is sufficient for A376459, but not
for the other seven records.  Summing the complete unit stratum supplies
the missing power in every case.

| Records | Minimum individual depth | Minimum paired depth | Complete unit-stratum depth |
| --- | ---: | ---: | ---: |
| A376459 | 1 | 3 | 3 |
| A376460, A376466 | 1 | 2 | 3 |
| A376461--A376465 | 2 | 2 | 3 |

The relevant optimization is therefore

```math
\max_{\mathcal P}
\min_{B\in\mathcal P}
v_p\!\left(\sum_{k\in B}F_j(N,k)\right),
```

where $\mathcal P$ ranges over proof-compatible residue partitions. The
data reject singleton and, usually, two-element partitions; complete unit
residue aggregation is the first partition that reaches the cubic target.

There is a limited analogy with paradoxical-decomposition proofs: both begin
with a group action, split into orbits, and reassemble.  Nothing paradoxical
occurs here.  All sets are finite, no choice principle is used, and the gain
comes from congruential cancellation over the finite unit group.

## 4. Boundary of the Gaussian synthesis

These eight classical cubic conjectures are **not** consequences of the
repository's Gaussian Frobenius-twist theorem. Weighting the summands by
$i^k$ destroys the complete unit-stratum cancellation.

In the exact adjacent-scale tests at $p=5,7,11$, and at the second
$5$-power level, the Gaussian-twist valuation is only

```math
r\quad\text{for A376459, A376460, A376466},
```

and

```math
2r\quad\text{for A376461--A376465}.
```

Equality occurs in every tested family.  Hence a cubic Gaussian version
would require a new cancellation mechanism; it is not hidden inside the
present synthesis.

## 5. Exact evidence

The checker verifies (1), its consequence (2), and the partition-depth table
on the following grid:

```text
p in {5,7,11}, r = 1, n = 1..3;
p in {5,7},    r = 2, n = 1..2;
p = 5,         r = 3, n = 1.
```

It also verifies the Gaussian-twist boundary exactly.  All arithmetic uses
Python integers; no floating-point approximation occurs.

Run:

```text
python verification/related/verify_bala_paired_orbit_transfer.py
```

The experiment identifies the missing lemma.  It is not evidence that the
shifted towers follow, and it is not a literature-priority claim.
