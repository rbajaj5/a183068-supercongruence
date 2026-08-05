# Transfer ledger for OpenAI's ten Lean-certified advances

**Status date:** August 5, 2026

**Status:** source and mechanism ledger. The ten results announced by OpenAI
on August 1, 2026 are accepted here as external theorems with public Lean
certificates. This note records exactly what each result contributes to the
supercongruence program. It does not relabel analogies as arithmetic
consequences.

## 1. Source policy

The public source supplies three layers:

1. a 249-page manuscript containing all ten arguments;
2. a public Lean 4 repository with a named endpoint for every result; and
3. a formalization manifest recording zero `sorry` declarations and only
   `propext`, `Classical.choice`, and `Quot.sound` at the main endpoints.

The source organization expressly takes responsibility for correctness. This
repository therefore treats the ten results as available external theorems,
while retaining the ordinary distinction between accepting a source theorem
and proving it locally.

The artifact inspected for this ledger was `openai/ten-proofs` commit
`94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6`. Pinning the commit prevents a
later repository update from silently changing the object cited here.

The manifest's main declarations are:

- `PackingBounds.sharpFullCohnElkiesManuscriptConclusions`;
- `MetricCodes.Johnson.binaryRate_lt_mrrw` and
  `MetricCodes.Spherical.HigherHierarchy.strict_hierarchy`;
- `SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group`;
- `ConnesRigidity.exists_infinite_pairwise_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors`;
- `PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound`;
- `QuantumParallelRepetition.distributionUniformExponential`;
- `GapCVP.Comparator.gapCVP400IsNPHard`;
- `Ehrhart.Volume.ehrhart_volume_inequality_for_sets`;
- `ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit`;
- `CompactnessConjecture.quantitativeCompactnessCounterexample` and
  `TwoDegenerateGraphs.twoDegenerateExtremalCounterexample`.

## 2. Exact relevance matrix

| Result | Lean certificate | Use in this repository | Classification |
| --- | --- | --- | --- |
| High-dimensional sphere packing | `SpherePacking.lean` | Fourier-positive dual certificates suggest how to separate a proposed congruence witness from the search that found it. No $p$-adic exponent follows. | Certificate architecture |
| Binary and spherical codes | `MetricCodes.lean` | Supplies a model for ranking finite fingerprints by distance and rate; relevant to Walsh/hypercube checkers, not to proof of an arithmetic tower. | Experimental design |
| Nonsofic groups | `NonSoficGroup.lean` | The median-normalized expander argument yields an exact conservation upgrade from one-sided permutation control to $L^1$ control. | Reusable proof-search lemma |
| Connes rigidity counterexample | `ConnesRigidity.lean` | Warns that equality of a powerful completed invariant need not identify the original object. In the arithmetic ledger, matching zeta factors or defect profiles must not be promoted to equality without injectivity. | Invariant boundary |
| Permanent circuit lower bounds | `Permanent.lean` | Motivates recording expression size and denominator growth separately from correctness. A short factorial-ratio identity can be mathematically decisive even when naive expansion is enormous. | Complexity accounting |
| Quantum parallel repetition | `QuantumParallelRepetition.lean` | Provides the correct model for audit amplification: independent or theorem-controlled repetitions can reduce soundness error exponentially; correlated LLM reviews cannot be multiplied as if independent. | Review protocol |
| Closest vector hardness | `GapCVP.lean` | Separates efficient verification from hard witness search. Exact congruence checkers certify candidates but do not imply that finding a proof or optimal witness is easy. | Search/verification boundary |
| Ehrhart volume theorem | `EhrhartVolumeInequality.lean` | Gives a direct arithmetic corollary: a sharp finite cutoff for primes that can create full-rank degeneration in eligible Newton polytopes. | Direct arithmetic consequence |
| Multicolor Ramsey lower bound | `MulticolorTriangleRamsey.lean` | Reinforces the repository's untrusted-search/trusted-checker pattern: a large combinatorial witness should be reduced to a small exact predicate. | Certificate architecture |
| Compactness and degeneracy counterexamples | `CompactnessAndDegeneracy.lean` | Supplies a concrete warning that every bounded or finite-looking regime need not assemble into the expected global theorem. Uniformity is an obligation, not an inference from many finite checks. | Local-to-global boundary |

