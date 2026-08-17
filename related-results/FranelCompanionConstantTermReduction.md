# A constant-term reduction for the Franel companions

**Status:** exact reduction and finite verification; the `A362676(p)` prime
boundary is now proved separately, while the full cubic contraction below
remains open

This note consolidates the finite sums on
[A362676](https://oeis.org/A362676) and
[A363985](https://oeis.org/A363985) into one two-variable constant-term
family.  It is a reduction, not a proof of the conjectured cubic towers.

## 1. The master family

For `a` in `{1,2}`, an integer `m`, and `N >= 0`, put

```math
W_{a,m}(N)=\sum_{k=0}^{N}(-4)^{N-k}\binom Nk
 \binom{mN+ak}{ak}\binom{2k}{k}.
```

The binomial coefficient with a negative upper entry is interpreted by

```math
\binom{-h}{j}=(-1)^j\binom{h+j-1}{j}
\qquad (h>0,\ j\ge 0).
```

Define

```math
P_{a,m}(y,z)
=(1+y)^m\left(
  \frac{(1+y)^a(1+z)^2}{y^a z}-4
\right).
```

When `m >= 0`, this is an integral Laurent polynomial.  When `m < 0`, we
expand `(1+y)^(mN)` in nonnegative powers of `y`; only finitely many of
those powers can contribute to the constant term below.

### Proposition 1 (exact constant term)

For every integer `m`, `a` in `{1,2}`, and `N >= 0`,

```math
\boxed{
W_{a,m}(N)=\operatorname{CT}_{y,z} P_{a,m}(y,z)^N.
}
```

### Proof

Choose `k` copies of the first term and `N-k` copies of `-4`.  The
corresponding summand in the `N`-th power is

```math
\binom Nk(-4)^{N-k}
(1+y)^{mN+ak}(1+z)^{2k}y^{-ak}z^{-k}.
```

Its constant term in `y` is `binom(mN+ak,ak)` and its constant term in `z`
is `binom(2k,k)`.  Summing over `k` proves the formula.  For negative `m`
the same calculation takes place in the `y`-adic expansion; the required
coefficient has degree `ak`, so the extraction is still finite.  QED

The case `a=1` also has the useful cancellation

```math
P_{1,m}(y,z)
=(1+y)^m\frac{(1+z)^2+y(1-z)^2}{yz}.
```

Thus the apparently alternating `u_m` sums have a kernel with no explicit
subtraction by `4` after simplification.

## 2. Recovery of the OEIS families

The two families on A363985 are exactly

```math
u_m(N)=W_{1,m}(N),
\qquad
v_m(N)=W_{2,m}(N).
```

Three boundary identifications are useful.

### Proposition 2 (named specializations)

Let

```math
F(N)=\sum_{k=0}^{N}4^{N-k}\binom Nk
\binom{N-1}{k}\binom{2k}{k}
```

be A362676. Then

```math
u_{-1}(N)=(-1)^N F(N).
```

Moreover,

```math
u_0(N)=v_0(N)=(-1)^N\binom{2N}{N},
```

and `v_1(N)` is the Franel number

```math
\sum_{j=0}^{N}\binom Nj^3.
```

### Proof

For the first identity, use

```math
\binom{-N+k}{k}=(-1)^k\binom{N-1}{k}.
```

Multiplying the signs gives

```math
(-4)^{N-k}(-1)^k=(-1)^N4^{N-k}.
```

The second identity follows by taking the constant term of
`((1+z)^2/z-4)^N=((1-z)^2/z)^N`.  The third is the classical
Franel--Askey--Gasper identity; the checker also verifies it directly from
the two finite sums.  QED

Because `p` is odd, `Np^r` and `Np^(r-1)` have the same parity.  Hence the
conjecture for A362676 is exactly the `m=-1` subcase of the conjectural
`u_m` tower, with no sign discrepancy between adjacent levels.

## 3. What existing theorems do and do not prove

Straub's multivariate theorem proves a cubic tower for the partition family
with at least two blocks and every block of size at most two.  In
particular, it proves the Franel tower through the multi-block realization
`lambda=(1,1,1)`.  The same paper explicitly leaves the alternative
one-block Askey--Gasper rational function as Conjecture 3.8.

This distinction matters here.  Proposition 1 gives a compact
constant-term representation, but a general constant-term or Dwork theorem
normally supplies only the Gauss modulus `p^r`.  It does not automatically
upgrade the entire integer-parameter deformation to `p^(3r)`.  Nor may the
known `m=1`, `a=2` Franel theorem simply be varied in `m`.

The exact missing statement is therefore the following.

### Cubic Cartier contraction target

For `p >= 5`, `r,n >= 1`, every integer `m`, and `a` in `{1,2}`, prove

```math
\operatorname{CT}P_{a,m}^{np^r}
\equiv
\operatorname{CT}P_{a,m}^{np^{r-1}}
\pmod {p^{3r}}.
```

For nonnegative `m` this is a Laurent-polynomial statement.  For negative
`m` it must also control the chosen `y`-adic expansion uniformly; clearing
the denominator without tracking that expansion would change the constant
term problem.  A proof must therefore produce the extra two powers on the
unit shell, not merely cite the ordinary constant-term Dwork congruence.

## 4. Exact evidence

The companion checker
[`verify_franel_companion_ct_reduction.py`](../verification/related/verify_franel_companion_ct_reduction.py)
does four independent jobs:

1. it constructs `P_{a,m}^N` as a Laurent-polynomial dictionary for
   `m >= 0` and verifies Proposition 1;
2. it verifies all three specializations in Proposition 2;
3. it checks both conjectural families for `-8 <= m <= 8`,
   `p in {5,7,11,13}`, `1 <= n <= 4`, and `r in {1,2}`; and
4. it records sharp instances where the adjacent difference has valuation
   exactly `3r`.

These computations are exact integer arithmetic.  They support the
conjecture and debug the reduction, but they are not used as a substitute
for the cubic Cartier contraction.

## 5. Campaign disposition

This note moves A362676 and A363985 from `open-target` to `partial` in the
110-record campaign.  The finite sums and their relationship are no longer
unstructured: both now reduce to one explicit kernel family and one precise
local lemma.  The separate
[A362676 prime-boundary theorem](A362676PrimeBoundary.md) proves the
`n=r=1` instance for every prime `p>=5`; it does not supply the missing
all-`n`, all-`r` contraction.  The records do not move to `proved-here`
until that lemma is proved for all integer `m`.
