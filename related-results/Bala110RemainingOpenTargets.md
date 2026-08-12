# The 23 remaining open targets in the Bala 110-record census

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
partial ledger. This file now lists the 23 records that remain fully open.

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

### Adjacent-binomial row families

- [A198060](https://oeis.org/A198060) states Gauss congruences for every
  row, a separate even-row congruence at `p^r-1`, and a cubic odd-row
  tower. The live odd-row formula contains `n*p*(r-1)` where the surrounding
  pattern indicates that `n*p^(r-1)` may have been intended. That ambiguity
  must be resolved before proof.
- [A198256](https://oeis.org/A198256), with offset 1, asks for a cubic tower
  for `p >= 5`.
- [A198258](https://oeis.org/A198258), also with offset 1, asks for a cubic
  tower for `p >= 3`; the ternary boundary is therefore part of the claim.

### Isolated finite-sum boundaries

- [A244973](https://oeis.org/A244973) asks that
  `(a(pn)-a(n))/(pn)^3` be `p`-adically integral for `p > 5`. On writing
  `n=mp^(r-1)`, this is a cubic adjacent-level valuation statement.
- [A362676](https://oeis.org/A362676) asks for a cubic tower for the finite
  sum

  ```math
  \sum_{k=0}^{N}4^{N-k}\binom Nk\binom{N-1}{k}\binom{2k}{k}
  ```

  at `p >= 5`.

### Integer-parameter Franel companions

[A363985](https://oeis.org/A363985) proposes the same cubic tower for every
integer `m` in both families

```math
u_m(N)=\sum_{k=0}^{N}(-4)^{N-k}
\binom Nk\binom{mN+k}{k}\binom{2k}{k},
```

```math
v_m(N)=\sum_{k=0}^{N}(-4)^{N-k}
\binom Nk\binom{mN+2k}{2k}\binom{2k}{k}.
```

The target is family-wide for `p >= 5`, including negative `m`; it is not
closed by checking the named specialization alone.

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

### Algebraic quadratic towers

- [A245926](https://oeis.org/A245926) first needs its conjectural Laurent
  representation proved; conditional on that representation, the page asks
  for a quadratic tower at `p >= 5`.

### Reversion coefficient family

Let `A(x)` be the offset-zero generating series of
[A263843](https://oeis.org/A263843). The record asks for the cubic tower of

```math
[x^{rn}]A(x)^{sn}
```

for positive `r`, integral `s`, and every `p >= 3`. This is a family claim,
not only the named case `[x^n]A(x)^n`.

### Uniform row theorem

[A331562](https://oeis.org/A331562) asks that every fixed row satisfy the
cubic tower for `p >= 5`. Rows 2, 3, and 4 are cited as known examples.
The remaining target is one uniform row theorem, not a sequence of isolated
row computations.

### Taylor-truncation packets

[A333090](https://oeis.org/A333090),
[A333091](https://oeis.org/A333091), and
[A333092](https://oeis.org/A333092) are the cases `m=1,2,3` of the family

```math
T_n\bigl(S(x)^{mn}\bigr)\big|_{x=1},
```

where `S(x)` is the large-Schroder generating series and `T_n` truncates at
degree `n`. The conjecture is a cubic tower for every integral `m` and
`p >= 5`.

[A333093](https://oeis.org/A333093),
[A333095](https://oeis.org/A333095),
[A333096](https://oeis.org/A333096), and
[A333097](https://oeis.org/A333097) state the parallel family with the
Catalan generating series. These seven records therefore represent two
parameterized proof targets.

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
- 23 records are explicit `open-target` entries;
- repeated records have been consolidated into family-sized proof units;
  and
- ambiguous or conditional inputs are identified before theorem work.

This does **not** assert that all 23 targets are true. Their next legitimate
status change requires a proof, an exact published-source reduction, or a
counterexample.
