# The 110-record Bala proof campaign

**Snapshot date:** July 29, 2026

**Status:** complete record-level ledger; proof work remains in progress

The reproducible OEIS search used by this repository returned 110 distinct
records. That does **not** mean that it returned 110 distinct open
conjectures. A record may contain several claims, a claim may already follow
from a published theorem, and one parameterized theorem may settle several
records at once.

The machine-readable ledger is
[`data/bala_110_campaign.tsv`](../data/bala_110_campaign.tsv). It assigns
every record:

1. one of the five proof routes from the
   [Gaussian generalization map](BalaGaussianGeneralizationMap.md);
2. a conservative current status;
3. the evidence controlling that status; and
4. the next proof operation.

## Current disposition

| Route | Records | Proved here | Published source | Partial | No explicit open target | Queued |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| T: finite-sum transfer | 40 | 2 | 3 | 1 | 2 | 32 |
| C: coefficient/constant term | 37 | 0 | 6 | 3 | 0 | 28 |
| F: factorial/block product | 14 | 6 | 3 | 0 | 0 | 5 |
| M: modular or infinite product | 14 | 0 | 0 | 0 | 0 | 14 |
| D: derived or inherited | 5 | 0 | 0 | 0 | 0 | 5 |
| **Total** | **110** | **8** | **12** | **4** | **2** | **84** |

The eight `proved-here` records are A091527, A141057, A262732, A275652,
A275654, A288470, A357568, and A364506. The
twelve `published-source` records are A002426, A082758, A103882, A168597,
A176335, A184423, A186420, A234839, A363864, A363867, A363871, and
A364509. The four partial records are A228960, A333592, A350383, and
A380290. A005259 and A005260 are retained as search-corpus records but
classified `no-explicit-open`: their live matches concern unrelated Bala
material, not a Bala supercongruence conjecture.

These labels refer only to the exact statements already matched. They do not
declare every comment on the corresponding OEIS page solved.

## Status definitions

- `proved-here`: a complete proof candidate in this repository matches the
  displayed OEIS conjecture.
- `published-source`: the live OEIS record or the repository's source audit
  identifies a published theorem implying the claim.
- `partial`: the repository proves a baseline, coefficientwise version, or
  subfamily, but a stronger statement on the record remains.
- `no-explicit-open`: the reproducible text search found the record, but a
  live open supercongruence attributable to Bala was not located.
- `queued`: the record is routed, but its exact conjecture still needs to be
  extracted and matched against the route theorem before proof work begins.

## Proof order

The campaign does not use A-number order. It uses expected proof yield.

1. **T route:** look for a termwise discard-and-rescale proof. A288470 is
   the model: two carries close the integer tower and automatically produce
   a Gaussian Frobenius twist.
2. **F route:** rewrite the term as a multinomial or an integral Laurent
   product. A364506 is one model.  The odd-unit block theorem is the second:
   it closes A091527 and A262732 simultaneously by splitting a half-integral
   factorial product into its divisible factors and complete odd unit blocks.
   The Dixon--Legendre theorem is the third: it packages A275652 and A275654
   into one parameter family and reduces their fractional factorials to
   ordinary binomial transfer plus a half-binomial unit block.
3. **C route:** first determine whether a direct finite-sum factorization is
   simpler than invoking Dwork or Cartier operators.
4. **M route:** take a p-adic logarithm and isolate the first moment that
   survives the product balance.
5. **D route:** identify the parent sequence and prove that the claimed
   congruence is inherited before treating it as an independent problem.

## Promotion rule

A row moves out of `queued` only when the exact source statement has been
copied into a proof note and one of the following is present:

- a complete proof;
- a precise reduction to a published theorem with parameter matching;
- a counterexample; or
- a smaller named obstruction that is explicitly marked unresolved.

Finite testing alone does not change the status to `proved-here`.

## Verification

Run

```text
python verification/related/verify_bala_110_campaign.py
```

The checker verifies the 110 unique A-numbers, the route totals
$40+37+14+14+5$, the five status totals, and the presence of a nonempty
next action for every record.
