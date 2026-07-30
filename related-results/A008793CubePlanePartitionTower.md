# The A008793 cube-plane-partition tower

**Status:** complete elementary proof candidate for the full all-prime
$p^{4r}$ conjecture

## 1. Statement

Let

**(1)** $\displaystyle A(N)=\prod_{i,j=1}^{N}
\frac{N+i+j-1}{i+j-1}$.

This is [OEIS A008793](https://oeis.org/A008793), the number of plane
partitions contained in an $N$-cube.  The source page conjectures that,
for every prime $p$ and positive integers $n,r$,

**(2)** $A(np^r)\equiv A(np^{r-1})^p\pmod {p^{4r}}$.

We prove (2).  The proof has three ingredients: exact complementary-factor
pairing, a reduced-residue reciprocal-block lemma, and a separate binary
parity argument.

## 2. Exact complementary-factor pairing

The multiplicity of $s=i+j-1$ in (1) is

**(3)** $\mu_N(s)=s$ for $1\le s\le N$, while
$\mu_N(s)=2N-s$ for $N<s\le2N-1$.

Pairing $s$ with $2N-s$ gives

**(4)** $A(N)=2^N P(N)$,

where

**(5)** $\displaystyle P(N)=
\prod_{s=1}^{N-1}
\left(1+\frac{3N^2}{s(2N-s)}\right)^s$.

Indeed, the paired factor is exactly

**(6)** $\displaystyle
\frac{N+s}{s}\frac{3N-s}{2N-s}
=1+\frac{3N^2}{s(2N-s)}$.

Now replace $N$ by $pN$ in (5).  The factors with $p\mid s$, after writing
$s=pt$, are exactly the factors of $P(N)^p$.  Therefore

**(7)** $A(pN)=A(N)^p U_p(N)$,

with

**(8)** $\displaystyle U_p(N)=
\prod_{\substack{1\le s<pN\\p\nmid s}}
\left(1+\frac{3p^2N^2}{s(2pN-s)}\right)^s$.

Thus the nonlinear comparison in (2) is not mysterious: it removes an
exact copy of the preceding product, leaving only a unit block.

## 3. Reciprocal-block estimates

### Lemma 1: odd primes

Put $q=p^r$.  If $p\ge3$ and $c$ is any integer, then

**(9)** $\displaystyle
\sum_{\substack{1\le u<q\\p\nmid u}}\frac1{cq+u}
\equiv0\pmod {p^{2r-\epsilon_p}}$,

where $\epsilon_3=1$ and $\epsilon_p=0$ for $p\ge5$.

### Proof

Inversion permutes the units modulo $q$.  Hence the reciprocal-square
sum has the same residue as the ordinary square sum.  The elementary
formula for sums of squares gives

**(10)** $\displaystyle
v_p\left(\sum_{\substack{1\le u<q\\p\nmid u}}\frac1{u^2}\right)
\ge r-\epsilon_p$.

Pairing $u$ with $q-u$ contributes one additional factor $q$ to the
reciprocal sum.  Replacing $u$ by $cq+u$ changes the sum first by
$-cq$ times the reciprocal-square sum; all later terms contain $q^2$.
This proves (9). $\square$

### Lemma 2: the binary block

For $t\ge0$, $q=2^{t+1}$, and every integer $c$,

**(11)** $\displaystyle
\sum_{a=0}^{2^t-1}\frac1{cq+2a+1}
\equiv0\pmod {2^{2t}}$.

### Proof

The case $t=0$ is immediate.  For $t\ge1$, pair $a$ with
$2^t-1-a$.  Each pair has numerator an odd multiple of $q$.  Modulo
$2^{t-1}$, the remaining inverse products are negatives of inverse
squares of all odd residue classes modulo $2^t$.  Inversion permutes
these classes.  The elementary identity

$\displaystyle
\sum_{a=0}^{2^{t-1}-1}(2a+1)^2
=4\sum_{a=0}^{2^{t-1}-1}a^2
+4\sum_{a=0}^{2^{t-1}-1}a+2^{t-1}$

then gives

**(12)** $\displaystyle
\sum_{a=0}^{2^{t-1}-1}(2a+1)^2
\equiv0\pmod {2^{t-1}}$.

The factor $q$ and (12) give $2^{t+1+t-1}=2^{2t}$. $\square$

## 4. Odd primes

Fix an odd prime $p$ and put $N=np^{r-1}$.  In (8), write

**(13)** $\displaystyle x_s=\frac{3p^2N^2}{s(2pN-s)}$.

For $p\ge5$, $v_p(x_s)\ge2r$; for $p=3$,
$v_3(x_s)\ge2r+1$.  The first term in the $p$-adic logarithm of (8) is

**(14)** $\displaystyle
3p^2N^2
\sum_{\substack{1\le s<pN\\p\nmid s}}\frac1{2pN-s}$.

The denominators in (14) occupy $n$ consecutive reduced-residue blocks
of length $p^r$.  Lemma 1 gives valuation at least $2r$ for $p\ge5$
and $2r-1$ for $p=3$.  Including the prefactor, (14) is divisible by
$p^{4r}$.

For every logarithmic term of degree $k\ge2$, the valuation is at least

**(15)** $2rk-v_p(k)\ge4r$ for $p\ge5$,

or

**(16)** $k(2r+1)-v_3(k)\ge4r$ for $p=3$.

Consequently

**(17)** $U_p(N)\equiv1\pmod {p^{4r}}$ for odd $p$.

Equations (7) and (17) prove (2) at every odd prime.

## 5. The binary prime

Write $N=2^t m$ with $m$ odd.  Equation (8) becomes

**(18)** $\displaystyle U_2(N)=
\prod_{\substack{1\le s<2N\\s\text{ odd}}}
\left(1+\frac{12N^2}{s(4N-s)}\right)^s$.

Each logarithmic variable has valuation $2t+2$.  The linear term is

**(19)** $\displaystyle
12N^2\sum_{\substack{1\le s<2N\\s\text{ odd}}}\frac1{4N-s}$.

The denominators in (19) split into $m$ blocks of the form in Lemma 2.
Therefore its valuation is at least

**(20)** $(2t+2)+2t=4t+2$.

Every logarithmic term of degree $k\ge2$ has valuation at least

**(21)** $k(2t+2)-v_2(k)\ge4t+3$.

The $2$-adic logarithm is an isometry on $1+4\mathbb Z_2$, so

**(22)** $U_2(N)\equiv1\pmod {2^{4t+2}}$.

There are two apparently missing powers in (22).  They come from the
preceding-level count itself.

### Lemma 3

$A(N)$ is even for every $N\ge1$.

### Proof

Let

**(23)** $\displaystyle D(M)=\sum_{j=0}^{M-1}s_2(j)$,

where $s_2$ is the binary digit sum.  From

**(24)** $\displaystyle
A(N)=\frac{H(N)^3H(3N)}{H(2N)^3}$, where
$\displaystyle H(N)=\prod_{k=1}^{N-1}k!$,

and Legendre's formula,

**(25)** $v_2(A(N))=3D(N)+3N-D(3N)$.

The identity $D(2M)=2D(M)+M$ gives

**(26)** $v_2(A(2M))=2v_2(A(M))$.

It remains to consider odd $M$.  Complementation is a fixed-point-free
involution on plane partitions in an $M$-cube: a fixed point would have
volume $M^3/2$, impossible when $M$ is odd.  Thus $A(M)$ is even.
Repeatedly applying (26) proves the lemma. $\square$

Finally, (7), (22), and Lemma 3 give

**(27)** $\displaystyle
v_2\left(A(2N)-A(N)^2\right)\ge2+(4t+2)=4t+4$.

For $N=n2^{r-1}$, $t\ge r-1$, so (27) is at least $4r$.  This proves
(2) at $p=2$ and completes the all-prime theorem.

## 6. Exact checks and provenance

The checker:

1. reproduces the initial A008793 values;
2. verifies the exact paired-product and block decomposition;
3. checks both reciprocal-block lemmas;
4. verifies the binary digit-sum valuation formula and doubling law;
5. checks the exact valuation of the residual unit product; and
6. tests the full conjecture for many $(p,n,r)$.

Run:

```text
python verification/related/verify_a008793_cube_plane_partitions.py
```

The named conjecture and product formulas come from the live OEIS page.
The plane-partition interpretation and the standard complementation
operation are also reviewed by
[Amdeberhan--Moll](https://doi.org/10.37236/1997). The reduced-residue
estimates are elementary Wolstenholme-type block calculations. A targeted
search found no matching proof of (2), but no literature-priority claim is
made here.
