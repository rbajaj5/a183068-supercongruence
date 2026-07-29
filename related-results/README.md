# Related supercongruence program

This directory contains the complete follow-on drafts that grew out of the
A183068 proof. It is organized as a mathematical reading queue, not as a claim
that every file has the same level of verification.

The common mechanism is:

1. split a finite sum into $p$-adic valuation strata;
2. use digit carries or finite-field symmetry to make low strata vanish;
3. transfer the surviving terms by scaling, Frobenius, or translation; and
4. measure whether the transfer error supplies the required power of $p$.

The complete Economist-style scorecard is
[`RANKINGS.md`](../RANKINGS.md). It scores every claim-level result, including
the finite-field determinant, Pfaffian, and hyperdeterminant branch, while
keeping proof maturity and cost remaining separate from estimated impact.

## Recommended reading order

| Order | Note | Connection to A183068 | Status |
| ---: | --- | --- | --- |
| 0 | [Repository-wide dyadic audit policy](../DYADIC_POLICY.md) | Defines what must be checked before any all-prime or ramified theorem is called complete | Governing proof and ranking policy |
| 1 | [Landau-depth synthesis](LandauDepthSupercongruenceSynthesis.md) | Extracts the A183068 carry-and-scaling proof into a computable theorem; contains an infinite all-prime $p^{2r}$ family and an all-prime $p^{3r}$ subfamily | Complete proof candidate; internal recheck passed, independent review pending |
| 1A | [q-calculus and cyclotomic supercongruences](QCalculusCyclotomicSupercongruences.md) | Turns Landau depth into exact root-of-unity multiplicity; gives a square q-lift of A183068 and an explicit corrected cubic theorem for depth-three families | Complete deductions from Clark and Straub; exact polynomial checks; priority preliminary |
| 1B | [Peter Bala's OEIS queue](BalaOeisSupercongruenceQueue.md) | Proves the A365029 boundary family and first two adjacent levels, plus the A375178 prime-level odd-power family; closes A333593 via Coster and Jacobsthal--Kazandzidis | Three complete elementary proof packets, published-theorem reductions, and exact checks; priority preliminary |
| 1B-A | [First two A365029 levels](A365029FirstTwoLevels.md) | Proves the \(p^3\) and \(p^6\) adjacent congruences by shifted scaling plus one- and two-digit harmonic cancellation | Complete unchecked proof; 67,310 exact checks |
| 1B-L | [Supercongruence literature and Bala--OEIS census](SupercongruenceLiteratureCensus.md) | Maps a reproducible 110-record OEIS search to the published theorem families and consolidates the genuinely live targets before more proof work is spent | Literature map with explicit source and priority boundaries |
| 1B-G | [Gaussian generalization map for the Bala queue](BalaGaussianGeneralizationMap.md) | Routes all 110 census records through five Gaussian proof architectures and separates formal coefficient changes from Frobenius twists and prime-ideal theorems | Exhaustive research map; no novelty claim |
| 1B-GE | [Exact Bala Gaussian-twist pilot](BalaGaussianTwistPilot.md) | Tests three finite-sum routes and supplies exact counterexamples to blindly preserving the untwisted cubic exponent | 195 exact checks; computational triage |
| 1C | [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md) | Turns collision counting into one second divided-difference curve in every degree; gives a genus ladder and a universal corrected tower | Complete theorem with cross-degree checks; priority preliminary |
| 1D | [Finite-field counts for the Fable Jacobian counterexample](JacobianCounterexampleFiniteFieldCounts.md) | Uses the same adjacent-extension viewpoint to organize cubic fibers, collisions, and Frobenius counts of the new counterexample | Complete elementary theorem with exact checks; priority preliminary |
| 1E | [Degree-four Jacobian Frobenius obstruction](JacobianDegreeFourFrobeniusObstruction.md) | Shows how quadratic Artin factors obstruct raw adjacency and how two-step or corrected towers recover exact congruences | Complete elementary theorem with exact checks; priority preliminary |
| 1F | [Degree-five elliptic Frobenius packet](JacobianDegreeFiveEllipticFrobenius.md) | Shows the next transition: a tangent cubic contributes a non-CM elliptic trace, and removing the full Frobenius packet leaves an exact \(2r-2\) tower | Complete theorem with direct finite-field and tower checks; priority preliminary |
| 2 | [Frobenius quotients of constant-term sequences](FrobeniusQuotientConstantTerms.md) | Proves the universal first-order expansion, identifies the exact rank-one condition behind the Cooper law, and gives exact counterexamples to two proposed Dwork shortcuts | Complete elementary theorem; Dwork boundaries certified |
| 3 | [p-adic Arzelà--Ascoli framework](PadicArzelaAscoliSupercongruenceTowers.md) | Proves the vertical limit supplied by A183068, uses the Banach contraction $x\mapsto px$ to rule out a global continuous interpolation, and proves uniform quadratic contraction of every normalized defect at zero | Complete elementary framework and obstruction; unit-shell estimate open |
| 4 | [Gaussian Frobenius twists](GaussianFrobeniusTwists.md) | Shows that discard-and-rescale proofs lift to roots-of-unity weights; specializes A183068 to a Gaussian split/inert congruence | Complete elementary deduction; priority unchecked |
| 4B | [Binomial-power polynomial Frobenius theorem](BinomialPowerFrobeniusTheorem.md) | Proves the coefficientwise \(X\mapsto X^p\) tower for every exponent \(m\ge3\), including the multiplicity bonus \(v_p(m)\) and all Gaussian local cases | Complete elementary deduction; priority not established |
| 4C | [Quadratic A005259/A333592-family polynomial towers](QuadraticGaussianQueueTheorem.md) | Closes the two remaining Gaussian-pilot targets at coefficientwise exponent \(2r\) and covers every positive parameter pair in the broader A333592 family | Complete classical-scaling corollary; not the stronger A333592 cubic conjecture |
| 4D | [Cyclotomic coefficient-pair theorem](CyclotomicCoefficientPairTheorem.md) | Proves the A228960 and A350383 \(p^{2r}\) conjectures in coefficientwise form and specializes them at \(X=i\) | Complete elementary proof candidate; priority search preliminary |
| 4E | [Colored Euler-product Frobenius theorem](EulerProductGaussianTower.md) | Proves one coefficientwise \(p^{2r}\) theorem containing Bala's full quadratic product packet, the A380290 baseline, and split/inert Gaussian part-count twists | Complete elementary proof candidate; the special untwisted A380290 cubic conjecture remains open |
| 4F | [Dyadic hypercube defect](DyadicHypercubeDefect.md) | Proves the sharp binary law \(e(1)=1\), \(e(r)=2r\) for \(r\ge2\), identifies the exact first-level modulus-\(4\) obstruction, and specializes it for A380290 to a lacunary binary theta coefficient | Complete elementary theorem and exact checks; no priority claim for the standard \(2\)-derivation |
| 4G | [Complete Gaussian local table for Euler products](EulerProductGaussianLocalTable.md) | Combines the odd and dyadic theorems into one split/inert/ramified prime-ideal law, including the \(i\mapsto-1\) binary cross-twist and exact \((1+i)\)-adic exponents | Complete corollary and exact local-valuation checks; withdrawn Witt--Hadamard near-match excluded as proof input |
| 4H | [Walsh analysis of the dyadic hypercube defect](DyadicHypercubeWalshAnalysis.md) | Shows that every output coordinate has a matching quadratic graph and computes its exact model count, Walsh spectrum, influences, noise stability, and every affine-face restriction | Complete combinatorial corollary and exhaustive checks; classical Boolean Fourier machinery |
| 4I | [Joint spectrum of the dyadic hypercube defect](DyadicHypercubeJointSpectrum.md) | Reduces every XOR of output coordinates to an alternating convolution matrix; recovers exact joint counts, collision probability, chi-squared distance, and distribution bounds from ranks, radicals, and Gauss-sum signs | Complete finite-dimensional theorem and exhaustive checks; classical quadratic-form Fourier theorem |
| 4J | [Exact hashing of affine Fourier spectra](AffineSpectrumHashing.md) | Converts affine Walsh-support dimension into an exact random-hash success probability and a \(\log_2(s)\)-scale sufficient measurement budget | Complete specialization of the classical binary full-rank formula with exact checks |
| 4K | [Exact matroid law for linear hashing](MatroidHashingLaw.md) | Extends the affine formula to every finite Fourier support through the characteristic polynomial of its difference matroid | Complete application of the classical Crapo--Rota Critical Theorem; [priority audit](HypercubeHashingPriorityAudit.md) |
| 4A | [Chowla--Dwork--Evans split-prime defect](ChowlaDworkEvansSplitDefect.md) | Rewrites their published modulo-\(p^2\) lift as an exact normalized defect and exceptional-prime criterion | Published theorem plus exact corollary; no novelty claim |
| 5 | [Cubic $(\eta)$ congruence at $p=3$](EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to fill a small-prime gap in a published theorem | Complete unchecked draft |
| 6 | [Gaussian Wolstenholme citation network](GaussianWolstenholmeCitationNetwork.md) | Replaces scaling by translation-invariant Gaussian residue blocks | Three major candidate results with exact certificates; independent review required |
| 7 | [Gaussian canonical-product synthesis](GaussianLucasCanonicalProducts.md) | Extracts the dominant logarithmic-moment mechanism, proves that the normalized ramified block is a bijective disk isometry, and extends it to a first-moment-dominance chamber | Proved local theorem plus open research program |
| 8 | [Gaussian product dynamics](GaussianProductDynamicsConjectures.md) | Proves the exact return valuation and finite-quotient cycle profile for every unit translation; asks whether the map is actually conjugate to addition | Complete deduction from the ramified moment estimates; conjugacy open |
| 9 | [Gaussian Lucas literature puzzle](GaussianLucasLiteraturePuzzle.md) | Connects the product theorem to Dwork/Frobenius theory, generalized factorials, and compatible $p$-adic dynamics | Literature map; bridges ranked by strength |
| 10 | [Gaussian power-sum conjectures](GaussianPowerSumConjectures.md) | Uses fourth-root and affine-orbit cancellation in the same residue-stratification spirit | Two formula proofs and exact counterexamples; independent review required |
| 11 | [Higher-degree finite-field box polynomials](HigherDegreeFiniteFieldBoxPolynomials.md) | Generalizes the Gaussian polynomial factorization to every finite-field degree | Complete elementary theorem; likely classical infrastructure |
| 12 | [Binary $s_{18}$ reduction](S18TwoAdicReduction.md) | Isolates the exact sharpened scaling lemma still needed at $p=2$ | Substantial reduction; naive factor-by-factor proof refuted |
| 13 | [Gaussian citation-network boundary report](GaussianCitationNetworkBoundaryReport.md) | Records rigorous limits of the Gaussian search, including Erdős--Moser reductions | Reduction and bounded search, not a global solution |
| 14 | [Cooper level-11 rare primes](CooperLevel11RarePrimes.md) | Isolates the first obstruction and records a 350-case first-order Frobenius law reducing the full $r=1$ conjecture to it | Computational theorem target; fixed-prime automata route is conditional on finding a rational diagonal |
| 15 | [Finite abelian \(G_{\mathbb Q_2}\) targets](GQ2FiniteAbelianCounts.md) | Opens the Roe--Turturean finite-target lane with a Frattini-shadow count | Complete elementary formula; no novelty claim |
| 15A | [Dihedral and quaternion \(G_{\mathbb Q_2}\) targets](GQ2DihedralCounts.md) / [quaternion targets](GQ2QuaternionCounts.md) | Introduces the rotation/reflection relator calculation and its low binary boundary layers | Complete direct derivations; enumeration literature exists |
| 15B | [Semidihedral and modular targets](GQ2MaximalCyclicCounts.md) | Completes the maximal-cyclic nonabelian families in the same coordinate language | Complete direct derivation and certificate; Ito--Yamagishi already published the counts |
| 15C | [Extraspecial rank obstruction](GQ2ExtraspecialObstruction.md) | Closes the higher pure-extraspecial branch before enumeration: the targets need at least four generators | Complete elementary obstruction |

## Strongest present claims

The directory currently contains these especially reviewable claims:

- the Landau-depth theorem unifying termwise vanishing with multinomial
  transfer;
- the universal first-order Frobenius-quotient identity for constant-term
  sequences and its A183068 corollary;
- the vertical-limit theorem and normalized-defect compactness framework for
  supercongruence towers;
- the Banach fixed-point obstruction proving that the nonconstant A183068
  tower limit cannot extend continuously to all of $\mathbb Z_p$;
- the exact quadratic scaling and uniform equicontinuity at zero of the
  normalized A183068 defects;
- the cubic $(\eta)$ congruence at the missing prime $3$;
- the Gaussian Lucas congruence modulo $p^3$ at every inert prime $p>5$; and
- the exact adjacent-scale valuation at the ramified prime $1+i$;
- the exact return filtration and finite-quotient cycle profile of every unit
  translation of the normalized ramified product; and
- an infinite counterexample family plus corrected theorem for a printed
  Gaussian reciprocal-power conjecture.

These are research drafts. Exact computation supports the claims that use it,
but none should be described as peer reviewed.

## Verification

Run every included checker from the repository root:

```text
python verification/run_all.py
```

The individual correspondence is:

| Note | Checker |
| --- | --- |
| Landau depth | `verification/related/verify_landau_supercongruence.py` |
| Peter Bala's OEIS queue | `verification/related/verify_bala_oeis_supercongruences.py` |
| First two A365029 levels | `verification/related/verify_a365029_first_two_levels.py` |
| q-calculus and cyclotomic lifts | `verification/related/verify_q_calculus_supercongruence.py` |
| All-degree weighted-lift collisions | `verification/related/verify_weighted_lift_collision_synthesis.py` |
| Fable Jacobian-counterexample counts | `verification/related/verify_jacobian_counterexample_counts.py` |
| Degree-four Jacobian collisions | `verification/related/verify_jacobian_degree_four.py` |
| Degree-five Jacobian collisions | `verification/related/verify_jacobian_degree_five.py` |
| Frobenius quotient identity | Coefficientwise algebraic proof; no checker required |
| Dwork and continuity boundaries | `verification/related/verify_dwork_boundaries.py` |
| p-adic Arzelà--Ascoli framework | Elementary ultrametric, contraction, and compactness proofs |
| Cubic $(\eta)$ | `verification/related/verify_eta_prime3.py` |
| Cooper level 11 | `verification/related/verify_cooper_level11.py` |
| Gaussian Frobenius twists | `verification/related/verify_gaussian_twists.py` |
| Bala Gaussian-twist pilot | `verification/related/verify_bala_gaussian_twist_pilot.py` |
| Binomial-power polynomial theorem | `verification/related/verify_binomial_power_frobenius.py` |
| Quadratic A005259/A333592 towers | `verification/related/verify_quadratic_gaussian_queue.py` |
| A228960/A350383 coefficient pair | `verification/related/verify_cyclotomic_coefficient_pair.py` |
| Colored Euler-product tower | `verification/related/verify_euler_product_gaussian_tower.py` |
| Dyadic hypercube defect | `verification/related/verify_dyadic_hypercube_defect.py` |
| Dyadic hypercube Walsh analysis | `verification/related/verify_dyadic_hypercube_walsh.py` |
| Dyadic hypercube joint spectrum | `verification/related/verify_dyadic_hypercube_walsh.py` |
| Affine-spectrum and matroid hashing laws | `verification/related/verify_affine_spectrum_hashing.py` |
| Chowla--Dwork--Evans split-prime defect | `verification/related/verify_chowla_dwork_evans_defect.py` |
| Gaussian power sums | `verification/related/verify_gaussian_power_sums.py` |
| Gaussian Wolstenholme network | `verification/related/verify_gaussian_wolstenholme.py` |
| Gaussian product isometry | `verification/related/verify_gaussian_product_isometry.py` |
| Gaussian product dynamics | `verification/related/experiment_gaussian_product_dynamics.py` (run separately; includes deeper finite-quotient tests) |
| Higher-degree box polynomials | `verification/related/verify_higher_degree_box_polynomial.py` |
| Roe--Turturean finite abelian \(2\)-target counts | `verification/related/verify_gq2_finite_abelian_counts.py` |
| Roe--Turturean dihedral \(2\)-target counts | `verification/related/verify_gq2_dihedral_counts.py` |
| Roe--Turturean generalized-quaternion \(2\)-target counts | `verification/related/verify_gq2_quaternion_counts.py` |
| Roe--Turturean semidihedral/modular counts and extraspecial rank boundary | `verification/related/verify_gq2_maximal_cyclic_counts.py` |
| Gaussian Erdős--Moser boundary search | `verification/related/verify_gaussian_erdos_moser.py` |

The binary $s_{18}$ file is a reduction rather than a completed theorem and
does not yet have a dedicated checker.

## Status discipline

Inclusion here means that a result is sufficiently coherent for Paul and other
specialists to inspect. It does not promote an unchecked candidate to a
theorem. Corrections, prior-art references, and failed cases should remain in
the repository so that the development history is auditable.

For all-prime statements, status also depends on the
[dyadic audit policy](../DYADIC_POLICY.md). An odd-prime proof with an open
\(p=2\) step remains a reduction or target; a ramified \(1+i\) theorem must
state its valuation normalization separately.

