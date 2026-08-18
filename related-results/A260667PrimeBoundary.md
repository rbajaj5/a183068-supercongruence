# The A260667 prime-boundary congruence

**Status:** complete elementary proof candidate; exact checks supplied;
literature priority not searched beyond the source record

The [OEIS A260667](https://oeis.org/A260667) page defines

```math
S(k,x)=\sum_{j=0}^k\binom{k}{j}\binom{x}{j}\binom{x+j}{j}
```

and

```math
a(n)=\frac1{n^2}\sum_{k=0}^{n-1}(2k+1)S(k,n)^2.
```

It conjectures that

```math
a(p-1)\equiv1\pmod {p^3}
```

for every prime `p >= 5`. This note proves that congruence directly.

## Theorem

For every prime `p >= 5`,

```math
a(p-1)\equiv1\pmod {p^3}.
```

The proof takes place in the localization of the integers at `p`. The
denominator `(p-1)^2` is a unit there, so no global integrality assertion is
needed for the congruence.

## 1. The local binomial expansion

Fix `0 <= k <= p-2`. For `1 <= j <= k`, exact product pairing gives

```math
\begin{aligned}
\binom{p-1}{j}\binom{p-1+j}{j}
&=(-1)^j\frac pj\left(1-\frac pj\right)
  \prod_{t=1}^{j-1}\left(1-\frac{p^2}{t^2}\right)\\
&\equiv(-1)^j\left(\frac pj-\frac{p^2}{j^2}\right)
  \pmod {p^3}.
\end{aligned}
```

All denominators here are `p`-adic units. The standard finite-binomial
identities

```math
\sum_{j=1}^k(-1)^j\binom{k}{j}\frac1j=-H_k,
```

and

```math
\sum_{j=1}^k(-1)^j\binom{k}{j}\frac1{j^2}
=-\frac{H_k^2+H_k^{(2)}}2
```

therefore imply

```math
S(k,p-1)\equiv
1-pH_k+\frac{p^2}{2}\left(H_k^2+H_k^{(2)}\right)
\pmod {p^3}.
```

Squaring gives

```math
S(k,p-1)^2\equiv
1-2pH_k+p^2\left(2H_k^2+H_k^{(2)}\right)
\pmod {p^3}.
\tag{1}
```

## 2. Two weighted harmonic sums

Put `n=p-2` and

```math
A_n=\sum_{k=0}^n(2k+1)H_k,
\qquad
B_n=\sum_{k=0}^n(2k+1)\left(2H_k^2+H_k^{(2)}\right).
```

Interchanging the order of summation yields the exact identity

```math
A_n=(n+1)^2H_n-\frac{n(n+1)}2.
```

Wolstenholme's congruence `H_(p-1) = 0 mod p^2` then gives

```math
A_{p-2}\equiv-\frac{p(p-1)}2\pmod {p^2}.
\tag{2}
```

For the quadratic term, write

```math
C_n=\sum_{k=0}^n(2k+1)H_k^{(2)},
\qquad
D_n=\sum_{k=0}^n(2k+1)H_k^2.
```

Another order reversal and one summation by parts give

```math
C_n=(n+1)^2H_n^{(2)}-n
```

and

```math
D_n=(n+1)^2H_n^2-n(n+1)H_{n-1}
    +\frac{(n-2)(n+1)}2.
```

Using `H_(p-1)^(2) = 0 mod p` and removing the last one or two terms from
the complete harmonic sums gives

```math
H_{p-2}\equiv1,
\qquad
H_{p-3}\equiv\frac32,
\qquad
H_{p-2}^{(2)}\equiv-1
\pmod p.
```

Consequently

```math
C_{p-2}\equiv1,
\qquad
D_{p-2}\equiv0,
\qquad
B_{p-2}=2D_{p-2}+C_{p-2}\equiv1
\pmod p.
\tag{3}
```

## 3. Completion

Summing (1), using

```math
\sum_{k=0}^{p-2}(2k+1)=(p-1)^2,
```

and then applying (2)--(3), we obtain

```math
\begin{aligned}
(p-1)^2a(p-1)
&\equiv(p-1)^2-2pA_{p-2}+p^2B_{p-2}\\
&\equiv(p-1)^2+p^2(p-1)+p^2\\
&\equiv(p-1)^2\pmod {p^3}.
\end{aligned}
```

Since `(p-1)^2` is invertible modulo `p^3`, the theorem follows.

## Verification

Run

```text
python verification/related/verify_a260667_prime_boundary.py
```

The checker compares the two exact formulas for the sequence, checks the
local binomial-harmonic expansion, verifies both weighted harmonic
congruences, and tests the claimed boundary through `p=97`. Computation is
used only as a transcription and regression check for the proof above.

