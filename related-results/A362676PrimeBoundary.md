# The prime boundary for A362676

**Status:** complete elementary proof of the `n=r=1` boundary; the full
adjacent cubic tower remains open; priority provisional

Let

```math
F(N)=\sum_{k=0}^{N}4^{N-k}\binom Nk\binom{N-1}{k}\binom{2k}{k},
```

the sequence [A362676](https://oeis.org/A362676).  The OEIS entry conjectures

```math
F(np^r)\equiv F(np^{r-1})\pmod {p^{3r}}
\tag{1}
```

for primes `p>=5`.  This note proves the first prime point of (1).

## Theorem

For every prime `p>=5`,

```math
\boxed{F(p)\equiv F(1)=4\pmod {p^3}.}
\tag{2}
```

The proof is not a finite check.  Its new local input is an exact
low-half/high-half cancellation for central binomial sums.

Throughout, put

```math
h=\frac{p-1}{2},\qquad
q=q_p(2)=\frac{2^{p-1}-1}{p},\qquad
a_k=\frac1{4^k}\binom{2k}{k},
```

and write `H_n` and `H_n^(2)` for the ordinary and second-order harmonic
sums.  All rational congruences below have denominators prime to `p`.

## 1. Two central-binomial blocks

Define

```math
S_1=\sum_{k=1}^{p-1}\frac{a_k}{k}
```

and

```math
S_2=\sum_{k=1}^{p-1}\frac{a_k}{k}
\left(2H_{k-1}+\frac1k\right).
```

### Lemma 1

For every prime `p>=5`,

```math
S_1\equiv-H_h\pmod {p^2}.
\tag{3}
```

### Proof

For `1<=k<=h`, set

```math
b_k=(-1)^k\binom hk,
\qquad
O_k=\sum_{j=1}^{k}\frac1{2j-1}.
```

The product formula for the binomial coefficient gives

```math
b_k
=a_k\prod_{j=1}^{k}\left(1-\frac p{2j-1}\right),
```

and hence

```math
a_k\equiv b_k(1+pO_k)\pmod {p^2}.
\tag{4}
```

For the upper half, write `k=p-j`, where `1<=j<=h`.  Wilson's theorem,
applied after removing the unique factor `p` from the numerator, gives

```math
\frac1p\binom{2p-2j}{p-j}
\equiv-\frac{2}{j\binom{2j}{j}}\pmod p.
\tag{5}
```

Since `4^(p-j) == 4^(1-j) (mod p)`, (5) implies

```math
\frac1p\sum_{k=h+1}^{p-1}\frac{a_k}{k}
\equiv
\frac12\sum_{j=1}^{h}\frac{4^j}{j^2\binom{2j}{j}}
\pmod p.
\tag{6}
```

The required cancellation is the following exact identity, valid for every
positive integer `n`:

```math
\sum_{k=1}^{n}\frac{(-1)^k}{k}\binom nk O_k
=-\frac12\sum_{k=1}^{n}\frac{4^k}{k^2\binom{2k}{k}}.
\tag{7}
```

For completeness, let the left side of (7) be `A_n`.  Pascal's identity
and

```math
O_{j+1}=\int_0^1\frac{1-x^{2j+2}}{1-x^2}\,dx
```

give

```math
A_n-A_{n-1}
=-\frac1n\int_0^1(1-x^2)^{n-1}\,dx
=-\frac{4^n}{2n^2\binom{2n}{n}}.
```

As `A_0=0`, summation proves (7).  Combining (4), (6), and (7), the two
order-`p` corrections cancel.  Finally,

```math
\sum_{k=1}^{h}\frac{(-1)^k}{k}\binom hk=-H_h,
```

which follows by integrating `((1-x)^h-1)/x`.  This proves (3). QED

### Lemma 2

For every prime `p>=5`,

```math
S_2\equiv\frac12H_h^2\pmod p.
\tag{8}
```

### Proof

The upper-half terms vanish modulo `p`, while (4) gives `a_k==b_k (mod p)`
on the lower half.  Two elementary binomial-harmonic identities are

```math
\sum_{k=1}^{n}\frac{(-1)^k}{k^2}\binom nk
=-\frac12\left(H_n^2+H_n^{(2)}\right)
\tag{9}
```

and

```math
\sum_{k=1}^{n}\frac{(-1)^kH_{k-1}}{k}\binom nk
=\frac12\left(H_n^2-H_n^{(2)}\right).
\tag{10}
```

For a direct verification, Pascal's identity shows that the left side of
(9), as `n` increases by one, changes by `-H_n/n`; summing gives its right
side.  The left side of (10) changes by `H_(n-1)/n`, and summing gives its
right side.  Thus no analytic continuation is involved.  Equations
(9)--(10) show that the lower half of `S_2` is exactly

```math
\frac12H_h^2-\frac32H_h^{(2)}.
```

The usual pairing `j` with `p-j` in the nonzero residues gives
`H_h^(2)==0 (mod p)`.  This proves (8). QED

## 2. Fermat-quotient normalization

The classical Morley--Lehmer congruence says

```math
H_h\equiv-2q+pq^2\pmod {p^2}.
\tag{11}
```

It follows from (3), (8), and (11) that

```math
S_1\equiv2q-pq^2\pmod {p^2},
\qquad
S_2\equiv2q^2\pmod p.
\tag{12}
```

## 3. Proof of the theorem

The `k=0` term of `F(p)` is `4^p`, and the `k=p` term is zero.  For
`1<=k<=p-1`, expanding the two binomial products gives

```math
\binom pk\binom{p-1}{k}
\equiv
-\frac pk\left[1-p\left(2H_{k-1}+\frac1k\right)\right]
\pmod {p^3}.
\tag{13}
```

Consequently,

```math
F(p)\equiv4^p(1-pS_1+p^2S_2)\pmod {p^3}.
\tag{14}
```

Because

```math
4^{p-1}=(1+pq)^2\equiv1+2pq+p^2q^2\pmod {p^3},
```

substitution of (12) into (14) yields

```math
\begin{aligned}
F(p)
&\equiv4(1+2pq+p^2q^2)(1-2pq+3p^2q^2)\\
&\equiv4\pmod {p^3}.
\end{aligned}
```

This proves (2). QED

## 4. Boundary and verification

The theorem proves only `F(p)==F(1) (mod p^3)`.  It does **not** prove the
uniform `F(np^r)==F(np^(r-1)) (mod p^(3r))` tower.  The remaining problem is
still the all-block Cartier contraction isolated in the
[Franel-companion reduction](FranelCompanionConstantTermReduction.md).

The companion checker
[`verify_a362676_prime_boundary.py`](../verification/related/verify_a362676_prime_boundary.py)
verifies (7), (9), and (10) as exact rational identities; checks (3), (8),
(11), and (12) in exact modular arithmetic; and tests (2) directly for all
primes below 200.  These checks audit the algebra but are not inputs to the
proof.

## References

- Peter Bala, [OEIS A362676](https://oeis.org/A362676), including the full
  cubic-tower conjecture.
- Emma Lehmer, *On congruences involving Bernoulli numbers and the quotients
  of Fermat and Wilson*, Annals of Mathematics **39** (1938), 350--360.
- Armin Straub,
  [*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854),
  for the surrounding Franel/Askey--Gasper boundary and the distinction
  between a constant-term representation and a cubic theorem.
