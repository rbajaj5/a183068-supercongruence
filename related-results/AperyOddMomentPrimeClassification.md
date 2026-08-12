# Apéry odd moments at the prime boundary

**Status:** complete elementary proof candidate for A357510, the full
A357512 composite divisibility conjecture, and the prime-boundary
classification; exact checks pass. Independent review and
literature-priority work remain.

This note resolves the prime conjecture on
[OEIS A357510](https://oeis.org/A357510) and proves an exact
prime-by-prime classification for the odd-moment family recorded on
[OEIS A357512](https://oeis.org/A357512).

For an integer $q\geq1$, define

**(1)** $U_q(n)=\displaystyle\sum_{k=0}^{n}k^q
\binom{n}{k}^{2}\binom{n+k}{k}^{2}$.

The result comes from expanding one Apéry summand at $n=p-1$. No
recurrence or unproved property of the Apéry numbers is needed.

## 1. The local product

Let $p$ be an odd prime and $1\leq k\leq p-1$. Directly from the
factorial products,

**(2)** $\displaystyle
\binom{p-1}{k}\binom{p-1+k}{k}
=(-1)^k\frac pk\left(1-\frac pk\right)
\prod_{j=1}^{k-1}\left(1-\frac{p^2}{j^2}\right).$

All denominators in (2) are $p$-adic units. Squaring and discarding
terms of valuation at least four gives, for every $q\geq1$,

**(3)** $\displaystyle
k^q\binom{p-1}{k}^{2}\binom{p-1+k}{k}^{2}
\equiv p^2k^{q-2}-2p^3k^{q-3}\pmod {p^4}.$

For negative exponents, the powers on the right are interpreted in
$\mathbb Z_{(p)}$. Put

**(4)** $\displaystyle S_j(p)=\sum_{k=1}^{p-1}k^j.$

Summing (3) yields the master congruence

**(5)** $\displaystyle
U_q(p-1)\equiv p^2S_{q-2}(p)-2p^3S_{q-3}(p)\pmod {p^4}.$

## 2. A357510

### Theorem 1

For every prime $p\geq5$,

**(6)** $\displaystyle U_1(p-1)\equiv0\pmod {p^4}.$

This is exactly the conjecture printed on A357510.

### Proof

For $q=1$, equation (5) reads

**(7)** $\displaystyle
U_1(p-1)\equiv
p^2\sum_{k=1}^{p-1}\frac1k
-2p^3\sum_{k=1}^{p-1}\frac1{k^2}
\pmod {p^4}.$

Wolstenholme's congruence makes the first reciprocal sum zero modulo
$p^2$. The second is zero modulo $p$, since inversion permutes
$\mathbb F_p^\times$ and the sum of the squares in that field is zero.
Both terms in (7) therefore vanish modulo $p^4$. $\square$

The prime $3$ is a sharp boundary:
$U_1(2)=108$ has $3$-adic valuation $3$, not $4$.

## 3. Exact classification of every higher odd moment

Let $m\geq2$, and set

**(8)** $q=2m+1,\quad a=2m-1,\quad b=2m-2.$

Define $\delta_{p,m}$ to be $1$ if $p-1\mid 2m-2$, and $0$
otherwise.

### Theorem 2

For every odd prime $p$ and every integer $m\geq2$,

**(9)** $\displaystyle
\frac{U_{2m+1}(p-1)}{p^3}
\equiv
\delta_{p,m}\frac{5-2m}{2}
\pmod p.$

In particular,

**(10)** $\displaystyle
U_{2m+1}(p-1)\equiv0\pmod {p^4}$

if and only if

**(11)** $\displaystyle
p-1\nmid 2m-2
\quad\text{or}\quad
p\mid 2m-5.$

If neither condition in (11) holds, the valuation is exactly $3$.

### Proof

Pair $k$ with $p-k$. Since $a$ is odd,

**(12)** $\displaystyle
S_a(p)
\equiv
ap\sum_{k=1}^{(p-1)/2}k^b
\pmod {p^2}.$

The exponent $b$ is even. Therefore the full finite-field power sum is
twice its half sum, and

**(13)** $\displaystyle
\sum_{k=1}^{(p-1)/2}k^b
\equiv-\frac{\delta_{p,m}}2\pmod p,\qquad
S_b(p)\equiv-\delta_{p,m}\pmod p.$

Substitute (12)--(13) into (5):

**(14)** $\displaystyle
U_{2m+1}(p-1)
\equiv
p^3\delta_{p,m}
\left(-\frac a2+2\right)
=p^3\delta_{p,m}\frac{5-2m}{2}
\pmod {p^4}.$

This is (9). Since $2$ is invertible modulo every odd prime, (10)--(11)
follow immediately. $\square$

## 4. Consequences for A357512

The sequence A357512 is $U_5(n)$, the case $m=2$. For every prime
$p\geq5$, one has $p-1\nmid2$, so Theorem 2 proves

**(15)** $\displaystyle U_5(p-1)\equiv0\pmod {p^4}.$

Thus the prime slice of the displayed A357512 conjecture is complete.
The stronger claim for every composite $n\equiv1,5\pmod6$ is proved in
Section 5.

Theorem 2 also determines the *minimal* exceptional-prime set for every
odd moment at the prime boundary:

**(16)** $\displaystyle
E(m)=
\left\{p\ \text{odd prime}:
p-1\mid2m-2\ \text{and}\ p\nmid2m-5
\right\}.$

For the parameters listed on A357512, the exact sets are:

| $m$ | exponent $2m+1$ | exact $E(m)$ |
| ---: | ---: | --- |
| 2 | 5 | $\{3\}$ |
| 3 | 7 | $\{3,5\}$ |
| 4 | 9 | $\{7\}$ |
| 5 | 11 | $\{3\}$ |
| 6 | 13 | $\{3,11\}$ |
| 7 | 15 | $\{5,7,13\}$ |
| 8 | 17 | $\{3\}$ |
| 9 | 19 | $\{3,5,17\}$ |
| 10 | 21 | $\{7,19\}$ |

Some sets printed on the OEIS record were deliberately or accidentally
nonminimal. More importantly, its proposed set $P(9)=\{3\}$ misses two
prime failures. The smallest is the exact counterexample

**(17)** $\displaystyle U_{19}(4)\equiv5^3\not\equiv0\pmod {5^4}.$

This does not affect the present A357512 case $m=2$.

## 5. The full A357512 composite conjecture

### Theorem 3

For every positive integer $n$ coprime to $6$,

```math
\boxed{U_5(n-1)\equiv0\pmod {n^4}.}
\tag{18}
```

This is exactly the remaining A357512 conjecture, since an integer is
congruent to $1$ or $5$ modulo $6$ precisely when it is coprime to $6$.

### 5.1 Removing two powers termwise

For $1\leq k<n$, put

```math
G_n(k)=\binom{n-2}{k-1}\binom{n+k-1}{k-1}.
\tag{19}
```

The two elementary identities

```math
\binom{n-1}{k}=\frac{n-1}{k}\binom{n-2}{k-1},
\qquad
\binom{n+k-1}{k}=\frac n{k}\binom{n+k-1}{k-1}
```

give

```math
U_5(n-1)=n^2(n-1)^2 B(n),
\qquad
B(n)=\sum_{k=1}^{n-1}kG_n(k)^2.
\tag{20}
```

It remains to prove $n^2\mid B(n)$. We shall use three elementary
integrality facts. First,

```math
\frac{G_n(k)}k
=\frac{(n-2)!(n+k-1)!}
{k!(k-1)!(n-k-1)!n!}
\in\mathbb Z.
\tag{21}
```

For completeness, Legendre's formula reduces (21), at every prime-power
$d$, to

```math
\left\lfloor\frac{n-2}{d}\right\rfloor
+\left\lfloor\frac{n+k-1}{d}\right\rfloor
-\left\lfloor\frac{k}{d}\right\rfloor
-\left\lfloor\frac{k-1}{d}\right\rfloor
-\left\lfloor\frac{n-k-1}{d}\right\rfloor
-\left\lfloor\frac n d\right\rfloor\geq0.
```

Writing $n\equiv r$ and $k\equiv s$ modulo $d$ turns the left side into

```math
-1_{r\leq1}
+\left\lfloor\frac{r+s-1}{d}\right\rfloor
+1_{s=0}
-\left\lfloor\frac{r-s-1}{d}\right\rfloor,
```

which is nonnegative by the four cases $s=0$, $0<s<r$,
$s=r$, and $s>r$. Second, the binomial identities

```math
\binom{n-1}{k}\binom{n+k-1}{k}
=\frac{n(n-1)}{k^2}G_n(k)
\tag{22}
```

and

```math
\binom{n+k-1}{k+1}
=\frac{n(n-1)}{k(k+1)}inom{n+k-1}{k-1}
\tag{23}
```

show respectively that $k^2\mid n(n-1)G_n(k)$ and that
$k(k+1)$ divides $n(n-1)\binom{n+k-1}{k-1}$.

### 5.2 An exact telescoping certificate

Set $t_k=kG_n(k)^2$ for $1\leq k<n$ and $t_n=0$. For $1\leq k<n$,

```math
\frac{t_{k+1}}{t_k}
=\frac{(k+1)(n-k-1)^2(n+k)^2}{k^5}.
\tag{24}
```

Define

```math
R_n(k)=\frac{3(k-1)^2}{k}-2n+\frac{2n}{k^2}
\tag{25}
```

and

```math
\begin{aligned}
E_n(k)={}&6k^4-4k^3n+16k^3-3k^2n^2-6k^2n+15k^2\\
&+2kn^3-7kn^2+5k+4n^3-8n^2+4n.
\end{aligned}
\tag{26}
```

Direct substitution in (24) gives the exact rational identity

```math
12t_k-igl(R_n(k+1)t_{k+1}-R_n(k)t_k\bigr)
=n^2\frac{G_n(k)^2E_n(k)}{k^3(k+1)}.
\tag{27}
```

The boundary terms vanish: $R_n(1)t_1=0$ and $t_n=0$. Hence

```math
12B(n)=n^2\sum_{k=1}^{n-1}
\frac{G_n(k)^2E_n(k)}{k^3(k+1)}.
\tag{28}
```

### 5.3 Local integrality of the certificate

Let $p\geq5$ divide $n$, put $a=v_p(n)$, and fix $k$. Write
$q=v_p(k)$ and $s=v_p(k+1)$, so $qs=0$. The polynomial in (26) has the
useful decomposition

```math
E_n(k)=k(k+1)(6k^2+10k+5)+nD_n(k)
\tag{29}
```

with $D_n(k)\in\mathbb Z[n,k]$. Thus

```math
v_p(E_n(k))\geq\min(a,q+s).
\tag{30}
```

Let $g=v_p(G_n(k))$. Equation (21) gives $g\geq q$. Equation (22)
gives $g\geq2q-a$, and (23) gives $g\geq s-a$.

If $q>0$ and $q\leq a$, then $2g+v_p(E_n(k))\geq3q$; if $q>a$, then
the bounds $g\geq2q-a$ and $v_p(E_n(k))\geq a$ give
$2g+v_p(E_n(k))\geq4q-a\geq3q$. If $s>0$, the analogous alternatives
$s\leq a$ and $s>a$ give respectively
$2g+v_p(E_n(k))\geq s$ and
$2g+v_p(E_n(k))\geq2s-a\geq s$. Therefore every summand on the
right of (28) is $p$-integral.

It follows that $v_p(12B(n))\geq2a$. Since $p\geq5$, the factor $12$ is
a $p$-adic unit, so $v_p(B(n))\geq2a$. Applying this to every prime
divisor of an integer $n$ coprime to $6$, equation (20) gives
$n^4\mid U_5(n-1)$ and proves Theorem 3. $\square$

## 6. Source and literature boundary

- A357510 states (6) for primes $p\geq5$.
- A357512 states the $m=2$ composite conjecture and proposes finite
  exceptional-prime sets for the family $m\geq2$.
- A July 2026 preprint by Chen, Wang, and Feng studies a reciprocal-power
  Apéry numerator family associated with A357513. Its local expansion is
  related in spirit, but it is a different sequence from the positive
  moments in (1).

Targeted searches by both OEIS identifiers and by the exact odd-moment
formula did not locate Theorems 1--3 in a publication. This is preliminary
routing evidence, not a priority certificate.

## 7. Verification

Run:

```text
python verification/related/verify_apery_odd_moment_prime_classification.py
```

The checker verifies the exact product identity, the local congruence (3),
the master congruence (5), Theorem 1, the residue formula (9), every exact
exceptional set in the table, the counterexample (17), the factorization
(20), the floor and divisibility lemmas (21)--(23), the telescoping
certificate (27), its local integrality, and Theorem 3 over a composite
test range.
