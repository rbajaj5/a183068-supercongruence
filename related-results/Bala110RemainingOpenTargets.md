# No wholly untreated targets remain in the Bala 110-record census

**Extraction date:** August 12, 2026  
**Status:** completion map; unresolved partial claims below are not declared proved

This note finishes the record-reading stage of the 110-record campaign.
Every former `queued` entry now has a live conjecture or family attached to
it. The status `open-target` meant:

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
[A351858 theorem and cyclotomic boundary](A351858CyclotomicFamilyBoundary.md)
refutes that record's all-parameter claim and proves its surviving named
$k=2$ cubic tower by a six-residue Cartier estimate. The
[A263843 reversion theorem](A263843ReversionCoefficientReduction.md) first
moved that record to `partial` and now closes it completely, including the
exceptional prime (3), by matching the leading quadratic and cubic
Cartier defects.  The
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
both to `partial`. The later
[balanced-matrix theorem](BalancedMatrixCoefficientQuadraticTower.md)
proves A124435. The
[A244973 Frobenius reduction](A244973QuadraticFrobeniusReduction.md)
then isolates Sun's remaining conjecture as one exact linear--quadratic
Cartier cancellation and moves that record to `partial`. The
[A331562 rational-diagonal reduction](A331562UniformRationalDiagonal.md)
also replaces the row-by-row search by one determinant-ratio family and one
uniform continuant Frobenius estimate. The
[A079489 Lagrange-kernel reduction](A079489LagrangeKernelReduction.md)
places both its direct and reverted coefficient families in one normalized
signed-binomial kernel. The
[exponential-coefficient reduction](ExponentialCoefficientCartierReduction.md)
does the same for A060941, A362722, and A362733 through one exact Cartier
defect. Finally, the
[A376 companion reduction](A376AperyCompanionReduction.md) proves the
A376458 prime-level `p^5` assertion, refutes A376466's shifted tower, and
places both surviving ordinary towers in one exact pairing framework. No
record is now wholly untreated.

## 1. Finite-sum transfer targets

### Recently reduced coefficient and reversion family

Let `A(x)` be the algebraic series on
[A079489](https://oeis.org/A079489), and let
`B(x)=x^{-1} rev(xA(x))`. For integral `r` and positive `s`, the record asks
for the cubic tower for both

```math
[x^{sn}]A(x)^{rn}
\quad\hbox{and}\quad
[x^{sn}]B(x)^{rn}
```

at every `p >= 5`. The exact coefficient representation, singular slopes,
and common normalized kernel are now recorded in the
[A079489 Lagrange-kernel reduction](A079489LagrangeKernelReduction.md), so
this record is no longer counted among the fully open targets.

### Paired Apéry companions (reduced and partly resolved)

- [A376458](https://oeis.org/A376458) asks for an ordinary cubic tower,
  plus `p^5` at the first pure-prime level and `p^(3r+3)` later.
- [A376466](https://oeis.org/A376466) asks for two cubic towers, at indices
  `np^r` and `np^r-1`, mirroring the paired property of the classical
  Apéry numbers.

Both use rows of A108625 in their summands. The paired claims must be proved
from the displayed sums; analogy with the Apéry sequences is evidence, not
inheritance. The [companion note](A376AperyCompanionReduction.md) now
collapses A376458 to one sum, proves its full ordinary cubic tower, and
proves its `p^5` prime boundary. It also
gives the exact counterexample
`A376466(9)-A376466(1) == 3 (mod 5)`, so that record's all-`n` shifted
conjecture is false. The ordinary cubic tower for A376466 and the higher
A376458 bonus remain open.

## 2. Recently reduced coefficient and constant-term targets

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
- no record remains `open-target`;
- repeated records have been consolidated into family-sized proof units;
  and
- ambiguous or conditional inputs are identified before theorem work.

This does **not** assert that all remaining targets are true. Their next legitimate
status change requires a proof, an exact published-source reduction, or a
counterexample.
