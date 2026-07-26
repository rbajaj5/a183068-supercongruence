# A return theorem for the ramified Gaussian product

## Status

**Complete deduction from the ramified reciprocal-moment estimates, July 26,
2026. The conjugacy statement in Section 4 remains conjectural.**

The main result determines every finite-quotient cycle length exactly. Exact
arithmetic independently checks the conclusion through the ranges in Section
5. Conventional review and a priority search remain necessary.

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

is a bijective analytic isometry of \(\mathcal O\). For a unit
\(u\in\mathcal O^\times\), define

```math
T_{r,u}(Z)=G_r(Z)+u.
\tag{1}
```

The reduction of (1) modulo \(\varpi^n\) is a permutation of a set of
\(2^n\) elements.

## 2. Arithmetic normal form

The extra fact needed for the dynamics is stronger than the previously stated
isometry congruence.

### Lemma 1

For every \(r\ge2\), there is an analytic 1-Lipschitz map
\(h_r:\mathcal O\to\mathcal O\) such that

```math
G_r(Z)=Z+4h_r(Z).
\tag{2}
```

### Proof

Write

```math
\log F_r(Z)=\sum_{k\ge1}a_{r,k}Z^k,
\qquad
a_{r,k}=\frac{(-1)^{k+1}}{k}2^{rk}S_{r,k},
\qquad
a_{r,1}=c_r.
\tag{3}
```

The reciprocal-moment theorem gives

```math
v_\varpi(c_r)=6r-3
\tag{4}
```

and, for \(k\ge2\),

```math
v_\varpi(a_{r,k})
\ge
4r+2k(r-1)-2v_2(k).
\tag{5}
```

Suppose first that \(r\ge3\). For \(k\ge3\), the elementary inequality

```math
(r-1)(k-1)\ge v_2(k)+2
```

puts (5) at least five \(\varpi\)-powers above \(c_r\). The same holds
for \(k=2\) when \(r\ge4\). At \(r=3,k=2\), use the four-coset recurrence
for \(S_{r,k}\). The \(j=0,1,2\) terms have valuations at least
\(10,12,10\), respectively, while the \(j\ge3\) terms have valuation at
least \(2j+4\). Hence

```math
v_\varpi(S_{3,2})\ge10,
\qquad
v_\varpi(a_{3,2}/c_3)\ge5.
```

Therefore, for every \(r\ge3\),

```math
\frac{\log F_r(Z)}{c_r}
=
Z+\varpi^5B_r(Z)
\tag{6}
```

with \(B_r\) an integral restricted power series. Expanding the exponential
does not affect this precision: the first nonlinear exponential contribution
after division by \(c_r\) has valuation at least

```math
v_\varpi(c_r)-v_\varpi(2)=6r-5\ge13.
```

Thus \(G_r(Z)-Z\) has all coefficients divisible by \(\varpi^5\) when
\(r\ge3\).

At \(r=2\), the exact twelve-term base table in the ramified-prime proof gives

```math
v_\varpi(a_{2,2}/c_2)
=
v_\varpi(a_{2,4}/c_2)
=3,
\tag{7}
```

while every other \(a_{2,k}/c_2\), \(k\ge2\), has valuation at least
six. The estimate for \(k\ge8\) follows from
\(v_\varpi(S_{2,k})\ge-k\). Since the residue field is \(\mathbb F_2\), the
two unit coefficients in (7) have the same residue. Consequently

```math
\frac{\log F_2(Z)}{c_2}
=
Z+\varpi^3u(Z^2+Z^4)+\varpi^4B_2(Z)
\tag{8}
```

for a unit \(u\) and an integral restricted power series \(B_2\). Nonlinear
terms in the exponential begin seven powers deep after division by \(c_2\),
so (8) also describes \(G_2\) to the displayed precision.

For \(X,Y\in\mathcal O\),

```math
\begin{aligned}
&(X^2+X^4)-(Y^2+Y^4)\\
&\quad=(X-Y)
\left(X+Y+X^3+X^2Y+XY^2+Y^3\right).
\end{aligned}
\tag{9}
```

The parenthesized factor vanishes after reducing \(X,Y\) to
\(\mathbb F_2\), and is therefore divisible by \(\varpi\). Equation (8)
now shows

```math
v_\varpi\bigl((G_2(X)-X)-(G_2(Y)-Y)\bigr)
\ge4+v_\varpi(X-Y).
\tag{10}
```

For \(r\ge3\), (10) follows coefficientwise from (6). Taking \(Y=0\)
also shows \(G_r(X)-X\in\varpi^4\mathcal O=4\mathcal O\). Division by
\(4=-\varpi^4\) proves (2) and the 1-Lipschitz property. \(\square\)

## 3. Exact return valuation

The dynamical part is a general near-translation lemma.

### Lemma 2

Let \(h:\mathcal O\to\mathcal O\) be 1-Lipschitz, let \(u\) be a unit,
and put

```math
T(Z)=Z+u+4h(Z).
\tag{11}
```

Then, for every \(m\ge0\) and \(Z\in\mathcal O\),

```math
v_\varpi\left(T^{2^m}(Z)-Z\right)=2m.
\tag{12}
```

### Proof

The map \(T\) is an isometry because its nonlinear difference is four
valuation levels deeper than \(X-Y\). Put

```math
E_m(Z)=\sum_{j=0}^{2^m-1}h(T^jZ).
\tag{13}
```

Then

```math
T^{2^m}(Z)-Z=2^mu+4E_m(Z).
\tag{14}
```

We prove simultaneously that (12) holds and, for \(m\ge1\),

