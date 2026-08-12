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
| T: finite-sum transfer | 40 | 13 | 8 | 12 | 4 | 3 | 0 |
| C: coefficient/constant term | 37 | 12 | 6 | 14 | 2 | 3 | 0 |
| F: factorial/block product | 14 | 8 | 3 | 2 | 1 | 0 | 0 |
| M: modular or infinite product | 14 | 9 | 0 | 5 | 0 | 0 | 0 |
| D: derived or inherited | 5 | 0 | 0 | 5 | 0 | 0 | 0 |
| **Total** | **110** | **42** | **17** | **38** | **7** | **6** | **0** |

The forty-two `proved-here` records are A002003, A005725, A008485, A008705,
A008793, A049505, A091527, A108625, A124435, A132303, A141057, A143007, A156554, A177316, A198060, A198256, A198258, A245926, A246437,
A255672, A260667, A262732, A270913, A270919, A270922, A270924, A275652,
A275654, A281267, A288470, A333592,
A348410, A351857, A352373, A357509, A357510, A357568, A364173,
A364303, A364506, A370101, and A370102. The seventeen
`published-source` records are A002426, A002895, A005258, A082758, A103882,
A112029, A168597, A176335, A183204, A184423, A186420, A208675, A234839,
A363864, A363867, A363871, and A364509.
The thirty-eight partial records are A003161, A003162, A008978, A023871,
A023873, A108628, A112028, A113424, A183069, A206622, A212334, A219562,
A228960, A229452, A244973, A263843, A283271, A331562, A333090, A333091, A333092, A333093,
A333095, A333096, A333097, A350383, A351858, A352655, A357506, A357512,
A357567, A357956, A357959, A361889, A361892, A362676, A363985, and A380290.
A001850, A002897,
A005259, A005260, A006318, A036917, and A143583 are retained as
search-corpus records but
classified `no-explicit-open`: the live pages contain no Bala
supercongruence conjecture that remains to be proved.
The remaining six records are `open-target`; their exact claims,
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

Two further live-page checks remove the word-count sums from the wholly open
queue. A208675 is exactly Straub's coefficient `B(n,n-1,n-1)`, so its stated
cubic tower is `published-source`. A212334 is a `1/12`-weighted combination
of the ordinary and shifted A005259 sequences; because `12` is a unit for
every `p >= 5`, its ordinary cubic tower is source-closed. Its stronger
`p^5` and `p^(3r+3)` pure-prime congruences remain open, so the record is
`partial`. This leaves 27 `open-target` records.

The next proof unit closes the isolated A260667 prime boundary. Expanding
its inner binomial kernel at `x=p-1` reduces the claimed cubic congruence to
one weighted linear harmonic sum modulo `p^2` and one weighted quadratic
harmonic sum modulo `p`. Both sums have elementary closed evaluations, and
their residues cancel exactly. This leaves 26 `open-target` records.

The following proof unit closes A132303.  The sum of cubes of trinomial
coefficients is the constant term of
`(x*y)^(-2)*(1+x+x^2)*(1+y+y^2)*(1+xy+x^2*y^2)`, raised to the index.
Its reduced cyclotomic Frobenius logarithm has no support on the
`p`-sublattice for `p >= 5`, so the linear defect vanishes exactly and every
higher exponential term carries `p^(2r)`.  This proves the conjectured sharp
quadratic tower and leaves 25 `open-target` records.

The next proof unit closes the full A156554 Legendre coefficient family.
The standard binomial formula for
`P_(sN)((1+x)/(1-x))` introduces one auxiliary constant-term variable.
Its reduced Frobenius logarithm is supported on three primitive, pairwise
unimodular rays.  Mixed quadratic products therefore miss the
`p`-sublattice, while each same-ray square is controlled by the existing
reciprocal-square Cartier lemma.  Formal integration by parts supplies the
third power of `p`.  This proves the family for arbitrary integral framing
parameters and leaves 24 `open-target` records.

The following boundary unit resolves the overbroad part of A351858.  For
every prime `p >= 5`, the proposed all-`k` family fails at both `k=p-1` and
`k=p`: direct coefficient extraction gives differences congruent to
`p^2(p-2)` and `p^2` modulo `p^3`, respectively.  The named `k=2` tower is
not touched by this ramified-step obstruction and remains open, so A351858
moves to `partial`.  This leaves 23 `open-target` records.

The next reduction treats A263843.  Lagrange--Bürmann inversion turns its
reversion family exactly into the coefficient-framing family with parameters
`(alpha,beta)=(3(c+s),-(c+s))`, up to the constant `s/(c+s)`.  Tracking the
factor `c+s` inside the reduced logarithm removes every denominator-prime
loss.  This proves the full family for `p>=5` and for `p=3` whenever
`3|(c+s)`; the singular line `c+s=0` is an explicit parity sequence.  Only
the ternary unit-slope boundary remains, so A263843 moves to `partial` and
22 records remain `open-target`.

