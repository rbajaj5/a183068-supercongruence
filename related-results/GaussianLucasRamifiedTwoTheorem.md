# The ramified prime in the Gaussian Lucas congruence

## Status

**Complete proof candidate; independent review and a priority search are
required.**

This note proves the adjacent-scale ratio congruence at the ramified Gaussian
prime. It does not rely on the inert-prime unit-block lemma, which is
inapplicable at $2$.

Put

```math
\varpi=1+i,
\qquad
v=v_\varpi,
```

with $v(\varpi)=1$. Thus $2=-i\varpi^2$.

For $a\ge c\ge1$ and $b\ge d\ge1$, define

```math
Q(a,b;c,d)
=
\prod_{x=0}^{c-1}\prod_{y=0}^{d-1}
\frac{(a-x)+i(b-y)}{(x+1)+i(y+1)}.
\qquad\text{(1)}
```

Equation (1) fixes a specific element of $\mathbb Q(i)$; it is not an
associate class, so no unit choice enters the ratio below. Reindexing the two
coordinates gives the exact consistency relation

```math
Q(b,a;d,c)=\overline{Q(a,b;c,d)}.
```

Thus conjugation preserves every valuation statement and the leading residue
after reduction modulo $\varpi$.

## 1. The theorem

For $A\ge C\ge1$, $B\ge D\ge1$, and $r\ge2$, put

```math
R_{2,r}=
\frac{Q(2^rA,2^rB;2^rC,2^rD)}
{Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D)}.
\qquad\text{(2)}
```

### Theorem

One has

```math
v(R_{2,r}-1)\ge6r-3.
\qquad\text{(3)}
```

In fact, put

```math
g=A-C+i(B-D).
```

If $g\ne0$, then the exact valuation is

```math
v(R_{2,r}-1)
=
6r-3+v\!\left(CDg\right).
\qquad\text{(3a)}
```

If $g=0$, then $A=C,\ B=D$, and $R_{2,r}=1$.

More precisely,

```math
\frac{R_{2,r}-1}{\varpi^{6r-3}}
\equiv
CD(A+B-C-D)
\pmod\varpi.
\qquad\text{(4)}
```

Consequently (3) is an equality exactly when $C,D$, and
$A+B-C-D$ are odd.

If

```math
\Delta_{2,r}
=
Q(2^rA,2^rB;2^rC,2^rD)
-
Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D),
\qquad\text{(5)}
```

then one also has

```math
v(\Delta_{2,r})\ge6r-4.
\qquad\text{(6)}
```

The restriction $r\ge2$ is necessary: already at $r=1$, the ratio can
have valuation $1$.

## 2. Reciprocal sums in the mixed block

Let

```math
U_r=
\left\{
a+bi:
1\le a,b\le2^r,\quad
\text{\(a,b\) are not both even}
\right\}
\qquad\text{(7)}
```

and, for $k\ge1$, let

```math
S_{r,k}=\sum_{\xi\in U_r}\xi^{-k}.
\qquad\text{(8)}
```

The elements of $U_r$ do not all have valuation zero: an odd--odd point
has valuation one. This is why the inert-prime proof cannot simply be
specialized to $p=2$.

### Lemma 1

For every $r\ge2$,

```math
v(S_{r,1})=4r-3.
\qquad\text{(9)}
```

For every $r\ge2$ and $k\ge2$,

```math
v(S_{r,k})\ge4r-2k.
\qquad\text{(10)}
```

### Proof

The finite base $r=2$ is exact. Put $D_0=16575$. Direct addition over the
twelve elements of $U_2$ gives the more compact integer table

**Table (11): exact $r=2$ base certificate**

| $k$ | $2D_0^kS_{2,k}$ | $v(S_{2,k})$ |
| ---: | --- | ---: |
| $1$ | $2^3\cdot10879(1-i)$ | $5$ |
| $2$ | $-2^4\cdot43604239i$ | $6$ |
| $3$ | $-2^2\cdot850577462821(1+i)$ | $3$ |
| $4$ | $-2\cdot20911814332048969$ | $0$ |
| $5$ | $-2^5\cdot9544029745743666769(1-i)$ | $9$ |
| $6$ | $2^2\cdot1220198154624646431442789i$ | $2$ |
| $7$ | $40476461909732086340946683071(1+i)$ | $-1$ |

