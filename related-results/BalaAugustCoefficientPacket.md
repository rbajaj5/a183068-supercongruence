# Bala's August coefficient packet: rational rays, Chebyshev towers, and a Bernoulli obstruction

**Status:** complete proof candidate for the two parameter families and the
prime-level defect formula; exact checks pass; independent review and
literature-priority work pending.

**Source boundary:** Peter Bala suggested the families in correspondence on
August 11, 2026.  The OEIS pages record the named conjectures cited below.
The rational-parameter framing argument and the Bernoulli correction are
proved here; finite verification is supporting evidence, not the proof.

## 1. Results at a glance

This packet produces three different outcomes.

1. Every ray $T(An,Bn)$ of the triangle A119258 has a cubic adjacent-scale
   tower at primes away from one fixed denominator.
2. Every coefficient family
   $[x^{rn}]T_n\!\left((1+x)/(1-x)\right)^s$ has the same cubic tower for
   $p\geq5$ with $p\nmid r$.
3. The proposed stronger negative-binomial congruence is false.  Its first
   nonzero term is controlled by $B_{p-3}$ and normally occurs at exactly
   $p^3$.

The first theorem closes the displayed odd-prime conjectures on A119259 and
A333562.  Fixed linear identities then close A333564 and A333565.  The
Chebyshev theorem includes A103885.  A333473 remains a separate quadratic
coefficient problem; nothing below silently promotes it.

## 2. Rational coefficient framing

For $a,b\in\mathbb Q$ put

```math
C_{a,b}(N)=[z^N](1+z)^{aN}(1-z)^{bN}.
\qquad\text{(1)}
```

