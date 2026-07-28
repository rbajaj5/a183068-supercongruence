# The Chowla--Dwork--Evans split-prime defect

## Status

The theorem quoted below is the published 1986 theorem of Sarvadaman Chowla,
Bernard Dwork, and Ronald Evans. The normalized-defect formula and exceptional
prime criterion are immediate algebraic restatements of that theorem.

This note makes no novelty claim. Its purpose is to record a particularly
close classical precedent for the split-Gaussian and first-defect branches of
this repository.

## 1. Setup

Let \(p\equiv1\pmod4\) be prime. Choose the signed integer \(a\) and an even
integer \(b\) such that

```math
p=a^2+b^2,
\qquad
a\equiv1\pmod4.
```

Thus \(a+bi\) is a primary choice of a Gaussian prime above \(p\), up to the
sign of \(b\). Put

```math
B_p=\binom{(p-1)/2}{(p-1)/4}
```

and let

```math
q_p(2)=\frac{2^{p-1}-1}{p}
```

be the Fermat quotient to base \(2\).

Gauss proved

```math
B_p\equiv2a\pmod p.
```

Consequently the normalized first defect

```math
\Delta_p=\frac{B_p-2a}{p}\pmod p
```

is well defined.

## 2. The published modulo-\(p^2\) theorem

Chowla, Dwork, and Evans proved

```math
B_p\equiv
\left(1+\frac{2^{p-1}-1}{2}\right)
\left(2a-\frac{p}{2a}\right)
\pmod {p^2}.
```

The reciprocal in the second factor is interpreted in
\(\mathbb Z/p^2\mathbb Z\). Their proof uses the Gross--Koblitz formula and a
formula of Diamond.

This is already a split-Gaussian supercongruence: the ordinary binomial
coefficient is determined one \(p\)-adic digit beyond Gauss's congruence by a
coordinate of the primary factor \(a+bi\) of \(p\).

## 3. Exact first-defect law

### Corollary

For every prime and primary coordinate as above,

```math
\boxed{\;
\Delta_p
\equiv
a\,q_p(2)-(2a)^{-1}
\pmod p.
\;}
```

### Proof

Since \(2^{p-1}-1=pq_p(2)\), expand the published congruence modulo \(p^2\):

```math
\begin{aligned}
B_p
&\equiv
\left(1+\frac{p}{2}q_p(2)\right)
\left(2a-\frac{p}{2a}\right) \\
&\equiv
2a+p\left(aq_p(2)-\frac1{2a}\right)
\pmod {p^2}.
\end{aligned}
```

Subtract \(2a\), divide by \(p\), and reduce modulo \(p\). \(\square\)

The formula separates the first defect into two pieces:

- the global multiplicative defect \(q_p(2)\); and
- the reciprocal of the primary split coordinate \(2a\).

In the language used elsewhere in this repository, the leading
modulo-\(p\) packet is \(2a\), while the first normalized lift is a
one-dimensional defect profile.

## 4. Exceptional lift criterion

The Gauss congruence gains one additional power of \(p\),

```math
B_p\equiv2a\pmod {p^2},
```

if and only if

```math
\boxed{\;
2a^2q_p(2)\equiv1\pmod p.
\;}
```

This is just the vanishing condition for \(\Delta_p\). It gives a precise,
reproducible exceptional-prime search rather than a vague request for extra
divisibility.

The included checker verifies the published congruence, the defect formula,
and this criterion for all \(1{,}125\) primes \(p<20{,}000\) with
\(p\equiv1\pmod4\). In that finite range the only vanishing defect is
\(p=5\). This observation is evidence only; no finiteness or distribution
conjecture is asserted.

## 5. Relation to the Gaussian program

Write the primary prime as \(\pi=a+bi\). Then

```math
2a=\pi+\overline{\pi}.
```

The theorem therefore supplies a classical model for what a successful
split-prime completion should look like:

1. a finite-field or Gaussian quantity determines the leading residue;
2. a \(p\)-adic gamma or reciprocal-sum calculation determines the next
   digit; and
3. exceptional extra divisibility is the zero locus of an explicit defect.

It does **not** prove the rectangular split-prime conjectures elsewhere in
this repository. It says that their likely correction term should be sought
among primary Gaussian coordinates, Fermat quotients, and finite-field
gamma values rather than inferred from inert-prime data alone.

## 6. Concrete next questions

The published modulo-\(p^3\) continuation introduces Euler-number data. A
useful next project is to normalize that result as a second defect and compare
it with the two-level defect profiles already used for the Cooper and
Gaussian-product problems.

For the rectangular Gaussian coefficients, the corresponding target is:

- identify the leading split-prime packet after choosing a prime
  \(\pi\mid p\);
- derive its first normalized defect separately at \(\pi\) and
  \(\overline{\pi}\); and
- state extra divisibility as the vanishing of those explicit defects.

These are research targets, not consequences of the theorem in this note.

## 7. Reproduction

From the repository root, run:

```text
python verification/related/verify_chowla_dwork_evans_defect.py
```

The program uses exact integer binomial coefficients and modular inverses. It
does not numerically approximate a \(p\)-adic quantity.

## References

1. S. Chowla, B. Dwork, and R. J. Evans,
   [*On the mod \(p^2\) determination of
   \(\binom{(p-1)/2}{(p-1)/4}\)*](https://mathweb.ucsd.edu/~revans/ChowlaDwork.pdf),
   *Journal of Number Theory* **24** (1986), 188--196.
2. R. G. Ayoub, J. G. Huard, and K. S. Williams,
   [*Sarvadaman Chowla (1907--1995)*](https://people.math.carleton.ca/~williams/papers/pdf/218.pdf),
   *Notices of the AMS* **45** (1998), 594--598.

