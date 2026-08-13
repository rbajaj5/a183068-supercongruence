# The all-level digit reduction for A365029

**Status:** exact all-level reduction; the final complete-digit cancellation
is isolated and verified through four levels; this note does not claim that
the remaining lemma is proved

The first two adjacent levels of the A365029 tower are proved in the
[two-digit note](A365029FirstTwoLevels.md).  This note records the exact
recursion that survives at every level and sharpens the remaining obligation.

Put

```math
F(N,k)=\binom{N+k-1}{k}^{2}\binom{2k-1}{N}.
```

Let $q=p^r$, $N=nq$, and write a nonmultiple of $p$ in a complete block as
$k=q\ell+u$, where $0<u<q$ and $p\nmid u$.  Set

```math
b=\left\lfloor\frac{k-1}{p}\right\rfloor,
\qquad
d=\left\lfloor\frac{2k-1}{p}\right\rfloor.
```

## Exact recursive factorization

Splitting the first shifted binomial into factors with index divisible and
not divisible by $p$ gives the exact identity

```math
\frac1q\binom{N+k-1}{k}
=
\frac nk
\binom{np^{r-1}+b}{b}
U_r(n,k),
\tag{1}
```

where

```math
U_r(n,k)=
\prod_{\substack{1\leq j<k\\p\nmid j}}
\left(1+\frac{nq}{j}\right).
\tag{2}
```

Since $U_r(n,k)\equiv1\pmod q$, (1) immediately gives the useful
all-level congruence

```math
\frac1q\binom{N+k-1}{k}
\equiv
\frac nk\binom{np^{r-1}+b}{b}
\pmod q.
\tag{3}
```

Lucas reduction of the second binomial is equally recursive:

```math
\binom{2k-1}{N}
\equiv
\binom d{np^{r-1}}
\pmod q.
\tag{4}
```

Formula (4) is the prime-power version of the carry digit
$2v+\epsilon(c)$ in the two-digit proof.  Equations (3)--(4) transform the
normalized complete block into the explicit lower-level sum

```math
\frac1{q^2}
\sum_{\substack{1\leq u<q\\p\nmid u}}F(nq,q\ell+u)
\equiv
n^2\sum_{\substack{1\leq u<q\\p\nmid u}}
u^{-2}
\binom{np^{r-1}+\lfloor(q\ell+u-1)/p\rfloor}
      {\lfloor(q\ell+u-1)/p\rfloor}^{2}
\binom{\lfloor(2q\ell+2u-1)/p\rfloor}{np^{r-1}}
\pmod q.
\tag{5}
```

Thus the whole tower is reduced to the following single statement.

## Complete-digit cancellation lemma

For every prime $p\geq5$, $r\geq1$, $n\geq1$, and
$0\leq\ell<n$, the right side of (5) vanishes modulo $p^r$.

Equivalently, each lower and upper half vanishes separately.  The exact
checker confirms the stronger half-block formulation through $r=4$.
Individual fixed last-digit subsums generally remain units after
normalization, so the lemma cannot be replaced by a termwise or
single-residue estimate.  The cancellation is genuinely over the complete
digit set.

The $r=1$ proof is the reciprocal-square half-sum identity.  The $r=2$
proof is the paired harmonic calculation already written out in the
first-two-level note.  Equation (5) is the induction-ready form of the same
mechanism: the only changing data are the two floor functions, which encode
the carry of the leading binary split.

## Verification

Run

```text
python verification/related/verify_a365029_all_level_digit_reduction.py
```

The checker verifies (1), (3), (4), (5), both half-block cancellations,
and the failure of fixed-last-digit cancellation.  This is a rigorous
reduction and boundary map, not a proof of the complete-digit lemma.
