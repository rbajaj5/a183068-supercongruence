# Supercongruence literature and the Bala--OEIS census

**Census date:** July 28, 2026
**Status:** literature map and research triage, not a priority certificate

This note maps Peter Bala's OEIS supercongruence corpus to the principal
published proof mechanisms.  Its purpose is economical: before treating an
OEIS comment as a new theorem target, determine whether it is already a
special case of Coster, Straub, a Dwork congruence, or a standard
Jacobsthal--Kazandzidis scaling theorem.

## 1. Reproducible scope

The OEIS query

> ["Peter Bala" supercongruence](https://oeis.org/search?q=%22Peter+Bala%22+supercongruence)

returned **110 sequence records** on the census date.  This is not a count of
110 open problems.  A record can appear because:

- Bala stated a conjecture there;
- Bala added a formula or comment to a sequence with a known
  supercongruence;
- the entry cites one of Bala's notes;
- a formerly conjectural statement was later marked as proved; or
- the same parameterized conjecture was posted on several related entries.

The working census therefore uses a second pass:

1. read the live OEIS statement and its modification history;
2. search the exact A-number and exact summand or generating-function
   fingerprint;
3. compare the statement with the hypotheses of the published general
   theorems below; and
4. label the result as **published**, **published-theorem reduction**,
   **proved in this repository**, **open refinement**, or **unclassified**.

Exact-formula searches reduce false novelty claims, but they do not establish
priority.  A negative search result is recorded only as "no proof located."

The second pass also applies the repository's
[dyadic audit policy](../DYADIC_POLICY.md). A theorem cited for \(p\ge5\), or
for odd primes, does not close an all-prime OEIS statement. The \(p=2\)
normalization, sign, first lifting level, and any ramification must be matched
separately.

A complementary
[Gaussian generalization map](BalaGaussianGeneralizationMap.md) classifies
all 110 records by the proof operation a Gaussian extension would require.
It should be consulted before adding an \(i^k\)-twist: only 40 records have a
direct finite-sum route, and even there the
[exact pilot](BalaGaussianTwistPilot.md) shows that the untwisted exponent can
drop after twisting.

## 2. The theorem-routing table

| Mechanism | Published starting points | Bala/OEIS families it should be checked against | Boundary |
| --- | --- | --- | --- |
| Binomial and multinomial scaling | Wolstenholme; Jacobsthal--Kazandzidis; Meštrović's survey | A333592--A333593, A375178--A375180, A364303, A364506, A364509 | Usually gives a cubic adjacent-scale baseline. It does not automatically give Bala's extra \(p^2\), \(p^3\), or exponent-dependent gain. |
| Generalized Apéry sums | Beukers; Coster, Theorem 4; Osburn--Sahu; Osburn--Sahu--Straub | A112028, A176335, A219562, A333592--A333593, A364114--A364119, A375178 | Shifted indices and linear combinations must match the theorem exactly. A \(p^{3r}\) baseline does not prove a \(p^{3r+3}\) refinement. |
| Multivariate rational functions | Straub's multivariate Apéry theorem | Apéry, Franel, Yang--Zudilin, and rational-diagonal entries including several A362xxx and A363xxx records | A rational representation alone does not imply Straub's exponent; the coefficient and partition hypotheses matter. |
| Factorial-ratio valuations and Landau functions | Bober; Soundararajan; Delaygue | The A364173--A364185 factorial-ratio packet and related Vasyunin/Bober entries | Integrality is logically prior to a congruence in \(\mathbb Z\). A height-one ratio at half-integral arguments is not automatically covered by the integral classification. |
| Constant terms and Dwork congruences | Samol--van Straten; Mellit--Vlasenko; Vlasenko's higher Hasse--Witt matrices | A228960, A350383, A333090--A333097, A380290 and other coefficient-of-\(F(x)^n\) families | These theorems provide powerful Frobenius congruences, but the Newton-polytope or Hasse--Witt hypotheses and the achieved exponent must be checked. |
| Finite harmonic sums | Wolstenholme-type harmonic congruences; Pan--Sun | Prime-level odd-power families such as A375178--A375180 and central-trinomial refinements | Excellent for \(r=1\); block iteration to every \(r\) is a separate theorem. |
| \(p\)-adic gamma and hypergeometric transformations | Long--Ramakrishna and subsequent truncated-hypergeometric work | Prime-level and truncated hypergeometric conjectures, including enhanced Apéry combinations | A gamma quotient is a representation, not the needed valuation estimate by itself. |
| Creative \(q\)-microscoping | Guo--Zudilin and later Dwork-type \(q\)-congruences | Proposed cyclotomic lifts of binomial and hypergeometric towers | A suitable \(q\)-analogue must be proved. The most obvious multilevel \(q\)-lift can be false even when the integer congruence is true. |
| Orbit counting and CRT | Kallat's proof of A028342 | Exponential generating functions with a direct labeled-combinatorial model | This is a distinct mechanism from factorial-ratio scaling and should not be forced onto truncated binomial sums without an actual action. |

One superficially close item must not be used as infrastructure:
Hartosh Singh Bal's 2025 preprint on Witt--Hadamard calculus, norm descent,
and prime-ideal ladders was
[withdrawn](https://arxiv.org/abs/2509.25038). The current arXiv record
states that its number-field Dold-congruence and norm-descent formulations
and proofs contain major errors. Its vocabulary is relevant to the
Euler-product program, but none of its withdrawn number-field claims are
used in this repository.

### Dyadic routing overlay

Every row in the table has a binary boundary:

- scaling theorems may lose powers or return a sign rather than \(1\);
- harmonic and gamma expansions can have exceptional denominators at \(2\);
- a Dwork theorem stated for odd \(p\) does not silently include \(2\);
- an even-order \(q\)-specialization can fail although its odd-order analogue
  holds; and
- over \(\mathbb Z[i]\), the prime above \(2\) is the ramified uniformizer
  \(1+i\), not an inert or split odd prime.

The census therefore records “all odd primes proved” and “all primes proved”
as different statuses.

## 3. Statements already removed from the open queue

The following examples show why the routing pass is necessary.

| Entry or family | Current mathematical status |
| --- | --- |
| [A028342](https://oeis.org/A028342) | Bala's congruence conjecture is proved by Kallat using colored permutations, orbit counting, prime-power residues, and CRT.  The paper also reports a Lean 4 formalization. |
| [A234839](https://oeis.org/A234839) | The OEIS record identifies the stated \(p^{3r}\) congruence with Osburn--Sahu--Straub, Example 3.3. |
| [A176335](https://oeis.org/A176335) | The live record marks the tower as a consequence of Coster's Theorem 4. |
| [A364509](https://oeis.org/A364509) | The live record marks the row-family congruence as following from the binomial congruence recorded by Meštrović.  The parameter matching should still be written explicitly before citing it as a proof. |
| [A082758](https://oeis.org/A082758) | The live record now derives the conjectured bound from Pan--Sun's central-trinomial theorem. |
| [A333593](https://oeis.org/A333593) | The repository gives an exact decomposition into a Coster generalized-Apéry tower and a Jacobsthal--Kazandzidis binomial tower.  This is a published-theorem reduction, not a new mechanism. |
| [A375178](https://oeis.org/A375178), cubic baseline | Coster supplies the \(p^{3r}\) tower for every exponent \(q\ge2\).  Bala's stronger \(p^{3r+q}\) odd-power tower remains open. |
| [A365029](https://oeis.org/A365029), boundary and first two levels | The repository proves the stronger prime-boundary result \(C_{A,B}(p-1)\equiv1\pmod {p^{A+B}}\) and the \(r=1,2\) adjacent congruences for \(C_{2,1}\). The tower from \(r=3\) onward remains open. |
| [A183068](https://oeis.org/A183068) | This repository contains a proposed all-prime proof and exact checks.  It remains a proof candidate pending conventional specialist review. |
| [A228960](https://oeis.org/A228960) and [A350383](https://oeis.org/A350383) | The repository's cyclotomic coefficient-pair theorem proves both displayed \(p^{2r}\) towers for \(p\ge5\), coefficientwise.  The broader cyclotomic-rational-function principle on A228960 remains open. |
| [A380290](https://oeis.org/A380290) and Bala's associated Euler-product packet | The colored Euler-product theorem proves the complete coefficientwise \(p^{2r}\) baseline for every odd prime, arbitrary integral mixed powers, and every degree weight \(m^d\), \(d\ge1\). The dyadic theorem restores \(2^{2r}\) for every \(r\ge2\), with a sharp first-level quadratic defect, and the Gaussian local table records the split, inert, and ramified specializations. The special untwisted A380290 \(p^{3r}\) conjecture remains open. |

## 4. Consolidated live targets

Several OEIS entries are best treated as one parameterized problem rather
than separate papers.

| Priority | Consolidated target | Why it survives the literature pass | Best first tool |
| ---: | --- | --- | --- |
| 1 | [A375178](https://oeis.org/A375178)--[A375180](https://oeis.org/A375180), odd-power enhanced towers | The cubic baseline is classical, while the claimed \(p^{3r+2m+1}\) gain and the three truncated-binomial geometries are not supplied by Coster | Blockwise harmonic expansion plus Jacobsthal--Kazandzidis scaling |
| 2 | [A365029](https://oeis.org/A365029), full \(A,B,n,r\) family | The boundary and \(C_{2,1}\) levels \(r=1,2\) are proved, but no published theorem located in the search yields the whole mixed-binomial tower | Induct the explicit two-digit reciprocal-square block cancellation through arbitrary \(p\)-adic depth |
| 3 | [A364118](https://oeis.org/A364118) and its companion Apéry combinations | These ask for \(p^5\) at the first level and \(p^{3r+3}\) later, beyond the ordinary Apéry tower | Linearized recurrence, modular parametrization, or a refined Coster expansion |
| 4 | [A008793](https://oeis.org/A008793), plane partitions in a cube | Its nonlinear congruence \(a(np^r)\equiv a(np^{r-1})^p\pmod {p^{4r}}\) has independent enumerative content and does not resemble a routine Coster corollary | \(p\)-adic logarithm of MacMahon's product |
| 5 | [A331562](https://oeis.org/A331562), all row sequences | Rows \(2,3,4\) are known; a uniform row theorem would replace infinitely many entries with one statement | Transfer matrix or rational-diagonal representation |
| 6 | [A364173](https://oeis.org/A364173)--[A364185](https://oeis.org/A364185) | The entries mix parity-dependent factorial ratios, and some still state integrality only conjecturally | Landau step functions first, supercongruences second |
| 7 | [A380290](https://oeis.org/A380290), cubic remainder | The quadratic tower and its coefficientwise Gaussian refinement are now proved, but the special untwisted \(d=2\) cancellation conjecturally raises \(p^{2r}\) to \(p^{3r}\) for \(p\ge7\) | Prove the extra untwisted convolution cancellation; a generic Gaussian twist has exact quadratic witnesses |
| 8 | [A333592](https://oeis.org/A333592) | The coefficientwise quadratic tower is proved in this repository, but its stronger untwisted cubic conjecture remains open | Exact comparison with Coster's \(w_{A,B,\epsilon}\) families |

The first three targets are closest to the current repository machinery.  The
plane-partition target is less likely to be quick, but a successful result
would carry more independent mathematical interest than another isolated
binomial instance.

## 5. Search findings for the current first queue

Exact A-number and formula searches through the census date found the live
OEIS statements, but no published proofs of the full conjectures for
A365029, A375178--A375180, A364118, or A364183.  This is evidence for
continued investigation, not proof of novelty.

The searches did locate three important boundary updates:

1. Kallat's July 2026 proof of A028342 demonstrates that Bala's OEIS corpus is
   now being actively mined and formally verified.
2. The A082758 record was updated in July 2026 to point to Pan--Sun, showing
   that some apparently open Bala comments are hidden corollaries of later
   literature.
3. Coster's 1989 report is broad enough that every truncated
   \(\binom{n+k}{k}^q\)-type tower must be checked against Theorem 4 before a
   novelty claim is made.

## 6. Core bibliography

### Scaling and generalized Apéry congruences

1. M. J. Coster,
   [*Supercongruences*](https://ir.cwi.nl/pub/5804/5804D.pdf),
   CWI Report AM-R8918 (1989), especially Theorem 4.
2. R. Meštrović,
   [*Wolstenholme's theorem: its generalizations and extensions in the last
   hundred and fifty years*](https://arxiv.org/abs/1111.3057).
3. R. Osburn and B. Sahu,
   [*Supercongruences for Apéry-like
   numbers*](https://arxiv.org/abs/0906.3413).
4. R. Osburn, B. Sahu, and A. Straub,
   [*Supercongruences for sporadic
   sequences*](https://arxiv.org/abs/1312.2195).
5. A. Straub,
   [*Multivariate Apéry numbers and supercongruences of rational
   functions*](https://arxiv.org/abs/1401.0854).
6. E. Delaygue,
   [*Arithmetic properties of Apéry-like
   numbers*](https://arxiv.org/abs/1310.4131).

### Factorial ratios and integrality

7. J. Bober,
   [*Factorial ratios, hypergeometric series, and a family of step
   functions*](https://arxiv.org/abs/0709.1977).
8. K. Soundararajan,
   [*Integral factorial ratios*](https://arxiv.org/abs/1901.05133).

### Dwork, constant terms, and Frobenius

9. K. Samol and D. van Straten,
   [*Dwork congruences and reflexive
   polytopes*](https://arxiv.org/abs/0911.0797).
10. A. Mellit and M. Vlasenko,
    [*Dwork's congruences for the constant terms of powers of a Laurent
    polynomial*](https://arxiv.org/abs/1306.5811).
11. M. Vlasenko,
    [*Higher Hasse--Witt matrices*](https://arxiv.org/abs/1605.06440).

### Harmonic, hypergeometric, and \(q\)-methods

12. H. Pan and Z.-W. Sun,
    [*Supercongruences for central trinomial
    coefficients*](https://arxiv.org/abs/2012.05121).
13. L. Long and R. Ramakrishna,
    [*Some supercongruences occurring in truncated hypergeometric
    series*](https://arxiv.org/abs/1403.5232).
14. V. J. W. Guo and W. Zudilin,
    [*Dwork-type supercongruences through a creative
    \(q\)-microscope*](https://arxiv.org/abs/2001.02311).
15. T. Amdeberhan and R. Tauraso,
    [*Supercongruences for the Almkvist--Zudilin
    numbers*](https://arxiv.org/abs/1506.08437).
16. Z.-H. Sun and D. Ye,
    [*Supercongruences via Beukers'
    method*](https://arxiv.org/abs/2408.09776).

### Bala-specific recent precedent

17. A. Kallat,
    [*A Proof of Bala's Congruence Conjecture for
    A028342*](https://arxiv.org/abs/2607.18313), with the associated
    [Lean formalization](https://github.com/ahaankallat/bala-a028342-lean).

## 7. Maintenance rule

Every new Bala target added to this repository should include:

- the exact live OEIS statement and date checked;
- the nearest general theorem and a written hypothesis comparison;
- a status label distinguishing a theorem from a computation;
- an exact checker when computation is material; and
- a priority note that says "no proof located," never "novel," until a
  specialist literature review has been completed.

This turns the collaboration into a cumulative program: solving one entry
should either close a whole family or sharpen the routing theorem used for
the next entry.
