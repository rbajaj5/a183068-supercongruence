# The one-step cubic congruence for A362676

**Status:** complete proof of the full `r=1` layer; the higher adjacent
levels remain open; priority provisional

Let

```math
F(N)=\sum_{k=0}^{N}4^{N-k}\binom Nk\binom{N-1}{k}\binom{2k}{k},
```

the sequence [A362676](https://oeis.org/A362676).  The OEIS entry conjectures

```math
F(np^r)\equiv F(np^{r-1})\pmod {p^{3r}}
\tag{1}
```

for primes `p>=5`.  The prime-point case `n=r=1` was proved in the
[prime-boundary note](A362676PrimeBoundary.md).  Here the same level is
proved uniformly in `n`.

## Theorem

For every prime `p>=5` and every positive integer `n`,

```math
\boxed{F(np)\equiv F(n)\pmod {p^3}.}
\tag{2}
```

The proof has two independent parts.  Terms whose index is divisible by
`p` contract term by term.  Every complete nonzero residue block vanishes
modulo `p^3`; the last cancellation is exactly

```math
\sum_{b=1}^{(p-1)/2}\frac1{b^2}\equiv0\pmod p.
```

## 1. A positive convolution form

Put

```math
A_N(k)=\binom{N+k-1}{k}
       \binom{2(N-k)}{N-k}\binom{2k}{k}.
\tag{3}
```

### Lemma 1

For every positive integer `N`,

```math
F(N)=\sum_{k=0}^{N}A_N(k).
\tag{4}
```

### Proof

The defining sum is

```math
F(N)=4^N\,{}_3F_2\!\left(
\begin{matrix}-N,1-N,1/2\\1,1\end{matrix};1\right).
```

Use the terminating transformation

```math
{}_3F_2\!\left(
\begin{matrix}-N,a,b\\c,d\end{matrix};1\right)
=\frac{(d-b)_N}{(d)_N}
{}_3F_2\!\left(
\begin{matrix}-N,c-a,b\\c,1+b-d-N\end{matrix};1\right).
\tag{5}
```

Identity (5) follows by expanding the finite sums and applying the
Chu--Vandermonde identity; no convergence assertion is needed.  Taking
`a=1-N`, `b=1/2`, and `c=d=1` gives

```math
F(N)=4^N\frac{(1/2)_N}{N!}
{}_3F_2\!\left(
\begin{matrix}-N,N,1/2\\1,1/2-N\end{matrix};1\right).
```

For `0<=k<=N`,

```math
\frac{(1/2)_{N-k}}{(N-k)!}
=\frac{(1/2)_N}{N!}\frac{(-N)_k}{(1/2-N)_k}.
```

Consequently the `k`-th term of the last hypergeometric sum is precisely

```math
4^N\frac{(N)_k}{k!}\frac{(1/2)_k}{k!}
\frac{(1/2)_{N-k}}{(N-k)!}=A_N(k),
```

using `binom(2m,m)=4^m(1/2)_m/m!`.  This proves (4). QED

## 2. Three local binomial facts

Fix a prime `p>=5` and put `h=(p-1)/2`.

First, the Jacobsthal unit-product argument gives, for integers `a>=1`
and `0<=b<a`,

```math
\binom{pa-1}{pb}\equiv\binom{a-1}{b}\pmod {p^3}.
\tag{6}
```

Indeed, after separating the factors with index divisible by `p`, the
quotient of the two sides is

```math
\prod_{\substack{1\le i\le pb\\p\nmid i}}
\left(1-\frac{pa}{i}\right).
```

The reciprocal sums of first and second powers over these units vanish
modulo `p^2` and `p`, respectively.  Expanding the product therefore gives
`1` modulo `p^3`.  The same argument supplies the familiar congruence

```math
\binom{pa}{pb}\equiv\binom ab\pmod {p^3}.
\tag{7}
```

The two formulas needed for a nonzero residue are as follows.  For
`a>=0` and `1<=b<=h`, Lucas' theorem gives

```math
\binom{2(ap+b)}{ap+b}
\equiv\binom{2a}{a}\binom{2b}{b}\pmod p.
\tag{8}
```

For `a>=1`, removing the unique unit-digit carry gives

```math
\frac1p\binom{2(ap-b)}{ap-b}
\equiv-\frac{a\binom{2a}{a}}
 {b\binom{2b}{b}}\pmod p.
\tag{9}
```

For completeness, divide

```math
\binom{2ap-2b}{ap-b}
=\binom{2ap}{ap}
\frac{\left((ap)^{\underline b}\right)^2}
     {(2ap)^{\underline {2b}}}
```

by `p`.  Only the initial factor of each falling factorial is divisible
by `p`.  Reduction modulo `p`, followed by (7), gives (9).

## 3. The nonzero residue blocks

Let `N=np`.  For `0<=j<n`, define the complete block

```math
B_j=\sum_{b=1}^{p-1}A_N(jp+b).
\tag{10}
```

### Lemma 2

Every block in (10) satisfies

```math
B_j\equiv0\pmod {p^3}.
\tag{11}
```

### Proof

For `1<=b<=p-1`, the first binomial factor in (3) satisfies

```math
\frac1p\binom{(n+j)p+b-1}{jp+b}
\equiv\frac nb\binom{n+j}{j}\pmod p.
\tag{12}
```

This follows from

```math
\binom{N+k-1}{k}=\frac{N}{N+k}\binom{N+k}{k}
```

and Lucas' theorem.

For `1<=b<=h`, apply (8) to `k=jp+b` and (9) to
`N-k=(n-j)p-b`.  After the central binomial factors cancel,

```math
\frac{A_N(jp+b)}{p^2}
\equiv-\frac{C_j^-}{b^2}\pmod p,
\tag{13}
```

where

```math
C_j^-=n(n-j)\binom{n+j}{j}
       \binom{2j}{j}\binom{2(n-j)}{n-j}.
```

For the upper half write `b=p-c`, with `1<=c<=h`.  Now (9) applies to
`k=(j+1)p-c`, while (8) applies to
`N-k=(n-j-1)p+c`.  Equation (12), with `b==-c (mod p)`, yields

```math
\frac{A_N(jp+p-c)}{p^2}
\equiv\frac{C_j^+}{c^2}\pmod p,
\tag{14}
```

where

```math
C_j^+=n(j+1)\binom{n+j}{j}
       \binom{2(j+1)}{j+1}
       \binom{2(n-j-1)}{n-j-1}.
```

Thus

```math
\frac{B_j}{p^2}
\equiv(C_j^+-C_j^-)
\sum_{b=1}^{h}\frac1{b^2}\pmod p.
```

The full nonzero quadratic reciprocal sum is zero modulo `p`, and pairing
`b` with `p-b` shows that it is twice the displayed half-sum.  Hence the
half-sum is zero modulo `p`, proving (11). QED

## 4. Contraction of the divisible terms

For `0<=j<=n`, equations (6)--(7) give

```math
\begin{aligned}
A_{np}(jp)
&=\binom{(n+j)p-1}{jp}
  \binom{2(n-j)p}{(n-j)p}\binom{2jp}{jp}\\
&\equiv
\binom{n+j-1}{j}
\binom{2(n-j)}{n-j}\binom{2j}{j}
=A_n(j)\pmod {p^3}.
\tag{15}
\end{aligned}
```

Split the convolution (4) into indices divisible and not divisible by
`p`.  Lemma 2 and (15) give

```math
F(np)
=\sum_{j=0}^{n}A_{np}(jp)+\sum_{j=0}^{n-1}B_j
\equiv\sum_{j=0}^{n}A_n(j)=F(n)\pmod {p^3}.
```

This proves the theorem. QED

## 5. Remaining boundary

The theorem closes the entire `r=1` layer, but it does not prove (1) for
`r>=2`.  At higher levels, indices with intermediate valuation
`0<v_p(k)<r` create nested residue blocks.  The next target is a
valuation-stratified version of Lemma 2 that gains `3r`, rather than only
the first three powers.

The companion checker
[`verify_a362676_one_step.py`](../verification/related/verify_a362676_one_step.py)
verifies the convolution identity, the local carry formulas, every block
congruence in a finite grid, and the theorem directly in exact integer
arithmetic.  Those checks audit the proof but are not inputs to it.

## References

- Peter Bala, [OEIS A362676](https://oeis.org/A362676), including the
  convolution formula and the full cubic-tower conjecture.
- Robert Osburn and Brundaban Sahu,
  [*A supercongruence for generalized Domb numbers*](https://arxiv.org/abs/1201.6195),
  for the unit-product and divisible/nondivisible-index architecture.
- Armin Straub,
  [*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854),
  for the surrounding Franel and Askey--Gasper towers.
