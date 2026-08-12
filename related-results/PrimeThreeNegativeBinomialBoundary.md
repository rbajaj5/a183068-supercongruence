# The exact prime-three boundary for negative-binomial prefixes

**Status:** complete elementary all-level renormalization theorem, maximal
cubic parameter subclass, and sharp counterexamples outside that subclass.

**Source boundary:** this note continues the August 11, 2026 mixed-binomial
direction proposed by Peter Bala. The residue calculation below was developed
in this repository. No literature-priority claim is made.

## 1. Setup

For positive integers $a,b,c$, put

```math
U_{a,b;c}(N)=
\sum_{k=0}^{cN}\binom{-aN}{k}\binom{-bN}{k}.
\qquad\text{(1)}
```

The general prefix theorem proves a $p^{3r}$ adjacent tower for every prime
$p\geq5$. The prime $3$ is not merely absent from that proof: it has a real
quadratic obstruction. This note computes the obstruction exactly.

Use the constant-term notation

```math
H(t)=\frac1{1-t},
\qquad
G(x,t)=\frac{t^{-c}}{(1-x)^a(1-t/x)^b},
\qquad y=\frac tx.
\qquad\text{(2)}
```

Then

```math
U_{a,b;c}(N)=\operatorname{CT}_{x,t}H(t)G(x,t)^N.
\qquad\text{(3)}
```

Define the three rational functions over $\mathbb F_3$:

```math
X=\frac{x}{(1-x)^2},
\qquad
Y=\frac{y}{(1-y)^2},
\qquad
Z=\frac{xy}{(1-x)(1-y)}.
\qquad\text{(4)}
```

## 2. Exact first-defect formula

### Theorem 1

For all positive integers $a,b,c,n$,

```math
\boxed{
\frac{U_{a,b;c}(3n)-U_{a,b;c}(n)}9
\equiv
\frac{n^2}{2}\operatorname{CT}_{x,t}
H G^n
\left[
a^2X+abZ+b^2Y+n(aX+bY)
\right]
\pmod3.
}
\qquad\text{(5)}
```

The quotient on the left is integral. Formula (5) is therefore an exact
criterion for whether the prime-level modulus improves from $3^2$ to
$3^3$.

### Proof

Let

```math
V(z)=\sum_{\substack{j\geq1\\3\nmid j}}\frac{z^j}{j},
\qquad
L=aV(x)+bV(y).
\qquad\text{(6)}
```

As in the general prefix proof,

```math
\frac{G(x,t)^3}{G(x^3,t^3)}=\exp(3L).
```

Hence

```math
U(3n)-U(n)=
\operatorname{CT}H G(x^3,t^3)^n
\left(\exp(3nL)-1\right).
\qquad\text{(7)}
```

The linear term has zero constant coefficient: every $x$-exponent in $L$
is prime to $3$, while the $x$-exponents of $G(x^3,t^3)^n$ are divisible
by $3$. For degrees $j\geq4$,

```math
v_3\!\left(\frac{(3n)^j}{j!}\right)\geq3.
```

Thus, modulo $27$, only the quadratic and cubic terms remain. If
$\mathcal C_3$ denotes the two-variable Cartier operator, then

```math
\frac{U(3n)-U(n)}9
\equiv
\frac{n^2}{2}\operatorname{CT}
\mathcal C_3(HL^2)G^n
+\frac{n^3}{2}\operatorname{CT}
\mathcal C_3(HL^3)G^n
\pmod3.
\qquad\text{(8)}
```

It remains to evaluate two finite-field Cartier images. In $\mathbb F_3$,

```math
V(z)=\frac{z-z^2}{1-z^3}=\frac{z}{(1-z)^2}.
\qquad\text{(9)}
```

Direct residue-class extraction gives

```math
\mathcal C_3(HL^2)
=H\left(a^2X+abZ+b^2Y\right),
\qquad\text{(10)}
```

and Frobenius gives

```math
\mathcal C_3(HL^3)=H(aX+bY).
\qquad\text{(11)}
```

For completeness, the cross term in (10) follows from

```math
\mathcal C_3\bigl(HV(x)V(y)\bigr)=-HZ
```

together with the coefficient $2ab=-ab$ in characteristic $3$; their
product is $+abHZ$. Substitution of (10)--(11) into (8) proves (5).
$\square$

