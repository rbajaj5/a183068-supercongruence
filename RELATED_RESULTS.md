# Related supercongruence results

This page keeps Paul D. Hanna informed about developments that grew out of the
A183068 proof without mixing them into the proof itself.

## Status key

- **Audited draft:** received a separate machine-assisted referee-style audit,
  but is not peer reviewed.
- **Internally rechecked candidate:** the written proof was rederived and its
  checker strengthened, but no independent reviewer has yet audited it.
- **Unchecked candidate:** exact tests pass, but the written proof and
  literature priority still need independent review.
- **Reduction only:** useful progress, not a claimed solution.

## Direct line from A183068

| Result | Relationship | Status |
| --- | --- | --- |
| A183068 modulo $p^{2r}$ for every prime | The core named conjecture | Audited draft |
| [Repository-wide dyadic audit policy](DYADIC_POLICY.md) | Requires every all-prime result to discharge binary normalization, sign, ramification, first-level boundaries, and cancellation explicitly | Editorial proof standard with four repository case studies |
| [Peter Bala's OEIS queue](related-results/BalaOeisSupercongruenceQueue.md) | Proves the first A365029 conjecture in the stronger \(p^{A+B}\) form, proves the complete A375178 prime-level odd-power family, closes the A333593 tower by reduction to Coster and Jacobsthal--Kazandzidis, and isolates Coster's \(p^{3r}\) baseline beneath the stronger A375178 tower | Two complete elementary proofs plus published-theorem reductions, with 1,518 exact checks; priority preliminary |
| [Supercongruence literature and Bala--OEIS census](related-results/SupercongruenceLiteratureCensus.md) | Routes the 110-record Bala/OEIS search corpus through Coster, Straub, Dwork, Landau, harmonic-sum, \(p\)-adic gamma, and \(q\)-microscope methods; separates published instances from consolidated open families | Reproducible literature map; negative searches are not priority certificates |
| [Gaussian generalization map for the Bala queue](related-results/BalaGaussianGeneralizationMap.md) | Classifies all 110 census records into finite-sum twist, constant-term, factorial/block, modular-product, and derived routes; separates coefficient extension, Frobenius twist, and prime-ideal theorems | Exhaustive routing map; not a theorem or novelty certificate |
| [Bala Gaussian-twist pilot](related-results/BalaGaussianTwistPilot.md) | Tests A005260, A005259, and A333592 under the split/inert \(i^k\)-twist and gives exact witnesses showing that a cubic untwisted exponent need not survive twisting | 195 exact tests; computational triage, not a proof |
| [Binomial-power polynomial Frobenius theorem](related-results/BinomialPowerFrobeniusTheorem.md) | Proves the coefficientwise \(X\mapsto X^p\) tower for every power \(m\ge3\), including split/inert Gaussian twists and the prime-specific multiplicity bonus \(v_p(m)\) | Complete elementary deduction with 8,220 exact checks; priority not established |
| [Landau-depth synthesis](related-results/LandauDepthSupercongruenceSynthesis.md) | Extracts the carry-and-scaling argument into a computable criterion; gives an infinite all-prime $p^{2r}$ family containing A183068 and an all-prime $p^{3r}$ subfamily | Internally rechecked candidate |
| [q-calculus and cyclotomic supercongruences](related-results/QCalculusCyclotomicSupercongruences.md) | Lifts Landau depth to an exact cyclotomic filtration; proves a universal square-cyclotomic q-congruence and an explicit corrected cubic q-congruence. The $(4,2)$ case is a q-lift of A183068 | Complete elementary deductions with exact polynomial checks; priority preliminary |
| [Frobenius quotients of constant-term sequences](related-results/FrobeniusQuotientConstantTerms.md) | Proves the universal first-order expansion, identifies the additional rank-one condition behind the Cooper law, and gives exact counterexamples showing that unique-interior Dwork congruences neither imply that pairing nor apply to the displayed A183068 polynomial | Complete elementary theorem and boundary certificates; no novelty claim |
| [p-adic Arzelà--Ascoli framework](related-results/PadicArzelaAscoliSupercongruenceTowers.md) | Shows that every uniform supercongruence tower has a quantitative vertical limit; the Banach contraction $x\mapsto px$ proves that the nonconstant A183068 limit cannot extend continuously to all of $\mathbb Z_p$, while the normalized defects satisfy exact quadratic scaling and are uniformly equicontinuous at zero | Complete elementary framework and obstruction |
| [Gaussian Frobenius twists](related-results/GaussianFrobeniusTwists.md) | Lifts a termwise supercongruence to roots-of-unity weights; the $i^k$-twist detects split versus inert primes in $\mathbb Z[i]$ | Unchecked candidate |
| [Chowla--Dwork--Evans split-prime defect](related-results/ChowlaDworkEvansSplitDefect.md) | Rewrites their published modulo-\(p^2\) lift of Gauss's binomial congruence as an exact normalized defect and exceptional-prime criterion | Published theorem plus exact corollary; no novelty claim |

The Landau-depth synthesis is the most important direct generalization. It
explains which part of the A183068 proof is special and which part is reusable.

## Neighboring literature reached by the method

| Result | Relationship | Status |
| --- | --- | --- |
| [Catalan ballot-power audit](related-results/CatalanBallotPowerSupercongruenceAudit.md) | Unifies the parallel \(p^{3r}\) conjectures for A183069, A361889, and A361892 and records sharp computational refinements at \(2\) and \(3\) | Computational target: 2,211 exact checks, no proof or novelty claim |
| [Roe--Turturean \(2\)-adic lifting packet](ROE_2ADIC.md) | Gives a finite-input comparison case for compatible \(2\)-adic lifting, identifies the source shear with a tower of outer Dehn twists, and computes exact affine filtrations and finite-quotient samplers | Complete elementary deductions and source audit with five exact checkers; no correction or novelty claim |
| [Dyadic Dehn-twist conjugacy moments](related-results/DyadicDehnTwistConjugacyMoments.md) | Classifies the affine images of nonzero twists by \(2\)-adic depth and converts their conjugacy-shell sizes into the exact lift \(D_{m+1,j}-2D_{m,j}=2^{jm}\) | Complete elementary deduction with exhaustive finite-quotient checks; no novelty claim |
| [All-degree weighted-lift collision theorem](related-results/WeightedLiftCollisionSynthesis.md) | Extracts the common tangent-curve mechanism in every generic degree; gives the genus ladder, zeta decomposition, and universal corrected \(2r-2\) tower | Complete theorem with cross-degree exact checks; literature priority provisional |
| [Finite-field counts for the Fable Jacobian counterexample](related-results/JacobianCounterexampleFiniteFieldCounts.md) | Converts the marked-root cubic description into complete factorization statistics, an exact collision zeta function, and a characteristic-\(3\) adjacent-extension gain | Complete elementary theorem with exact prime-field and extension-field checks; literature priority provisional |
| [Degree-four Jacobian Frobenius obstruction](related-results/JacobianDegreeFourFrobeniusObstruction.md) | Extends collision counting to Gallagher's quartic lift; quadratic Artin factors explain failure of raw adjacency, while two-step and corrected towers recover exact valuations | Complete elementary theorem with exact prime-field and extension-field checks; literature priority provisional |
| [Degree-five elliptic Frobenius packet](related-results/JacobianDegreeFiveEllipticFrobenius.md) | Continues Gallagher's lift to degree five; the tangent locus becomes a plane cubic and a non-CM elliptic trace enters the collision zeta function | Complete theorem with exact prime-field, extension-field, and tower checks; literature priority provisional |
| [Hyperdeterminant Fourier packet](related-results/HyperdeterminantFourierSupercongruence.md) | Shows what changes when the relative-invariant scaling weight has index two: square/nonsquare fibers produce a Gauss packet whose paired product satisfies a sharp \(8(r-1)\) adjacent-extension supercongruence | Complete elementary theorem with exact checks; classical ingredients, paired formulation apparently new; priority provisional |
| [Finite-field Pfaffian bias](related-results/FiniteFieldPfaffianBiasSupercongruence.md) | Extends the rank-deficiency mechanism from determinant to Pfaffian: high-degree cancellation gives \(q^{-3}\) bias and the first low-degree coefficient gives a sharp \((m^2-m+1)(r-1)\) valuation | Complete elementary theorem with exact checks; rank counts classical, sharp valuation formulation apparently new; priority provisional |
| [Finite-field determinant bias](related-results/FiniteFieldDeterminantBiasSupercongruence.md) | Replaces the smallest-singular-value obstruction by exact rank deficiency over \(\mathbf F_q\); opposite ends of one character-sum polynomial give a non-asymptotic bias bound and a sharp adjacent-extension supercongruence | Complete elementary theorem with exact checks; the count is classical, while the sharp valuation formulation appears new in a targeted search; priority provisional |
| [Cubic $(\eta)$ congruence at $p=3$](related-results/EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to address a small prime omitted from a published theorem | Unchecked candidate |
| [Bhatt--Singh/Dwork period synthesis](related-results/BhattSinghDworkPeriodSupercongruence.md) | Connects the Fermat Calabi--Yau \(F\)-pure-threshold tower to the diagonal period \(A_d(n)=(dn)!/(n!)^d\), proving an all-prime adjacent-scale bound with a uniform \(v_p(d!)\) gain | Complete elementary deduction with exact checks; no novelty claim |
| [Gaussian Wolstenholme citation network](related-results/GaussianWolstenholmeCitationNetwork.md) | Applies related residue-block ideas in Gaussian-integer arithmetic; contains a Gaussian Lucas proof candidate, a polynomial-product proof candidate, and a corrected reciprocal-power statement | Unchecked candidate |
| [Gaussian Lucas canonical products](related-results/GaussianLucasCanonicalProducts.md) | Recasts the inert and ramified proofs as local analytic products, proves the normalized ramified block is a bijective disk isometry, and identifies the split-prime normalization problem | Proved local theorem plus open research program |
| [Gaussian product dynamics](related-results/GaussianProductDynamicsConjectures.md) | Proves an exact return-valuation law and finite-quotient cycle profile for unit translations of the ramified disk isometry; compatible conjugacy to addition remains open | Complete deduction plus open conjugacy problem |
| [Gaussian Lucas literature puzzle](related-results/GaussianLucasLiteraturePuzzle.md) | Places the product theorem beside Dwork/Frobenius theory, generalized factorials, and compatible $p$-adic dynamics, while separating direct links from analogies | Literature map |
| [Gaussian power-sum conjectures](related-results/GaussianPowerSumConjectures.md) | Proves the printed $p=3,5$ formulas and gives exact counterexamples to two broader claims in a recent source | Unchecked candidate |
| [Higher-degree finite-field box polynomials](related-results/HigherDegreeFiniteFieldBoxPolynomials.md) | Extends the Gaussian polynomial mechanism to arbitrary finite-field degree by Boolean Möbius inversion | Unchecked candidate; likely classical infrastructure |
| [Gaussian citation-network boundary report](related-results/GaussianCitationNetworkBoundaryReport.md) | Records rigorous reductions for Gaussian Erdős--Moser and identifies the classical Wolstenholme-prime obstruction | Reduction only |
| [Binary $s_{18}$ problem](related-results/S18TwoAdicReduction.md) | Reduces a published binary supercongruence to one sharpened scaling lemma and gives a counterexample to a tempting factor-by-factor proof | Reduction only |
| [Cooper level-11 rare primes](related-results/CooperLevel11RarePrimes.md) | Starts from the Lucas theorem of Beukers--Tsai--Ye, isolates the $n=1$ obstruction, and reformulates an 8,300-case first-order law as a rank-one Cartier lift modulo $p^2$; proving it would settle both parts of Cooper's Conjecture 11.2. It also finds a stronger three-branch base-$3$ recursion modulo $9$ in 30,003 exact checks and rejects the naive $X_0(11)$ trace-$2$ explanation | Existing proved modulo-$p$ foundation plus reproducible modulo-$p^2$ theorem targets; the new identities remain unproved |

These neighboring results are not all logical consequences of A183068. Their
connection is methodological: $p$-adic residue strata supply vanishing, and a
scaling or translation map controls the surviving terms.

## Gaussian-prime terminology

For a concise public entry point, see
[Kalinin's Gaussian Lucas congruence](GAUSSIAN_LUCAS.md).

Gaussian integers are numbers $a+bi$ with $a,b\in\mathbb Z$. A Gaussian
prime is an irreducible element of this ring. Ordinary primes
$p\equiv3\pmod4$ remain prime (are *inert*), while primes
$p\equiv1\pmod4$ split; for example,

```math
5=(2+i)(2-i).
```

The Gaussian work above concerns congruences in this enlarged arithmetic. It
does not claim a result about the distribution of Gaussian primes or an
immediate cryptographic application.

## Communication policy

The full drafts and their exact checkers are now included in this repository.
Their labels are part of the mathematical record: inclusion means that Paul
can inspect the work, not that an unchecked candidate has become a theorem.
The next status update should follow independent review of the Gaussian and
Landau-depth candidates.
