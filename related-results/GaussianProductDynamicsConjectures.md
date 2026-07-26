# Cycle conjectures for the ramified Gaussian product

## Status

**Exact computational conjectures, July 26, 2026.**

The statements below are not proved. They are supported by exact arithmetic
on finite quotients, with every unit translation checked through the ranges
listed in Section 4. The point is to turn the broad cryptographic analogy into
a sharp question whose failure would have a concrete certificate.

The underlying analytic isometry is proved, conditional only on the
reciprocal-moment estimates in the ramified-prime draft, in the
[canonical-product note](GaussianLucasCanonicalProducts.md#6-the-mixed-block-product-is-an-exact-disk-isometry).

## 1. The translated product

Put

```math
\varpi=1+i,
\qquad
\mathcal O=\mathbb Z_2[i],
```

and, for \(r\ge2\), let

```math
F_r(Z)
=
\prod_{\substack{1\le a,b\le2^r\\
                  \text{\(a,b\) not both even}}}
\left(1+\frac{2^rZ}{a+bi}\right).
```

If

```math
c_r=F_r'(0)
=
2^r
\sum_{\substack{1\le a,b\le2^r\\
                 \text{\(a,b\) not both even}}}
\frac1{a+bi},
```

then

```math
G_r(Z)=\frac{F_r(Z)-1}{c_r}
```

is a bijective analytic isometry of \(\mathcal O\) satisfying

```math
G_r(Z)\equiv Z\pmod\varpi.
```

For a unit \(u\in\mathcal O^\times\), define

```math
T_{r,u}(Z)=G_r(Z)+u.
\tag{1}
```

The reduction of (1) modulo \(\varpi^n\) is a permutation of a set of
\(2^n\) elements.

## 2. Return-valuation conjecture

### Conjecture A

For every \(r\ge2\), every unit \(u\in\mathcal O^\times\), every
\(Z\in\mathcal O\), and every integer \(m\ge0\),

```math
v_\varpi\left(T_{r,u}^{\,2^m}(Z)-Z\right)=2m.
\tag{2}
```

Consequently, on \(\mathcal O/\varpi^n\mathcal O\), every cycle of
\(T_{r,u}\) has length

```math
2^{\lceil n/2\rceil},
\tag{3}
```

and the number of cycles is

```math
2^{\lfloor n/2\rfloor}.
\tag{4}
```

The consequence follows because cycles lift through successive quotients with
residue-field fiber of size two, so their lengths can only stay fixed or
double, while \(2^m\) is the first power-of-two iterate in (2) whose
displacement is divisible by \(\varpi^n\).

Equations (3)--(4) are exactly the cycle profile of ordinary translation
\(Z\mapsto Z+u\). This is not the profile of a random permutation and is not
a single-cycle permutation once \(n\ge2\).

## 3. Conjugacy conjecture

The repeated agreement with translation suggests a stronger explanation.

### Conjecture B

For every \(r\ge2\) and every unit \(u\in\mathcal O^\times\), there is a
compatible bijective isometry \(H_{r,u}:\mathcal O\to\mathcal O\) such that

```math
H_{r,u}\!\left(T_{r,u}(Z)\right)
=
H_{r,u}(Z)+u.
\tag{5}
```

The first version to seek is topological or 1-Lipschitz conjugacy. Analytic
conjugacy is a stronger possibility and should not be assumed without
controlling the denominators in the associated Abel equation.

Conjecture B implies Conjecture A. The converse need not hold: matching cycle
lengths on every finite quotient does not by itself construct a compatible
conjugacy.

## 4. Exact evidence

The checker encodes a class modulo \(\varpi^n\) by its unique first \(n\)
uniformizer digits. It evaluates the product and its normalization in exact
\(\mathbb Q(i)\) arithmetic; no floating-point approximation or hash-based
identification is used.

The following tests pass:

- \(r=2\): every unit translation class at every precision \(1\le n\le8\);
- \(r=3\): every unit translation class at every precision \(1\le n\le6\);
- \(r=2\): the four translations \(1,i,1+\varpi,1+\varpi^2\) through
  \(n=12\);
- \(r=3\): the same four translations through \(n=7\).

The all-unit portion comprises 318 exact quotient permutations. No cycle
length other than (3) occurs.

Run:

```text
python verification/related/experiment_gaussian_product_dynamics.py
```

## 5. Mathematical and cryptographic meaning

If Conjecture A holds, the translated products are highly structured
permutations but not ergodic full-cycle generators. Their orbit length grows
only like the square root of the state-space size:

```math
2^{\lceil n/2\rceil}
\quad\text{versus}\quad
2^n.
```

That is a useful negative result for deployment claims. The arithmetic
construction gives exact bijectivity and predictable cycles, not immediate
pseudorandomness.

The mathematical question remains worthwhile because (2) would say that a
nonlinear product built from Gaussian reciprocal sums has the same entire
return-valuation filtration as addition. A proof should probably use one of
two mechanisms:

1. solve the non-Archimedean Abel equation (5) by successive approximation;
   or
2. prove (2) directly by controlling the error accumulated over
   \(2^m\) iterates.

The general theory of compatible \(p\)-adic maps explains why transitivity on
all finite quotients is the relevant ergodic condition. Work on analytic maps
tangent to the identity supplies a neighboring conjugacy theory. Neither
literature source has yet been shown to imply (2) for this ramified Gaussian
product.

Two useful entry points are Anashin's
["Ergodic Transformations of the Space of \(p\)-adic
Integers"](https://arxiv.org/abs/math/0602083) and Jenkins--Spallone's
["A \(p\)-adic approach to local analytic
dynamics"](https://arxiv.org/abs/0712.0963).

## 6. Failure certificates and review boundary

The conjecture is deliberately easy to falsify. A counterexample consists of

```text
(r, u mod varpi^n, n, one cycle length)
```

with the cycle length different from (3), or equivalently a triple
\((r,u,Z)\) and exponent \(m\) for which (2) fails.

The main proof obligations are:

1. show that nonlinear errors do not lower the valuation after
   \(2^m\) iterates;
2. exclude cancellation that would raise the valuation above \(2m\);
3. decide whether the finite conjugacies can be chosen compatibly; and
4. determine whether a general local-dynamics theorem already supplies (5).

No novelty claim is made before those points and a specialist priority search
are resolved.
