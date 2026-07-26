# Audit log

This file records machine-assisted audits of the exact public proof text.
An audit is evidence about a draft, not peer review or formal verification.

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
