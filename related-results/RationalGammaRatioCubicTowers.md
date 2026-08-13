# Rational gamma ratios inherit a cubic tower

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

This note isolates the congruence part of Peter Bala's fractional-factorial
packet.  The main point is that the unit-block proof for half-binomial
coefficients works with every fixed denominator, not only denominator two.

## 1. A rational-binomial transfer

Let $a,b,q$ be positive integers with $a>bq$, and put

```math
G_{a,b,q}(N)=
\binom{aN/q}{bN}
=
\frac{\Gamma(aN/q+1)}
{\Gamma(bN+1)\Gamma((a-bq)N/q+1)}.
\tag{1}
```

The value in (1) need not be an ordinary integral binomial coefficient.
It is a rational number whose fixed denominator is controlled by $q$.

### Lemma 1 (rational-binomial unit block)

Let $p\geq5$ be prime, $p\nmid q$, and $N=pM$.  If $e=v_p(N)$, then

```math
\boxed{
\frac{G_{a,b,q}(N)}{G_{a,b,q}(M)}
\equiv1\pmod {p^{3e}}.
}
\tag{2}
```

Here and below a congruence between rational numbers is interpreted in
$\mathbb Q_p$.

#### Proof

The finite product for (1) is

```math
G_{a,b,q}(N)
=
\frac1{q^{bN}(bN)!}
\prod_{j=0}^{bN-1}(aN-qj).
\tag{3}
```

Because $p\nmid q$ and $p\mid N$, the numerator factor in (3) is divisible
by $p$ exactly when $p\mid j$.  Those factors reproduce the numerator at
level $M$, and the multiples of $p$ in $(bN)!$ reproduce $(bM)!$.
There are $b(N-M)$ remaining factors.  Since $p$ is odd,
$b(N-M)=bM(p-1)$ is even.  Cancelling the powers of $q$ and the signs gives
the exact identity

```math
\frac{G_{a,b,q}(N)}{G_{a,b,q}(M)}
=
\prod_{\substack{1\leq j<bN\\p\nmid j}}
\left(1-\frac{aN}{qj}\right).
\tag{4}
```

Put $P=p^e$ and

```math
S_\nu=
\sum_{\substack{1\leq j<bN\\p\nmid j}}j^{-\nu}.
```

The interval in this sum is a union of complete blocks of length $P$.
For one block of reduced residues modulo $P$,

```math
S_1\equiv0\pmod {P^2},
\qquad
S_2\equiv0\pmod P.
\tag{5}
```

For the second congruence, multiplication by a unit whose square is not
$1$ modulo $p$ permutes the reduced residues.  For the first, pair $u$
with $P-u$ and use the second congruence.  Translating a block by a
multiple of $P$ preserves both precisions, because

```math
\frac1{tP+u}\equiv\frac1u-\frac{tP}{u^2}\pmod {P^2},
\qquad
\frac1{(tP+u)^2}\equiv\frac1{u^2}\pmod P.
```

In the expansion of (4), the linear term is $(aN/q)S_1$.  The quadratic
term is

```math
\left(\frac{aN}{q}\right)^2
\frac{S_1^2-S_2}{2}.
```

They are both divisible by $P^3$.  Every term of degree at least three
contains $N^3$, while all $j$ and $q$ in (4) are $p$-adic units.  Thus
every nonconstant term is divisible by $P^3=p^{3e}$, proving (2).
$\square$

## 2. The residue-balanced gamma theorem

Let $E$ be a finitely supported integer-valued function on the positive
rationals, and define

```math
F(N)=\prod_{\alpha\in\mathbb Q_{>0}}
\Gamma(\alpha N+1)^{E(\alpha)}.
\tag{6}
```

Assume the following two conditions.

**Slope balance:**

```math
\sum_\alpha \alpha E(\alpha)=0.
\tag{7}
```

**Residue-class balance:** for every nonzero class
$\rho\in\mathbb Q/\mathbb Z$,

```math
\sum_{\alpha\equiv\rho\pmod{\mathbb Z}}E(\alpha)=0.
\tag{8}
```

Let $Q$ be a common denominator of the slopes in (6).

### Theorem 2 (fractional-factorial cubic tower)

For every prime $p\geq5$ with $p\nmid Q$ and all positive integers $n,r$,

```math
\frac{F(np^r)}{F(np^{r-1})}\equiv1\pmod {p^{3r}}.
\tag{9}
```

If $F(np^{r-1})$ is $p$-integral, then

