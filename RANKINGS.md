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

## Dyadic maturity rule

The repository's [dyadic audit policy](DYADIC_POLICY.md) is part of the
scoring rubric. An all-prime claim cannot receive complete-proof maturity
while its \(p=2\) transfer, sign, ramification, or first-level boundary
remains unresolved. A binary exception is recorded as proof cost even when
every odd-prime case is complete. Conversely, a separate ramified
\(1+i\)-argument is scored as substantive work rather than as routine
bookkeeping.

## Executive allocation view

The detailed tables below are the controlling scorecard. For quick research
allocation, the portfolio currently has four tiers:

| Tier | Results | Recommended use of effort |
| --- | --- | --- |
| **A: specialist review now** | ZHANG-4, FRAMING-COUNTEREX, GWL-TWO, GWL-SCALE, JC-WL, JC5-FF, A183068 | Check proofs and priority before extending the statements |
| **B: broad theorem engines** | FROB-PACKET, JC-ORBIT, LD-2/LD-3, QC-SQ/QC-CUBIC, EULER-PRODUCT, BINOMIAL-POWER | Reuse on named conjectures and consolidate families |
| **C: exact infrastructure** | DYADIC-Q, DYADIC-WALSH, DYADIC-JOINT, BLACK-WALSH, HASH-MATROID, FQ-CT, WALK-FROB, GQ2-ABCOUNT, GQ2-DIHEDRAL, GQ2-QUATERNION, GQ2-MAXCYCLIC, GQ2-EXTRASPECIAL | Improve experiments, certification, source consolidation, and proof organization |
| **D: retained open targets** | C11, CAT-ODD, BALA-TOWERS, APERY-DEFECT, s18-2 | Spend proof effort only against the explicit unresolved lemma or obstruction |

Tier A has the highest estimated mathematical payoff. Tier C is deliberately
kept separate: these results can make the portfolio faster and more coherent
without increasing a supercongruence exponent.

## Completed drafts, theorems, and deductions

