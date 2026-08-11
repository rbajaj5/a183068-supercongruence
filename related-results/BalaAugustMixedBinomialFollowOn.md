# The August mixed-binomial follow-on

**Status:** complete elementary mixed-binomial theorem; A333473 and A333592
corollaries; two exact counterexamples; the cubic mixed negative-binomial
case remains open.

**Source boundary:** Peter Bala proposed the product, twist, and
negative-parameter families in correspondence on August 11, 2026. The proof
below uses the classical Ljunggren--Jacobsthal--Kazandzidis scaling theorem.
No literature-priority claim is made for the present assembly.

## 1. Disposition of the August queue

| Item | Result |
| --- | --- |
| A119258 denominator primes | Closed: the arbitrary integral coefficient slope removes the exclusion |
| Chebyshev primes dividing the coefficient slope | Closed by the same theorem |
| A333473 | Its named quadratic tower holds for every odd prime; the larger algebraic-kernel family remains open |
| Mixed negative-binomial sum | Quadratic tower proved; prime-level cubic term proved in the first packet; all-level cubic tower still open |
| Products and twists | Cubic for three or more generalized-binomial factors; quadratic for two |
| Index-dependent negative substitutions | Two families fail cubically at $p=5$; two companion families remain computational candidates |
| A333592 | Cubic tower closed by Coster's shifted theorem plus one endpoint |

The main structural point is that the number of independent binomial
factors supplies the discard exponent. The scaled stratum is then controlled
by one common Jacobsthal quotient estimate.

## 2. A mixed-binomial Frobenius theorem

For an integer $a$ and $m\geq0$, generalized binomial coefficients are
interpreted by

```math
\binom{-a}{m}=(-1)^m\binom{a+m-1}{m}
\qquad(a>0).
```

Fix nonzero integers $a_1,\ldots,a_d$, positive integers
$b_1,\ldots,b_d,c$, and define

```math
P_N(X)=
\sum_{k=0}^{cN}
\left(\prod_{j=1}^d\binom{a_jN}{b_jk}\right)X^k.
\qquad\text{(1)}
```

For an odd prime $p$ not dividing any $b_j$, put

```math
\epsilon_p=
\begin{cases}
1,&p=3,\\
0,&p\geq5,
\end{cases}
```

and

```math
E_{p,d}(r)=\min\{dr,\,3r-\epsilon_p\}.
\qquad\text{(2)}
```

### Theorem 1

For all $n,r\geq1$,

```math
\boxed{
P_{np^r}(X)
\equiv P_{np^{r-1}}(X^p)
\pmod {p^{E_{p,d}(r)}}
}
\qquad\text{(3)}
```

coefficientwise in $\mathbb Z[X]$.

For $p\geq5$, the exponent is therefore $r$ for one factor, $2r$ for
two factors, and $3r$ for three or more factors. Evaluation at $X=1$ gives
the untwisted sums. Evaluation at $X=-1$ gives the twisted sums because
$p$ is odd.

### 2.1 The discarded coefficients

Let $N=np^r$ and suppose $p\nmid k$. If $a_j>0$ and the binomial
coefficient is nonzero, then

```math
\binom{a_jN}{b_jk}
=\frac{a_jN}{b_jk}
 \binom{a_jN-1}{b_jk-1},
```

so its valuation is at least $r$. If $a_j=-h_j<0$, then

```math
\binom{-h_jN}{b_jk}
=(-1)^{b_jk}
 \frac{h_jN}{h_jN+b_jk}
 \binom{h_jN+b_jk}{b_jk}.
```

The denominator is a $p$-adic unit, so this factor also has valuation at
least $r$. Hence the coefficient of $X^k$ in $P_N$ is divisible by
$p^{dr}$, and therefore by the modulus in (3).

### 2.2 The scaled coefficients

Write $N=pM$ and $k=p\ell$. For a positive slope, the adjacent quotient is

```math
\frac{\binom{pa_jM}{pb_j\ell}}
     {\binom{a_jM}{b_j\ell}}.
```

For a negative slope, the signs agree because $p$ is odd, the rational
prefactors in the preceding display cancel, and the remaining quotient is

```math
\frac{\binom{p(h_jM+b_j\ell)}{pb_j\ell}}
     {\binom{h_jM+b_j\ell}{b_j\ell}}.
```

Thus every factor is governed by the same adjacent binomial scaling
theorem.

Put $s=v_p(\ell)$. If $s<r-1$, then $p\nmid b_j$ implies that the minimum
valuation of the two lower binomial parts is $s$. Every quotient is
therefore $1$ modulo

```math
p^{3(s+1)-\epsilon_p}.
\qquad\text{(4)}
```