## 3. The maximal parameter-residue subclass

### Corollary 2

For all positive $a,b,c,n$ satisfying

```math
3\mid nab(a+b),
```

one has

```math
\boxed{
U_{a,b;c}(3n)\equiv U_{a,b;c}(n)\pmod {27}.
}
\qquad\text{(12)}
```

In particular, Bala's sum $u(N)=U_{1,2;1}(N)$ satisfies
$u(3n)\equiv u(n)\pmod {27}$ for every $n$.

### Proof

If $3\mid n$, the factor $n^2$ in (5) proves the result. Assume that $n$
is a unit modulo $3$.

First suppose $3\mid a+b$. If $a\equiv b\equiv0$, the right side is
zero. Otherwise write $b=-a$ in $\mathbb F_3$ and set

```math
P=\frac{x}{1-x},
\qquad
Q=\frac{y}{1-y},
\qquad
W=P+Q.
```

With $E_x=x\partial_x$,

```math
X+Y-Z=W+W^2,
\qquad
X-Y=E_xW.
\qquad\text{(13)}
```

Put $R=HG^n$. Since

```math
E_x\log R=naW,
```

formal integration by parts gives

```math
\operatorname{CT}R E_xW=-na\operatorname{CT}RW^2.
```

The constant term in (5) is consequently

```math
a^2\operatorname{CT}R\left(W+W^2\right)
+an\operatorname{CT}R E_xW
=a^2\operatorname{CT}RW,
```

because $n^2=1$ in $\mathbb F_3$. Finally
$\operatorname{CT}E_xR=na\operatorname{CT}RW=0$, and $na$ is a unit.
This handles the factor $a+b$.

Now suppose $a=0$ in $\mathbb F_3$. The bracket in (5) reduces to

```math
b(b+n)Y.
```

There is nothing to prove if $b=0$ or $b=-n$. In the remaining case
$b=n$, so $bn=1$ in $\mathbb F_3$. In $RY$, with $R=HG^n$, the two
relevant factors can be grouped as

```math
(1-x)^{-an}
\quad\text{and}\quad
y(1-y)^{-(bn+2)}.
```

The first is a power series in $x^3$, while the second has only powers
$y^{1+3j}$. Since $y=t/x$, no monomial can have $x$-exponent zero.
Hence $\operatorname{CT}RY=0$. The case $b=0$ is symmetric: if its scalar
does not already vanish, $a=n$, and the powers of $x$ are $1$ modulo $3$
while the powers of $y$ are $0$ modulo $3$. This proves (12). $\square$

The condition is maximal among conditions depending only on the residue
class of $(a,b,n)$ modulo $3$ and intended to hold uniformly in $c$. It
includes $23$ of the $27$ triples in $\mathbb F_3^3$. The four omitted
triples have $a=b\ne0$ and $n\ne0$; every one has a sharp counterexample,
as shown next.

## 4. The universal theorem cannot include $p=3$

For $(a,b,n)=(1,1,1)$, take $c=1$. Then

```math
U_{1,1;1}(1)=2,
\qquad
U_{1,1;1}(3)=146,
```

so

```math
U_{1,1;1}(3)-U_{1,1;1}(1)=144=3^2\cdot16.
\qquad\text{(14)}
```

Thus the exponent $2$ is exact. The restriction $p\geq5$ in the universal
cubic prefix theorem is sharp.

The other three omitted residue triples fail just as sharply:

```math
U_{2,2;1}(1)=5,
\qquad
U_{2,2;1}(3)=3614,
\qquad
3614-5=3609=3^2\cdot401.
\qquad\text{(15)}
```

```math
U_{1,1;1}(6)-U_{1,1;1}(2)
=296438-14
=296424
=3^2\cdot32936,
\qquad\text{(16)}
```

and

```math
U_{2,2;2}(6)-U_{2,2;2}(2)
=2485268015414-1742
=2485268013672
=3^2\cdot276140890408.
\qquad\text{(17)}
```

These examples represent $(2,2,1)$, $(1,1,2)$, and $(2,2,2)$,
respectively. Consequently no further parameter residue class can be
added to Corollary 2 while retaining a theorem uniform in $c$.

## 5. The all-level ternary kernel

Write

```math
D_r(a,b,c;n)=
U_{a,b;c}(n3^r)-U_{a,b;c}(n3^{r-1}).
```