| Rank | ID and result | Math-community value | Deployment value | Novelty confidence | Breadth | Maturity | Cost remaining | Mathematical status |
| ---: | --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 1 | [GWL-TWO: ramified Gaussian prime theorem](related-results/GaussianLucasRamifiedTwoTheorem.md) | **8** | 2 | 8 | 8 | 7 | 5 | Complete proof candidate with machine-assisted audits and exact checks; specialist review and priority search pending. |
| 2 | [GWL-SCALE: Gaussian prime-power scaling](related-results/GaussianLucasPrimePowerTheorem.md) | **8** | 2 | 8 | 8 | 6 | 6 | Complete proof candidate with exact checks; independent review and priority search pending. |
| 3 | [JC-WL: all-degree weighted-lift collision theorem](related-results/WeightedLiftCollisionSynthesis.md) | **8** | 3 | 8 | 10 | 8 | 4 | Complete all-degree collision, genus-ladder, zeta-factor, and corrected-tower theorem with exact checks through generic degree seven; priority provisional. |
| 4 | [JC5-FF: degree-five elliptic Frobenius packet](related-results/JacobianDegreeFiveEllipticFrobenius.md) | **8** | 3 | 8 | 9 | 8 | 4 | Complete collision-count, non-CM elliptic-factor, local-zeta, and corrected-tower theorem with direct extension-field checks; priority provisional. |
| 5 | [FF-HYPERDET: hyperdeterminant Fourier and entropy packet](related-results/HyperdeterminantFourierSupercongruence.md) | **7** | 6 | 7 | 9 | 8 | 4 | Proved elementary theorem with exhaustive checks and an exact Rényi/KL/convolution profile; entropy identities are corollaries, while the fiber refinement and paired supercongruence have provisional priority. |
| 6 | [JC4-FF: degree-four Frobenius obstruction](related-results/JacobianDegreeFourFrobeniusObstruction.md) | **7** | 3 | 8 | 8 | 8 | 3 | Complete collision-count, Artin-factor, obstruction, and corrected-supercongruence theorem with exact extension-field checks; priority provisional. |
| 7 | [JC-FF: finite-field arithmetic of the Fable counterexample](related-results/JacobianCounterexampleFiniteFieldCounts.md) | **7** | 2 | 8 | 7 | 8 | 3 | Complete elementary fiber-distribution, collision-zeta, and adjacent-valuation theorem with exact extension-field checks; priority provisional. |
| 8 | [QC-CUBIC: corrected cubic q-supercongruence](related-results/QCalculusCyclotomicSupercongruences.md#4-the-second-q-jet-and-a-corrected-cubic-theorem) | **7** | 1 | 5 | 9 | 8 | 4 | Complete deduction from Straub's q-Ljunggren theorem with exact polynomial checks; full priority search pending. |
| 9 | [EULER-PRODUCT: colored product Frobenius tower](related-results/EulerProductGaussianTower.md) | **7** | 1 | 6 | 10 | 9 | 2 | Complete coefficientwise \(p^{2r}\) theorem for arbitrary integral multicolored Euler products with degree weight \(m^d\), \(d\ge1\); proves Bala's full quadratic product packet and Gaussian twists, while leaving the special A380290 cubic gain open. |
| 9 | [A008793-CUBE: cube-plane-partition tower](related-results/A008793CubePlanePartitionTower.md) | **7** | 1 | 6 | 7 | 9 | 2 | Complete elementary proof candidate for a named nonlinear all-prime \(p^{4r}\) conjecture; exact product splitting and reduced-residue blocks include the sharp binary boundary, with 455 exact checks. |
| 9 | [LD-2: Landau-depth family](related-results/LandauDepthSupercongruenceSynthesis.md) | **7** | 1 | 5 | 9 | 7 | 4 | Complete proof candidate giving an infinite all-prime family; independent review pending. |
| 10 | [GL-CANON: canonical-product synthesis](related-results/GaussianLucasCanonicalProducts.md) | **7** | 3 | 6 | 9 | 7 | 5 | Proved structural lemma and synthesis; the split-prime program remains conjectural. |
| 11 | [GL-ISO: ramified Gaussian disk isometry](related-results/GaussianLucasCanonicalProducts.md#6-the-mixed-block-product-is-an-exact-disk-isometry) | **7** | 4 | 7 | 8 | 7 | 5 | Complete deduction with exact checks; conventional review and priority pending. |
| 12 | [LD-3: depth-three family](related-results/LandauDepthSupercongruenceSynthesis.md) | **7** | 1 | 5 | 8 | 7 | 4 | Complete proof candidate for an all-prime \(p^{3r}\) subfamily. |
| 13 | [GWL-LUCAS: rectangular Gaussian Lucas congruence](GAUSSIAN_LUCAS.md) | **7** | 2 | 7 | 7 | 6 | 5 | Complete unchecked draft for inert primes; exact \(p=3\) boundary included. |
| 14 | [QC-SQ: square-cyclotomic Landau lift](related-results/QCalculusCyclotomicSupercongruences.md#3-a-universal-square-cyclotomic-q-congruence) | **6** | 1 | 4 | 9 | 9 | 3 | Complete deduction from Clark's q-Babbage theorem; exact polynomial checks pass and the A183068 q-lift is explicit. |
| 14 | [FROB-PACKET: arithmetic Frobenius packet framework](related-results/ArithmeticFrobeniusPacketFramework.md) | **6** | 2 | 3 | 10 | 9 | 2 | Complete local-to-global, aggregation, closure, finite-field orbit, and arbitrary-depth budget framework routing all 110 Bala records; broad infrastructure rather than a claim that the census is solved. |
| 15 | [A183068: all-prime supercongruence](PROOF.md) | **6** | 1 | 6 | 6 | 8 | 3 | Machine-audited proof draft of a named all-prime conjecture; specialist review pending. |
| 15 | [CYCLOTOMIC-PAIR: A228960/A350383 polynomial towers](related-results/CyclotomicCoefficientPairTheorem.md) | **6** | 1 | 5 | 6 | 9 | 2 | Complete elementary proof candidate for two named OEIS conjectures, strengthened coefficientwise and at Gaussian twists; broader cyclotomic principle and priority remain open. |
| 15 | [BALA-ODD: A375178 prime-level odd-power family](related-results/BalaOeisSupercongruenceQueue.md#3-the-full-prime-level-odd-power-theorem-for-a375178) | **6** | 1 | 6 | 8 | 7 | 3 | Complete elementary proof of an infinite named OEIS conjecture family; 56 exact checks pass, with priority and independent review pending. |
| 15 | [A365029-R12: first two adjacent levels](related-results/A365029FirstTwoLevels.md) | **6** | 1 | 6 | 7 | 8 | 3 | Complete elementary proof of the \(r=1,2\) cases of a named OEIS \(p^{3r}\) tower; shifted transfer and the two-digit harmonic cancellation are proved, with 67,310 exact checks. |
| 15 | [BALA-BINOMIAL: A357509/A357568 families](related-results/BinomialQuotientCancellation.md#4-the-complete-a357509-two-parameter-family) | **6** | 1 | 6 | 9 | 8 | 3 | One quotient-cancellation theorem proves the full two-parameter A357509 conjecture for \(p\ge5\) and the A357568 power family for every odd prime; 2,192 exact checks include sharp cases in both families. |
| 15 | [APERY-ODD-MOMENT: A357510 and A357512 prime boundary](related-results/AperyOddMomentPrimeClassification.md) | **6** | 1 | 6 | 8 | 8 | 3 | One local \(p^4\) expansion proves A357510 and exactly classifies every exceptional prime in the higher odd-moment family; the composite A357512 statement remains open. |
| 15 | [A288470-ODD: double-binomial tower](related-results/A288470OddPrimeTower.md) | **6** | 1 | 5 | 7 | 8 | 3 | Complete proof candidate for the named \(p^{2r}\) tower, strengthened from \(p\ge5\) to every odd prime; \(p=2\) fails at the second level. |
| 15 | [A141057-MULTI: multinomial-power Frobenius tower](related-results/MultinomialPowerFrobeniusTowers.md) | **6** | 1 | 6 | 9 | 8 | 3 | Complete elementary proof candidate closing A141057, adding $p=3$, and proving a coefficientwise theorem for arbitrary dimension and exponent; 12,036 exact checks pass. |
| 15 | [ODD-UNIT-BLOCK: A091527/A262732 family](related-results/OddUnitBlockFrobeniusTowers.md) | **6** | 1 | 6 | 9 | 8 | 3 | Complete elementary proof candidate closing two named towers through one odd-unit harmonic theorem for every $m\ge2$; 806 exact checks pass and the small-prime boundary is sharp. |
| 15 | [DIXON-LEGENDRE: A275652/A275654 family](related-results/DixonLegendreHalfBinomialTowers.md) | **6** | 1 | 6 | 9 | 8 | 3 | Complete elementary proof candidate closing two named towers through one Dixon evaluation and a half-binomial unit-block theorem for every $a\ge3$; 961 exact checks pass. |
| 15 | [A364173-INTEGRAL: integrality and cubic tower](related-results/A364173IntegralHalfBinomialTower.md) | **6** | 1 | 7 | 8 | 8 | 3 | Complete elementary proof candidate resolving two explicit conjectures on one record: global integrality and the full $p^{3r}$ tower; 487,211 exact checks pass. |
| 15 | [A049505-SPP: three symmetric-plane-partition congruences](related-results/A049505SymmetricPlanePartitionCongruences.md) | **6** | 1 | 5 | 6 | 9 | 2 | Complete elementary proof of all three named congruences through the stronger evaluation \(a(p^r)\equiv2^{(p^r+1)/2}\pmod {p^3}\); 229 exact checks pass and priority is unclaimed. |
| 16 | [ZHANG-4: exact four-matrix counterexample](related-results/ZhangFourMatrixCounterexample.md) | **6** | 2 | 6 | 5 | 8 | 3 | Complete dimension-minimal counterexample with an exact positive-definite interval and rational-arithmetic checker; the parent four-factor problem remains separate and priority is provisional. |
| 16 | [FF-PFAFF: Pfaffian bias and supercongruence](related-results/FiniteFieldPfaffianBiasSupercongruence.md) | **6** | 6 | 6 | 8 | 8 | 4 | Proved elementary theorem with exact checks; rank counts are classical and priority of the valuation formulation is provisional. |
| 17 | [GL-DYN: translated-product return filtration](related-results/GaussianProductDynamicsConjectures.md) | **6** | 6 | 7 | 7 | 7 | 5 | Complete local dynamical deduction; compatible global conjugacy remains open. |
| 18 | [ETA-3: cubic extension at \(p=3\)](related-results/EtaPrime3CubicExtension.md) | **6** | 1 | 6 | 5 | 6 | 5 | Complete unchecked draft addressing an exceptional prime in a published theorem. |
| 19 | [GWL-POWER: obstruction and corrected theorem](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture) | **6** | 1 | 7 | 5 | 6 | 5 | Complete unchecked correction and infinite failure mechanism for a printed conjecture. |
| 20 | [FQ-CT: first Frobenius quotient](related-results/FrobeniusQuotientConstantTerms.md) | **5** | 2 | 3 | 8 | 9 | 3 | Complete elementary theorem and boundary analysis; no novelty claim. |
| 20 | [JC-ORBIT: primitive collision-orbit criterion](related-results/JacobianCollisionEulerOrbitBridge.md) | **5** | 2 | 3 | 9 | 9 | 2 | Complete Dold/Gauss synthesis: a \(p^{hr}\) tower is exactly \(p^{(h-1)r}\)-divisibility of primitive orbit multiplicities; the degree-three Jacobian collision scheme is proved sharp only at the ordinary Gauss level. |
| 15 | [FRAMING-CUBIC: six coefficient-power towers](related-results/CoefficientFramingCubicTower.md) | **6** | 1 | 6 | 10 | 8 | 3 | Complete elementary Cartier proof closing six named OEIS records, with 5,473 exact checks; a counterexample prevents reliance on the previously cited framing theorem, so specialist review and priority work remain. |
| 16 | [FRAMING-COUNTEREX: rational-framing boundary](related-results/RationalFramingCounterexample.md) | **6** | 1 | 7 | 5 | 9 | 2 | Exact rational counterexample to both principal congruences of a cited framing theorem as printed; it corrects provenance without affecting the independent six-record proof. |
| 20 | [COEFF-POWER-GAUSS: integral roots and universal baseline](related-results/CoefficientPowerGaussBaseline.md) | **5** | 1 | 3 | 9 | 9 | 2 | Complete elementary theorem proving three coefficient-root integrality claims, an exact Lagrange bridge, and the sharp universal all-prime \(p^r\) tower; the two named cubic refinements remain open. |
| 20 | [STRAUB-5: prime-five multivariate Apéry packet](related-results/StraubPrimeFiveCoefficientPacket.md) | **5** | 1 | 6 | 8 | 8 | 2 | Complete boundary extension of Straub's published theorem from \(p>5\) to \(p\geq5\), closing three named OEIS towers after exact coefficient matching; independent review pending. |
| 20 | [MODULAR-PRIME: seven modular-product OEIS records](related-results/ModularProductPrimeCoefficientPacket.md) | **5** | 1 | 4 | 9 | 9 | 2 | Complete elementary packet proving five prime-level claims and three full quadratic towers, plus four rigorous baselines; paired-product follow-ons complete the route and priority is unclaimed. |
| 20 | [A229452-ROOT: parameterized coefficient root](related-results/A229452CoefficientRootBaseline.md) | **5** | 1 | 4 | 8 | 9 | 3 | Complete proof of the all-\(m\) integrality conjecture, exact Lagrange bridge, and all-prime \(p^r\) baselines for both source families; the named cubic towers remain open. |
| 20 | [DYADIC-Q: restored binary hypercube tower](related-results/DyadicHypercubeDefect.md) | **6** | 2 | 3 | 10 | 9 | 2 | Complete sharp law \(e(1)=1\), \(e(r)=2r\) for \(r\ge2\), exact first-level quadratic-defect classification, and an A380290-specific binary theta obstruction; standard \(2\)-derivation infrastructure, with priority provisional. |
| 21 | [EULER-LOCAL: complete Gaussian local table](related-results/EulerProductGaussianLocalTable.md) | **5** | 1 | 2 | 10 | 9 | 1 | Complete split/inert/ramified prime-ideal corollary of EULER-PRODUCT and DYADIC-Q; useful synthesis and exact local checks, but not a new proof engine. |
| 21 | [FF-DET: determinant bias and supercongruence](related-results/FiniteFieldDeterminantBiasSupercongruence.md) | **5** | 7 | 4 | 8 | 9 | 3 | Proved elementary theorem; count is classical and priority of the sharp adjacent-extension formulation is provisional. |
| 22 | [BS-DWORK: Bhatt--Singh/Dwork period scaling](related-results/BhattSinghDworkPeriodSupercongruence.md) | **5** | 1 | 3 | 6 | 8 | 3 | Complete elementary deduction with exact checks; no novelty claim. |
| 23 | [BINOMIAL-POWER: all-prime polynomial tower](related-results/BinomialPowerFrobeniusTheorem.md) | **5** | 1 | 3 | 9 | 9 | 2 | Complete theorem for every exponent \(m\ge3\), with prime-specific multiplicity bonus and split, inert, and ramified Gaussian specializations; priority not established. |
| 23 | [GPS: Gaussian power sums](related-results/GaussianPowerSumConjectures.md) | **5** | 1 | 6 | 4 | 6 | 5 | Complete unchecked proofs of two formulas plus exact counterexamples to two broader claims. |
| 23 | [A333-COSTER: complete A333593 tower](related-results/BalaOeisSupercongruenceQueue.md#4-the-a333593-tower-is-a-coster-corollary) | **5** | 1 | 2 | 6 | 9 | 1 | Named OEIS tower closed by an exact reduction to Coster and Jacobsthal--Kazandzidis; likely a previously implicit corollary rather than a new mechanism. |
| 23 | [A364506-LAURENT: complete row tower](related-results/BinomialQuotientCancellation.md#2-application-to-a364506) | **5** | 1 | 3 | 8 | 9 | 2 | Every row of a named OEIS array is closed by one integral Laurent-binomial theorem; mathematically useful breadth, but the mechanism is a clean reduction to classical scaling. |
| 24 | [DWORK-BOUNDARY: failure of the proposed shortcut](related-results/FrobeniusQuotientConstantTerms.md#3-what-the-standard-dwork-theorem-does-not-supply-automatically) | **4** | 1 | 5 | 5 | 9 | 2 | Complete exact counterexamples delimiting the constant-term approach. |
| 25 | [GFT: Gaussian Frobenius twists](related-results/GaussianFrobeniusTwists.md) | **4** | 3 | 4 | 7 | 8 | 3 | Complete elementary deduction; literature priority unchecked. |
| 25 | [WALK-FROB: finite lattice-walk Frobenius congruences](related-results/LatticeWalkFrobeniusCongruences.md) | **4** | 3 | 2 | 8 | 9 | 2 | Complete trace/Euler-product proof with Gaussian and Eisenstein local tables and ramified uniformizer bounds; unramified theorem is standard infrastructure, and no SAW-to-SLE arithmetic implication is claimed. |
| 25 | [BLACK-WALSH: planar-noise Walsh congruence](related-results/BlackNoiseWalshCongruences.md) | **4** | 4 | 3 | 8 | 9 | 2 | Complete lacunary-spectrum theorem giving a \(3r-2\) congruence at every Gaussian prime for complement-odd finite noise observables; black-noise scaling limits are cited context, not proof input. |
| 25 | [BALA-BOUNDARY: strengthened A365029 boundary family](related-results/BalaOeisSupercongruenceQueue.md#2-a-stronger-boundary-theorem-for-a365029) | **4** | 1 | 6 | 7 | 8 | 2 | Complete termwise proof strengthening a named OEIS conjecture to modulus \(p^{A+B}\); 390 exact checks pass. |
| 25 | [DYADIC-WALSH: matching spectrum of the binary defect](related-results/DyadicHypercubeWalshAnalysis.md) | **4** | 3 | 2 | 8 | 10 | 1 | Complete exact Boolean-Fourier classification of each defect coordinate, including face counts and noise stability; useful for CSP verification, but based on classical matching-quadratic analysis. |
| 25 | [DYADIC-JOINT: joint spectrum of the binary defect](related-results/DyadicHypercubeJointSpectrum.md) | **4** | 4 | 2 | 9 | 10 | 1 | Exact joint model counts, collision probability, chi-squared distance, support bound, and total-variation certificate from alternating convolution ranks; classical quadratic-form Fourier analysis. |
| 26 | [AA-TOWER: \(p\)-adic compactness framework](related-results/PadicArzelaAscoliSupercongruenceTowers.md) | **4** | 2 | 3 | 6 | 8 | 4 | Complete framework and obstruction; horizontal unit-shell interpolation remains open. |
| 26 | [HASH-MATROID: exact linear measurement law](related-results/MatroidHashingLaw.md) | **4** | 6 | 2 | 9 | 9 | 1 | Complete exact application of the classical Crapo--Rota Critical Theorem to finite Fourier supports; gives measurement certificates for dyadic defect spectra but no stronger \(p\)-adic modulus. |
| 27 | [BOX-d: higher-degree box polynomials](related-results/HigherDegreeFiniteFieldBoxPolynomials.md) | **4** | 2 | 2 | 8 | 7 | 3 | Complete unchecked theorem; likely classical infrastructure. |
| 28 | [GWL-POLY: Gaussian box polynomial](related-results/GaussianWolstenholmeCitationNetwork.md#2-the-polynomial-conjecture) | **4** | 1 | 6 | 4 | 6 | 5 | Complete unchecked finite-field polynomial formulas. |
| 29 | [CDE-DEFECT: Chowla--Dwork--Evans split-prime defect](related-results/ChowlaDworkEvansSplitDefect.md) | **4** | 1 | 1 | 6 | 10 | 1 | Exact reformulation of a published modulo-\(p^2\) theorem, with 1,125 exact regression checks and no novelty claim. |
| 30 | [GQ2-ABCOUNT: finite abelian \(2\)-target counts](related-results/GQ2FiniteAbelianCounts.md) | **4** | 1 | 1 | 6 | 10 | 1 | Complete closed formula solving the finite abelian \(2\)-group subcase of Roe--Turturean's explicit-counting question; elementary from their abelianization and no novelty claim. |
| 30 | [GQ2-DIHEDRAL: exact dihedral \(2\)-target counts](related-results/GQ2DihedralCounts.md) | **4** | 1 | 1 | 6 | 10 | 1 | Complete direct relator calculation for the first nonabelian target family; existing enumeration literature makes this a new derivation rather than a priority claim. |
| 30 | [GQ2-QUATERNION: exact generalized-quaternion \(2\)-target counts](related-results/GQ2QuaternionCounts.md) | **4** | 1 | 1 | 6 | 10 | 1 | Complete direct relator calculation with exceptional \(Q_8,Q_{16}\) layers and a stable all-orders formula; published enumeration exists, so no priority claim. |
| 30 | [GQ2-MAXCYCLIC: semidihedral and modular target counts](related-results/GQ2MaximalCyclicCounts.md) | **4** | 1 | 1 | 7 | 10 | 1 | Complete direct relator derivation and exact certificate for both remaining maximal-cyclic families; Ito--Yamagishi already published the enumeration. |
| 30 | [GQ2-EXTRASPECIAL: higher extraspecial rank obstruction](related-results/GQ2ExtraspecialObstruction.md) | **4** | 1 | 1 | 7 | 10 | 1 | Complete generator-rank obstruction showing that no extraspecial group of order at least \(32\) is a quotient; useful target triage rather than a new enumeration. |
| 30 | [GQ2-ORIENT: Roe--Turturean exact orientation lift](related-results/GQ2OrientationLifts.md) | **4** | 2 | 3 | 6 | 9 | 1 | Complete elementary sharpening: the compatible finite classes determine one nonintegral \(2\)-adic exponent; no correction or novelty claim. |
| 31 | [GQ2-TWIST: dyadic HNN Dehn-twist tower and affine filtration](related-results/GQ2OrientationLifts.md#theorem-exact-pro-2-dehn-twist-tower) | **4** | 3 | 3 | 7 | 9 | 1 | Complete exact \(\mathbb Z_2\)-parameterized outer-twist tower and affine commutator-depth theorem; scope is the Roe--Turturean follow-on. |
| 32 | [QUADRATIC-GAUSSIAN: A005259/A333592-family polynomial towers](related-results/QuadraticGaussianQueueTheorem.md) | **3** | 1 | 1 | 6 | 9 | 1 | Complete all-prime coefficientwise \(p^{2r}\) deduction for A005259 and every positive parameter pair in the A333592 family; classical-scaling infrastructure, not the stronger cubic conjecture. |
| 32 | [GQ2-H2: mixed dyadic affine obstruction](related-results/DyadicAffineMixedCohomology.md) | **3** | 1 | 1 | 7 | 9 | 1 | Complete continuous-cohomology calculation and explicit parity-classified extension; linear proxy only and no novelty claim. |
| 33 | [GQ2-SAMPLE: exact sampling on the dyadic Dehn-twist shadow](related-results/DyadicDehnTwistSampler.md) | **3** | 5 | 2 | 6 | 9 | 1 | Complete optimal lift-bit sampler and exact coordinate-refresh spectrum; classical probability applied to the Roe--Turturean quotient. |
| 34 | [GQ2-CAYLEY: fixed-generator dyadic Dehn-twist walk](related-results/DyadicDehnTwistCayleyWalk.md) | **3** | 5 | 2 | 6 | 9 | 1 | Complete elementary spectral-gap estimate for an explicit affine Cayley walk; no priority claim. |
| 35 | [GQ2-GRAMMAR: affine twist grammar and almost periodicity](related-results/DyadicTwistGrammarAlmostPeriodicity.md) | **3** | 3 | 1 | 7 | 8 | 2 | Complete normal-form theorem plus a direct finite-group almost-periodicity specialization; no novelty claim. |
| 36 | [GQ2-SHELL: dyadic Dehn-twist conjugacy moments](related-results/DyadicDehnTwistConjugacyMoments.md) | **3** | 3 | 1 | 6 | 10 | 1 | Complete elementary affine-quotient theorem and exact adjacent depth-moment identity; no novelty claim. |

## Reductions, computational targets, and synthesis

For open targets, Math-community value is conditional on completing the
stated target. Maturity records the work presently in the repository.

| Rank | ID and result | Math-community value | Deployment value | Novelty confidence | Breadth | Maturity | Cost remaining | Current mathematical status |
| ---: | --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 1 | [C11: Cooper level-11 exceptional primes](related-results/CooperLevel11RarePrimes.md) | **8** | 1 | 7 | 8 | 3 | 8 | Published Lucas foundation plus reproducible first-order targets; the rank-one Cartier identity remains unproved. |
| 2 | [CAT-ODD: Catalan ballot-power supercongruences](related-results/CatalanBallotPowerSupercongruenceAudit.md) | **7** | 1 | 5 | 8 | 2 | 8 | Three named \(p^{3r}\) conjectures unified as one computational target; sharp \(p=2,3\) refinements are experimental. |
| 2 | [BALA-TOWERS: higher A365029 and A375178 towers](related-results/BalaOeisSupercongruenceQueue.md#5-exact-status-of-the-remaining-first-queue) | **7** | 1 | 6 | 8 | 6 | 4 | Two named OEIS prime-power targets: A365029 is now proved through \(r=2\) and reduced above it to iterating a two-digit block lemma; Coster supplies the cubic baseline beneath A375178. |
| 3 | [s18-2: binary supercongruence reduction](related-results/S18TwoAdicReduction.md) | **7** | 1 | 7 | 6 | 3 | 8 | Substantial reduction to one sharpened scaling lemma; target not proved. |
| 3 | [APERY-DEFECT: five-record enhanced packet](related-results/AperyRankOneDefectPacket.md) | **7** | 1 | 5 | 8 | 6 | 6 | Exact reduction of five named OEIS records and two nonlinear companions to three linear Apéry defect congruences; strong consolidation, but the core arithmetic remains open. |
| 5 | [GBQ-MAP: Gaussian routing of the Bala census](related-results/BalaGaussianGeneralizationMap.md) | **4** | 1 | 1 | 10 | 9 | 3 | Exhaustive routing of 110 records into five proof architectures; high portfolio breadth, but not a theorem or novelty certificate. |
| 6 | [GL-MAP: Gaussian literature and structural map](related-results/GaussianLucasLiteraturePuzzle.md) | **3** | 1 | 1 | 7 | 8 | Literature synthesis, not a theorem or novelty certificate. |
| 7 | [G-BOUNDARY: classical Gaussian obstructions](related-results/GaussianCitationNetworkBoundaryReport.md) | **3** | 1 | 4 | 4 | 6 | 5 | Rigorous reductions and bounded searches, not solutions of the classical problems. |

## Portfolio reading

The strongest current theorem-generating assets are now the linked
FROB-PACKET \(\rightarrow\) LD-2/LD-3
\(\rightarrow\) QC-SQ/QC-CUBIC line, the relative-invariant line
FF-DET \(\rightarrow\) FF-PFAFF \(\rightarrow\) FF-HYPERDET, and the
collision-zeta ladder
JC-WL \(\rightarrow\) \{JC-FF, JC4-FF, JC5-FF\}, together with the
orthogonal JC-ORBIT dictionary that converts multiplicative index towers
into primitive closed-collision divisibility.
The degree-five rung is the first to replace finite quadratic monodromy by a
non-CM elliptic Frobenius packet. The q-calculus
line is especially broad: Landau depth predicts cyclotomic multiplicity,
while a quadratic pair-energy computes the complete second q-jet. The
colored Euler-product theorem is the broadest completed Bala-queue closure:
one occupation-stratum argument proves the whole quadratic product packet.
Its Gaussian specialization is sharp, while the untwisted \(d=2\) cubic
gain remains a distinct target. The
Gaussian prime-power and ramified results retain the highest estimated
community value, but also carry more specialist review and priority risk.

Deployment scores are intentionally conservative. Finite-field Fourier bias
and local \(p\)-adic dynamics are structurally adjacent to coding and
cryptography, but this repository does not yet prove a protocol-level
security or performance improvement.
