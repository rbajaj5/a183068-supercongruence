# Peter Bala's OEIS supercongruence queue

**Status:** the A365029 boundary theorem and full \(r=1,2\) adjacent
supercongruences are proved; the A375178 prime-level family is proved; the
complete A333593 prime-power tower is reduced to Coster's generalized Apéry
theorem. Two higher-level towers remain exact computational targets.
Literature priority is preliminary, and the new arguments have not been
independently reviewed.

The broader
[supercongruence literature census](SupercongruenceLiteratureCensus.md)
starts from 110 OEIS records returned by the reproducible query
`"Peter Bala" supercongruence`, separates already-published instances from
open refinements, and consolidates the next targets by proof mechanism.

## 1. Source inventory

Peter Bala's OEIS postscript points to a substantial, coherent collection
rather than one isolated conjecture. This first pass separates five
representative targets by mechanism.

| OEIS entry | Conjectural statement | Present result |
| --- | --- | --- |
| [A365029] | \(a(p-1)\equiv1\pmod{p^3}\), plus an all-\(n,r\) \(p^{3r}\) tower | The first congruence is proved below in the stronger two-parameter form \(p^{A+B}\); the full \(r=1,2\) adjacent congruences are also proved; only \(r\ge3\) remains |
| [A375178] | An odd-power family satisfies \(b_m(p)\equiv1\pmod{p^{2m+3}}\), plus a stronger tower for \(r\ge2\) | The entire prime-level family is proved below; the tower remains a target |
| [A375179], [A375180] | Two parallel signed odd-power families have the same proposed exponents | Retained as one consolidated extension of the A375178 program; neither follows formally from Theorem 2 below |
| [A333593] | \(a(np^r)\equiv a(np^{r-1})\pmod{p^{3r}}\) | Proved below by an exact decomposition into a Coster generalized Apéry tower and a Jacobsthal--Kazandzidis binomial tower |
| [A364118] | An Apéry linear combination gains two or three powers beyond the underlying tower | Modular/Apéry target; not yet reduced to the termwise framework |
| [A364183] | A parity-sensitive height-one factorial ratio is integral and satisfies a \(p^{3r}\) tower | Integrality itself is still conjectural on the OEIS entry; treat before the tower |

The live OEIS records are the source of the statements and attribution.

## 2. A stronger boundary theorem for A365029

For positive integers \(A,B\), define

```math
C_{A,B}(n)=
\sum_{k=0}^{n}
\binom{n+k-1}{k}^{A}
\binom{2k-1}{n}^{B},
\qquad n\ge0,
\tag{1}
```

using the integral generalized binomial convention. The OEIS sequence
A365029 is \(C_{2,1}\).

### Theorem 1

For every odd prime \(p\) and all positive integers \(A,B\),

```math
\boxed{
C_{A,B}(p-1)\equiv1\pmod {p^{A+B}}.
}
\tag{2}
```

In particular,

```math
C_{2,1}(p-1)\equiv C_{2,1}(0)\pmod {p^3},
```

proving the first A365029 conjecture, and slightly strengthening its stated
range from \(p\ge5\) to every odd prime.

#### Proof

The \(k=0\) term in (1) is \(1\). If
\(1\le k\le(p-1)/2\), then

```math
0\le2k-1<p-1,
```

so \(\binom{2k-1}{p-1}=0\).

It remains to consider \((p+1)/2\le k\le p-1\). In this range,

```math
p\le p+k-2<2p,
\qquad
p\le2k-1<2p,
```

while every denominator in

```math
\binom{p+k-2}{k},
\qquad
\binom{2k-1}{p-1}
```

has factorial arguments below \(p\). Each binomial coefficient therefore
has \(p\)-adic valuation exactly \(1\). Its contribution to (1) is divisible
by \(p^{A+B}\). Adding the terms proves (2). \(\square\)

This proof is termwise and sharp in the tested range. The separate
adjacent-scale conjecture is now proved at \(r=1,2\) in the
[A365029 first-two-level note](A365029FirstTwoLevels.md); its higher levels
remain open.

## 3. The full prime-level odd-power theorem for A375178

For \(m\ge1\), put \(q=2m+1\) and

