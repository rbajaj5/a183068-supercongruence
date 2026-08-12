# Prime-boundary cubic congruences for the index-dependent companions

**Status:** complete elementary prime-level theorem; the all-level lift
remains open

## 1. The two surviving August families

Define

```math
V(N)=\sum_{k=0}^{N}
\binom{-N}{k}\binom Nk\binom{2k}{N}\binom{N+k}{k}
tag{1}
```

and, for a positive integer $c$,

```math
W_c(N)=\sum_{k=0}^{cN}
\binom{-N}{k}^2\binom{2k}{N}\binom{N+k}{k}.
tag{2}
```

The August mixed-binomial note recorded cubic evidence for these two
sign-opposite companions.  They are not covered by the fixed-slope theorem:
$\binom{2k}{N}$ and $\binom{N+k}{k}$ depend on the index in their upper
arguments.  Also, a unit-index summand generally has valuation only two,
so a termwise cubic proof is impossible.

### Theorem 1

For every prime $p\ge5$ and positive integers $n,c$,

```math
\boxed{V(np)\equiv V(n)\pmod {p^3}}
tag{3}
```

and

```math
\boxed{W_c(np)\equiv W_c(n)\pmod {p^3}.}
tag{4}
```

The missing power is an exact half-residue cancellation.

## 2. The scaled stratum

For $k=pq$, every factor at $(np,pq)$ is an adjacent scaling of the
corresponding factor at $(n,q)$.  For the negative binomial, oddness of $p$
and cancellation of the rational prefactor give

```math
\frac{\binom{-np}{pq}}{\binom{-n}{q}}
=\frac{\binom{p(n+q)}{pq}}{\binom{n+q}{q}}.
tag{5}
```

The other three quotients are attached to

```math
\binom{np}{pq},\qquad
\binom{2pq}{np},\qquad
\binom{p(n+q)}{pq}.
```

The adjacent Jacobsthal--Kazandzidis congruence therefore gives, whenever
the terms are nonzero,

```math
v_{np}(pq)\equiv v_n(q)\pmod {p^3},
\qquad
w_{np}(pq)\equiv w_n(q)\pmod {p^3},
tag{6}
```

where $v_N(k)$ and $w_N(k)$ denote the summands of (1) and (2).
Zero values of $\binom{2q}{n}$ occur at both scales.  Thus the scaled
stratum already transfers modulo $p^3$.

## 3. The half-residue lemma

Put $h=(p-1)/2$.  In $\mathbb F_p$,

```math
\sum_{s=1}^{h}\frac1{s^2}
=\sum_{s=h+1}^{p-1}\frac1{s^2}=0.
tag{7}
```

Indeed, $s\mapsto p-s$ identifies the two sums, while their sum is
$\sum_{s\in\mathbb F_p^\times}s^{p-3}=0$ for $p\ge5$.

This elementary identity is exactly the aggregate cancellation absent from
a termwise valuation count.

## 4. Unit blocks for the cutoff family

Write a unit index uniquely as

```math
k=pq+s,qquad 1\le s\le p-1.
```

Modulo $p$, Lucas' theorem and

```math
\binom{-np}{k}
=(-1)^k\frac{np}{np+k}\binom{np+k}{k}
```

give

```math
\frac1p\binom{-np}{pq+s}
\equiv
(-1)^{q+s}\frac ns\binom{n+q}{q}.
tag{8}
```

The remaining factors satisfy

```math
\binom{np+pq+s}{pq+s}\equiv\binom{n+q}{q}pmod p
tag{9}
```

and

```math
\binom{2pq+2s}{np}
\equiv
\begin{cases}
\binom{2q}{n},&1\le s\le h,\\
\binom{2q+1}{n},&h<s<p
\end{cases}
\pmod p.
tag{10}
```

Consequently the complete $q$-block of unit terms in (2), divided by
$p^2$, is congruent to

```math
n^2\binom{n+q}{q}^3
\left(
\binom{2q}{n}\sum_{s=1}^{h}s^{-2}
+\binom{2q+1}{n}\sum_{s=h+1}^{p-1}s^{-2}
\right),
tag{11}
```

which vanishes by (7).  The range $0\le k\le cnp$ contains the complete
unit blocks $0\le q<cn$; the endpoint $k=cnp$ belongs to the scaled
stratum.  Hence all discarded terms in $W_c(np)$ sum to zero modulo $p^3$.
Together with (6), this proves (4).

## 5. Unit blocks for the finite family

For $1\le s<p$, a second Lucas calculation gives

```math
\frac1p\binom{np}{pq+s}
\equiv
\frac ns(-1)^{s-1}\binom{n-1}{q}pmod p.
tag{12}
```

Multiplying (8), (9), (10), and (12), the unit $q$-block in (1), divided by
$p^2$, becomes

```math
(-1)^{q-1}n^2
\binom{n-1}{q}\binom{n+q}{q}
\left(
\binom{2q}{n}\sum_{s=1}^{h}s^{-2}
+\binom{2q+1}{n}\sum_{s=h+1}^{p-1}s^{-2}
\right).
tag{13}
```

It also vanishes by (7).  Here $0\le q<n$, exactly the complete unit blocks
inside $0\le k\le np$.  Combining this with (6) proves (3). $\square$

## 6. Boundary and next rung

The argument explains both the success and the limitation of the current
result.

- A generic unit summand has valuation two, so the cubic gain is genuinely
  aggregate.
- At $p=3$, the half-residue sum in (7) is nonzero.  Exact examples attain
  valuation two, so Theorem 1 cannot be extended uniformly to $p=3$.
- For $r>1$, one needs a lifted version of (7) compatible with the two
  Lucas carry states in (10), together with the higher-precision change of
  the $q$-dependent factors.  The first-level theorem alone does not imply
  the $p^{3r}$ tower.

Thus the prime boundary is closed for every parameter, while the all-level
companion towers remain an explicit higher-lift obligation.

## 7. Verification

Run

```text
python verification/related/verify_index_dependent_companion_boundary.py
```

The checker verifies the half-residue identity, formulas (8)--(13), every
complete unit block, the scaled transfer, and the two prime-boundary
congruences over an extended exact grid.

## 8. Source boundary

Peter Bala proposed the substitution families in the August correspondence.
The proof uses only Lucas' theorem, the classical adjacent
Jacobsthal--Kazandzidis congruence, and the finite-field inverse-square sum.
No priority claim is made.