The number $D_0$ and every displayed scalar cofactor are odd. Since
$v(2)=2$, the table proves (9) and (10) for $1\le k\le7$. In
particular,

```math
S_{2,1}=\frac{43516}{16575}(1-i),
\qquad
\frac{S_{2,1}}{\varpi^5}
=
\frac{10879}{16575}i
\equiv1\pmod\varpi.
\qquad\text{(12)}
```

If $k\ge8$, every $\xi\in U_2$ has $v(\xi)\le1$, so

```math
v(S_{2,k})\ge-k\ge8-2k.
\qquad\text{(13)}
```

This completes the base case for every $k$.

For the lift, put

```math
T=\{0,1,i,1+i\},
\qquad
M_j=\sum_{t\in T}t^j.
\qquad\text{(14)}
```

Then

```math
M_0=4,\qquad v(M_1)=3,\qquad v(M_j)\ge0\quad(j\ge1).
\qquad\text{(15)}
```

Every element of $U_{r+1}$ has a unique expression

```math
\xi+2^rt,
\qquad
\xi\in U_r,\quad t\in T.
\qquad\text{(16)}
```

Since $v(\xi)\le1$, the binomial expansion converges for $r\ge2$ and
gives

```math
S_{r+1,k}
=
\sum_{j\ge0}
(-1)^j
\binom{k+j-1}{j}
2^{rj}M_jS_{r,k+j}.
\qquad\text{(17)}
```

Assume (10) at level $r$. For $k\ge2$, the $j=0$ term in (17) has
valuation at least

```math
4+(4r-2k)=4(r+1)-2k.
\qquad\text{(18)}
```

For $j\ge1$, the corresponding term has valuation at least

```math
2rj+v(M_j)+4r-2(k+j)
=
4r-2k+2j(r-1)+v(M_j).
\qquad\text{(19)}
```

If $r\ge3$, this is at least the target in (18). If $r=2$, it is at
least the target when $j\ge2$, while the remaining case $j=1$ gains
three powers from $M_1$. The lower bound in (19) tends to infinity with
$j$, so the entire infinite tail is controlled. This proves (10) at
level $r+1$.

For $k=1$, the $j=0$ term has valuation exactly

```math
4+(4r-3)=4r+1.
\qquad\text{(20)}
```

Using (10), the $j$-th term for $j\ge1$ has valuation at least

```math
4r-2+2j(r-1)+v(M_j).
\qquad\text{(21)}
```

For $j=1$, (15) puts this at least two powers beyond (20). For $j\ge2$,
it is at least one power beyond (20), and the bound tends to infinity with
$j$. Hence

```math
S_{r+1,1}
\equiv
4S_{r,1}
\pmod{\varpi^{4r+2}}.
\qquad\text{(22)}
```

Since $4=-\varpi^4$, (22) and the exact base valuation in (11) prove (9)
at every level. ∎

## 3. Translation of a complete mixed block

Define

```math
H_r(Z)=\prod_{\xi\in U_r}(2^rZ+\xi).
\qquad\text{(23)}
```

### Lemma 2

For $r\ge2$ and $Z\in\mathbb Z[i]$,

```math
\frac{H_r(Z)}{H_r(0)}
\equiv
1+2^rZS_{r,1}
\pmod{\varpi^{6r-2}}.
\qquad\text{(24)}
```

### Proof

Every quotient $2^rZ/\xi$ has valuation at least $2r-1$, so the
$\varpi$-adic logarithm converges. More precisely, $r\ge2$ puts every factor
in $1+\varpi^3\mathcal O$. Over $\mathbb Q_2(i)$ the exponential requires
valuation greater than $2$, so logarithm and exponential are inverse on this
depth-three neighborhood. The nontrivial fourth roots of unity do not enter:
$v(i-1)=v(-i-1)=1$ and $v(-1-1)=2$. It gives

```math
\log\frac{H_r(Z)}{H_r(0)}
=
\sum_{k\ge1}
\frac{(-1)^{k+1}}{k}
2^{rk}Z^kS_{r,k}.
\qquad\text{(25)}
```

The $k=1$ term has valuation at least $6r-3$. For $k\ge2$, Lemma 1
gives the lower bound

```math
2rk-2v_2(k)+4r-2k.
\qquad\text{(26)}
```

This is at least $6r-2$, because

```math
(r-1)(k-1)\ge v_2(k).
\qquad\text{(27)}
```

