# Cubic towers for mixed negative-binomial prefixes

**Status:** complete elementary proof candidate for every prime $p\geq5$;
exact checks pass; independent review and literature priority remain open.

**Source boundary:** Peter Bala proposed the special case
$\sum_{k=0}^N\binom{-N}{k}\binom{-2N}{k}$ and the wider
negative-parameter direction in correspondence on August 11, 2026. The
two-variable Cartier proof below was developed in this repository. No
priority claim is made.

## 1. The theorem

Fix positive integers $a,b,c$ and put

```math
U_{a,b;c}(N)=
\sum_{k=0}^{cN}
\binom{-aN}{k}\binom{-bN}{k}.
\qquad\text{(1)}
```

### Theorem 1

For every prime $p\geq5$ and all $n,r\geq1$,

```math
\boxed{
U_{a,b;c}(np^r)
\equiv
U_{a,b;c}(np^{r-1})
\pmod {p^{3r}}.
}
\qquad\text{(2)}
```

Two consequences answer open items from the August coefficient packet.

1. Bala's mixed sum is $u(N)=U_{1,2;1}(N)$, so its ordinary cubic tower
   holds for every $p\geq5$.
2. For positive $A,B$,

   ```math
   \sum_{k=0}^{AN}\binom{BN+k-1}{k}^2
   =U_{B,B;A}(N).
   ```

   Hence the full positive-parameter family surrounding A333592 has a
   cubic tower. The named A333592 specialization is $A=B=1$.

The theorem is stronger than the coefficientwise two-factor bound. Its
third power of $p$ appears only after the prefix is summed.

## 2. Constant-term realization

Work in the cone-completed Laurent-series ring over $\mathbb Z_p$ in
variables $x,t$: powers of $t$ are bounded below, and at each fixed
$t$-degree the constant-term operations below are finite. Define

```math
H(t)=\frac1{1-t},
\qquad
G(x,t)=
\frac{t^{-c}}{(1-x)^a(1-t/x)^b}.
\qquad\text{(3)}
```

Expanding the three geometric factors gives

```math
\operatorname{CT}_{x,t} H(t)G(x,t)^N
=
\sum_{k=0}^{cN}
\binom{aN+k-1}{k}\binom{bN+k-1}{k}.
```

The signs in the two generalized binomial coefficients cancel, so

```math
U_{a,b;c}(N)=\operatorname{CT}_{x,t}H(t)G(x,t)^N.
\qquad\text{(4)}
```

The factor $H$ encodes the upper cutoff: after the $x$-constant term forces
the two expansion indices to equal $k$, the $t$-constant term contributes
exactly when $0\leq k\leq cN$.

Let the two-variable Cartier operator be

```math
\mathcal C_p
\left(\sum q_{i,j}x^it^j\right)
=\sum q_{pi,pj}x^it^j.
```

The key observation is

```math
\mathcal C_p(H)=H.
\qquad\text{(5)}
```

Thus the fixed prefix factor survives the descent from $N$ to $N/p$
without an error term.

## 3. Reduced logarithm

Put

```math
V_p(z)=
\sum_{\substack{j\geq1\\p\nmid j}}\frac{z^j}{j},
\qquad
L_p(x,t)=aV_p(x)+bV_p(t/x).
\qquad\text{(6)}
```

The monomial $t^{-c}$ cancels, and cancellation of the exponents divisible
by $p$ gives the exact identity

```math
\frac{G(x,t)^p}{G(x^p,t^p)}
=\exp\bigl(pL_p(x,t)\bigr).
\qquad\text{(7)}
```

Let $N=np^r$ and $M=N/p$. From (4), (5), and (7),

```math
U_{a,b;c}(N)-U_{a,b;c}(M)
=
\operatorname{CT}
H(t)G(x^p,t^p)^M
\left(\exp(NL_p)-1\right).
\qquad\text{(8)}
```

The linear term has zero constant coefficient. Every exponent of
$G(x^p,t^p)^M$ is divisible by $p$, while each monomial of $L_p$ has
$x$-exponent not divisible by $p$. The factor $H(t)$ has no $x$-exponent
and cannot change this.

## 4. The prefix-Cartier quadratic lemma

Write $E_x=x\partial_x$ and $E_t=t\partial_t$.

### Lemma 2

For $p\geq5$ there are $p$-integral formal Laurent series $K_1,K_2$ such
that

```math
\boxed{
\mathcal C_p\!\left(HL_p^2\right)
=p(E_xK_1+E_tK_2).
}
\qquad\text{(9)}
```

### Proof

First note the elementary unit-block identity

```math
\sum_{u\in(\mathbb Z/p^e\mathbb Z)^\times}u^{-2}
\equiv0\pmod {p^e}
\qquad(e\geq1).
\qquad\text{(10)}
```

Inversion permutes the units, so the sum equals the sum of their squares.
Multiplication by $2$ also permutes the units. Therefore the square sum is
four times itself; since $3$ is a unit for $p\geq5$, it vanishes.

Expand

```math
HL_p^2
=a^2H V_p(x)^2
+2abH V_p(x)V_p(t/x)
+b^2H V_p(t/x)^2.
\qquad\text{(11)}
```

For the first square, the coefficient selected by Cartier at $x^m$ is

