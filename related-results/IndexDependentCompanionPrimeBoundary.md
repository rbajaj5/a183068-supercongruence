# Prime boundary and scaled cubic shells for the index-dependent companions

**Status:** complete elementary prime-level theorem and complete all-level
scaled-stratum theorem; the unit-shell lift remains open

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

## 2. The scaled stratum at every level

For $k=pq$, every factor at $(pM,pq)$ is an adjacent scaling of the
corresponding factor at $(M,q)$.  For the negative binomial, oddness of $p$
and cancellation of the rational prefactor give

```math
\frac{\binom{-pM}{pq}}{\binom{-M}{q}}
=\frac{\binom{p(M+q)}{pq}}{\binom{M+q}{q}}.
tag{5}
```

The other three quotients are attached to

```math
\binom{pM}{pq},\qquad
\binom{2pq}{pM},\qquad
\binom{p(M+q)}{pq}.
```

The four lower-scale binomials are therefore

```math
\binom{-M}{q},\quad \binom Mq,\quad
\binom{2q}{M},\quad \binom{M+q}{q}.
```

### Theorem 2 (all-level scaled transfer)

Let $p\ge5$, $N=np^r$, $M=N/p$, and $q\ge0$.  Then

```math
\boxed{
v_N(pq)\equiv v_M(q)\pmod {p^{3r}},\qquad
w_N(pq)\equiv w_M(q)\pmod {p^{3r}}.
}
tag{6}
```

Here a binomial that is zero at one scale is zero at the other, so the
display includes the support boundary.

To prove the theorem, put $s=v_p(q)$ and first suppose $s<r-1$.  The
factors $\binom{-M}{q}$ and $\binom Mq$ each have valuation at least
$r-1-s$.  The finite summand contains one of each; the cutoff summand
contains two copies of the first.  Hence either lower summand has valuation
at least

```math
2(r-1-s).
tag{6a}
```

For each of the four adjacent quotients, the full
Jacobsthal--Kazandzidis modulus contains the factor

```math
p^3ab(a-b).
```

For example, the quotient attached to $\binom Mq$ has valuation bound

```math
3+v_p(M)+v_p(q)+v_p(M-q)=r+2s+2.
tag{6b}
```

The other three quotients have the same bound: their triples are
$(M+q,q,M)$, $(M,q,M-q)$, and $(2q,M,2q-M)$, respectively, and
$v_p(M\pm q)=v_p(2q-M)=s$.  A product of quantities congruent to one
modulo $p^{r+2s+2}$ is again congruent to one to that precision.  Combining
(6a) and (6b) gives

```math
2(r-1-s)+(r+2s+2)=3r.
```

If $s\ge r-1$, the same Jacobsthal modulus is already at least $3r$;
integrality of the lower summand finishes the proof.  The case $q=0$ is
an equality.  This proves (6).

Thus the scaled stratum is not part of the remaining all-level problem.
Only the sum of indices prime to $p$ still needs a higher lift.

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

Theorem 2 now removes the entire scaled stratum from that obligation.  An
exact coefficient representation makes the remaining carry particularly
transparent.  Define

```math
F_N(X)=\sum_{k=0}^{N}
\binom{-N}{k}\binom Nk\binom{N+k}{k}X^k
tag{14}
```

and

```math
G_{c,N}(X)=\sum_{k=0}^{cN}
\binom{-N}{k}^2\binom{N+k}{k}X^k.
tag{15}
```

Since $[z^N](1+z)^{2k}=\binom{2k}{N}$, the two companions are exactly

```math
\boxed{
V(N)=[z^N]F_N((1+z)^2),\qquad
W_c(N)=[z^N]G_{c,N}((1+z)^2).
}
tag{16}
```

Thus the two Lucas states are simply the two halves of the coefficient
extraction through the quadratic substitution $X=(1+z)^2$.  The
coefficientwise mixed-binomial theorem gives two powers on unit indices;
the remaining third power is exactly the reciprocal-square cancellation
created by (16).  At level one it is (7).  At higher levels the remaining
task is a carry-aware version of Straub's aggregate block lemma for the
weights in (14)--(15).  No termwise strengthening can supply it.

Thus the prime boundary and every scaled shell are closed for every
parameter.  The all-level companion towers have been reduced to one
explicit aggregate unit-shell identity.

## 7. Verification

Run

```text
python verification/related/verify_index_dependent_companion_boundary.py
```

The checker verifies the half-residue identity, formulas (8)--(16), every
complete unit block, the all-level scaled transfer, and the two
prime-boundary congruences over an extended exact grid.

## 8. Source boundary

Peter Bala proposed the substitution families in the August correspondence.
The proof uses only Lucas' theorem, the classical adjacent
Jacobsthal--Kazandzidis congruence, and the finite-field inverse-square sum.
The aggregate induction targeted in (16) is modeled on Armin Straub's
[generalized Beukers block lemma](https://arxiv.org/abs/1401.0854), but its
published hypothesis has a one-state Cartier descent; the doubling carry in
$\binom{2k}{N}$ prevents applying it verbatim.  No priority claim is made.
