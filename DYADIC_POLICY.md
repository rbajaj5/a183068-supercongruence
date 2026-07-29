# Dyadic cases: repository-wide audit policy

The prime \(2\) is not a routine substitution into an odd-prime proof.
Throughout this repository, an all-prime theorem is complete only after its
dyadic case has been proved with the correct valuation normalization, signs,
boundary levels, and ramification.

This is a proof policy, not a claim that every \(p=2\) argument has the same
mechanism.

## Why \(2\) is different

Several independent losses can occur at the binary prime:

1. **Scaling exponents degrade.** Jacobsthal--Kazandzidis-type quotients
   commonly lose two powers at \(p=2\), rather than one at \(p=3\) or none
   for \(p\ge5\).
2. **The unit may be a sign.** A binary scaling quotient can be congruent to
   \(\pm1\), so a proof requiring \(+1\) must exclude the negative branch or
   show that the modulus identifies the two signs.
3. **The first level can be exceptional.** A bound valid for \(r\ge2\) may
   leave \(r=1\) one power short. Parity or cancellation must then supply the
   missing power.
4. **Ramification changes the unit of measurement.** In
   \(\mathbb Z[i]\),
   \[
   2=-i(1+i)^2.
   \]
   Thus \(v_{1+i}(2)=2\), and a statement modulo \(2^m\) is not numerically
   the same as a statement modulo \((1+i)^m\).
5. **Linear data can miss a quadratic obstruction.** At \(2\), signs,
   repeated parts, Arf-type information, and quadratic Gauss sums can carry
   information invisible in the corresponding odd-prime linearization.
6. **Compatible finite solutions need not be finite witnesses.** An inverse
   system can converge to a genuine element of \(\mathbb Z_2\) without coming
   from one ordinary integer.

## Required checklist

Every result that includes \(p=2\), \(2\)-power levels, or the prime
\(1+i\) must answer the following questions explicitly.

### Normalization

- Is the valuation \(v_2(2)=1\), or is a ramified uniformizer used?
- If \(\varpi=1+i\), has the conversion \(v_\varpi(2)=2\) been applied?
- Are congruence exponents stated in the same normalization on both sides?

### Transfer

- What does the scaling or Frobenius quotient equal modulo the required
  power: \(1\), \(-1\), or only a unit?
- If a published theorem is stated for odd primes, what replaces it at
  \(2\)?
- Are zero components and minimum-valuation hypotheses handled before a
  product of quotients is formed?

### Boundary and cancellation

- Are \(r=1\) and any smallest admissible parameters checked separately?
- Is the claimed gain termwise, or does it require cancellation in the sum
  or product?
- If cancellation is required, is it proved rather than inferred from
  numerical data?

### Evidence and status

- Does the checker include \(p=2\), equality cases, and the first two lifting
  levels?
- Has a tempting odd-prime extrapolation been tested for a binary
  counterexample?
- Is the result labelled **dyadic complete**, **dyadic reduction**, or
  **dyadic experimental**?

An all-prime claim with an unresolved binary step cannot be labelled a
complete proof in the result index or assigned full proof maturity in the
rankings.

## Four case studies in this repository

### A183068: dyadic complete in the draft

The core proof has three binary ingredients.

First, if \(t=v_2(N)\) and \(s=v_2(k)<t\), carry counting is slightly
stronger at \(p=2\):

\[
v_2(F(N,k))\ge 2(t-s)+1.
\]

Second, the scaling quotient loses two powers and has a possible sign. In
the equal-index specialization used here, the negative sign is impossible
for \(s\ge1\); for \(s=0\), it agrees with \(+1\) modulo \(2\).

Third, the remaining \(p=2,r=1\) deficit is repaired by a repeated
multinomial component:

\[
\binom{2b}{b}\equiv0\pmod2
\qquad(b\ge1).
\]

These are the two load-bearing review points identified in
[the proof](PROOF.md): the binary sign qualification and the
central-binomial parity repair.

### Gaussian Lucas scaling: ramified dyadic candidate

For Gaussian integers the binary prime is ramified, so the relevant
uniformizer is \(\varpi=1+i\). The repository's current proof candidate gives

\[
v_\varpi(R_{2,r}-1)
=6r-3+
v_\varpi\!\left(CD(A-C+i(B-D))\right)
\]

for \(r\ge2\), together with the corresponding difference exponent
\(6r-4\). This is a separate ramified argument, not a specialization of the
inert-prime proof.

### The binary \(s_{18}\) target: dyadic reduction

The [\(s_{18}\) note](related-results/S18TwoAdicReduction.md) reduces a
published binary conjecture to one sharpened product-scaling lemma. A
factor-by-factor signed Jacobsthal estimate is explicitly false; any proof
must account for the interaction of the factors. This remains a reduction,
not a theorem.

### Roe--Turturean: architectural comparison

Roe and Turturean's
[*A Presentation of the Absolute Galois Group of
\(\mathbb Q_2\)*](https://roed314.github.io/gq2/)
is a genuinely dyadic local-field result. Its pro-\(2\) structure,
orientation lifting, quadratic Gauss-sum layer, and compatible finite
quotients illustrate why the prime \(2\) needs additional data.

It does not prove the A183068 binary scaling lemma. The connection is
architectural: in both settings an odd-prime template is insufficient, and
the binary repair must be made explicit.

## Editorial consequences

This policy applies to:

- the central A183068 proof;
- every all-prime Landau-depth or factorial-ratio theorem;
- Gaussian split, inert, and ramified comparisons;
- \(q\)-congruences specialized at even cyclotomic order;
- Dwork and constant-term towers when \(p=2\) is included; and
- any future Bala/OEIS target advertised for every prime.

The literature census must record whether a cited theorem includes \(2\).
The result index must state the dyadic status of an all-prime claim. The
portfolio ranking must count an unresolved binary case as remaining proof
cost, not as a cosmetic edge case.
