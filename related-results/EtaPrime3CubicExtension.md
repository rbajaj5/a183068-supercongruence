# A cubic two-term supercongruence for the $(\eta)$ sequence at $p=3$

**Status:** complete unchecked proof draft, 2026-07-25.

## 1. Result

For an integer $a$ and $j\ge0$, use the polynomial extension

```math
\binom aj=(-1)^j\binom{j-a-1}{j}\qquad(a<0).
```

Define

```math
Z(n)=\sum_{k=0}^{n}A(n,k),
```

where

```math
A(n,k)=(-1)^k\binom nk^3
\left(
\binom{4n-5k-1}{3n}+
\binom{4n-5k}{3n}
\right).
\qquad\text{(1)}
```

This is the sporadic Apéry-like sequence labeled $(\eta)$, up to the
customary harmless normalization by $2$.

### Theorem

For every $m,r\ge1$,

```math
Z(m3^r)\equiv Z(m3^{r-1})\pmod {3^{3r}}.
\qquad\text{(2)}
```

Osburn--Sahu--Straub proved the corresponding cubic congruence for primes
$p\ge5$.  Straub later observed that the arguments in the literature at
$p=3$ give the uniform modulus $3^{2r}$.  The extra power in (2) does
not appear to have been recorded in the sources found so far.

## 2. The scaling input

We use the $p=3$ form of the generalized Jacobsthal congruence.  For
integers $a,b$ and positive $u,v$, whenever the quotient is defined,

```math
\frac{\binom{3^u a}{3^v b}}
     {\binom{3^{u-1}a}{3^{v-1}b}}
\equiv1
\pmod {3^{\,u+v+\min(u,v)-1}}.
\qquad\text{(3)}
```

The version for negative upper entries is part of the standard generalized
statement used by Osburn--Sahu--Straub.

The elementary observation that recovers the lost power is

```math
Q\equiv1\pmod {3^e}
\quad\Longrightarrow\quad
Q^3\equiv1\pmod {3^{e+1}}.
\qquad\text{(4)}
```

Indeed, write $Q=1+3^e t$ and expand the cube.

## 3. The bracket has a scale-invariant prefactor

Put

```math
H(n,k)=
\binom{4n-5k-1}{3n}+
\binom{4n-5k}{3n},
\qquad X=4n-5k.
```

If $X\ne0$, Pascal's adjacent-binomial identity gives

```math
H(n,k)=
\frac{5(n-2k)}{4n-5k}\binom{4n-5k}{3n}.
\qquad\text{(5)}
```

The rational prefactor is unchanged when $(n,k)$ is replaced by
$(3n,3k)$.  Consequently, away from the zero cases,

```math
\frac{H(3n,3k)}{H(n,k)}
=
\frac{\binom{3(4n-5k)}{9n}}
     {\binom{4n-5k}{3n}}.
\qquad\text{(6)}
```

If $0<X<3n$, both brackets vanish and there is nothing to prove.  If
$X=0$, then

```math
H(n,k)=\binom{-1}{3n}=(-1)^n,
```

which is also unchanged by scaling by $3$.  Thus (6) may safely be used
in every nontrivial case.

## 4. Termwise scaling

It is enough to assume $3\nmid m$.  If $m=3^t m_0$, applying the result
for $m_0$ at exponent $r+t$ gives a congruence stronger than (2).

Set

```math
N=m3^r,\qquad K=3^s h,\qquad 3\nmid h,\quad s\ge1.
```

Compare $A(N,K)$ with $A(N/3,K/3)$.  The signs agree because division
by $3$ preserves parity.  The ratio of the nonzero magnitudes is

```math
R=Q_1^3Q_2,
\qquad\text{(7)}
```

where

```math
Q_1=
\frac{\binom NK}{\binom{N/3}{K/3}},
\qquad
Q_2=
\frac{\binom{4N-5K}{3N}}
     {\binom{(4N-5K)/3}{N}}.
\qquad\text{(8)}
```

We show that the difference of the two terms is divisible by $3^{3r}$.

### Case 1: $s<r$

Congruence (3) gives

```math
v_3(Q_1-1)\ge r+2s-1,
```

so (4) gives

```math
v_3(Q_1^3-1)\ge r+2s.
\qquad\text{(9)}
```

Because

```math
v_3(4N-5K)=s
```

in this case, (3) applied to $Q_2$ also gives

```math
v_3(Q_2-1)\ge r+2s.
\qquad\text{(10)}
```

Hence $v_3(R-1)\ge r+2s$.  On the other hand,

```math
v_3\binom{N/3}{K/3}\ge r-s,
\qquad\text{(11)}
```

using

```math
\binom ab=\frac ab\binom{a-1}{b-1}.
```

The cube in (1) therefore supplies $3(r-s)$ additional powers.  Thus

```math
v_3\bigl(A(N,K)-A(N/3,K/3)\bigr)
\ge (r+2s)+3(r-s)
=4r-s\ge3r.
\qquad\text{(12)}
```

### Case 2: $s=r$

Here (3) initially gives only

```math
Q_1\equiv1\pmod {3^{3r-1}},
```

but the quotient occurs cubed.  Equation (4) therefore gives

```math
Q_1^3\equiv1\pmod {3^{3r}}.
\qquad\text{(13)}
```

Also $3^r\mid4N-5K$, while the lower entry $3N$ is divisible by
$3^{r+1}$.  Congruence (3) gives

```math
Q_2\equiv1\pmod {3^{3r}}.
\qquad\text{(14)}
```

Therefore $R\equiv1\pmod {3^{3r}}$.

### Case 3: $s>r$

Now

```math
v_3(Q_1-1)\ge2r+s-1\ge3r.
```

Moreover $v_3(4N-5K)=r$, so (3) again gives

```math
Q_2\equiv1\pmod {3^{3r}}.
```

The desired termwise congruence follows.  The case $K=0$ is the same
calculation with $Q_1=1$.

We have proved

```math
A(m3^r,3\ell)\equiv A(m3^{r-1},\ell)
\pmod {3^{3r}}
\qquad\text{(15)}
```

for every $\ell$.

## 5. The discarded stratum

If $3\nmid k$, then

```math
\binom{m3^r}{k}
=\frac{m3^r}{k}\binom{m3^r-1}{k-1}
```

is divisible by $3^r$.  Its cube in (1) therefore implies

```math
A(m3^r,k)\equiv0\pmod {3^{3r}}.
\qquad\text{(16)}
```

Split the sum for $Z(m3^r)$ according as $3\mid k$, use (15) on the
first part and (16) on the second.  The surviving indices are in bijection
with the indices of $Z(m3^{r-1})$, proving (2).

## 6. Verification and provenance

Run

```text
python verification/related/verify_eta_prime3.py
```

The script:

- checks the binomial formula against the recurrence
  ```math
  (n+1)^3z_{n+1}
  =(2n+1)(11n^2+11n+5)z_n-125n^3z_{n-1};
  ```
- checks the two termwise congruences in the proof over a finite grid; and
- verifies (2) exactly for every admissible pair with $m3^r\le10,000$.

The last test contains 4,996 exact congruences, and the exponent $3r$ is
attained.

Primary sources:

1. R. Osburn, B. Sahu, and A. Straub,
   *Supercongruences for sporadic sequences*,
   <https://arxiv.org/abs/1312.2195>, especially Example 3.1.
2. A. Straub, *Gessel--Lucas congruences for sporadic sequences*,
   <https://arxiv.org/abs/2301.12248>.

The argument and the literature claim require independent specialist review.
