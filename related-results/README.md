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

The [sofic finite-approximation boundary note](SoficFiniteApproximationBoundary.md)
records one adjacent methodological analogy without treating it as a
supercongruence theorem. It accepts the August 2026 construction as an
external Lean-certified theorem and extracts only a proof-search analogy from
its expander-component matching argument.

The [ten-advances transfer ledger](OpenAITenAdvancesTransferLedger.md) routes
all ten results through the repository's proof, experiment, and audit lanes.
It records two direct arithmetic transfers, one reusable conservation lemma,
and explicit non-transfer boundaries for the remaining results. The
[group-ring Gauss boundary](NonSoficGroupRingGaussBoundary.md) proves that
prime-order torsion, rather than soficity, exactly controls the universal
coefficient-return congruence.

The [Ehrhart--Newton prime cutoff](EhrhartNewtonPrimeCutoff.md) is the direct
arithmetic deduction extracted from the collection. It turns the accepted
sharp volume theorem into a finite exceptional-prime bound for
full-dimensional exponent-rank degeneration; it does not claim a stronger
supercongruence exponent.

## Recommended reading order

| Order | Note | Connection to A183068 | Status |
| ---: | --- | --- | --- |
| 0 | [Repository-wide dyadic audit policy](../DYADIC_POLICY.md) | Defines what must be checked before any all-prime or ramified theorem is called complete | Governing proof and ranking policy |
| 1 | [Landau-depth synthesis](LandauDepthSupercongruenceSynthesis.md) | Extracts the A183068 carry-and-scaling proof into a computable theorem; contains an infinite all-prime $p^{2r}$ family and an all-prime $p^{3r}$ subfamily | Complete proof candidate; internal recheck passed, independent review pending |
| 1A | [q-calculus and cyclotomic supercongruences](QCalculusCyclotomicSupercongruences.md) | Turns Landau depth into exact root-of-unity multiplicity; gives a square q-lift of A183068 and an explicit corrected cubic theorem for depth-three families | Complete deductions from Clark and Straub; exact polynomial checks; priority preliminary |
| 1B | [Peter Bala's OEIS queue](BalaOeisSupercongruenceQueue.md) | Proves the A365029 boundary family and first two adjacent levels, plus the A375178 prime-level odd-power family; closes A333593 via Coster and Jacobsthal--Kazandzidis | Three complete elementary proof packets, published-theorem reductions, and exact checks; priority preliminary |
| 1B-A | [First two A365029 levels](A365029FirstTwoLevels.md) | Proves the \(p^3\) and \(p^6\) adjacent congruences by shifted scaling plus one- and two-digit harmonic cancellation | Complete unchecked proof; 67,310 exact checks |
| 1B-Q | [Binomial-quotient cancellation](BinomialQuotientCancellation.md) | Proves the complete two-parameter A357509 tower, the A357568 enhanced tower for every odd prime and every power parameter, and every A364506 row | Complete proof candidate; 2,192 exact checks; priority search preliminary |
| 1B-D | [A288470 double-binomial tower](A288470OddPrimeTower.md) | Uses two carries per missed digit level and adjacent binomial transfer to prove the named \(p^{2r}\) tower for every odd prime | Complete proof candidate; explicit \(p=2\) counterexample; priority search pending |
| 1B-M | [A141057 multinomial-power tower](MultinomialPowerFrobeniusTowers.md) | Proves a coefficientwise $p^{3r}$ Frobenius theorem for arbitrary multinomial dimension and power, closing A141057 and adding $p=3$ | Complete elementary proof candidate; 12,036 exact checks; priority search preliminary |
| 1B-U | [Odd-unit block towers](OddUnitBlockFrobeniusTowers.md) | Splits half-integral factorial products into a central-binomial transfer and odd unit blocks, proving A091527 and A262732 together | Complete elementary proof candidate; 806 exact checks; small-prime failures explicit |
| 1B-X | [Dixon--Legendre half-binomial towers](DixonLegendreHalfBinomialTowers.md) | Uses Dixon's evaluation and a complete half-binomial unit block to prove A275652, A275654, every stable row of A364303, and A364304 in one parameter family | Complete elementary proof candidate; 961 exact checks; small-prime failures explicit |
| 1B-I | [A364173 integrality and half-binomial tower](A364173IntegralHalfBinomialTower.md) | Resolves the record's separate integrality conjecture by a carry-interval floor lemma, then proves its full $p^{3r}$ tower using ordinary and half-binomial transfers | Complete elementary proof candidate; 487,211 exact checks; small-prime failures explicit |
| 1B-I2 | [A364176 affine-Landau integrality and tower](A364176AffineLandauTower.md) | Resolves A295456 at half-index by a five-case affine floor lemma, then invokes the rational gamma-ratio transfer | Complete elementary proof candidate; 501,908 exact checks; priority pending |
| 1B-RG | [Rational gamma-ratio cubic towers](RationalGammaRatioCubicTowers.md) | Extends the unit-block transfer to every fixed denominator; closes A364175, every row of A365025, and the stable A364513 rows while reducing A364172--A364184 to integrality | Complete elementary proof candidate; 8,666 exact checks; priority search preliminary |
| 1B-R | [Integral coefficient roots and Gauss baseline](CoefficientPowerGaussBaseline.md) | Resolves the integrality of the A002897/A008978/A113424 coefficient roots, proves the exact Lagrange bridge, and supplies the universal all-prime \(p^r\) variable-power tower | Complete elementary baseline; 1,819 exact checks; two cubic refinements remain open |
| 1B-O | [Apéry odd moments and the A357512 composite theorem](AperyOddMomentPrimeClassification.md) | Proves A357510, classifies every exceptional prime in the odd-moment family, and closes A357512 for all integers coprime to 6 by an exact telescoping certificate | Complete elementary proof candidate; 137,703 exact checks; independent review pending |
| 1B-CF | [Two-parameter coefficient-framing tower](CoefficientFramingCubicTower.md) | Proves six Bala/OEIS records, including the full A352373 parameter family, and arbitrary integral coefficient slopes by one elementary Cartier argument | Complete elementary proof candidate; 5,761 exact checks; independent review pending |
| 1B-AUG | [A119258 rays, Chebyshev towers, and negative-binomial defect](BalaAugustCoefficientPacket.md) | Extends coefficient framing to arbitrary integral slopes, proves every A119258 ray and Bala's Chebyshev family without fixed-denominator exclusions, closes five named records, and computes the Bernoulli obstruction to a proposed stronger congruence | Complete proof candidate; 940 exact checks; the corrected cubic tower is proved in 1B-AUG3 |
| 1B-AUG2 | [August mixed-binomial follow-on](BalaAugustMixedBinomialFollowOn.md) | Proves a coefficientwise Frobenius theorem for products of generalized binomials with signed upper slopes and weighted lower indices; closes named A333473, classifies fixed products and twists, and isolates a stabilized first-defect conjecture | Complete elementary theorem and classical reduction; 3,390 exact checks; the growing-modulus defect remains open |
| 1B-AUG2A | [Full A333473 algebraic-family tower](A333473AlgebraicFamilyTower.md) | Normalizes the Lagrange summands and proves coefficientwise discard/transfer modulo $p^{2r}$ for every positive $(R,S)$ and every odd prime | Complete elementary proof candidate; 91,260 exact checks; no parameter-prime exclusions |
| 1B-AUG2B | [Full index-dependent companion towers](IndexDependentCompanionPrimeBoundary.md) | Proves the $p^{3r}$ towers for both surviving substitution families by parity-doubling reciprocal blocks, shifted kernel descent, and cubic transfer on scaled shells | Complete proof candidate for every $p\ge5$; 19,758 exact checks |
| 1B-AUG3 | [Cubic towers for mixed negative-binomial prefixes](MixedNegativeBinomialCubicTower.md) | Uses a two-variable Cartier operator, unit-block reciprocal-square cancellation, and formal integration by parts to prove every positive-slope prefix tower cubically; closes Bala's $u(N)$ and the full positive A333592 family | Complete elementary proof candidate for $p\ge5$; 1,640 exact checks; the first $p=3$ boundary is classified in 1B-AUG4 |
| 1B-AUG4 | [All-level prime-three negative-binomial boundary](PrimeThreeNegativeBinomialBoundary.md) | Computes the normalized first defect modulo $3$, proves the maximal parameter-residue criterion $3\mid nab(a+b)$, and proves the universal all-level renormalization modulo $3^{3r+1}$ | Complete elementary theorem; 36,929 checks; sharp failures in all four excluded residue triples |
| 1B-AUG5 | [First-defect kernel for negative-binomial prefixes](BalaAugustFirstDefectKernel.md) | Extracts the normalized $p^{3r}$ defect as one Cartier moment and proves its coefficientwise Frobenius fixedness through a finite logarithm and piecewise-linear Green kernel | Complete first-residue stabilization theorem for $p\ge5$; 3,902 exact checks; the stronger growing-modulus refinement remains open |
| 1B-AUG6 | [Higher August defect reduction](BalaAugustHigherDefectLift.md) | Rewrites the growing-modulus conjecture as one division-free three-level congruence, proves the quartic coefficient lift, and isolates the remaining cubic-kernel contraction | Exact reduction plus quartic theorem; 1,277 checks; final cubic higher-Frobenius estimate open |
| 1B-CX | [Counterexample to the rational-framing theorem as printed](RationalFramingCounterexample.md) | Gives a global period-four rational 2-sequence for which both the weighted-harmonic lemma and the claimed cubic framing congruence fail at \(p=5\) | Complete exact counterexample; 3,620 checks; author notification appropriate |
| 1B-S5 | [Straub prime-five source audit](StraubPrimeFiveCoefficientPacket.md) | Corrects the source boundary: Straub's printed theorem already includes \(p=5\), and exact parameter matches source-close A108625, A143007, A177316, and the ordinary A108628 tower | Published-source reconciliation; 792 exact checks of the endpoint and coefficient matches |
| 1B-A108 | [A108628 half-index boundary](A108628HalfIndexBoundary.md) | Proves the first half-index vanishing conjecture and the exact exceptional valuation of its Dixon comparison term | Complete first-boundary proof; 1,797 exact checks; one aggregate master comparison would close all three higher claims |
| 1B-FR | [Balanced factorial-ratio cubic towers](BalancedFactorialRatioCubicTowers.md) | Converts every balanced integral factorial ratio to a Laurent binomial product and proves the A061164 cubic tower | Complete classical deduction; exact checks; no claim for \(p=2,3\) |
| 1B-J31 | [Bala July 31 research update](BalaJuly31ResearchUpdate.md) | Separates the newly closed symmetric-box and A061164 directions from the two live Apéry queues | Status ledger with links to controlling proofs |
| 1B-AP | [Apéry enhanced-congruence packet](AperyRankOneDefectPacket.md) | Collapses A352655, A357506, A357567, A357956, A357959 and two nonlinear companions to three linear Apéry defect relations | Complete exact reduction; 260 checks; core defect packet open |
| 1B-B52 | [Bober sporadic factorial-ratio packet](BoberSporadicFactorialRatioPacket.md) | Applies the balanced and rational-gamma engines to all 52 Bober ratios and Bala's 15 visible fractional-index variants | Ordinary 52-record tower proved for $p\ge5$; A364176 completely closed; 14 fractional integrality targets remain |
| 1B-BR | [Draft reply to Bala and Hanna](BalaBoberAugustReply.md) | Gives a short elementary account of the 52 ordinary towers and the newly completed A364176 case | Correspondence draft; no additional theorem claim |
| 1B-S | [110-record proof-campaign ledger](Bala110ProofCampaign.md) | Gives every census record a route, conservative status, evidence pointer, and next proof operation | Complete machine-readable ledger; 42 proved here, 20 source-closed, 41 partial, 7 with no explicit open target, no wholly untreated records, and none queued |
| 1B-BM | [Balanced-matrix coefficient tower](BalancedMatrixCoefficientQuadraticTower.md) | Uses a two-row carry lemma and Eisenstein Frobenius/transposition symmetry to prove A124435 | Complete elementary proof candidate; 94 exact checks; priority unestablished |
| 1B-A244 | [A244973 linear--quadratic Frobenius reduction](A244973QuadraticFrobeniusReduction.md) | Converts Sun's residual conjecture into one exact cancellation between the first two Dwork terms | Exact reduction; 113 checks; target remains open |
| 1B-A331 | [A331562 uniform rational diagonal](A331562UniformRationalDiagonal.md) | Encodes every fixed row by one path-matrix determinant ratio and isolates its finite continuant Frobenius numerator | Exact reduction; determinant, language, row, and sharp boundary checks pass; cubic estimate remains open |
| 1B-A079 | [A079489 Lagrange-kernel reduction](A079489LagrangeKernelReduction.md) | Reduces both variable-power families, including reversion and singular slopes, to one signed-binomial coefficient kernel | Exact reduction; 895 checks; normalized cubic kernel estimate remains open |
| 1B-EC | [Exponential-coefficient Cartier reduction](ExponentialCoefficientCartierReduction.md) | Gives one exact adjacent-difference identity for A060941, A362722, A362733, and arbitrary Euler-transform iterations | Exact reduction; 448 structural checks and 12 tower checks; quadratic/cubic Cartier estimates remain open |
| 1B-A376 | [A376 Apéry-companion reduction](A376AperyCompanionReduction.md) | Collapses A376458 to one four-binomial sum, proves its ordinary cubic tower and prime-level fifth power, and reduces A376466 to a four-variable adjacent-power constant term | Partial resolution; A376466 shifted tower refuted; 5,696 exact checks; only the A376466 ordinary tower and higher A376458 bonus remain open |
| 1B-FC | [Franel-companion constant-term reduction](FranelCompanionConstantTermReduction.md) | Unifies A362676 and the two integer-parameter A363985 families as constant terms of one two-kernel deformation | Exact reduction; 1,282 checks including 914 sharp tower cases; one cubic Cartier contraction remains |
| 1B-PB | [A260667 prime-boundary congruence](A260667PrimeBoundary.md) | Proves the isolated \(p^3\) boundary by a local binomial expansion and two exact weighted harmonic evaluations | Complete elementary proof candidate; 349 exact checks; priority search pending |
| 1B-TC | [A132303 trinomial-cube tower](A132303TrinomialCubeTower.md) | Uses a cyclotomic two-variable constant term whose linear Frobenius defect vanishes off the \(p\)-sublattice | Complete elementary proof candidate; exact checks; sharp quadratic exponent observed |
| 1B-LG | [A156554 Legendre coefficient tower](A156554LegendreCoefficientTower.md) | Adds a Legendre factor through three primitive, pairwise-unimodular Cartier rays and proves the full integral-parameter family | Complete elementary proof candidate; 10,868 exact checks; independent review pending |
| 1B-CY | [A351858 theorem and cyclotomic-family boundary](A351858CyclotomicFamilyBoundary.md) | Proves the named $k=2$ cubic tower by a six-residue Cartier lemma and gives two infinite valuation-two counterexample families at $k=p-1,p$ | Complete named proof candidate plus complete elementary boundary counterexamples |
| 1B-RV | [A263843 reversion theorem](A263843ReversionCoefficientReduction.md) | Uses exact Lagrange inversion and a ternary quadratic--cubic cancellation to reduce the reversion family to coefficient framing | Full family proved for every prime $p\ge3$, including denominator slopes and the named ternary case |
| 1B-ME | [Adjacent-binomial meander-row towers](MeanderAdjacentBinomialTowers.md) | Symmetrizes every A198060 row into adjacent binomial shells, proving its three intended congruence families and closing A198256/A198258 | Complete elementary proof candidate; 1,304 checks; A198060's printed exponent typo needs editorial correction |
| 1B-L | [Supercongruence literature and Bala--OEIS census](SupercongruenceLiteratureCensus.md) | Maps a reproducible 110-record OEIS search to the published theorem families and consolidates the genuinely live targets before more proof work is spent | Literature map with explicit source and priority boundaries |
| 1B-G | [Gaussian generalization map for the Bala queue](BalaGaussianGeneralizationMap.md) | Routes all 110 census records through five Gaussian proof architectures and separates formal coefficient changes from Frobenius twists and prime-ideal theorems | Exhaustive research map; no novelty claim |
| 1B-F | [Arithmetic Frobenius packet framework](ArithmeticFrobeniusPacketFramework.md) | Unifies the five census routes through number fields, prime ideals, local Frobenius transitions, finite-field orbits, valuation budgets, and local-to-global assembly | Complete elementary framework and 158,755 exact checks; routing is not a proof of all 110 conjectures |
| 1B-GE | [Exact Bala Gaussian-twist pilot](BalaGaussianTwistPilot.md) | Tests three finite-sum routes and supplies exact counterexamples to blindly preserving the untwisted cubic exponent | 195 exact checks; computational triage |
| 1C | [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md) | Turns collision counting into one second divided-difference curve in every degree; gives a genus ladder and a universal corrected tower | Complete theorem with cross-degree checks; priority preliminary |
| 1C-O | [Primitive collision-orbit bridge](JacobianCollisionEulerOrbitBridge.md) | Identifies Bala's multiplicative index tower with the Dold/Gauss primitive-orbit filtration, proves \(p^{2r}\)-packet divisibility for realizations of the Apéry and fourth-order Franel sequences, and gives a sharp obstruction for the degree-three collision scheme | Complete elementary synthesis and obstruction with 4,192 exact checks; classical inputs, new repository interpretation, no priority claim |
| 1C-KLS | [Crystalline-locus support and Frobenius packets](CrystallineLocusSupportFrobeniusBridge.md) | Adds a support-order layer from the Kansal--Levin--Savitt crystalline-locus classification, derives the baseline Gauss tower for every relative support packet, and identifies the Barsotti--Tate/Steinberg obstruction to recovering stack geometry from support data | Complete synthesis with 10,148 exact checks; no claim that the source paper proves a new supercongruence |
| 1D | [Finite-field counts for the Fable Jacobian counterexample](JacobianCounterexampleFiniteFieldCounts.md) | Uses the same adjacent-extension viewpoint to organize cubic fibers, collisions, and Frobenius counts of the new counterexample | Complete elementary theorem with exact checks; priority preliminary |
| 1E | [Degree-four Jacobian Frobenius obstruction](JacobianDegreeFourFrobeniusObstruction.md) | Shows how quadratic Artin factors obstruct raw adjacency and how two-step or corrected towers recover exact congruences | Complete elementary theorem with exact checks; priority preliminary |
| 1F | [Degree-five elliptic Frobenius packet](JacobianDegreeFiveEllipticFrobenius.md) | Shows the next transition: a tangent cubic contributes a non-CM elliptic trace, and removing the full Frobenius packet leaves an exact \(2r-2\) tower | Complete theorem with direct finite-field and tower checks; priority preliminary |
| 1G | [Hyperdeterminant entropy profile](HyperdeterminantEntropyProfile.md) | Converts the exact zero/square/nonsquare fibers and Gauss packet into complete Rényi, KL, total-variation, and additive-convolution laws | Complete entropy corollaries with exact checks; no separate priority claim |
| 1H | [Zhang four-matrix counterexample](ZhangFourMatrixCounterexample.md) | Applies exact low-dimensional matrix analysis to a named auxiliary conjecture from the noncommutative AM--GM program | Complete dimension-minimal counterexample, positive-definite interval, and exact checker; priority provisional |
| 2 | [Frobenius quotients of constant-term sequences](FrobeniusQuotientConstantTerms.md) | Proves the universal first-order expansion, identifies the exact rank-one condition behind the Cooper law, and gives exact counterexamples to two proposed Dwork shortcuts | Complete elementary theorem; Dwork boundaries certified |
| 3 | [p-adic Arzelà--Ascoli framework](PadicArzelaAscoliSupercongruenceTowers.md) | Proves the vertical limit supplied by A183068, uses the Banach contraction $x\mapsto px$ to rule out a global continuous interpolation, and proves uniform quadratic contraction of every normalized defect at zero | Complete elementary framework and obstruction; unit-shell estimate open |
| 4 | [Gaussian Frobenius twists](GaussianFrobeniusTwists.md) | Shows that discard-and-rescale proofs lift to roots-of-unity weights; specializes A183068 to a Gaussian split/inert congruence | Complete elementary deduction; priority unchecked |
| 4J | [Finite lattice-walk Frobenius congruences](LatticeWalkFrobeniusCongruences.md) | Gives the exact trace-sequence bridge from finite transfer matrices to Gaussian and Eisenstein split/inert/ramified congruences; separates finite-width SAW models from the conjectural SLE limit | Complete elementary theorem and 174 exact checks; unramified part is standard, ramified priority not established |
| 4J-G | [Group-ring Gauss torsion boundary](NonSoficGroupRingGaussBoundary.md) | Characterizes universal coefficient-return Gauss towers by absence of order-$p$ torsion and applies the obstruction to the explicit nonsofic group | Complete elementary theorem and 130 exact checks; ordinary depth $r$, priority unclaimed |
| 4J-N | [Walsh-chaos congruences for planar noise and Y](BlackNoiseWalshCongruences.md) | Turns color reversal into a \(3r-2\) Gaussian-prime congruence; the classical Y-game majority reduction supplies an exact multiscale Boolean observable alongside finite percolation and coalescing-walk models | Complete elementary arithmetic theorem with exhaustive Y checks through side length 5; priority provisional |
| 4B | [Binomial-power polynomial Frobenius theorem](BinomialPowerFrobeniusTheorem.md) | Proves the coefficientwise \(X\mapsto X^p\) tower for every exponent \(m\ge3\), including the multiplicity bonus \(v_p(m)\) and all Gaussian local cases | Complete elementary deduction; priority not established |
| 4C | [Quadratic A005259/A333592-family polynomial towers](QuadraticGaussianQueueTheorem.md) | Closes the two remaining Gaussian-pilot targets at coefficientwise exponent \(2r\) and covers every positive parameter pair in the broader A333592 family | Complete classical-scaling corollary; the full positive A333592 family is separately cubic in 1B-AUG3 |
| 4D | [Cyclotomic coefficient-pair theorem](CyclotomicCoefficientPairTheorem.md) | Proves the A228960 and A350383 \(p^{2r}\) conjectures in coefficientwise form and specializes them at \(X=i\) | Complete elementary proof candidate; priority search preliminary |
| 4E | [Colored Euler-product Frobenius theorem](EulerProductGaussianTower.md) | Proves one coefficientwise \(p^{2r}\) theorem containing Bala's full quadratic product packet, the A380290 baseline, and split/inert Gaussian part-count twists | Complete elementary proof candidate; the special untwisted A380290 cubic conjecture remains open |
| 4E-M | [Modular-product prime-coefficient packet](ModularProductPrimeCoefficientPacket.md) | Proves all displayed conjectures on seven route-M records and supplies four quadratic baselines by combining one universal first-coefficient formula with the colored Euler-product theorem | Complete elementary packet; 256 exact checks; route completed by the two paired-product follow-ons |
| 4E-M2 | [Cubic Euler-product Cartier square](EulerProductCubicCartierMoments.md) | Reduces A023871, A023873, A206622, A283271, and A380290 at every level to one coefficientwise Cartier-square stratum bound; both weighted moments and all logarithmic degrees at least three are discharged | Exact all-level reduction; 4,546 checks; the one stratum estimate remains open |
| 4E-R | [A229452 coefficient root](A229452CoefficientRootBaseline.md) | Proves the all-\(m\) integrality conjecture through a strong multinomial Gauss seed, gives its exact Lagrange bridge, and establishes the all-prime tower for both source parameter families | Complete integrality and \(p^r\) baseline; 1,268 exact checks; cubic gains open |
| 4E-S | [A049505 symmetric-plane-partition congruences](A049505SymmetricPlanePartitionCongruences.md) | Uses exact complementary-factor pairing and half-range harmonic cancellation to prove all three named congruences | Complete elementary proof; 229 exact checks; priority not claimed |
| 4E-C | [A008793 cube-plane-partition tower](A008793CubePlanePartitionTower.md) | Uses exact complementary-factor splitting, reduced-residue blocks, and binary parity to prove the full nonlinear \(p^{4r}\) tower | Complete elementary proof candidate; 455 exact checks; priority not claimed |
| 4E-B | [Symmetric-box plane-partition tower](SymmetricBoxPlanePartitionTower.md) | Extends the cube mechanism to every \(N\times N\times cN\) box and proves A352656 and A352657 | Complete elementary proof candidate; 1,074 exact checks; priority search pending |
| 4F | [Dyadic hypercube defect](DyadicHypercubeDefect.md) | Proves the sharp binary law \(e(1)=1\), \(e(r)=2r\) for \(r\ge2\), identifies the exact first-level modulus-\(4\) obstruction, and specializes it for A380290 to a lacunary binary theta coefficient | Complete elementary theorem and exact checks; no priority claim for the standard \(2\)-derivation |
| 4G | [Complete Gaussian local table for Euler products](EulerProductGaussianLocalTable.md) | Combines the odd and dyadic theorems into one split/inert/ramified prime-ideal law, including the \(i\mapsto-1\) binary cross-twist and exact \((1+i)\)-adic exponents | Complete corollary and exact local-valuation checks; withdrawn Witt--Hadamard near-match excluded as proof input |
| 4H | [Walsh analysis of the dyadic hypercube defect](DyadicHypercubeWalshAnalysis.md) | Shows that every output coordinate has a matching quadratic graph and computes its exact model count, Walsh spectrum, influences, noise stability, and every affine-face restriction | Complete combinatorial corollary and exhaustive checks; classical Boolean Fourier machinery |
| 4I | [Joint spectrum of the dyadic hypercube defect](DyadicHypercubeJointSpectrum.md) | Reduces every XOR of output coordinates to an alternating convolution matrix; recovers exact joint counts, collision probability, chi-squared distance, and distribution bounds from ranks, radicals, and Gauss-sum signs | Complete finite-dimensional theorem and exhaustive checks; classical quadratic-form Fourier theorem |
| 4J | [Exact hashing of affine Fourier spectra](AffineSpectrumHashing.md) | Converts affine Walsh-support dimension into an exact random-hash success probability and a \(\log_2(s)\)-scale sufficient measurement budget | Complete specialization of the classical binary full-rank formula with exact checks |
| 4K | [Exact matroid law for linear hashing](MatroidHashingLaw.md) | Extends the affine formula to every finite Fourier support through the characteristic polynomial of its difference matroid | Complete application of the classical Crapo--Rota Critical Theorem; [priority audit](HypercubeHashingPriorityAudit.md) |
| 4A | [Chowla--Dwork--Evans split-prime defect](ChowlaDworkEvansSplitDefect.md) | Rewrites their published modulo-\(p^2\) lift as an exact normalized defect and exceptional-prime criterion | Published theorem plus exact corollary; no novelty claim |
| 5 | [Cubic $(\eta)$ congruence at $p=3$](EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to fill a small-prime gap in a published theorem | Complete unchecked draft |
| 6 | [Gaussian Wolstenholme citation network](GaussianWolstenholmeCitationNetwork.md) | Replaces scaling by translation-invariant Gaussian residue blocks | Three major candidate results with exact certificates; independent review required |
| 7 | [Gaussian canonical-product synthesis](GaussianLucasCanonicalProducts.md) | Extracts the dominant logarithmic-moment mechanism, proves that the normalized ramified block is a bijective disk isometry, and exhibits the sharp anisotropic polydisc together with its critical-shell parity hyperplane | Proved local theorem plus open research program; 3,000 pair checks, four sharp witnesses, and 5,274 boundary-residue checks |
| 7A | [Gaussian critical-shell filtration](GaussianCriticalShellFiltration.md) | Improves the reciprocal-square valuation, raises the full logarithmic tail to \(8r-4\), and proves that every affine-defect depth through \(2r-2\) is an exact isometry chamber | Complete local theorem; 2,400 pair checks and 224 higher-coefficient checks; priority unchecked |
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
| Arithmetic Frobenius packets | `verification/related/verify_arithmetic_frobenius_packet_framework.py` |
| Landau depth | `verification/related/verify_landau_supercongruence.py` |
| Peter Bala's OEIS queue | `verification/related/verify_bala_oeis_supercongruences.py` |
| Franel-companion constant-term reduction | `verification/related/verify_franel_companion_ct_reduction.py` |
| Balanced-matrix coefficient tower | `verification/related/verify_balanced_matrix_coefficient_tower.py` |
| A244973 linear--quadratic Frobenius reduction | `verification/related/verify_a244973_frobenius_reduction.py` |
| A331562 uniform rational diagonal | `verification/related/verify_a331562_uniform_rational_diagonal.py` |
| A079489 Lagrange-kernel reduction | `verification/related/verify_a079489_lagrange_kernel.py` |
| Exponential-coefficient Cartier reduction | `verification/related/verify_exponential_coefficient_cartier.py` |
| A376 Apéry-companion reduction | `verification/related/verify_a376_apery_companions.py` |
| Bober sporadic factorial-ratio packet | `verification/related/verify_bober_sporadic_packet.py` |
| A364176 affine-Landau theorem | `verification/related/verify_a364176_affine_landau.py` |
| Bala August coefficient packet | `verification/related/verify_bala_august_coefficient_packet.py` |
| Bala August mixed-binomial follow-on | `verification/related/verify_bala_august_mixed_binomial_follow_on.py` |
| Bala August first-defect kernel | `verification/related/verify_bala_august_first_defect.py` |
| Bala August kernel Frobenius lift | `verification/related/verify_bala_august_kernel_frobenius.py` |
| Bala August higher-defect reduction | `verification/related/verify_bala_august_higher_defect.py` |
| Mixed negative-binomial cubic prefixes | `verification/related/verify_mixed_negative_binomial_cubic_tower.py` |
| Prime-three negative-binomial boundary | `verification/related/verify_prime_three_negative_binomial_boundary.py` |
| Group-ring Gauss torsion boundary | `verification/related/verify_group_ring_gauss_boundary.py` |
| First two A365029 levels | `verification/related/verify_a365029_first_two_levels.py` |
| A005725 quadrinomial and ratio coefficients | `verification/related/verify_quadrinomial_coefficient_tower.py` |
| Mixed-step coefficient tower | `verification/related/verify_mixed_step_coefficient_tower.py` |
| A260667 prime boundary | `verification/related/verify_a260667_prime_boundary.py` |
| A132303 trinomial-cube tower | `verification/related/verify_a132303_trinomial_cube.py` |
| A156554 Legendre coefficient tower | `verification/related/verify_a156554_legendre_tower.py` |
| A351858 cyclotomic-family boundary | `verification/related/verify_a351858_cyclotomic_boundary.py` |
| A263843 reversion reduction | `verification/related/verify_a263843_reversion_reduction.py` |
| Binomial-quotient cancellation | `verification/related/verify_binomial_quotient_cancellation.py` |
| Apéry odd-moment prime classification | `verification/related/verify_apery_odd_moment_prime_classification.py` |
| q-calculus and cyclotomic lifts | `verification/related/verify_q_calculus_supercongruence.py` |
| All-degree weighted-lift collisions | `verification/related/verify_weighted_lift_collision_synthesis.py` |
| Fable Jacobian-counterexample counts | `verification/related/verify_jacobian_counterexample_counts.py` |
| Degree-four Jacobian collisions | `verification/related/verify_jacobian_degree_four.py` |
| Degree-five Jacobian collisions | `verification/related/verify_jacobian_degree_five.py` |
| Primitive collision-orbit bridge | `verification/related/verify_jacobian_euler_orbit_bridge.py` |
| Crystalline-locus support bridge | `verification/related/verify_crystalline_locus_support_bridge.py` |
| Hyperdeterminant Fourier packet | `verification/related/verify_hyperdeterminant_fourier.py` |
| Hyperdeterminant entropy profile | `verification/related/verify_hyperdeterminant_entropy.py` |
| Zhang four-matrix counterexample | `verification/related/verify_zhang_four_matrix_counterexample.py` |
| Frobenius quotient identity | Coefficientwise algebraic proof; no checker required |
| Dwork and continuity boundaries | `verification/related/verify_dwork_boundaries.py` |
| p-adic Arzelà--Ascoli framework | Elementary ultrametric, contraction, and compactness proofs |
| Cubic $(\eta)$ | `verification/related/verify_eta_prime3.py` |
| Cooper level 11 | `verification/related/verify_cooper_level11.py` |
| Gaussian Frobenius twists | `verification/related/verify_gaussian_twists.py` |
| Finite lattice-walk Frobenius congruences | `verification/related/verify_lattice_walk_frobenius.py` |
| Planar-noise Walsh congruences | `verification/related/verify_black_noise_chaos_filter.py` |
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
| Gaussian critical-shell filtration | `verification/related/verify_gaussian_critical_shell.py` |
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

