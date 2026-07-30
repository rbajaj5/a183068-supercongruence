# Integrality and the half-binomial tower for A364173

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

The [OEIS A364173](https://oeis.org/A364173) page records two conjectures:
the displayed gamma quotient is always an integer, and it satisfies an
adjacent $p^{3r}$ supercongruence for $p\geq5$.  This note proves both.

## 1. Statement

For $N\geq0$, define

```math
C(N)
=
\frac{
\Gamma(9N+1)\Gamma(2N+1)\Gamma(3N/2+1)}
{\Gamma(9N/2+1)\Gamma(4N+1)\Gamma(3N+1)\Gamma(N+1)}.
\tag{1}
```

### Theorem 1

For every nonnegative integer $N$, the rational number $C(N)$ is an
integer.  Moreover, for every prime $p\geq5$ and all positive integers
$n,r$,

```math
C(np^r)\equiv C(np^{r-1})\pmod {p^{3r}}.
\tag{2}
```

The prime range is sharp for the named sequence:

```math
v_2(C(2)-C(1))=1,
\qquad
v_3(C(3)-C(1))=2.
\tag{3}
```

## 2. Even indices

If $N=2m$, then

```math
C(2m)
=
\frac{(18m)!(4m)!(3m)!}{(9m)!(8m)!(6m)!(2m)!}.
\tag{4}
```

This is A295440, entry 10 in Bober's table of the sporadic integral
height-one factorial ratios.  Hence $C(2m)$ is an integer.

## 3. Odd indices

Let $N=2m+1$.  Applying the half-integer gamma formula and cancelling
the two neighboring linear factors gives

```math
C(2m+1)
=
4^{6m+3}
\frac{(4m+2)!(9m+4)!}
{(3m+1)!(8m+4)!(2m+1)!}.
\tag{5}
```

It remains to show that the factorial ratio in (5) has no prime in its
denominator.  For an integer $q\geq2$, set

```math
\delta_q(m)
=
\left\lfloor\frac{9m+4}{q}\right\rfloor
+\left\lfloor\frac{4m+2}{q}\right\rfloor
-\left\lfloor\frac{8m+4}{q}\right\rfloor
-\left\lfloor\frac{3m+1}{q}\right\rfloor
-\left\lfloor\frac{2m+1}{q}\right\rfloor .
\tag{6}
```

### Lemma 2

For all $q\geq2$ and $m\geq0$, one has $\delta_q(m)\geq0$.

#### Proof

The coefficient sums in (6) balance, so $\delta_q(m)$ depends only on
$s=m\bmod q$.  Assume $0\leq s<q$ and put

```math
\begin{aligned}
A&=
\left\lfloor\frac{9s+4}{q}\right\rfloor
-\left\lfloor\frac{8s+4}{q}\right\rfloor,\\
B&=
\left\lfloor\frac{4s+2}{q}\right\rfloor
-\left\lfloor\frac{3s+1}{q}\right\rfloor,\\
C&=\left\lfloor\frac{2s+1}{q}\right\rfloor .
\end{aligned}
\tag{7}
```

Then $\delta_q(m)=A+B-C$.  Each of $A,B,C$ is either $0$ or $1$.
If $C=0$, nonnegativity is immediate.  Suppose $C=1$.  If $B=1$,
again there is nothing to prove.  If $B=0$, then

```math
2q\leq3s+1<4s+2<3q.
\tag{8}
```

The right inequality gives $8s+4<6q$, while the left inequality gives
$6q\leq9s+2<9s+4$.  Thus the interval

```math
(8s+4,9s+4]
```

contains the multiple $6q$, so $A=1$.  Hence $A+B-C=0$ in the only
remaining case.  This proves the lemma. $\square$

For a prime $\ell$, Legendre's formula expresses the $\ell$-adic
valuation of the factorial ratio in (5) as

```math
\sum_{j\geq1}\delta_{\ell^j}(m).
\tag{9}
```

Every summand is nonnegative by Lemma 2.  The power of $4$ causes no
denominator, so (5) is an integer.  Together with Section 2 this proves
the first assertion of Theorem 1.

## 4. Half-binomial factorization

For an integer $c\geq2$, write

```math
B_c(N)=\binom{cN/2}{N}.
\tag{10}
```

Direct cancellation in (1) gives the exact factorization

```math
C(N)
=
\binom{9N}{4N}
\binom{5N}{2N}
\binom{2N}{N}^{2}
\left(B_9(N)B_7(N)B_5(N)\right)^{-1}.
\tag{11}
```

The previous
[Dixon--Legendre note](DixonLegendreHalfBinomialTowers.md#3-half-binomial-scaling)
proved that, for $p\geq5$, $N=pM$, and $e=v_p(N)$,

```math
\frac{B_c(N)}{B_c(M)}\equiv1\pmod {p^{3e}}.
\tag{12}
```

The same modulus holds for the adjacent quotient of every ordinary
binomial coefficient in (11) by the
Ljunggren--Jacobsthal--Kazandzidis congruence.  All adjacent quotients
are $p$-adic units, so taking products, powers, and inverses preserves
the congruence.  Therefore

```math
\frac{C(N)}{C(M)}\equiv1\pmod {p^{3e}}.
\tag{13}
```

For $N=np^r$, one has $e\geq r$.  Since $C(M)$ is an integer by
Sections 2--3, multiplying (13) by $C(M)$ proves (2). $\square$

## 5. Scope and priority boundary

This note proves both explicit conjectures on A364173:

- global integrality of the gamma quotient; and
- the complete adjacent $p^{3r}$ tower for every prime $p\geq5$.

It does not claim a binary or ternary tower.  The exact failures in (3)
show that the stated prime cutoff is necessary.

The even-index integrality input is the published Vasyunin--Bober
factorial-ratio classification.  The odd-index floor argument and the
half-binomial tower are elementary deductions.  A targeted search by
the A-number and exact factorial formula did not locate this combined
proof, but that negative search is not a priority certificate.

## 6. References

- [OEIS A364173](https://oeis.org/A364173), source of the two
  conjectures.
- [OEIS A295440](https://oeis.org/A295440), the even-index integral
  factorial ratio.
- [Bober, *Factorial ratios, hypergeometric series, and a family of
  step functions*](https://arxiv.org/abs/0709.1977), especially Table 2,
  entry 10.
- [Meštrović, *Wolstenholme's theorem: Its Generalizations and
  Extensions in the last hundred and fifty years
  (1862--2012)*](https://arxiv.org/abs/1111.3057), for the classical
  binomial scaling congruence.

## 7. Verification

Run:

```text
python verification/related/verify_a364173_integral_tower.py
```

The checker verifies the OEIS initial values, the odd-index gamma
simplification, the floor inequality for a large exact grid, global
integrality, the factorization (11), every adjacent factor transfer, the
full tower over a range of $n,p,r$, and the sharp small-prime failures.
