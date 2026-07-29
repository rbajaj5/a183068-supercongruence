# Exact pilot for Gaussian twists in the Bala queue

**Status:** exact computational triage; not a proof

**Scope:** 195 adjacent-scale tests across three finite-sum sequences

## 1. Definition

For each displayed integer summand \(F(N,k)\), define

```math
T_i(N)=\sum_{k=0}^N i^kF(N,k)\in\mathbb Z[i].
```

At an odd prime \(p\), the natural adjacent-scale comparison is

```math
T_i(np^r)-T_{i^p}(np^{r-1}).
\qquad\text{(1)}
```

Thus the lower term is unchanged when \(p\equiv1\pmod4\) and conjugated when
\(p\equiv3\pmod4\).

The script computes the real and imaginary parts of (1) exactly and records

```math
\min\{v_p(\Re(1)),v_p(\Im(1))\}.
```

No floating-point arithmetic is used.

## 2. Sequences tested

```math
\begin{aligned}
\text{A005260:}\quad
F(N,k)&=\binom Nk^4,\\
\text{A005259:}\quad
F(N,k)&=\left(\binom Nk\binom{N+k}{k}\right)^2,\\
\text{A333592:}\quad
F(N,k)&=\binom{N+k-1}{k}^2.
\end{aligned}
```

For each sequence the test grid is

```text
p in {3,5,7,11,13}
r = 1, n = 1..8
r = 2, n = 1..4
r = 3, n = 1
```

This gives 65 exact cases per sequence and 195 in total.

## 3. Findings

| Sequence | Bound holding throughout the grid | Equality occurs? | Stronger bound rejected? |
| --- | --- | --- | --- |
| A005260 | \(v_p\ge3r\) for \(p\ge5\); \(v_3\ge2r\) | Yes | \(v_3\ge3r\), e.g. \(p=3,r=1,n=2\) has valuation \(2\) |
| A005259 | \(v_p\ge2r\) | Yes | \(v_p\ge3r\), e.g. \(p=5,r=1,n=1\) has valuation \(2\) |
| A333592 | \(v_p\ge2r\) | Yes | \(v_p\ge3r\), e.g. \(p=5,r=1,n=1\) has valuation \(2\) |

The failures of the stronger statements are exact integer witnesses, not
numerical roundoff.

## 4. Interpretation

The pilot establishes a useful queue boundary:

> An untwisted cubic supercongruence does not automatically remain cubic
> after a fourth-root-of-unity twist.

The twist exposes residue classes of \(k\) that can cancel after setting the
weight to \(1\).  A proof must therefore return to the termwise valuation and
transfer lemmas.  If those lemmas hold term by term to exponent \(e\), the
[general twist theorem](GaussianFrobeniusTwists.md) applies.  If the integer
proof obtains its final power only after summing, that power may disappear.

A005260 is the strongest next target in this pilot: the data suggest that
its depth-three behavior survives the Gaussian twist for \(p\ge5\), while
\(p=3\) is a genuine lower-exponent boundary.  This remains a conjectural
interpretation until a termwise proof is supplied.

## 5. Reproduction

Run:

```text
python verification/related/verify_bala_gaussian_twist_pilot.py
```

The output reports all 195 passed lower-bound checks and prints the exact
equality witnesses used to reject the naive stronger extrapolations.