Let $Q$ be a common denominator of $a$ and $b$.  The rational-parameter
extension of the repository's
[coefficient-framing theorem](CoefficientFramingCubicTower.md#44-rational-parameters-away-from-their-denominators)
gives, for $p\geq5$ and $p\nmid Q$,

```math
C_{a,b}(np^r)\equiv C_{a,b}(np^{r-1})\pmod {p^{3r}}.
\qquad\text{(2)}
```

For clarity, the proof does not divide an integer theorem by $Q$.  In the
local ring $\mathbb Z_p$, both $a$ and $b$ are integral.  Hence every
generalized binomial coefficient occurring in (1) is $p$-integral.  The
reduced-logarithm identity, quadratic Cartier estimate, and integration by
parts in the original proof then apply word for word.

## 3. All rays of A119258

Let $T(N,K)$ be the triangle [A119258](https://oeis.org/A119258).  For
$0\leq K\leq N$ its row-polynomial description is

```math
T(N,K)=[x^K]\frac{(1+2x)^N}{1+x}.
\qquad\text{(3)}
```

The coefficient change $x=z/(1-z)$ gives the exact residue identity

```math
[x^K]f(x)
=[z^K](1-z)^{K-1}f\!\left(\frac z{1-z}\right).
\qquad\text{(4)}
```

Applying (4) to (3), and then putting $N=An$, $K=Bn$, yields

```math
T(An,Bn)
=[z^{Bn}](1+z)^{An}(1-z)^{-(A-B)n}.
\qquad\text{(5)}
```

Set $M=Bn$.  Formula (5) is

```math
T(An,Bn)=C_{A/B,-(A-B)/B}(M).
\qquad\text{(6)}
```

### Theorem 1 (A119258 ray theorem)

Let $A>B\geq1$, put

```math
q=\frac{B}{\gcd(A,B)},
```

and let $p\geq5$ be prime with $p\nmid q$.  For all $n,r\geq1$,

```math
\boxed{
T(Anp^r,Bnp^r)
\equiv T(Anp^{r-1},Bnp^{r-1})
\pmod {p^{3r}}.
}
\qquad\text{(7)}
```

Indeed, $q$ is a common denominator after reducing the two rational
parameters in (6), and (7) is (2) with base index $Bn$.

### The truncated negative-binomial ray

For $c\geq1$, define

```math
S_c(n)=\sum_{j=0}^{cn}2^j\binom{n+j-1}{j}.
\qquad\text{(8)}
```

Since

```math
S_c(n)=[x^{cn}]\frac1{(1-x)(1-2x)^n},
```

the change $x=z/(1+z)$ gives

```math
S_c(n)
=[z^{cn}](1+z)^{(c+1)n}(1-z)^{-n}
=T((c+1)n,cn).
\qquad\text{(9)}
```

Therefore

```math
S_c(np^r)\equiv S_c(np^{r-1})\pmod {p^{3r}}
\qquad\text{(10)}
```

for every $p\geq5$ with $p\nmid c$.  The cases $c=1$ and $c=3$ are
[A119259](https://oeis.org/A119259) and
[A333562](https://oeis.org/A333562), respectively, so their displayed cubic
towers are unconditional for every $p\geq5$.

## 4. Three more named consequences

For $n\geq1$, the OEIS identities

```math
\begin{aligned}
\operatorname{A333564}(n)
 &=\frac{\operatorname{A119259}(n)-(-1)^n}{2},\\
\operatorname{A333565}(n)
 &=2\operatorname{A119259}(n)-(-1)^n
\end{aligned}
\qquad\text{(11)}
```

show that [A333564](https://oeis.org/A333564) and
[A333565](https://oeis.org/A333565) inherit (7).  For odd $p$, the parity of
$np^r$ is independent of $r$, and $2$ is a $p$-adic unit.  Thus both
sequences satisfy their conjectured $p^{3r}$ tower for every $p\geq5$.

The page [A103885](https://oeis.org/A103885) gives, for $n\geq1$,

```math
\operatorname{A103885}(n)
=\frac12[x^n]\left(\frac{1+x}{1-x}\right)^{2n}
=\frac12 C_{2,-2}(n).
\qquad\text{(12)}
```

The integer-parameter case of (2) proves its full cubic tower for every
$p\geq5$.

## 5. The complete Chebyshev family

Let

```math
R(x)=\frac{1+x}{1-x},
\qquad
A_{r,s}(n)=[x^{rn}]T_n(R(x))^s,
\qquad\text{(13)}
```

where $r,s\geq1$ and $T_n$ is the Chebyshev polynomial of the first kind.
Put $x=t^2$.  The elementary identity

```math
T_n(R(t^2))
=\frac12\left(R(t)^n+R(t)^{-n}\right)
\qquad\text{(14)}
```

follows either from $T_n((w+w^{-1})/2)=(w^n+w^{-n})/2$ or directly from the
Chebyshev recurrence.  Raising (14) to the $s$-th power gives

```math
A_{r,s}(n)
=2^{-s}\sum_{j=0}^s\binom sj
[t^{2rn}]R(t)^{(2j-s)n}.
\qquad\text{(15)}
```

With $N=2rn$, each summand in (15) is

```math
C_{(2j-s)/(2r),-(2j-s)/(2r)}(N).
\qquad\text{(16)}
```

### Theorem 2 (Chebyshev coefficient tower)

For every $r,s,n,k\geq1$ and every prime $p\geq5$ with $p\nmid r$,

```math
\boxed{
A_{r,s}(np^k)
\equiv A_{r,s}(np^{k-1})
\pmod {p^{3k}}.
}
\qquad\text{(17)}
```

All denominators in (16) divide $2r$, so (2) applies when $p\geq5$ and
$p\nmid r$.  The factor $2^{-s}$ is a $p$-adic unit, and summing proves
(17).  The source case $r=s=1$ is A103885.  The primes dividing $r$ remain a
separate boundary; (17) does not hide them inside the notation.

## 6. The negative-binomial strengthening is false

Consider Bala's proposed example

```math
u(n)=\sum_{k=0}^n\binom{-n}{k}\binom{-2n}{k}.
\qquad\text{(18)}
```

The first terms are

```text
3, 39, 705, 14343, 310878, 7012533, 162602583, ...
```

The suggested congruence $u(p)\equiv u(1)\pmod {p^5}$ does not hold.  The
first defect can in fact be evaluated.

### Theorem 3 (Bernoulli leading defect)

For every prime $p\geq5$,

```math
\boxed{
u(p)\equiv3+2p^3B_{p-3}\pmod {p^4},
}
\qquad\text{(19)}
```

where $B_m$ is the $m$-th Bernoulli number, interpreted $p$-adically.

#### Proof

Write $H_m^{(a)}=\sum_{k=1}^m k^{-a}$ and

```math
H(1,2)=\sum_{1\leq j<k\leq p-1}\frac1{jk^2}.
```

The standard finite harmonic congruences are

```math
\begin{aligned}
H_{p-1}^{(1)}&\equiv-\frac{p^2}{3}B_{p-3}\pmod {p^3},\\
H_{p-1}^{(2)}&\equiv \frac{2p}{3}B_{p-3}\pmod {p^2},\\
H_{p-1}^{(3)}&\equiv0\pmod p,\\
H(1,2)&\equiv B_{p-3}\pmod p.
\end{aligned}
\qquad\text{(20)}
```

They follow by replacing inverse powers by their Fermat power residues and
applying Faulhaber's formula; the last line is the depth-two version of the
same calculation.  The general depth-two congruence is also recorded in
Roberto Tauraso's work on alternating multiple harmonic sums and in
Jianqiang Zhao's structural treatment of multiple harmonic sums modulo $p$.

For $1\leq k<p$,

```math
\binom{-p}{k}\binom{-2p}{k}
=\frac{2p^2}{k^2}
\prod_{j=1}^{k-1}\left(1+\frac pj\right)
                    \left(1+\frac{2p}j\right).
```

Modulo $p^4$ this is

```math
\frac{2p^2}{k^2}
+\frac{6p^3}{k^2}H_{k-1}^{(1)}.
```

Summing the interior terms and using (20) gives

```math
\sum_{k=1}^{p-1}\binom{-p}{k}\binom{-2p}{k}
\equiv
\frac{22}{3}p^3B_{p-3}pmod {p^4}.
\qquad\text{(21)}
```

The endpoint is

```math
\binom{-p}{p}\binom{-2p}{p}
=\binom{2p-1}{p}\binom{3p-1}{p}.
```

Expanding the two products with (20) gives

```math
\binom{2p-1}{p}
\equiv1-\frac23p^3B_{p-3},
\qquad
\binom{3p-1}{p}
\equiv2-4p^3B_{p-3}pmod {p^4}.
```

Their product is $2-(16/3)p^3B_{p-3}$ modulo $p^4$.  Adding the $k=0$
term, (21), and the endpoint proves (19). $\square$

At the smallest prime in Bala's proposed range,

```math
u(7)-u(1)
=162602580
=2^2\cdot3\cdot5\cdot7^3\cdot7901.
\qquad\text{(22)}
```

Thus the valuation is exactly $3$, not at least $5$.  The proposed
$p^{3k+3}$ higher-level tower also fails: exact arithmetic gives

```math
v_7\bigl(u(49)-u(7)\bigr)=6<9.
\qquad\text{(23)}
```

The corrected experimental target is the ordinary cubic tower

```math
u(np^k)\equiv u(np^{k-1})\pmod {p^{3k}}.
\qquad\text{(24)}
```

The checker finds no failure in its stated finite grid, but (24) is retained
as a conjecture: Theorem 3 proves only its prime-level case.

## 7. What remains open

- [A333473](https://oeis.org/A333473) asks for a quadratic tower attached to
  an algebraic Schröder kernel.  It is not a rational-binomial ray and is not
  proved by Theorems 1 or 2.
- The primes dividing $B/\gcd(A,B)$ in Theorem 1 and the primes dividing $r$
  in Theorem 2 need separate local arguments.
- The ordinary cubic tower (24) remains open beyond the prime boundary.
- Bala's broader negative-parameter substitutions and twisted products must
  be normalized individually; (22) shows that sign replacement alone does
  not create a uniform exponent bonus.

## 8. Literature boundary

Bala's [notes on A103885](https://oeis.org/A103885/a103885.pdf) prove the
prime-boundary congruence $a(p)\equiv2\pmod {p^3}$ and describe the full tower
as a computational suggestion.  The targeted search for this packet located
no source proving Theorem 1 or the full two-parameter Theorem 2.  That is a
search report, not a priority claim.

The harmonic inputs in (20) are classical.  Relevant primary references are:

- Roberto Tauraso,
  [*Congruences involving alternating multiple harmonic sum*](https://arxiv.org/abs/0905.3327);
- Jianqiang Zhao,
  [*Mod $p$ structure of alternating and non-alternating multiple harmonic sums*](https://doi.org/10.5802/jtnb.762),
  *Journal de Théorie des Nombres de Bordeaux* 23 (2011), 299--308.

Thus any eventual priority claim must concern the coefficient-family
assembly or the particular defect formula, not the Bernoulli evaluations
used inside its proof.

## 9. Verification

Run

```text
python verification/related/verify_bala_august_coefficient_packet.py
```

The checker independently compares the triangle, partial-sum, rational-ray,
and Chebyshev formulas; tests both proved towers on parameter grids; verifies
(19) for a range of primes; records the exact failures (22)--(23); and tests
the corrected conjecture (24) on a small grid.  The calculations use exact
integers and rational Bernoulli numbers throughout.
