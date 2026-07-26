# Reduction of the binary $s_{18}$ supercongruence

**Status:** incomplete unchecked research note, 2026-07-25.

Osburn--Sahu--Straub conjecture that, for $m\ge2$ and $r\ge1$,

```math
s_{18}(m2^r)\equiv s_{18}(m2^{r-1})
\pmod {2^{2r+3}}.
\qquad\text{(1)}
```

Their published theorem gives $2^{2r}$.

Write their summand as

```math
D(n,k)=(-1)^k\binom nk^2S(n-k,k)H(n,k),
\qquad\text{(2)}
```

where

```math
S(a,b)=\frac{(2a)!(2b)!}{a!b!(a+b)!}
```

is a super Catalan number and

```math
H(n,k)=
\binom{2n-3k-1}{n}+\binom{2n-3k}{n}.
```

## 1. An exact digit identity

Legendre's formula gives the unexpectedly simple identity

```math
v_2(S(a,b))=s_2(a+b),
\qquad\text{(3)}
```

where $s_2$ is the number of ones in the binary expansion.  In particular,

```math
v_2(S(n-k,k))=s_2(n)
\qquad\text{(4)}
```

is independent of $k$.

After absorbing powers of two into $r$, the nontrivial case of (1) has
$m$ odd and $m\ge3$, hence $s_2(m)\ge2$.

## 2. Odd indices already have the conjectured valuation

Let $n=m2^r$ with odd $m\ge3$, and let $k$ be odd.  Then

```math
v_2\binom nk\ge r.
```

The bracket $H(n,k)$ is even.  Using (2)--(4),

```math
v_2(D(n,k))
\ge2r+s_2(m)+1
\ge2r+3.
\qquad\text{(5)}
```

Thus every term discarded by the map $k\mapsto2k$ vanishes individually
at the full conjectured modulus.

This bound is sharp: exact examples attain $2r+3$.

## 3. The remaining scaling lemma

It remains to prove

```math
D(m2^r,2\ell)\equiv D(m2^{r-1},\ell)
\pmod {2^{2r+3}}.
\qquad\text{(6)}
```

Exact testing is substantially stronger:

```math
v_2\!\left(
D(m2^r,2\ell)-D(m2^{r-1},\ell)
\right)\ge3r+2
\qquad\text{(7)}
```

through the tested range for odd $m$.

The bracket has the useful form

```math
H(n,k)=
\frac{3(n-2k)}{2n-3k}\binom{2n-3k}{n},
\qquad\text{(8)}
```

so its rational prefactor is invariant under simultaneous doubling.  The
scaling quotient is consequently a product of ordinary binomial and
super-Catalan scaling quotients.  Experiments indicate the precise estimate

```math
v_2\!\left(R-(-1)^\ell\right)
\ge r+1+2v_2(\ell),
\qquad\text{(9)}
```

where $R$ is the quotient of the unsigned magnitudes.  Combining (9) with
the two copies of $\binom nk$ and the exact digit identity (3) yields (7).

Equation (9), including its sign, is the sole unresolved lemma in this
draft.  It is a sharpened product version of the binary Jacobsthal
congruence used in the published proof.

### Why a factor-by-factor bound does not immediately prove (9)

The factorization

```math
S(a,b)=
\frac{\binom{2a}{a}\binom{2b}{b}}{\binom{a+b}{a}}
```

is useful, but a tempting signed-Jacobsthal estimate for each individual
factor is one power too strong. For example, take

```math
(m,r,\ell)=(3,2,1).
```

The ordinary binomial quotient coming from (8) is

```math
\frac{\binom{18}{12}}{\binom96}=221.
```

However,

```math
v_2(221-1)=2,\qquad v_2(221+1)=1,
```

whereas the proposed individual-factor exponent
$r+1+2v_2(\ell)$ is $3$. Thus no choice of sign makes this factor congruent
to $\pm1$ modulo $2^3$.

The full product in (9) may still gain the missing power through the squared
binomial factor or cancellation among factor errors. What fails is the claim
that the desired exponent follows from the $H$-binomial quotient by itself.
The unresolved content is therefore valuation interaction as well as sign
bookkeeping.

## 4. Exact evidence

The sequence recurrence was evaluated exactly through $n=5,000$.
All 4,979 admissible instances of (1) passed.  The minimum slack was zero,
with equality for

```math
(m,r)=(5,1),(9,1),(17,1),(33,1),(65,1),\ldots.
```

The other three small-prime conjectures in the same paper also passed:

- $s_7(m2^r)$ modulo $2^{3r+2}$;
- $s_7(m3^r)$ modulo $3^{3r}$; and
- $s_{18}(m3^r)$ modulo $3^{3r-1}$.

All four advertised exponents are attained, so none is merely a loose
numerical lower bound.  Unlike (1), the other three targets exhibit
termwise failures and require cancellation between summands.

Source: R. Osburn, B. Sahu, and A. Straub,
*Supercongruences for sporadic sequences*,
<https://arxiv.org/abs/1312.2195>, equations (15)--(18).
