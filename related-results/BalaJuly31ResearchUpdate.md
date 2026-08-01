# Research update on Peter Bala's July 31 directions

**Status date:** July 31, 2026

This page is a shareable status ledger for the three groups Peter Bala
identified by email.  A row marked **proved** has a written argument in this
repository.  A row marked **open** remains open even when extensive exact
checks pass.

## Current disposition

| Direction | Exact records | Current mathematical status |
| --- | --- | --- |
| Superfactorial analogues | A008793, A352656, A352657 | **Proved in one parameter family:** every $N\times N\times cN$ plane-partition number satisfies the proposed all-prime $p^{4r}$ Frobenius tower |
| Enhanced combinations of Apéry numbers | A352655, A357506, A357567, A357956, A357959 and two nonlinear companions | **Exact reduction:** all claims collapse to three linear adjacent-defect congruences; those three congruences remain open |
| Paired ordinary/shifted towers | A363984, A376459--A376466 | **Open:** the source statements are captured; no published theorem has yet been matched to all hypotheses |
| Recent factorial-ratio direction | A061164, with Peter's complete A-number list still pending | **A061164 cubic tower proved:** it is an immediate balanced-factorial consequence of classical binomial scaling; integrality and normalization remain the first obligations for the pending fractional-factorial records |

## 1. Superfactorial family: closed uniformly

For every integer $c\geq1$, let

```math
B_c(N)=\prod_{i,j=1}^{N}\frac{cN+i+j-1}{i+j-1}.
```

The [symmetric-box theorem](SymmetricBoxPlanePartitionTower.md) proves, for
every prime $p$ and all $n,r\geq1$,

```math
B_c(np^r)\equiv B_c(np^{r-1})^p\pmod {p^{4r}}.
```

The cases $c=1,2,3$ are A008793, A352656, and A352657.  The proof includes
the odd-prime reciprocal-block argument and the separate binary parity
repair.

## 2. Enhanced Apéry combinations: one residual packet

The [rank-one defect packet](AperyRankOneDefectPacket.md) proves that the five
named records and both multiplicative companions introduce only three
independent arithmetic obligations.  This is a genuine consolidation, not a
proof of those obligations.  The next useful output is one of:

- a proof of the three linear defect congruences;
- a counterexample to one of them; or
- a published theorem whose hypotheses match those exact defects.

## 3. Paired ordinary and shifted towers: source captured, proof open

The live pages for [A363984](https://oeis.org/A363984) and
[A376459](https://oeis.org/A376459)--[A376466](https://oeis.org/A376466)
conjecture both

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{3r}}
```

and

```math
u(np^r-1)\equiv u(np^{r-1}-1)\pmod {p^{3r}}
```

for $p\geq5$.  Straub's theorem explains this pair for the two classical
Apéry sequences, but the new sequences must first be identified with his
specific multivariate coefficient family.  A generic constant-term formula
is not enough.

In particular, A376460 received a four-variable constant-term formula in
May 2026.  Direct comparison of its MacMahon matrix with Straub's block
denominators does **not** give an immediate parameter match.  The formula is
useful structure, but citing Straub at this point would leave a gap.

## 4. Recent factorial ratios: the congruence step is automatic

The [balanced factorial-ratio theorem](BalancedFactorialRatioCubicTowers.md)
shows that every integral ratio

```math
F(N)=\prod_m((mN)!)^{c_m},
\qquad \sum_m m c_m=0,
```

satisfies the full $p^{3r}$ adjacent tower for $p\geq5$.  This proves the
ordinary cubic tower for A061164.  For Peter's newer fractional-factorial
entries, the remaining source work is to obtain the exact A-number list and
audit each integrality/normalization statement.

## Next review package

The economical package to send after one week is:

1. the symmetric-box theorem and checker;
2. the balanced factorial-ratio theorem and A061164 corollary;
3. the three exact unresolved Apéry defects; and
4. a request for Peter's complete list of the new fractional-factorial
   A-numbers.

This distinguishes completed mathematics from the live queue and gives
Peter and Paul Hanna specific statements to inspect.
