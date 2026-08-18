# The A351858 cubic tower and its exact family boundary

**Status:** complete elementary proof candidate for the named $k=2$ tower;
complete counterexamples to the all-parameter extensions; exact checks pass;
independent review pending.

**Source boundary:** [OEIS A351858](https://oeis.org/A351858) defines the
named $k=2$ sequence and conjectures the same cubic tower for every $k\geq2$,
then proposes a still broader coefficient-slope family.  Sections 2--3
refute both broader assertions.  Sections 5--7 prove the named sequence.

## 1. The proposed family

For $k\geq1$, write

```math
G_k(x)=
\frac{(1+x+\cdots+x^k)^{k+1}}
     {(1+x+\cdots+x^{k-1})^k}
=\frac{(1-x^{k+1})^{k+1}}
       {(1-x)(1-x^k)^k}
\tag{1}
```

and

```math
u_k(N)=[x^N]G_k(x)^N.
\tag{2}
```

The page proposes

```math
u_k(np^r)\equiv u_k(np^{r-1})\pmod {p^{3r}}
\tag{3}
```

for all $k\geq2$, primes $p\geq5$, and positive $n,r$.

## 2. The first infinite counterexample family

Take any prime $p\geq5$ and set $k=p-1$.  Equation (1) gives

```math
G_{p-1}(x)^p=
\frac{(1-x^p)^{p^2}}
{(1-x)^p(1-x^{p-1})^{p(p-1)}}.
\tag{4}
```

Only degrees $0$ and $p-1$ from the final factor and degrees $0$ and $p$
from the numerator can contribute to $[x^p]$.  Hence

```math
u_{p-1}(p)
=\binom{2p-1}{p}+p^2(p-1)-p^2
=\binom{2p-1}{p}+p^2(p-2).
\tag{5}
```

Also $u_{p-1}(1)=[x]G_{p-1}(x)=1$.  Wolstenholme's congruence gives

```math
\binom{2p-1}{p}\equiv1\pmod {p^3}.
\tag{6}
```

Combining (5)--(6),

```math
u_{p-1}(p)-u_{p-1}(1)
\equiv p^2(p-2)\not\equiv0\pmod {p^3}.
\tag{7}
```

In fact the valuation is exactly two.

The smallest instance is

```math
u_4(5)-u_4(1)=201-1=200=2^3\cdot5^2.
\tag{8}
```

## 3. A second infinite counterexample family

Set $k=p$.  Now

```math
G_p(x)^p=
\frac{(1-x^{p+1})^{p(p+1)}}
{(1-x)^p(1-x^p)^{p^2}}.
\tag{9}
```

The numerator cannot affect degree $p$.  The two denominator contributions
give

```math
u_p(p)=\binom{2p-1}{p}+p^2,
\qquad
u_p(1)=1.
\tag{10}
```

Therefore

```math
u_p(p)-u_p(1)\equiv p^2\not\equiv0\pmod {p^3},
\tag{11}
```

again with exact valuation two.  At $p=5$ this is

```math
u_5(5)-u_5(1)=151-1=150=2\cdot3\cdot5^2.
\tag{12}
```

## 4. What survives the counterexamples

The obstruction occurs precisely when the prime divides one of the adjacent
cyclotomic step sizes $k$ or $k+1$.  In the Frobenius-logarithm language,
the offending reduced-log support then lands on the $p$-sublattice, so the
linear defect no longer vanishes.  This explains why a theorem proved only
under $p\nmid k(k+1)$ would not settle the page's uniform claim.

The named sequence A351858 has fixed $k=2$ and asks only for $p\geq5$, so
neither $p\mid k$ nor $p\mid k+1$ can occur.  Its cubic tower is a coherent
separate target, and it is proved below.  The exact disposition is therefore:

- the universal all-$k$ assertion is false;
- the broader $u_k(c,s;N)=[x^{cN}]G_k(x)^{sN}$ assertion is also false,
  because it contains $c=s=n=r=1$; and
- the named $k=2$ conjecture is true.

## 5. The named reduced logarithm

Put

```math
\phi(x)=G_2(x)=\frac{(1-x^3)^3}{(1-x)(1-x^2)^2},
\qquad
H(x)=\frac{\phi(x)}x.
\tag{13}
```

For a prime $p\geq5$, define

```math
U_{a,p}(x)=\sum_{\substack{j\geq1\\p\nmid j}}\frac{x^{aj}}j,
\qquad
L_p=U_{1,p}+2U_{2,p}-3U_{3,p}.
\tag{14}
```

Cancellation of the terms with index divisible by $p$ gives the exact
identity

```math
\frac{\phi(x)^p}{\phi(x^p)}=\exp(pL_p(x)).
\tag{15}
```

If $p\nmid j$, the coefficient of $x^j$ in $L_p$ is

```math
\frac{c(j)}j,
\qquad
c(j)=1+4\,1_{2\mid j}-9\,1_{3\mid j},
\tag{16}
```

and it is zero when $p\mid j$.  The periodic vector of $c$, indexed modulo
$6$, is

```math
(-4,1,5,-8,5,1).
\tag{17}
```

## 6. The six-residue Cartier lemma

### 6.1 A reciprocal-square interval identity

Let $P=p^e$ with $p\geq5$, and write

```math
R(t)=\sum_{\substack{1\le j\le t\\p\nmid j}}\frac1{j^2}.
```

Then

```math
5R(\lfloor P/3\rfloor)\equiv R(\lfloor P/6\rfloor)\pmod P.
\tag{18}
```

Indeed, the complete inverse-square sum over the units modulo $P$ is zero:
inversion permutes the units and their square sum is zero modulo $P$.
Pairing $j$ with $P-j$ therefore gives
$R(\lfloor P/2\rfloor)=0$.  Write $P=6q+\epsilon$ with
$\epsilon\in\{1,-1\}$.  The part of this half sum after
$R(\lfloor P/3\rfloor)$ is sent by $h=P-2j$ to the positive odd integers
at most $2q-1$.  Since $j^{-2}\equiv4h^{-2}\pmod P$, that tail is

```math
4R(\lfloor P/3\rfloor)-R(\lfloor P/6\rfloor),
```

which proves (18).

For $r\in\mathbb Z/6\mathbb Z$, put

```math
A_r(P)=\sum_{\substack{1\le v<P,\ p\nmid v\\v\equiv r\ (6)}}\frac1{v^2}.
\tag{19}
```

Pairing $v$ with $P-v$, using the vanishing of the even inverse-square
sum, and applying (18) gives, for some $\lambda\in\mathbb Z/P\mathbb Z$,

```math
(A_0,\ldots,A_5)=
\begin{cases}
\lambda(-5,-5,4,1,1,4),&P\equiv1\pmod6,\\
\lambda(-5,4,1,1,4,-5),&P\equiv-1\pmod6.
\end{cases}
\tag{20}
```

For example, when $P=6q+1$, pairing leaves three values
$A_0=A_1=a$, $A_2=A_5=b$, and $A_3=A_4=d$.  Equation (18) gives
$a=-5d$, while the even sum gives $a+b+d=0$, hence $b=4d$.
The case $P=6q-1$ is identical with the paired residue classes shifted.

### 6.2 The weighted convolution

Let $T=Pu$ and put $q_T(j)=c(j)c(T-j)$.  Direct convolution yields

```math
[x^T]L_p(x)^2
=\sum_{\substack{1\le j<T\\p\nmid j}}
\frac{q_T(j)}{j(T-j)}.
\tag{21}
```

Write $j=aP+v$ with $0\leq a<u$ and $1\leq v<P$.  Reducing (21) modulo
$P$ changes its denominator to $-v^2$.  Put
$\epsilon=P\pmod6$ and $s=u\pmod6$.  Complete blocks of six values of $a$
contribute a constant multiple of $\sum_rA_r=0$.  The remaining
autocorrelation vector

```math
f_{\epsilon,s}(v)=
\sum_{a=0}^{s-1}c(v+\epsilon a)c(\epsilon s-v-\epsilon a)
\tag{22}
```

has the following six possibilities.  For $\epsilon=1$ they are

```text
s=0: (  0,  0,  0,  0,  0,  0)
s=1: ( -4, -4,  5,-40,-40,  5)
s=2: (-19,-19,-28, 17, 17,-28)
s=3: ( 42, 42, 42, 42, 42, 42)
s=4: (-11,-11, -2,-47,-47, -2)
s=5: (-74,-74,-83,-38,-38,-83).
```

For $\epsilon=-1$, reflect each row.  Every displayed row has dot product
zero with the corresponding vector in (20).  Therefore

```math
v_p([x^T]L_p^2)\geq v_p(T)
\qquad(p\mid T).
\tag{23}
```

Equivalently, there is a $p$-integral series $K_p$ such that

```math
C_p(L_p^2)=p xK_p'(x),
\tag{24}
```

where $C_p(\sum a_jx^j)=\sum a_{pj}x^j$.

## 7. Proof of the named cubic tower

Let $N=np^r$ and $M=N/p$.  Equations (13) and (15) give

```math
u_2(N)-u_2(M)
=\operatorname{CT}H(x^p)^M\bigl(\exp(NL_p(x))-1\bigr).
\tag{25}
```

The linear term is zero: $H(x^p)^M$ is supported on the $p$-sublattice,
while $L_p$ has no exponent divisible by $p$.  For the quadratic term,
(24), Cartier extraction, and formal integration by parts give

```math
\begin{aligned}
\operatorname{CT}H(x^p)^M L_p^2
&=p\operatorname{CT}H(x)^M xK_p'(x)\\
&=-pM\operatorname{CT}K_p(x)H(x)^{M-1}xH'(x).
\end{aligned}
\tag{26}
```

The last constant coefficient is $p$-integral.  Multiplication by
$N^2/2$ therefore gives valuation at least $3r$.  Every exponential term
of degree $j\geq3$ has valuation at least

```math
jr-v_p(j!)\geq3r
\qquad(p\geq5).
```

Only finitely many terms can contribute to the constant coefficient, so
(25) proves

```math
\boxed{
u_2(np^r)\equiv u_2(np^{r-1})\pmod {p^{3r}}
}
\qquad(p\geq5).
\tag{27}
```

This is the complete supercongruence conjecture for the named A351858
sequence.  The counterexamples in Sections 2--3 show why it does not extend
uniformly to all $k$.

## 8. Verification

Run

```text
python verification/related/verify_a351858_cyclotomic_boundary.py
```

The exact checker verifies the published A351858 values, the cyclotomic
factorization, both counterexample formulas for every prime through $97$,
the exact valuation-two failures, the sixth-interval and six-residue lemmas,
the weighted quadratic Cartier estimate, and a grid of named cubic towers.
