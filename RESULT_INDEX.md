# Result index

This is the repository's claim-level index. It lists mathematical results
separately even when several appear in one note. Check this page before
starting a new search or describing a result as new.

Status labels are deliberately conservative:

- **Audited draft:** received a separate machine-assisted referee-style audit;
  not peer reviewed.
- **Complete unchecked draft:** a complete written argument and exact checks
  are present; independent mathematical and priority review remain.
- **Deduction:** an elementary consequence of a broader proved or proposed
  statement; priority remains unchecked.
- **Reduction:** meaningful progress, not a proof of the target statement.
- **Computational:** exact evidence or a certificate without a general proof.

## Core result

### A183068 — all-prime supercongruence

- **Claim:** $a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}$ for every prime $p$.
- **Status:** Audited draft.
- **Proof:** [PROOF.md](PROOF.md)
- **Exact checker:** [`verify_a183068.py`](verification/verify_a183068.py)

## Direct generalizations

### LD-2 — Landau-depth family

- **Claim:** A computable Landau-depth criterion gives an infinite all-prime
  $p^{2r}$ family containing A183068.
- **Status:** Complete proof candidate; internal recheck passed, independent
  review and priority pending.
- **Proof:** [Landau-depth synthesis](related-results/LandauDepthSupercongruenceSynthesis.md)
- **Exact checker:** [`verify_landau_supercongruence.py`](verification/related/verify_landau_supercongruence.py)

### LD-3 — depth-three family

- **Claim:** The depth-$3$ subfamily satisfies an all-prime $p^{3r}$
  congruence.
- **Status:** Complete proof candidate; internal recheck passed, independent
  review and priority pending.
- **Proof:** [Landau-depth synthesis](related-results/LandauDepthSupercongruenceSynthesis.md)
- **Exact checker:** [`verify_landau_supercongruence.py`](verification/related/verify_landau_supercongruence.py)

### FQ-CT — first Frobenius quotient

- **Claim:** Every integral Laurent-polynomial constant-term sequence has a
  universal first-order Frobenius expansion modulo $p^2$. The $n=1$ A183068
  theorem therefore gives an explicit vanishing constant term for every
  prime. The unique-interior Dwork theorem does not imply the additional
  rank-one pairing needed for the Cooper law.
- **Status:** Complete elementary theorem and corollary; no novelty claim.
- **Proof:** [Frobenius-quotient identity](related-results/FrobeniusQuotientConstantTerms.md)
- **Exact boundary checker:** [`verify_dwork_boundaries.py`](verification/related/verify_dwork_boundaries.py)

### AA-TOWER — p-adic compactness of supercongruence towers

- **Claim:** A uniform adjacent-scale valuation tending to infinity gives a
  quantitative uniform limit of the full tower. A uniform horizontal modulus
  extends that limit to $\mathbb Z_p$, while equicontinuity of normalized
  defects gives subsequential defect profiles by Arzelà--Ascoli. For A183068,
  the scale-invariant limit is nonconstant, so the Banach contraction
  $x\mapsto px$ proves that no continuous extension to all of $\mathbb Z_p$
  exists. Its normalized defects nevertheless obey
  $D_r(p^h n)=p^{2h}D_{r+h}(n)$ and are uniformly equicontinuous at zero.
- **Status:** Complete elementary framework and obstruction. Horizontal
  interpolation on the unit shell remains open.
- **Proof:** [p-adic Arzelà--Ascoli framework](related-results/PadicArzelaAscoliSupercongruenceTowers.md)
- **Exact boundary checker:** [`verify_dwork_boundaries.py`](verification/related/verify_dwork_boundaries.py)

### DWORK-BOUNDARY — exact failure of the proposed shortcut

- **Claim:** The displayed A183068 Laurent polynomial has three, not one,
  interior lattice points. Moreover, the unique-interior hypothesis by itself
  does not imply the Cooper rank-one pairing; the Laurent polynomial
  $1+2x^{-1}+x$ fails it at $p=3$.
