# Gaussian Wolstenholme sums: two conjectures proved and one sharply corrected

**Status:** complete draft proofs and exact certificates; unchecked by Fable
and not peer reviewed.

## 1. Source and notation

Let $p$ be an odd prime and put

```math
D_p=\{a+bi:1\leq a,b\leq p-1,\ p\nmid a^2+b^2\}.
```

Nikita Kalinin defines

```math
S_p^{(k)}=\sum_{z\in D_p}z^{-k}\in\mathbb Z_{(p)}[i]
\tag{1}
```

and

```math
g_p(X)=\prod_{z\in D_p}(X-z)\in\mathbb F_p[i][X].
\tag{2}
```

His 2025 paper *Wolstenholme's theorem over Gaussian integers* states:

- Conjecture 1: $S_p^{(k)}\equiv0\pmod{p^{m(k)}}$ for all $k\geq1$
  and $p>17$, where
  ```math
  m(k)=
  \begin{cases}
  4,&k\equiv1\pmod4,\\
  3,&k\equiv2\pmod4,\\
  2,&k\equiv3\pmod4,\\
  1,&k\equiv0\pmod4;
  \end{cases}
  \tag{3}
  ```
- Conjecture 2: an explicit geometric-series formula for $g_p$ when
  $p\equiv3\pmod4$, together with the question of finding the
  coefficients when $p\equiv1\pmod4$.
- Conjecture 3: a Lucas-type congruence modulo $p^3$ for the
  rectangular Gaussian binomial coefficient introduced in the source.

Theorem 1 below proves Conjecture 2 and answers its coefficient question.
Theorem 2 proves the natural stable-range version of Conjecture 1 and
exhibits its exact periodic obstruction.  In particular, Conjecture 1 as
printed fails for every prime in its stated range.  Theorem 4 proves
Conjecture 3 in the inert-prime setting $p\equiv3\pmod4$, $p>5$.

## 2. The polynomial conjecture

### Theorem 1

For every odd prime $p$, the following identities hold in
$\mathbb F_p[i][X]$.

If $p\equiv3\pmod4$, then

```math
g_p(X)
=
\frac{X^{p^2-1}-1}{X^{2(p-1)}-1}
=
\sum_{j=0}^{(p-1)/2}X^{2j(p-1)}.
\tag{4}
```

If $p\equiv1\pmod4$, then

```math
g_p(X)
=
\left(X^{p-1}-1\right)^{p-3}
=
\sum_{j=0}^{p-3}\binom{j+2}{2}X^{j(p-1)}.
\tag{5}
```

Thus the coefficients $b_j$ asked for in the source have the closed
form

```math
b_j\equiv\binom{j+2}{2}\pmod p.
\tag{6}
```

### Proof

Suppose first that $p\equiv3\pmod4$.  Then
$\mathbb F_p[i]\cong\mathbb F_{p^2}$, and $a^2+b^2=0$ forces
$a=b=0$.  Consequently, $D_p$ consists of all nonzero elements of
$\mathbb F_{p^2}$ except the two coordinate axes.  Hence

```math
\begin{aligned}
g_p(X)
&=
\frac{\prod_{z\in\mathbb F_{p^2}^{\times}}(X-z)}
{\prod_{a\in\mathbb F_p^\times}(X-a)
 \prod_{b\in\mathbb F_p^\times}(X-bi)}\\
&=
\frac{X^{p^2-1}-1}
{(X^{p-1}-1)(X^{p-1}+1)}.
\end{aligned}
\tag{7}
```

Here $i^{p-1}=-1$.  The geometric-series identity gives (4).

Now suppose that $p\equiv1\pmod4$, and choose $s\in\mathbb F_p$ with
$s^2=-1$.  The isomorphism

```math
\Phi:\mathbb F_p[i]\longrightarrow\mathbb F_p\times\mathbb F_p,
\qquad
a+bi\longmapsto(a+sb,a-sb)
\tag{8}
```

sends $D_p$ to

```math
\{(u,v)\in(\mathbb F_p^\times)^2:v\neq u,\ v\neq-u\}.
\tag{9}
```

For each fixed $u$, exactly $p-3$ values of $v$ occur.  Therefore
each coordinate of $\Phi(g_p(X))$ equals

```math
\prod_{u\in\mathbb F_p^\times}(X-u)^{p-3}
=
(X^{p-1}-1)^{p-3}.
\tag{10}
```

This proves the first equality in (5).  Finally,

```math
(-1)^{p-3-j}\binom{p-3}{j}
\equiv
\binom{j+2}{2}\pmod p,
\tag{11}
```

which proves the coefficient formula.

## 3. The exact obstruction to the higher-power conjecture

For $k\geq1$, let $r\in\{0,1,2,3\}$ be determined by

```math
k+r\equiv0\pmod4,
\qquad q=k+r.
\tag{12}
```

Thus $m(k)=r+1$.

### Theorem 2

For every odd prime $p$, the sum $S_p^{(k)}$ is divisible by $p^r$
in $\mathbb Z_{(p)}[i]$, and

