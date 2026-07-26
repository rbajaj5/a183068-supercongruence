# Related supercongruence program

This directory contains the complete follow-on drafts that grew out of the
A183068 proof. It is organized as a mathematical reading queue, not as a claim
that every file has the same level of verification.

The common mechanism is:

1. split a finite sum into $p$-adic valuation strata;
2. use digit carries or finite-field symmetry to make low strata vanish;
3. transfer the surviving terms by scaling, Frobenius, or translation; and
4. measure whether the transfer error supplies the required power of $p$.

## Recommended reading order

| Order | Note | Connection to A183068 | Status |
| ---: | --- | --- | --- |
| 1 | [Landau-depth synthesis](LandauDepthSupercongruenceSynthesis.md) | Extracts the A183068 carry-and-scaling proof into a computable theorem; contains an infinite all-prime $p^{2r}$ family and an all-prime $p^{3r}$ subfamily | Complete unchecked draft; highest direct-generalization priority |
| 2 | [Gaussian Frobenius twists](GaussianFrobeniusTwists.md) | Shows that discard-and-rescale proofs lift to roots-of-unity weights; specializes A183068 to a Gaussian split/inert congruence | Complete elementary deduction; priority unchecked |
| 3 | [Cubic $(\eta)$ congruence at $p=3$](EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to fill a small-prime gap in a published theorem | Complete unchecked draft |
| 4 | [Gaussian Wolstenholme citation network](GaussianWolstenholmeCitationNetwork.md) | Replaces scaling by translation-invariant Gaussian residue blocks | Three major candidate results with exact certificates; independent review required |
| 5 | [Gaussian canonical-product synthesis](GaussianLucasCanonicalProducts.md) | Extracts the dominant logarithmic-moment mechanism, proves that the normalized ramified block is a bijective disk isometry, and extends it to a first-moment-dominance chamber | Proved local theorem plus open research program |
| 6 | [Gaussian product dynamics](GaussianProductDynamicsConjectures.md) | Tests translated disk isometries on every finite ramified quotient and conjectures an exact return-valuation law and conjugacy to addition | Exact computational conjectures; 318 all-unit quotient maps plus deeper tests |
| 7 | [Gaussian Lucas literature puzzle](GaussianLucasLiteraturePuzzle.md) | Connects the product theorem to Dwork/Frobenius theory, generalized factorials, and compatible $p$-adic dynamics | Literature map; bridges ranked by strength |
| 8 | [Gaussian power-sum conjectures](GaussianPowerSumConjectures.md) | Uses fourth-root and affine-orbit cancellation in the same residue-stratification spirit | Two formula proofs and exact counterexamples; independent review required |
| 9 | [Higher-degree finite-field box polynomials](HigherDegreeFiniteFieldBoxPolynomials.md) | Generalizes the Gaussian polynomial factorization to every finite-field degree | Complete elementary theorem; likely classical infrastructure |
| 10 | [Binary $s_{18}$ reduction](S18TwoAdicReduction.md) | Isolates the exact sharpened scaling lemma still needed at $p=2$ | Substantial reduction, not a proof |
| 11 | [Gaussian citation-network boundary report](GaussianCitationNetworkBoundaryReport.md) | Records rigorous limits of the Gaussian search, including Erdős--Moser reductions | Reduction and bounded search, not a global solution |
| 12 | [Cooper level-11 rare primes](CooperLevel11RarePrimes.md) | Tests another published supercongruence family and isolates its first obstruction | Computational result and structural clue |

## Strongest present claims

The directory currently contains five especially reviewable claims:

- the Landau-depth theorem unifying termwise vanishing with multinomial
  transfer;
- the cubic $(\eta)$ congruence at the missing prime $3$;
- the Gaussian Lucas congruence modulo $p^3$ at every inert prime $p>5$; and
- the exact adjacent-scale valuation at the ramified prime $1+i$; and
- an infinite counterexample family plus corrected theorem for a printed
  Gaussian reciprocal-power conjecture.

All four are research drafts. Exact computation supports them, but none should
be described as peer reviewed.

## Verification

Run every included checker from the repository root:

```text
python verification/run_all.py
```

The individual correspondence is:

| Note | Checker |
| --- | --- |
| Landau depth | `verification/related/verify_landau_supercongruence.py` |
| Cubic $(\eta)$ | `verification/related/verify_eta_prime3.py` |
| Cooper level 11 | `verification/related/verify_cooper_level11.py` |
| Gaussian Frobenius twists | `verification/related/verify_gaussian_twists.py` |
| Gaussian power sums | `verification/related/verify_gaussian_power_sums.py` |
| Gaussian Wolstenholme network | `verification/related/verify_gaussian_wolstenholme.py` |
| Gaussian product isometry | `verification/related/verify_gaussian_product_isometry.py` |
| Gaussian product dynamics | `verification/related/experiment_gaussian_product_dynamics.py` (run separately; computational conjecture) |
| Higher-degree box polynomials | `verification/related/verify_higher_degree_box_polynomial.py` |
| Gaussian Erdős--Moser boundary search | `verification/related/verify_gaussian_erdos_moser.py` |

The binary $s_{18}$ file is a reduction rather than a completed theorem and
does not yet have a dedicated checker.

## Status discipline

Inclusion here means that a result is sufficiently coherent for Paul and other
specialists to inspect. It does not promote an unchecked candidate to a
theorem. Corrections, prior-art references, and failed cases should remain in
the repository so that the development history is auditable.

