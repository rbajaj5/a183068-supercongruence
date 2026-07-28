# Targeted audit of the current Roe--Turturean manuscript

## Status

This is a narrow audit of the July 26, 2026 manuscript
[*A Presentation of the Absolute Galois Group of $\mathbb Q_2$*][paper].
It is not a substitute for specialist review.

**Current result:** no new mathematical error was found in the portions
checked here.

The authors maintain both a [current errata page][errata] and a
[formalization repository][lean]. The repository's
[historical formalization findings][history] are especially useful: they
record three corrections, eleven load-bearing hypotheses, five fragility
remarks, and four transcription-control notes found against earlier
manuscript states. The present PDF has incorporated the three listed
corrections in the places checked below.

## Exact calculations independently checked

### Proposition C.10

Let $X$ be the odd $2$-adic root of

$$
X^3+2X^2+1=0,
$$

and put

$$
S=-\frac{X^3}{X^2+X+1},
\qquad
Y=-X^2.
$$

Exact arithmetic in the cubic algebra
$\mathbb Q[X]/(X^3+2X^2+1)$ gives

$$
X\equiv5\pmod {16},
\qquad
S\equiv13\pmod {16},
$$

and

$$
N(X)=-1,
\qquad
N(S)=\frac14,
\qquad
N(Y)=-1.
$$

These are precisely the congruences and norm values used in Proposition
C.10 and Proposition C.6.

### Appendix D.2: $S_3$

The checker enumerated the complete admissible search space with
$O_2(S_3)=1$, evaluated the paper's tame and wild words with its
right-conjugation convention, and tested generation. It found

- 12 admissible quadruples; and
- 6 surjective quadruples.

Thus the displayed value

$$
|\mathrm{Sur}(\Gamma_A,S_3)|=6
$$

is reproduced exactly.

### Appendix D.3: $S_4$

Using $O_2(S_4)=V_4$, the same exhaustive calculation found

- 288 admissible quadruples; and
- 72 surjective quadruples.

Thus the displayed value

$$
|\mathrm{Sur}(\Gamma_A,S_4)|=72
$$

is also reproduced exactly.

The executable certificate is
[`verification/related/verify_gq2_appendices.py`](../verification/related/verify_gq2_appendices.py).

## Historical findings checked against the current PDF

The formalization record lists three corrections against earlier versions.

1. A degree-two display omitted a cup term. The current development uses the
   corrected formula.
2. Lemma 2.5 used ambiguous finite-cardinality language. The current statement
   is a set-cardinality equality, and its proof first transports finiteness
   before applying the reconstruction argument.
3. A quadratic-form zero-count formula needed a nonzero-space hypothesis.
   The current uses occur in the nontrivial-simple-module context, and the
   later corollary states the nonzero hypothesis explicitly.

These are historical corrections, not newly discovered defects in the
current PDF.

## Remaining trust boundary

The Lean development is sorry-free, but the main theorem intentionally rests
on nine literature axioms. That is a much smaller and clearer audit boundary
than the full paper, not an elimination of external mathematics. The
project's own axiom review identifies the composite interfaces—especially
the marked dyadic orientation, peripheral cyclotomic action, and local norm
criterion—as the places where a citation must be checked together with the
translation into the repository's exact definitions.

For the current manuscript, Lemma 3.7 explicitly supplies the cyclotomic
surjectivity input before applying the peripheral-action theorem. The earlier
formalization concern that the bundled axiom could look stronger than its
single displayed citation therefore does not produce a paper-level gap.

## Audit policy

A candidate issue enters this file only after one of the following:

- an exact finite or symbolic countercalculation;
- a mismatch with a cited theorem checked in the cited source; or
- a missing hypothesis that is actually consumed by a later argument.

Numerical unease, an unfamiliar formulation, or a stronger Lean interface is
not by itself an erratum.

[paper]: https://roed314.github.io/gq2/paper.pdf
[errata]: https://roed314.github.io/gq2/errata/
[lean]: https://github.com/roed-math/gq2-lean
[history]: https://github.com/roed-math/gq2-lean/blob/master/docs/paper-errata.md