The lower bound in (26) tends to infinity with $k$, so the logarithmic
tail converges uniformly. Thus (25) is congruent to $2^rZS_{r,1}$ modulo
$\varpi^{6r-2}$. Since this leading term has valuation at least
$6r-3\ge9$, all nonlinear terms in its exponential are beyond the same
modulus. This proves (24). ∎

## 4. Rectangular cancellation

Put

```math
P(X,Y)=\prod_{a=1}^{X}\prod_{b=1}^{Y}(a+bi).
\qquad\text{(28)}
```

Then

```math
Q(A,B;C,D)=
\frac{P(A,B)P(A-C,B-D)}
{P(A-C,B)P(A,B-D)P(C,D)}.
\qquad\text{(29)}
```

Separating the points whose two coordinates are even gives the exact block
factorization

```math
\begin{aligned}
P(2^rX,2^rY)
={}&
2^{\,2^{2r-2}XY}
P(2^{r-1}X,2^{r-1}Y)\\
&\mathrel{}\times
\prod_{u=0}^{X-1}\prod_{v=0}^{Y-1}H_r(u+iv).
\end{aligned}
\qquad\text{(30)}
```

Substitute (30) into the five occurrences of $P$ in (29). The explicit
powers of $2$ and the factors $H_r(0)$ cancel because

```math
AB+(A-C)(B-D)-(A-C)B-A(B-D)-CD=0.
\qquad\text{(31)}
```

For a function $f$, define

```math
\begin{aligned}
\Phi(f)={}&
\sum_{u<A,\,v<B}f(u+iv)
+\sum_{u<A-C,\,v<B-D}f(u+iv)\\
&-\sum_{u<A-C,\,v<B}f(u+iv)
-\sum_{u<A,\,v<B-D}f(u+iv)\\
&-\sum_{u<C,\,v<D}f(u+iv).
\end{aligned}
\qquad\text{(32)}
```

Direct summation gives

```math
\Phi(1)=0,
\qquad
\Phi(Z)=CD\bigl(A-C+i(B-D)\bigr).
\qquad\text{(33)}
```

Lemma 2 and the fact that
$v(2^rS_{r,1})=6r-3$ now give

```math
R_{2,r}-1
\equiv
2^rS_{r,1}\,
CD\bigl(A-C+i(B-D)\bigr)
\pmod{\varpi^{6r-2}}.
\qquad\text{(34)}
```

Here multiplication and inversion preserve the linear expansion:
$(1+cZ+O(\varpi^m))^{-1}=1-cZ+O(\varpi^m)$, because
$v(c)=m-1$ and $2v(c)\ge m$.

The coefficient

```math
\frac{2^rS_{r,1}}{\varpi^{6r-3}}
\qquad\text{(35)}
```

is a unit of the $\varpi$-adic valuation ring by Lemma 1. Its residue
field is $\mathbb F_2$, so every unit reduces to $1$. Also
$i\equiv1\pmod\varpi$.
Dividing (34) by $\varpi^{6r-3}$ therefore proves (4), and hence the
original leading-residue assertion. The stronger exact formula (3a) requires
a relative, rather than absolute, estimate on the higher moments. We prove
it next. ∎

## 5. Relative error and the exact valuation

Retain

```math
g=A-C+i(B-D),
\qquad
t=v(CDg),
```

and suppose first that $g\ne0$. The five-rectangle functional has the
exact translated-corner form

```math
\Phi(f)
=
\sum_{u=0}^{C-1}\sum_{v=0}^{D-1}
\left(
f(u+iv+g)-f(u+iv)
\right).
\qquad\text{(35a)}
```

This identity is obtained by cancelling the four overlapping rectangles in
(32). For $k\ge1$, define

```math
q_k(z,g)=\frac{(z+g)^k-z^k}{g}
\in\mathbb Z[i][z,g]
```

and let angle brackets denote the normalized rectangular average over
$0\le u<C,\ 0\le v<D$. Then

```math
\Phi(Z^k)=CDg\,\mathcal B_k,
\qquad
\mathcal B_k=\left\langle q_k(u+iv,g)\right\rangle.
\qquad\text{(35b)}
```

The normalized average need not be a Gaussian integer. The following
elementary power-sum estimate controls its possible denominator.

### Lemma 3

For $N\ge1$ and $m\ge0$,