```math
b_m(n)=
\sum_{k=0}^{n-1}
\binom{n+k-1}{k}^{q}.
\tag{3}
```

The sequence A375178 is \(b_1\).

### Theorem 2

If \(p\) is prime and \(p\ge2m+5\), then

```math
\boxed{
b_m(p)\equiv1\pmod {p^{2m+3}}.
}
\tag{4}
```

This proves the full prime-level family conjectured on A375178.

#### Proof

Work in the localization \(\mathbb Z_{(p)}\), so every
\(1,\ldots,p-1\) is invertible. For \(1\le k\le p-1\),

```math
\binom{p+k-1}{k}
=
\frac{p}{k}
\prod_{j=1}^{k-1}\left(1+\frac pj\right).
\tag{5}
```

Let

```math
H_s=\sum_{k=1}^{p-1}\frac1{k^s},
\qquad
H(a,b)=\sum_{1\le j<k\le p-1}\frac1{j^a k^b}.
```

Raising (5) to the odd power \(q\), dividing by \(p^q\), and expanding
modulo \(p^2\) gives

```math
\frac{b_m(p)-1}{p^q}
\equiv
H_q+qp\,H(1,q)
\pmod {p^2}.
\tag{6}
```

The assumption \(p\ge q+4\) gives

```math
H_{q+1}\equiv0\pmod p
```

by the standard finite-field power sum. Replacing \(k\) by \(p-k\) yields

```math
H_q
\equiv
-H_q-qpH_{q+1}
\pmod {p^2},
```

and therefore

```math
H_q\equiv0\pmod {p^2}.
\tag{7}
```

The exact stuffle identity is

```math
H_1H_q=H(1,q)+H(q,1)+H_{q+1}.
\tag{8}
```

Modulo \(p\), reversal of the two indices gives

```math
H(1,q)\equiv(-1)^{q+1}H(q,1)=H(q,1),
```

because \(q\) is odd. All single harmonic sums in (8) vanish modulo \(p\),
so

```math
2H(1,q)\equiv0\pmod p.
```

Thus \(H(1,q)\equiv0\pmod p\). Equation (6), together with (7), is
divisible by \(p^2\). Since \(q=2m+1\), this proves divisibility by
\(p^{q+2}=p^{2m+3}\). \(\square\)

### The published cubic baseline

There is already a complete adjacent-scale baseline for every exponent, not
only the odd exponents in Bala's family. For an integer \(q\ge2\), set

```math
B_q(N)=
\sum_{k=0}^{N-1}\binom{N+k-1}{k}^{q}.
```

Then, for \(p\ge5\) and positive integers \(n,r\),

```math
B_q(np^r)\equiv B_q(np^{r-1})\pmod {p^{3r}}.
\tag{9}
```

Indeed,

```math
B_q(N)=w_{0,q,1}(N-1),
```

