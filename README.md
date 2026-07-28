# The A183068 supercongruence

This repository is a short, self-contained account of a proposed proof of the
supercongruence attached to [OEIS A183068](https://oeis.org/A183068). It is
organized for Paul D. Hanna, the author of the sequence, and for a specialist
who wants to audit the argument without first reading the larger research
repository or a Lean formalization.

## Current research portfolio

The continually updated Economist-style scorecard is
**[RANKINGS.md](RANKINGS.md)**. It ranks every completed result and open
target by mathematical-community value, deployment value, novelty
confidence, breadth, maturity, and cost remaining. The present first-priority
line is Gaussian and harmonic: ramified and inert Gaussian-prime lifting,
angular Fourier projections, and their radial Bernoulli residues. The
all-degree weighted-lift collision program remains active at lower priority;
source status and proof status are recorded separately.

The ranking is canonical rather than chronological: GWL-TWO currently holds
the crown, GWL-SCALE is the heir, and GPS-CUBIC is the first ascendant.

## Public follow-on tracks

### Gaussian-prime follow-on

The principal public research line is the Gaussian-prime stack:

- [ramified-prime theorem](related-results/GaussianLucasRamifiedTwoTheorem.md);
- [prime-power scaling](related-results/GaussianLucasPrimePowerTheorem.md);
- [cubic angular residue](related-results/GaussianAngularResidueTheorem.md);
- [canonical products](related-results/GaussianLucasCanonicalProducts.md).

### 2-adic Roe-inspired follow-on

The second public line is
**[orientation lifting, Dehn twists, and affine symmetry](ROE_2ADIC.md)**.
It extracts an exact dyadic lifting package from the Roe--Turturean
presentation: a nonintegral compatible orientation exponent, a
$\mathbb Z_2$-family of outer Dehn twists, and the affine commutator
filtration. Its newest corollary gives an optimal exact sampler for every
finite affine quotient and the complete spectrum of a Dehn-twist coordinate
refresh chain. A second corollary replaces coordinate refresh by the fixed
Cayley generators $\mathcal T_{\pm1}$, $5^{\pm1}$, and $-1$; its cyclotomic
spectrum gives explicit two-sided spectral-gap bounds and
$\Theta(4^m)$ relaxation. Source ingredients and new deductions are separated
explicitly on the landing page. A separate
[current-PDF audit](related-results/GQ2CurrentPdfAudit.md) reproduces the
Appendix C norm identities and the complete $S_3$ and $S_4$ counts without
finding a new error.

The newest result is the
[cubic angular-residue theorem](related-results/GaussianAngularResidueTheorem.md):
for every inert prime $p\ge7$, it replaces a printed constant-valuation
conjecture by an explicit congruence modulo $p^4$ for every odd
$1\le r\le2p-1$, produces three universal zeros, and exhibits failure of
that formula immediately outside the proved range.

The newest auxiliary lifting result is
[GQ2-LIFT](ROE_2ADIC.md), an exact $2$-adic
orientation law sharpening Roe--Turturean Remark C.7 together with the exact
$\mathbb Z_2$-family of outer Dehn twists hidden in their HNN shear and the
resulting affine commutator filtration. It is included as a clean
local-to-global boundary example, not as a supercongruence or a novelty
claim. The [sampling follow-on](related-results/DyadicDehnTwistSampler.md)
is an exact classical-algorithmic corollary, not a solution of a
mapping-class-group open problem. The
[fixed-generator follow-on](related-results/DyadicDehnTwistCayleyWalk.md)
turns the same twists and unit scalings into a genuine Cayley walk with
cyclotomic eigenvalues and explicit spectral-gap bounds. The
[grammar and almost-periodicity note](related-results/DyadicTwistGrammarAlmostPeriodicity.md)
then gives affine words a unique translation-first normal form and applies
finite-group almost periodicity to dense averages of twist observables.

## The result

Define

```math
a(n)=\sum_{k=0}^{n}\frac{(2n+2k)!}{k!^4(n-k)!^2}.
```

Peter Bala conjectured in July 2024 that for every prime $p$ and all positive
integers $n,r$,

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
```

**[Read the friendly proof](PROOF.md).** Its first screen gives the complete
idea in plain language; the carry calculation and small-prime bookkeeping
follow underneath for verification.

## Attribution

- Paul D. Hanna created A183068 in December 2010 as the central terms of
  triangle A183065.
- Peter Bala added the factorial-sum formula and the supercongruence conjecture
  in July 2024.
- The present proof draft was prepared by Ravi Bajaj and Alexander Burns.

The attribution above follows the live OEIS record. Paul D. Hanna was first
contacted about the proposed proof on July 24, 2026.

## The proof in four steps

1. Each summand is a six-part multinomial coefficient.
2. Legendre's formula shows that terms with $p\nmid k$ vanish modulo
   $p^{2r}$.
3. A Ljunggren--Jacobsthal--Kazandzidis scaling congruence identifies the terms
   with $p\mid k$ with the preceding $p$-adic level.
4. A separate parity argument closes the only deficient case, $p=2,r=1$.

This is an ordinary mathematical proof. A future Lean development would be a
separate verification project, not a prerequisite for reading the argument.

## Present status

| Item | Status |
| --- | --- |
| Written proof | Complete draft |
| Exact computation | 105 congruence cases, including $r=3$ samples |
| Machine-assisted referee audit | Two exact-text audits completed; no proof-level error reported, and the second audit narrowed one finite-test sharpness remark |
| Conventional specialist review | Pending |
| Literature-priority search | Preliminary only |
| Lean formalization | Not attempted in this repository |

The [audit log](AUDIT.md) records what was checked and what changed. The
audits and computations are evidence, not substitutes for peer review. Please
report any gap, attribution issue, or earlier proof.

For an Economist-style assessment of every result in the repository, see the
public [mathematical research portfolio](RANKINGS.md). It scores
math-community value, deployment value, novelty confidence, breadth,
maturity, and cost remaining separately.

## Public research policy

This repository is public so that claims can be inspected, reproduced, and
corrected. Publication here follows six rules:

1. source conjectures and prior authors are credited explicitly;
2. theorem, proof candidate, computation, and conjecture are labeled
   separately;
3. machine assistance and exact checks are not described as peer review;
4. counterexamples, failed approaches, and corrections remain auditable; and
5. priority and novelty are treated as pending until the literature and
   specialists have been checked; and
6. each research result is identified as a **named open problem**, an
   **explicit source direction**, or a **structural follow-on**, so a new
   theorem is not quietly presented as a solved published conjecture.

## Public q-calculus follow-on

The
[q-calculus lift](related-results/QCalculusCyclotomicSupercongruences.md)
refines the Landau carry argument at roots of unity. It proves a
square-cyclotomic q-supercongruence containing A183068 and computes the full
second cyclotomic defect for every depth-three balanced multinomial family.

The note also records the precise connection with Bhatt--Scholze prisms:
$\Phi_p(q)=[p]_q$ is the q-crystalline prismatic ideal and
$q\mapsto q^{p^2}$ is the second Frobenius iterate. This is an
interpretation of the elementary polynomial theorem, not a claim that
prismatic cohomology was used in its proof.

## Public finite-field Fourier follow-on

The
[hyperdeterminant convolution theorem](related-results/HyperdeterminantConvolutionTower.md)
uses exact Fourier inversion on $\mathbf F_q$ to determine the distribution
of every sum
$$
\Delta(T_1)+\cdots+\Delta(T_m).
$$
Each convolution power has only three fiber classes: zero, nonzero square,
and nonsquare. For every odd prime and every class it proves the sharp law
$$
v_p\!\left(C_m^\sigma(p^r)-C_m^\sigma(p^{r-1})\right)
=(4m-1)(r-1).
$$
The same calculation gives a quantitative total-variation mixing bound.
This is finite-field harmonic analysis in the restriction/Kakeya orbit:
the note carefully separates the proved scalar pushforward spectrum from
the still-open ambient Fourier transform of a hyperdeterminant level set.
It makes no geometric-Langlands or cryptographic-extractor claim.

The companion
[constant-spectrum theorem](related-results/DeterminantPfaffianConvolutionTowers.md)
does the same for determinant and Pfaffian. For convolution length $\ell$,
both zero and nonzero fibers satisfy the sharp general law
$$
v_p\!\left(N_{\ell,\star}(p^r)-N_{\ell,\star}(p^{r-1})\right)
=(\ell E-1)(r-1).
$$
It also gives an exact, rather than bounded, total-variation mixing formula.
At the algorithmic level, the determinant/Pfaffian spectrum has two orbits
and the hyperdeterminant spectrum has three. Their arbitrary convolution
powers therefore require only a constant number of scalar exponentiations,
not a length-$q$ FFT. This is a structured spectral shortcut, not an
improvement to general audio-codec FFTs.

The
[USAMO dyadic follow-on](related-results/USAMODyadicHammingSupercongruence.md)
starts from the forced-halving proof of 2008 USAMO Problem 4. It gives the
exact number of all-isosceles triangulations, identifies the admissible
binary indices with a radius-two Hamming ball, and reduces its $2^d$-point
Walsh convolution to $d+1$ Krawtchouk packets. The resulting zero-XOR
polynomials form an adjacent-extension supercongruence family whose first
exceptional prime is $439$.

## Public Jacobian-counterexample follow-on

The
[all-degree weighted-lift synthesis](related-results/WeightedLiftCollisionSynthesis.md)
is the central theorem for this branch. A generic fiber degree $n$ produces
one tangent curve of degree $n-2$ and arithmetic genus
$(n-3)(n-4)/2$. The exact collision zeta function separates into Tate,
curve-Frobenius, and finite permutation factors. Removing the last two gives
a universal corrected adjacent valuation of $2r-2$.

The
[finite-field counting theorem for the Fable Jacobian counterexample](related-results/JacobianCounterexampleFiniteFieldCounts.md)
turns the counterexample's cubic fibers into exact arithmetic data. It gives
the complete factorization-type distribution over every odd finite field,
the image and collision counts, the local zeta function of the self-fiber
product, and the exact adjacent-extension valuations. Characteristic $3$
has an additional $p$-adic layer because the fixed mixed coefficient
forbids triple-root cubics there.

This is elementary finite-field counting organized by the supercongruence
program. It is not an application of geometric Langlands, localization, or
ultrafilters. The formulas are complete and exactly checked; literature
priority remains provisional.

The
[degree-four follow-on](related-results/JacobianDegreeFourFrobeniusObstruction.md)
shows where this simple picture first breaks. Its collision zeta function has
three quadratic Artin factors. Their extension-parity signs destroy the raw
adjacent congruence at seven of the eight prime classes modulo $24$; a
two-step tower or an explicit Frobenius correction restores a sharp
congruence. This separates polynomial/Tate data from finite-monodromy data in
an entirely explicit example.

The
[degree-five follow-on](related-results/JacobianDegreeFiveEllipticFrobenius.md)
is the next structural transition. The tangent locus is now a smooth plane
cubic, and the exact collision count contains the Frobenius trace of an
explicit non-CM elliptic curve, together with finite root-count corrections.
The note gives the complete local zeta factorization, isolates a sharp
characteristic-$17$ boundary exception, and proves an exact
Frobenius-corrected adjacent valuation of $2r-2$.

The
[degree-six follow-on](related-results/JacobianDegreeSixGenusThree.md)
makes the first higher-genus rung explicit. At $p=13$, the tangent locus is
a smooth genus-three quartic with a computed degree-six local
$L$-polynomial. Its Frobenius packet forces the raw adjacent collision
difference to be a $13$-adic unit at every level. Removing the complete
curve and finite-orbit packet restores the exact valuation $2r-2$. This is
both a new theorem candidate and a useful warning: higher-degree collision
counts need Frobenius correction before a supercongruence can exist.

The
[degree-seven follow-on](related-results/JacobianDegreeSevenGenusSix.md)
continues the ladder with an integral seed having good reduction at $p=5$.
Its tangent curve has genus six. The raw collision congruence is controlled
by an exact period-$156$ Frobenius automaton: divisibility by $5$ occurs
in exactly $28$ level classes. The same canonical correction again leaves
the exact valuation $2r-2$.

The
[Frobenius obstruction-automaton theorem](related-results/FrobeniusObstructionAutomata.md)
now closes the structural loop. At every good prime and every fixed
precision $p^k$, the raw successful levels form an eventually periodic set
with rational density, equivalently a unary regular language. The state is
the curve's Frobenius-recurrence state together with the finite-orbit phase.
For the genus-six example, the exact densities through $5^4$ are
$7/39,8/195,2/195,$ and $11/3900$. This is an exact finite-state
classification, not a claim of pseudorandomness or cryptographic hardness.

The
[finite-state thermodynamics follow-on](related-results/FrobeniusTransferThermodynamics.md)
makes the statistical-mechanics dictionary exact rather than metaphorical.
Its transfer matrix gives a rational two-variable orbit series, and a single
valuation partition polynomial records every fixed congruence threshold. For
the degree-seven $p=5$ automaton, the complete precision-$5^4$ polynomial
is
$$
16000+2700u+600u^2+145u^3+55u^4.
$$
At fixed precision this is a finite analytic system, so no physical phase
transition or randomness claim is made.

The
[all-precision lifting theorem](related-results/PadicValuationExpansion.md)
then proves that the degree-seven unit-root trace has exact period
$39\cdot5^{k-1}$ modulo $5^k$ for every $k$. A single Hensel factor
and matrix tangent certificate modulo $125$ force every subsequent period
lift. The complete $5^5$ and $5^6$ valuation polynomials are checked over
$97500$ and $487500$ clock classes. The nested divisibility layers live
on the profinite grid
$\mathbf Z/156\mathbf Z\times\mathbf Z_5$, where truncated valuation is
an exact sum of clopen indicator functions.

## Public Gaussian-prime follow-on

The most concise shareable follow-on is
**[Kalinin's Gaussian Lucas congruence](GAUSSIAN_LUCAS.md)**. It gives the
statement, proof mechanism, exact $p=3$ boundary, source paper, and
reproduction command. Its present status is an unchecked proof candidate,
not a peer-reviewed theorem.

An [adjacent-scale experiment](related-results/GaussianLucasScalingExperiment.md)
led to a [prime-power proof candidate](related-results/GaussianLucasPrimePowerTheorem.md)
with exponent $3r$ for inert primes $p>5$ and $3r-1$ at $p=3$. It requires
independent review and a priority search.

At the ramified prime $2=-i(1+i)^2$, a separate
[proof candidate](related-results/GaussianLucasRamifiedTwoTheorem.md)
determines the adjacent ratio valuation exactly:

```math
v_{1+i}(R_{2,r}-1)
=
6r-3+
v_{1+i}\!\left(CD(A-C+i(B-D))\right)
```

for every nontrivial rectangle and $r\ge2$. It also gives the difference
exponent $6r-4$. The mechanism is a four-coset reciprocal-sum lift, a
normalized power-sum estimate, and a parity induction for the possible
denominator loss. It has exact checks and machine-assisted audits, but still
requires conventional review and a priority search.

The accompanying
[canonical-product synthesis](related-results/GaussianLucasCanonicalProducts.md)
rewrites these ratios as non-Archimedean finite products. It also proves that,
after normalization by the first logarithmic coefficient, the ramified block
is a bijective analytic isometry of $\mathbb Z_2[i]$. The
[literature map](related-results/GaussianLucasLiteraturePuzzle.md) explains how
this connects to Dwork/Frobenius questions, generalized factorials, and
compatible $p$-adic dynamics. The Blaschke-product comparison is an analytic
analogy, not a claim that the Gaussian ratios are classical Blaschke products.

The follow-on
[finite-quotient dynamics theorem](related-results/GaussianProductDynamicsConjectures.md)
shows that every unit translation of the normalized product has exactly the
same return-valuation filtration as ordinary addition. Modulo
$(1+i)^n$, every orbit has length $2^{\lceil n/2\rceil}$. This gives a precise
negative cryptographic conclusion: the maps are bijective and predictable,
but not full-cycle generators. Compatible conjugacy to addition remains open.

## Suggested reading order

1. Read Sections 1--3 of [PROOF.md](PROOF.md) for the statement and carry
   estimate.
2. Check the precise small-prime losses in Lemma 2.
3. Audit the three cases in Lemma 3, especially $p=2,r=1$.
4. Run `python verification/verify_a183068.py`.
5. Consult [RELATED_RESULTS.md](RELATED_RESULTS.md) only after the core proof.

To reproduce every computation in the expanded repository, run
`python verification/run_all.py`.

## Repository map

- [RESULT_INDEX.md](RESULT_INDEX.md): the claim-level ledger. Consult this
  before beginning a new search; it separates distinct theorems even when they
  share one proof note.
- [RANKINGS.md](RANKINGS.md): the public multi-criteria ranking of every
  claim-level result and open target.
- [PROOF.md](PROOF.md): the complete proof and references.
- [verification/verify_a183068.py](verification/verify_a183068.py): a small
  exact-integer regression check.
- [RELATED_RESULTS.md](RELATED_RESULTS.md): an index of every current result
  produced by the same program, separated by audit status.
- [related-results/QCalculusCyclotomicSupercongruences.md](related-results/QCalculusCyclotomicSupercongruences.md):
  the q-calculus theorem generator, square A183068 lift, corrected cubic
  theorem, and prismatic interpretation.
- [related-results/HyperdeterminantConvolutionTower.md](related-results/HyperdeterminantConvolutionTower.md):
  exact additive convolution fibers, sharp adjacent-extension valuations,
  Fourier mixing, and the boundary of the ambient restriction/Kakeya problem.
- [related-results/DeterminantPfaffianConvolutionTowers.md](related-results/DeterminantPfaffianConvolutionTowers.md):
  the constant-spectrum compiler, two infinite sharp convolution families,
  and exact determinant/Pfaffian mixing.
- [related-results/USAMODyadicHammingSupercongruence.md](related-results/USAMODyadicHammingSupercongruence.md):
  exact isosceles-triangulation counts, Hamming-orbit Walsh compression, and
  the derivative-controlled adjacent tower.
- [related-results/WeightedLiftCollisionSynthesis.md](related-results/WeightedLiftCollisionSynthesis.md):
  the all-degree tangent-curve collision theorem, genus ladder, zeta
  decomposition, and universal corrected tower.
- [related-results/FrobeniusObstructionAutomata.md](related-results/FrobeniusObstructionAutomata.md):
  the fixed-$p$-adic-precision automaton theorem, rational-density law,
  and higher-precision degree-six and degree-seven examples.
- [related-results/FrobeniusTransferThermodynamics.md](related-results/FrobeniusTransferThermodynamics.md):
  the exact transfer-matrix formulation and degree-seven valuation partition
  polynomial.
- [related-results/PadicValuationExpansion.md](related-results/PadicValuationExpansion.md):
  the all-precision unit-root period theorem, higher valuation polynomials,
  and profinite clopen expansion.
- [related-results/JacobianCounterexampleFiniteFieldCounts.md](related-results/JacobianCounterexampleFiniteFieldCounts.md):
  complete finite-field fiber statistics, collision zeta function, and the
  characteristic-$3$ adjacent-extension gain for the Fable counterexample.
- [related-results/JacobianDegreeFourFrobeniusObstruction.md](related-results/JacobianDegreeFourFrobeniusObstruction.md):
  degree-four collision formula, quadratic Artin factors, obstruction to raw
  adjacency, and Frobenius-corrected supercongruence.
- [related-results/JacobianDegreeFiveEllipticFrobenius.md](related-results/JacobianDegreeFiveEllipticFrobenius.md):
  degree-five collision formula, explicit non-CM elliptic factor, local zeta
  function, and corrected adjacent-extension law.
- [related-results/JacobianDegreeSixGenusThree.md](related-results/JacobianDegreeSixGenusThree.md):
  degree-six genus-three local $L$-polynomial, permanent raw obstruction at
  $p=13$, and corrected adjacent-extension law.
- [related-results/JacobianDegreeSevenGenusSix.md](related-results/JacobianDegreeSevenGenusSix.md):
  degree-seven genus-six local $L$-polynomial, period-$156$ raw
  obstruction automaton, and corrected adjacent-extension law.
- [GAUSSIAN_LUCAS.md](GAUSSIAN_LUCAS.md): the public entry point for the
  Gaussian-prime follow-on.
- [related-results/](related-results/): the complete related proof drafts and
  reductions. These are stored locally in this repository rather than merely
  linked from the larger working repository.
- [verification/related/](verification/related/): the corresponding exact
  checkers.
- [verification/run_all.py](verification/run_all.py): one command for all twenty-nine
  verification programs.

The broader working repository remains available at
[rbajaj5/oeis-conjecture-proofs](https://github.com/rbajaj5/oeis-conjecture-proofs).
