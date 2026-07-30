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
| Check what was audited and corrected | [Audit log](AUDIT.md) | Exact-text audit record |
| Find one precise mathematical claim | [Claim-level result index](RESULT_INDEX.md) | Controlling status ledger |
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
| Core and named OEIS problems | [A183068](PROOF.md), [Bala queue](related-results/BalaOeisSupercongruenceQueue.md), [literature census](related-results/SupercongruenceLiteratureCensus.md) | Named conjectures, published baselines, and a reproducible target queue |
| General theorem engines | [Landau depth](related-results/LandauDepthSupercongruenceSynthesis.md), [q-calculus](related-results/QCalculusCyclotomicSupercongruences.md), [binomial-power Frobenius](related-results/BinomialPowerFrobeniusTheorem.md), [Euler products](related-results/EulerProductGaussianTower.md) | Reusable carry, transfer, Frobenius, and cyclotomic mechanisms |
| Gaussian and Eisenstein local arithmetic | [Inert-prime scaling](related-results/GaussianLucasPrimePowerTheorem.md), [ramified \(1+i\) theorem](related-results/GaussianLucasRamifiedTwoTheorem.md), [lattice-walk transfer congruences](related-results/LatticeWalkFrobeniusCongruences.md), [planar-noise Walsh congruences](related-results/BlackNoiseWalshCongruences.md), [canonical products](related-results/GaussianLucasCanonicalProducts.md) | Split/inert/ramified prime separation, exact local valuations, and finite transfer- or Walsh-polynomial congruences for planar models |
| Dyadic structure | [Dyadic policy](DYADIC_POLICY.md), [Euler-product defect](related-results/DyadicHypercubeDefect.md), [Roe-inspired packet](ROE_2ADIC.md), [finite abelian counts](related-results/GQ2FiniteAbelianCounts.md), [dihedral counts](related-results/GQ2DihedralCounts.md), [quaternion counts](related-results/GQ2QuaternionCounts.md), [maximal-cyclic counts](related-results/GQ2MaximalCyclicCounts.md), [extraspecial obstruction](related-results/GQ2ExtraspecialObstruction.md) | Explicit binary normalization, parity, finite-shadow tests, uniform lift fibers, commutator and central-square corrections, first-level boundaries, and generator-rank obstructions |
| Finite-field and Frobenius packets | [Weighted-lift collisions](related-results/WeightedLiftCollisionSynthesis.md), [degree-five elliptic packet](related-results/JacobianDegreeFiveEllipticFrobenius.md), [hyperdeterminant Fourier packet](related-results/HyperdeterminantFourierSupercongruence.md), [hyperdeterminant entropy profile](related-results/HyperdeterminantEntropyProfile.md) | Exact zeta factors, corrected adjacent towers, finite-field Fourier structure, and arithmetic entropy laws |
| Measurement and certification | [Dyadic joint spectrum](related-results/DyadicHypercubeJointSpectrum.md), [affine-spectrum hashing](related-results/AffineSpectrumHashing.md), [exact matroid hashing law](related-results/MatroidHashingLaw.md) | Exact collision probabilities and efficient finite-spectrum measurement design |
| Boundary results and corrections | [Zhang four-matrix counterexample](related-results/ZhangFourMatrixCounterexample.md), [Gaussian reciprocal-power correction](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture), [Dwork boundaries](related-results/FrobeniusQuotientConstantTerms.md) | Exact counterexamples, minimal obstructions, and precise separation between a failed auxiliary route and its parent problem |

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

1. the [dimension-minimal counterexample to Zhang's four-matrix conjecture](related-results/ZhangFourMatrixCounterexample.md);
2. the exact ramified Gaussian valuation at \(1+i\);
3. inert Gaussian adjacent prime-power scaling;
4. the new [first two A365029 levels](related-results/A365029FirstTwoLevels.md);
5. the all-degree weighted-lift collision theorem;
6. the degree-five elliptic Frobenius packet; and
7. the original A183068 proof.

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