At the lower scale, each nonzero binomial factor has valuation at least
$r-1-s$. Consequently the difference between the upper and lower products
has valuation at least

```math
d(r-1-s)+3(s+1)-\epsilon_p.
\qquad\text{(5)}
```

If $d\leq3$, expression (5) is at least $dr$; if $d\geq3$, it is at least
$3r-\epsilon_p$. If $s\geq r-1$, the scaling quotient alone is $1$ modulo
$p^{3r-\epsilon_p}$. Zero factors at a positive upper argument occur at
both scales simultaneously, and $\ell=0$ is an equality. This proves the
coefficientwise transfer and hence Theorem 1.

## 3. A333473 is the two-factor case

The OEIS sequence [A333473](https://oeis.org/A333473) has the exact sum

```math
a(N)=\sum_{k=0}^N
\binom Nk\binom{N+2k-1}{2k}.
\qquad\text{(6)}
```

Since

```math
\binom{N+2k-1}{2k}=\binom{-N}{2k},
```

formula (6) is Theorem 1 with

```math
(a_1,a_2)=(1,-1),
\qquad
(b_1,b_2)=(1,2),
\qquad
c=1.
```

### Corollary 2

For every odd prime $p$ and all $n,r\geq1$,

```math
\boxed{
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
}
\qquad\text{(7)}
```

This proves the displayed conjecture on A333473 and extends its stated
range from $p\geq5$ to every odd prime.

The page also proposes a larger family. If

```math
F(x)=\frac{1-\sqrt{1-4x-4x^2}}{2x},
```

then $F=1+x+xF^2$. Writing $W=F-1$ and applying Lagrange inversion gives,
for $R>0$,

```math
[x^{RN}]F(x)^{SN}
=\frac SR[t^{RN-1}]
(1+t)^{SN-1}(t^2+2t+2)^{RN}.
\qquad\text{(8)}
```

Formula (8) is an exact normalization of the remaining problem, but for
general $(R,S)$ it is not the two-factor sum (6). Since
$t^2+2t+2=1+(1+t)^2$, expanding (8) gives the completely explicit form

```math
[x^{RN}]F(x)^{SN}
=\frac SR\sum_{j=0}^{RN}
\binom{RN}{j}\binom{SN+2j-1}{RN-1}.
\qquad\text{(8a)}
```

The second upper argument in (8a) depends on $j$. This locates the remaining
obstruction precisely: (8a) lies in the index-dependent lane of Section 7,
not in Theorem 1's fixed-slope lane. The full family therefore remains open.
The checker verifies (8a) directly and finds no quadratic-tower failure for
$1\leq R,S\leq3$, $p\in\{5,7\}$, $n\in\{1,2\}$, and levels one and two.

## 4. The mixed negative-binomial tower

The first packet considered

```math
u(N)=\sum_{k=0}^N\binom{-N}{k}\binom{-2N}{k}.
\qquad\text{(9)}
```

Theorem 1 immediately supplies the unconditional baseline

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{2r}}
\qquad\text{(10)}
```

for every odd prime. The Bernoulli calculation in the
[first packet](BalaAugustCoefficientPacket.md#6-the-negative-binomial-strengthening-is-false)
proves the stronger $p^3$ congruence at the prime boundary and computes its
leading term. Exact tests now find

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{3r}}
```

for $p\in\{3,5,7,11,13\}$, $1\leq n\leq4$, and every tested level with
$np^r\leq700$. This is evidence only. The missing theorem is precisely one
extra power per level after evaluating the two-factor polynomial at $X=1$;
it cannot come from coefficientwise divisibility.

### 4.1 A stabilized first-defect conjecture

The cubic evidence has a stronger structure. Put

```math
D_{p,r}(n)=u(np^r)-u(np^{r-1}).
```

Whenever $p^{3r}\mid D_{p,r}(n)$, define

```math
Q_{p,r}(n)=\frac{D_{p,r}(n)}{p^{3r}}.
\qquad\text{(10a)}
```

The exact data support the simultaneous conjectures

```math
D_{p,r}(n)\equiv0\pmod {p^{3r}}
```

and, for $r\geq2$,

```math
\boxed{
Q_{p,r}(n)\equiv Q_{p,r-1}(n)
\pmod {p^{\,2r-2-\delta_p}},
}
\qquad
\delta_p=
\begin{cases}
1,&p=5,\\
0,&p\ne5.
\end{cases}
\qquad\text{(10b)}
```

In particular, the leading residue $Q_{p,r}(n)\bmod p$ is independent of
$r$. Thus the missing cubic theorem appears to be the integrality boundary
of a substantially more rigid $p$-adic defect tower.