```math
\frac{S_p^{(k)}}{p^r}
\equiv
(-1)^r\binom{k+r-1}{r}
\left(\frac{1+i}{2}\right)^r A_p(q)
\pmod p,
\tag{13}
```

where, if $p\equiv3\pmod4$,

```math
A_p(q)=
\begin{cases}
0,&p-1\nmid q,\\
2,&p-1\mid q,\ p^2-1\nmid q,\\
1,&p^2-1\mid q,
\end{cases}
\tag{14}
```

and, if $p\equiv1\pmod4$,

```math
A_p(q)=
\begin{cases}
0,&p-1\nmid q,\\
3,&p-1\mid q.
\end{cases}
\tag{15}
```

Consequently:

1. if $p-1\nmid k+r$, then
   ```math
   S_p^{(k)}\equiv0\pmod{p^{m(k)}};
   \tag{16}
   ```
2. in particular, (16) holds whenever $p>k+4$;
3. if $p-1\mid k+r$ and
   $p\nmid\binom{k+r-1}{r}$, then
   ```math
   v_p(S_p^{(k)})=r=m(k)-1.
   \tag{17}
   ```

### Proof

The affine quarter-turn

```math
T(z)=iz+p
\tag{18}
```

permutes $D_p$.  It has center

```math
h=\frac{p(1+i)}2
\tag{19}
```

and partitions $D_p$ into orbits of length four.  If $z=h+w$, its
orbit is $h+i^tw$, $0\leq t\leq3$.  Since $w$ is a $p$-adic
unit, the convergent binomial expansion gives

```math
\begin{aligned}
\sum_{t=0}^3(h+i^tw)^{-k}
&=
4\sum_{\substack{j\geq0\\k+j\equiv0\ (4)}}
(-1)^j\binom{k+j-1}{j}h^jw^{-k-j}.
\end{aligned}
\tag{20}
```

Modulo $p^{r+1}$, only the term $j=r$ can survive.  Summing over
orbit representatives and reducing $w\equiv z\pmod p$ yields (13),
with

```math
A_p(q)=\sum_{z\in D_p}z^{-q}\pmod p.
\tag{21}
```

It remains to evaluate (21).  If $p\equiv3\pmod4$, subtract the two
axes from $\mathbb F_{p^2}^\times$:

```math
A_p(q)
=
\sum_{z\in\mathbb F_{p^2}^\times}z^{-q}
-2\sum_{a\in\mathbb F_p^\times}a^{-q}.
\tag{22}
```

Because $4\mid q$, the usual finite-field power-sum formula gives
(14).  In the split case, use (8)--(9).  The first component of (21)
is

```math
(p-3)\sum_{u\in\mathbb F_p^\times}u^{-q},
\tag{23}
```

and the second component is identical.  This is $0$ when
$p-1\nmid q$ and $3$ when $p-1\mid q$, proving (15).

## 4. Infinite counterexamples to Conjecture 1

### Corollary 3

Conjecture 1 of the source is false for every prime $p>17$.

- If $p\equiv1\pmod4$, take
  ```math
  k=p-4,\qquad r=3,\qquad q=p-1.
  \tag{24}
  ```
  Then the coefficient in (13) is $4\pmod p$, $A_p(q)=3$, and
  ```math
  v_p(S_p^{(p-4)})=3,
  ```
  whereas the conjecture predicts at least $4$.

- If $p\equiv3\pmod4$, take
  ```math
  k=2p-5,\qquad r=3,\qquad q=2(p-1).
  \tag{25}
  ```
  Then the coefficient in (13) is $10\pmod p$, $A_p(q)=2$, and
  ```math
  v_p(S_p^{(2p-5)})=3,
  ```
  again one power short of the conjecture.

The smallest permitted example is

```math
S_{19}^{(33)}
\equiv
19^3(14+5i)
\pmod{19^4}.
\tag{26}
```

Thus the source's suggestion that a linear lower bound on $p$ in
terms of $k$ might be needed was correct.  Theorem 2 supplies the
simple sufficient bound $p>k+4$ and identifies the exact periodic
obstruction beyond that range.

## 5. The Gaussian Lucas congruence

For integers $A\geq C\geq1$ and $B\geq D\geq1$, define the
rectangular Gaussian binomial coefficient

```math
\left[\begin{matrix}A+Bi\\ C+Di\end{matrix}\right]
=
\frac{
\displaystyle\prod_{\substack{0\leq a<C\\0\leq b<D}}
(A+Bi-(a+bi))}
{\displaystyle\prod_{\substack{1\leq a\leq C\\1\leq b\leq D}}
(a+bi)}.
\tag{27}
```

### Theorem 4

Let $p>5$ be a prime with $p\equiv3\pmod4$.  Then

```math
\left[\begin{matrix}pA+pBi\\pC+pDi\end{matrix}\right]
\equiv
\left[\begin{matrix}A+Bi\\C+Di\end{matrix}\right]
\pmod {p^3}.
\tag{28}
```

Thus Conjecture 3 of the source holds in the inert-prime setting of the
preceding theorem in that paper.

### Proof

Put

```math
P(X,Y)=\prod_{\substack{1\leq a\leq X\\1\leq b\leq Y}}(a+bi).
\tag{29}
```

