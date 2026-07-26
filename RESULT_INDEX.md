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

## Claim ledger

| ID | Mathematical claim | Status | Proof or report | Exact checker |
| --- | --- | --- | --- | --- |
| A183068 | \(a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}\) for every prime \(p\) | Audited draft | [PROOF.md](PROOF.md) | [`verify_a183068.py`](verification/verify_a183068.py) |
| LD-2 | A computable Landau-depth criterion gives an infinite all-prime \(p^{2r}\) family containing A183068 | Complete unchecked draft | [Landau-depth synthesis](related-results/LandauDepthSupercongruenceSynthesis.md) | [`verify_landau_supercongruence.py`](verification/related/verify_landau_supercongruence.py) |
| LD-3 | The depth-\(3\) subfamily satisfies an all-prime \(p^{3r}\) congruence | Complete unchecked draft | [Landau-depth synthesis](related-results/LandauDepthSupercongruenceSynthesis.md) | [`verify_landau_supercongruence.py`](verification/related/verify_landau_supercongruence.py) |
| GFT | Termwise supercongruences lift to roots-of-unity weights; the \(i^k\) twist distinguishes split and inert primes | Deduction | [Gaussian Frobenius twists](related-results/GaussianFrobeniusTwists.md) | [`verify_gaussian_twists.py`](verification/related/verify_gaussian_twists.py) |
| ETA-3 | A cubic \(\eta\)-sequence congruence extends to the omitted prime \(p=3\) | Complete unchecked draft | [Cubic \(p=3\) extension](related-results/EtaPrime3CubicExtension.md) | [`verify_eta_prime3.py`](verification/related/verify_eta_prime3.py) |
| GWL-POLY | Kalinin's Gaussian box polynomial has explicit closed forms for both inert and split primes, including \(b_j\equiv\binom{j+2}{2}\pmod p\) in the split case | Complete unchecked draft | [Gaussian Wolstenholme network, Theorem 1](related-results/GaussianWolstenholmeCitationNetwork.md#2-the-polynomial-conjecture) | [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py) |
| GWL-POWER | Kalinin's printed higher-power conjecture has an exact periodic obstruction and fails for every prime \(p>17\); a corrected stable-range theorem holds | Complete unchecked draft | [Gaussian Wolstenholme network, Theorem 2 and Corollary 3](related-results/GaussianWolstenholmeCitationNetwork.md#3-the-exact-obstruction-to-the-higher-power-conjecture) | [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py) |
| GWL-LUCAS | Kalinin's rectangular Gaussian coefficient satisfies the Lucas congruence modulo \(p^3\) for every inert prime \(p>5\); \(p=3\) is an exact boundary | Complete unchecked draft | [Public entry point](GAUSSIAN_LUCAS.md); [full proof](related-results/GaussianWolstenholmeCitationNetwork.md#5-the-gaussian-lucas-congruence) | [`verify_gaussian_wolstenholme.py`](verification/related/verify_gaussian_wolstenholme.py) |
| GPS | Two printed small-prime Gaussian power-sum formulas hold, while two broader claims have exact counterexamples | Complete unchecked draft | [Gaussian power-sum conjectures](related-results/GaussianPowerSumConjectures.md) | [`verify_gaussian_power_sums.py`](verification/related/verify_gaussian_power_sums.py) |
| BOX-\(d\) | The finite-field box-polynomial mechanism extends to arbitrary degree by Boolean Möbius inversion | Complete unchecked draft; likely classical infrastructure | [Higher-degree box polynomials](related-results/HigherDegreeFiniteFieldBoxPolynomials.md) | [`verify_higher_degree_box_polynomial.py`](verification/related/verify_higher_degree_box_polynomial.py) |
| \(s_{18}\)-2 | A published binary supercongruence is reduced to one sharpened scaling lemma | Reduction | [Binary \(s_{18}\) reduction](related-results/S18TwoAdicReduction.md) | None yet |
| C11 | Exact tests isolate the \(n=1\) obstruction at the two exceptional Cooper level-11 primes | Computational | [Cooper level-11 report](related-results/CooperLevel11RarePrimes.md) | [`verify_cooper_level11.py`](verification/related/verify_cooper_level11.py) |
| G-BOUNDARY | Gaussian Erdős--Moser and Wolstenholme-prime directions are reduced to identified classical obstructions | Reduction | [Gaussian boundary report](related-results/GaussianCitationNetworkBoundaryReport.md) | [`verify_gaussian_erdos_moser.py`](verification/related/verify_gaussian_erdos_moser.py) |

## Search discipline

Before opening a new research branch:

1. search this ledger by theorem name, source author, sequence, and mechanism;
2. search the full repository text;
3. inspect the public repository, not only a private working branch;
4. check whether a note contains multiple independently reportable theorems;
5. then perform a current external literature and priority search.

The ledger records what this project already contains. It is not evidence that
the claims are novel in the wider literature.
