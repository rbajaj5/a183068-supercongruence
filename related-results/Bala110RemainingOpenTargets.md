# The 9 remaining open targets in the Bala 110-record census

**Extraction date:** August 12, 2026  
**Status:** complete live-target map; the claims below are not declared proved

This note finishes the record-reading stage of the 110-record campaign.
Every former `queued` entry now has a live conjecture or family attached to
it. The new status `open-target` means:

- the live claim has been identified;
- its normalization and prime range have been recorded here;
- no complete proof or exact published-source closure is currently recorded;
  and
- the next operation is mathematical proof, not database extraction.

The original 26 records consolidate to substantially fewer proof families. Repeated
entries are retained because the campaign denominator is a record count, but
the proposed proof units below are family-sized.

The [A132303 trinomial-cube theorem](A132303TrinomialCubeTower.md) and the
[A156554 Legendre coefficient theorem](A156554LegendreCoefficientTower.md)
have closed two targets, while the
[A351858 cyclotomic boundary](A351858CyclotomicFamilyBoundary.md) refutes
that record's all-parameter claim and moves its surviving named case to the
partial ledger. The
[A263843 reversion reduction](A263843ReversionCoefficientReduction.md) has
also moved that record to `partial`.  The
[A245926 algebraic coefficient theorem](A245926AlgebraicCoefficientTower.md)
proves both that record's conjectural coefficient representation and its
quadratic tower. The
[Taylor-truncation reduction](TaylorTruncationCoefficientReduction.md)
has consolidated A333090--A333097 into two exact coefficient families and
moved those seven records to `partial`.  The
[adjacent-binomial meander theorem](MeanderAdjacentBinomialTowers.md) then
proved the three intended A198060 families and closed A198256 and A198258,
including the exceptional ternary sextic case. The subsequent
[Franel-companion reduction](FranelCompanionConstantTermReduction.md)
places A362676 and A363985 in one explicit constant-term family and moves
both to `partial`. This file now lists the 9 records that remain fully open.

## 1. Finite-sum transfer targets

### Coefficient and reversion family

Let `A(x)` be the algebraic series on
[A079489](https://oeis.org/A079489), and let
`B(x)=x^{-1} rev(xA(x))`. For integral `r` and positive `s`, the record asks
for the cubic tower for both

```math
[x^{sn}]A(x)^{rn}
\quad\hbox{and}\quad
[x^{sn}]B(x)^{rn}
```

at every `p >= 5`. The two statements require a coefficient representation
that survives reversion; a formal similarity of the series is not enough.

### Quadratic tower

- [A124435](https://oeis.org/A124435) asks for
  `a(np^r) = a(np^(r-1)) mod p^(2r)` for `p >= 5`. The live rational
  diagonal is `1/(1-x-y-z+xyz)`, but a rational diagonal alone does not
  supply the second power.

### Isolated finite-sum boundary

- [A244973](https://oeis.org/A244973) asks that
  `(a(pn)-a(n))/(pn)^3` be `p`-adically integral for `p > 5`. On writing
  `n=mp^(r-1)`, this is a cubic adjacent-level valuation statement.

### Paired Apéry companions

- [A376458](https://oeis.org/A376458) asks for an ordinary cubic tower,
  plus `p^5` at the first pure-prime level and `p^(3r+3)` later.
- [A376466](https://oeis.org/A376466) asks for two cubic towers, at indices
  `np^r` and `np^r-1`, mirroring the paired property of the classical
  Apéry numbers.

Both use rows of A108625 in their summands. The paired claims must be proved
from the displayed sums; analogy with the Apéry sequences is evidence, not
inheritance.

## 2. Coefficient and constant-term targets

### Duchon algebraic-series packet

On [A060941](https://oeis.org/A060941), if `A(x)` denotes the page's
algebraic generating series, the proposed family is

```math
[x^{sn}]A(x)^{rn}
```

for integral `r`, positive `s`, and `p >= 7`, with modulus `p^(3k)` at the
`k`-th adjacent level. A further conjecture applies the operation

```math
F\longmapsto
\exp\left(\sum_{j\ge1} f_j x^j/j\right)
```

iteratively and asks that the resulting coefficient sequences retain the
same tower. Closure under this nonlinear operation is a separate theorem.

### Uniform row theorem

[A331562](https://oeis.org/A331562) asks that every fixed row satisfy the
cubic tower for `p >= 5`. Rows 2, 3, and 4 are cited as known examples.
The remaining target is one uniform row theorem, not a sequence of isolated
row computations.

### Exponential coefficient pair

- [A362722](https://oeis.org/A362722) asks for modulus `p^(2r)` at general
  adjacent levels and an extra power, `p^(2r+1)`, on the pure-prime line.
- [A362733](https://oeis.org/A362733) asks for a cubic tower for every
  `p >= 3`.

Both are defined through exponentials of earlier sequence data. The known
Gauss congruence of the source coefficients does not by itself give the
claimed higher exponent.

## 3. What completion means here

The database stage is now closed:

- 110 records have routes and statuses;
- none remains `queued` for lack of an extracted statement;
- 9 records are explicit `open-target` entries;
- repeated records have been consolidated into family-sized proof units;
  and
- ambiguous or conditional inputs are identified before theorem work.

This does **not** assert that all remaining targets are true. Their next legitimate
status change requires a proof, an exact published-source reduction, or a
counterexample.