The modular checker computes each summand by tracking its $p$-adic exponent
and unit separately. It verifies (10a)--(10b) for
$p\in\{3,5,7,11,13\}$, $1\leq n\leq6$, and every level $r\leq4$ with
$np^r\leq100{,}000$. This remains evidence, not a proof. The exceptional
$p=5$ loss is attained in the grid.

## 5. Bala's product and twist proposal

Take $b_j=1$ in Theorem 1. For any nonzero integers
$a_1,\ldots,a_d$, any fixed cutoff $cN$, and either sign, define

```math
S_\pm(N)=
\sum_{k=0}^{cN}(\pm1)^k
\prod_{j=1}^d\binom{a_jN}{k}.
\qquad\text{(11)}
```

### Corollary 3

For every $p\geq5$,

```math
S_\pm(np^r)\equiv S_\pm(np^{r-1})
\pmod {p^{\min(d,3)r}}.
\qquad\text{(12)}
```

Thus Bala's proposed untwisted and twisted products have a uniform cubic
tower as soon as there are at least three factors. Two factors have a
uniform quadratic tower. Special two-factor sums may be stronger after a
Vandermonde collapse or a sum-level cancellation, but that is extra
structure rather than a consequence of sign replacement.

## 6. A Coster closure for A333592

The sequence [A333592](https://oeis.org/A333592) is

```math
A(N)=\sum_{k=0}^N\binom{N+k-1}{k}^2.
```

Separate its endpoint:

```math
A(N)=
\sum_{k=0}^{N-1}\binom{N+k-1}{k}^2
+\binom{2N-1}{N}^2.
\qquad\text{(13)}
```

The first term is Coster's shifted generalized Apéry sum
$w_{0,2,1}(N-1)$. The $B=2$, $\epsilon=(-1)^A$ branch of
[Coster's Theorem 4](https://ir.cwi.nl/pub/5804/5804D.pdf) gives its cubic
tower for $p\geq5$. For the endpoint,

```math
\binom{2N-1}{N}^2=\frac14\binom{2N}{N}^2,
```

and adjacent Jacobsthal scaling gives the same modulus because $4$ is a
$p$-adic unit.

### Corollary 4

For every prime $p\geq5$ and all $n,r\geq1$,

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.
}
\qquad\text{(14)}
```

This is a reduction to a published theorem, not a new supercongruence
mechanism.

## 7. Index-dependent companions: two failures and two survivors

Theorem 1 does not cover factors such as $\binom{2k}{N}$ or
$\binom{-N-k}{k}$, whose upper arguments depend on the summation index.
Direct normalization matters here.

Consider

```math
V(N)=\sum_{k=0}^N
\binom Nk^2\binom{2k}{N}\binom{-N-k}{k}.
```

Then

```math
V(2)=48,
\qquad
V(10)=-2645496479352,
```

and

```math
v_5\bigl(V(10)-V(2)\bigr)=2.
\qquad\text{(15)}
```

Thus even the first cubic level fails. The cutoff family

```math
W_c(N)=\sum_{k=0}^{cN}
\binom{-N}{k}^2\binom{2k}{N}\binom{-N-k}{k}
```

also fails: $W_2(1)=20$, $W_2(5)=28417526446039920$, and

```math
v_5\bigl(W_2(5)-W_2(1)\bigr)=2.
\qquad\text{(16)}
```

The analogous companions with the last factor
$\binom{N+k}{k}$ survive the exact grid in the checker through the second
level for $p\in\{5,7,11\}$. They remain conjectures; the contrasting
behavior in (15)--(16) shows that they require a sign-sensitive proof.

## 8. Literature boundary

The external arithmetic input is classical binomial scaling. Coster's
report supplies only Corollary 4's shifted generalized-Apéry block.
[Straub's polynomial Apéry theorem](https://arxiv.org/abs/1803.07146)
is a nearby polynomial Frobenius result, but the theorem stated here allows
arbitrary integral upper slopes, weighted lower indices, negative upper
parameters, and a fixed linear cutoff. A targeted search found no exact
statement with that full combination. This is a search report, not a
priority claim.

## 9. Verification

Run

```text
python verification/related/verify_bala_august_mixed_binomial_follow_on.py
```

The checker performs 3,390 exact checks. It tests the coefficientwise mixed
theorem, the A333473 identification and tower, the formerly excluded
A119258 and Chebyshev primes, the extended cubic evidence for $u$, the
A333473 algebraic-family normalization and evidence, the stabilized
negative-binomial defect grid, the A333592 decomposition, both
counterexamples, and the surviving companion grid.