```math
v_2\!\left(
\frac1N\sum_{j=0}^{N-1}j^m
\right)\ge-1.
\qquad\text{(35c)}
```

Consequently, if $P\in\mathbb Z[i][u,v]$, then

```math
v\!\left(
\frac1{CD}
\sum_{u=0}^{C-1}\sum_{v=0}^{D-1}P(u,v)
\right)\ge-4.
\qquad\text{(35d)}
```

#### Proof

For $m=0$, the normalized average in (35c) equals $1$. For $m\ge1$,
put $T_m(N)=\sum_{j<N}j^m$. If $N=2M$, expansion of
$(j+M)^m$ gives

```math
T_m(2M)=2T_m(M)+M K
```

for an integer $K$. Induction on $v_2(N)$, with the odd case
immediate, gives

```math
v_2(T_m(N))\ge v_2(N)-1,
```

which is (35c). Expand $P$ into monomials. Each normalized
one-variable power sum loses at most one ordinary $2$-adic power.
Since $v(2)=2$, a product of two such averages loses at most four
$\varpi$-powers. The ultrametric inequality proves (35d). ∎

Applied to (35b), Lemma 3 gives

```math
v(\mathcal B_k)\ge-4.
\qquad\text{(35e)}
```

Two low moments have better bounds. Directly,

```math
\mathcal B_2
=
2\langle u+iv\rangle+g
=
A-1+i(B-1)
\in\mathbb Z[i].
\qquad\text{(35f)}
```

Also,

```math
\mathcal B_4
=
4\langle z^3\rangle
+6g\langle z^2\rangle
+4g^2\langle z\rangle
+g^3.
\qquad\text{(35g)}
```

Writing

```math
\mu_m(N)=\frac1N\sum_{j=0}^{N-1}j^m,
```

one has

```math
\begin{aligned}
\langle z\rangle
&=\mu_1(C)+i\mu_1(D),\\
\langle z^2\rangle
&=\mu_2(C)-\mu_2(D)+2i\mu_1(C)\mu_1(D).
\end{aligned}
```

Lemma 3 applied termwise, and the analogous binomial expansion of
$\langle z^3\rangle$, therefore give

```math
v(\langle z\rangle)\ge-2,\qquad
v(\langle z^2\rangle)\ge-2,\qquad
v(\langle z^3\rangle)\ge-4.
```

The coefficients $4,6,4$ in (35g) compensate these possible losses, so
$v(\mathcal B_4)\ge0$.

Now write

```math
a_{r,k}
=
\frac{(-1)^{k+1}}{k}2^{rk}S_{r,k}.
```

Lemma 1 gives, for $k\ge2$,

```math
v(a_{r,k})
\ge
4r+2k(r-1)-2v_2(k).
\qquad\text{(35h)}
```

If $k\ge3$ and $(r,k)\ne(2,4)$, then

```math
(r-1)(k-1)\ge v_2(k)+2.
```

Thus (35h) is at least $6r+2$, and (35b), (35e) imply

```math
v\!\left(a_{r,k}\Phi(Z^k)\right)
\ge
t+6r-2.
\qquad\text{(35i)}
```

For $k=2$, (35f) and (35h) give

```math
v(a_{r,2})\ge8r-6\ge6r-2,
```

so (35i) again holds. In the remaining case $(r,k)=(2,4)$,
(35g) gives $v(\mathcal B_4)\ge0$, while (35h) gives
$v(a_{2,4})\ge12>10=6r-2$. Hence (35i) holds for every
$k\ge2$, and the bounds tend to infinity with $k$.

Applying (25) to the five normalized block products gives the exact
identity

```math
\log R_{2,r}
=
\sum_{k\ge1}a_{r,k}\Phi(Z^k).
```

The preceding estimates therefore strengthen (34) to

```math
\log R_{2,r}
=
2^rS_{r,1}\,CDg
+O\!\left(\varpi^{\,t+6r-2}\right).
\qquad\text{(35j)}
```

The first term has exact valuation $t+6r-3$ by Lemma 1. This is at
least $9$, so the $\varpi$-adic exponential preserves its valuation
and its relative one-power error. Thus

```math
R_{2,r}-1
=
2^rS_{r,1}\,CDg\,(1+\varpi\eta)
```

