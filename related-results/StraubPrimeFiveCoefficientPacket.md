# Straub's prime-five multivariate Apéry boundary

**Status:** published-source reconciliation with an independent boundary audit

**Correction:** Straub's published Theorem 3.2(b) already states the
multivariate cubic tower for primes \(p\geq5\). An earlier version of this
repository incorrectly described the source as `p>5` and presented the
boundary check below as an extension. It is instead an independent audit of
the theorem's included endpoint and an exact match to three OEIS records.

## 1. The source theorem and its boundary

For a partition
\(\lambda=(\lambda_1,\ldots,\lambda_\ell)\), a sign
\(\varepsilon\in\{-1,1\}\), and an integer vector \(\boldsymbol n\), Straub
defines the finite multivariate coefficient sum
\(A_{\lambda,\varepsilon}(\boldsymbol n)\) in equation (20) of
[Multivariate Apéry numbers and supercongruences of rational
functions](https://arxiv.org/abs/1401.0854).

The cubic part of Straub's Theorem 3.2 says that, when
\(\ell\geq2\), every part \(\lambda_j\leq2\), and the defining sum is finite,

```math
A_{\lambda,\varepsilon}(p^r\boldsymbol n)
\equiv
A_{\lambda,\varepsilon}(p^{r-1}\boldsymbol n)
\pmod {p^{3r}}
\tag{1}
```

for primes \(p\geq5\) and integers \(r\geq1\).

Thus no prime-five extension is needed. The next section verifies directly
that the two local inputs in the printed proof have no loss at its endpoint.

## 2. Why the published endpoint is sound

There are two local estimates worth checking explicitly at `p=5`.

### 2.1 The binomial scaling estimate

Straub's Lemma 5.1 is the Jacobsthal congruence

```math
\frac{\binom{pa}{pb}}{\binom ab}
\equiv 1 \pmod {p^q}
```

for odd \(p\), where

```math
q=v_p\left(\frac{p^3ab(a-b)}{12}\right).
```

At \(p=5\), the denominator \(12\) is a unit. Thus

```math
q=3+v_5\bigl(ab(a-b)\bigr),
```

which is exactly the no-loss estimate used in Straub's equations
(39)--(41). Every binomial or multinomial quotient in that part of the proof
therefore has the modulus required by the printed `p>=5` theorem.

### 2.2 The reciprocal-square block

The second input is Straub's Lemma 5.2. At \(p=5\), put

```math
S_t^\varepsilon
=
\sum_{\substack{1\leq k<5^t\\5\nmid k}}
\frac{\varepsilon^k}{k^2}
\quad\text{in }\mathbb Z/5^t\mathbb Z.
```

If \(\varepsilon=-1\), pair \(k\) with \(5^t-k\). Their inverse squares are
equal modulo \(5^t\), while their signs are opposite because \(5^t\) is odd.
Hence \(S_t^{-1}=0\).

If \(\varepsilon=1\), multiplication by \(2\) permutes the units modulo
\(5^t\), so

```math
S_t^1\equiv 2^{-2}S_t^1\pmod {5^t}.
```

Since \(2^2-1=3\) is a 5-adic unit, this again gives \(S_t^1=0\).
Therefore

```math
\sum_{\substack{1\leq k<5^t\\5\nmid k}}
\frac{\varepsilon^k}{k^2}
\equiv0\pmod {5^t}
\tag{2}
```

for both signs.

Straub's remaining proof of Theorem 3.2(b) uses the prime restriction only
through the no-loss Jacobsthal estimate and (2). The calculation above
therefore independently confirms the published endpoint; it does not add a
new prime to the theorem.

## 3. Four OEIS consequences

Straub's theorem, after the following exact parameter matches, source-closes
three complete records and the ordinary tower on a fourth record in the
110-record campaign.

### 3.1 A108625

Let

```math
T_2(n,m)
=
\sum_{k=0}^{\min(n,m)}
\binom nk^2\binom{n+m-k}{m-k}.
```

This is [A108625](https://oeis.org/A108625), and it is Straub's
three-variable coefficient

```math
T_2(n,m)=B(n,m,n).
```

Applying (1) to the vector \((n,m,n)\) gives, for \(p\geq5\),

```math
T_2(np^r,mp^r)
\equiv T_2(np^{r-1},mp^{r-1})
\pmod {p^{3r}}.
```

### 3.2 A143007

Let

```math
T_3(n,m)
=
\sum_{k=0}^{\min(n,m)}
\binom nk^2\binom{n+m-k}{m-k}^2.
```

This is [A143007](https://oeis.org/A143007), with the exact coefficient
identification

```math
T_3(n,m)=A(n,m,n,m).
```

Thus, for \(p\geq5\),

```math
T_3(np^r,mp^r)
\equiv T_3(np^{r-1},mp^{r-1})
\pmod {p^{3r}}.
```

### 3.3 A177316

For \(N\geq1\), [A177316](https://oeis.org/A177316) has the sum

```math
a(N)=
\sum_{k=0}^N
\binom Nk^2\binom{N+k-1}{k}^2.
\tag{3}
```

Set

```math
t_k=\binom Nk^2\binom{N+k-1}{k}^2.
```

The elementary telescoping identity

```math
(N^2-2k^2)t_k
=
\frac{(k+1)^4}{N^2}t_{k+1}
-
\frac{k^4}{N^2}t_k
\tag{4}
```

holds for \(0\leq k\leq N\), with \(t_{N+1}=0\). Summing (4) gives

```math
a(N)=2\sum_{k=1}^N\frac{k^2}{N^2}t_k.
\tag{5}
```

On the other hand, Straub's bilateral coefficient formula and the standard
negative-binomial identities give

```math
\begin{aligned}
A(-N,N,-N,N)
&=
\sum_{k=1}^N
\binom{-N}{k}^2\binom{-k}{-N}^2\\
&=
\sum_{k=1}^N
\binom{N+k-1}{k}^2\binom{N-1}{k-1}^2\\
&=
\sum_{k=1}^N\frac{k^2}{N^2}t_k.
\end{aligned}
```

Combining this with (5),

```math
a(N)=2A(-N,N,-N,N).
\tag{6}
```

The vector on the right of (6) scales without a shift. Applying (1) to
\((-n,n,-n,n)\), then multiplying by \(2\), proves

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}
```

for every \(p\geq5\).

### 3.4 The offset-one A108628 tower

With its original offset zero, [A108628](https://oeis.org/A108628) is

```math
a(n)=B(n+1,n,n+1).
\tag{7}
```

When the same list is indexed from one, its `N`-th term is therefore

```math
\widehat a(N)=a(N-1)=B(N,N-1,N).
\tag{8}
```

The apparent shift causes no loss under the tower: for fixed `N`, the
entire vector `(N,N-1,N)` scales homogeneously. Applying (1) directly gives

```math
\boxed{
\widehat a(np^r)\equiv\widehat a(np^{r-1})
\pmod {p^{3r}}}
\tag{9}
```

for every prime `p>=5` and positive `n,r`, including `p=5`. An earlier
source-boundary note instead passed through
`a(n)=(2*A005258(n+1)-A005258(n))/5` and therefore appeared to lose a
factor at five. Equation (8) is the direct parameter match and removes
that artificial loss.

The four half-index vanishing conjectures on A108628 are different affine
coefficient problems and are not consequences of (9). The companion
[half-index note](A108628HalfIndexBoundary.md) proves the first one; the
three higher-power statements remain open.

## 4. Verification and non-claims

The exact checker
[`verify_straub_prime5_packet.py`](../verification/related/verify_straub_prime5_packet.py)
performs exact integer-arithmetic checks of:

- the four parameter identifications, including (7)--(8);
- 230 checks of the telescoping identity (4);
- 10 checks of the two signed reciprocal-square blocks through \(5^5\); and
- the four prime-five towers at the first two levels; and
- 160 randomized exact checks of the full signed multivariate coefficient
  theorem across five partition shapes and two adjacent levels.

These computations test transcription and boundary behavior. The
controlling theorem is Straub's published result; Section 2 is a redundant
endpoint audit, not a claim of priority.

No claim is made here about \(p=2\) or \(p=3\), and the three higher-power
half-index claims on A108628 are explicitly not settled.
