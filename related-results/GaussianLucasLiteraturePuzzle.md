# How the Gaussian Lucas results fit into the literature

## Status

**Literature map and research agenda, July 26, 2026.**

This note separates direct antecedents from conceptual neighbors. It is not a
proof of priority. Searches by theorem fingerprint found no earlier statement
of the exact ramified valuation or the mixed-block disk isometry, but a
specialist literature review is still required.

## 1. The puzzle in one line

The present results fit the following chain:

```text
Gaussian lattice factorial
    -> local residue-block product
    -> logarithmic reciprocal moments
    -> exact supercongruence exponent
    -> normalized p-adic disk automorphism
    -> possible Frobenius-compatible system across scales.
```

The first four arrows are proved in the current drafts at the ramified prime.
The disk-automorphism arrow is proved in the
[canonical-product note](GaussianLucasCanonicalProducts.md). The final arrow
is the main structural question suggested by the literature.

## 2. Direct source: Kalinin's Gaussian coefficient

Kalinin's
["Wolstenholme's theorem over Gaussian integers"](https://arxiv.org/abs/2504.07978)
proves a reciprocal-sum congruence in \(\mathbb Z[i]\), defines the rectangular
coefficient

```math
Q(A,B;C,D)
=
\frac{
\prod_{0\le x<C,\,0\le y<D}
(A-x+i(B-y))
}{
\prod_{1\le x\le C,\,1\le y\le D}
(x+iy)
},
```

and conjectures the adjacent \(p\)-scale Lucas congruence modulo \(p^3\).
Kalinin explicitly notes that these coefficients need not be Gaussian
integers and that little is known about them.

This is the direct parent of the current program. Our candidate results add:

- the inert adjacent-scale exponent \(3r\), with the \(p=3\) boundary
  \(3r-1\);
- the exact ramified valuation at \(\varpi=1+i\);
- the factorization of \(Q\) as a translated lattice product; and
- an exact analytic isometry after normalizing the ramified residue block by
  its first logarithmic coefficient.

The phrase “Gaussian binomial coefficient” is ambiguous. The
[Formichella--Straub paper](https://arxiv.org/abs/1802.02684) concerns
Gaussian **\(q\)-binomial** coefficients. It proves Lucas phenomena for a
different object and is not prior art for Kalinin's two-dimensional
\(\mathbb Z[i]\)-valued factorial ratio.

## 3. Four neighboring theories

| Literature | What it already explains | What it does not yet supply here | Fit |
| --- | --- | --- | --- |
| Wolstenholme--Lucas congruences | Why scaled factorial ratios are controlled by reciprocal sums | The ramified two-dimensional block and its exact \(6r-3\) slope | Direct mechanism |
| Dwork congruences and Frobenius lifts | How scale-compatible congruences become \(p\)-adic analytic structure | A constant-term or Cartier model for Kalinin's \(Q\) | Strong research bridge |
| Generalized factorials over Dedekind domains | Prime-ideal-local factorial and binomial ideals, including denominator normalization | The rectangular ordering and exact moment estimates | Strong algebraic bridge |
| \(p\)-adic 1-Lipschitz dynamics | Why a bijective isometry induces compatible permutations modulo every prime power | Number-theoretic construction of this particular map | Consequence and crypto bridge |

### 3.1 Wolstenholme and Lucas

The classical landscape is surveyed in Meštrović's
[Wolstenholme survey](https://arxiv.org/abs/1111.3057) and
[Lucas survey](https://arxiv.org/abs/1409.3820). The familiar proof pattern
expands a scaled factorial quotient into factors close to \(1\); harmonic or
reciprocal sums then kill the first logarithmic terms.

Our ramified proof is recognizably in this lineage, but the residue set is a
mixed-parity Gaussian block and its four-coset lift raises the leading
valuation by six at each scale.

### 3.2 Dwork and constant terms

Mellit and Vlasenko prove
[Dwork congruences for constant terms of powers of Laurent polynomials](https://arxiv.org/abs/1306.5811).
Samol and van Straten connect such congruences with
[reflexive polytopes and \(p\)-adic continuation of the unit root](https://arxiv.org/abs/0911.0797).
Beukers and Vlasenko identify
[excellent Frobenius lifts as a source of supercongruences](https://arxiv.org/abs/2105.14841).
Gorodetsky uses Laurent-polynomial constant terms to prove both Lucas
congruences and prime-power supercongruences for
[sporadic Apéry-like sequences](https://arxiv.org/abs/2102.11839).

These papers do not directly imply the Gaussian rectangle theorem. They
identify the right next question:

> Do the disk automorphisms \(G_r\) arise from a single object carrying a
> Frobenius lift, rather than from separate products at each scale?

The coefficient law

```math
c_{r+1}=8c_r(1+\varpi\theta_r)
```

is the first evidence of scale coherence. A constant-term representation or a
Cartier operator for the block products would turn that analogy into a
mathematical bridge.

### 3.3 Bhargava factorials and the split-prime problem

Bhargava's
[\(\mathfrak p\)-orderings](https://eudml.org/doc/153942)
attach generalized factorials and binomial coefficients to subsets of
Dedekind rings. Lagarias and Yangjit recently extended this to
[orderings for arbitrary ideals of Dedekind domains](https://arxiv.org/abs/2502.19072),
again producing ideal-valued generalized factorials and binomial
coefficients.

This is relevant because Kalinin's \(Q\) is generally a fraction, while its
valuation is prime-ideal-local. At a split rational prime
\(p=\pi\bar\pi\), one should not expect a single rational-\(p\)
normalization to see both components cleanly. The promising algebraic task is
to reinterpret the numerator and denominator grids as local generalized
factorial ideals, then normalize separately at \(\pi\) and \(\bar\pi\).

This is a proposed route, not an established identification with a known
\(\mathfrak p\)-ordering.

### 3.4 Non-Archimedean dynamics and cryptography

The normalized ramified product

```math
G_r(Z)=\frac{F_r(Z)-1}{c_r}
```

is a bijective isometry of \(\mathbb Z_2[i]\). It therefore preserves Haar
measure and induces a permutation on every quotient
\(\mathbb Z_2[i]/(1+i)^n\). This places it in the broad theory of compatible
1-Lipschitz \(p\)-adic maps studied by Anashin; see
["Ergodic Transformations of the Space of \(p\)-adic Integers"](https://arxiv.org/abs/math/0602083)
and the earlier
[cryptographic motivation via pseudorandom generators](https://arxiv.org/abs/cs/0401030).

This is a genuine mathematical connection but not yet a cryptographic
construction. Our map satisfies \(G_r(Z)\equiv Z\pmod\varpi\) and fixes zero,
so it is not transitive modulo \(\varpi\) and should not be advertised as an
ergodic pseudorandom generator. The useful research question is whether
arithmetic translations or compositions of these maps yield transitive
compatible permutations while retaining a provable scale law.

## 4. The concrete research seams

### A. Frobenius compatibility across scales

Determine whether there is a normalization for which \(G_{r+1}\) is congruent
to \(G_r\), a Frobenius twist of \(G_r\), or a controlled composition of
\(G_r\) modulo a growing power of \(\varpi\). This is the highest-value
structural question because it could replace one theorem per scale by a
single local dynamical object.

### B. Split-prime local normalization

Construct separate \(\pi\)- and \(\bar\pi\)-adic block products for
\(p\equiv1\pmod4\). Generalized factorial ideals may tell us which
denominator factor to remove before asking for a Lucas congruence.

### C. Constant-term realization

Find a Laurent polynomial, rational function, or diagonal whose coefficients
recover the rectangular ratios or their first moments. A successful
realization would make the Dwork/Cartier literature available.

### D. Finite-quotient dynamics

Classify the cycle structure of \(G_r\) modulo \(\varpi^n\), and then of
translated maps \(Z\mapsto a+G_r(Z)\). Isometry gives bijectivity for free;
ergodicity requires the much stronger single-cycle condition at every level.

### E. Higher-degree residue blocks

Kalinin originally sought finite-field-extension analogues. The same blueprint
can be tested in rings of integers where the chosen rational prime is inert,
split, or ramified. The expected exponent should be read from the first
nonzero reciprocal moment and the ramification index.

## 5. Assessment

The “big puzzle” is not that Blaschke products, Dwork theory, generalized
factorials, and \(p\)-adic dynamics are secretly the same subject. It is that
they describe different layers of one construction:

1. **factorial geometry** supplies the finite product;
2. **local prime decomposition** chooses the residue block;
3. **logarithmic moments** determine the congruence exponent;
4. **non-Archimedean analysis** upgrades the leading term to an isometry; and
5. **Frobenius compatibility**, if it exists, would explain the whole tower at
   once.

The exact ramified theorem and disk isometry occupy layers 2--4. The best
next attempt is layer 5, with split-prime normalization as the parallel
algebraic problem.

## 6. Priority boundary

Searches included the fingerprints:

- “rectangular Gaussian” with \(1+i\);
- “Gaussian binomial” with \(6r-3\);
- Gaussian Wolstenholme congruences at the ramified prime;
- mixed Gaussian reciprocal blocks; and
- the exact leading factor
  \(CD(A-C+i(B-D))\).

No matching source was located. That supports further review; it does not
establish novelty. In particular:

- the disk-isometry argument itself is standard local analysis;
- the possible new content is its exact application to Kalinin's product and
  its coefficient slope;
- the Dwork, Bhargava, and cryptographic connections above are research
  directions unless a precise theorem is stated and proved.
