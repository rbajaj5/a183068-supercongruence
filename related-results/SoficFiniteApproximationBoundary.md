# Sofic finite approximation: a boundary note

**Status:** literature and provenance note; the August 2026 nonsofic-group
theorem is accepted here as an external, Lean-certified result. No
supercongruence is claimed.

This note records a useful distinction that is easy to lose in discussion:

1. **Sofic groups exist.** This is classical and elementary.
2. Until August 2026, the open question was whether **every** countable group
   is sofic, equivalently whether a nonsofic group exists.
3. OpenAI announced a construction of a nonsofic group on August 1, 2026 and
   released a Lean artifact. This repository accepts the result as an external
   theorem, not as a theorem reproved here and not as a premise of any
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
for a finitely presented nonsofic group.  The announcement also says that
OpenAI takes responsibility for the correctness of the results after humans
helped prepare the manuscripts and the model formalized the arguments.

That establishes four provenance facts:

- the document is an authentic public claim, not merely a fabricated
  screenshot;
- a substantial formal artifact accompanies it; and
- the organization making the claim expressly accepts responsibility for its
  correctness;
- the claim is recent enough that surveys and preprints written before the
  announcement still describing the problem as open are not refutations.

The public certificate states the theorem

```math
\exists G,\quad G\text{ is finitely presented and }G\text{ is not sofic}.
```

The corresponding Lean declaration is
`SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group`.
The published audit records zero `sorry` declarations and only Lean's standard
`propext`, `Classical.choice`, and `Quot.sound` axioms. This is strong enough
for the repository to use the theorem as an external mathematical input.
Nothing in the supercongruence proofs depends on it.

Its current label here is therefore:

> **Accepted external theorem with a public Lean certificate; logically
> independent of the arithmetic results in this repository.**

An older source that merely says the problem was open when it was written is
not a counter-audit. The status change here rests on the released theorem, its
named Lean endpoint, its recorded axiom audit, and the subsequent expert
explanation of the proof mechanism.

### Three groups that should not be conflated

The construction uses three groups with different jobs:

1. The commuting subgroup $J\cong V$ is Thompson's group $V$. Its role is to
   provide the contradiction: it is finitely presented, infinite, simple, and
   not LEF. The argument does **not** conclude merely from this that $V$ is
   nonsofic.
2. The elementary group
   $G=\operatorname{EL}_9(L_{\mathbb F_2}(1,2))$ is the explicit finitely
   generated group shown nonsofic by the expander-component argument. The
   construction does not need to prove that this particular $G$ is finitely
   presented.
3. A separate finite-table group $H_F$ is obtained by imposing the finitely
   many multiplication relations from a forbidden finite test $F\subset G$.
   It maps onto $G$, so it is infinite, and any sofic approximation of $H_F$
   would induce the forbidden finite model. Consequently $H_F$ is finitely
   presented and nonsofic.

This last finite-table passage is why the released theorem really does imply
the existence of a finitely presented nonsofic group. The fact that $V$, rather
than $G$, is the finitely presented group appearing inside the LEF
contradiction does not invalidate that separate conclusion.

## 4. The new mechanism: matching expander components

The accepted MathOverflow explanation by Andreas Thom isolates the real new
step. Earlier results provide two ingredients:

1. a sofic approximation of a property-$(T)$ group can be changed on a
   vanishing fraction of edges into a disjoint union of uniform expanders;
2. if the relevant property-$(T)$ generator graph is one expander, an
   asymptotically commuting group must be LEF.

The obstruction was that the first result gives many components, possibly of
different sizes, while the second needs one controlled component. The new
construction compares an original component $C$ with its images under
permutations representing the extra generators. If $m$ is a vertex-weighted
median component size, define

```math
f(z)=\frac{|C(z)|}{|C(z)|+m}.
```

Conjugation gives an almost one-sided inequality
$f(\tau_i z)\ge f(z)-o(1)$. Because $\tau_i$ is a permutation, the total
change of $f$ is exactly zero; hence small total decrease forces small total
increase. Expansion and a coarea estimate then concentrate $f$ near its
median $1/2$. Thus almost all relevant components have comparable sizes.
A transported component occupying more than half of an original component
cannot collide with another transported component, giving an asymptotically
injective matching. Restricting to a matched component recovers the
single-expander setting and forces a chosen non-LEF subgroup to be LEF, a
contradiction.

This is more specific than a generic appeal to concentration of measure or
Arzelà--Ascoli: permutation conservation upgrades one-sided control to
two-sided $L^1$ control, and expansion turns that control into component
matching.

Thom's useful verdict is therefore precise: the proof does not invent a new
source of expansion or a general new stability theorem. Its reusable novelty
is an **expander-component matching principle**. Median normalization,
permutation conservation, and ambient expansion make two earlier results fit
together in a setting where a disjoint union of unequal expanders had blocked
the single-expander theorem.

The exact finite identity underlying that upgrade is recorded as Lemma 1 in
the [ten-advances transfer ledger](OpenAITenAdvancesTransferLedger.md).
The [group-ring Gauss boundary](NonSoficGroupRingGaussBoundary.md) gives the
direct arithmetic follow-on: prime-order torsion exactly characterizes when
all coefficient-return sequences satisfy the ordinary Gauss tower.

## 5. The genuine connection to the supercongruence program

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

The more precise transferable lesson is the **conservation upgrade**. In the
nonsofic proof, a permutation makes the signed global defect vanish, so a
one-sided local estimate becomes a two-sided estimate. In a congruence proof,
the analogous useful move is to identify an exact block product, residue sum,
or involution whose signed defect vanishes before estimating valuations. This
is a search heuristic, not a deduction from group theory.

## 6. Repository policy

- Known sofic examples may be cited as exact finite-model anchors.
- The August 2026 nonsofic construction may be cited as an external theorem,
  with its exact Lean declaration and provenance attached.
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
- A. Thom, [answer to *What are the key new ideas in the proof of
  nonsoficity of groups in OpenAI's construction?*](https://mathoverflow.net/a/513885),
  MathOverflow, August 2026.
