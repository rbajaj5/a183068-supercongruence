# Research update on Peter Bala's July 31 directions

**Status date:** August 3, 2026

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
| Recent factorial-ratio direction | A061164 and the public A364172--A364184 packet, with Peter's exact new list still pending | **Two uniform transfers proved:** A061164 follows from balanced integer factorials; residue-balanced rational gamma ratios inherit the same cubic tower. This fully closes A364175 using Radcliffe's July 2026 integrality proof and reduces the remaining fractional records to integrality |
| Bober sporadic follow-up | A295431--A295482 and 12 newly commented records | **Ordinary packet closed for $p\ge5$:** all 52 inherit the full $p^{3r}$ tower. All 15 visible fractional variants pass the rational-gamma test; A295456 at $N/2$ (A364176) now has proved integrality and an unconditional tower, leaving 14 visible integrality targets |

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
ordinary cubic tower for A061164.

The new [rational gamma-ratio theorem](RationalGammaRatioCubicTowers.md)
extends that transfer to fractional slopes.  If the slopes balance and each
nonzero residue class modulo $\mathbb Z$ has net multiplicity zero, the
adjacent quotient is $1$ modulo $p^{3r}$ for every $p\geq5$ away from the
fixed denominator.  Every record in the public A364172--A364184
fractional-factorial packet satisfies those hypotheses.

This has two immediate named payoffs. David Radcliffe proved A364175 integral
on July 19, 2026, and the rational-gamma theorem now proves its still-open
full cubic tower. The new affine-Landau lemma proves A364176 integral and the
rational-gamma theorem proves its tower. A364173 was already closed in this
repository. On the remaining records, the congruence component is proved in
$\mathbb Q_p$ and global integrality is the only unresolved assertion.

The same transfer proves the full all-row conjecture on A365025, including
A365026 and A365027, and every stable row $s\ge3$ of A364513, including the
named sequences A364515--A364517.  Row $1$ of A364513 (A364514) has an
affine odd-index formula and remains outside the homogeneous theorem.

## 5. August 3 addendum: Bober's sporadic packet

Peter's follow-up identifies the 52 Bober ratios and 12 records with new
fractional-index comments.  The
[Bober packet](BoberSporadicFactorialRatioPacket.md) gives the exact
disposition:

- every ordinary ratio A295431--A295482 satisfies the full $p^{3r}$ tower
  for $p\ge5$ by the balanced-factorial theorem;
- all 15 fractional formulas currently visible on OEIS pass the
  residue-balance test and therefore satisfy the rational $p$-adic tower;
- A295456 at $N/2$ is A364176, and its global integrality is proved by a
  five-case affine floor lemma; and
- the other 14 global integrality claims remain open, despite exact
  integrality through the first 31 values.

The A295464 email report is retained as pending because its new comment was
not yet visible on the approved OEIS page when this addendum was prepared.

## Next review package

The economical package to send after one week is:

1. the symmetric-box theorem and checker;
2. the balanced and rational factorial-ratio theorems, including A061164
   and the newly closed A364175 tower;
3. the three exact unresolved Apéry defects; and
4. the Bober 52 corollary, the completed A364176 theorem, and the remaining
   14-item fractional-integrality queue.

This distinguishes completed mathematics from the live queue and gives
Peter and Paul Hanna specific statements to inspect.
