# The quadratic tower for cubes of trinomial coefficients

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open.

**Source boundary:** [OEIS A132303](https://oeis.org/A132303) conjectures the
theorem below for every prime $p\geq5$.  The proof here uses only the displayed
trinomial definition and a cyclotomic constant-term identity.  No claim of
literature priority is made.

## 1. Statement

Write

```math
(1+z+z^2)^N=\sum_{k=0}^{2N}t(N,k)z^k
```

and define

```math
A(N)=\sum_{k=0}^{2N}t(N,k)^3.
\tag{1}
```

### Theorem

For every prime $p\geq5$ and all positive integers $n,r$,

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{2r}}.
}
\tag{2}
```

This proves the supercongruence conjectured on A132303.  The exponent is
frequently exact: the checker records witnesses with valuation exactly $2r$.

## 2. Constant-term realization

Put

```math
F(z)=1+z+z^2=\frac{1-z^3}{1-z}.
```

Expanding three copies of $F(z)^N$ gives

```math
\begin{aligned}
A(N)
&=\operatorname{CT}_{x,y}
  F(x)^N F(y)^N F((xy)^{-1})^N\\
&=\operatorname{CT}_{x,y}G(x,y)^N,
\end{aligned}
\tag{3}
```

where

```math
G(x,y)=x^{-2}y^{-2}\Psi(x,y),
\qquad
\Psi(x,y)=F(x)F(y)F(xy).
\tag{4}
```

Indeed, the constant term in the first line forces the three coefficient
indices to be equal.  The second line uses
$F((xy)^{-1})=x^{-2}y^{-2}F(xy)$.

## 3. The reduced Frobenius logarithm

For $p\geq5$, define the $p$-integral series

```math
R_p(z)=
\sum_{\substack{j\geq1\\p\nmid j}}
\frac{z^j-z^{3j}}{j}.
\tag{5}
```

Since

```math
\log F(z)=\sum_{j\geq1}\frac{z^j-z^{3j}}j,
```

separating the indices divisible by $p$ gives the exact identity

```math
\frac{F(z)^p}{F(z^p)}=\exp\bigl(pR_p(z)\bigr).
\tag{6}
```

Set

```math
L_p(x,y)=R_p(x)+R_p(y)+R_p(xy).
\tag{7}
```

The Laurent monomial in (4) cancels under Frobenius, so (6) yields

```math
\frac{G(x,y)^p}{G(x^p,y^p)}
=\exp\bigl(pL_p(x,y)\bigr).
\tag{8}
```

Every monomial of $L_p$ lies on one of the three rays

```math
(e,0),\qquad(0,e),\qquad(e,e),
```

where $p\nmid e$.  The last assertion uses $p\nmid3$.  Consequently

```math
\mathcal C_p(L_p)=0,
\tag{9}
```

where $\mathcal C_p$ retains precisely the monomials whose two exponents are
both divisible by $p$.

This support statement is the whole source of the quadratic gain.  It also
explains the prime restriction: at $p=3$, the terms $z^{3j}$ in (5) can land
on the Frobenius sublattice.

## 4. Proof of the theorem

Let $N=np^r$ and $M=N/p$.  From (3) and (8),

```math
A(N)-A(M)
=\operatorname{CT}
G(x^p,y^p)^M\left(\exp(NL_p)-1\right).
\tag{10}
```

The equality also uses
$\operatorname{CT}G(x^p,y^p)^M=\operatorname{CT}G(x,y)^M$.

All exponent vectors in $G(x^p,y^p)^M$ belong to $p\mathbb Z^2$.  Equation
(9) therefore makes the linear term in (10) vanish exactly:

```math
\operatorname{CT}G(x^p,y^p)^M L_p=0.
\tag{11}
```

For every $h\geq2$,

```math
v_p\left(\frac{N^h}{h!}\right)
\geq hr-v_p(h!)
\geq2r.
\tag{12}
```

For the last inequality, Legendre's bound gives
$v_p(h!)\leq h-2$ when $p\geq5$ and $h\geq2$, and hence

```math
hr-v_p(h!)\geq hr-h+2
=2r+(h-2)(r-1).
```

The coefficients of $L_p$ are $p$-integral.  Thus every term of degree at
least two in the exponential in (10) is divisible by $p^{2r}$.  Only
finitely many degrees can contribute to the constant term: $G(x^p,y^p)^M$
has finite support, whereas every monomial of $L_p$ has positive total
degree.  Equations (10)--(12) prove (2). $\square$

## 5. Verification

Run

```text
python verification/related/verify_a132303_trinomial_cube.py
```

The exact checker verifies the twenty published initial values, the
constant-term identity, the reduced-log support exclusion, the factorial
valuation budget, and adjacent towers through level three on a prime and
index grid.  It also records sharp examples.  These computations are
regression evidence; the argument above establishes the general theorem.

## 6. Campaign effect

This result moves A132303 from `open-target` to `proved-here` in the
110-record Bala ledger.  It does not settle A124435, the other quadratic
target formerly grouped beside it: that sequence has a different
constant-term logarithm and remains open.
