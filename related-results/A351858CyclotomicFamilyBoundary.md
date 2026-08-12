# An exact boundary for the A351858 cyclotomic family

**Status:** complete elementary counterexample to the all-parameter
conjecture; the named $k=2$ tower remains open.

**Source boundary:** [OEIS A351858](https://oeis.org/A351858) defines the
named $k=2$ sequence and conjectures the same cubic tower for every $k\geq2$,
then proposes a still broader coefficient-slope family.  The calculation
below refutes both broader assertions.  It does not refute the named
A351858 sequence.

## 1. The proposed family

For $k\geq1$, write

```math
G_k(x)=
\frac{(1+x+\cdots+x^k)^{k+1}}
     {(1+x+\cdots+x^{k-1})^k}
=\frac{(1-x^{k+1})^{k+1}}
       {(1-x)(1-x^k)^k}
\tag{1}
```

and

```math
u_k(N)=[x^N]G_k(x)^N.
\tag{2}
```

The page proposes

```math
u_k(np^r)\equiv u_k(np^{r-1})\pmod {p^{3r}}
\tag{3}
```

for all $k\geq2$, primes $p\geq5$, and positive $n,r$.

## 2. The first infinite counterexample family

Take any prime $p\geq5$ and set $k=p-1$.  Equation (1) gives

```math
G_{p-1}(x)^p=
\frac{(1-x^p)^{p^2}}
{(1-x)^p(1-x^{p-1})^{p(p-1)}}.
\tag{4}
```

Only degrees $0$ and $p-1$ from the final factor and degrees $0$ and $p$
from the numerator can contribute to $[x^p]$.  Hence

```math
u_{p-1}(p)
=\binom{2p-1}{p}+p^2(p-1)-p^2
=\binom{2p-1}{p}+p^2(p-2).
\tag{5}
```

Also $u_{p-1}(1)=[x]G_{p-1}(x)=1$.  Wolstenholme's congruence gives

```math
\binom{2p-1}{p}\equiv1\pmod {p^3}.
\tag{6}
```

Combining (5)--(6),

```math
u_{p-1}(p)-u_{p-1}(1)
\equiv p^2(p-2)\not\equiv0\pmod {p^3}.
\tag{7}
```

In fact the valuation is exactly two.

The smallest instance is

```math
u_4(5)-u_4(1)=201-1=200=2^3\cdot5^2.
\tag{8}
```

## 3. A second infinite counterexample family

Set $k=p$.  Now

```math
G_p(x)^p=
\frac{(1-x^{p+1})^{p(p+1)}}
{(1-x)^p(1-x^p)^{p^2}}.
\tag{9}
```

The numerator cannot affect degree $p$.  The two denominator contributions
give

```math
u_p(p)=\binom{2p-1}{p}+p^2,
\qquad
u_p(1)=1.
\tag{10}
```

Therefore

```math
u_p(p)-u_p(1)\equiv p^2\not\equiv0\pmod {p^3},
\tag{11}
```

again with exact valuation two.  At $p=5$ this is

```math
u_5(5)-u_5(1)=151-1=150=2\cdot3\cdot5^2.
\tag{12}
```

## 4. What survives

The obstruction occurs precisely when the prime divides one of the adjacent
cyclotomic step sizes $k$ or $k+1$.  In the Frobenius-logarithm language,
the offending reduced-log support then lands on the $p$-sublattice, so the
linear defect no longer vanishes.  This explains why a theorem proved only
under $p\nmid k(k+1)$ would not settle the page's uniform claim.

The named sequence A351858 has fixed $k=2$ and asks only for $p\geq5$, so
neither $p\mid k$ nor $p\mid k+1$ can occur.  Its cubic tower remains a
coherent separate target.  The exact result here is therefore:

- the universal all-$k$ assertion is false;
- the broader $u_k(c,s;N)=[x^{cN}]G_k(x)^{sN}$ assertion is also false,
  because it contains $c=s=n=r=1$; and
- the named $k=2$ conjecture is not decided by these counterexamples.

## 5. Verification

Run

```text
python verification/related/verify_a351858_cyclotomic_boundary.py
```

The exact checker verifies the published A351858 values, the cyclotomic
factorization, both coefficient formulas for every prime through $97$, the
exact valuation-two failures, and direct truncated-series coefficients.
