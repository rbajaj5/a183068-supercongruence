# The 110-record Bala proof campaign

**Snapshot date:** August 12, 2026

**Status:** complete record-level ledger; proof work remains in progress

The reproducible OEIS search used by this repository returned 110 distinct
records. That does **not** mean that it returned 110 distinct open
conjectures. A record may contain several claims, a claim may already follow
from a published theorem, and one parameterized theorem may settle several
records at once.

The machine-readable ledger is
[`data/bala_110_campaign.tsv`](../data/bala_110_campaign.tsv). It assigns
every record:

1. one of the five proof routes from the
   [Gaussian generalization map](BalaGaussianGeneralizationMap.md);
2. a conservative current status;
3. the evidence controlling that status; and
4. the next proof operation.

## Current disposition

| Route | Records | Proved here | Published source | Partial | No explicit open target | Open target | Queued |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| T: finite-sum transfer | 40 | 7 | 7 | 8 | 4 | 14 | 0 |
| C: coefficient/constant term | 37 | 10 | 6 | 4 | 2 | 15 | 0 |
| F: factorial/block product | 14 | 8 | 3 | 2 | 1 | 0 | 0 |
| M: modular or infinite product | 14 | 9 | 0 | 5 | 0 | 0 | 0 |
| D: derived or inherited | 5 | 0 | 0 | 5 | 0 | 0 | 0 |
| **Total** | **110** | **34** | **16** | **24** | **7** | **29** | **0** |

The thirty-four `proved-here` records are A002003, A005725, A008485, A008705,
A008793, A049505, A091527, A108625, A141057, A143007, A177316, A255672, A262732,
A246437, A270913, A270919, A270922, A270924, A275652, A275654, A281267, A288470, A333592,
A348410, A351857, A352373, A357509, A357510, A357568, A364173,
A364303, A364506, A370101, and A370102. The sixteen
`published-source` records are A002426, A002895, A005258, A082758, A103882,
A112029, A168597, A176335, A183204, A184423, A186420, A234839, A363864,
A363867, A363871, and A364509.
The twenty-four partial records are A003161, A003162, A008978, A023871,
A023873, A108628, A112028, A113424, A183069, A206622, A219562, A228960, A229452,
A283271, A350383,
A352655, A357506, A357512,
A357567, A357956, A357959, A361889, A361892, and A380290. A001850, A002897,
A005259, A005260, A006318, A036917, and A143583 are retained as
search-corpus records but
classified `no-explicit-open`: the live pages contain no Bala
supercongruence conjecture that remains to be proved.
The remaining twenty-nine records are `open-target`; their exact claims,
prime ranges, normalizations, and family consolidations are recorded in the
[remaining-open-target map](Bala110RemainingOpenTargets.md).

These labels refer only to the exact statements already matched. They do not
declare every comment on the corresponding OEIS page solved.

## Status definitions

- `proved-here`: a complete proof candidate in this repository matches the
  displayed OEIS conjecture.
- `published-source`: the live OEIS record or the repository's source audit
  identifies a published theorem implying the claim.
- `partial`: the repository proves a baseline, coefficientwise version, or
  subfamily, but a stronger statement on the record remains.
- `no-explicit-open`: the reproducible text search found the record, but a
  live open supercongruence attributable to Bala was not located.
- `open-target`: the live statement has been extracted and routed, but no
  complete proof, source closure, or counterexample is yet recorded.
- `queued`: the record is routed, but its exact conjecture still needs to be
  extracted and matched against the route theorem before proof work begins.

## August 12 reconciliation

This refresh makes evidence-backed promotions without treating a search
hit as a proof:

- A333592 moves from `partial` to `proved-here` because the later
  [prefix-Cartier theorem](MixedNegativeBinomialCubicTower.md) proves the
  named cubic tower and its full positive-parameter family;
- A364303 moves from `queued` to `proved-here` because the
  [Dixon--Legendre theorem](DixonLegendreHalfBinomialTowers.md) proves every
  stable row;
- A112029 moves from `queued` to `published-source` because its live OEIS
  comment cites Coster's Theorem 4 for the full shifted-index tower; and
- A183069, A361889, and A361892 move from `queued` to `partial` because the
  [ballot-power audit](CatalanBallotPowerSupercongruenceAudit.md) now copies
  their exact common conjecture, checks its sharp boundary, and isolates the
  unified proof target.

The follow-up [live-source boundary](Bala110LiveSourceBoundary.md) removes
nine further false starts. It source-closes A002895, A005258, and A183204;
records only the enhanced parts of A112028 and A219562 as open; and marks
A001850, A006318, A036917, and A143583 as search anchors with no live Bala
supercongruence target.

The final [open-target extraction](Bala110RemainingOpenTargets.md) reads and
routes every one of the other 35 live statements. Two of those records,
A003161 and A003162, subsequently reduce to the single existing
[ballot-power obstruction](CatalanBallotPowerSupercongruenceAudit.md),
leaving 33 independent `open-target` records. Consequently no record is
left `queued`: the remaining work is proof work rather than OEIS-page
extraction.

The first post-extraction proof unit closes both conjectures on A005725. The
[quadrinomial proof](QuadrinomialCoefficientOddPrimeTower.md) establishes
the full odd-prime quadratic tower by discard-and-rescale and proves the
separate prime-level cubic coefficient congruence by an exact rational
simplification, Wolstenholme's theorem, and alternating reciprocal-square
cancellation. This leaves 32 `open-target` records.