The following proof unit closes A245926.  Lagrange--Bürmann inversion and
the substitution `u=(1+y)/(1-y)`, `v=u^2` reduce the conjectural coefficient
representation to the quadratic equation
`3*z*v^2+(z-1)*v+1=0`; eliminating `v` recovers exactly the algebraic
generating function on the OEIS page.  The resulting kernel factors as
`(1-x^3)*(1-x^2)^2/(1-x)^5`.  For `p>=5` its reduced Frobenius logarithm
has no exponent on the `p`-sublattice, so the linear defect vanishes and
all remaining exponential terms carry `p^(2r)`.  This proves both the
representation and the quadratic tower, leaving 21 `open-target` records.

The next reduction consolidates the seven Catalan and large-Schröder
Taylor-truncation records. Residue substitution turns every integral power
parameter into one of two explicit rational-prefactor coefficient families.
For Catalan, the prefactor has the exact Cartier fixed-point
`C_p(Q)=Q` for `p>=5`; for Schröder, the prefactor denominator splits over
the Gaussian integers. The new note states the two remaining Catalan
constant-term estimates exactly and verifies them on a finite grid. Because
those estimates are not yet proved, all seven records move to `partial`,
leaving 14 `open-target` records.

The adjacent-binomial unit closes three more records at once.  Writing the
row index as `d-1`, reflection turns every offset row into a symmetric
homogeneous polynomial in two adjacent binomial coefficients.  For even
`d` it has a double factor `L+R`; its residual value on `L=-R` is `d/4`.
Jacobsthal scaling closes the divisible shells and reciprocal-square blocks
close the unit shell.  This proves the intended three A198060 conjectures,
the A198256 quartic identity and cubic tower, and the A198258 cubic tower.
The factor `d/4` supplies exactly the missing ternary power when `3|d`,
explaining why A198258 includes `p=3` while A198256 does not.  The printed
`n*p*(r-1)-1` in A198060 still needs the evident editorial correction to
`n*p^(r-1)-1`.  Eleven records remain `open-target`.

The next reduction places A362676 and A363985 in one exact two-variable
[Franel-companion constant-term family](FranelCompanionConstantTermReduction.md).
It identifies A362676 with the `m=-1` member (up to a parity sign), recovers
the central-binomial and Franel boundary cases, and passes 1,088 exact cubic
tower checks across both kernels.  Straub's multiblock theorem proves the
Franel specialization through a different representation, but does not
prove this full integer-parameter deformation; the missing statement is now
one explicit cubic Cartier contraction.  Both records therefore move to
`partial`, leaving nine records `open-target`.

The balanced-matrix unit then closes A124435.  A general coefficientwise
theorem proves a `p^(2r)` Frobenius tower for products of linear forms with
equal row and column margins: every missed residue matrix forces carries in
at least two rows.  An Eisenstein `3` by `3` matrix realizes the A124435
rational diagonal; its entrywise Frobenius is either the matrix itself or
its transpose, and balanced coefficients are transpose-invariant.  This
proves the exact OEIS tower and leaves eight records `open-target`.

The A244973 unit then identifies Sun's exact residual conjecture. Peter
Bala's signed-multinomial formula becomes a two-variable Laurent period and,
after normalizing at one hexagonal vertex, a diagonal coefficient of
`((1+u+uv)(1-v+uv))^N`. A reduced-logarithm expansion proves that every
term of Frobenius degree at least three already has the target depth. The
entire conjecture is therefore equivalent to one displayed cancellation
between the linear and quadratic Frobenius terms. Exact arithmetic shows
that these terms are individually one power short at `p=7,M=7`, while their
sum has the required valuation. A244973 moves to `partial`, leaving seven
records `open-target`.

The A331562 unit then gives every fixed row one uniform multivariate
rational model. If `A_d` is the path-with-loops adjacency matrix and `J_d`
is the all-one matrix, the complete weighted word language is exactly
`det(I-(A_d-J_d)X)/det(I-A_dX)`. The denominator is a second-order
continuant, and the conjectured cubic tower becomes one explicit diagonal
estimate for its finite Frobenius numerator. The determinant identity and
the first untreated rows pass independent exact checks. A331562 moves to
`partial`, leaving six records `open-target`.

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
   [two-variable Legendre extension](A156554LegendreCoefficientTower.md)
   uses three pairwise-unimodular rays to prove the full A156554 family. A
   [cyclotomic-family boundary](A351858CyclotomicFamilyBoundary.md) shows
   that A351858's universal parameter claim fails whenever `k=p-1` or
   `k=p`, while preserving its named `k=2` problem as a separate target. A
   [reversion reduction](A263843ReversionCoefficientReduction.md) sends the
   A263843 family back to coefficient framing and isolates one ternary
   boundary instead of leaving the entire parameter family open. A
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
