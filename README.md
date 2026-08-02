# A183068 and a public supercongruence research program

This repository began with a proposed proof of Peter Bala's
[OEIS A183068](https://oeis.org/A183068) supercongruence and has grown into a
public portfolio of related \(p\)-adic, Gaussian-integer, cyclotomic, and
finite-field results.

The repository is a research record, not a journal. Every claim has a proof
status, a source status, and—where appropriate—an exact checker. Machine
assistance and finite verification are disclosed and are not called peer
review.

## Start here

| If you want to… | Read | Status |
| --- | --- | --- |
| Understand the original theorem | [Friendly proof](PROOF.md) | Machine-audited draft; specialist review pending |
| See the response to Peter Bala's suggested proof routes | **[BALA_VERSION.md](BALA_VERSION.md)** | Preserved public bridge document |
| Review the compact manuscript | **[ArXiv review draft](paper/README.md)** ([PDF](output/pdf/supercongruence-portfolio.pdf)) | Working draft for external review; not submitted or peer reviewed |
| Check what was audited and corrected | [Audit log](AUDIT.md) | Exact-text audit record |
| Find one precise mathematical claim | [Claim-level result index](RESULT_INDEX.md) | Controlling status ledger |
| Track all 110 Bala/OEIS records | [110-record proof campaign](related-results/Bala110ProofCampaign.md) and [July 31 update](related-results/BalaJuly31ResearchUpdate.md) | Record-level route, status, evidence, and next action |
| Compare the portfolio economically | [Economist-style rankings](RANKINGS.md) | Editorial scores, not correctness claims |
| Browse the wider program | [Related-results reading map](related-results/README.md) | Theorem, reduction, computation, and synthesis lanes |
| Reproduce the computations | [`verification/run_all.py`](verification/run_all.py) | Exact checkers with no floating-point tolerance unless stated |

The repository workflow and promotion rules are documented in
[RESEARCH_WORKFLOW.md](RESEARCH_WORKFLOW.md).

## Core theorem

Define

```math
a(n)=\sum_{k=0}^{n}\frac{(2n+2k)!}{k!^4(n-k)!^2}.
```

The proposed theorem is

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}
```

for every prime \(p\) and all positive integers \(n,r\).

The proof has four ingredients:

1. each summand is a six-part multinomial coefficient;
2. Legendre carry counting kills the terms with \(p\nmid k\);
3. Ljunggren--Jacobsthal--Kazandzidis scaling transfers the terms with
   \(p\mid k\) to the previous level; and
4. a separate parity argument repairs the exceptional \(p=2,r=1\) case.

The [friendly proof](PROOF.md) contains the complete argument. The
[dyadic policy](DYADIC_POLICY.md) explains why the prime \(2\) is audited
separately throughout the repository.

## Portfolio dashboard

The portfolio is organized by mathematical mechanism rather than by the date
that a file was added.

| Lane | Flagship results | What the lane contributes |
| --- | --- | --- |
| Core and named OEIS problems | [A183068](PROOF.md), [Bala queue](related-results/BalaOeisSupercongruenceQueue.md), [July 31 Bala update](related-results/BalaJuly31ResearchUpdate.md), [paired Apéry residue-block target](related-results/BalaPairedResidueBlockExperiment.md), [symmetric-box plane partitions](related-results/SymmetricBoxPlanePartitionTower.md), [balanced factorial ratios](related-results/BalancedFactorialRatioCubicTowers.md), [rational gamma-ratio towers](related-results/RationalGammaRatioCubicTowers.md), [binomial-quotient closures](related-results/BinomialQuotientCancellation.md), [coefficient-framing family](related-results/CoefficientFramingCubicTower.md), [Straub prime-five packet](related-results/StraubPrimeFiveCoefficientPacket.md), [A288470 odd-prime tower](related-results/A288470OddPrimeTower.md), [A141057 multinomial-power tower](related-results/MultinomialPowerFrobeniusTowers.md), [A091527/A262732 odd-unit block towers](related-results/OddUnitBlockFrobeniusTowers.md), [A275652/A275654 Dixon--Legendre towers](related-results/DixonLegendreHalfBinomialTowers.md), [A364173 integrality and tower](related-results/A364173IntegralHalfBinomialTower.md), [literature census](related-results/SupercongruenceLiteratureCensus.md) | Named conjectures, published baselines, new family closures, and a reproducible target queue |
| General theorem engines | [Arithmetic Frobenius packets](related-results/ArithmeticFrobeniusPacketFramework.md), [Landau depth](related-results/LandauDepthSupercongruenceSynthesis.md), [q-calculus](related-results/QCalculusCyclotomicSupercongruences.md), [binomial-power Frobenius](related-results/BinomialPowerFrobeniusTheorem.md), [Euler products](related-results/EulerProductGaussianTower.md) | Local-to-global assembly plus reusable carry, transfer, Frobenius, and cyclotomic mechanisms |
| Gaussian and Eisenstein local arithmetic | [Inert-prime scaling](related-results/GaussianLucasPrimePowerTheorem.md), [ramified \(1+i\) theorem](related-results/GaussianLucasRamifiedTwoTheorem.md), [lattice-walk transfer congruences](related-results/LatticeWalkFrobeniusCongruences.md), [planar-noise and Y-game Walsh congruences](related-results/BlackNoiseWalshCongruences.md), [canonical products](related-results/GaussianLucasCanonicalProducts.md) | Split/inert/ramified prime separation, exact local valuations, and finite transfer- or Walsh-polynomial congruences for planar models |
| Dyadic structure | [Dyadic policy](DYADIC_POLICY.md), [Euler-product defect](related-results/DyadicHypercubeDefect.md), [Roe-inspired packet](ROE_2ADIC.md), [finite abelian counts](related-results/GQ2FiniteAbelianCounts.md), [dihedral counts](related-results/GQ2DihedralCounts.md), [quaternion counts](related-results/GQ2QuaternionCounts.md), [maximal-cyclic counts](related-results/GQ2MaximalCyclicCounts.md), [extraspecial obstruction](related-results/GQ2ExtraspecialObstruction.md) | Explicit binary normalization, parity, finite-shadow tests, uniform lift fibers, commutator and central-square corrections, first-level boundaries, and generator-rank obstructions |
| Finite-field and Frobenius packets | [Crystalline support bridge](related-results/CrystallineLocusSupportFrobeniusBridge.md), [primitive collision-orbit bridge](related-results/JacobianCollisionEulerOrbitBridge.md), [weighted-lift collisions](related-results/WeightedLiftCollisionSynthesis.md), [degree-five elliptic packet](related-results/JacobianDegreeFiveEllipticFrobenius.md), [hyperdeterminant Fourier packet](related-results/HyperdeterminantFourierSupercongruence.md), [hyperdeterminant entropy profile](related-results/HyperdeterminantEntropyProfile.md) | Support-order packets, exact Dold/Gauss orbit criteria, zeta factors, corrected adjacent towers, finite-field Fourier structure, and arithmetic entropy laws |
| Measurement and certification | [Dyadic joint spectrum](related-results/DyadicHypercubeJointSpectrum.md), [affine-spectrum hashing](related-results/AffineSpectrumHashing.md), [exact matroid hashing law](related-results/MatroidHashingLaw.md) | Exact collision probabilities and efficient finite-spectrum measurement design |
| Boundary results and corrections | [Zhang four-matrix counterexample](related-results/ZhangFourMatrixCounterexample.md), [rational-framing counterexample](related-results/RationalFramingCounterexample.md), [Gaussian reciprocal-power correction](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture), [Dwork boundaries](related-results/FrobeniusQuotientConstantTerms.md) | Exact counterexamples, minimal obstructions, and precise separation between a failed auxiliary route and its parent problem |

The last lane improves the experimental and certification infrastructure of
the program. It does not strengthen a \(p\)-adic exponent by itself.

## Status language

The exact label in [RESULT_INDEX.md](RESULT_INDEX.md) controls. In brief:

| Label | Meaning |
| --- | --- |
| **Published theorem** | A cited external source proves the statement used here |
| **Audited draft** | A complete argument received a separate machine-assisted exact-text audit; not peer reviewed |
| **Complete unchecked draft** | A complete written proof and checks are present; independent review and priority work remain |
| **Deduction** | An explicit consequence of a broader theorem or proof candidate |
| **Reduction** | A target has been reduced to a smaller unresolved statement |
| **Computational** | Exact finite evidence or a certificate is present, but no general proof is claimed |
| **Framework or synthesis** | Organizes mechanisms or literature without claiming a new theorem |

Source status is recorded separately as **named open problem**,
**explicit source direction**, or **structural follow-on**. A high ranking
never upgrades a proof status.

## Current review queue

The highest-value specialist-review targets are:

1. the new [symmetric-box plane-partition tower](related-results/SymmetricBoxPlanePartitionTower.md), which proves A352656 and A352657 and subsumes A008793;
2. the [dimension-minimal counterexample to Zhang's four-matrix conjecture](related-results/ZhangFourMatrixCounterexample.md);
3. the exact ramified Gaussian valuation at \(1+i\);
4. inert Gaussian adjacent prime-power scaling;
5. the new [first two A365029 levels](related-results/A365029FirstTwoLevels.md);
6. the all-degree weighted-lift collision theorem;
7. the primitive collision-orbit interpretation and sharp obstruction;
8. the degree-five elliptic Frobenius packet; and
9. the original A183068 proof.

The active Bala campaign has now proved 29 census records in this repository
and matched 12 more to published sources. Its recent
half-binomial work proves five named $p^{3r}$ towers:
[A091527](https://oeis.org/A091527) and
[A262732](https://oeis.org/A262732) by an
[odd-unit block argument](related-results/OddUnitBlockFrobeniusTowers.md),
then [A275652](https://oeis.org/A275652) and
[A275654](https://oeis.org/A275654) by one
[Dixon--Legendre half-binomial argument](related-results/DixonLegendreHalfBinomialTowers.md),
and [A364173](https://oeis.org/A364173) by a related
[factorization and carry-interval argument](related-results/A364173IntegralHalfBinomialTower.md)
that also proves the source page's integrality conjecture.  The subsequent
[rational gamma-ratio theorem](related-results/RationalGammaRatioCubicTowers.md)
works at every fixed denominator and closes the A364175 tower using David
Radcliffe's July 2026 integrality proof; the same theorem reduces the rest
of A364172--A364184 to global integrality and proves the all-row A365025
conjecture together with every stable row of A364513.
The [binomial-quotient cancellation theorem](related-results/BinomialQuotientCancellation.md)
also closes the complete two-parameter conjecture on
[A357509](https://oeis.org/A357509), rather than only its displayed
sequence.
The [Apéry odd-moment theorem](related-results/AperyOddMomentPrimeClassification.md)
then proves the prime conjecture on A357510 and gives an exact
exceptional-prime formula for every higher positive odd moment. In
particular, it proves the prime slice of A357512 and exhibits two missing
exceptions in one proposed family member, while leaving the record's
composite-\(n\) claim open.
The [coefficient-root theorem](related-results/CoefficientPowerGaussBaseline.md)
then finishes the factorial route's source audit: it proves the displayed
root series on A002897, A008978, and A113424 integral and establishes their
universal \(p^r\) variable-power baseline, while leaving the two genuinely
stronger \(p^{3r}\) conjectures explicitly open.
The [Apéry defect packet](related-results/AperyRankOneDefectPacket.md)
also finishes the derived route's source audit: five records and two
nonlinear companions collapse to three linear adjacent-defect congruences.
Those three congruences remain open.
The [modular-product packet](related-results/ModularProductPrimeCoefficientPacket.md)
proves seven further named records: four by a universal prime-coefficient
formula and three by specialization of the colored Euler-product theorem.
It also supplies quadratic baselines for four proposed cubic towers. The
route now has no untouched record. The
[A229452 coefficient-root theorem](related-results/A229452CoefficientRootBaseline.md)
proves that record's all-\(m\) integrality conjecture and all-prime
\(p^r\) towers for both source parameter families while leaving the proposed
cubic gains open. The
[A049505 paired-product theorem](related-results/A049505SymmetricPlanePartitionCongruences.md)
proves all three displayed symmetric-plane-partition congruences from one
stronger prime-power evaluation. The
[A008793 cube-plane-partition theorem](related-results/A008793CubePlanePartitionTower.md)
proves its full nonlinear all-prime \(p^{4r}\) tower by exact product
splitting and reduced-residue reciprocal blocks, including the separate
binary argument.
The [symmetric-box theorem](related-results/SymmetricBoxPlanePartitionTower.md)
now shows that this is one member of an infinite family: for every fixed
\(c\geq1\), plane partitions in an \(N\times N\times cN\) box satisfy the
same all-prime nonlinear \(p^{4r}\) tower. Its \(c=2\) and \(c=3\)
specializations prove the named A352656 and A352657 conjectures, while a
refined reciprocal-interval pairing absorbs the exceptional prime \(3\)
uniformly.
The [coefficient-framing theorem](related-results/CoefficientFramingCubicTower.md)
then closes six more source records at once: A002003, A348410, A351857,
A352373, A370101, and A370102 follow from one self-contained elementary
Cartier proof, with the sharper $3^{3r-1}$ exceptional-prime bound.
An [exact counterexample](related-results/RationalFramingCounterexample.md)
shows that the broader rational-framing congruences previously cited for
these records do not hold as printed. The six records are therefore counted
as proved here, not as published-source closures.

See [RANKINGS.md](RANKINGS.md) for the complete multi-criteria assessment and
the separate queue of reductions and computational targets.

## Reproduction

Run the core checker:

```text
python verification/verify_a183068.py
```

Run every registered exact checker:

```text
python verification/run_all.py
```

Run the repository integrity and local-link audit:

```text
python verification/check_repository_integrity.py
```

The integrity checker also protects the published
[`BALA_VERSION.md`](BALA_VERSION.md) bridge document from accidental edits.

## Repository structure

| Path | Purpose |
| --- | --- |
| [`PROOF.md`](PROOF.md) | Readable core proof |
| [`BALA_VERSION.md`](BALA_VERSION.md) | Preserved response to the proof routes supplied by Peter Bala |
| [`RESULT_INDEX.md`](RESULT_INDEX.md) | Claim-level status ledger |
| [`RANKINGS.md`](RANKINGS.md) | Economist-style portfolio assessment |
| [`RELATED_RESULTS.md`](RELATED_RESULTS.md) | Compact relationship map |
| [`related-results/`](related-results/README.md) | Full follow-on notes |
| [`verification/`](verification/) | Exact checkers and experiments |
| [`AUDIT.md`](AUDIT.md) | Corrections and machine-assisted audits |
| [`DYADIC_POLICY.md`](DYADIC_POLICY.md) | Required checklist for all-prime and ramified claims |
| [`ROE_2ADIC.md`](ROE_2ADIC.md) | Public Roe--Turturean-inspired dyadic packet |
| [`ROE_TURTUREAN_NOTE.md`](ROE_TURTUREAN_NOTE.md) | Short source-facing statement of the finite abelian \(2\)-target result |
| [`paper/`](paper/README.md) | Compact review manuscript and submission checklist |
| [`output/pdf/`](output/pdf/) | Rendered review copies of repository manuscripts |

## Public research policy

1. Cite the originating sequence, conjecture, and prior theorem.
2. Separate theorem, proof candidate, computation, reduction, and analogy.
3. Preserve counterexamples and corrections.
4. Treat negative literature searches as routing evidence, not proof of
   novelty.
5. Require an explicit \(p=2\) analysis before calling an all-prime theorem
   complete.
6. Keep verification scripts reproducible and distinguish them from proofs.
7. Promote a claim only through the gates in
   [RESEARCH_WORKFLOW.md](RESEARCH_WORKFLOW.md).

## Attribution

- Paul D. Hanna created A183068 in December 2010.
- Peter Bala added the factorial-sum formula and supercongruence conjecture in
  July 2024.
- The present proof draft was prepared by Ravi Bajaj and Alexander Burns.

Corrections, prior-art references, and specialist reviews are welcome.