We prove the coupled renormalization

```math
\boxed{
D_r(a,b,c;n)\equiv27D_{r-1}(a,b,c;n)
\pmod {3^{3r+1}}
\qquad(r\geq2).
}
\qquad\text{(18)}
```

The extra power in (18) is sharp: for $(a,b,c,n,r)=(1,1,1,1,2)$ the
difference has valuation exactly $7$.

Continue in the unimodular coordinates $(x,y)$, so

```math
H=\frac1{1-xy},
\qquad
G=\frac{x^{-c}y^{-c}}{(1-x)^a(1-y)^b}.
```

Put $D_x=x\partial_x$ and $D_y=y\partial_y$.  Choose the canonical
$3$-integral primitives $P,Q$ defined coefficientwise by

```math
\mathcal C_3(HL^2)=D_xP+D_yQ:
```

at $(m,n)$ assign the coefficient to $D_xP$ when
$m\ne0$ and $v_3(m)\leq v_3(n)$, and otherwise assign it to $D_yQ$.
The unit-block square estimate gives enough divisibility to perform these
divisions.  Define

```math
\mathscr B_3=
\frac12\mathcal C_3(HL^3)
-\frac12\left(PD_x\log G+QD_y\log G\right).
\tag{19}
```

### Lemma 3 (ternary kernel lemma)

The canonical primitives and kernel satisfy

```math
\mathcal C_3(P)\equiv P,
\qquad
\mathcal C_3(Q)\equiv Q,
\qquad
\mathcal C_3(\mathscr B_3)\equiv\mathscr B_3
\pmod9,
\tag{20}
```

and

```math
\mathcal C_3(\mathscr B_3L)=0\pmod3.
\tag{21}
```

### Proof

The proof is a finite residue calculation, but we give the reduction.  The
square-unit sum modulo $3^e$ has valuation $e-1$.  Repeating the unit-block
argument for the lifted difference gives

```math
v_3\!\left(
[x^{9m}y^{9n}]HL^2
-3[x^{3m}y^{3n}]HL^2
\right)
\geq3+\min\{v_3(m),v_3(n)\}.
\tag{22}
```

The only new Taylor boundary compared with the odd-prime square lift is
degree two.  Its binomial coefficient is $3$, supplying exactly the
missing factor.  Bound (22), followed by division by the selected one of
$3m,3n$, proves the first two congruences in (20).

For the remaining calculation, periodicity of unit inverses gives, in
$(\mathbb Z/9\mathbb Z)[[z]]$,

```math
V(z)=\frac{W_9(z)}{1-z^9},
\quad
W_9(z)=z+5z^2+7z^4+2z^5+4z^7+8z^8.
\tag{23}
```

Direct extraction of the exponents divisible by $3$ gives

```math
\mathcal C_3(V(x)^2)=X,
\qquad
\mathcal C_3(HV(x)V(y))=-HZ
\pmod9.
\tag{24}
```

For example,

```math
\mathcal C_3(W_9^2)
=z+2z^2+3z^3+2z^4+z^5
=z(1+z+z^2)^2,
```

which proves the first identity after the denominator is restored; the
second is the identical two-variable extraction.  Consequently, if

```math
R_{m,n}=[x^my^n]\mathcal C_3(HL^2),
```

then

```math
\boxed{
R_{m,n}\equiv
a^2(m-n)_++b^2(n-m)_+-2ab\min\{m,n\}
\pmod9.
}
\tag{25}
```

The cube calculation is just as short.  The pure terms use

```math
\mathcal C_3(W_9^3)
=z+2z^2+3z^3+z^4+8z^5+6z^6+7z^7+8z^8,
```

and

```math
\mathcal C_9(W_9^3)=3z+6z^2.
```

After restoring denominators, these say that the diagonal Moebius
difference of the pure cube defect is $2X$ modulo $9$.  The two mixed
terms already carry their binomial coefficient $3$, so extraction modulo
$3$ suffices; each contributes $3Z$ modulo $9$.  Thus, with

```math
\Delta_{m,n}=[x^{9m}y^{9n}]HL^3-[x^{3m}y^{3n}]HL^3,
```

one obtains

