# Gaussian Lucas ratios as non-Archimedean canonical products

## Status

**Structural synthesis with a proved local isometry theorem, July 26, 2026.**

This note reorganizes the existing Gaussian Lucas proofs around normalized
finite products and their logarithmic moments. The dominant-moment lemma below
is elementary but reusable. Section 6 proves that the normalized mixed-block
product is an exact analytic isometry, and indeed a disk automorphism, at the
ramified prime. The proposed splitting-type program is a research direction,
not a claimed theorem. No novelty claim is made for the general language of
non-Archimedean analytic products or inverse-function arguments.

The motivating coefficient is Definition 2 in Nikita Kalinin,
["Wolstenholme's theorem over Gaussian integers"](https://arxiv.org/abs/2504.07978).

## 1. The rectangular coefficient is a translated product

For integers \(A\ge C\ge1\) and \(B\ge D\ge1\), put

```math
Q(A,B;C,D)
=
\prod_{x=0}^{C-1}\prod_{y=0}^{D-1}
\frac{(A-x)+i(B-y)}{(x+1)+i(y+1)}.
\tag{1}
```

Set

```math
z_{u,v}=(u+1)+i(v+1),
\qquad
g=A-C+i(B-D).
\tag{2}
```

Reversing the two numerator indices gives the exact identity

```math
Q(A,B;C,D)
=
\prod_{u=0}^{C-1}\prod_{v=0}^{D-1}
\frac{z_{u,v}+g}{z_{u,v}}
=
\prod_{u=0}^{C-1}\prod_{v=0}^{D-1}
\left(1+\frac{g}{z_{u,v}}\right).
\tag{3}
```

Thus \(Q\) is a normalized finite canonical product in the translation
parameter \(g\). In particular, \(g=0\) implies \(Q=1\) without a congruence
argument.

## 2. The mixed-block analytic unit

At the ramified prime, write

```math
\varpi=1+i,
\qquad
2=-i\varpi^2.
```

The mixed residue block at scale \(2^r\) is

```math
U_r=
\left\{
a+bi:
1\le a,b\le2^r,
\qquad
\text{\(a,b\) are not both even}
\right\}.
\tag{4}
```

Define

```math
H_r(Z)=\prod_{\xi\in U_r}(2^rZ+\xi),
\qquad
F_r(Z)=\frac{H_r(Z)}{H_r(0)}.
\tag{5}
```

Then

```math
F_r(Z)
=
\prod_{\xi\in U_r}
\left(1+\frac{2^rZ}{\xi}\right).
\tag{6}
```

This is a finite analytic unit over \(\mathbb Q_2(i)\). Introduce the
reciprocal moments

```math
S_{r,k}=\sum_{\xi\in U_r}\xi^{-k}.
\tag{7}
```

For \(r\ge2\), the \(\varpi\)-adic logarithm converges and gives

```math
\log F_r(Z)
=
\sum_{k\ge1}c_{r,k}Z^k,
\qquad
c_{r,k}
=
\frac{(-1)^{k+1}}{k}2^{rk}S_{r,k}.
\tag{8}
```

The ramified-prime proof establishes

```math
v_\varpi(c_{r,1})=6r-3
\tag{9}
```

and places every \(k\ge2\) contribution at least one
\(\varpi\)-power deeper in the applications below. Consequently,

```math
F_r(Z)
\equiv
1+c_{r,1}Z
\pmod{\varpi^{6r-2}}
\tag{10}
```

for \(Z\in\mathbb Z[i]\).

This is the analytic core of the ramified congruence: the whole product
becomes linear to the precision relevant to the theorem.

## 3. Multiplicative rectangular cancellation

Let \(\Phi\) be the five-rectangle functional

```math
\begin{aligned}
\Phi(f)={}&
\sum_{u<A,\,v<B}f(u+iv)
+\sum_{u<A-C,\,v<B-D}f(u+iv)\\
&-\sum_{u<A-C,\,v<B}f(u+iv)
-\sum_{u<A,\,v<B-D}f(u+iv)\\
&-\sum_{u<C,\,v<D}f(u+iv).
\end{aligned}
\tag{11}
```

Cancellation of the overlapping rectangles gives

```math
\Phi(f)
=
\sum_{u=0}^{C-1}\sum_{v=0}^{D-1}
\left(f(u+iv+g)-f(u+iv)\right).
\tag{12}
```

In particular,

```math
\Phi(1)=0,
\qquad
\Phi(Z)=CDg.
\tag{13}
```

After the even-even points are removed from the large rectangular products,
the logarithm of the adjacent-scale ratio is exactly

```math
\log R_{2,r}
=
\sum_{k\ge1}c_{r,k}\Phi(Z^k).
\tag{14}
```

Thus the geometric factor \(CDg\) is not an experimental coincidence. It is
the first discrete moment of the translated rectangle.

## 4. Dominant-first-moment lemma

The following lemma isolates the reusable part of the argument.

### Lemma

Let \(K\) be a complete discretely valued field with uniformizer \(\pi\)
and valuation ring \(\mathcal O_K\). Work in an ideal on which logarithm and
exponential converge and satisfy

```math
\frac{\exp(x)-1}{x}
\in
1+\pi\mathcal O_K.
\tag{15}
```

Let \(c_k\in K\) and let \(\Phi\) be a linear functional on polynomials.
Suppose \(h=\Phi(Z)\ne0\), the series

```math
L=\sum_{k\ge1}c_k\Phi(Z^k)
\tag{16}
```

converges, and

```math
v_\pi(c_k\Phi(Z^k))
\ge
v_\pi(c_1h)+1
\qquad(k\ge2).
\tag{17}
```

Then

```math
v_\pi(\exp(L)-1)
=
v_\pi(c_1h).
\tag{18}
```

More precisely, there is an \(\eta\) in the valuation ring such that

```math
\exp(L)-1
=
c_1h(1+\pi\eta).
\tag{19}
```

### Proof

By (17), the nonleading part of (16) is \(c_1h\,\pi\eta_0\) for some
integral \(\eta_0\). Hence

```math
L=c_1h(1+\pi\eta_0)
```

and \(v_\pi(L)=v_\pi(c_1h)\). Equation (15) gives both (18) and (19).
\(\square\)

## 5. Recovery of the exact ramified theorem

In (14), take

```math
c_1=2^rS_{r,1},
\qquad
h=CDg.
```

The normalized rectangular power-sum estimate and the two exceptional
low-moment calculations in the
[ramified-prime proof](GaussianLucasRamifiedTwoTheorem.md)
verify (17). Equation (9) and the lemma therefore give, for \(g\ne0\),

```math
v_{1+i}(R_{2,r}-1)
=
6r-3+
v_{1+i}\!\left(CDg\right).
\tag{20}
```

The theorem is therefore an instance of a general phenomenon:

> An exact supercongruence exponent is the valuation of the first surviving
> logarithmic moment, provided every later moment lies one level deeper.

## 6. The mixed-block product is an exact disk isometry

The same coefficient estimates contain more information than the rectangular
congruence. Let

```math
\mathcal O=\mathbb Z_2[i],
\qquad
c_r=c_{r,1}=2^rS_{r,1}.
\tag{21}
```

### Theorem

For every \(r\ge2\) and all distinct \(Z,W\in\mathcal O\),

```math
v_\varpi\!\left(F_r(Z)-F_r(W)\right)
=
6r-3+v_\varpi(Z-W).
\tag{22}
```

More precisely,

```math
F_r(Z)-F_r(W)
=
c_r(Z-W)(1+\varpi\eta_{Z,W})
\tag{23}
```

for some \(\eta_{Z,W}\in\mathcal O\). Therefore the normalized map

```math
G_r(Z)=\frac{F_r(Z)-1}{c_r}
\tag{24}
```

is a bijective analytic isometry of \(\mathcal O\):

```math
v_\varpi\!\left(G_r(Z)-G_r(W)\right)
=
v_\varpi(Z-W).
\tag{25}
```

Equivalently,

```math
F_r:\mathcal O\longrightarrow1+c_r\mathcal O
\tag{26}
```

is a bijection and a similarity of ratio \(|c_r|_\varpi\). Its derivative has
constant valuation

```math
v_\varpi\!\left(F_r'(Z)\right)=6r-3
\qquad(Z\in\mathcal O).
\tag{27}
```

### Proof

Write \(L_r=\log F_r\). The reciprocal-moment estimates used above give the
slightly stronger coefficient statement

```math
v_\varpi(c_r)=6r-3,
\qquad
v_\varpi(c_{r,k})\ge6r-2
\quad(k\ge2).
\tag{28}
```

For \(Z,W\in\mathcal O\),

```math
\begin{aligned}
L_r(Z)-L_r(W)
&=
c_r(Z-W)
+
\sum_{k\ge2}c_{r,k}(Z^k-W^k)\\
&=
c_r(Z-W)(1+\varpi\alpha_{Z,W}),
\end{aligned}
\tag{29}
```

because \((Z^k-W^k)/(Z-W)\in\mathcal O\). Now

```math
F_r(Z)-F_r(W)
=
F_r(W)
\left(\exp(L_r(Z)-L_r(W))-1\right).
\tag{30}
```

The first factor lies in \(1+\varpi\mathcal O\), and the quotient
\((\exp D-1)/D\) does as well. Substitution of (29) proves (23), hence
(22) and (25).

Taking \(W=0\) in (23) shows

```math
G_r(Z)\equiv Z\pmod\varpi.
\tag{31}
```

Put \(G_r(Z)=Z+\varpi K_r(Z)\). Equation (23) also shows that \(K_r\) is
1-Lipschitz. For a prescribed \(Y\in\mathcal O\), the map

```math
Z\longmapsto Y-\varpi K_r(Z)
\tag{32}
```

is a strict contraction of the complete ring \(\mathcal O\). Its unique fixed
point satisfies \(G_r(Z)=Y\). Thus \(G_r\) is surjective; (25) already gives
injectivity. Differentiating (23), or taking limits of its difference
quotients, gives (27). \(\square\)

The four-coset lift also supplies a scale law for the leading coefficient:

```math
c_{r+1}
=
8c_r(1+\varpi\theta_r),
\qquad
\theta_r\in\mathcal O.
\tag{33}
```

Indeed,
\(S_{r+1,1}\equiv4S_{r,1}\pmod{\varpi^{4r+2}}\); multiplication by
\(2^{r+1}\) puts the error in
\(\varpi^{6r+4}\), one level above \(8c_r\). Since
\(8=i\varpi^6\), each scale increases the leading valuation by exactly six.
This is the local renormalization law behind the slope \(6r-3\).

### A finite-dimensional isometry chamber

The proof is stable under variation of the individual factors. For a parameter
vector \(\mathbf a=(a_\xi)_{\xi\in U_r}\in\mathcal O^{U_r}\), define

```math
F_{r,\mathbf a}(Z)
=
\prod_{\xi\in U_r}
\left(1+\frac{a_\xi2^rZ}{\xi}\right)
```

and write

```math
\log F_{r,\mathbf a}(Z)
=
\sum_{k\ge1}b_k(\mathbf a)Z^k,
\qquad
b_k(\mathbf a)
=
\frac{(-1)^{k+1}}{k}2^{rk}
\sum_{\xi\in U_r}a_\xi^k\xi^{-k}.
```

Call \(\mathbf a\) **first-moment dominant** when

```math
b_1(\mathbf a)\ne0,
\qquad
v_\varpi(b_k(\mathbf a))
\ge
v_\varpi(b_1(\mathbf a))+1
\quad(k\ge2).
```

For every first-moment-dominant parameter, the same difference-logarithm and
contraction proof gives a bijective analytic isometry

```math
Z\longmapsto
\frac{F_{r,\mathbf a}(Z)-1}{b_1(\mathbf a)}
```

of \(\mathcal O\). Thus the all-ones vector is not merely one isolated
identity: it lies in a finite-dimensional parameter region on which the
normalized product has the same rigid local geometry. The boundary problem is
to classify parameters where the first moment cancels or a later moment
reaches the same valuation. Such loci are natural candidates for exceptional
or strengthened supercongruences.

### A certified neighborhood of the unweighted block

The abstract dominance condition contains an explicit full-dimensional
neighborhood. This makes the word "region" above effective rather than merely
set-theoretic.

#### Theorem

Fix \(r\ge2\). If

\[
a_\xi\in1+\varpi^{4r-1}\mathcal O
\qquad(\xi\in U_r),
\tag{34}
\]

then

\[
v_\varpi(b_1(\mathbf a))=6r-3,
\qquad
v_\varpi(b_k(\mathbf a))\ge6r-2
\quad(k\ge2).
\tag{35}
\]

Moreover,

\[
\frac{b_1(\mathbf a)}{c_r}
\in1+\varpi\mathcal O,
\tag{36}
\]

and therefore

\[
Z\longmapsto
\frac{F_{r,\mathbf a}(Z)-1}{b_1(\mathbf a)}
\tag{37}
\]

is a bijective analytic isometry of \(\mathcal O\).

#### Proof

Write \(a_\xi=1+\delta_\xi\) and \(q=4r-1\). Since every
\(\xi\in U_r\) has \(v_\varpi(\xi)\le1\),

\[
v_\varpi\bigl(b_1(\mathbf a)-c_r\bigr)
\ge2r+q-1
=6r-2.
\tag{38}
\]

Together with \(v_\varpi(c_r)=6r-3\), this proves the first assertion in
(35) and (36).

For \(k\ge2\), the factorization
\(a_\xi^k-1=(a_\xi-1)(1+a_\xi+\cdots+a_\xi^{k-1})\) gives
\(v_\varpi(a_\xi^k-1)\ge q\). Hence

\[
v_\varpi\bigl(b_k(\mathbf a)-c_{r,k}\bigr)
\ge
2rk-2v_2(k)+q-k.
\tag{39}
\]

The right side is at least \(6r-2\), because

\[
(2r-1)(k-1)\ge2v_2(k)
\qquad(r\ge2,\ k\ge2).
\tag{40}
\]

Indeed \(v_2(k)\le k-1\) and \(2r-1\ge3\). The unweighted estimate
\(v_\varpi(c_{r,k})\ge6r-2\) from (28) now proves the second assertion in
(35). Thus every parameter vector in (34) is first-moment dominant, and
the preceding difference-logarithm and contraction argument proves (37).
\(\square\)

The radius in (34) is sharp for a uniform coordinatewise ball. To see this,
keep every weight equal to \(1\) except at \(\xi_0=1+i\), and put

\[
a_{\xi_0}
=1-\frac{c_r\xi_0}{2^r}.
\tag{41}
\]

The perturbation has exact valuation

\[
v_\varpi\left(\frac{c_r\xi_0}{2^r}\right)
=(6r-3)+1-2r
=4r-2.
\]

Thus this vector belongs to the larger coordinatewise ball with exponent
\(4r-2\). But its first logarithmic coefficient is

\[
b_1(\mathbf a)
=c_r-\frac{2^r}{\xi_0}\frac{c_r\xi_0}{2^r}
=0.
\tag{42}
\]

Thus replacing \(4r-1\) by \(4r-2\) would include a parameter vector for
which first-moment dominance fails completely.

The exact checker
[`verify_gaussian_product_isometry.py`](../verification/related/verify_gaussian_product_isometry.py)
tests (22), (25), and the neighborhood theorem on 1,800 pairs at scales
\(r=2,3\), and checks the two sharp boundary witnesses, using exact arithmetic
in \(\mathbb Q(i)\).

## 7. Relation with Blaschke products

The analogy with a finite Blaschke product is structural, not literal.
Both constructions:

1. normalize a product into factors close to \(1\);
2. use a logarithm to replace the product by moments of its zeros or lattice
   points; and
3. obtain global control from cancellation among those moments.

A complex Blaschke factor pairs a zero with a reflected pole so that the
product has unit modulus on a boundary. Equation (6) instead pairs a Gaussian
lattice block with its translation. Its distinguished property is
\(\varpi\)-adic proximity to \(1\), not unit modulus on the complex unit
circle. "Non-Archimedean canonical product" is therefore the more accurate
description.

## 8. Splitting-type research program

The product viewpoint suggests organizing Gaussian Lucas congruences locally,
according to the behavior of a rational prime in \(\mathbb Z[i]\).

| Rational prime | Local behavior | Product question |
| --- | --- | --- |
| \(p\equiv3\pmod4\) | inert | control reciprocal moments in the full quadratic residue field |
| \(p\equiv1\pmod4\) | split as \(\pi\bar\pi\) | normalize and analyze the \(\pi\)- and \(\bar\pi\)-adic products separately |
| \(p=2\) | ramified as a unit times \((1+i)^2\) | use the mixed-parity block and its four-coset lift |

For a prime ideal \(\mathfrak p\), the desired local statement has the form

```math
R_{\mathfrak p,r}-1
=
c_{\mathfrak p,r}\,
CD\bigl(A-C+i(B-D)\bigr)
+\text{one valuation level deeper},
\tag{43}
```

where \(c_{\mathfrak p,r}\) is the first reciprocal moment of the relevant
local residue block.

The inert and ramified proof candidates already fit this template. The split
case is the important obstruction: rational \(p\)-scaling mixes the two prime
ideals, so a theorem should be formulated after localization and suitable
normalization rather than by copying the inert statement.

## 9. Review boundary

The identities (3), (8), and (12)--(14), and the dominant-moment lemma are
proved algebraically. Equation (20) is the existing ramified-prime theorem,
not a new independent proof. The disk-isometry theorem is a new deduction
from the same reciprocal-moment bounds; its contraction argument is standard
non-Archimedean analytic infrastructure.

The claims still requiring specialist attention are:

1. the full ramified reciprocal-moment estimates used to verify (17);
2. priority for the exact ramified and disk-isometry theorems;
3. the correct normalization at split primes; and
4. whether the local formulation (34) is already implicit in a general
   theorem on factorial products over local fields.