The second post-extraction proof unit rewrites A246437 as the
\((u,v,c)=(3,2,1)\) case of a new
[mixed-step coefficient theorem](MixedStepCoefficientQuadraticTower.md).
The linear coefficient constraint synchronizes the two summation indices
modulo \(p\), so every missed term has two valuation contributions and every
retained term transfers through two ordinary Jacobsthal quotients. This
leaves 31 `open-target` records.

The third unit recognizes A281267 as the one-color, \(d=1\), \(h_m=1\)
specialization of the existing
[colored Euler-product theorem](EulerProductGaussianTower.md). Its
Frobenius twist is trivial at \(Z=1\), so the theorem proves the exact
\(p^{2r}\) tower for every odd prime, including \(p=3\). This leaves 30
`open-target` records.

The next source reconciliation identifies the offset-one A108628 tower as
Straub's shifted multivariate Apéry coefficient theorem for \(p>5\).
Because the live page also includes \(p=5\) and four half-index vanishing
claims, the record moves to `partial`, not `published-source`. This leaves
29 `open-target` records and records the two residual obligations
explicitly.

## Proof order

The campaign does not use A-number order. It uses expected proof yield.

1. **T route:** look for a termwise discard-and-rescale proof. A288470 is
   the model: two carries close the integer tower and automatically produce
   a Gaussian Frobenius twist. The
   [Apéry odd-moment theorem](AperyOddMomentPrimeClassification.md)
   is the prime-boundary model: one local product expansion proves A357510
   and exactly classifies the exceptional primes for every higher odd
   moment, including the complete prime slice of A357512.
2. **F route:** rewrite the term as a multinomial or an integral Laurent
   product. A364506 is one model.  The odd-unit block theorem is the second:
   it closes A091527 and A262732 simultaneously by splitting a half-integral
   factorial product into its divisible factors and complete odd unit blocks.
   The Dixon--Legendre theorem is the third: it packages A275652 and A275654
   into one parameter family and reduces their fractional factorials to
   ordinary binomial transfer plus a half-binomial unit block.  A364173 is
   the fourth: the same transfer proves its tower, while a separate
   carry-interval lemma resolves the source page's integrality conjecture.
   A357509 is the fifth: a universal quadratic cancellation between
   adjacent binomial blocks proves the record's full two-parameter family.
   The route is now fully triaged.  The
   [coefficient-root theorem](CoefficientPowerGaussBaseline.md) proves the
   integrality assertions and the universal all-prime \(p^r\) baseline for
   A002897, A008978, and A113424; the latter two retain their stronger
   conjectural \(p^{3r}\) variable-power towers.
3. **C route:** first determine whether a direct finite-sum factorization is
   simpler than invoking Dwork or Cartier operators.  The
   [coefficient-framing theorem](CoefficientFramingCubicTower.md) proves six
   records by one elementary Cartier argument. In particular, it proves the
   general two-parameter conjecture on A352373. A
   [small exact counterexample](RationalFramingCounterexample.md) shows why
   Müller's broader framing theorem cannot be used as the source closure
   without repair. The
   [Straub prime-five packet](StraubPrimeFiveCoefficientPacket.md) supplies
   the omitted boundary prime in Straub's multivariate Apéry theorem and
   closes A108625, A143007, and A177316 after exact coefficient matching.
4. **M route:** take a p-adic logarithm and isolate the first moment that
   survives the product balance.  The
   [prime-coefficient packet](ModularProductPrimeCoefficientPacket.md)
   proves all displayed conjectures on A008485, A008705, A270913, and
   A270919 by one universal first-coefficient lemma.  The existing colored
   Euler-product theorem proves the complete A255672, A270922, and A270924
   towers and supplies rigorous quadratic baselines for four proposed cubic
   towers.  The
   [A229452 coefficient-root theorem](A229452CoefficientRootBaseline.md)
   also proves that record's all-\(m\) integrality conjecture, an
   exact Lagrange bridge, and an all-prime \(p^r\) baseline. The
   [A049505 paired-product theorem](A049505SymmetricPlanePartitionCongruences.md)
   proves all three symmetric-plane-partition congruences through the
   stronger evaluation
   $a(p^r)\equiv2^{(p^r+1)/2}\pmod {p^3}$ for every odd prime and $r\ge1$.
   Finally, the
   [A008793 cube-product theorem](A008793CubePlanePartitionTower.md)
   proves the full all-prime $p^{4r}$ conjecture by exact product splitting,
   reduced-residue blocks, and a separate binary parity argument. No route-M
   record remains queued.
5. **D route:** identify the parent sequence and prove that the claimed
   congruence is inherited before treating it as an independent problem.
   This route is now fully triaged.  The
   [Apéry defect packet](AperyRankOneDefectPacket.md) proves that its five
   records are equivalent to only three linear defect relations, and that
   the two nonlinear companion conjectures introduce no new arithmetic
   direction.  The three defect relations themselves remain open.

## Promotion rule

A row moves out of `queued` only when the exact source statement has been
copied into a proof note and one of the following is present:

- a complete proof;
- a precise reduction to a published theorem with parameter matching;
- a counterexample; or
- a smaller named obstruction that is explicitly marked unresolved.

Finite testing alone does not change the status to `proved-here`.

## Verification

Run

```text
python verification/related/verify_bala_110_campaign.py
```

The checker verifies the 110 unique A-numbers, the route totals
$40+37+14+14+5$, the five status totals, and the presence of a nonempty
next action for every record.