```math
\boxed{
F(np^r)\equiv F(np^{r-1})\pmod {p^{3r}}.
}
\tag{10}
```

#### Proof

Condition (8) lets us pair every numerator gamma factor of nonintegral
slope with a denominator factor in the same residue class modulo
$\mathbb Z$.  Suppose the two slopes are $\alpha>\beta$ and put
$d=\alpha-\beta\in\mathbb Z_{>0}$.  The exact identity

```math
\frac{\Gamma(\alpha N+1)}{\Gamma(\beta N+1)}
=
\binom{\alpha N}{dN}\Gamma(dN+1)
\tag{11}
```

replaces that pair by one rational binomial of the form (1) and one
integer-slope factorial.  If the numerator slope is smaller, use the
inverse of (11).  Repeating this operation removes every nonintegral
gamma factor.

What remains is a product of rational binomials and a balanced
integer-slope factorial ratio.  Balance is preserved by (11), so the
integer-slope part is balanced.  Its adjacent quotient is $1$ modulo
$p^{3r}$ by the classical Ljunggren--Jacobsthal binomial congruence (or
equivalently by the balanced-factorial closure theorem).  Each rational
binomial quotient has the same property by Lemma 1.  Products, integer
powers, and inverses preserve the congruence, proving (9).  Multiplication
by the $p$-integral lower-level value proves (10). $\square$

## 3. A364175 is now closed

