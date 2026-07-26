# The A183068 supercongruence

This repository is a short, self-contained account of a proposed proof of the
supercongruence attached to [OEIS A183068](https://oeis.org/A183068). It is
organized for Paul D. Hanna, the author of the sequence, and for a specialist
who wants to audit the argument without first reading the larger research
repository or a Lean formalization.

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
corrected. Publication here follows five rules:

1. source conjectures and prior authors are credited explicitly;
2. theorem, proof candidate, computation, and conjecture are labeled
   separately;
3. machine assistance and exact checks are not described as peer review;
4. counterexamples, failed approaches, and corrections remain auditable; and
5. priority and novelty are treated as pending until the literature and
   specialists have been checked.

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

## Public Jacobian-counterexample follow-on

The
[finite-field counting theorem for the Fable Jacobian counterexample](related-results/JacobianCounterexampleFiniteFieldCounts.md)
turns the counterexample's cubic fibers into exact arithmetic data. It gives
the complete factorization-type distribution over every odd finite field,
the image and collision counts, the local zeta function of the self-fiber
product, and the exact adjacent-extension valuations. Characteristic \(3\)
has an additional \(p\)-adic layer because the fixed mixed coefficient
forbids triple-root cubics there.

This is elementary finite-field counting organized by the supercongruence
program. It is not an application of geometric Langlands, localization, or
ultrafilters. The formulas are complete and exactly checked; literature
priority remains provisional.

The
[degree-four follow-on](related-results/JacobianDegreeFourFrobeniusObstruction.md)
shows where this simple picture first breaks. Its collision zeta function has
three quadratic Artin factors. Their extension-parity signs destroy the raw
adjacent congruence at seven of the eight prime classes modulo \(24\); a
two-step tower or an explicit Frobenius correction restores a sharp
congruence. This separates polynomial/Tate data from finite-monodromy data in
an entirely explicit example.

The
[degree-five follow-on](related-results/JacobianDegreeFiveEllipticFrobenius.md)
is the next structural transition. The tangent locus is now a smooth plane
cubic, and the exact collision count contains the Frobenius trace of an
explicit non-CM elliptic curve, together with finite root-count corrections.
The note gives the complete local zeta factorization, isolates a sharp
characteristic-\(17\) boundary exception, and proves an exact
Frobenius-corrected adjacent valuation of \(2r-2\).

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
- [related-results/JacobianCounterexampleFiniteFieldCounts.md](related-results/JacobianCounterexampleFiniteFieldCounts.md):
  complete finite-field fiber statistics, collision zeta function, and the
  characteristic-\(3\) adjacent-extension gain for the Fable counterexample.
- [related-results/JacobianDegreeFourFrobeniusObstruction.md](related-results/JacobianDegreeFourFrobeniusObstruction.md):
  degree-four collision formula, quadratic Artin factors, obstruction to raw
  adjacency, and Frobenius-corrected supercongruence.
- [related-results/JacobianDegreeFiveEllipticFrobenius.md](related-results/JacobianDegreeFiveEllipticFrobenius.md):
  degree-five collision formula, explicit non-CM elliptic factor, local zeta
  function, and corrected adjacent-extension law.
- [GAUSSIAN_LUCAS.md](GAUSSIAN_LUCAS.md): the public entry point for the
  Gaussian-prime follow-on.
- [related-results/](related-results/): the complete related proof drafts and
  reductions. These are stored locally in this repository rather than merely
  linked from the larger working repository.
- [verification/related/](verification/related/): the corresponding exact
  checkers.
- [verification/run_all.py](verification/run_all.py): one command for all twenty
  verification programs.

The broader working repository remains available at
[rbajaj5/oeis-conjecture-proofs](https://github.com/rbajaj5/oeis-conjecture-proofs).