for some $\eta\in\mathcal O_{\mathbb Q_2(i)}$. This proves (3a). If
$g=0$, (35a) makes the five-rectangle functional vanish identically,
so $R_{2,r}=1$.
∎

## 6. The denominator loss and the difference

It remains to account for the fact that $Q$ need not itself be a
$\varpi$-adic integer.

For $u,v\ge0$, define

```math
w(a,b)=v(a+bi),
\qquad
W(u,v;C,D)
=
\sum_{a=u+1}^{u+C}\sum_{b=v+1}^{v+D}w(a,b).
\qquad\text{(36)}
```

Then

```math
v(Q(A,B;C,D))
=
W(A-C,B-D;C,D)-W(0,0;C,D).
\qquad\text{(37)}
```

### Lemma 4

For every admissible rectangle,

```math
v(Q(A,B;C,D))\ge-1.
\qquad\text{(38)}
```

Moreover,

```math
v(Q(2A,2B;2C,2D))
=
v(Q(A,B;C,D)).
\qquad\text{(39)}
```

### Proof

Write

```math
C=2c+\varepsilon,
\qquad
D=2d+\delta,
\qquad
\varepsilon,\delta\in\{0,1\}.
\qquad\text{(40)}
```

In the translated intervals, let $e=c+\alpha$ and $f=d+\beta$ be the
numbers of even coordinates. Here
$\alpha\in\{0,\varepsilon\}$ and
$\beta\in\{0,\delta\}$. Since

```math
w(2x,2y)=2+w(x,y),
\qquad
w(\text{odd},\text{odd})=1,
\qquad\text{(41)}
```

and mixed-parity pairs have weight zero, parity decomposition gives

```math
W(u,v;C,D)
=
W(\lfloor u/2\rfloor,\lfloor v/2\rfloor;e,f)
+2ef+(C-e)(D-f).
\qquad\text{(42)}
```

At the origin,

```math
W(0,0;C,D)
=
W(0,0;c,d)+2cd+(c+\varepsilon)(d+\delta).
\qquad\text{(43)}
```

The difference of the elementary correction terms in (42) and (43) is

```math
L=
\alpha(d-\delta)
+\beta(c-\varepsilon)
+3\alpha\beta.
\qquad\text{(44)}
```

We prove (38) by strong induction on $C+D$. If $c,d\ge1$, then
$L\ge0$. Since $e\ge c$, $f\ge d$, and all weights are nonnegative,
the translated $e$-by-$f$ sum is at least the translated
$c$-by-$d$ sum. The induction hypothesis applied to that smaller
rectangle therefore gives a lower bound of $-1$.

If $c=0$ or $d=0$, the smaller origin rectangle is empty, the translated
weighted sum is nonnegative, and the four possibilities for
$\alpha,\beta$ in (44) give $L\ge-1$. This proves (38).

For scale invariance, put $V(X,Y)=W(0,0;X,Y)$. Taking even side lengths
in (42) gives

```math
V(2X,2Y)=V(X,Y)+3XY.
\qquad\text{(45)}
```

Substitute (45) into the five-product valuation formula arising from (29).
The added area terms cancel by (31), proving (39). ∎

Iterating (39) shows that the lower-scale coefficient in (5) has valuation
at least $-1$. Since

```math
\Delta_{2,r}
=
Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D)
(R_{2,r}-1),
\qquad\text{(46)}
```

(3), (38), and (39) prove (6).

## 7. Exact checks and review boundary

The active review obligations and the 2026-08-16 checkpoint are maintained in
the [GWL-TWO audit packet](GWLTwoAuditPacket.md).

The companion exact-arithmetic script verifies the full exact formula (3a)
on all admissible rectangles with $A,B\le6$, at both $r=2$ and $r=3$:
810 checks with no mismatch. At each scale, 72 of 405 ratios attain the
lower bound. It also checks a targeted rectangle with excess valuation
$53$ at four consecutive scales.

Run:

```text
python verification/related/experiment_gaussian_lucas_scaling.py
python verification/related/verify_gaussian_lucas_ramified_audit.py
```

The main independent-review targets are:

1. the twelve-term base calculation (11);
2. the uniform tail estimates in (19), (21), and (26);
3. the exact block factorization (30);
4. the use of the five-term functional with inverse block factors; and
5. the normalized power-sum estimate and exceptional moments in Section 5;
6. the parity induction in Lemma 4.

No novelty claim should be made before a priority search and independent
review.
