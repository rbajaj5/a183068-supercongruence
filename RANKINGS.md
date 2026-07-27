# Mathematical research portfolio

This page scores every claim-level result in
[`RESULT_INDEX.md`](RESULT_INDEX.md). It uses the same Economist-style
portfolio rubric previously used in the broader proofs repository.

All scores run from 1 to 10:

- **Math-community value:** usefulness to the mathematical community if the
  result is correct, novel, and published. This is the primary ranking.
- **Deployment value:** potential usefulness in real software, standards,
  coding, or cryptographic systems. It is independent of mathematical value.
- **Novelty confidence:** present confidence that the contribution is not
  already in the literature.
- **Breadth:** reusability beyond the named problem.
- **Maturity:** proximity to a submission-quality mathematical result.
- **Cost remaining:** expected difficulty of proof checking, provenance work,
  and completion. A larger number means more work.

These are editorial estimates, not claims of priority, correctness, or peer
review. Close scores should be read as the same tier. Proof status remains
controlling: a high-value conjectural target is not thereby promoted to a
theorem.

## Completed drafts, theorems, and deductions

| Rank | ID and result | Math-community value | Deployment value | Novelty confidence | Breadth | Maturity | Cost remaining | Mathematical status |
| ---: | --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 1 | [GWL-TWO: ramified Gaussian prime theorem](related-results/GaussianLucasRamifiedTwoTheorem.md) | **8** | 2 | 8 | 8 | 7 | 5 | Complete proof candidate with machine-assisted audits and exact checks; specialist review and priority search pending. |
| 2 | [GWL-SCALE: Gaussian prime-power scaling](related-results/GaussianLucasPrimePowerTheorem.md) | **8** | 2 | 8 | 8 | 6 | 6 | Complete proof candidate with exact checks; independent review and priority search pending. |
| 3 | [JC-WL: all-degree weighted-lift collision theorem](related-results/WeightedLiftCollisionSynthesis.md) | **8** | 3 | 8 | 10 | 8 | 4 | Complete all-degree collision, genus-ladder, zeta-factor, and corrected-tower theorem with exact checks through generic degree seven; priority provisional. |
| 4 | [JC-AUTO: fixed-precision Frobenius obstruction automata](related-results/FrobeniusObstructionAutomata.md) | **8** | 3 | 7 | 10 | 9 | 3 | Complete theorem: every fixed-precision raw congruence language is eventually periodic with rational density; higher-precision genus-three and genus-six checks pass; priority provisional. |
| 5 | [JC5-FF: degree-five elliptic Frobenius packet](related-results/JacobianDegreeFiveEllipticFrobenius.md) | **8** | 3 | 8 | 9 | 8 | 4 | Complete collision-count, non-CM elliptic-factor, local-zeta, and corrected-tower theorem with direct extension-field checks; priority provisional. |
| 6 | [JC6-FF: degree-six genus-three Frobenius obstruction](related-results/JacobianDegreeSixGenusThree.md) | **8** | 3 | 8 | 9 | 8 | 4 | Complete genus-three local-\(L\)-polynomial, permanent raw obstruction, and corrected-tower theorem with exact extension-field and symbolic certificates; priority provisional. |
| 7 | [JC7-FF: degree-seven genus-six Frobenius automaton](related-results/JacobianDegreeSevenGenusSix.md) | **8** | 3 | 8 | 9 | 8 | 4 | Complete genus-six local-\(L\)-polynomial, period-\(156\) raw obstruction, and corrected-tower theorem with exact counts through \(\mathbb F_{5^6}\); priority provisional. |
| 8 | [FF-HYPERDET: hyperdeterminant Fourier packet](related-results/HyperdeterminantFourierSupercongruence.md) | **7** | 6 | 7 | 9 | 8 | 4 | Proved elementary theorem with exhaustive checks; total nondegenerate count is known, while the fiber refinement and paired supercongruence have provisional priority. |
| 9 | [JC4-FF: degree-four Frobenius obstruction](related-results/JacobianDegreeFourFrobeniusObstruction.md) | **7** | 3 | 8 | 8 | 8 | 3 | Complete collision-count, Artin-factor, obstruction, and corrected-supercongruence theorem with exact extension-field checks; priority provisional. |
| 10 | [JC-FF: finite-field arithmetic of the Fable counterexample](related-results/JacobianCounterexampleFiniteFieldCounts.md) | **7** | 2 | 8 | 7 | 8 | 3 | Complete elementary fiber-distribution, collision-zeta, and adjacent-valuation theorem with exact extension-field checks; priority provisional. |
| 11 | [QC-CUBIC: corrected cubic q-supercongruence](related-results/QCalculusCyclotomicSupercongruences.md#4-the-second-q-jet-and-a-corrected-cubic-theorem) | **7** | 1 | 5 | 9 | 8 | 4 | Complete deduction from Straub's q-Ljunggren theorem with exact polynomial checks; full priority search pending. |
| 12 | [LD-2: Landau-depth family](related-results/LandauDepthSupercongruenceSynthesis.md) | **7** | 1 | 5 | 9 | 7 | 4 | Complete proof candidate giving an infinite all-prime family; independent review pending. |
| 13 | [GL-CANON: canonical-product synthesis](related-results/GaussianLucasCanonicalProducts.md) | **7** | 3 | 6 | 9 | 7 | 5 | Proved structural lemma and synthesis; the split-prime program remains conjectural. |
| 14 | [GL-ISO: ramified Gaussian disk isometry](related-results/GaussianLucasCanonicalProducts.md#6-the-mixed-block-product-is-an-exact-disk-isometry) | **7** | 4 | 7 | 8 | 7 | 5 | Complete deduction with exact checks; conventional review and priority pending. |
| 15 | [LD-3: depth-three family](related-results/LandauDepthSupercongruenceSynthesis.md) | **7** | 1 | 5 | 8 | 7 | 4 | Complete proof candidate for an all-prime \(p^{3r}\) subfamily. |
| 16 | [GWL-LUCAS: rectangular Gaussian Lucas congruence](GAUSSIAN_LUCAS.md) | **7** | 2 | 7 | 7 | 6 | 5 | Complete unchecked draft for inert primes; exact \(p=3\) boundary included. |
| 17 | [QC-SQ: square-cyclotomic Landau lift](related-results/QCalculusCyclotomicSupercongruences.md#3-a-universal-square-cyclotomic-q-congruence) | **6** | 1 | 4 | 9 | 9 | 3 | Complete deduction from Clark's q-Babbage theorem; exact polynomial checks pass and the A183068 q-lift is explicit. |
| 18 | [A183068: all-prime supercongruence](PROOF.md) | **6** | 1 | 6 | 6 | 8 | 3 | Machine-audited proof draft of a named all-prime conjecture; specialist review pending. |
| 19 | [FF-PFAFF: Pfaffian bias and supercongruence](related-results/FiniteFieldPfaffianBiasSupercongruence.md) | **6** | 6 | 6 | 8 | 8 | 4 | Proved elementary theorem with exact checks; rank counts are classical and priority of the valuation formulation is provisional. |
| 20 | [GL-DYN: translated-product return filtration](related-results/GaussianProductDynamicsConjectures.md) | **6** | 6 | 7 | 7 | 7 | 5 | Complete local dynamical deduction; compatible global conjugacy remains open. |
| 21 | [ETA-3: cubic extension at \(p=3\)](related-results/EtaPrime3CubicExtension.md) | **6** | 1 | 6 | 5 | 6 | 5 | Complete unchecked draft addressing an exceptional prime in a published theorem. |
| 22 | [GWL-POWER: obstruction and corrected theorem](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture) | **6** | 1 | 7 | 5 | 6 | 5 | Complete unchecked correction and infinite failure mechanism for a printed conjecture. |
| 23 | [FQ-CT: first Frobenius quotient](related-results/FrobeniusQuotientConstantTerms.md) | **5** | 2 | 3 | 8 | 9 | 3 | Complete elementary theorem and boundary analysis; no novelty claim. |
| 24 | [FF-DET: determinant bias and supercongruence](related-results/FiniteFieldDeterminantBiasSupercongruence.md) | **5** | 7 | 4 | 8 | 9 | 3 | Proved elementary theorem; count is classical and priority of the sharp adjacent-extension formulation is provisional. |
| 25 | [BS-DWORK: Bhatt--Singh/Dwork period scaling](related-results/BhattSinghDworkPeriodSupercongruence.md) | **5** | 1 | 3 | 6 | 8 | 3 | Complete elementary deduction with exact checks; no novelty claim. |
| 26 | [GPS: Gaussian power sums](related-results/GaussianPowerSumConjectures.md) | **5** | 1 | 6 | 4 | 6 | 5 | Complete unchecked proofs of two formulas plus exact counterexamples to two broader claims. |
| 27 | [DWORK-BOUNDARY: failure of the proposed shortcut](related-results/FrobeniusQuotientConstantTerms.md#3-what-the-standard-dwork-theorem-does-not-supply-automatically) | **4** | 1 | 5 | 5 | 9 | 2 | Complete exact counterexamples delimiting the constant-term approach. |
| 28 | [GFT: Gaussian Frobenius twists](related-results/GaussianFrobeniusTwists.md) | **4** | 3 | 4 | 7 | 8 | 3 | Complete elementary deduction; literature priority unchecked. |
| 29 | [AA-TOWER: \(p\)-adic compactness framework](related-results/PadicArzelaAscoliSupercongruenceTowers.md) | **4** | 2 | 3 | 6 | 8 | 4 | Complete framework and obstruction; horizontal unit-shell interpolation remains open. |
| 30 | [BOX-d: higher-degree box polynomials](related-results/HigherDegreeFiniteFieldBoxPolynomials.md) | **4** | 2 | 2 | 8 | 7 | 3 | Complete unchecked theorem; likely classical infrastructure. |
| 31 | [GWL-POLY: Gaussian box polynomial](related-results/GaussianWolstenholmeCitationNetwork.md#2-the-polynomial-conjecture) | **4** | 1 | 6 | 4 | 6 | 5 | Complete unchecked finite-field polynomial formulas. |

## Reductions, computational targets, and synthesis

For open targets, Math-community value is conditional on completing the
stated target. Maturity records the work presently in the repository.

| Rank | ID and result | Math-community value | Deployment value | Novelty confidence | Breadth | Maturity | Cost remaining | Current mathematical status |
| ---: | --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 1 | [C11: Cooper level-11 exceptional primes](related-results/CooperLevel11RarePrimes.md) | **8** | 1 | 7 | 8 | 3 | 8 | Published Lucas foundation plus reproducible first-order targets; the rank-one Cartier identity remains unproved. |
| 2 | [s18-2: binary supercongruence reduction](related-results/S18TwoAdicReduction.md) | **7** | 1 | 7 | 6 | 3 | 8 | Substantial reduction to one sharpened scaling lemma; target not proved. |
| 3 | [GL-MAP: Gaussian literature and structural map](related-results/GaussianLucasLiteraturePuzzle.md) | **3** | 1 | 1 | 7 | 8 | 2 | Literature synthesis, not a theorem or novelty certificate. |
| 4 | [G-BOUNDARY: classical Gaussian obstructions](related-results/GaussianCitationNetworkBoundaryReport.md) | **3** | 1 | 4 | 4 | 6 | 5 | Rigorous reductions and bounded searches, not solutions of the classical problems. |

## Portfolio reading

The strongest current theorem-generating assets are now the linked
LD-2/LD-3 \(\rightarrow\) QC-SQ/QC-CUBIC line, the relative-invariant line
FF-DET \(\rightarrow\) FF-PFAFF \(\rightarrow\) FF-HYPERDET, and the
collision-zeta ladder
JC-WL \(\rightarrow\) JC-AUTO
\(\rightarrow\) \{JC-FF, JC4-FF, JC5-FF, JC6-FF, JC7-FF\}.
The degree-five rung is the first to replace finite quadratic monodromy by a
non-CM elliptic Frobenius packet; degree six is the first explicit
higher-genus packet and gives a permanent raw obstruction at \(p=13\).
Degree seven turns the obstruction into an exact period-\(156\) automaton.
JC-AUTO then proves that this finite-state behavior, including rational
densities at every fixed \(p\)-adic precision, is universal for the good
weighted-lift collision towers.
The q-calculus
line is especially broad: Landau depth predicts cyclotomic multiplicity,
while a quadratic pair-energy computes the complete second q-jet. The
Gaussian prime-power and ramified results retain the highest estimated
community value, but also carry more specialist review and priority risk.

Deployment scores are intentionally conservative. Finite-field Fourier bias
and local \(p\)-adic dynamics are structurally adjacent to coding and
cryptography, but this repository does not yet prove a protocol-level
security or performance improvement.
