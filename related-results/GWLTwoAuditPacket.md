# GWL-TWO audit packet

**Claim entry date:** 2026-07-26 (first theorem commit `6784eb5`).

**Audit checkpoint:** 2026-08-16.

**Author-completeness:** apparently gapless candidate.

**Audit status:** machine-assisted exact-text audits; no conventional
specialist review.

**Priority status:** named-corpus audit incomplete; no novelty claim.

This packet controls the current review queue. If the listed obligations are
not closed by the checkpoint, GWL-TWO leaves the active rankings and returns
to unindexed intake without deleting its proof or history.

## Statement under review

Let `varpi = 1+i`, normalized by `v_varpi(varpi)=1` and
`v_varpi(2)=2`. For the explicitly defined rectangular Gaussian product `Q`
and every admissible nontrivial rectangle, the candidate theorem asserts

```math
v_\varpi(R_{2,r}-1)
=6r-3+v_\varpi\!\left(CD(A-C+i(B-D))\right)
```

for `r >= 2`, together with the stated leading residue and the lower bound
`v_varpi(Delta_{2,r}) >= 6r-4`.

The controlling proof is
[`GaussianLucasRamifiedTwoTheorem.md`](GaussianLucasRamifiedTwoTheorem.md).

## Ramified-place obligations

| Obligation | Current disposition | Remaining action |
| --- | --- | --- |
| Ratio and nonvanishing | `Q` is an explicit element of `Q(i)`, not an associate class; every displayed factor is nonzero under the stated inequalities | Specialist rederive the five-product identity |
| Unit ambiguity | The explicit product fixes the representative; valuation is associate-invariant | Retain the explicit convention in every quotation |
| Conjugation | Reindexing gives `Q(b,a;d,c) = conjugate(Q(a,b;c,d))`; the leading residue is symmetric after reducing `i` modulo `varpi` | Exact checker now tests swapped rectangles |
| Logarithm domain | Every local increment has valuation at least `2r-1 >= 3` | Confirm no line uses the weaker unramified domain |
| Exponential domain | Every exponentiated leading term has valuation at least `6r-3 >= 9` | Confirm relative-error precision survives exponentiation |
| Principal-unit torsion | The nontrivial elements of `mu_4` lie below `1+varpi^3 O`; the argument works inside the torsion-free depth-three domain | Check that no uniqueness claim is made on all principal units |
| Reciprocal denominators | The sums live in `Q_2(i)` and need not be integral termwise; Lemma 1 tracks their possible negative valuation | Recheck every valuation loss in the lift induction |
| Base level | Seven exact reciprocal sums at `r=2` are tabulated | Independent transcription check |
| Gaussian sharpness | `(A,B;C,D)=(1,2;1,1)` is genuinely Gaussian and attains `6r-3` at `r=2` | Repeat from the product definition |
| Difference bound | Requires the separate lower-scale valuation bound `v(Q)>=-1` | Recheck the parity induction and equality boundary |

## Checker evidence

Run:

```text
python verification/related/verify_gaussian_lucas_ramified_audit.py
```

The checker verifies the exact formula on nested finite grids, tests an
extended scale, checks conjugation, checks the log/exp depth and the `mu_4`
boundary, and reports its kill rate against near-miss statement mutations.
These checks test the transcription and boundary handling; they are not a
proof.

## Priority corpus

The GWL-TWO priority audit must include:

1. Kalinin's definition and odd-prime conjectures;
2. Gaussian Wolstenholme and Lucas-type literature;
3. work on the ramified prime in `Z[i]` and dyadic Gaussian factorials;
4. forward citations of the closest anchor papers; and
5. searches by the exact slopes `6r-3` and `6r-4`, the mixed block `U_r`,
   and the leading factor `CD(A-C+i(B-D))`.

An unsuccessful search remains an incomplete priority audit until a
specialist has reviewed the corpus.
