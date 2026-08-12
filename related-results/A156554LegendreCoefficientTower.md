# A cubic tower for the Legendre coefficient family

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open.

**Source boundary:** [OEIS A156554](https://oeis.org/A156554) states the
parameterized conjecture proved below.  The proof uses the standard binomial
formula for the Legendre polynomials and a two-variable Cartier argument.  No
claim of literature priority is made.

## 1. Statement

Let $P_m$ denote the $m$-th Legendre polynomial.  For integers $A,B$, positive
integers $c,s$, and $N\geq1$, define

```math
C_{A,B;c,s}(N)=
[x^{cN}](1+x)^{AN}(1-x)^{BN}
P_{sN}\!\left(\frac{1+x}{1-x}\right).
\tag{1}
```

Generalized binomial expansion at $x=0$ makes (1) an integer for every choice
of these parameters, including negative $A$ or $B$.

### Theorem

For every prime $p\geq5$ and all positive integers $n,r$,

```math
\boxed{
C_{A,B;c,s}(np^r)
\equiv C_{A,B;c,s}(np^{r-1})\pmod {p^{3r}}.
}
\tag{2}
```

The named sequence A156554 is the specialization

```math
(A,B;c,s)=(0,0;1,2).
\tag{3}
```

Thus (2) proves both the named conjecture and the full integral-parameter
family stated on that page.

## 2. A two-variable constant term

The standard Legendre identity

```math
P_m\!\left(\frac{1+x}{1-x}\right)
=(1-x)^{-m}\sum_{k=0}^{m}\binom{m}{k}^{\!2}x^k
\tag{4}
```

has the constant-term form

```math
P_m\!\left(\frac{1+x}{1-x}\right)
=(1-x)^{-m}\operatorname{CT}_y
(1+y)^m(1+x/y)^m.
\tag{5}
```

Consequently,

```math
C_{A,B;c,s}(N)=\operatorname{CT}_{x,y}G(x,y)^N,
\tag{6}
```

where

```math
G(x,y)=x^{-c}(1+x)^A(1-x)^{B-s}
(1+y)^s(1+x/y)^s.
\tag{7}
```

These expressions may be read in the Laurent-series cone defined by the
weight $(2,1)$: the three nonconstant directions

```math
(1,0),\qquad(0,1),\qquad(1,-1)
\tag{8}
```

all have positive weight.  Hence every coefficient used below receives only
finitely many contributions.  This also handles negative exponents $A$ and
$B-s$ without an analytic convergence assumption.

## 3. The reduced Frobenius logarithm

For an odd prime $p$, put

```math
U_p(z)=\sum_{\substack{j\geq1\\p\nmid j}}\frac{z^j}{j},
\qquad
V_p(z)=\sum_{\substack{j\geq1\\p\nmid j}}
\frac{(-1)^{j+1}z^j}{j}.
\tag{9}
```

Define

```math
\begin{aligned}
L_p(x,y)={}&A V_p(x)-(B-s)U_p(x)\\
&+sV_p(y)+sV_p(x/y).
\end{aligned}
\tag{10}
```

Separating the logarithmic terms whose indices are divisible by $p$ gives
the exact formal identity

```math
\frac{G(x,y)^p}{G(x^p,y^p)}=\exp\bigl(pL_p(x,y)\bigr).
\tag{11}
```

The Laurent monomial $x^{-c}$ cancels from the quotient.  Every monomial of
$L_p$ lies on one of the primitive rays (8), at a distance $j$ not divisible
by $p$.  If $\mathcal C_p$ retains precisely the monomials whose two
exponents are divisible by $p$, then

```math
\mathcal C_p(L_p)=0.
\tag{12}
```

## 4. The quadratic Cartier gain

We need one more power than (12) supplies.  The required one-variable fact is
the reciprocal-square estimate already used by the
[coefficient-framing theorem](CoefficientFramingCubicTower.md): if $W$ is
any integral linear combination of $U_p$ and $V_p$, then, for $p\geq5$,

```math
\mathcal C_p(W(z)^2)=p zK'(z)
\tag{13}
```

for a series $K\in\mathbb Z_{(p)}[[z]]$.

For clarity, (13) follows directly from

```math
[z^T]U_p(z)^2=\frac{2H_T}{T},
\qquad
[z^T]V_p(z)^2=(-1)^T\frac{2H_T}{T},
\tag{14}
```

and

```math
[z^T]U_p(z)V_p(z)
=\frac{1+(-1)^T}{T}H_T^{\pm},
\tag{15}
```

where the reduced harmonic sums satisfy
$v_p(H_T),v_p(H_T^{\pm})\geq2v_p(T)$ in the cases contributing to
(14)--(15).  Thus the coefficient of $z^{pm}$ in $W^2$ is divisible by
$pm$, which is equivalent to (13).

Now expand $L_p^2$ by pairs of rays.  A mixed pair has zero Cartier image.
Indeed, every pair among the vectors in (8) is a unimodular basis of
$\mathbb Z^2$.  If

```math
ju+kv\in p\mathbb Z^2
```

for two distinct rays $u,v$, then $p\mid j$ and $p\mid k$, contrary to the
support condition in (9).  Applying (13) separately on each same-ray square
therefore gives

```math
\mathcal C_p(L_p^2)
=p\sum_{i=1}^{3}E_iK_i,
\tag{16}
```

where the $K_i$ have $p$-integral coefficients and $E_i$ is the Euler
derivation along the corresponding ray.  For example,
$E_1=x\partial_x$, $E_2=y\partial_y$, and one may take
$E_3=x\partial_x$ on series in $x/y$.

## 5. Proof of the theorem

Set $N=np^r$ and $M=N/p$.  Equations (6) and (11) give

```math
C_{A,B;c,s}(N)-C_{A,B;c,s}(M)
=\operatorname{CT}G(x^p,y^p)^M
\left(\exp(NL_p)-1\right).
\tag{17}
```

The linear term vanishes exactly by (12).  For the quadratic term, Cartier
extraction, (16), and formal integration by parts give

```math
\begin{aligned}
\operatorname{CT}G(x^p,y^p)^M L_p^2
&=p\sum_i\operatorname{CT}G(x,y)^M E_iK_i\\
&=-pM\sum_i\operatorname{CT}
K_iG(x,y)^{M-1}E_iG(x,y).
\end{aligned}
\tag{18}
```

All coefficients on the last line are $p$-integral.  Since $p$ is odd, the
quadratic term in (17) has valuation at least

```math
v_p\!\left(\frac{N^2}{2}\,pM\right)=3r.
\tag{19}
```

For every $h\geq3$,

```math
v_p\!\left(\frac{N^h}{h!}\right)
=hr-v_p(h!)\geq3r
\qquad(p\geq5).
\tag{20}
```

For $r=1$, this follows from $h-v_p(h!)\geq3$; increasing $r$ only improves
the bound.  Therefore every remaining exponential term in (17) is divisible
by $p^{3r}$.  Equations (17)--(20) prove (2). $\square$

## 6. Verification

Run

```text
python verification/related/verify_a156554_legendre_tower.py
```

The exact checker verifies the published A156554 values, the Legendre
constant-term identity, the mixed-ray Cartier exclusion, the reciprocal-
square valuation used in (13), the factorial budget, and a parameter grid
including negative $A,B$ and adjacent levels through $r=3$.  These checks are
regression evidence; the proof above establishes the parameterized theorem.

## 7. Campaign effect

This result moves A156554 from `open-target` to `proved-here` in the
110-record Bala ledger.  It also demonstrates that adding a Legendre factor
to the one-variable coefficient-framing family does not consume the third
power: the new Cartier variable contributes three primitive, pairwise
unimodular rays, so mixed quadratic terms vanish and the old same-ray
reciprocal-square estimate remains sufficient.
