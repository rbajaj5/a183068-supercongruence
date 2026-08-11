# The exact prime-three boundary for negative-binomial prefixes

**Status:** complete elementary prime-level theorem and sharp counterexample;
the all-level defect renormalization is conjectural.

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

## 5. The next all-level lemma

Write

```math
D_r(a,b,c;n)=
U_{a,b;c}(n3^r)-U_{a,b;c}(n3^{r-1}).
```

Exact arithmetic supports the coupled renormalization

```math
\boxed{
D_r(a,b,c;n)\equiv27D_{r-1}(a,b,c;n)
\pmod {3^{3r+1}}
\qquad(r\geq2).
}
\qquad\text{(18)}
```

The extra power in (18) is sharp: for $(a,b,c,n,r)=(1,1,1,1,2)$ the
difference has valuation exactly $7$. If (18) is proved, Corollary 2
immediately propagates to every level and supplies the complete $p=3$
tower for Bala's $u$. Equation (18) remains a conjecture, not a theorem of
this note.

## 6. Verification

Run

```text
python verification/related/verify_prime_three_negative_binomial_boundary.py
```

The checker verifies the exact residue formula, the maximal
$3\mid nab(a+b)$ corollary, sharp counterexamples in all four excluded
parameter residue classes, the sharp second-level renormalization witness,
and extended exact and modular grids for (18). These computations certify
the formulas and boundaries but do not prove the conjectural all-level
renormalization.
