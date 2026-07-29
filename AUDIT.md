# Audit log

This file records machine-assisted audits of the exact public proof text.
An audit is evidence about a draft, not peer review or formal verification.

All future all-prime audits also apply the repository's
[dyadic audit policy](DYADIC_POLICY.md). A report that checks only odd primes
does not certify an all-prime theorem; it must identify the binary
normalization, scaling sign, first-level boundary, and any required
cancellation.

## Exact-text audit, July 26, 2026

The second audit reported **no proof-level errors** and independently checked:

- 86 instances of the main congruence, including selected cases with $r=3$;
- the floor identity in Lemma 1 by hand and on 3,000 randomized
  configurations;
- the valuation bound in Lemma 1 on 385 systematic cases;
- Lemma 2 on 5,006 cases for $p=2,3,5$ and $s=0,1,2$;
- Lemma 3 on 334 cases; and
- the constant-term representation for $n=1,2,3$ by exact Laurent arithmetic.

### Correction made

The proof formerly said that finite tests found the exponent in Lemma 2 sharp
for each of $p=2,3,5$.  The audit reproduced sharpness for $p=3,5$ and for
$p=2$ at $s=0$, but not for $p=2$ with $s\ge1$.  In the latter range its
finite search attained $3s+2$, one power stronger than the lemma's stated
$3s+1$ bound.

The theorem and its proof use only the weaker one-directional bound, so this
changes no theorem.  The sharpness sentence in `PROOF.md` has been narrowed.

### Expository repairs made

- stated explicitly that a product of units congruent to $1$ modulo $p^m$
  remains congruent to $1$ modulo $p^m$;
- added Straub's companion paper on multivariate Apéry supercongruences; and
- replaced set braces in inline mathematics by `\lbrace` and `\rbrace` to
  avoid a Markdown rendering ambiguity.

### Remaining review obligations

- conventional specialist review;
- an independent literature-priority search; and
- formal verification, if pursued separately.

## Landau-depth internal recheck, July 26, 2026

A repository survey identified
`related-results/LandauDepthSupercongruenceSynthesis.md` as the highest-value
next target, but explicitly accepted the note's claims rather than auditing
them. A separate internal line-by-line recheck was therefore performed.

### Proof obligations rechecked

- the active-level identity obtained from Legendre's formula;
- the exact transfer budget
  $d(r-1-s)+3(s+1)-\varepsilon_p$;
- both branches of the generic transfer theorem;
- the residue and uniform-divisibility compensation at $p=2,3$;
- the closed Landau fiber of the two-parameter family; and
- the divisibility arguments used by the quadratic and cubic corollaries.

No proof-level error was found. This was an internal machine-assisted recheck,
not an independent audit.

### Checker strengthened

The checker formerly compared the closed Landau-fiber formula with the same
formula. It now computes one side directly from the defining floor sum. It
also verifies:

- 21,420 active-level decompositions against direct Legendre valuations; and
- 1,386 generic and compensated termwise transfer bounds before summation.

Together with the existing family and divisibility checks, the Landau checker
now performs 79,983 exact checks.

### Priority boundary

Targeted searches located the broader factorial-ratio and sporadic-sequence
frameworks already cited in the note, but did not locate the exact
small-prime deficit formula or the displayed two-parameter all-prime
families. Absence from those searches is not a priority determination.
