# A prime-power Gaussian Lucas congruence

## Status

**Complete proof candidate; independent review and a priority search are
required.**

This note strengthens the adjacent-scale pattern first found by exact
computation. It uses the rectangular Gaussian coefficient introduced by
Nikita Kalinin in
[*Wolstenholme's theorem over Gaussian integers*](https://arxiv.org/abs/2504.07978).

## 1. Statement

For integers $A\ge C\ge1$ and $B\ge D\ge1$, put

```math
Q(A,B;C,D)=
\frac{
\displaystyle\prod_{a=0}^{C-1}\prod_{b=0}^{D-1}
\bigl(A-a+(B-b)i\bigr)}
{\displaystyle\prod_{a=1}^{C}\prod_{b=1}^{D}(a+bi)}.
```

### Theorem

Let $p\ge7$ be a rational prime satisfying $p\equiv3\pmod4$, and let
$r\ge1$. Then

```math
Q(p^rA,p^rB;p^rC,p^rD)
\equiv
Q(p^{r-1}A,p^{r-1}B;p^{r-1}C,p^{r-1}D)
\pmod {p^{3r}}.
\tag{1}
```

At the exceptional inert prime $p=3$, the same argument gives

```math
Q(3^rA,3^rB;3^rC,3^rD)
\equiv
Q(3^{r-1}A,3^{r-1}B;3^{r-1}C,3^{r-1}D)
\pmod {3^{3r-1}}.
\tag{2}
```

Both exponents are attained in the exact experiments, so the uniform bounds
are sharp.

## 2. Complete unit blocks

Work in the unramified quadratic extension $\mathbb Z_p[i]$. For $r\ge1$,
let

```math
U_r=
\left\{
a+bi:
1\le a,b\le p^r,\quad
p\nmid a+bi
\right\}.
```

Because $p$ is inert, $p\nmid a+bi$ means that $p$ does not divide both
$a$ and $b$. Define

```math
S_{r,k}=\sum_{\xi\in U_r}\xi^{-k}.
\tag{3}
```

The two estimates needed below are the following.

### Lemma 1

For $p\ge7$,

```math
v_p(S_{r,1})\ge2r,
\qquad
v_p(S_{r,2})\ge r.
\tag{4}
```

For $p=3$,

```math
v_3(S_{r,1})\ge2r-1,
\qquad
v_3(S_{r,2})\ge r.
\tag{5}
```

### Proof

At level $r=1$, reduction modulo $p$ identifies $U_1$ with
$\mathbb F_{p^2}^{\times}$. Therefore

```math
S_{1,1}\equiv S_{1,2}\equiv0\pmod p.
\tag{6}
```

For $p\ge7$, the first estimate gains one additional power. The interior
part of $S_{1,1}$ is divisible by $p^4$ by the Gaussian Wolstenholme theorem.
The two axes satisfy

```math
\sum_{a=1}^{p-1}\frac1{a+ip}
+
\sum_{b=1}^{p-1}\frac1{p+ib}
\equiv0\pmod {p^2}
\tag{7}
```

by classical Wolstenholme together with
$\sum_{a=1}^{p-1}a^{-2}\equiv0\pmod p$. Hence
$v_p(S_{1,1})\ge2$.

It remains to lift the estimates. Every element of $U_{r+1}$ has a unique
expression

```math
\xi+p^rt,
\qquad
\xi\in U_r,\quad
t=a+bi,\quad 0\le a,b<p.
```

Put $M_j=\sum_t t^j$. Then

```math
M_0=p^2,\qquad v_p(M_1)\ge2,
\tag{8}
```

and, for $1\le j\le p-2$,

```math
v_p(M_j)\ge2.
\tag{9}
```

Indeed, expand $(a+bi)^j$ and separate the sums over $a$ and $b$.
Every one-variable power sum of exponent between $0$ and $p-2$ is divisible
by $p$; the exponent-$0$ sum is exactly $p$. We will also use
$v_p(M_2)\ge2$, which follows directly from the same expansion and remains
valid when $p=3$.

The convergent expansion

```math
(\xi+p^rt)^{-k}
=
\sum_{j\ge0}
(-1)^j
\binom{k+j-1}{j}
p^{rj}t^j\xi^{-k-j}
\tag{10}
```

gives, for $k=1$,

```math
S_{r+1,1}
=
\sum_{j\ge0}(-1)^jp^{rj}M_jS_{r,j+1}.
\tag{11}
```

For $p\ge7$, the $j=0$ term has valuation at least $2r+2$.
The $j=1$ term has valuation at least

```math
r+2+r=2r+2.
```

For $2\le j\le p-2$, (9) gives valuation at least $rj+2\ge2r+2$.
For $j\ge p-1$, the factor $p^{rj}$ alone has valuation at least
$r(p-1)\ge2r+2$. This proves the first estimate in (4) by induction.

When $p=3$, the target at level $r+1$ is $2r+1$. The $j=0$ term reaches
that value, the $j=1$ and $j=2$ terms are controlled by (8) and the
$M_2$ observation, and $j\ge3$ is controlled by $p^{rj}$. This proves the
first estimate in (5).

For $k=2$, (10) gives

```math
S_{r+1,2}
=
\sum_{j\ge0}
(-1)^j(j+1)p^{rj}M_jS_{r,j+2}.
\tag{12}
```

The $j=0$ term has valuation at least $r+2$, while every later term is
controlled by the same moment estimates. Thus
$v_p(S_{r+1,2})\ge r+1$ for both ranges of primes. This completes the
induction. ∎

## 3. Translation invariance at level r

Define the complete unit block

```math
H_{p,r}(Z)=
\prod_{\xi\in U_r}(p^rZ+\xi).
\tag{13}
```

### Lemma 2

For $p\ge7$,

```math
H_{p,r}(Z)\equiv H_{p,r}(0)\pmod {p^{3r}}.
\tag{14}
```

For $p=3$, the same congruence holds modulo $3^{3r-1}$.

### Proof

Since every $\xi\in U_r$ is a $p$-adic unit,

```math
\log\frac{H_{p,r}(Z)}{H_{p,r}(0)}
=
\sum_{k\ge1}
\frac{(-1)^{k+1}}{k}
p^{rk}Z^kS_{r,k}.
\tag{15}
```

For $p\ge7$, the $k=1$ term has valuation at least
$r+2r=3r$, and the $k=2$ term has valuation at least
$2r+r=3r$. For $k\ge3$,

```math
rk-v_p(k)\ge3r.
\tag{16}
```

Thus the logarithm lies in $p^{3r}\mathbb Z_p[i]$, and so does the
difference of the quotient from $1$.

For $p=3$, the $k=1$ estimate is $r+(2r-1)=3r-1$. Also,

```math
rk-v_3(k)\ge3r-1
\qquad(k\ge3),
```

with equality possible at $k=3$. This is the precise source of the
one-power loss at $p=3$. ∎

## 4. The rectangular cancellation

Put

```math
P(X,Y)=\prod_{a=1}^{X}\prod_{b=1}^{Y}(a+bi).
```

Then

```math
Q(A,B;C,D)=
\frac{P(A,B)P(A-C,B-D)}
{P(A-C,B)P(A,B-D)P(C,D)}.
\tag{17}
```

Separate the factors of $P(p^rX,p^rY)$ according to whether $p$ divides
both coordinates. The divisible factors contribute a copy of
$P(p^{r-1}X,p^{r-1}Y)$; all other factors form complete level-$r$ unit
blocks. Hence the exact identity

```math
P(p^rX,p^rY)
=
p^{p^{2r-2}XY}
P(p^{r-1}X,p^{r-1}Y)
\prod_{u=0}^{X-1}\prod_{v=0}^{Y-1}
H_{p,r}(u+iv).
\tag{18}
```

Substitute (18) into the five occurrences of $P$ in (17). Both the explicit
powers of $p$ and the constant factors $H_{p,r}(0)$ cancel because

```math
AB+(A-C)(B-D)-(A-C)B-A(B-D)-CD=0.
\tag{19}
```

Lemma 2 therefore gives

```math
\frac{Q(p^rA,p^rB;p^rC,p^rD)}
{Q(p^{r-1}A,p^{r-1}B;p^{r-1}C,p^{r-1}D)}
\equiv1\pmod {p^{3r}}
\tag{20}
```

for $p\ge7$, with modulus $3^{3r-1}$ at $p=3$.

Finally, the lower-scale coefficient is $p$-integral. At each level $p^j$,
its valuation contribution is

```math
\left(
\left\lfloor\frac A{p^j}\right\rfloor
-
\left\lfloor\frac{A-C}{p^j}\right\rfloor
\right)
\left(
\left\lfloor\frac B{p^j}\right\rfloor
-
\left\lfloor\frac{B-D}{p^j}\right\rfloor
\right)
-
\left\lfloor\frac C{p^j}\right\rfloor
\left\lfloor\frac D{p^j}\right\rfloor,
\tag{21}
```

which is nonnegative. Multiplying (20) by the lower-scale coefficient proves
(1) and (2). ∎

## 5. Checks and remaining review

The exact companion experiment recovers:

- valuation $3r$ throughout the tested inert-prime grids;
- the deep witnesses $(p,r)=(7,4),(11,3),(19,3)$;
- the sharp $3r-1$ pattern at $p=3$; and
- failure of the unnormalized split-prime analogue.

Run:

```text
python verification/related/experiment_gaussian_lucas_scaling.py
```

The main review targets are the moment bounds in Lemma 1, the use of the
Gaussian Wolstenholme theorem in the base case, and the exact block
factorization (18). No claim of novelty should be made before a broader
priority search and independent mathematical review.
