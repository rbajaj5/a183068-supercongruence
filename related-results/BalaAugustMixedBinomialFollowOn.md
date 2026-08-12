# The August mixed-binomial follow-on

**Status:** complete elementary mixed-binomial theorem; A333473 and A333592
corollaries; two exact counterexamples; the mixed negative-binomial cubic
tower is proved separately for every prime $p\geq5$.

**Source boundary:** Peter Bala proposed the product, twist, and
negative-parameter families in correspondence on August 11, 2026. The proof
below uses the classical Ljunggren--Jacobsthal--Kazandzidis scaling theorem.
No literature-priority claim is made for the present assembly.

## 1. Disposition of the August queue

| Item | Result |
| --- | --- |
| A119258 denominator primes | Closed: the arbitrary integral coefficient slope removes the exclusion |
| Chebyshev primes dividing the coefficient slope | Closed by the same theorem |
| A333473 | Its named quadratic tower and the full positive algebraic-kernel family hold for every odd prime |
| Mixed negative-binomial sum | Cubic tower proved for every odd prime; first normalized-defect residue proved stable for $p\geq5$, with only the stronger growing-modulus refinement open |
| Products and twists | Cubic for three or more generalized-binomial factors; quadratic for two |
| Index-dependent negative substitutions | Two families fail cubically at $p=5$; the two sign-opposite companions are proved cubically at the full prime boundary, and every scaled shell transfers modulo $p^{3r}$; only the aggregate unit-shell lift remains open |
| A333592 | Named cubic tower closed by Coster; the full positive-parameter family is also covered by the prefix-Cartier theorem |

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

Formula (8) is an exact normalization of the larger problem, but for
general $(R,S)$ it is not the two-factor sum (6). Since
$t^2+2t+2=1+(1+t)^2$, expanding (8) gives the completely explicit form

```math
[x^{RN}]F(x)^{SN}
=\frac SR\sum_{j=0}^{RN}
\binom{RN}{j}\binom{SN+2j-1}{RN-1}.
\qquad\text{(8a)}
```

The second upper argument in (8a) depends on $j$, so Theorem 1 does not
apply.  The separate
[algebraic-family theorem](A333473AlgebraicFamilyTower.md) resolves this
index-dependent lane: its Lagrange summand has a second normalization in
which the discarded stratum contributes two powers and the scaled stratum
is a product of two Jacobsthal quotients.  It proves the full $p^{2r}$ tower
for every odd prime, including primes dividing $R$ or $S$.

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
leading term. The separate
[prefix-Cartier theorem](MixedNegativeBinomialCubicTower.md) proves

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{3r}}
```

for every $p\geq5$ and $n,r\geq1$. It proves the extra power only after
prefix summation: the coefficientwise two-factor theorem itself remains
quadratic. The [prime-three boundary theorem](PrimeThreeNegativeBinomialBoundary.md)
proves the first cubic level for Bala's sum and computes the exact obstruction
for the full family. The prime-three boundary theorem proves the all-level
$p=3$ propagation for the maximal residue subclass, including Bala's sum.

### 4.1 A stabilized first-defect conjecture

The cubic evidence has a stronger structure. Put

```math
D_{p,r}(n)=u(np^r)-u(np^{r-1}).
```

For $p\geq5$, the prefix-Cartier theorem makes the quotient

```math
Q_{p,r}(n)=\frac{D_{p,r}(n)}{p^{3r}}.
\qquad\text{(10a)}
```

integral. Exact data support, for $r\geq2$, the further conjecture

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
$r$ by the first-defect theorem. The cubic integrality boundary is proved
for every odd prime in Bala's specialization. Only the additional powers
asserted in (10b) remain open.

The modular checker computes each summand by tracking its $p$-adic exponent
and unit separately. It verifies the cubic divisibility and (10b) for
$p\in\{3,5,7,11,13\}$, $1\leq n\leq6$, and every level $r\leq4$ with
$np^r\leq100{,}000$. These calculations remain evidence for the additional
powers in (10b); the residue modulo $p$ is now proved. The exceptional
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

## 6. Two closures for A333592

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
mechanism. Independently, the
[prefix-Cartier theorem](MixedNegativeBinomialCubicTower.md) applies to

```math
\sum_{k=0}^{AN}\binom{BN+k-1}{k}^2
```

for every pair of positive integers $A,B$, proving the cubic tower for the
entire positive-parameter family surrounding A333592.

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
$\binom{N+k}{k}$ have a proved prime boundary and a proved all-level
scaled-stratum transfer.  The
[companion boundary theorem](IndexDependentCompanionPrimeBoundary.md) shows,
for every $p\ge5$, that both sums at $np$ agree with their values at $n$
modulo $p^3$.  Its half-residue inverse-square cancellation is genuinely
sum-level: generic discarded summands have valuation only two.  It also
shows that every $p$-divisible index transfers termwise modulo $p^{3r}$ at
all levels and rewrites both sequences through one quadratic substitution.
The full towers now reduce to the aggregate unit-shell identity alone.

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
A119258 and Chebyshev primes, an extended cubic grid for $u$, the
A333473 algebraic-family normalization, the stabilized
negative-binomial defect grid, the A333592 decomposition, both
counterexamples, and the surviving companion grid.  The companion boundary
and scaled-shell theorem has its own 14,004-check certificate.

The algebraic-family theorem has a separate 91,260-check certificate.

The separate prefix-Cartier theorem has its own 1,640-check certificate.
