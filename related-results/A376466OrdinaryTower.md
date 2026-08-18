# The ordinary A376466 cubic tower

**Status:** exact two-moment reduction and extensive verification; the
quadratic Cartier-kernel lemma is now proved away from the scaled boundary
`j=0 mod p`, while the proposed shifted companion is false

Let

```math
T(m,k)=sum_{j=0}^m
 \binom mj\binom{m+j}{j}\binom kj
```

and define A376466 by

```math
B(N)=sum_{k=0}^N(-1)^{N+k}
 \binom Nk\binom{N+k}{k}^2T(N-1,k).
tag{1}
```

The companion reduction proves that `T(N-1,k)` is a homogeneous
negative-coordinate Apéry coefficient.  That settles its scaled row, but a
single unit summand in (1) can have only one factor of `p`.  The point of
this note is that the missing two powers are aggregate reciprocal moments.

## Conditional theorem

Subject to Lemma 2 below, for every prime `p>=5` and positive integers `n,r`,

```math
\boxed{B(np^r)\equiv B(np^{r-1})\pmod {p^{3r}}.}
tag{2}
```

The shifted conjecture on the OEIS record is different and is false; the
exact counterexample is retained in
[the companion reduction](A376AperyCompanionReduction.md#theorem-4-the-proposed-shifted-a376466-tower-is-false).

## 1. Two kernels

For `1<=k<=N`, extract the rational factor from the first binomial:

```math
\binom Nk=\frac Nk\binom{N-1}{k-1}.
```

Put

```math
K_N(k)=(-1)^{N+k}\binom{N-1}{k-1}
 \binom{N+k}{k}^2T(N-1,k),
tag{3}
```

so that the `k`-th summand of (1) is `N K_N(k)/k`.  The descended kernel is

```math
D_M(q)=(-1)^{M+q-1}\binom{M-1}{q}
 \binom{M+q}{q}^2T(M-1,q)
tag{4}
```

for `0<=q<M`, and zero otherwise.

We need two elementary lemmas.  They are stated at the precision used in
the proof; keeping the full product quotients gives slightly stronger
versions.

### Lemma 1 (two-moment unit expansion)

Let `N=np^r`, `M=N/p`, and let `p` not divide `k`.  With `q=floor(k/p)`,

```math
\boxed{
K_N(k)\equiv D_M(q)\left(1+\frac Nk\right)
\pmod {p^{2r}}.}
tag{5}
```

### Proof

Write

```math
A_N(k)=(-1)^{N+k}\binom{N-1}{k-1}\binom{N+k}{k}^2.
```

Separating factors whose indices are divisible by `p` from the three
factorial products gives, with

```math
H_p(k)=\sum_{\substack{1\le h\le k\\p\nmid h}}\frac1h,
```

the first-order expansion

```math
A_N(k)\equiv
(-1)^{M+q-1}\binom{M-1}{q}\binom{M+q}{q}^2
\left(1+\frac Nk+NH_p(k)\right)
\pmod {p^{2r}}.
tag{6}
```

Indeed every unit factor is of the form `1+cN/h`; products of two
nonconstant terms are divisible by `N^2`, while the multiples of `p`
give exactly the three displayed lower binomials.  The coefficients of the
linear logarithm are `+1` from `binom(N-1,k-1)` and `+2` from the two
copies of `binom(N+k,k)`; after the common multiples are removed they
combine to `N/k+NH_p(k)`.

For the shifted row, use its negative-coordinate form

```math
T(N-1,k)=\mathcal B(-N,k,-N).
```

The same separation of multiples of `p`, now in the three factors defining
`mathcal B`, gives

```math
T(N-1,k)\equiv T(M-1,q)(1-NH_p(k))
\pmod {p^{2r}}.
tag{7}
```

The two linear harmonic terms in (6)--(7) cancel.  Their product is a
multiple of `N^2`; multiplication leaves (5). QED

The proof uses only finite products.  Thus (6)--(7) remain valid when a
lower binomial vanishes: perform the cancellation before reducing modulo
`p^(2r)`, or use the integer-binomial continuation in the displayed
negative-coordinate row.

### Lemma 2 (quadratic Cartier descent)

For `N=np^r`, `M=N/p`, and every nonnegative `j`,

```math
\boxed{D_N(j)\equiv D_M(\lfloor j/p\rfloor)\pmod {p^{2r}}.}
tag{8}
```

### Unit digits are already proved

There is an exact relation between the two kernels:

```math
K_N(j)=\frac{j}{j-N}D_N(j),
\qquad
D_N(j)=\left(1-\frac Nj\right)K_N(j).
tag{8a}
```

If `p` does not divide `j`, multiply (5) by `1-N/j`.  Since this factor is
a `p`-adic integer and

```math
\left(1+\frac Nj\right)\left(1-\frac Nj\right)
=1-\frac{N^2}{j^2}\equiv1\pmod {p^{2r}},
```

we obtain (8) immediately.  Thus no residue-by-residue induction is needed:
the two-moment expansion already proves every unit digit.

### Remaining scaled-boundary lemma

It remains to prove only

```math
\boxed{D_N(pq)\equiv D_M(q)\pmod {p^{2r}}}.
tag{8b}
```

Conversely, (8b) together with the proved unit case gives (8) for every
`j`; hence (8) and (8b) are equivalent modulo Lemma 1.

The three outer binomials in (4) satisfy signed shifted-binomial descent,
and the negative-coordinate identity

```math
T(N-1,pq)=\mathcal B(-N,pq,-N)
```

supplies the homogeneous scaled row.  Straub's theorem proves each scaled
row difference modulo `p^(3(min(v_p(M),v_p(q))+1))`.  The remaining issue is
to show that its first defect cancels the first defect of the three outer
binomials uniformly when that exponent is below `2r`.

### Evidence and source boundary

Exact arithmetic shows that the two first defects cancel and that (8b)
holds through three adjacent levels in the audit range.  This is stronger
than the ordinary Cartier descent supplied directly by Straub's
shifted-binomial lemmas.

That observation is not yet a proof of (8b).  Accordingly, the scaled
boundary cancellation--not the full digitwise statement--is retained as the
one explicit proof obligation of this note.  Once (8b) is proved, the
remainder below is a formal weighted block argument.

## 2. Reciprocal block sums

For `s>=1`, `L>=0`, and `a=1,2`, put

```math
R_{a,s}(L)=
\sum_{\substack{Lp^s<k<(L+1)p^s\\p\nmid k}}\frac1{k^a}.
```

The complete reduced-residue calculation gives

```math
v_p(R_{1,s}(L))\ge2s,
\qquad
v_p(R_{2,s}(L))\ge s.
tag{9}
```

For the second estimate, reduce modulo `p^s` and use that inversion
permutes the units, so the sum is congruent to the sum of their squares.
For the first, pair `u` with `p^s-u`; after division by `p^s` the residual
reciprocal-square sum vanishes once more.  Translation by `Lp^s` changes
only terms beyond the displayed precision.

Straub's weighted block induction says that if `C_t(j)` satisfies

```math
C_t(j)\equiv C_{t-1}(\lfloor j/p\rfloor)\pmod {p^{2t}},
tag{10}
```

then the reciprocal-square estimate in (9), grouping a `p^t`-block into
`p` subblocks recursively, gives

```math
\sum_{\substack{Lp^t<k<(L+1)p^t\\p\nmid k}}
 \frac{C_{t-1}(\lfloor k/p\rfloor)}k\equiv0\pmod {p^{2t}},
tag{11}
```

The reciprocal-first-moment analogue is

```math
\sum_{\substack{Lp^t<k<(L+1)p^t\\p\nmid k}}
 \frac{C_{t-1}(\lfloor k/p\rfloor)}{k^2}\equiv0\pmod {p^t}.
tag{12}
```

For completeness, (11) needs the strengthened descent (8), not merely
ordinary mod-`p^t` descent.  Replace the weight on the first digit by its
parent using (8); the error is a multiple of `p^(2t)`.  The unweighted
reciprocal sum over each complete child block has valuation `2`, and
iteration through `t` digits gives `2t`.  Formula (12) is exactly Straub's
induction with `a_k=1/k^2` on the unit indices and zero otherwise.

## 3. The unit shell

Take `N=np^r` and `M=N/p`.  Lemma 1 gives

```math
\sum_{p\nmid k}\frac NkK_N(k)
\equiv
N\sum_{p\nmid k}\frac{D_M(\lfloor k/p\rfloor)}k
+N^2\sum_{p\nmid k}\frac{D_M(\lfloor k/p\rfloor)}{k^2}
\pmod {p^{3r}}.
tag{13}
```

The range `1<=k<N` is a union of `n` complete blocks of length `p^r`.
Apply (11)--(12) with the descent (8).  The first sum in (13) is divisible
by `p^(2r)` and the second by `p^r`; the prefactors `N` and `N^2` therefore
make both terms divisible by `p^(3r)`.  Hence the entire unit shell
vanishes modulo `p^(3r)`.

## 4. The scaled shell

For `k=pq`, compare the corresponding summands at `N` and `M`.  The outer
triple is a product of adjacent binomial-scaling quotients, and the row is
the homogeneous coefficient `mathcal B(-N,pq,-N)`.  The
Jacobsthal--Kazandzidis valuation, together with the valuation of the lower
summand when `q` lies below the current scale, gives

```math
\frac N{pq}K_N(pq)\equiv\frac MqK_M(q)
\pmod {p^{3r}}.
tag{14}
```

This is the composite scaled transfer already checked factor by factor in
the companion reduction: if `s=v_p(q)<r-1`, the lower summand supplies the
missing `2(r-1-s)` powers, while the scaling quotient supplies
`r+2s+2`; if `s>=r-1`, the scaling quotient alone reaches `3r`.
The endpoints are equal or covered by the same integer identity.

Summing (14) and adding the unit-shell result proves (2), conditional only
on Lemma 2. QED

## 5. Verification and source boundary

Run

```text
python verification/related/verify_a376466_ordinary_tower.py
```

The checker tests (5)--(12), the exact unit-digit deduction (8a), the
remaining scaled boundary (8b), both shell congruences, and the full tower.
It includes primes through 19 at the first level, the second level for
`p=5,7`, and third-level scaled-boundary cases at `p=5`; 37 sampled tower
instances attain the claimed exponent exactly.

The sequence and conjecture are Peter Bala's OEIS contribution.  The
negative-coordinate row and scaled-shell reduction are proved in the
companion note.  The ingredients used here are finite binomial products,
the classical Jacobsthal--Kazandzidis congruence, and the weighted block
induction in Armin Straub's
[*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854).
The two-moment decomposition (5) and the reduction of (8) to the scaled
boundary (8b) are the exact reductions recorded here.  The checker is
evidence for, not a proof of, (8b).  No literature-priority claim is made.