The expression in (27) is

```math
Q(A,B;C,D)=
\frac{P(A,B)P(A-C,B-D)}
{P(A-C,B)P(A,B-D)P(C,D)}.
\tag{30}
```

For $Z\in\mathbb Z[i]$, define one complete nonzero residue block

```math
H_p(Z)=
\prod_{\substack{1\leq a,b\leq p\$a,b)\neq(p,p)}}
(pZ+a+bi).
\tag{31}
```

We first claim

```math
H_p(Z)\equiv H_p(0)\pmod {p^3}.
\tag{32}
```

All factors in $H_p(0)$ are $p$-adic units because $p$ is inert.
Writing $\xi=a+bi$ and expanding the quotient gives

```math
\frac{H_p(Z)}{H_p(0)}
\equiv
1+pZ E_1+p^2Z^2E_2
\pmod {p^3},
\tag{33}
```

where

```math
E_1=\sum_\xi\xi^{-1},
\qquad
E_2=\sum_{\xi<\eta}(\xi\eta)^{-1}.
\tag{34}
```

The interior part of $E_1$ is $S_p^{(1)}$, which is $0\pmod
{p^4}$ by the Gaussian Wolstenholme theorem proved in the source.  The
two axes give, modulo $p^2$,

```math
\begin{aligned}
&\sum_{a=1}^{p-1}\frac1{a+ip}
+\sum_{b=1}^{p-1}\frac1{p+ib}\\
&\qquad\equiv
(1-i)\sum_{a=1}^{p-1}\frac1a
+p(1-i)\sum_{a=1}^{p-1}\frac1{a^2}
\equiv0\pmod {p^2}.
\end{aligned}
\tag{35}
```

The last step is classical Wolstenholme together with
$\sum a^{-2}\equiv0\pmod p$.  Hence $E_1\equiv0\pmod {p^2}$.
Modulo $p$, the block in (31) is exactly
$\mathbb F_{p^2}^{\times}$.  Therefore

```math
\sum_\xi\xi^{-1}=0,
\qquad
\sum_\xi\xi^{-2}=0
\quad\text{in }\mathbb F_{p^2},
\tag{36}
```

and

```math
2E_2=E_1^2-\sum_\xi\xi^{-2}\equiv0\pmod p.
\tag{37}
```

This proves (32).

Partitioning the $pX$-by-$pY$ rectangle into complete residue blocks
now gives the exact identity

```math
P(pX,pY)
=
p^{XY}P(X,Y)
\prod_{u=0}^{X-1}\prod_{v=0}^{Y-1}H_p(u+iv).
\tag{38}
```

By (32), the last product is congruent to $H_p(0)^{XY}\pmod{p^3}$
after the displayed powers of $p$ and $P(X,Y)$ are removed.
Substitute (38) into (30).  Both the powers of $p$ and the powers of
$H_p(0)$ cancel because

```math
AB+(A-C)(B-D)-(A-C)B-A(B-D)-CD=0.
\tag{39}
```

Thus

```math
\frac{Q(pA,pB;pC,pD)}{Q(A,B;C,D)}
\equiv1\pmod {p^3}.
\tag{40}
```

Finally, $Q(A,B;C,D)$ is $p$-integral.  Indeed, the contribution of
each power $p^j$ to its valuation is

```math
\left(
\left\lfloor\frac A{p^j}\right\rfloor
-\left\lfloor\frac{A-C}{p^j}\right\rfloor
\right)
\left(
\left\lfloor\frac B{p^j}\right\rfloor
-\left\lfloor\frac{B-D}{p^j}\right\rfloor
\right)
-
\left\lfloor\frac C{p^j}\right\rfloor
\left\lfloor\frac D{p^j}\right\rfloor,
\tag{41}
```

which is nonnegative because each parenthesized difference is at least
the corresponding final floor.  Multiplying (40) by this $p$-integral
quantity proves (28).

The prime $3$ is a real boundary: already
$(A,B,C,D)=(1,2,1,1)$ gives valuation $2$, not $3$, for the
difference in (28).  This does not contradict the source's preceding
inert-prime theorem, whose range begins at $p=7$.

## 6. Verification

The companion script:

1. multiplies the defining polynomial directly for small primes and
   verifies (4)--(6);
2. checks the normalized congruence (13) across small primes and
   exponents;
3. checks the counterexample family for every prime $19\leq p\leq199$;
4. verifies the certificate (26);
5. checks the block congruence (32) and the Gaussian Lucas congruence
   (28) over small rectangles.

Run:

```text
python verification/related/verify_gaussian_wolstenholme.py
```

## 7. Provenance

The source is:

- N. Kalinin, *Wolstenholme's theorem over Gaussian integers*,
  arXiv:2504.07978, 2025; subsequently published in *Functiones et
  Approximatio Commentarii Mathematici*.

A targeted search found no later proof of Conjecture 2 or Conjecture 3,
no published formula (6), and no counterexample to Conjecture 1.  A
current bibliographic index lists no papers citing the source.  This
priority search is not exhaustive and should be repeated before
circulation.
