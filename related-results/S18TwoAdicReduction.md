# Reduction of the binary $s_{18}$ supercongruence

**Status:** incomplete unchecked research note, 2026-07-25.

Osburn--Sahu--Straub conjecture that, for $m\ge2$ and $r\ge1$,

$$
s_{18}(m2^r)\equiv s_{18}(m2^{r-1})
\pmod {2^{2r+3}}.
\tag{1}
$$

Their published theorem gives $2^{2r}$.

Write their summand as

$$
D(n,k)=(-1)^k\binom nk^2S(n-k,k)H(n,k),
\tag{2}
$$

where

$$
S(a,b)=\frac{(2a)!(2b)!}{a!b!(a+b)!}
$$

is a super Catalan number and

$$
H(n,k)=
\binom{2n-3k-1}{n}+\binom{2n-3k}{n}.
$$

## 1. An exact digit identity

Legendre's formula gives the unexpectedly simple identity

$$
v_2(S(a,b))=s_2(a+b),
\tag{3}
$$

where $s_2$ is the number of ones in the binary expansion.  In particular,

$$
v_2(S(n-k,k))=s_2(n)
\tag{4}
$$

is independent of $k$.

After absorbing powers of two into $r$, the nontrivial case of (1) has
$m$ odd and $m\ge3$, hence $s_2(m)\ge2$.

## 2. Odd indices already have the conjectured valuation

Let $n=m2^r$ with odd $m\ge3$, and let $k$ be odd.  Then

$$
v_2\binom nk\ge r.
$$

The bracket $H(n,k)$ is even.  Using (2)--(4),

$$
v_2(D(n,k))
\ge2r+s_2(m)+1
\ge2r+3.
\tag{5}
$$

Thus every term discarded by the map $k\mapsto2k$ vanishes individually
at the full conjectured modulus.

This bound is sharp: exact examples attain $2r+3$.

## 3. The remaining scaling lemma

It remains to prove

$$
D(m2^r,2\ell)\equiv D(m2^{r-1},\ell)
\pmod {2^{2r+3}}.
\tag{6}
$$

Exact testing is substantially stronger:

$$
v_2\!\left(
D(m2^r,2\ell)-D(m2^{r-1},\ell)
\right)\ge3r+2
\tag{7}
$$

through the tested range for odd $m$.

The bracket has the useful form

$$
H(n,k)=
\frac{3(n-2k)}{2n-3k}\binom{2n-3k}{n},
\tag{8}
$$

so its rational prefactor is invariant under simultaneous doubling.  The
scaling quotient is consequently a product of ordinary binomial and
super-Catalan scaling quotients.  Experiments indicate the precise estimate

$$
v_2\!\left(R-(-1)^\ell\right)
\ge r+1+2v_2(\ell),
\tag{9}
$$

where $R$ is the quotient of the unsigned magnitudes.  Combining (9) with
the two copies of $\binom nk$ and the exact digit identity (3) yields (7).

Equation (9), including its sign, is the sole unresolved lemma in this
draft.  It is a sharpened product version of the binary Jacobsthal
congruence used in the published proof.

## 4. Exact evidence

The sequence recurrence was evaluated exactly through $n=5,000$.
All 4,979 admissible instances of (1) passed.  The minimum slack was zero,
with equality for

$$
(m,r)=(5,1),(9,1),(17,1),(33,1),(65,1),\ldots.
$$

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
