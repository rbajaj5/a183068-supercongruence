# Gaussian-prime follow-on: Kalinin's Lucas congruence

This is the short public entry point for a Gaussian-integer result that grew
out of the residue-stratification methods used around the A183068
supercongruence.

## Status

**Complete proof candidate with exact checks; not peer reviewed or formally
verified.**

The source problem is Conjecture 3 in Nikita Kalinin,
["Wolstenholme's theorem over Gaussian integers"](https://arxiv.org/abs/2504.07978)
(2025; subsequently published in *Functiones et Approximatio Commentarii
Mathematici*).

The detailed proof and the neighboring results are in
[GaussianWolstenholmeCitationNetwork.md](related-results/GaussianWolstenholmeCitationNetwork.md#5-the-gaussian-lucas-congruence).

## The coefficient

For integers $A\ge C\ge1$ and $B\ge D\ge1$, Kalinin defines

```math
\left[\begin{matrix}A+Bi\\ C+Di\end{matrix}\right]
=
\frac{
\displaystyle\prod_{a=0}^{C-1}\prod_{b=0}^{D-1}
\bigl(A-a+(B-b)i\bigr)}
{\displaystyle\prod_{a=1}^{C}\prod_{b=1}^{D}(a+bi)}.
```

These rectangular coefficients are generally rational Gaussian numbers, not
ordinary Gaussian integers.

## Proposed theorem

Let $p>5$ be a rational prime satisfying $p\equiv3\pmod4$. Then

```math
\left[\begin{matrix}pA+pBi\\pC+pDi\end{matrix}\right]
\equiv
\left[\begin{matrix}A+Bi\\C+Di\end{matrix}\right]
\pmod {p^3}.
```

Thus the conjecture holds in the inert-prime regime of the theorem immediately
preceding it in Kalinin's paper.

The restriction matters:

- $p=3$ is an exact boundary. The choice
  $(A,B,C,D)=(1,2,1,1)$ has difference divisible by $3^2$ but not
  $3^3$.
- A rational prime $p\equiv1\pmod4$ splits in $\mathbb Z[i]$, so a
  split-prime analogue must choose a Gaussian prime $\pi\mid p$ and be
  formulated $\pi$-adically. It is a separate problem.

## Proof mechanism

The proof uses one complete nonzero residue block

```math
H_p(Z)=
\prod_{\substack{1\leq a,b\leq p\\(a,b)\neq(p,p)}}
(pZ+a+bi).
```

Four facts finish the argument:

1. Because $p\equiv3\pmod4$, the nonzero residue pairs form the unit group
   of $\mathbb F_{p^2}$.
2. Kalinin's Gaussian Wolstenholme theorem controls the reciprocal sum over
   the interior of the block.
3. Classical Wolstenholme and
   $\sum_{a=1}^{p-1}a^{-2}\equiv0\pmod p$ control its two axes.
4. Consequently $H_p(Z)\equiv H_p(0)\pmod {p^3}$. Partitioning each scaled
   rectangle into these blocks makes every block factor cancel, leaving the
   unscaled coefficient.

The last step also requires $p$-integrality of the unscaled coefficient.
That follows level by level: an interval of $C$ consecutive integers
contains at least $\lfloor C/p^j\rfloor$ multiples of $p^j$, and
similarly for $D$.

## Reproduction

Run the combined exact checker:

```text
python verification/related/verify_gaussian_wolstenholme.py
```

It checks the Gaussian Lucas congruence over small rectangles, the complete
residue-block congruence, the $p=3$ boundary, and the two other results in
the full Gaussian citation-network note.

## Why it belongs here

The A183068 proof stratifies summands by $p$-adic valuation and transfers
the surviving stratum by scaling. The Gaussian proof replaces scaling of
multinomial coefficients by translation of complete residue blocks. Both are
instances of the same program:

> identify the low-valuation stratum, prove that symmetry kills its error, and
> transfer the remaining structure between adjacent $p$-adic scales.

That connection is methodological rather than a claimed cryptographic
application. It may become relevant wherever arithmetic protocols use
extension fields, Gaussian integers, or explicit prime-power congruence
bounds.
