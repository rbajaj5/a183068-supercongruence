# Sofic finite approximation: a boundary note

**Status:** literature and provenance note; no supercongruence is claimed.

This note records a useful distinction that is easy to lose in discussion:

1. **Sofic groups exist.** This is classical and elementary.
2. Until August 2026, the open question was whether **every** countable group
   is sofic, equivalently whether a nonsofic group exists.
3. OpenAI announced a construction of a nonsofic group on August 1, 2026 and
   released a Lean artifact.  This repository records that as a new external
   claim under review, not as a theorem proved here and not as a premise of any
   supercongruence proof.

The word *sofic* therefore must not be used as shorthand for *nonsofic*, and a
question about the new construction must not cast doubt on the large classical
class of known sofic groups.

## 1. Definition

Let $G$ be a countable group.  In one standard formulation, $G$ is sofic when
for every finite set $F\subset G$ and every $\varepsilon>0$ there are a finite
set $X$ and a map

```math
\sigma:F\longrightarrow \operatorname{Sym}(X)
```

which is approximately multiplicative on the products visible in $F$ and
which moves almost every point whenever $g\ne 1$.  Approximation is measured
with normalized Hamming distance on permutations.

This is a local finite-model property.  The approximating map need not be a
homomorphism on the whole group.

## 2. An exact anchor: finite groups are sofic

Let $G$ be finite and take $X=G$.  For $g\in G$, let

```math
\sigma_g(x)=gx.
```

Then

```math
\sigma_{gh}=\sigma_g\sigma_h
```

exactly.  If $g\ne 1$, the permutation $\sigma_g$ has no fixed point, since
$gx=x$ implies $g=1$.  Thus the left-regular action supplies an
$\varepsilon=0$ model on every finite subset.  Hence every finite group is
sofic.

Classically, the class is much larger: it contains every residually finite
group and every amenable group, and it is closed under several standard group
constructions.  Free groups, finitely generated abelian groups, and all finite
groups are therefore routine examples.

## 3. What changed in August 2026

OpenAI's August 1 announcement states that it constructed a nonsofic group and
released both a manuscript and a Lean certificate.  The associated public
repository contains `NonSoficGroup.lean` and states a final existence theorem
for a finitely presented nonsofic group.

That establishes three provenance facts:

- the document is an authentic public claim, not merely a fabricated
  screenshot;
- a substantial formal artifact accompanies it; and
- the claim is recent enough that surveys and preprints written before the
  announcement still describing the problem as open are not refutations.

It does **not** by itself establish specialist consensus.  A kernel-checked
formalization verifies a statement relative to its definitions, imported
library, and axioms; mathematical review must also check that these definitions
and reductions match the standard theorem.  No argument in this repository
depends on the announced nonsofic example.

The appropriate current label here is therefore:

> **External formalized claim; independent specialist review not recorded in
> this repository.**

Calling the claim "fake" would require a concrete defect, retraction, or
counter-audit.  None is supplied by an older source that merely says the
problem was open when that source was written.

## 4. The genuine connection to the supercongruence program

The connection is methodological, not deductive.

| Sofic approximation | Supercongruence tower |
| --- | --- |
| A finite multiplication table is approximated by permutations of a finite set. | Adjacent $p$-power levels are compared modulo a growing power of $p$. |
| Error is measured by normalized Hamming distance. | Error is measured by a $p$-adic or prime-ideal valuation. |
| One asks whether compatible local finite models exist for every finite test. | One asks whether carry, block, or Frobenius estimates persist uniformly through every level. |

Both settings reward finite certificates and explicit defect budgets.  But the
metrics, objects, and closure theorems differ, so no soficity theorem currently
proves a congruence in this repository.  The comparison is useful for audit
design: test a finite multiplication table or a finite congruence level, record
the error metric, and never infer a global theorem without the required
uniform passage.

## 5. Repository policy

- Known sofic examples may be cited as exact finite-model anchors.
- The August 2026 nonsofic construction remains in the literature/provenance
  lane until an independent specialist audit is recorded.
- It is excluded from `RANKINGS.md`, because this repository neither proves
  the result nor obtains a supercongruence from it.
- It must not be used to upgrade the status of any claim in `RESULT_INDEX.md`.

## References

- G. Elek and E. Szabo, [*On sofic groups*](https://arxiv.org/abs/math/0305352),
  2003.
- K. Juschenko, [*Sofic Groups*](https://web.ma.utexas.edu/users/juschenko/files/soficgroups.pdf),
  introductory notes recording the classical definition and known subclasses.
- OpenAI, [*Ten advances in mathematics and theoretical computer science*](https://openai.com/index/ten-advances-in-mathematics/),
  August 1, 2026.
- OpenAI, [`ten-proofs`](https://github.com/openai/ten-proofs), accompanying
  Lean certificates, including `NonSoficGroup.lean`.
