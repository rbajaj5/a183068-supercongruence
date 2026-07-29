# Peter Bala's OEIS supercongruence queue

**Status:** two prime-level conjecture families proved below; three deeper
prime-power towers retained as exact computational targets. Literature
priority is preliminary, and the proofs have not been independently reviewed.

## 1. Source inventory

Peter Bala's OEIS postscript points to a substantial, coherent collection
rather than one isolated conjecture. This first pass separates five
representative targets by mechanism.

| OEIS entry | Conjectural statement | Present result |
| --- | --- | --- |
| [A365029] | \(a(p-1)\equiv1\pmod{p^3}\), plus an all-\(n,r\) \(p^{3r}\) tower | The first congruence is proved below in the stronger two-parameter form \(p^{A+B}\); the tower remains a target |
| [A375178] | An odd-power family satisfies \(b_m(p)\equiv1\pmod{p^{2m+3}}\), plus a stronger tower for \(r\ge2\) | The entire prime-level family is proved below; the tower remains a target |
| [A333593] | \(a(np^r)\equiv a(np^{r-1})\pmod{p^{3r}}\) | Peter proved the \(n=r=1\) case; 128 further exact cases are recorded here |
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

This proof is termwise and sharp in the tested range. It does not prove the
separate adjacent-scale \(p^{3r}\) conjecture for \(C_{2,1}(np^r)\).

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

The exponent is attained in the exact tested range. The higher-level OEIS
conjecture

```math
b_m(p^r)\equiv b_m(p^{r-1})
\pmod {p^{3r+2m+1}}
\qquad(r\ge2)
\tag{9}
```

requires a new block decomposition: the clean \(k=1,\ldots,p-1\) harmonic
argument above does not simply iterate.

## 4. Exact status of the remaining first queue

The dependency-free checker records:

- 390 instances of Theorem 1, for \(1\le A\le6\), \(1\le B\le5\), and
  odd primes through \(43\);
- 56 instances of Theorem 2, for \(1\le m\le6\) and primes through \(43\);
- 128 instances of the open A333593 tower;
- 128 instances of the open A365029 tower; and
- 17 higher-level instances of the open A375178 family.

Every asserted bound passes, and each displayed exponent is attained
somewhere in the tested range. The tower computations are evidence only.

Run:

```text
python verification/related/verify_bala_oeis_supercongruences.py
```

## 5. Next proof order

The economical order is:

1. **A365029 tower.** Its boundary congruence is now termwise and the tower
   has the same observed cubic exponent.
2. **A333593 tower.** Peter's existing \(r=1,n=1\) proof supplies the base,
   and the signed pairing is explicit.
3. **A375178 tower.** The prime-level harmonic cancellation is now proved,
   but the additional \(3r\) block gain must be made uniform.
4. **A364183 integrality.** Resolve the even/odd factorial-ratio branches
   before discussing supercongruences.
5. **A364118.** Use its Apéry/modular structure rather than forcing a
   termwise proof.

This ordering is a research-budget decision, not a ranking of Peter's
mathematical contributions.

## Literature boundary

Targeted exact-formula and A-number searches located the conjectures on OEIS
but no proof of Theorems 1--2 in the forms above. That is not a priority
certificate. Both proofs use standard binomial-valuation and finite
multiple-harmonic-sum identities, so overlap with the literature remains
possible.

[A333593]: https://oeis.org/A333593
[A365029]: https://oeis.org/A365029
[A375178]: https://oeis.org/A375178
[A364118]: https://oeis.org/A364118
[A364183]: https://oeis.org/A364183