```math
\Delta_{m,n}\equiv
\begin{cases}
2a^3(m-n)+3ab(a+b)n,&m\geq n,\\
2b^3(n-m)+3ab(a+b)m,&n\geq m
\end{cases}
\pmod9.
\tag{26}
```

The unit shifts of the canonical primitives require no further primitive
formula.  In a shift contributing to $P$, the first index is a $3$-adic
unit, so its coefficient is $R_{i,3n}/i$; the analogous statement holds
for $Q$.  The two complete-block evaluations are

```math
\#\{1\leq i<3M:3\nmid i\}=2M,
\qquad
\sum_{\substack{1\leq i<3M\\3\nmid i}}\frac1i
\equiv-3M^2\pmod9.
\tag{27}
```

Substituting (25) into the unit shifts and using (27) gives, for $m\geq n$,

```math
\begin{aligned}
U^P_{m,n}&\equiv
-2nb(b+2a)+2(m-n)a^2,\\
U^Q_{m,n}&\equiv-2na(a+2b)
\end{aligned}
\pmod9,
\tag{28}
```

with the symmetric formulas when $n\geq m$.  Therefore

```math
aU^P_{m,n}+bU^Q_{m,n}=\Delta_{m,n}\pmod9.
\tag{29}
```

Using the first two congruences of (20), the divisible shifts in
$\mathcal C_3(PD_x\log G)$ and
$\mathcal C_3(QD_y\log G)$ cancel their lower-level copies; the remaining
unit shifts are exactly (29).  This proves the third congruence in (20).

Finally, expand $\mathcal C_3(\mathscr B_3L)$ using (19), (24), and (25).
The terms proportional to $c a^3,c a^2b,c ab^2,c b^3$ and to
$a^4,a^3b,a^2b^2,ab^3,b^4$ cancel separately.  Coefficientwise, each
pair reduces to the two block sums in (27), together with

```math
\sum_{\substack{1\leq i<3M\\3\nmid i}}i^{-2}\equiv-M\pmod3.
```

This proves (21). $\square$

### Theorem 4 (all-level ternary renormalization)

For every positive $a,b,c,n$ and every $r\geq2$, congruence (18) holds.

### Proof

The same exponential expansion as in (7), now at level $r$, and formal
integration by parts with $P,Q$ show

```math
\boxed{
\frac{D_r(a,b,c;n)}{3^{3r-1}}
\equiv
n^3\operatorname{CT}\mathscr B_3G^{n3^{r-1}}
\pmod9.
}
\tag{30}
```

All terms of exponential degree at least five lie two powers deeper.  At
$r=1$ the degree-four scalar is only one power deeper, but its remaining
Cartier image vanishes modulo $3$: Frobenius gives
$L^3=L(x^3,y^3)$ and $\mathcal C_3(HL)=0$, hence
$\mathcal C_3(HL^4)=0$.  Thus (30) also holds at the first level.

For $M\geq0$, equation $G^3/G(x^3,y^3)=\exp(3L)$ gives

```math
G^{3M}\equiv G(x^3,y^3)^M(1+3ML)\pmod9.
```

Apply Cartier inside the constant term and use (20)--(21):

```math
\operatorname{CT}\mathscr B_3G^{3M}
\equiv
\operatorname{CT}\mathcal C_3(\mathscr B_3)G^M
+3M\operatorname{CT}\mathcal C_3(\mathscr B_3L)G^M
\equiv
\operatorname{CT}\mathscr B_3G^M
\pmod9.
```

Substituting this in (30) proves (18). $\square$

### Corollary 5 (complete ternary tower for the maximal subclass)

If $3\mid nab(a+b)$, then for every $r\geq1$,

```math
U_{a,b;c}(n3^r)\equiv U_{a,b;c}(n3^{r-1})\pmod {3^{3r}}.
\tag{31}
```

In particular, (31) proves Bala's complete $p=3$ tower.  Corollary 2 is
the base level, and Theorem 4 propagates its extra factor of $3$.

## 6. Verification

Run

```text
python verification/related/verify_prime_three_negative_binomial_boundary.py
```

The checker verifies the exact residue formula, the maximal
$3\mid nab(a+b)$ corollary, sharp counterexamples in all four excluded
parameter residue classes, the square lift, the mod-$9$ Green kernel, the
ternary defect kernel, the sharp second-level witness, and extended exact
and modular grids for Theorem 4.
