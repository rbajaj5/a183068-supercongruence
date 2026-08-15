# The A108628 half-index boundary

**Status:** the complete offset-one cubic tower is a direct corollary of
Straub's published multivariate theorem; the first half-index conjecture is
proved here; three higher-power half-index congruences remain open

Let

```math
a(n)=\sum_{k=0}^n
\binom nk\binom{n+1}{k}\binom{n+k+1}{k},
\qquad n\ge0,
\tag{1}
```

the sequence [A108628](https://oeis.org/A108628).

## 1. The ordinary tower is source-closed, including five

Straub's three-variable Apéry coefficient satisfies

```math
a(n)=B(n+1,n,n+1).
\tag{2}
```

Indexing the same list from one gives

```math
\widehat a(N)=a(N-1)=B(N,N-1,N).
\tag{3}
```

Hence the upper level is

```math
\widehat a(np^r)=B\bigl(p^r(n,n-1,n)\bigr).
```

Straub's Theorem 3.2(b) therefore proves, directly and without dividing by
five,

```math
\widehat a(np^r)\equiv\widehat a(np^{r-1})
\pmod {p^{3r}}
\tag{4}
```

for every prime `p>=5` and positive `n,r`. The separate source audit gives
the exact parameter and endpoint details.

## 2. A terminating Dixon identity

Define

```math
D_n=\sum_{j=1}^n(-1)^{n-j}
\binom{n+1}{j}^2\binom{n-1}{j-1}.
\tag{5}
```

### Lemma 1

For every positive integer `n`,

```math
D_{2m}=0,
\qquad
D_{2m+1}=4(-1)^m\binom{2m}{m}\binom{3m+2}{m}.
\tag{6}
```

### Proof

Putting `j=k+1` in (5) gives

```math
D_n=(-1)^{n-1}(n+1)^2
{}_3F_2\!\left(
\begin{matrix}1-n,-n,-n\\2,2\end{matrix};1
\right).
\tag{7}
```

This is the terminating Dixon sum with
`a=1-n` and `b=c=-n`, because both lower parameters are
`1+a-b=1+a-c=2`. The terminating form of Dixon's identity evaluates (7)
to zero for even `n` and to the second expression in (6) for odd `n`.
All sums are finite, so the specialization involves no convergence issue.
QED

The odd formula is included because it checks the parity boundary exactly;
only the even vanishing is needed below.

## 3. The first half-index conjecture

### Theorem 2

For every prime `p` congruent to `1` modulo `4`,

```math
\boxed{a((p-1)/2)\equiv0\pmod p.}
\tag{8}
```

### Proof

The Legendre-polynomial formula on A108628 is equivalently

```math
a(n)=[x^n]
\frac{1}{(1-x)^{n+2}}
\sum_{j=0}^{n+1}\binom{n+1}{j}^2x^j.
\tag{9}
```

Thus

```math
a(n)=\sum_{j=0}^n
\binom{n+1}{j}^2\binom{2n+1-j}{n-j}.
\tag{10}
```

Set `n=(p-1)/2`. The `j=0` term in (10) is divisible by `p`. For
`1<=j<=n`, reduction of the upper argument modulo `p` gives

```math
\binom{p-j}{n-j}
\equiv
(-1)^{n-j}\binom{n-1}{j-1}
\pmod p.
\tag{11}
```

Consequently `a(n)` is congruent to `D_n` modulo `p`. If
`p` is `1` modulo `4`, then `n` is even, and Lemma 1 gives `D_n=0`
as an exact integer identity. This proves (8). QED

## 4. The exact valuation of the Dixon comparison term

The closed form in Lemma 1 already contains the exceptional loss for primes
congruent to `3` modulo `4`.

### Theorem 3

Let `p` be an odd prime, let `r>=1`, and put

```math
n_r=\frac{p^r-1}{2}.
```

If `n_r` is even, then `D_(n_r)=0`. If `p` is congruent to `3` modulo `4`
and `r` is odd, then

```math
\boxed{v_p(D_{n_r})=r-1.}
\tag{12}
```

### Proof

Only the second assertion needs proof. Write

```math
m=\frac{p^r-3}{4}.
```

Lemma 1 gives

```math
D_{n_r}=4(-1)^m\binom{2m}{m}\binom{3m+2}{m}.
```

For `t=p^j`, the contribution at level `j` in Legendre's formula for the
product of the two binomial coefficients is

```math
\left\lfloor\frac{2m}{t}\right\rfloor
+\left\lfloor\frac{3m+2}{t}\right\rfloor
-3\left\lfloor\frac{m}{t}\right\rfloor
-\left\lfloor\frac{2m+2}{t}\right\rfloor.
```

Put `Q=p^(r-j)`. Direct substitution of `p^r=tQ` shows that this expression
is zero when `Q` is `1` modulo `4` and is two when `Q` is `3` modulo `4`.
Since `p` is `3` modulo `4` and `r` is odd, the second case occurs exactly
for the even integers `j` in `1<=j<=r`. There are `(r-1)/2` of them. The
total valuation is therefore `2*(r-1)/2=r-1`. QED

## 5. One master congruence would close the remaining packet

The exact computations suggest the stronger uniform comparison

```math
a\!\left(\frac{p^r-1}{2}\right)
\equiv D_{(p^r-1)/2}\pmod {p^r}
\qquad(p\ge5,\ r\ge1).
\tag{13}
```

This statement is **not proved here**. It is recorded because it consolidates
the three surviving OEIS claims into one precise Frobenius/Cartier target:

- if `p` is `1` modulo `4`, then `(p^r-1)/2` is even and the right side is
  zero;
- if `p` is `3` modulo `4` and `r` is even, the same parity argument applies;
- if `p` is `3` modulo `4` and `r` is odd, Theorem 3 supplies exactly the
  exceptional valuation `r-1`.

Thus (13) would prove the two stated `r=3` congruences and the stated `r=2`
congruence at once, and would extend their pattern to every level.

The reduction is genuinely aggregate. Individual summands in the difference
between (10) and (5) need not be divisible by `p^r`; their low-valuation
parts cancel only after summation. Any proof of (13) must retain that
cancellation, for example through a Cartier operator on the parity-lifted
diagonal or through a blockwise hypergeometric transformation.

## 6. What remains

The live OEIS page also conjectures

```math
a((p^3-1)/2)\equiv0\pmod {p^3}
\quad (p\equiv1\pmod4),
```

```math
a((p^3-1)/2)\equiv0\pmod {p^2}
\quad (p\equiv3\pmod4),
```

and

```math
a((p^2-1)/2)\equiv0\pmod {p^2}
\quad (p\ge5).
```

These three statements concern affine towers of coefficient vectors. They
do not follow from the homogeneous theorem (4), and Theorem 2 supplies only
their first residue boundary. By Theorem 3, all three would follow from the
single master congruence (13). That aggregate comparison is the remaining
proof obligation.

## 7. Verification

The exact checker
[`verify_a108628_half_index.py`](../verification/related/verify_a108628_half_index.py)
performs 1,797 exact checks. It verifies (1), (5)--(6), and (9)--(12), tests Theorem 2 through a broad prime
range, checks the direct `p=5` tower at two levels, verifies the valuation in
Theorem 3, and records exact finite evidence for (13) and the three surviving
half-index conjectures.

The source theorem is Armin Straub,
[*Multivariate Apéry numbers and supercongruences of rational
functions*](https://arxiv.org/abs/1401.0854), Theorem 3.2(b). No literature
priority claim is made for Theorem 2 pending a targeted search.

A nearby but distinct result is Zhi-Hong Sun's evaluation of the classical
zeta-two Apéry number `A'((p-1)/2)` modulo `p^3` for primes congruent to `3`
modulo `4` in
[*Congruences for the Apéry numbers modulo p^3*](https://arxiv.org/abs/2409.06544).
Together with `a(n)=(2A'(n+1)-A'(n))/5`, it explains why half-index Apéry
methods are relevant, but it does not provide the adjacent value or the
higher affine levels required for (13).
