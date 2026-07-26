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
| 1 | [Landau-depth synthesis](LandauDepthSupercongruenceSynthesis.md) | Extracts the A183068 carry-and-scaling proof into a computable theorem; contains an infinite all-prime $p^{2r}$ family and an all-prime $p^{3r}$ subfamily | Complete proof candidate; internal recheck passed, independent review pending |
| 2 | [Frobenius quotients of constant-term sequences](FrobeniusQuotientConstantTerms.md) | Proves the universal first-order expansion, identifies the exact rank-one condition behind the Cooper law, and gives exact counterexamples to two proposed Dwork shortcuts | Complete elementary theorem; Dwork boundaries certified |
| 3 | [p-adic Arzelà--Ascoli framework](PadicArzelaAscoliSupercongruenceTowers.md) | Proves the vertical limit supplied by A183068, uses the Banach contraction $x\mapsto px$ to rule out a global continuous interpolation, and proves uniform quadratic contraction of every normalized defect at zero | Complete elementary framework and obstruction; unit-shell estimate open |
| 4 | [Gaussian Frobenius twists](GaussianFrobeniusTwists.md) | Shows that discard-and-rescale proofs lift to roots-of-unity weights; specializes A183068 to a Gaussian split/inert congruence | Complete elementary deduction; priority unchecked |
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
| Frobenius quotient identity | Coefficientwise algebraic proof; no checker required |
| Dwork and continuity boundaries | `verification/related/verify_dwork_boundaries.py` |
| p-adic Arzelà--Ascoli framework | Elementary ultrametric, contraction, and compactness proofs |
| Cubic $(\eta)$ | `verification/related/verify_eta_prime3.py` |
| Cooper level 11 | `verification/related/verify_cooper_level11.py` |
| Gaussian Frobenius twists | `verification/related/verify_gaussian_twists.py` |
| Gaussian power sums | `verification/related/verify_gaussian_power_sums.py` |
| Gaussian Wolstenholme network | `verification/related/verify_gaussian_wolstenholme.py` |
| Gaussian product isometry | `verification/related/verify_gaussian_product_isometry.py` |
| Gaussian product dynamics | `verification/related/experiment_gaussian_product_dynamics.py` (run separately; includes deeper finite-quotient tests) |
| Higher-degree box polynomials | `verification/related/verify_higher_degree_box_polynomial.py` |
| Gaussian Erdős--Moser boundary search | `verification/related/verify_gaussian_erdos_moser.py` |

The binary $s_{18}$ file is a reduction rather than a completed theorem and
does not yet have a dedicated checker.

## Status discipline

Inclusion here means that a result is sufficiently coherent for Paul and other
specialists to inspect. It does not promote an unchecked candidate to a
theorem. Corrections, prior-art references, and failed cases should remain in
the repository so that the development history is auditable.