Only the Ehrhart row currently changes an arithmetic theorem statement. The
nonsofic row contributes a precise lemma used to improve proof search. The
other eight rows improve certification, ranking, or logical hygiene.

## 3. Conservation upgrade extracted from the nonsofic proof

### Lemma 1 (permutation conservation)

Let $X$ be finite, let $\tau$ be a permutation of $X$, and let
$f:X\to\mathbb R$. Put

```math
\Delta(x)=f(\tau x)-f(x).
```

Then

```math
\sum_{x\in X}\Delta(x)=0
```

and consequently

```math
\sum_{x\in X}|\Delta(x)|
=2\sum_{x\in X}\max(\Delta(x),0)
=2\sum_{x\in X}\max(-\Delta(x),0).
\tag{1}
```

### Proof

Because $\tau$ is a bijection,

```math
\sum_{x\in X}f(\tau x)=\sum_{x\in X}f(x).
```

Thus the signed sum of $\Delta$ is zero. Its total positive and total negative
parts are equal, and their sum is the $L^1$ norm, proving (1). $\square$

The nonsofic construction combines this elementary identity with expansion
and a coarea estimate. A one-sided component-size estimate controls the
negative part of $\Delta$; (1) controls the positive part; expansion then
forces concentration and permits an almost-injective component matching.

For congruence searches, the analogous instruction is concrete:

> Before estimating every local error independently, look for an exact
> permutation, involution, residue-block product, or character sum that makes
> the signed aggregate error vanish.

This can recover a missing factor that termwise absolute-value estimates
discard. It is a heuristic until the relevant arithmetic conservation law is
written explicitly.

## 4. Direct arithmetic transfer from the Ehrhart theorem

The accepted sharp Ehrhart theorem states that a $d$-dimensional convex body
with barycenter zero and no other interior lattice point has volume at most

```math
\frac{(d+1)^d}{d!}.
```

The repository's
[Ehrhart--Newton prime cutoff](EhrhartNewtonPrimeCutoff.md) proves the exact
corollary: any determinant of $d+1$ lattice points in such a body is either
zero or has absolute value at most $(d+1)^d$. Hence every prime
$p>(d+1)^d$ preserves full-dimensional affine independence after reduction.

This turns one potentially infinite exceptional-prime search into a finite
one. It controls Newton-support rank, not a supercongruence exponent, and it
does not apply to a polytope failing the interior-point hypothesis.

## 5. Audit amplification without fake independence

Suppose one exact randomized checker has false-acceptance probability at most
$\varepsilon$, and $t$ repetitions are independent conditional on a fixed
false claim. Then accepting only when all repetitions accept has probability
at most $\varepsilon^t$.

This elementary product law is the part of parallel repetition that the
repository may use without importing quantum-game machinery. It does **not**
justify multiplying confidence scores from Fable, Claude, Kimi, or ChatGPT:
their training data, prompts, and characteristic proof errors are correlated.
Exact deterministic checkers, Lean kernels, and genuinely independent random
seeds should be recorded separately.

## 6. Consequences for ranking

The ten advances do not receive ten new entries in `RESULT_INDEX.md`, because
this repository did not prove them. Their effects are instead:

- `EHRHART-CUTOFF` moves from conditional to a completed deduction from an
  accepted external theorem;
- the nonsofic boundary note moves from quarantine to accepted provenance and
  gains Lemma 1 as its transferable mechanism;
- checker-heavy results must state whether repeated tests are deterministic,
  independently randomized, or correlated reviews;
- invariant matches and finite-range success cannot by themselves raise proof
  maturity.

## 7. Sources

- OpenAI, [*Ten advances in mathematics and theoretical computer
  science*](https://openai.com/index/ten-advances-in-mathematics/), August 1,
  2026.
- OpenAI, [*Ten Advances in Mathematics and Theoretical Computer Science*](https://cdn.openai.com/pdf/ten-proofs-oai.pdf),
  complete manuscript.
- OpenAI, [`ten-proofs`](https://github.com/openai/ten-proofs), public Lean 4
  certificates and `formalization.yaml` audit manifest.
- A. Thom, [MathOverflow explanation of the nonsofic component-matching
  argument](https://mathoverflow.net/a/513885), August 2026.