The [OEIS A364175](https://oeis.org/A364175) sequence is

```math
A(N)=
\frac{(6N)!\,(2N/3)!}
{(3N)!\,(2N)!\,(5N/3)!}.
\tag{12}
```

Its slopes balance, and the only nonzero residue class contains
$+2/3$ and $-5/3$.  More concretely,

```math
A(N)=
\binom{6N}{3N}
\binom{3N}{N}
\binom{5N/3}{N}^{-1}.
\tag{13}
```

David Radcliffe proved in July 2026 that every value in (12) is an
integer.  Theorem 2, with $Q=3$, therefore proves the conjecture still
recorded on the OEIS page:

### Corollary 3

For every prime $p\geq5$ and all positive integers $n,r$,

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.
}
\tag{14}
```

The initial values are

```text
1, 36, 3564, 408408, 49697388, 6249195036, ...
```

## 4. Two whole row families

Theorem 2 also closes two live parameterized directions that a search of
Peter Bala's fractional-factorial records exposed.

### Corollary 4 (every row of A365025)

For a fixed integer $s\geq0$, put

```math
U_s(N)=
\frac{
\Gamma(N/2+1)
\Gamma((2s+1)N+1)
\Gamma((2s+1/2)N+1)}
{
\Gamma(N+1)
\Gamma(sN+1)^2
\Gamma((s+1/2)N+1)^2}.
\tag{15}
```

The finite-sum identity on [OEIS A365025](https://oeis.org/A365025),

```math
U_s(N)=
\sum_{j=0}^{sN}
\binom{(2s+1)N}{sN-j}^{2}
\binom{N+j-1}{j},
\tag{16}
```

shows that every value is an integer.  The slopes in (15) balance.  In the
nonzero class $1/2+\mathbb Z$ there are two numerator factors and two
denominator factors.  Theorem 2 therefore proves, for every $s\geq0$,
prime $p\geq5$, and positive $n,r$,

```math
\boxed{
U_s(np^r)\equiv U_s(np^{r-1})\pmod {p^{3r}}.
}
\tag{17}
```

This proves the all-row conjecture on A365025, including its named rows
[A365026](https://oeis.org/A365026) and
[A365027](https://oeis.org/A365027).

### Corollary 5 (the stable rows of A364513)

For a fixed integer $s\geq3$ and $N\geq1$, the Dixon evaluation recorded
on [OEIS A364513](https://oeis.org/A364513) is

```math
V_s(N)=
\frac{s-2}{s}
\frac{
\Gamma((s+2)N+1)\Gamma(sN/2+1)^2}
{
\Gamma((s+2)N/2+1)
\Gamma(sN+1)
\Gamma((s-2)N/2+1)
\Gamma(N+1)^2}.
\tag{18}
```

The exact finite sum

```math
V_s(N)=
\sum_{j=0}^{N}
\binom{sN-1}{N-j}^{2}
\binom{(s-2)N+j-2}{j}
\tag{19}
```

from the same record makes these values integers.  If $s$ is even, all
slopes in (18) are integral.  If $s$ is odd, the two
copies of $s/2$ balance the copies of $(s+2)/2$ and $(s-2)/2$ in the class
$1/2+\mathbb Z$.  The constant $(s-2)/s$ cancels from every adjacent
quotient.  Hence every fixed row $s\geq3$ satisfies the full cubic tower.

In particular this proves the conjectures on
[A364515](https://oeis.org/A364515),
[A364516](https://oeis.org/A364516), and
[A364517](https://oeis.org/A364517), which are rows $4,6,7$.
It does **not** settle row $1$, A364514: that row has an affine
odd-index factorial formula rather than the homogeneous form (18).

The same source pass also shows that
[A364304](https://oeis.org/A364304), row $7$ of A364303, is the case
$a=7$ of the already proved
[Dixon--Legendre tower](DixonLegendreHalfBinomialTowers.md).  Its named
conjecture is therefore closed without another argument.

## 5. What happens to the surrounding packet

The same theorem applies to A364172--A364184 (A364185 is not part of this
fractional-factorial family).  Each displayed gamma quotient has balanced
slopes and balanced nonintegral residue classes, with fixed denominator
$2$ or $3$.  Consequently its proposed $p^{3r}$ tower for $p\geq5$ is
automatic **once its values are known to be integral**.

Thus the packet separates cleanly:

- A364173: integrality and the tower are proved in the repository's
  [dedicated note](A364173IntegralHalfBinomialTower.md);
- A364175: Radcliffe supplies integrality and Corollary 3 supplies the
  tower;
- A364176: integrality follows from the repository's
  [affine-Landau floor lemma](A364176AffineLandauTower.md), and Theorem 2
  supplies the tower;
- the remaining records: their cubic congruence component follows from
  Theorem 2 in $\mathbb Q_p$, while their stated global integrality
  conjectures remain the actual unresolved obligations.

This is stronger than checking each residue class of $N$ separately.  It
shows that no new odd-prime supercongruence mechanism is needed anywhere
in this packet: the only new arithmetic is integrality.

## 6. The Bober fractional-index packet

Peter Bala's August 2026 follow-up identifies fractional-index variants of
12 Bober records.  The 15 formulas currently visible in approved OEIS
comments all satisfy slope balance and residue-class balance. Theorem 2
therefore proves their adjacent $p^{3r}$ quotient congruence for every
$p\geq5$. A uniform translated-Landau theorem now proves all eleven $N/2$
variants integral; the four denominator-three/four global integrality
statements remain separate open problems.

The exact records, admissible denominators, source boundary, and 1,149-check
certificate are in the
[Bober sporadic factorial-ratio packet](BoberSporadicFactorialRatioPacket.md).

## 7. Scope and priority boundary

The theorem does not cover primes dividing the fixed denominator $Q$.
For the named packet this excludes $2$ and/or $3$, exactly outside the
conjectured range.  It also does not prove integrality of a gamma quotient;
$p$-adic stability and global integrality are logically separate.

Zudilin's 2019 factorial-ratio theorem treats balanced **integer-slope**
factorial ratios and supplies the published classical baseline.  Targeted
searches for A364175, its exact gamma quotient, and rational-binomial
adjacent scaling did not locate the denominator-$q$ formulation above.
That is evidence for review routing, not a priority certificate.

## 8. References

- [OEIS A364175](https://oeis.org/A364175), including the integrality
  update and the stated cubic-tower conjecture.
- David Radcliffe,
  [*Integrality of a Ratio of Fractional Factorials*](https://oeis.org/A364175/a364175.pdf),
  linked from the A364175 record.
- [Zudilin, *Congruences for q-binomial coefficients*](https://arxiv.org/abs/1901.07843),
  especially Section 5 for balanced integer factorial ratios.
- [Balanced factorial ratios inherit a cubic tower](BalancedFactorialRatioCubicTowers.md),
  for the integer-slope closure used in Theorem 2.
- [Dixon--Legendre half-binomial towers](DixonLegendreHalfBinomialTowers.md),
  the denominator-two precursor to Lemma 1.
- [OEIS A365025](https://oeis.org/A365025) and
  [OEIS A364513](https://oeis.org/A364513), for the two row-family
  formulas and their stated conjectures.

## 9. Verification

Run

```text
python verification/related/verify_rational_gamma_ratio_towers.py
```

The checker verifies the exact quotient identity for many values of
$a,b,q,p,N$; the $p^{3e}$ transfer; A364175's factorization and initial
values; exact adjacent towers at two levels; the residue-balance, initial
finite integrality, and finite tower checks for A364172--A364184; and the
two row-family identities and towers.
