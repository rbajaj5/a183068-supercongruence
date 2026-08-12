# The A263843 reversion family away from one ternary boundary

**Status:** complete proof for every prime $p\geq5$ and for the ternary
subfamily $3\mid(c+s)$; the remaining $p=3$, $3\nmid(c+s)$ case is open.

**Source boundary:** [OEIS A263843](https://oeis.org/A263843) conjectures the
full family below for every prime $p\geq3$.  The note proves all of its odd
prime content except one explicitly identified ternary unit-slope boundary.
In particular, it proves the named sequence for $p\geq5$ but does not claim
the named $p=3$ case.

## 1. Reversion and the proposed family

Let $Y(x)$ be the unique formal series with zero constant term satisfying

```math
Y=x\frac{(1+Y)^3}{1-Y},
\tag{1}
```

and set

```math
H(x)=\frac{Y(x)}x=1+4x+23x^2+\cdots.
\tag{2}
```

For a positive integer $c$, an integer $s$, and $N\geq1$, define

```math
B_{c,s}(N)=[x^{cN}]H(x)^{sN}.
\tag{3}
```

The OEIS page asks for

```math
B_{c,s}(np^r)\equiv B_{c,s}(np^{r-1})\pmod {p^{3r}}
\tag{4}
```

for every prime $p\geq3$.

## 2. Exact Lagrange reduction

Put

```math
\phi(t)=\frac{(1+t)^3}{1-t},
\qquad d=c+s.
\tag{5}
```

Equation (1) is $Y=x\phi(Y)$ and (2) is $H=\phi(Y)$.  If $s\ne0$ and
$d\ne0$, Lagrange--Bürmann inversion gives

```math
\begin{aligned}
B_{c,s}(N)
&=\frac1{cN}[t^{cN-1}]
\frac{d}{dt}\bigl(\phi(t)^{sN}\bigr)\phi(t)^{cN}\\
&=\frac{s}{c+s}[t^{cN}]\phi(t)^{(c+s)N}.
\end{aligned}
\tag{6}
```

Thus

```math
B_{c,s}(N)=\frac{s}{d}
[t^{cN}](1+t)^{3dN}(1-t)^{-dN}.
\tag{7}
```

This is exactly the repository's coefficient-framing family, with the
parameters $(\alpha,\beta;c)=(3d,-d;c)$.

There are two elementary singular cases.  If $s=0$, then (3) is zero.  If
$d=0$, direct use of the first line of (6) gives

```math
B_{c,-c}(N)=-1-3(-1)^{cN-1}.
\tag{8}
```

For odd $p$, the right side is unchanged under $N\mapsto pN$, so its tower
is an equality.

## 3. Denominator primes do not cause a loss

Formula (7) contains a factor $1/d$, so simply quoting the coefficient-
framing theorem would lose powers when $p\mid d$.  The proof itself supplies
exactly the missing compensation.

Let

```math
A_d(N)=[t^{cN}](1+t)^{3dN}(1-t)^{-dN}.
\tag{9}
```

For $N=np^r$, the reduced Frobenius logarithm in the framing proof is

```math
L_p(t)=d\bigl(3V_p(t)+U_p(t)\bigr),
\tag{10}
```

where $U_p,V_p$ are the reduced logarithms used in
[the coefficient-framing theorem](CoefficientFramingCubicTower.md).  Write
$e=v_p(d)$.  The linear exponential term still vanishes exactly.  For
$p\geq5$, the reciprocal-square Cartier estimate and integration by parts
give the quadratic term valuation

```math
3r+2e,
\tag{11}
```

while every term of degree $h\geq3$ has valuation at least

```math
hr-v_p(h!)+he\geq3r+e.
\tag{12}
```

Consequently,

```math
v_p\bigl(A_d(np^r)-A_d(np^{r-1})\bigr)
\geq3r+v_p(d).
\tag{13}
```

Multiplying by $s/d$ in (7) loses at most $v_p(d)$ and proves (4) for every
$p\geq5$, including primes dividing $c+s$.

## 4. The exact ternary boundary

At $p=3$, the general reciprocal-square estimate is one power weaker.  The
same calculation gives the quadratic budget

```math
3r-1+2v_3(d)
\tag{14}
```

before division by $d$.  Therefore (4) is proved whenever $3\mid d=c+s$.
Together with (8), this includes $d=0$ as an exact equality.

When $3\nmid(c+s)$, this argument proves only modulus $3^{3r-1}$.  Exact
tests continue to support the conjectured extra power, including the named
case $(c,s)=(1,1)$, but they do not replace the missing cancellation.  The
entire unresolved content of the OEIS family is therefore reduced to

```math
p=3,\qquad 3\nmid(c+s).
\tag{15}
```

## 5. Verification

Run

```text
python verification/related/verify_a263843_reversion_reduction.py
```

The exact checker verifies the published named values, the Lagrange formula
and its two singular cases, integrality across positive and negative slopes,
the full $p\geq5$ tower including denominator primes, the proved ternary
subfamily, and the surviving ternary unit-slope test grid.
