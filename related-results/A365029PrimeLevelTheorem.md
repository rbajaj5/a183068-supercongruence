# The prime-level A365029 supercongruence

**Status:** complete unchecked proof of the \(r=1\) case of Peter Bala's
second [OEIS A365029](https://oeis.org/A365029) conjecture; exact checks
included; the \(r\ge2\) tower remains open.

Define

```math
a(N)=\sum_{k=0}^{N}
\binom{N+k-1}{k}^{2}\binom{2k-1}{N},
\tag{1}
```

where generalized binomial coefficients are used at \(k=0\), so
\(\binom{-1}{N}=(-1)^N\).

## Theorem

For every prime \(p\ge5\) and every positive integer \(n\),

```math
\boxed{a(np)\equiv a(n)\pmod {p^3}.}
\tag{2}
```

This is the full \(r=1\) case of the conjectured tower

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}.
\tag{3}
```

The proof exposes the two mechanisms that a proof of (3) must lift:

1. shifted Jacobsthal scaling transfers the terms with \(p\mid k\);
2. reciprocal-square cancellation kills the terms with \(p\nmid k\).

The second mechanism is essential. Individual \(p\nmid k\) terms generally
have valuation only \(2\), not \(3\).

## 1. The shifted scaling lemma

For \(p\ge5\), \(A\ge1\), and \(0\le B\le A\), the
Ljunggren--Jacobsthal congruence implies

```math
\binom{pA-1}{pB}\equiv\binom{A-1}{B}\pmod {p^3}.
\tag{4}
```

Indeed,

```math
\binom{pA-1}{pB}
=\frac{A-B}{A}\binom{pA}{pB},
\qquad
\binom{A-1}{B}
=\frac{A-B}{A}\binom AB,
```

and the Jacobsthal quotient

```math
Q_p(A,B)=\frac{\binom{pA}{pB}}{\binom AB}
```

is a \(p\)-adic unit congruent to \(1\pmod {p^3}\). Thus

```math
\binom{pA-1}{pB}
=\binom{A-1}{B}Q_p(A,B),
```

which proves (4). The endpoint cases are immediate. References for this
quotient form are collected in the scaling section of
[the A183068 proof](../PROOF.md#3-multinomial-scaling).

Put

```math
F(N,k)=
\binom{N+k-1}{k}^{2}\binom{2k-1}{N}.
\tag{5}
```

For \(k=p\ell\), equation (4), first with
\((A,B)=(n+\ell,\ell)\), gives

```math
\binom{p(n+\ell)-1}{p\ell}
\equiv
\binom{n+\ell-1}{\ell}
\pmod {p^3}.
\tag{6}
```

If \(n\le2\ell\), its second application with
\((A,B)=(2\ell,n)\) gives

```math
\binom{2p\ell-1}{pn}
\equiv
\binom{2\ell-1}{n}
\pmod {p^3}.
\tag{7}
```

If \(n>2\ell>0\), both sides of (7) are zero. For \(\ell=0\), they
are equal because \(p\) is odd:

```math
\binom{-1}{pn}=(-1)^{pn}=(-1)^n=\binom{-1}{n}.
```

Consequently,

```math
F(np,p\ell)\equiv F(n,\ell)\pmod {p^3}
\qquad(0\le\ell\le n).
\tag{8}
```

## 2. The nonmultiples of \(p\)

Write

```math
k=p\ell+u,
\qquad
0\le\ell\le n-1,
\qquad
1\le u\le p-1.
\tag{9}
```

The first binomial in (5) satisfies

```math
\binom{np+k-1}{k}
=
\frac{np}{np+k}\binom{np+k}{k}.
\tag{10}
```

The denominator is a \(p\)-adic unit. Lucas' theorem applied to (10)
therefore gives

```math
\frac1p\binom{np+k-1}{k}
\equiv
\frac n u\binom{n+\ell}{\ell}
\pmod p.
\tag{11}
```

Set \(h=(p-1)/2\). A second application of Lucas' theorem gives

```math
\binom{2k-1}{np}
\equiv
\begin{cases}
\binom{2\ell}{n},&1\le u\le h,\\
\binom{2\ell+1}{n},&h<u\le p-1
\end{cases}
\pmod p.
\tag{12}
```

After dividing a complete block by \(p^2\), equations (11)--(12) give

```math
\begin{aligned}
\frac1{p^2}\sum_{u=1}^{p-1}F(np,p\ell+u)
\equiv{}&
n^2\binom{n+\ell}{\ell}^{2}\\
&{}\cdot\left(
\binom{2\ell}{n}\sum_{u=1}^{h}u^{-2}
+
\binom{2\ell+1}{n}\sum_{u=h+1}^{p-1}u^{-2}
\right)
\pmod p.
\end{aligned}
\tag{13}
```

The substitution \(u\mapsto p-u\) identifies the two half sums. Their
total is

```math
\sum_{u=1}^{p-1}u^{-2}
\equiv
\sum_{u=1}^{p-1}u^{p-3}
\equiv0\pmod p,
\tag{14}
```

because \(p-1\nmid p-3\). Since \(2\) is invertible modulo \(p\), each
half sum in (13) vanishes. Hence

```math
\sum_{u=1}^{p-1}F(np,p\ell+u)\equiv0\pmod {p^3}
\tag{15}
```

for every \(0\le\ell\le n-1\).

## 3. Assembly

Split (1) into multiples and nonmultiples of \(p\). Equations (8) and
(15) yield

```math
\begin{aligned}
a(np)
&=
\sum_{\ell=0}^{n}F(np,p\ell)
+
\sum_{\ell=0}^{n-1}\sum_{u=1}^{p-1}F(np,p\ell+u)\\
&\equiv
\sum_{\ell=0}^{n}F(n,\ell)
=a(n)
\pmod {p^3}.
\end{aligned}
```

This proves (2). \(\square\)

## 4. What remains at higher levels

For \(q=p^r\), exact computations suggest the stronger block statement

```math
\sum_{\substack{1\le u<q\\p\nmid u}}
F(nq,q\ell+u)
\equiv0\pmod {q^3}
\tag{16}
```

for every complete block \(0\le\ell<n\). Equation (16), together with
the adjacent shifted-scaling congruence, would prove the whole tower (3).

The checker verifies (16) for \(p\in\{5,7,11\}\), \(r\le3\), and
\(n\le7\), but this is evidence, not a proof. At \(r=1\), (16) is exactly
the proved reciprocal-square cancellation above. The next task is to lift
that half-system cancellation from \(\mathbb F_p\) to
\(\mathbb Z/p^r\mathbb Z\).

## Reproduction

Run:

```text
python verification/related/verify_a365029_prime_level.py
```

The script checks the theorem, the shifted transfer, the Lucas block
formula, the half-system reciprocal-square identity, and the higher-level
block target separately.
