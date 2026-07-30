# Binomial-quotient cancellation and three Bala families

**Status:** complete proof candidate; exact checks are supplied; conventional
review and a priority search are still pending

This note records two economical consequences of the
Ljunggren--Jacobsthal--Kazandzidis binomial scaling theorem.

1. A Laurent product of scaled binomial coefficients inherits the ordinary
   cubic tower whenever its values are $p$-integral.
2. A universal quadratic cancellation between adjacent scaling quotients
   proves the complete two-parameter conjecture on
   [OEIS A357509](https://oeis.org/A357509).
3. The same cancellation between the adjacent scaling quotients of
   $\binom{2n}{n}$ and $\binom{3n}{n}$ proves the full family conjectured
   on [OEIS A357568](https://oeis.org/A357568), including the exceptional
   prime $3$.

The first result closes the row-family conjecture on
[OEIS A364506](https://oeis.org/A364506).  The second is stronger than the
single sequence displayed on A357568.

## 1. Laurent binomial products

We use the standard adjacent-scale binomial congruence: if $p\ge5$ is
prime, $r\ge1$, and $0\le b\le a$, then

```math
\frac{\binom{a p^r}{b p^r}}
     {\binom{a p^{r-1}}{b p^{r-1}}}
\equiv 1 \pmod {p^{3r}}.
```

The quotient is a $p$-adic unit.  The usual statement with the additional
valuation of $ab(a-b)$ is stronger; only the displayed baseline is needed
here.

### Theorem 1: Laurent-product closure

Fix integers

```math
0\le \beta_j\le\alpha_j,
\qquad
e_j\in\mathbb Z
\quad (1\le j\le s),
```

and define

```math
F(n)=
\prod_{j=1}^{s}
\binom{\alpha_j n}{\beta_j n}^{e_j}.
```

Suppose $F(n)$ is $p$-integral for every $n\ge1$.  Then for every
prime $p\ge5$ and all $m,r\ge1$,

```math
F(mp^r)\equiv F(mp^{r-1})\pmod {p^{3r}}.
```

#### Proof

For each $j$, apply the adjacent-scale congruence with
$a=\alpha_jm$ and $b=\beta_jm$.  Its quotient $Q_j$ satisfies

```math
Q_j\equiv1\pmod {p^{3r}}.
```

The same is true of every integral power $Q_j^{e_j}$, including negative
powers because $Q_j$ is a unit.  Hence

```math
\frac{F(mp^r)}{F(mp^{r-1})}
=\prod_j Q_j^{e_j}
\equiv1\pmod {p^{3r}}.
```

Multiplication by the $p$-integral number $F(mp^{r-1})$ proves the
claim. $\square$

The integrality assumption matters.  It is exactly what prevents a
denominator in $F(mp^{r-1})$ from spending part of the cubic precision.

## 2. Application to A364506

For a fixed row $h\ge0$, the A364506 entry is

```math
T_h(n)=
\frac{(2n)!}{n!}\,
\frac{(2hn)!\,((2h+1)n)!}
     {(hn)!^2\,((h+1)n)!^2}.
```

The entry supplies an integral alternating sum for $T_h(n)$, so its
integrality is known.  More importantly, there is an exact Laurent-binomial
factorization:

```math
T_h(n)=
\binom{2n}{n}
\binom{2hn}{hn}
\binom{(2h+1)n}{hn}
\binom{(h+1)n}{hn}^{-1}.
```

Theorem 1 therefore gives the following result.

### Corollary 2: the complete A364506 row tower

For every row $h\ge0$, every prime $p\ge5$, and all $m,r\ge1$,

```math
\boxed{
T_h(mp^r)\equiv T_h(mp^{r-1})\pmod {p^{3r}}.
}
```

This proves the row-family supercongruence conjectured on A364506.  It is a
reduction to the classical binomial scaling theorem, not a new
supercongruence mechanism.  The neighboring A364509 entry already records
an analogous reduction.

## 3. The cancellation quotient

Put

```math
U_r=\{1\le u<p^r:p\nmid u\}
```

and, in $\mathbb Z_p$,

```math
H_j(r)=\sum_{u\in U_r}\frac1{u^j}.
```

We need two elementary bounds.

### Lemma 3: reduced harmonic sums

For every odd prime $p$, every $r\ge1$, and every $j\ge1$,

```math
v_p(H_j(r))\ge r-1.
```

If $j$ is odd, then

```math
v_p(H_j(r))\ge2r-1.
```

#### Proof

The first assertion is the standard power-sum estimate over
$(\mathbb Z/p^r\mathbb Z)^\times$.  It follows either by summing a
geometric progression along a generator of the cyclic unit group, or by
lifting each unit class from $p^s$ to $p^{s+1}$.  If
$p-1\nmid j$, the stronger bound $v_p(H_j(r))\ge r$ follows.

For odd $j$, pair $u$ with $p^r-u$.  Expanding in $\mathbb Z_p$
gives

```math
\frac1{u^j}+\frac1{(p^r-u)^j}
=-\frac{j p^r}{u^{j+1}}
+O\!\left(p^{2r}\right).
```

The first assertion applied to $H_{j+1}(r)$ makes the summed first term
divisible by $p^{2r-1}$, and the remaining terms have at least the same
valuation. $\square$

For $t\in\mathbb Z$, define the adjacent block quotient

```math
P_r(t)=
\prod_{u\in U_r}\left(1+\frac{t p^r}{u}\right).
```

We also use the standard Wolstenholme lift

```math
v_p(H_1(r))\ge2r\quad(p\ge5),
\qquad
v_3(H_1(r))\ge2r-1.
```

Together with the stronger even estimate
$v_p(H_2(r))\ge r$ for $p\ge5$, the logarithmic expansion used below gives,
for every integer $t$,

```math
v_p(P_r(t)-1)\ge3r\quad(p\ge5),
\qquad
v_3(P_r(t)-1)\ge3r-1.
\tag{13}
```

Cancellation of the factors whose indices are divisible by $p$ gives

```math
P_r(1)=
\frac{\binom{2p^r}{p^r}}{\binom{2p^{r-1}}{p^{r-1}}},
\qquad
P_r(2)=
\frac{\binom{3p^r}{p^r}}{\binom{3p^{r-1}}{p^{r-1}}}.
```

### Lemma 4: universal quadratic quotient cancellation

Let $r\ge2$, and, for every integer $t$, put

```math
E_r(t)=P_r(t)-1.
```

For every prime $p\ge5$ and all integers $a,b$,

```math
\boxed{
b(b+1)E_r(a)-a(a+1)E_r(b)
\equiv0\pmod {p^{3r+3}}.
}
\tag{14}
```

At $p=3$, the same expression is divisible by $3^{3r+2}$.  In
particular,

```math
E_r(2)-3E_r(1)\equiv0\pmod {3^{3r+2}}.
\tag{15}
```

#### Proof

The $p$-adic logarithm converges because $r\ge2$.  Write

```math
L_r(t)=\log P_r(t)
=\sum_{j\ge1}
\frac{(-1)^{j+1}}{j}\,
t^j p^{rj}H_j(r).
```

Pairing $u$ with $p^r-u$ also gives the exact convergent identity

```math
2H_1(r)+p^rH_2(r)
=-\sum_{j\ge2}p^{rj}H_{j+1}(r).
```

Using this identity to eliminate $H_1(r)$ gives

```math
\begin{aligned}
L_r(t)
={}&-\frac{t(t+1)}2p^{2r}H_2(r)\\
&+\sum_{j\ge3}
\left(
\frac{(-1)^{j+1}t^j}{j}-\frac t2
\right)p^{rj}H_j(r).
\end{aligned}
\tag{16}
```

Therefore the $H_2(r)$ term cancels from

```math
b(b+1)L_r(a)-a(a+1)L_r(b).
```

Every remaining coefficient has $p$-adic valuation at least
$-v_p(j)$.

For $j=3$, Lemma 3 gives valuation at least

```math
5r-1-v_p(3).
```

For $j\ge4$, it gives valuation at least

```math
(j+1)r-1-v_p(j).
```

When $r\ge2$, these bounds are at least $3r+3$ for $p\ge5$, and at
least $3r+2$ for $p=3$.  This proves the required congruence between
the logarithms.

Finally, (13) and $\log(1+E_r(t))=L_r(t)$ give

```math
v_p(L_r(t))\ge3r \quad(p\ge5),
\qquad
v_3(L_r(t))\ge3r-1.
```

All nonlinear terms in the exponential have valuation at least $6r$
for $p\ge5$ and at least $6r-2$ for $p=3$, so they lie beyond the
asserted precision.  Passing from logarithms back to $E_r(t)$ proves
(14).  The ternary statement follows in the same way; taking
$(a,b)=(2,1)$ and cancelling the $3$-adic unit $2$ gives (15).
$\square$

## 4. The complete A357509 two-parameter family

For integers $j,k$, not necessarily positive, define

```math
U_{j,k}(N)
=
k^2(k-1)\binom{jN}{N}
-j^2(j-1)\binom{kN}{N}.
\tag{17}
```

The sequence A357509 is the case $(j,k)=(3,2)$.

### Theorem 5: complete A357509 family

For every prime $p\ge5$, every $r\ge2$, and all integers $j,k$,

```math
\boxed{
U_{j,k}(p^r)\equiv U_{j,k}(p^{r-1})
\pmod {p^{3r+3}}.
}
\tag{18}
```

#### Proof

If $j=0$ or $k=0$, both sides of (18) vanish.  Assume $jk\ne0$ and
write

```math
X_j=\frac1j\binom{jp^{r-1}}{p^{r-1}},
\qquad
X_k=\frac1k\binom{kp^{r-1}}{p^{r-1}}.
\tag{19}
```

These are integers.  Exact factor cancellation and (13) give

```math
X_j=\prod_{s=1}^{r-1}P_s(j-1),
\qquad
X_k=\prod_{s=1}^{r-1}P_s(k-1),
```

and hence

```math
X_j\equiv X_k\equiv1\pmod {p^3}.
\tag{20}
```

Cancellation of the factors with indices divisible by $p$ gives

```math
\binom{jp^r}{p^r}=jX_j(1+E_r(j-1)),
\qquad
\binom{kp^r}{p^r}=kX_k(1+E_r(k-1)).
\tag{21}
```

Put $a=j-1$ and $b=k-1$.  The adjacent difference in (18) is

```math
jk\left(
b(b+1)X_jE_r(a)-a(a+1)X_kE_r(b)
\right).
\tag{22}
```

By Lemma 4, the same expression with $X_j=X_k=1$ vanishes modulo
$p^{3r+3}$.  The correction terms also vanish to that precision:
(20) supplies $p^3$, while the ordinary adjacent binomial congruence
supplies

```math
E_r(a)\equiv E_r(b)\equiv0\pmod {p^{3r}}.
```

Thus (22) is divisible by $p^{3r+3}$, proving (18).  The argument is
unchanged for negative $j$ or $k$, using the usual integral extension
of the binomial coefficient to a negative upper index. $\square$

## 5. The A357568 power family

For an integer $k\ge1$, define

```math
A_k(n)=
9\binom{2n}{n}^{k}
-k\,2^k\binom{3n}{n}.
```

The sequence A357568 is $A_2$.  Its OEIS entry conjectures the same tower
for every $k\ge1$.

### Theorem 6: complete enhanced tower

For every odd prime $p$, every $r\ge2$, and every $k\ge1$,

```math
\boxed{
A_k(p^r)\equiv A_k(p^{r-1})
\pmod {p^{3r+3}}.
}
```

#### Proof for $p\ge5$

Set

```math
X=\frac12\binom{2p^{r-1}}{p^{r-1}},
\qquad
Y=\frac13\binom{3p^{r-1}}{p^{r-1}}.
```

Telescoping the ordinary cubic binomial congruence from the first level
shows

```math
X\equiv Y\equiv1\pmod {p^3}.
```

With $E=E_r(1)$ and $G=E_r(2)$ as in Lemma 4,

```math
\binom{2p^r}{p^r}=2X(1+E),
\qquad
\binom{3p^r}{p^r}=3Y(1+G).
```

Since $v_p(E)\ge3r$,

```math
(1+E)^k=1+kE+O(p^{6r}).
```

Consequently, modulo $p^{3r+3}$, the adjacent difference of $A_k$ is

```math
3k2^k\left(3X^kE-YG\right).
```

Now

```math
3X^kE-YG
=3E(X^k-Y)-Y(G-3E).
```

The first term is divisible by $p^{3r+3}$, and Lemma 4 gives the same
bound for the second.  This proves the assertion.

#### Proof for $p=3$

The ternary Jacobsthal bound gives

```math
X\equiv Y\equiv1\pmod9,
\qquad
v_3(E)\ge3r-1.
```

The same calculation applies.  This time

```math
3E(X^k-Y)
```

has valuation at least $3r+2$, and Lemma 4 gives

```math
v_3(G-3E)\ge3r+2.
```

The outer factor $3$ supplies the final power.  The discarded
$E^2$ terms have valuation at least $6r$, which is no smaller than
$3r+3$.  Hence the stated congruence also holds at $p=3$. $\square$

For $k=1$, one has $A_1(n)=-a_{\mathrm{A357509}}(n)$.  Thus Theorem 6
also strengthens the named A357509 member to $p=3$.  Theorem 5 proves
the broader two-parameter A357509 conjecture in its stated range
$p\ge5$, while A357568 is the case $k=2$ of Theorem 6.

## 6. Verification and source boundary

Run

```text
python verification/related/verify_binomial_quotient_cancellation.py
```

The checker verifies:

- the A364506 Laurent factorization and cubic tower over many rows;
- the universal quotient cancellation in Lemma 4;
- Theorem 5 over positive and negative parameters;
- Theorem 6 for several primes, levels, and powers $k$; and
- equality cases showing that the exponent $3r+3$ is frequently attained.

These computations are regression checks, not the proof.

The external input is the classical binomial scaling congruence.  A useful
survey source is R. Meštrović,
[*Wolstenholme's theorem: its generalizations and extensions in the last
hundred and fifty years*](https://arxiv.org/abs/1111.3057).  No priority
claim is made until the two parameter families and the A364506 reduction
have been checked against the specialist literature.
