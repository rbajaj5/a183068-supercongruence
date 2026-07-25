# Related supercongruence results

This page keeps Paul D. Hanna informed about developments that grew out of the
A183068 proof without mixing them into the proof itself.

## Status key

- **Audited draft:** received a separate machine-assisted referee-style audit,
  but is not peer reviewed.
- **Unchecked candidate:** exact tests pass, but the written proof and
  literature priority still need independent review.
- **Reduction only:** useful progress, not a claimed solution.

## Direct line from A183068

| Result | Relationship | Status |
| --- | --- | --- |
| A183068 modulo $p^{2r}$ for every prime | The core named conjecture | Audited draft |
| [Landau-depth synthesis](https://github.com/rbajaj5/oeis-conjecture-proofs/blob/agent/exact-modulo-bias/unchecked-by-fable/LandauDepthSupercongruenceSynthesis.md) | Extracts the carry-and-scaling argument into a computable criterion; gives an infinite all-prime $p^{2r}$ family containing A183068 and an all-prime $p^{3r}$ subfamily | Unchecked candidate |
| [Gaussian Frobenius twists](https://github.com/rbajaj5/oeis-conjecture-proofs/blob/agent/exact-modulo-bias/unchecked-by-fable/supercongruence-program/GaussianFrobeniusTwists.md) | Lifts a termwise supercongruence to roots-of-unity weights; the $i^k$-twist detects split versus inert primes in $\mathbb Z[i]$ | Unchecked candidate |

The Landau-depth synthesis is the most important direct generalization. It
explains which part of the A183068 proof is special and which part is reusable.

## Neighboring literature reached by the method

| Result | Relationship | Status |
| --- | --- | --- |
| [Cubic $(\eta)$ congruence at $p=3$](https://github.com/rbajaj5/oeis-conjecture-proofs/blob/agent/exact-modulo-bias/unchecked-by-fable/supercongruence-program/EtaPrime3CubicExtension.md) | Uses the same valuation-versus-scaling budget to address a small prime omitted from a published theorem | Unchecked candidate |
| [Gaussian Wolstenholme citation network](https://github.com/rbajaj5/oeis-conjecture-proofs/blob/agent/exact-modulo-bias/unchecked-by-fable/supercongruence-program/GaussianWolstenholmeCitationNetwork.md) | Applies related residue-block ideas in Gaussian-integer arithmetic; contains a Gaussian Lucas proof candidate, a polynomial-product proof candidate, and a corrected reciprocal-power statement | Unchecked candidate |
| [Binary $s_{18}$ problem](https://github.com/rbajaj5/oeis-conjecture-proofs/blob/agent/exact-modulo-bias/unchecked-by-fable/supercongruence-program/S18TwoAdicReduction.md) | Reduces a published binary supercongruence to one sharpened scaling lemma | Reduction only |

These neighboring results are not all logical consequences of A183068. Their
connection is methodological: $p$-adic residue strata supply vanishing, and a
scaling or translation map controls the surviving terms.

## Gaussian-prime terminology

Gaussian integers are numbers $a+bi$ with $a,b\in\mathbb Z$. A Gaussian
prime is an irreducible element of this ring. Ordinary primes
$p\equiv3\pmod4$ remain prime (are *inert*), while primes
$p\equiv1\pmod4$ split; for example,

$$
5=(2+i)(2-i).
$$

The Gaussian work above concerns congruences in this enlarged arithmetic. It
does not claim a result about the distribution of Gaussian primes or an
immediate cryptographic application.

## Communication policy

Only stable, reviewable developments should be added here. Speculative searches
and failed experiments belong in the working repository. The next update
should follow independent review of the Gaussian and Landau-depth candidates.

