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
| Machine-assisted referee audit | Completed with no mathematical error reported after the $p=2$ sourcing clarification |
| Conventional specialist review | Pending |
| Literature-priority search | Preliminary only |
| Lean formalization | Not attempted in this repository |

The audit and computation are evidence, not substitutes for peer review.
Please report any gap, attribution issue, or earlier proof.

## Public Gaussian-prime follow-on

The most concise shareable follow-on is
**[Kalinin's Gaussian Lucas congruence](GAUSSIAN_LUCAS.md)**. It gives the
statement, proof mechanism, exact \(p=3\) boundary, source paper, and
reproduction command. Its present status is an unchecked proof candidate,
not a peer-reviewed theorem.

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
- [PROOF.md](PROOF.md): the complete proof and references.
- [verification/verify_a183068.py](verification/verify_a183068.py): a small
  exact-integer regression check.
- [RELATED_RESULTS.md](RELATED_RESULTS.md): an index of every current result
  produced by the same program, separated by audit status.
- [GAUSSIAN_LUCAS.md](GAUSSIAN_LUCAS.md): the public entry point for the
  Gaussian-prime follow-on.
- [related-results/](related-results/): the complete related proof drafts and
  reductions. These are stored locally in this repository rather than merely
  linked from the larger working repository.
- [verification/related/](verification/related/): the corresponding exact
  checkers.
- [verification/run_all.py](verification/run_all.py): one command for all nine
  verification programs.

The broader working repository remains available at
[rbajaj5/oeis-conjecture-proofs](https://github.com/rbajaj5/oeis-conjecture-proofs).