- **Status:** Complete exact counterexamples.
- **Proof:** [Frobenius-quotient identity, Section 3](related-results/FrobeniusQuotientConstantTerms.md#3-what-the-standard-dwork-theorem-does-not-supply-automatically)
- **Exact checker:** [`verify_dwork_boundaries.py`](verification/related/verify_dwork_boundaries.py)

### GFT — Gaussian Frobenius twists

- **Claim:** Termwise supercongruences lift to roots-of-unity weights; the
  $i^k$ twist distinguishes split and inert primes.
- **Status:** Deduction.
- **Proof:** [Gaussian Frobenius twists](related-results/GaussianFrobeniusTwists.md)
- **Exact checker:** [`verify_gaussian_twists.py`](verification/related/verify_gaussian_twists.py)

### ETA-3 — cubic extension at the exceptional prime

- **Claim:** A cubic $\eta$-sequence congruence extends to the omitted prime
  $p=3$.
- **Status:** Complete unchecked draft.
- **Proof:** [Cubic $p=3$ extension](related-results/EtaPrime3CubicExtension.md)
- **Exact checker:** [`verify_eta_prime3.py`](verification/related/verify_eta_prime3.py)

### BS-DWORK — Bhatt--Singh/Dwork period scaling

- **Claim:** For \(A_d(n)=(dn)!/(n!)^d\), multinomial scaling and a
  base-\(p\) digit-sum estimate give
  \[
  v_p(A_d(np^r)-A_d(np^{r-1}))
  \ge 3(r+v_p(n))-\epsilon_p+s_p(n)v_p(d!).
  \]
  This places an explicit all-prime supercongruence beside the
  Bhatt--Singh \(F\)-pure-threshold tower for Fermat Calabi--Yau
  hypersurfaces.
- **Status:** Complete elementary deduction with exact checks; no novelty
  claim and priority unchecked.
- **Proof:** [Bhatt--Singh/Dwork period synthesis](related-results/BhattSinghDworkPeriodSupercongruence.md)
- **Exact checker:** [`verify_dwork_period_supercongruence.py`](verification/related/verify_dwork_period_supercongruence.py)

### FF-DET - finite-field determinant bias

- **Claim:** The additive determinant character sum over \(n\)-by-\(n\)
  matrices over \(\mathbf F_q\) has an exact closed form. Its high-degree end
  gives a uniform non-asymptotic Fourier-bias bound, while its low-degree end
  gives the sharp adjacent-extension identity
  \[
  v_p(\mathcal S_n(p^r)-\mathcal S_n(p^{r-1}))
  =\frac{n^2-n+2}{2}(r-1).
  \]
- **Status:** Complete elementary theorem with exact checks; new to this
  program. The rank count is classical; the sharp adjacent-extension
  valuation and two-ended formulation appear new in a targeted search, with
  priority still provisional.
- **Proof:** [Finite-field determinant bias and supercongruence](related-results/FiniteFieldDeterminantBiasSupercongruence.md)
- **Exact checker:** [`verify_finite_field_determinant_bias.py`](verification/related/verify_finite_field_determinant_bias.py)

### FF-PFAFF - finite-field Pfaffian bias

- **Claim:** The Pfaffian additive-character sum on alternating
  \(2m\)-by-\(2m\) matrices has an exact closed form, Fourier bias of order
  \(q^{-3}\), and the sharp adjacent-extension valuation
  \[
  v_p(\mathcal P_m(p^r)-\mathcal P_m(p^{r-1}))
  =(m^2-m+1)(r-1).
  \]
- **Status:** Complete elementary theorem with exact checks. Alternating-rank
  counts are classical; the sharp valuation and two-ended formulation appear
  new in a targeted search, with priority provisional.
- **Proof:** [Pfaffian bias and supercongruence](related-results/FiniteFieldPfaffianBiasSupercongruence.md)
- **Exact checker:** [`verify_finite_field_pfaffian_bias.py`](verification/related/verify_finite_field_pfaffian_bias.py)

## Gaussian-integer results

### GWL-POLY — Gaussian box polynomial

- **Claim:** Kalinin's Gaussian box polynomial has explicit closed forms for
  inert and split primes, including
  $b_j\equiv\binom{j+2}{2}\pmod p$ in the split case.
- **Status:** Complete unchecked draft.
- **Proof:** [Gaussian Wolstenholme network, Theorem 1](related-results/GaussianWolstenholmeCitationNetwork.md#2-the-polynomial-conjecture)
- **Exact checker:** [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py)

### GWL-POWER — exact obstruction and corrected theorem

- **Claim:** Kalinin's printed higher-power conjecture has an exact periodic
  obstruction and fails for every prime $p>17$; a corrected stable-range
  theorem holds.
- **Status:** Complete unchecked draft.
- **Proof:** [Gaussian Wolstenholme network, Theorem 2 and Corollary 3](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture)
- **Exact checker:** [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py)

### GWL-LUCAS — rectangular Gaussian Lucas congruence

- **Claim:** Kalinin's rectangular Gaussian coefficient satisfies the Lucas
  congruence modulo $p^3$ for every inert prime $p>5$; $p=3$ is an exact
  boundary.
- **Status:** Complete unchecked draft.
- **Public summary:** [GAUSSIAN_LUCAS.md](GAUSSIAN_LUCAS.md)
- **Full proof:** [Gaussian Wolstenholme network, Theorem 4](related-results/GaussianWolstenholmeCitationNetwork.md#5-the-gaussian-lucas-congruence)
- **Exact checker:** [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py)

### GWL-SCALE — adjacent prime-power scaling

- **Claim:** The inert-prime Gaussian Lucas difference is divisible by
  $p^{3r}$ between scales $p^{r-1}$ and $p^r$; at $p=3$ the corresponding
  exponent is $3r-1$.
- **Status:** Complete proof candidate with exact checks; independent review
  and a priority search required.
- **Proof:** [Prime-power Gaussian Lucas congruence](related-results/GaussianLucasPrimePowerTheorem.md)
- **Report:** [Adjacent-scale Gaussian Lucas experiment](related-results/GaussianLucasScalingExperiment.md)
- **Exact experiment:** [`experiment_gaussian_lucas_scaling.py`](verification/related/experiment_gaussian_lucas_scaling.py)

### GWL-TWO — ramified prime theorem

- **Claim:** At $\varpi=1+i$ and $r\ge2$, every nontrivial adjacent ratio has
  exact valuation
  $6r-3+v_\varpi(CD(A-C+i(B-D)))$. The unnormalized difference has
  valuation at least $6r-4$.
- **Status:** Complete proof candidate with independent machine-assisted
  audits and exact checks, including excess valuation $53$; conventional
  review and a priority search required.
- **Proof:** [Ramified-prime theorem](related-results/GaussianLucasRamifiedTwoTheorem.md)
- **Report:** [Ramified-prime experiment](related-results/GaussianLucasRamifiedTwoExperiment.md)
- **Exact experiment:** [`experiment_gaussian_lucas_scaling.py`](verification/related/experiment_gaussian_lucas_scaling.py)

### GL-CANON — local canonical-product synthesis

- **Claim:** Gaussian Lucas ratios are normalized finite products whose exact
  valuation is controlled by the first surviving logarithmic moment. A
  dominant-first-moment lemma isolates this implication, and the inert,
  split, and ramified cases form a single local research program.
- **Status:** Proved structural lemma and synthesis; the split-prime program
  remains conjectural and priority is unchecked.
- **Note:** [Gaussian Lucas canonical products](related-results/GaussianLucasCanonicalProducts.md)
- **Depends on:** [Ramified-prime theorem](related-results/GaussianLucasRamifiedTwoTheorem.md)

### GL-ISO — ramified Gaussian disk isometry

- **Claim:** For \(r\ge2\), the mixed-block product satisfies
  \(v_{1+i}(F_r(Z)-F_r(W))=6r-3+v_{1+i}(Z-W)\). After division by its
  first logarithmic coefficient, it is a bijective analytic isometry of
  \(\mathbb Z_2[i]\). The same conclusion holds throughout the
  finite-dimensional parameter region where the first logarithmic moment
  dominates every later moment by one valuation level.
- **Status:** Complete deduction from the ramified reciprocal-moment theorem;
  exact checks are present, while conventional review and priority remain
  pending.
- **Proof:** [Gaussian Lucas canonical products, Section 6](related-results/GaussianLucasCanonicalProducts.md#6-the-mixed-block-product-is-an-exact-disk-isometry)
- **Exact checker:** [`verify_gaussian_product_isometry.py`](verification/related/verify_gaussian_product_isometry.py)

### GL-DYN — translated-product return filtration

- **Claim:** For every unit \(u\), the translated isometry
  \(T_{r,u}=G_r+u\) satisfies
  \(v_{1+i}(T_{r,u}^{2^m}(Z)-Z)=2m\). Thus every orbit modulo
  \((1+i)^n\) has length \(2^{\lceil n/2\rceil}\), exactly as for ordinary
  addition.
- **Status:** Complete deduction from the ramified reciprocal-moment
  estimates. A stronger compatible-conjugacy statement remains conjectural;
  318 all-unit quotient maps and deeper selected tests pass exactly.
- **Note:** [Gaussian product dynamics](related-results/GaussianProductDynamicsConjectures.md)
- **Exact experiment:** [`experiment_gaussian_product_dynamics.py`](verification/related/experiment_gaussian_product_dynamics.py)

### GL-MAP — literature and structural map

- **Claim:** The current results sit at the intersection of Gaussian
  Wolstenholme--Lucas congruences, local product expansions, generalized
  factorial ideals, Dwork/Frobenius questions, and compatible \(p\)-adic
  dynamics.
- **Status:** Literature synthesis, not a theorem or a novelty certificate.
- **Note:** [Gaussian Lucas literature puzzle](related-results/GaussianLucasLiteraturePuzzle.md)

### GPS — Gaussian power sums

- **Claim:** Two printed small-prime Gaussian power-sum formulas hold, while
  two broader claims have exact counterexamples.
- **Status:** Complete unchecked draft.
- **Proof:** [Gaussian power-sum conjectures](related-results/GaussianPowerSumConjectures.md)
- **Exact checker:** [`verify_gaussian_power_sums.py`](verification/related/verify_gaussian_power_sums.py)

### BOX-d — higher-degree box polynomials

- **Claim:** The finite-field box-polynomial mechanism extends to arbitrary
  degree by Boolean Möbius inversion.
- **Status:** Complete unchecked draft; likely classical infrastructure.
- **Proof:** [Higher-degree box polynomials](related-results/HigherDegreeFiniteFieldBoxPolynomials.md)
- **Exact checker:** [`verify_higher_degree_box_polynomial.py`](verification/related/verify_higher_degree_box_polynomial.py)

## Reductions and computational reports

### s18-2 — binary supercongruence reduction

- **Claim:** A published binary supercongruence is reduced to one sharpened
  scaling lemma.
- **Status:** Reduction.
- **Report:** [Binary $s_{18}$ reduction](related-results/S18TwoAdicReduction.md)
- **Exact checker:** None yet.

### C11 — Cooper level-11 exceptional primes

- **Claim:** Beukers--Tsai--Ye prove the required Lucas congruence modulo
  every prime. Exact tests then isolate the $n=1$ obstruction at the two
  exceptional Cooper level-11 primes. In 8,300 further cases, the full
  first-order defect is $nT(n-1)q_p$ modulo $p$. This is equivalent to an
  explicit rank-one Cartier identity modulo $p^2$ and, if proved, settles
  both parts of Cooper's Conjecture 11.2. At $p=3$, 30,003 exact checks
  support a stronger three-branch base-$3$ recursion modulo $9$.
- **Status:** Existing proved Lucas foundation plus reproducible computational
  theorem targets. The rank-one Cartier lift and the three-branch
  modulo-$9$ refinement remain unproved. The naive $X_0(11)$ trace-$2$
  interpretation is refuted by exact witnesses. A rational-diagonal
  representation would make each fixed-prime instance a finite-automaton
  equivalence problem, but no such representation is currently supplied.
- **Report:** [Cooper level-11 report](related-results/CooperLevel11RarePrimes.md)
- **Exact checker:** [`verify_cooper_level11.py`](verification/related/verify_cooper_level11.py)

### G-BOUNDARY — classical Gaussian obstructions

- **Claim:** Gaussian Erdős–Moser and Wolstenholme-prime directions are reduced
  to identified classical obstructions.
- **Status:** Reduction.
- **Report:** [Gaussian boundary report](related-results/GaussianCitationNetworkBoundaryReport.md)
- **Exact checker:** [`verify_gaussian_erdos_moser.py`](verification/related/verify_gaussian_erdos_moser.py)

## Search discipline

Before opening a new research branch:

1. search this ledger by theorem name, source author, sequence, and mechanism;
2. search the full repository text;
3. inspect the public repository, not only a private working branch;
4. check whether a note contains multiple independently reportable theorems;
5. then perform a current external literature and priority search.

The ledger records what this project already contains. It is not evidence that
the claims are novel in the wider literature.
