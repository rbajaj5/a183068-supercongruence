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
the finite-field determinant, Pfaffian, and hyperdeterminant Fourier branch,
while keeping proof maturity and cost remaining separate from estimated
impact.

## Recommended reading order

| Order | Note | Connection to A183068 | Status |
| ---: | --- | --- | --- |
| 1 | [Landau-depth synthesis](LandauDepthSupercongruenceSynthesis.md) | Extracts the A183068 carry-and-scaling proof into a computable theorem; contains an infinite all-prime $p^{2r}$ family and an all-prime $p^{3r}$ subfamily | Complete proof candidate; internal recheck passed, independent review pending |
| 1A | [q-calculus and cyclotomic supercongruences](QCalculusCyclotomicSupercongruences.md) | Turns Landau depth into exact root-of-unity multiplicity; gives a square q-lift of A183068 and an explicit corrected cubic theorem for depth-three families | Complete deductions from Clark and Straub; exact polynomial checks; priority preliminary |
| 1B | [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md) | Turns collision counting into one second divided-difference curve in every degree; gives a genus ladder and a universal corrected tower | Complete theorem with cross-degree checks; priority preliminary |
| 1C | [Frobenius obstruction automata](FrobeniusObstructionAutomata.md) | Converts every fixed-precision raw collision congruence into an eventually periodic unary language with rational density; the corrected tower remains universal | Complete structural theorem with exact checks through four precisions; priority preliminary |
| 1C.1 | [Finite-state Frobenius thermodynamics](FrobeniusTransferThermodynamics.md) | Packages all fixed-precision valuation strata into one rational orbit series and one partition polynomial; gives the complete degree-seven \(5^4\) distribution | Complete structural deduction with direct full-period check; priority preliminary |
| 1C.2 | [All-precision unit-root lifting](PadicValuationExpansion.md) | Proves the degree-seven trace period \(39\cdot5^{k-1}\) at every precision, computes the \(5^5\) and \(5^6\) valuation polynomials, and identifies the profinite valuation grid | Complete structural theorem with direct certificates; priority preliminary |
| 1C.3 | [Hyperdeterminant convolution tower](HyperdeterminantConvolutionTower.md) | Uses exact finite-field Fourier inversion to determine every convolution fiber, prove a sharp infinite adjacent-extension family, and quantify mixing; it isolates the ambient restriction/Kakeya transform as the next problem | Complete elementary theorem with exact checks; priority preliminary |
| 1C.4 | [Determinant and Pfaffian convolution towers](DeterminantPfaffianConvolutionTowers.md) | Extracts a constant-spectrum Fourier compiler and obtains all convolution fibers, exact mixing, and sharp \((\ell E-1)(r-1)\) towers for two classical relative invariants | Complete elementary theorem with exact checks; priority preliminary |
| 1C.5 | [USAMO dyadic Hamming supercongruence](USAMODyadicHammingSupercongruence.md) | Turns the forced-halving solution of a named olympiad problem into an exact enumeration, a \(d+1\)-packet Walsh algorithm, and a polynomial adjacent-extension tower with exceptional prime \(439\) | Complete elementary theorem with exact checks; priority preliminary |
| 1D | [Finite-field counts for the Fable Jacobian counterexample](JacobianCounterexampleFiniteFieldCounts.md) | Uses the same adjacent-extension viewpoint to organize cubic fibers, collisions, and Frobenius counts of the new counterexample | Complete elementary theorem with exact checks; priority preliminary |
| 1E | [Degree-four Jacobian Frobenius obstruction](JacobianDegreeFourFrobeniusObstruction.md) | Shows how quadratic Artin factors obstruct raw adjacency and how two-step or corrected towers recover exact congruences | Complete elementary theorem with exact checks; priority preliminary |
| 1F | [Degree-five elliptic Frobenius packet](JacobianDegreeFiveEllipticFrobenius.md) | Shows the next transition: a tangent cubic contributes a non-CM elliptic trace, and removing the full Frobenius packet leaves an exact \(2r-2\) tower | Complete theorem with direct finite-field and tower checks; priority preliminary |
| 1G | [Degree-six genus-three Frobenius obstruction](JacobianDegreeSixGenusThree.md) | Gives the first explicit higher-genus packet and a permanent raw obstruction at \(p=13\) | Complete theorem with extension-field and symbolic checks; priority preliminary |
| 1H | [Degree-seven genus-six Frobenius automaton](JacobianDegreeSevenGenusSix.md) | Produces the period-\(156\) example that motivates the general fixed-precision automaton | Complete theorem with exact counts through \(\mathbf F_{5^6}\); priority preliminary |
| 2 | [Frobenius quotients of constant-term sequences](FrobeniusQuotientConstantTerms.md) | Proves the universal first-order expansion, identifies the exact rank-one condition behind the Cooper law, and gives exact counterexamples to two proposed Dwork shortcuts | Complete elementary theorem; Dwork boundaries certified |
| 3 | [p-adic Arzelà--Ascoli framework](PadicArzelaAscoliSupercongruenceTowers.md) | Proves the vertical limit supplied by A183068, uses the Banach contraction $x\mapsto px$ to rule out a global continuous interpolation, and proves uniform quadratic contraction of every normalized defect at zero | Complete elementary framework and obstruction; unit-shell estimate open |
| 4 | [Gaussian Frobenius twists](GaussianFrobeniusTwists.md) | Shows that discard-and-rescale proofs lift to roots-of-unity weights; specializes A183068 to a Gaussian split/inert congruence | Complete elementary deduction; priority unchecked |
| 5 | [Cubic $(\eta)$ congruence at $p=3$](EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to fill a small-prime gap in a published theorem | Complete unchecked draft |
| 6 | [Gaussian Wolstenholme citation network](GaussianWolstenholmeCitationNetwork.md) | Replaces scaling by translation-invariant Gaussian residue blocks | Three major candidate results with exact certificates; independent review required |
| 7 | [Gaussian canonical-product synthesis](GaussianLucasCanonicalProducts.md) | Extracts the dominant logarithmic-moment mechanism, proves that the normalized ramified block is a bijective disk isometry, and extends it to a first-moment-dominance chamber | Proved local theorem plus open research program |
| 8 | [Gaussian product dynamics](GaussianProductDynamicsConjectures.md) | Proves the exact return valuation and finite-quotient cycle profile for every unit translation; asks whether the map is actually conjugate to addition | Complete deduction from the ramified moment estimates; conjugacy open |
| 9 | [Cubic angular residue](GaussianAngularResidueTheorem.md) | Combines a \(C_4\) Fourier projection with Kummer congruence; replaces a false constant-valuation conjecture by an explicit residue through \(r=2p-1\), three universal inert-prime zero families, and a sharp first obstruction | Complete proof candidate with 3,348 extended exact residue checks; independent review and priority search required |
| 10 | [Gaussian Lucas literature puzzle](GaussianLucasLiteraturePuzzle.md) | Connects the product theorem to Dwork/Frobenius theory, generalized factorials, and compatible $p$-adic dynamics | Literature map; bridges ranked by strength |
| 11 | [Gaussian power-sum conjectures](GaussianPowerSumConjectures.md) | Uses fourth-root and affine-orbit cancellation in the same residue-stratification spirit | Two formula proofs, a cubic residue theorem, and exact counterexamples; independent review required |
| 12 | [Higher-degree finite-field box polynomials](HigherDegreeFiniteFieldBoxPolynomials.md) | Generalizes the Gaussian polynomial factorization to every finite-field degree | Complete elementary theorem; likely classical infrastructure |
| 13 | [Binary $s_{18}$ reduction](S18TwoAdicReduction.md) | Isolates the exact sharpened scaling lemma still needed at $p=2$ | Substantial reduction; naive factor-by-factor proof refuted |
| 14 | [Gaussian citation-network boundary report](GaussianCitationNetworkBoundaryReport.md) | Records rigorous limits of the Gaussian search, including Erdős--Moser reductions | Reduction and bounded search, not a global solution |
| 15 | [Cooper level-11 rare primes](CooperLevel11RarePrimes.md) | Isolates the first obstruction and records a 350-case first-order Frobenius law reducing the full $r=1$ conjecture to it | Computational theorem target; fixed-prime automata route is conditional on finding a rational diagonal |
| 16 | [Exact dyadic orientation lifts and Dehn twists](GQ2OrientationLifts.md) | Gives a clean comparison case for small-prime lifting and identifies the source's shear as an exact \(\mathbb Z_2\)-family of outer Dehn twists acting on the defect tower | Complete elementary sharpening and structural extraction from Roe--Turturean; checked through \(2^{32}\); no novelty claim |

## Strongest present claims

The directory currently contains these especially reviewable claims:

- the Landau-depth theorem unifying termwise vanishing with multinomial
  transfer;
- the fixed-precision Frobenius automaton theorem, which makes every good
  weighted-lift raw-congruence level set eventually periodic with rational
  density;
- the universal first-order Frobenius-quotient identity for constant-term
  sequences and its A183068 corollary;
- the vertical-limit theorem and normalized-defect compactness framework for
  supercongruence towers;
- the Banach fixed-point obstruction proving that the nonconstant A183068
  tower limit cannot extend continuously to all of $\mathbb Z_p$;
- the exact quadratic scaling and uniform equicontinuity at zero of the
  normalized A183068 defects;
- the full additive convolution distribution, sharp adjacent valuation, and
  Fourier mixing law for Cayley's \(2\times2\times2\) hyperdeterminant;
- the constant-spectrum convolution theorem and its determinant and Pfaffian
  supercongruence families;
- the exact USAMO isosceles-triangulation count and the resulting
  Hamming-scheme supercongruence with its first exceptional prime;
- the cubic $(\eta)$ congruence at the missing prime $3$;
- the Gaussian Lucas congruence modulo $p^3$ at every inert prime $p>5$; and
- the exact adjacent-scale valuation at the ramified prime $1+i$;
- the cubic angular residue for odd multiples of \(p-1\), producing a
  universal counterexample family to the printed constant-valuation
  conjecture;
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
| q-calculus and cyclotomic lifts | `verification/related/verify_q_calculus_supercongruence.py` |
| All-degree weighted-lift collisions | `verification/related/verify_weighted_lift_collision_synthesis.py` |
| Frobenius obstruction automata | `verification/related/verify_frobenius_obstruction_automata.py` |
| Finite-state Frobenius thermodynamics | `verification/related/verify_frobenius_transfer_thermodynamics.py` |
| All-precision unit-root lifting | `verification/related/verify_padic_valuation_expansion.py` |
| Fable Jacobian-counterexample counts | `verification/related/verify_jacobian_counterexample_counts.py` |
| Degree-four Jacobian collisions | `verification/related/verify_jacobian_degree_four.py` |
| Degree-five Jacobian collisions | `verification/related/verify_jacobian_degree_five.py` |
| Degree-six Jacobian collisions | `verification/related/verify_jacobian_degree_six.py` |
| Degree-seven Jacobian collisions | `verification/related/verify_jacobian_degree_seven.py` |
| Frobenius quotient identity | Coefficientwise algebraic proof; no checker required |
| Dwork and continuity boundaries | `verification/related/verify_dwork_boundaries.py` |
| p-adic Arzelà--Ascoli framework | Elementary ultrametric, contraction, and compactness proofs |
| Hyperdeterminant convolution tower | `verification/related/verify_hyperdeterminant_convolution.py` |
| Determinant and Pfaffian convolution towers | `verification/related/verify_determinant_pfaffian_convolution.py` |
| USAMO dyadic Hamming tower | `verification/related/verify_usamo_hamming_supercongruence.py` |
| Cubic $(\eta)$ | `verification/related/verify_eta_prime3.py` |
| Cooper level 11 | `verification/related/verify_cooper_level11.py` |
| Gaussian Frobenius twists | `verification/related/verify_gaussian_twists.py` |
| Gaussian power sums | `verification/related/verify_gaussian_power_sums.py` |
| Gaussian cubic angular residue | `verification/related/verify_gaussian_angular_residue.py` |
| Gaussian Wolstenholme network | `verification/related/verify_gaussian_wolstenholme.py` |
| Gaussian product isometry | `verification/related/verify_gaussian_product_isometry.py` |
| Gaussian product dynamics | `verification/related/experiment_gaussian_product_dynamics.py` (run separately; includes deeper finite-quotient tests) |
| Higher-degree box polynomials | `verification/related/verify_higher_degree_box_polynomial.py` |
| Gaussian Erdős--Moser boundary search | `verification/related/verify_gaussian_erdos_moser.py` |
| Exact GQ2 orientation lifts | `verification/related/verify_gq2_orientation_lifts.py` |

The binary $s_{18}$ file is a reduction rather than a completed theorem and
does not yet have a dedicated checker.

## Status discipline

Inclusion here means that a result is sufficiently coherent for Paul and other
specialists to inspect. It does not promote an unchecked candidate to a
theorem. Corrections, prior-art references, and failed cases should remain in
the repository so that the development history is auditable.

