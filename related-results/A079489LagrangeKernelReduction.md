# The two A079489 families have one Lagrange kernel

**Status:** exact reduction of both named coefficient families; all algebraic
identities and sampled towers pass exact checks; the normalized cubic kernel
estimate in (16) remains open

Let `A(x)` be the generating function on
[OEIS A079489](https://oeis.org/A079489).  The page asks whether, for every
integer `r`, positive integer `s`, prime `p>=5`, and positive `n,k`, both

```math
u_{r,s}(n)=[x^{sn}]A(x)^{rn}
\tag{1}
```

and the corresponding coefficients formed from

```math
B(x)=\frac1x\operatorname{rev}(xA(x))
\tag{2}
```

satisfy a `p^(3k)` adjacent tower.  This note proves that the two apparently
different conjectures are instances of one signed binomial kernel.

## 1. The algebraic series

The defining reversion on the OEIS page implies that, if
`Y=xA(x^2)`, then

```math
Y=x\frac{(1+Y^2)^2}{1-Y^2}.
```

Putting `W=Y^2` gives

```math
W=x\Phi(W),
\qquad
\Phi(t)=\frac{(1+t)^4}{(1-t)^2},
\qquad
A(x)^2=\Phi(W).
\tag{3}
```

For integers `q`, positive `s,n`, define

```math
K_{q,s}(n)
=[t^{sn}]
\left(\frac{(1+t)^2}{1-t}\right)^{qn}.
\tag{4}
```

Generalized binomial expansion makes this a finite exact computation:

```math
K_{q,s}(n)=
\sum_{j=0}^{sn}
\binom{2qn}{j}
\binom{qn+sn-j-1}{sn-j}.
\tag{5}
```

Formula (5) is valid for negative `q` under the usual integral extension of
binomial coefficients.

## 2. Direct powers

The Lagrange identity

```math
\operatorname{coeff}_{x^m}(W/x)^\alpha
=\frac{\alpha}{m+\alpha}[t^m]\Phi(t)^{m+\alpha}
\tag{6}
```

applied with `m=sn` and `alpha=rn/2` proves the following.

### Theorem 1

If `r+2s` is nonzero, then

```math
\boxed{
u_{r,s}(n)=
\frac{r}{r+2s}K_{r+2s,s}(n).
}
\tag{7}
```

The singular slope is not an omission.  Taking the Lagrange limit, or
differentiating `log Phi`, gives

```math
u_{-2s,s}(n)=4(-1)^{sn}-2.
\tag{8}
```

The case `r=0` is identically zero at every positive requested coefficient.

## 3. Reverted powers

Let `Z=xB(x)`.  By (2), `ZA(Z)=x`, so

```math
Z=\frac{x}{A(Z)}.
\tag{9}
```

One application of Lagrange inversion gives

```math
[x^{sn}]B(x)^{rn}
=\frac{r}{r+s}[t^{sn}]A(t)^{-(r+s)n}.
\tag{10}
```

Applying (7), now to the power `-(r+s)n`, yields the second family.

### Theorem 2

If `s-r` is nonzero, then

```math
\boxed{
[x^{sn}]B(x)^{rn}
=-\frac{r}{s-r}K_{s-r,s}(n).
}
\tag{11}
```

At the singular slope `r=s`, equations (8) and (10) give the exact formula

```math
[x^{sn}]B(x)^{sn}=2(-1)^{sn}-1.
\tag{12}
```

Thus both singular slopes satisfy every odd-prime adjacent tower by literal
equality.

## 4. The one remaining arithmetic statement

For a nonzero integer `m`, write `v_p(m)` for its `p`-adic valuation.
Equations (7) and (11) show that the direct A079489 conjecture is equivalent
to

```math
v_p\bigl(K_{r+2s,s}(np^k)-K_{r+2s,s}(np^{k-1})\bigr)
\ge 3k+v_p(r+2s)-v_p(r),
\tag{13}
```

and the reverted conjecture is equivalent to

```math
v_p\bigl(K_{s-r,s}(np^k)-K_{s-r,s}(np^{k-1})\bigr)
\ge 3k+v_p(s-r)-v_p(r).
\tag{14}
```

The integrality of (1) and its reverted analogue guarantees the final
expressions are integral, but it does not allow the displayed prefactors to
be discarded when `p` divides their denominators.

It is therefore enough to prove the single normalized kernel statement

```math
\boxed{
v_p\bigl(K_{q,s}(np^k)-K_{q,s}(np^{k-1})\bigr)
\ge 3k+v_p(q)-v_p(q-2s)
}
\tag{15}
```

for the direct family, and the same estimate after the substitution
`q=s-r` for the reverted family.  More symmetrically, the exact remaining
obligation is

```math
v_p\left(
\frac{c}{q}
\bigl(K_{q,s}(np^k)-K_{q,s}(np^{k-1})\bigr)
\right)\ge3k,
\tag{16}
```

for the two parameter maps `(q,c)=(r+2s,r)` and `(s-r,-r)`.

The mixed-step theorem elsewhere in this repository supplies a uniform
quadratic layer for closely related coefficients.  It does not supply the
third power in (16); that extra cancellation is the genuine remaining
problem.

## 5. Exact verification

[`verify_a079489_lagrange_kernel.py`](../verification/related/verify_a079489_lagrange_kernel.py)
checks:

1. the OEIS formula for `A(x)` against the algebraic equation (3);
2. (7) against direct formal-series powers, including negative exponents;
3. (11) against an independently iterated series-reversion equation;
4. both singular-slope formulas;
5. integrality throughout the tested parameter box; and
6. the normalized valuation statement (16) at sampled first and second
   levels, including denominator-prime cases and sharp examples.

These checks prove no unbounded valuation estimate.  They make the
reduction reproducible and ensure that the exceptional prefactors have not
been silently treated as units.

## 6. Source boundary

- The two conjectured families and prime range are from
  [OEIS A079489](https://oeis.org/A079489).
- Lagrange inversion and generalized binomial expansion are classical.
- No literature source located in the campaign proves (16) for all integral
  parameters, and no priority claim is made for the reduction.