so (9) is exactly the \(B\ge2\) branch of [Coster's] generalized Apéry
theorem. Thus the open A375178-family target is not the existence of a cubic
tower. It is the uniform gain of a further \(q=2m+1\) powers at \(n=1\) and
\(r\ge2\):

```math
b_m(p^r)\equiv b_m(p^{r-1})
\pmod {p^{3r+2m+1}}
\qquad(r\ge2)
\tag{10}
```

The exponent in Theorem 2 is attained in the exact tested range. Reaching
(10) still requires a refinement beyond Coster's cubic theorem: the clean
\(k=1,\ldots,p-1\) harmonic argument above does not simply iterate.

## 4. The A333593 tower is a Coster corollary

Define

```math
A(N)=
\sum_{k=0}^{N}
(-1)^{N+k}\binom{N+k-1}{k}^{2}
```

and the generalized Apéry sum

```math
W(t)=
\sum_{k=0}^{t}
(-1)^k\binom{t+k}{k}^{2}.
\tag{11}
```

The OEIS sequence A333593 is \(A(N)\).

### Theorem 3

For every prime \(p\ge5\) and positive integers \(n,r\),

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.
}
\tag{12}
```

#### Proof

Separating the final summand in \(A(N)\) gives the exact identity

```math
A(N)=
(-1)^N W(N-1)+\binom{2N-1}{N}^{2}.
\tag{13}
```

[Coster's] generalized Apéry theorem applies to
\(W=w_{0,2,-1}\): for \(p\ge5\),

```math
W(np^r-1)\equiv W(np^{r-1}-1)\pmod {p^{3r}}.
\tag{14}
```

The standard Jacobsthal--Kazandzidis binomial congruence gives

```math
\binom{2np^r}{np^r}
\equiv
\binom{2np^{r-1}}{np^{r-1}}
\pmod {p^{3r}}.
\tag{15}
```

Because \(2\) is a \(p\)-adic unit,
\(\binom{2N-1}{N}=\frac12\binom{2N}{N}\), so (14) remains valid
after dividing by \(2\) and squaring. Finally \(p\) is odd, hence

```math
(-1)^{np^r}=(-1)^{np^{r-1}}=(-1)^n.
```

Substituting (14)--(15) into (13) proves (12). \(\square\)

This closes the full conjecture recorded on A333593, but it should be
described as a new reduction to a published theorem rather than as a new
independent supercongruence mechanism. [Coster] states the required result as
Theorem 4 of his report *Supercongruences* and refers to pages 49--55 of his
1988 thesis for its technical proof.

## 5. Exact status of the remaining first queue

The dependency-free checker records:

- 390 instances of Theorem 1, for \(1\le A\le6\), \(1\le B\le5\), and
  odd primes through \(43\);
- 56 instances of Theorem 2, for \(1\le m\le6\) and primes through \(43\);
- 343 instances of Coster's cubic baseline (9), for \(2\le q\le8\);
- 584 checks of Theorem 3 and its reduction: 200 exact decompositions,
  128 final tower congruences, and 256 component congruences;
- 128 instances of the open A365029 tower; and
- 17 higher-level instances of the open A375178 family.

Every asserted bound passes, and each displayed open-tower exponent is
attained somewhere in the tested range. The A365029 and A375178 tower
computations are evidence only.

The separate A365029 checker adds 67,310 exact checks. It verifies the
complete \(r=1,2\) theorems, shifted transfer, the one- and two-digit local
expansions, both half-block cancellations, and 177 remaining higher-level
complete-block instances. Those last 177 checks support, but do not prove,
the \(r\ge3\) induction.

Run:

```text
python verification/related/verify_bala_oeis_supercongruences.py
python verification/related/verify_a365029_first_two_levels.py
```

## 6. Next proof order

The economical order is:

1. **A365029 tower above \(r=2\).** The boundary and first two adjacent
   congruences are proved. The remaining task is to induct the explicit
   two-digit reciprocal-square calculation through
   \(\mathbb Z/p^r\mathbb Z\).
2. **A375178 tower.** The prime-level harmonic cancellation is now proved,
   but the additional \(3r\) block gain must be made uniform.
3. **A364183 integrality.** Resolve the even/odd factorial-ratio branches
   before discussing supercongruences.
4. **A364118.** Use its Apéry/modular structure rather than forcing a
   termwise proof.

This ordering is a research-budget decision, not a ranking of Peter's
mathematical contributions.

## Literature boundary

Targeted exact-formula and A-number searches located the conjectures on OEIS
but no proof of Theorems 1--2 in the forms above. That is not a priority
certificate. Both proofs use standard binomial-valuation and finite
multiple-harmonic-sum identities, so overlap with the literature remains
possible.

[Kallat's] 2026 proof of Bala's A028342 congruence uses cyclic actions on
colored permutations: full orbits disappear modulo the modulus and fixed
points determine the prime-power residues. It is a valuable nearby precedent,
but it does not directly supply an action on the truncated factorial sums in
this queue. The operative input for Theorem 3 is instead Coster's generalized
Apéry theorem.

[A333593]: https://oeis.org/A333593
[A365029]: https://oeis.org/A365029
[A375178]: https://oeis.org/A375178
[A375179]: https://oeis.org/A375179
[A375180]: https://oeis.org/A375180
[A364118]: https://oeis.org/A364118
[A364183]: https://oeis.org/A364183
[Coster]: https://ir.cwi.nl/pub/5804/5804D.pdf
[Kallat]: https://arxiv.org/abs/2607.18313
