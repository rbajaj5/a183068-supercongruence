# The Bober sporadic factorial-ratio packet

**Status date:** August 12, 2026

**Status:** complete proof candidates for the ordinary 52-sequence cubic
tower and all 15 approved fractional-index integrality conjectures and
towers. The ordinary result follows from the balanced-factorial theorem. A
parity-transfer and binary-digit argument proves all eleven variants at
index $N/2$; a denominator-transfer lemma proves the two $N/3$ and two
$N/4$ claims. Every resulting tower is unconditional for $p\ge5$.

This note records Peter Bala's August 2026 follow-up about the 52 sporadic
integral factorial ratios cross-referenced from
[OEIS A295431](https://oeis.org/A295431).  It separates three facts that
should not be merged:

1. Bober's classification supplies the integrality of the original 52
   factorial ratios;
2. their full adjacent cubic tower follows from a classical binomial-scaling
   reduction; and
3. Bala's newer fractional-index sequences require a separate integrality
   argument, even though their odd-prime congruence transfer is already
   available.

## 1. The 52 ordinary ratios have the full cubic tower

For each record A295431--A295482, write

```math
A(N)=
\frac{\prod_i (u_iN)!}{\prod_j(v_jN)!}.
\tag{1}
```

The coefficient vectors are the 52 entries in the data file linked from
A295431.  Every entry is balanced:

```math
\sum_i u_i=\sum_jv_j,
\tag{2}
```

and Bober's classification proves that its values are integers.

The repository's
[balanced factorial-ratio theorem](BalancedFactorialRatioCubicTowers.md)
therefore applies without any further sequence-specific work.

### Corollary 1 (Bober's 52 sporadic ratios)

For every record A295431--A295482, every prime $p\geq5$, and all positive
integers $n,r$,

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.
}
\tag{3}
```

### Proof

Balance gives the exact Laurent-binomial factorization

```math
A(N)=\prod_{k=2}^{M}\binom{kN}{N}^{E_k},
\qquad
E_k=\sum_{m=k}^{M}c_m,
\tag{4}
```

where $c_m$ is the multiplicity of $m$ among the $u_i$ minus its
multiplicity among the $v_j$.  Ljunggren--Jacobsthal scaling gives

```math
\frac{\binom{knp^r}{np^r}}
     {\binom{knp^{r-1}}{np^{r-1}}}
\equiv1\pmod {p^{3r}}
\tag{5}
```

for $p\geq5$.  Products and inverses of these $p$-adic units preserve the
congruence.  Multiplication by the integral lower-level value proves (3).
$\square$

The OEIS page credits Zudilin's Section 5 with the prime-step congruence
$A(np)\equiv A(n)\pmod {p^3}$.  Corollary 1 is the all-level formulation.
It is recorded here as a deduction from classical scaling, not as a claim of
a new mechanism or a completed literature-priority audit.

## 2. Bala's fractional-index packet

For fixed $q\geq2$, define the gamma-interpolated subsequence

```math
B_q(N)=A(N/q)
=
\frac{\prod_i\Gamma(u_iN/q+1)}
     {\prod_j\Gamma(v_jN/q+1)}.
