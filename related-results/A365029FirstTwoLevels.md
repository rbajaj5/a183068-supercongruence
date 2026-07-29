# The first two levels of the A365029 supercongruence

**Status:** complete unchecked proof of the \(r=1,2\) cases of Peter Bala's
second [OEIS A365029](https://oeis.org/A365029) conjecture; exact checks
included; the \(r\ge3\) tower remains open.

Define

```math
a(N)=\sum_{k=0}^{N}
\binom{N+k-1}{k}^{2}\binom{2k-1}{N},
\tag{1}
```

where generalized binomial coefficients are used at \(k=0\), so
\(\binom{-1}{N}=(-1)^N\).

## Theorem

For every prime \(p\ge5\), every positive integer \(n\), and
\(r\in\{1,2\}\),

```math
\boxed{a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}.}
\tag{2}
```

These are the first two complete levels of the conjectured tower

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}.
\tag{3}
```

The proof exposes the two mechanisms that a proof of (3) must iterate:

1. shifted Jacobsthal scaling transfers the terms with \(p\mid k\);
2. reciprocal-square cancellation kills the terms with \(p\nmid k\).

The second mechanism is essential. At level \(r\), individual
\(p\nmid k\) terms generally have valuation only \(2r\), not \(3r\).

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

This proves (2) for \(r=1\). \(\square\)

## 4. The second level

We now prove

```math
a(np^2)\equiv a(np)\pmod {p^6}.
\tag{16}
```

### 4.1 Adjacent transfer for the multiples

The valuation-sensitive Jacobsthal estimate gives more than (4). Let
\(t=v_p(N)\). For every \(k\ge0\),

```math
F(pN,pk)\equiv F(N,k)\pmod {p^{3(t+1)}}.
\tag{17}
```

Here is the valuation check. The cases \(k=0\) and \(2k\le N\) are
immediate, so assume \(k>0\) and \(2k>N\). Put

```math
t=v_p(N),\quad
\alpha=v_p(k),\quad
\beta=v_p(N+k),\quad
\gamma=v_p(2k-N).
```

The scale-invariant factorization

```math
F(N,k)=
\left(\frac{N}{N+k}\binom{N+k}{k}\right)^2
\left(\frac{2k-N}{2k}\binom{2k}{N}\right)
\tag{18}
```

shows that \(F(pN,pk)/F(N,k)\) is the product of two copies of the
Jacobsthal quotient for \(\binom{N+k}{k}\) and one copy of the quotient
for \(\binom{2k}{N}\). Their errors have valuations at least

```math
3+t+\alpha+\beta,
\qquad
3+t+\alpha+\gamma,
\tag{19}
```

respectively.

Let \(x=\binom{N+k-1}{k}\). If \(\alpha<t\), then
\(\beta=\gamma=\alpha\) and

```math
v_p(x)\ge t-\alpha.
```

If \(\alpha\ge t\), then \(\beta,\gamma\ge t\). In either case,

```math
v_p(F(N,k))+\alpha+\beta\ge2t,
\qquad
v_p(F(N,k))+\alpha+\gamma\ge2t.
\tag{20}
```

Multiplying (19) by the lower-level summand therefore puts every error in
\(p^{3+3t}\), proving (17). With \(N=np\), this transfers all terms with
\(p\mid k\) modulo \(p^6\).

### 4.2 Two digit expansions

Set \(q=p^2\), write

```math
k=q\ell+u,
\qquad
u=pv+c,
\qquad
0\le v\le p-1,\quad1\le c\le p-1,
\tag{21}
```

and put

```math
K=n\binom{n+\ell}{\ell},
\qquad
H_m=\sum_{j=1}^{m}\frac1j
\quad(H_0=0).
```

All congruences in this subsection are in \(\mathbb Z_{(p)}\) modulo
\(p^2\). Splitting the product

```math
\frac1q\binom{nq+k-1}{k}
=
\frac n k\prod_{j=1}^{k-1}\left(1+\frac{nq}{j}\right)
```

first at \(p\mid j\), and then into complete residue blocks, gives

```math
X(v,c):=
\frac1q\binom{nq+k-1}{k}
\equiv
Kc^{-1}
\left(1+p\left(nH_v-vc^{-1}\right)\right).
\tag{22}
```

For the second binomial, set

```math
\epsilon(c)=
\begin{cases}
0,&1\le c\le(p-1)/2,\\
1,&(p+1)/2\le c\le p-1,
\end{cases}
```

and write

```math
2v+\epsilon(c)=pe+b,
\qquad0\le b<p.
```

Two applications of the elementary congruence

```math
\binom{pA+b}{pB}
\equiv
\binom AB\left(1+pB H_b\right)
\pmod {p^2}
\tag{23}
```

give

```math
Y(v,c):=
\binom{2k-1}{nq}
\equiv
\binom{2\ell+e}{n}\left(1+pnH_b\right).
\tag{24}
```

Equations (22)--(24) are the complete second-level local expansion.

### 4.3 The paired harmonic identity

Let \(h=(p-1)/2\), and in \(\mathbb Z/p^2\mathbb Z\) put

```math
S_j=\sum_{c=1}^{p-1}c^{-j},
\qquad
s_j=\sum_{c=1}^{h}c^{-j},
\qquad
\bar s_j=\sum_{c=h+1}^{p-1}c^{-j}.
```

Finite-field power sums and pairing \(c\leftrightarrow p-c\) give

```math
s_2\equiv\bar s_2\equiv0\pmod p,
\qquad
S_3\equiv0\pmod p,
\tag{25}
```

and

```math
S_2\equiv2s_2+2ps_3\pmod {p^2},
\quad
\bar s_2\equiv s_2+2ps_3\pmod {p^2},
\quad
\bar s_3\equiv-s_3\pmod p.
\tag{26}
```

We sum \(X(v,c)^2Y(v,c)\) over the lower half \(1\le u<q/2\).
For each \(0\le v<h\), all \(1\le c<p\) occur, \(e=0\), and the
terms multiplied by \(p\) in (22)--(24) vanish after summation by (25).
Each such row is therefore

```math
K^2\binom{2\ell}{n}S_2\pmod {p^2}.
```

The boundary row \(v=h,\ 1\le c\le h\) contributes

```math
K^2\binom{2\ell}{n}
\left(s_2-2phs_3\right)
\pmod {p^2}.
```

The full lower-half sum is consequently the same constant times

```math
hS_2+s_2-2phs_3
\equiv
(2h+1)s_2
=ps_2
\equiv0\pmod {p^2},
\tag{27}
```

where (26) was used in the middle step.

The upper half is identical with
\(\binom{2\ell+1}{n}\) in place of \(\binom{2\ell}{n}\). Its harmonic
factor is

```math
hS_2+\bar s_2-2ph\bar s_3
\equiv
ps_2+2p^2s_3
\equiv0\pmod {p^2}.
\tag{28}
```

Since \(F(nq,q\ell+u)=q^2X(v,c)^2Y(v,c)\), equations (27)--(28) prove

```math
\sum_{\substack{1\le u<q\\p\nmid u}}
F(nq,q\ell+u)
\equiv0\pmod {p^6}
\tag{29}
```

for every complete block \(0\le\ell<n\).

### 4.4 Assembly

Split the defining sum for \(a(np^2)\) according to \(p\mid k\).
Equation (17) with \(N=np\) identifies the multiple terms with the
summands of \(a(np)\) modulo \(p^6\), while (29) kills every remaining
complete block. This proves (16), and hence (2) for \(r=2\).
\(\square\)

## 5. What remains at higher levels

For \(q=p^r\), exact computations suggest the stronger block statement

```math
\sum_{\substack{1\le u<q\\p\nmid u}}
F(nq,q\ell+u)
\equiv0\pmod {q^3}
\tag{30}
```

for every complete block \(0\le\ell<n\). Equation (30), together with
the adjacent shifted-scaling congruence, would prove the whole tower (3).

The checker verifies (30) for \(p\in\{5,7,11\}\), \(r\le3\), and
\(n\le7\). The cases \(r=1,2\) are now proved above; the \(r=3\) checks
remain evidence only. The next task is to turn the two-digit calculation
into an induction on the number of base-\(p\) digits.

## Reproduction

Run:

```text
python verification/related/verify_a365029_first_two_levels.py
```

The script checks both proved levels, the shifted transfer, both local
expansions, the lower/upper block cancellations, the harmonic identities,
and the higher-level block target separately.
