# Affine-word grammar and almost periodicity of dyadic twists

## Status

This note connects two exact structures already present in the public
Roe-inspired project:

1. the normal-form grammar of the finite affine shadow; and
2. almost periodicity for convolutions on finite abelian groups.

The normal form is an elementary deduction from the affine multiplication
law. The analytic statement is a direct specialization of Yuval Wigderson's
exposition of the Croot--Sisask almost-periodicity argument. No novelty claim
is made for that theorem or for its specialization here.

The purpose is to state precisely what the language analogy buys and where
the additive-combinatorial theorem applies.

## 1. An exact grammar for affine words

For $m\geq3$, put

$$
R_m=\mathbb Z/2^m\mathbb Z,
\qquad
G_m=R_m\rtimes R_m^\times.
$$

Write

$$
T_b=M(1,b),
\qquad
U_u=M(u,0).
$$

Here $T_b$ is the image of the dyadic Dehn twist with parameter $b$, while
$U_u$ is a unit scaling. Matrix multiplication gives the production and
rewriting rules

$$
T_bT_c=T_{b+c},
\qquad
U_uU_v=U_{uv},
\qquad
U_uT_b=T_{ub}U_u.
\tag{1}
$$

### Proposition 1

Every word in the symbols $T_b,U_u$ rewrites to a unique normal form

$$
T_bU_u.
\tag{2}
$$

#### Proof

Orient the third rule in (1) from left to right. Each application moves a
translation one place to the left, so the number of unit-before-translation
inversions strictly decreases. The first two rules then combine adjacent
symbols of the same type. Hence every word reaches a form (2).

Moreover,

$$
T_bU_u=M(u,b).
$$

Equality of two normal forms is therefore equality of their two matrix
coordinates. Thus $T_bU_u=T_cU_v$ implies $b=c$ and $u=v$. $\square$

In linguistic language, moving the translation to the front resembles
topicalization, but equation (1) is the mathematical content: fronting the
twist changes its parameter from $b$ to $ub$. The grammar is a terminating
normal-form procedure, not a claim about natural-language syntax.

## 2. Dense twist averages

Fix a unit $u\in R_m^\times$ and a bounded observable

$$
f:G_m\longrightarrow[0,1].
$$

Use the coordinate

$$
g_u(y)=f(M(u,uy)),
\qquad y\in R_m.
$$

For a nonempty set of twist parameters $A\subseteq R_m$, define

$$
H_{A,u}(y)
=
\mathbb E_{a\in A}
f\bigl(M(u,uy)T_{-a}\bigr).
\tag{3}
$$

Since

$$
M(u,uy)T_{-a}=M(u,u(y-a)),
$$

equation (3) is exactly the additive convolution

$$
H_{A,u}=\mu_A*g_u
\tag{4}
$$

on $R_m$.

### Theorem 2 - twist almost periodicity

Let $A\subseteq R_m$ have density $\alpha>0$, let
$\varepsilon\in(0,1)$, and let $p\geq1$. There is a set $X\subseteq R_m$
with

$$
\mu(X)\geq
\alpha^{Cp/\varepsilon^2}
\tag{5}
$$

such that, for every $c\in X-X$,

$$
\left(
\mathbb E_{y\in R_m}
\left|H_{A,u}(y-c)-H_{A,u}(y)\right|^p
\right)^{1/p}
\leq\varepsilon.
\tag{6}
$$

Here $C>0$ is an absolute constant.

#### Proof

Apply Theorem 3.1 of Wigderson's exposition to the finite abelian group
$R_m$, the set $A$, and the function $g_u$. Its conclusion is

$$
\left\|
\mu_c*\mu_A*g_u-\mu_A*g_u
\right\|_p
\leq\varepsilon
$$

for every $c\in X-X$, with the density bound (5). Convolution by $\mu_c$ is
translation by $c$, and (4) converts the displayed inequality into (6).
$\square$

Thus averaging a bounded quantity over a dense family of dyadic Dehn twists
creates many approximate symmetries under further twists. The statement is
uniform in the modulus, although the resulting set $X$ depends on the
observable, the averaging set, and the chosen unit fiber.

## 3. Why the spectrum is cyclotomic

Let

$$
\zeta_m=\exp(2\pi i/2^m).
$$

The additive characters of $R_m$ are

$$
\chi_k(y)=\zeta_m^{ky},
\qquad 0\leq k<2^m.
$$

They diagonalize (4):

$$
\widehat{H_{A,u}}(k)
=
\widehat{\mu_A}(k)\widehat{g_u}(k).
$$

A translation by $c$ multiplies the $k$-th coefficient by
$\zeta_m^{-kc}$. Consequently, an almost period is a twist parameter on
which the cyclotomic phases supporting the convolution are simultaneously
close to $1$.

This is the connection with Bohr sets. Wigderson observes that the final
finite-field subspace step has a general-abelian analogue in which subspaces
are replaced by Bohr sets. In the dyadic translation group, those Bohr sets
are cut out by a small family of $2^m$-th-root cyclotomic phases.

## 4. Boundary of the deduction

The theorem concerns an averaged observable on one additive translation
fiber. It does not imply:

- a better spectral gap for the fixed-generator Cayley walk;
- simultaneous almost periodicity on every unit fiber;
- mixing of the full outer automorphism group;
- pseudorandomness or cryptographic security; or
- a new supercongruence.

The value is structural. Proposition 1 turns affine words into canonical
syntax, while Theorem 2 says that dense averages of the translation
constituents admit a compressed approximate-symmetry set.

## 5. Verification

Run:

```text
python verification/related/verify_dyadic_twist_grammar.py
```

The checker verifies the three rewriting identities, uniqueness and
exhaustion of normal forms through modulus $2^7$, and the exact identity
between twist averaging and additive convolution.

## References

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of $\mathbb Q_2$*][RT].
- Y. Wigderson,
  [*An exposition of almost periodicity*][W].
- E. Croot and O. Sisask,
  [*A probabilistic technique for finding almost-periods of
  convolutions*][CS].

[RT]: https://roed314.github.io/gq2/paper.pdf
[W]: https://ywigderson.math.ethz.ch/math/static/AlmostPeriodicity.pdf
[CS]: https://doi.org/10.1007/s00222-011-0331-8