\tag{6}
```

The relevant admission test is finite.  Besides (2), require, for every
nonzero residue $a\pmod q$,

```math
\#\{i:u_i\equiv a\pmod q\}
=
\#\{j:v_j\equiv a\pmod q\}.
\tag{7}
```

Condition (7) is exactly the residue-balance hypothesis in the repository's
[rational gamma-ratio theorem](RationalGammaRatioCubicTowers.md).  It makes
all nonintegral gamma factors pair into rational binomials.

### Corollary 2 (conditional fractional-index tower)

If (7) holds, then for every prime $p\geq5$ with $p\nmid q$,

```math
\frac{B_q(np^r)}{B_q(np^{r-1})}
\equiv1\pmod {p^{3r}}.
\tag{8}
```

If the lower-level value is $p$-integral - in particular, if Bala's proposed
global integrality statement is true - then

```math
\boxed{
B_q(np^r)\equiv B_q(np^{r-1})\pmod {p^{3r}}.
}
\tag{9}
```

Thus the supercongruence part of every currently visible proposal below is
settled conditionally.  The two integrality theorems below now remove that
condition in every approved case.

| OEIS record | Fractional indices in the approved OEIS comment | Residue-balance test | Current status |
| --- | --- | --- | --- |
| [A295456](https://oeis.org/A295456) | $N/2$, $N/3$ | Passes for $q=2,3$ | Both variants integral; (9) proved for both |
| [A295458](https://oeis.org/A295458) | $N/2$, $N/3$ | Passes for $q=2,3$ | Both variants integral; (9) proved for both |
| [A295460](https://oeis.org/A295460) | $N/2$, $N/4$ | Passes for $q=2,4$ | Both variants integral; (9) proved for both |
| [A295464](https://oeis.org/A295464) | No approved fractional-index comment visible on August 12 | Not applicable | No fractional claim entered |
| [A295465](https://oeis.org/A295465) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295468](https://oeis.org/A295468) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295470](https://oeis.org/A295470) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295471](https://oeis.org/A295471) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295475](https://oeis.org/A295475) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295477](https://oeis.org/A295477) | $N/2$, $N/4$ | Passes for $q=2,4$ | Both variants integral; (9) proved for both |
| [A295479](https://oeis.org/A295479) | $N/2$ | Passes for $q=2$ | Integral and tower proved |
| [A295481](https://oeis.org/A295481) | $N/2$ | Passes for $q=2$ | Integral and tower proved |

There are 15 approved fractional-index sequences in this table. The
[Bober half-index theorem](BoberHalfIndexIntegralityTowers.md) proves all
eleven $N/2$ integrality claims and their cubic towers. The
[denominator-transfer theorem](BoberRemainingFractionalIntegralityTowers.md)
proves the remaining two $N/3$ and two $N/4$ claims. Hence all 15 approved
fractional variants are now closed.

## 3. A compact CSP admission filter

The two admission conditions can be treated as a finite affine constraint
system on the multiplicity vector $(c_m)$:

```math
\sum_m mc_m=0,
\qquad
\sum_{m\equiv a\pmod q}c_m=0
\quad(1\leq a<q).
\tag{10}
```

This is the useful connection to
[*Notes on CSPs and Polymorphisms*](https://notzeb.com/csp-notes.pdf): when
searching a large factorial-ratio database, (10) is an affine CSP that
filters candidates before any expensive integrality or congruence work.
The CSP language improves search organization; it does not prove (3), (8),
or integrality.

For this packet the filter gives a sharp division of labor:

- **ordinary 52 ratios:** balance plus known integrality, hence (3);
- **all eleven $N/2$ variants:** parity transfer to the original Landau
  function plus an exact binary digit-sum certificate, hence global
  integrality and (9);
- **the four $N/3$ and $N/4$ variants:** coprime-modulus Landau transfer and
  an exact denominator-prime valuation table, hence global integrality and
  (9);
- **A295464:** no approved public fractional-index formula is presently
  assigned a theorem status.

## 4. Small-prime and priority boundaries

- Nothing in this note asserts the same exponent for $p=2$ or $p=3$.
  These primes fall outside the classical unit-block proof and must be
  handled separately under the repository's [dyadic policy](../DYADIC_POLICY.md).
- For $B_q$, primes dividing $q$ are also excluded.
- Exact checks are transcription and counterexample screens, not proofs of
  global integrality.
- A targeted source pass located the Bober classification and Zudilin's
  prime-step theorem, but not a published statement of Corollary 1 in this
  exact 52-record form.  That is not a priority certificate.

## 5. Verification

Run

```text
python verification/related/verify_bober_sporadic_packet.py
```

The checker stores the 52 coefficient pairs from A295431's linked data,
verifies balance and Laurent-binomial factorization, and tests exact
adjacent cubic congruences.  It separately checks the residue constraints,
the first 31 exact values, and two adjacent levels for all 15 approved
fractional-index variants.

The separate command

```text
python verification/related/verify_a364176_affine_landau.py
```

checks the completed A364176 floor reduction, integrality, and tower.

The uniform half-index command

```text
python verification/related/verify_bober_half_index.py
```

reconstructs the eleven odd-index factorial ratios, verifies the Landau
transfer and binary digit identities, checks exact integrality, and tests the
resulting towers.

The remaining-fractional command

```text
python verification/related/verify_bober_remaining_fractional.py
```

tests the general coprime-modulus transfer and the exact $2$- and $3$-adic
valuation formulas for the four denominator-three and denominator-four
variants.

The [QRCert blueprint](https://github.com/rbajaj5/qrcert) suggests a clean
future certification split: encode each coefficient pair canonically, let a
small checked decoder verify (2) and compute the exponents in (4), and prove
that an extracted Rust checker refines the Lean specification through the
Charon--Aeneas pipeline.  That would certify the data path.  It is not used
as evidence for Corollary 1 or Corollary 2 in the present note.

## 6. Sources

- [OEIS A295431](https://oeis.org/A295431), including the 52-entry data file,
  Bala's all-level conjecture, and the reference to Zudilin's prime-step
  result.
- J. W. Bober,
  [*Factorial ratios, hypergeometric series, and a family of step functions*](https://arxiv.org/abs/0709.1977).
- W. Zudilin,
  [*Congruences for q-binomial coefficients*](https://arxiv.org/abs/1901.07843),
  especially Section 5.
- Peter Bala's August 2026 email identifying the 12 recent OEIS records;
  exact public formulas were taken from the approved OEIS pages rather than
  inferred from the email.