```math
v_\varpi(E_m(Z))\ge2m-2.
\tag{15}
```

The bound (15) is trivial at \(m=1\); equation (14) then proves (12)
because \(v_\varpi(2u)=2<4\).

Assume both claims at level \(m\). Since every iterate of \(T\) is an
isometry,

```math
v_\varpi\left(
T^{j+2^m}Z-T^jZ
\right)=2m.
```

The 1-Lipschitz property of \(h\) therefore gives

```math
E_{m+1}(Z)
\equiv
2E_m(Z)
\pmod{\varpi^{2m}}.
\tag{16}
```

Now (15) and \(v_\varpi(2)=2\) imply
\(v_\varpi(E_{m+1})\ge2m\). In (14) at level \(m+1\), the translation
term has exact valuation \(2m+2\), while the error has valuation at least
\(2m+4\). This proves (12) and closes the induction. The case \(m=0\)
is immediate from (11). \(\square\)

### Theorem

For every \(r\ge2\), every unit \(u\in\mathcal O^\times\), every
\(Z\in\mathcal O\), and every integer \(m\ge0\),

```math
v_\varpi\left(T_{r,u}^{\,2^m}(Z)-Z\right)=2m.
\tag{17}
```

Consequently, on \(\mathcal O/\varpi^n\mathcal O\), every cycle of
\(T_{r,u}\) has length

```math
2^{\lceil n/2\rceil},
\tag{18}
```

and the number of cycles is

```math
2^{\lfloor n/2\rfloor}.
\tag{19}
```

### Proof

Lemma 1 puts \(T_{r,u}\) in the form required by Lemma 2. Modulo
\(\varpi\), it is the unique two-cycle \(Z\mapsto Z+1\) on
\(\mathbb F_2\). A cycle lifts through a fiber of size two by either staying
the same length or doubling. Its length is therefore a power of two, and
(17) says that the first returning power is (18). Dividing the \(2^n\)
points by this common length gives (19). \(\square\)

Equations (18)--(19) are exactly the cycle profile of ordinary translation
\(Z\mapsto Z+u\). This is not the profile of a random permutation and is not
a single-cycle permutation once \(n\ge2\).

## 4. Conjugacy conjecture

The agreement with translation suggests a stronger explanation.

### Conjecture

For every \(r\ge2\) and every unit \(u\in\mathcal O^\times\), there is a
compatible bijective isometry \(H_{r,u}:\mathcal O\to\mathcal O\) such that

```math
H_{r,u}\!\left(T_{r,u}(Z)\right)
=
H_{r,u}(Z)+u.
\tag{20}
```

The first version to seek is topological or 1-Lipschitz conjugacy. Analytic
conjugacy is stronger and should not be assumed without controlling the
denominators in the associated Abel equation. The theorem is necessary
evidence for (20), but matching cycle lengths on every finite quotient does
not by itself construct a compatible conjugacy.

## 5. Exact verification

The checker encodes a class modulo \(\varpi^n\) by its unique first \(n\)
uniformizer digits. It evaluates the product and its normalization in exact
\(\mathbb Q(i)\) arithmetic; no floating-point approximation or hash-based
identification is used.

The following tests pass:

- \(r=2\): every unit translation class at every precision \(1\le n\le8\);
- \(r=3\): every unit translation class at every precision \(1\le n\le6\);
- \(r=2\): the four translations \(1,i,1+\varpi,1+\varpi^2\) through
  \(n=12\);
- \(r=3\): the same four translations through \(n=7\); and
- deep mode: \(r=2,u=1\) through \(n=15\).

The all-unit portion comprises 318 exact quotient permutations. No cycle
length other than (18) occurs.

Run:

```text
python verification/related/experiment_gaussian_product_dynamics.py
python verification/related/experiment_gaussian_product_dynamics.py --deep
```

## 6. Mathematical and cryptographic meaning

The translated products are highly structured permutations but not ergodic
full-cycle generators. Their orbit length grows only like the square root of
the state-space size:

```math
2^{\lceil n/2\rceil}
\quad\text{versus}\quad
2^n.
```

That is a useful negative result for deployment claims. The arithmetic
construction gives exact bijectivity and predictable cycles, not immediate
pseudorandomness.

Mathematically, (17) says that a nonlinear product built from Gaussian
reciprocal sums has the same entire return-valuation filtration as addition.
The proof separates into an arithmetic normal form and a general
near-translation induction. The remaining Abel-equation problem is whether
the agreement is explained by an actual compatible conjugacy.

The general theory of compatible \(p\)-adic maps explains why transitivity on
all finite quotients is the relevant ergodic condition. Work on analytic maps
tangent to the identity supplies a neighboring conjugacy theory. Two useful
entry points are Anashin's
["Ergodic Transformations of the Space of \(p\)-adic
Integers"](https://arxiv.org/abs/math/0602083) and Jenkins--Spallone's
["A \(p\)-adic approach to local analytic
dynamics"](https://arxiv.org/abs/0712.0963). Neither source has yet been
shown to imply (20) for this ramified Gaussian product.

## 7. Review boundary

The return theorem is a deduction from the reciprocal-moment estimates, not
an independent verification of them. Its main review points are:

1. the exceptional \(r=2\) coefficient calculation in (7)--(10);
2. the \(r=3,k=2\) lift used before (6);
3. the simultaneous induction (13)--(16);
4. whether a general local-dynamics theorem already contains Lemma 2; and
5. whether the finite conjugacies can be chosen compatibly to prove (20).

No novelty claim is made before those points and a specialist priority search
are resolved.
