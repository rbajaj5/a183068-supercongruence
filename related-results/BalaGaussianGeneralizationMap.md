# Gaussian generalization map for the Bala--OEIS queue

**Census date:** July 28, 2026

**Status:** complete routing of the reproducible 110-record census; this is a
research map, not a claim that 110 Gaussian theorems have been proved

## 1. The question being classified

The repository's
[Bala--OEIS census](SupercongruenceLiteratureCensus.md) starts from the
reproducible OEIS query

> ["Peter Bala" supercongruence](https://oeis.org/search?q=%22Peter+Bala%22+supercongruence).

It returned 110 records on July 28, 2026.  This note asks a narrower question:

> What would a mathematically natural Gaussian-prime generalization of each
> record actually mean?

There is no single answer.  In particular, inserting \(i^k\) into every
displayed sum would manufacture formulas without preserving their proof
mechanism.  The 110 records instead divide into five routes:

| Route | Count | Natural first operation |
| --- | ---: | --- |
| **T: finite-sum twist** | 40 | Weight a summand by \(i^k\) or a more general root of unity and track Frobenius |
| **C: coefficient/constant term** | 37 | Extend the coefficient ring to \(\mathbb Z[i]\) and use Cartier/Dwork Frobenius |
| **F: factorial or block product** | 14 | Build a genuinely two-dimensional Gaussian factorial/block analogue |
| **M: modular or partition product** | 14 | Decompose into quartic-character or CM eigenspaces |
| **D: derived sequence** | 5 | First prove compatibility of the Gaussian structures of the component sequences |

The counts are exhaustive and disjoint:

```text
40 + 37 + 14 + 14 + 5 = 110.
```

The classification is about proof architecture, not difficulty or novelty.

## 2. Three local behaviors, not one

Any Gaussian-prime statement must identify the local case.

### Split primes

If \(p\equiv1\pmod4\), then

```math
(p)=(\pi)(\bar\pi)
```

in \(\mathbb Z[i]\), and rational Frobenius fixes \(i\).  A congruence modulo
\(p^e\) is simultaneously a congruence modulo \(\pi^e\) and
\(\bar\pi^e\).  It does **not** distinguish the two prime factors.  A
one-sided theorem modulo \(\pi^e\), normalized by a chosen primary Gaussian
prime, is a stronger target.

### Inert primes

If \(p\equiv3\pmod4\), then \(p\) remains prime in \(\mathbb Z[i]\), the
residue field is \(\mathbb F_{p^2}\), and Frobenius sends

```math
i\longmapsto i^p=-i.
```

Thus a twisted sequence naturally returns to its complex conjugate at the
preceding scale.

### The ramified prime

At \(p=2\),

```math
2=-i(1+i)^2.
```

The relevant normalized valuation is therefore

```math
v_{1+i}(2)=2.
```

The map \(i\mapsto i^2=-1\) is not a residue-field automorphism of the same
kind as at an odd prime.  A binary cross-twist or a theorem in the
\((1+i)\)-adic valuation must be proved separately.  The repository's
[dyadic policy](../DYADIC_POLICY.md) applies to every route below.

## 3. What counts as a Gaussian generalization

The following three operations should not be conflated.

1. **Gaussian coefficient extension.**  An integer formula is simply viewed
   in \(\mathbb Z[i]\).  This is formal and usually adds no theorem.
2. **Gaussian Frobenius twist.**  A roots-of-unity weighted sequence changes
   by \(i\mapsto i^p\) between adjacent \(p\)-power scales.  This can be a
   useful new corollary of a termwise transfer proof.
3. **Gaussian prime-ideal theorem.**  A result is normalized at a chosen
   prime \(\pi\), or treats the ramified uniformizer \(1+i\), and proves a
   valuation not visible modulo the rational ideal \((p)\).

Only the third operation reaches genuinely new local arithmetic without
additional qualifications.  The second is reusable and informative, but it
is often an elementary consequence of an integer termwise theorem.

## 4. Route T: finite-sum Frobenius twists

For a summand \(F(N,k)\), put

```math
T_i(N)=\sum_k i^kF(N,k).
```

If a proof has already established

```math
F(np^r,k)\equiv0\pmod {p^e}\quad(p\nmid k)
```

and

```math
F(np^r,p\ell)\equiv F(np^{r-1},\ell)\pmod {p^e},
```

then the
[Gaussian Frobenius-twist theorem](GaussianFrobeniusTwists.md) gives

```math
T_i(np^r)\equiv T_{i^p}(np^{r-1})\pmod {p^e}.
```

This is the lowest-cost route because the Gaussian statement follows after
the two integer termwise hypotheses are proved.  The formula of a sequence
alone does not establish either hypothesis.

The 40 route-T records are:

```text
A001850 A002003 A002895 A003161 A003162 A005258 A005259 A005260
A079489 A082758 A103882 A112028 A112029 A124435 A132303 A141057
A143583 A183069 A183204 A198060 A198256 A198258 A208675 A212334
A219562 A234839 A244973 A260667 A288470 A333592 A357510 A357512
A361889 A361892 A362676 A363985 A370101 A370102 A376458 A376466
```

The termwise hypotheses are now proved for A288470 in the
[odd-prime double-binomial theorem](A288470OddPrimeTower.md). Consequently
its $i^k$-weighted sum satisfies the exact Frobenius-twist congruence modulo
$p^{2r}$ for every odd prime: split primes preserve the twist, while inert
primes conjugate it.

### First exact pilot

The [pilot report](BalaGaussianTwistPilot.md) tests three representative
route-T sequences.  It finds:

- A005260 retains \(p^{3r}\) in the tested Gaussian twists for \(p\ge5\),
  but the sharp tested exponent at the small-prime boundary is only
  \(3^{3r-1}\);
- A005259 and A333592 retain \(p^{2r}\) in the tested range; and
- both have exact witnesses against a naive \(p^{3r}\) twisted statement.

The A005260 observation has since been proved in the stronger coefficientwise
form

```math
P_{np^r}(X)\equiv P_{np^{r-1}}(X^p).
```

The [binomial-power Frobenius theorem](BinomialPowerFrobeniusTheorem.md)
proves this as its \(m=4\) case and gives a unified result for every
\(m\ge3\).  The
[quadratic queue theorem](QuadraticGaussianQueueTheorem.md) proves the
A005259 and A333592 observations.  Thus every positive target in the pilot
is now closed at its tested termwise exponent.  The exact counterexamples
still demonstrate that the twist exponent must be determined from the
termwise filtration rather than copied from the untwisted theorem.

## 5. Route C: constant terms and Frobenius base change

For a Laurent polynomial \(P\), a sequence of the form

```math
a(n)=\mathrm{CT}(P^n)
```

or a diagonal/coefficient sequence is naturally transported to
\(\mathbb Z[i]\).  The substantive question is then whether the relevant
Cartier operator, Newton polytope, or Hasse--Witt matrix yields a Frobenius
congruence over that coefficient ring.

This is not the same as multiplying the \(k\)-th summand by \(i^k\).  The
correct Gaussian object may instead be a Frobenius eigenspace or a quartic
character projection of the original period.

The 37 route-C records are:

```text
A002426 A005725 A006318 A036917 A060941 A108625 A108628 A143007
A156554 A168597 A176335 A177316 A228960 A245926 A246437 A263843
A281267 A331562 A333090 A333091 A333092 A333093 A333095 A333096
A333097 A348410 A350383 A351857 A351858 A352373 A362722 A362733
A363864 A363867 A363871 A364303 A380290
```

The first two inspections, A228960 and A350383, are now closed by the
[cyclotomic coefficient-pair theorem](CyclotomicCoefficientPairTheorem.md).
Their factorizations expose finite binomial sums, and a direct
discard-and-rescale proof is stronger and simpler than a Dwork conversion.

A380290 has also produced a closure at the generic quadratic exponent.  The
[colored Euler-product theorem](EulerProductGaussianTower.md) proves a
coefficientwise \(p^{2r}\) Frobenius law for arbitrary integral multicolored
products weighted by \(m^d\), \(d\ge1\), at every odd prime.  It contains the
full product packet in Bala's notes and gives a split/inert part-count twist.
Exact equality witnesses show that this Gaussian twist is only quadratic.
The remaining A380290 problem is therefore the special untwisted
\(p^{3r}\) gain, not the construction of a generic quadratic period model.
The [cubic Cartier-square reduction](EulerProductCubicCartierMoments.md)
now isolates that gain, and the four analogous route-M conjectures, in one
coefficientwise stratum estimate.  Thus the Gaussian coefficientwise
theorem supplies the uniform baseline, while the extra rational cubic
power is an explicit cancellation that is lost under a generic color
twist.

The next economical unresolved inspection is A331562.  Its required output
is an explicit Laurent polynomial or rational diagonal and a written match
to a Dwork theorem, not another numerical congruence table.

Primary starting points are Mellit--Vlasenko's
[constant-term congruences](https://arxiv.org/abs/1306.5811) and
Vlasenko's higher Hasse--Witt formalism.  Their hypotheses still have to be
checked sequence by sequence.

## 6. Route F: Gaussian factorial and rectangular-block analogues

These records are driven by factorial ratios or finite products.  A
nontrivial Gaussian analogue replaces a one-dimensional factorial interval
by a two-dimensional Gaussian block, or by a generalized factorial adapted
to prime ideals.  Before asking for a supercongruence one must prove:

1. the proposed quotient is defined;
2. its Gaussian integrality or denominator valuation;
3. the correct normalization at split, inert, and ramified primes; and
4. the local block-product expansion.

The 14 route-F records are:

```text
A002897 A008978 A091527 A113424 A184423 A186420 A262732 A275652
A275654 A357509 A357568 A364173 A364506 A364509
```

Three integer problems in this route are now closed in the
[binomial-quotient cancellation note](BinomialQuotientCancellation.md).
The Laurent-binomial closure theorem proves every A364506 row for
\(p\ge5\).  A reduced-unit harmonic calculation proves the full
two-parameter A357509 family for \(p\ge5\) and the A357568 enhanced
family, including \(p=3\).  These are integer
supercongruences; defining a genuinely Gaussian block analogue remains a
different problem.

The remaining three source records have also been triaged in the
[coefficient-root note](CoefficientPowerGaussBaseline.md).  A002897's
former diagonal claim is already marked proved on the live record.
For A008978 and A113424, the displayed root series are now proved integral
and every variable-power family has an all-prime \(p^r\) tower; their
stronger \(p^{3r}\) refinements remain open.  Thus no route-F record remains
unclassified, although two retain genuine cubic work.

This route is closest to Kalinin's
[rectangular Gaussian products](https://arxiv.org/abs/2504.07978), but it is
also the easiest place to create an ill-defined analogy.  The repository
has now discharged A364173's rational integrality obligation, but a
prime-ideal analogue would still require its own Gaussian integrality and
normalization theorem.

## 7. Route M: modular products, partitions, and quartic characters

Partition products and modular-form sequences usually do not have a
distinguished summation index to twist.  Their natural Gaussian direction is
instead a decomposition under quartic characters or complex multiplication,
followed by a prime-ideal Frobenius statement.

The 14 route-M records are:

```text
A008485 A008705 A008793 A023871 A023873 A049505 A206622 A229452
A255672 A270913 A270919 A270922 A270924 A283271
```

A008793 is the highest-interest example in this route: its nonlinear
plane-partition congruence is naturally attacked through the \(p\)-adic
logarithm of MacMahon's product.  A Gaussian refinement would require a
quartic or CM factorization of that logarithm; merely replacing integers by
Gaussian integers does not define one.

The [modular-product prime-coefficient packet](ModularProductPrimeCoefficientPacket.md)
now completes the route's first pass. Seven records are proved here:
A008485, A008705, A255672, A270913, A270919, A270922, and A270924. Four
more records, A023871, A023873, A206622, and A283271, inherit a proved
\(p^{2r}\) baseline while retaining their conjectural \(p^{3r}\) gain.  The
[one-obstruction theorem](EulerProductCubicCartierMoments.md) now proves
that every term of logarithmic degree at least three already has cubic
depth, isolates the two weighted moments, and reduces both to one
coefficientwise Cartier-square estimate.  It also proves that A023871
cannot be extended to `p=5`, while exact checks show why A206622's
plus/minus product has a different prime-five boundary.
The [A229452 coefficient-root theorem](A229452CoefficientRootBaseline.md)
proves its all-\(m\) integrality and an all-prime \(p^r\) baseline for both
source parameter families.
The
[A049505 paired-product theorem](A049505SymmetricPlanePartitionCongruences.md)
proves all three of that record's congruences. The
[A008793 cube-product theorem](A008793CubePlanePartitionTower.md) now
proves that final all-prime \(p^{4r}\) conjecture, so route M has no queued
record.

Finite-field “Gaussian hypergeometric” functions can be relevant here
through Gauss sums and quartic characters.  The word *Gaussian* in that
literature does not itself mean arithmetic in \(\mathbb Z[i]\).  McCarthy's
[p-adic extension of Gaussian hypergeometric series](https://arxiv.org/abs/1204.1574)
is therefore a possible character-theoretic bridge, not evidence that these
14 records already have Gaussian-integer analogues.

## 8. Route D: derived and composite sequences

The five route-D records are:

```text
A352655 A357506 A357567 A357956 A357959
```

A product, convolution, linear combination, or transform inherits a
Gaussian theorem only when the component twists and Frobenius actions are
compatible.  These entries should remain behind their source sequences in
the queue; otherwise a derived formula can hide the actual local
obstruction.

The [Apéry defect packet](AperyRankOneDefectPacket.md) now performs this
reduction exactly.  All five records, including both nonlinear companions,
collapse to three linear congruences among the adjacent defects of A005258,
A005259, and their shifted sequences.  For \(p\ge7\) the defect vector is
one-dimensional modulo the enhanced power.  The three defining defect
relations remain open, so the records are classified `partial`, not
`proved-here`; no route-D record remains unclassified.

## 9. Priority queue after Gaussian routing

| Rank | Target | Route | Immediate deliverable | Main risk |
| ---: | --- | --- | --- | --- |
| 1 | A331562 | C | Produce a uniform rational diagonal for all rows and inspect the cubic Frobenius mechanism | Known rows \(2,3,4\) may rely on representations that do not persist |
| 2 | A380290 cubic remainder | C | Prove the single Cartier-square stratum bound isolated by the all-level reduction | The Gaussian twist has exact quadratic witnesses, so the scalar cancellation is not color-stable |
| 3 | Nearby depth-three finite sums beyond the closed pilot | T | Compute whether the scaling quotient remains deep after weighting | Twisting can remove cancellation used by the untwisted proof |
| 4 | A183068 and the repository's Landau-depth family | T | Package the already-proved general Frobenius-twist corollary family | Mostly a reusable corollary, not a new local mechanism |
| 5 | A008793 Gaussian lift | M | Seek a coefficientwise or prime-ideal refinement of the now-proved rational hyperfactorial tower | No canonical Gaussian object may exist |
| 6 | A364506, A364509, A008978, A002897, A113424 | F | Define and prove integrality of the Gaussian block analogue | The integer coefficient roots are settled, but Gaussian denominator control is a separate theorem |
| 7 | A352655, A357506, A357567, A357956, A357959 | D | Prove the three linear Apéry defect relations isolated by the packet theorem | Cubic baselines alone do not supply the enhanced three-power gain |

A228960 and A350383 have left this open queue: one coefficientwise theorem
proves both \(p^{2r}\) towers for \(p\ge5\) and supplies their split/inert
Gaussian specializations.  The broader cyclotomic-rational-function
principle recorded on A228960 remains open.

A380290 has partly left the queue as well: its full quadratic baseline and
the entire associated mixed Euler-product packet are proved for odd primes.
Only its distinguished untwisted cubic strengthening remains in the open
column, and that strengthening is now reduced exactly to the single
Cartier-square stratum estimate in the cubic Cartier note.

Two larger repository targets sit outside the literal 110-record query but
belong in the working queue: A183068 itself and the recently inspected
A333593, A365029, A375178--A375180, A364118, and A364183 families.  Their
integer status is tracked in
[Peter Bala's OEIS queue](BalaOeisSupercongruenceQueue.md).  They should be
Gaussianized only after the corresponding integer transfer mechanism is
identified.

## 10. What has and has not been achieved

Already available:

- a complete elementary Frobenius-twist deduction from any
  discard-and-rescale theorem;
- the A183068 split/inert specialization and ramified cross-twist;
- the all-prime binomial-power polynomial theorem for every \(m\ge3\),
  including its prime-specific multiplicity bonus and small-prime losses;
- the all-prime coefficientwise quadratic towers for A005259 and A333592;
- the odd-prime coefficientwise quadratic tower for arbitrary multicolored
  integral Euler products weighted by \(m^d\), including Bala's full product
  packet, the A380290 baseline, and its split/inert Gaussian twist;
- a complete classification of the reproducible 110-record census by
  Gaussian proof route; and
- a 195-case exact pilot that rejects one overly strong extrapolation.

Not established by this map:

- that every route-T entry satisfies the two termwise hypotheses;
- a one-sided theorem at a chosen split prime \(\pi\);
- a Gaussian period model for every route-C entry;
- integrality of any newly manufactured route-F analogue; or
- novelty of any candidate after specialist review.

## 11. Maintenance rule

Every future “Gaussian generalization” added to the queue must record:

1. route \(T,C,F,M,\) or \(D\);
2. local case: split, inert, or ramified;
3. modulus as an ideal or a normalized prime-ideal valuation;
4. the exact integer theorem being transported;
5. whether the result is a formal twist, a computation, a proof candidate,
   or a reviewed theorem; and
6. the first explicit obstruction or equality witness.

This keeps the queue cumulative without turning it into a list of formulas
containing the letter \(i\).
