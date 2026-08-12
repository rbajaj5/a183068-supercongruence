# Quadratic towers for every cyclotomic rational framing

**Status:** complete elementary proof of the general principle conjectured
on A228960 and A350383; no literature-priority claim

Let `k` be a positive integer, let `m` be an integer, and let

```math
f(x)=\frac{g(x)}{h(x)},
\tag{1}
```

where `g` and `h` are finite products of cyclotomic polynomials.  Bala
conjectured on [A228960](https://oeis.org/A228960) and
[A350383](https://oeis.org/A350383) that

```math
a(n)=[x^{kn}]f(x)^{mn}
\tag{2}
```

satisfies the adjacent tower modulo `p^(2r)` for all but finitely many
primes depending on `f`.  This note proves that statement and gives an
explicit finite exceptional set.

## 1. The theorem

Normalize the constant term by putting

```math
F(x)=f(x)/f(0).
```

Cyclotomic factorization gives integers `c_d`, only finitely many nonzero,
such that

```math
F(x)=\prod_{d\ge1}(1-x^d)^{c_d}.
\tag{3}
```

Indeed, this follows factor by factor from Möbius inversion for
cyclotomic polynomials.  Put

```math
D_f=\operatorname{lcm}\{d:c_d\ne0\},
\tag{4}
```

with `D_f=1` for the empty product.

### Theorem 1 (cyclotomic rational-framing tower)

For every positive `n,r`, every integer `m`, and every odd prime `p` with
`p` not dividing `D_f`,

```math
\boxed{
[x^{knp^r}]f(x)^{mnp^r}
\equiv
[x^{knp^{r-1}}]f(x)^{mnp^{r-1}}
\pmod {p^{2r}}.}
\tag{5}
```

Thus the possible exceptional primes are contained in the finite set
consisting of `2` and the prime divisors of `D_f`.

#### Proof

Since `p` is odd, the powers of the sign `f(0)` agree at the two adjacent
levels.  It is therefore enough to prove (5) with `f` replaced by `F`.

Define the reduced Frobenius logarithm

```math
\Lambda_p(x)
=\log F(x)-\frac1p\log F(x^p).
\tag{6}
```

Using (3), cancellation of the terms with `p|j` gives the exact expansion

```math
\Lambda_p(x)
=-\sum_d c_d
  \sum_{\substack{j\ge1\\p\nmid j}}\frac{x^{dj}}j.
\tag{7}
```

Hence `Lambda_p` belongs to `x Z_(p)[[x]]`.  More importantly, because
`p` divides neither `d` nor `j`, its support contains no exponent divisible
by `p`.

Write `N=np^r`, `M=N/p`, and set

```math
G(x)=x^{-k}F(x)^m.
```

Then (6) gives

```math
G(x)^N=G(x^p)^M\exp\!\left(mN\Lambda_p(x)\right).
\tag{8}
```

Taking constant coefficients yields the exact adjacent difference

```math
a(N)-a(M)
=\sum_{j\ge1}\frac{(mN)^j}{j!}
 \operatorname{CT}\!\left(G(x^p)^M\Lambda_p(x)^j\right).
\tag{9}
```

The term `j=1` is zero.  Every exponent of `G(x^p)^M` is divisible by
`p`, while (7) has no exponent divisible by `p`, so the two supports cannot
sum to zero.

All remaining constant coefficients are `p`-integral.  For `j>=2`,

```math
v_p\!\left(\frac{(mN)^j}{j!}\right)
\ge jr-v_p(j!)\ge2r.
\tag{10}
```

For the last inequality, the case `j=2` is immediate and, for `j>=3`,
`v_p(j!)<=j-2` for every odd prime.  Each term of (9) is therefore
divisible by `p^(2r)`, proving (5).  QED

Negative `m` causes no issue: `F(0)=1`, so every integral power of `F` is
an integral formal power series.  For any fixed coefficient, only finitely
many degrees in the exponential in (9) contribute.

## 2. The two named records

For A228960,

```math
1+x+x^3+x^4=(1+x)(1+x^3)
=\frac{(1-x^2)(1-x^6)}{(1-x)(1-x^3)}.
\tag{11}
```

Thus `D_f=6`, and Theorem 1 proves its displayed tower for every
`p>=5`.  It also proves the full general principle printed on that page.

For A350383,

```math
\frac1{1+x+x^2}=\frac{1-x}{1-x^3},
\tag{12}
```

so `D_f=3`; again every `p>=5` is covered.  The earlier
[coefficient-pair theorem](CyclotomicCoefficientPairTheorem.md) remains a
stronger coefficientwise result for these two special polynomials, but is
no longer needed to close the general scalar conjecture.

## 3. Verification and source boundary

The exact checker
[`verify_cyclotomic_rational_framing.py`](../verification/related/verify_cyclotomic_rational_framing.py)

1. verifies the depleted logarithm (7) by independent ghost subtraction;
2. tests (5) for positive and negative exponent profiles, positive and
   negative `m`, several coefficient slopes `k`, and two adjacent levels;
3. checks both named OEIS specializations; and
4. records examples at excluded primes to show why the theorem states only
   a sufficient exceptional set, not an exact one.

The computation is transcription control.  The proof is the support
separation and valuation estimate (7)--(10).  The conjectures are those on
the linked OEIS pages.  No claim is made that this proof or its full
generality has literature priority.