```math
d_m=[z^{pm}]V_p(z)^2
=
\sum_{\substack{1\leq j<pm\\p\nmid j}}
\frac1{j(pm-j)}.
\qquad\text{(12)}
```

Put $e=1+v_p(m)$. Modulo $p^e$, each summand is $-j^{-2}$. The interval in
(12) is a union of complete blocks modulo $p^e$, so (10) gives

```math
v_p(d_m)\geq1+v_p(m).
\qquad\text{(13)}
```

The second square has the same coefficient after substituting $z=t/x$.

It remains to handle the cross term. For output exponent $(m,n)$ with
$m\geq0$ and $n\geq1$, its coefficient before the factor $2ab$ is

```math
S_{m,n}=
\sum_{\substack{1\leq j\leq pn\\p\nmid j}}
\frac1{j(j+pm)}.
\qquad\text{(14)}
```

Let $s=\min\{v_p(m),v_p(n)\}$, with $v_p(0)=+\infty$. Both $pm$ and $pn$
are divisible by $p^{s+1}$. Modulo that power, the summand in (14) is
$j^{-2}$, and the range again splits into complete unit blocks. Hence

```math
v_p(S_{m,n})
\geq1+\min\{v_p(m),v_p(n)\}.
\qquad\text{(15)}
```

If $m<0$, put $h=-m$. A nonempty coefficient requires $n>h$, and shifting
$j$ by $ph$ changes (14) to $S_{h,n-h}$. The ultrametric identity

```math
\min\{v_p(h),v_p(n-h)\}
=\min\{v_p(h),v_p(n)\}
```

gives the same bound.

Consequently, if

```math
\mathcal C_p(HL_p^2)=
\sum c_{m,n}x^mt^n,
```

then

```math
v_p(c_{m,n})
\geq1+\min\{v_p(m),v_p(n)\}.
\qquad\text{(16)}
```

There is no $(0,0)$ term. For each remaining monomial, divide by $pm$ when
$v_p(m)\leq v_p(n)$ and $m\ne0$, and otherwise divide by $pn$. Bound (16)
makes the resulting coefficient $p$-integral. Assigning these quotients
monomial by monomial constructs $K_1,K_2$ and proves (9). $\square$

## 5. Completion of the proof

The quadratic term in (8) is

```math
\frac{N^2}{2}
\operatorname{CT}
\mathcal C_p(HL_p^2)G(x,t)^M.
```

By Lemma 2 and formal integration by parts,

```math
\operatorname{CT}(E_xK_1)G^M
=-M\operatorname{CT}K_1G^M E_x\log G,
```

and similarly for $E_t$. The logarithmic derivatives

```math
E_x\log G
=\frac{ax}{1-x}-\frac{b(t/x)}{1-t/x},
```

```math
E_t\log G
=-c+\frac{b(t/x)}{1-t/x}
```

are integral. The quadratic term therefore has valuation at least

```math
v_p(N^2pM)\geq3r.
```

For every exponential term of degree $j\geq3$,

```math
v_p\!\left(\frac{N^j}{j!}\right)\geq3r
\qquad(p\geq5).
```

Indeed this is immediate for $j=3,4$, while for $j\geq5$ Legendre's bound
$v_p(j!)\leq(j-1)/(p-1)$ gives the result. This scalar estimate is the
precise place where the proof excludes $p=3$: at $j=3$ one loses one
power of $3$.

All remaining coefficients are $p$-integral. Only finitely many
exponential degrees can contribute to the constant term because the
negative $x$-degree is bounded by the available $t$-degree $cN$. Thus
every term in (8) is divisible by $p^{3r}$, proving Theorem 1.

## 6. The next defect layer

For the special case $u=U_{1,2;1}$ define

```math
Q_{p,r}(n)=
\frac{u(np^r)-u(np^{r-1})}{p^{3r}}.
```

Theorem 1 proves that this is $p$-integral for $p\geq5$. Exact computations
suggest the stronger stabilization

```math
Q_{p,r}(n)\equiv Q_{p,r-1}(n)
\pmod {p^{2r-2-\delta_p}},
\qquad
\delta_5=1,\quad \delta_p=0\ (p\geq7).
\qquad\text{(17)}
```

This remains conjectural. It is the natural next refinement of the proved
cubic tower.

## 7. Literature boundary

Coster's generalized Apéry theorem supplies an economical published route
for the named A333592 specialization after its endpoint is separated. The
argument above has a different scope: it treats arbitrary positive slopes
$a,b$ and arbitrary linear cutoff $cN$ in one prefix theorem. The nearest
repository references are:

- [Coster, Theorem 4](https://ir.cwi.nl/pub/5804/5804D.pdf), for shifted
  generalized Apéry sums;
- [Straub's multivariate Apéry supercongruences](https://arxiv.org/abs/1401.0854),
  for broad Laurent-polynomial families.

No claim is made here that either source contains Theorem 1, and no novelty
claim should be made until a specialist search checks the precise moving
prefix and two negative-binomial slopes.

## 8. Verification

Run

```text
python verification/related/verify_mixed_negative_binomial_cubic_tower.py
```

The exact checker verifies the constant-term values, the square and cross
coefficient bounds in Lemma 2, the full positive-parameter family on an
exact grid, and a larger modular grid. These computations support
transcription and boundary control; the Cartier argument is the proof.
