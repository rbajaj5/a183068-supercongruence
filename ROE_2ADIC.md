# Public 2-adic Roe-inspired follow-on

This is the public landing page for the $2$-adic project prompted by David
Roe and David Turturean's
[*A Presentation of the Absolute Galois Group of $\mathbb Q_2$*][RT].

The detailed proofs and checker are:

- [orientation lifts, Dehn twists, and affine symmetry](related-results/GQ2OrientationLifts.md);
- [exact sampling and mixing on the dyadic Dehn-twist shadow](related-results/DyadicDehnTwistSampler.md);
- [a fixed-generator Cayley walk on the dyadic Dehn-twist shadow](related-results/DyadicDehnTwistCayleyWalk.md);
- [affine-word grammar and almost periodicity of dyadic twists](related-results/DyadicTwistGrammarAlmostPeriodicity.md);
- [conjugacy shells and exact twist-depth moments](related-results/DyadicDehnTwistConjugacyMoments.md);
- [`verify_gq2_orientation_lifts.py`](verification/related/verify_gq2_orientation_lifts.py);
- [`verify_dyadic_dehn_twist_sampler.py`](verification/related/verify_dyadic_dehn_twist_sampler.py);
- [`verify_dyadic_dehn_twist_cayley.py`](verification/related/verify_dyadic_dehn_twist_cayley.py); and
- [`verify_dyadic_twist_grammar.py`](verification/related/verify_dyadic_twist_grammar.py).

[RT]: https://roed314.github.io/gq2/paper.pdf
[Gropper]: https://arxiv.org/abs/2303.04309

## What is proved

### 1. Exact orientation lifting

Let $X\in\mathbb Z_2$ be the root

$$
X^3+2X^2+1=0,\qquad X\equiv5\pmod8.
$$

There is a unique $\alpha\in\mathbb Z_2$ such that

$$
X^\alpha=-\frac13.
$$

At precision $2^k$, every solution is in the single class

$$
e\equiv\alpha\pmod {2^{k-2}}.
$$

The compatible limit $\alpha$ is not an ordinary integer. Thus all finite
orientation congruences are soluble and compatible even though no one fixed
finite exponent solves them all.

### 2. An exact dyadic Dehn-twist tower

The standard rank-three dyadic Demushkin group has the HNN presentation

$$
D_0=
\left\langle A,S,Y\ \middle|\
Y^{-1}SY=S^{-3}A^{-2}\right\rangle_{\mathrm{pro}\text{-}2}.
$$

For every $b\in\mathbb Z_2$,

$$
\mathcal T_b(A)=A,\qquad
\mathcal T_b(S)=S,\qquad
\mathcal T_b(Y)=S^bY
$$

defines an automorphism, and

$$
b\longmapsto[\mathcal T_b]
$$

embeds $\mathbb Z_2$ continuously into
$\mathrm{Out}(D_0)$. These are the pro-$2$ HNN Dehn twists. Their
depth on the abelianization is exactly $v_2(b)$.

### 3. The affine shadow

The full orientation-preserving abelian shadow is

$$
\mathrm{Aut}(B_{\mathrm{ab}},\chi)
\cong
\mathbb Z_2\rtimes\mathbb Z_2^\times,
$$

with matrices

$$
M(u,b)=
\begin{pmatrix}u&b\\0&1\end{pmatrix}.
$$

Roe--Turturean Proposition 3.9 makes the natural map from
$\mathrm{Out}(D_0)$ onto this affine group surjective. The twists
give an explicit section of its translation subgroup.

The commutator depth is exact:

$$
v_2\!\left((1-u^{-1})b\right)
=v_2(u-1)+v_2(b),
$$

and the lower-central translation layers are

$$
\gamma_n=2^{n-1}\mathbb Z_2
\qquad(n\ge2).
$$

### 4. Symmetry of the defect tower

The Dehn twists preserve the orientation condition and act equivariantly on
every finite stage of the Appendix C.5 defect-lifting construction. They are
therefore symmetries of the $D_0$ half of the existing proof tower, not a
separate analogy. This note does not construct a corresponding twist family
for $D_R$.

### 5. Exact sampling and mixing

Modulo $2^m$, every affine-shadow element has unique coordinates

$$
M((-1)^\sigma5^a,b),
\qquad
\sigma\in C_2,\quad
a\in C_{2^{m-2}},\quad
b\in\mathbb Z/2^m\mathbb Z.
$$

These are $2m-1$ binary coordinates. They give an information-theoretically
optimal exact uniform sampler, and every lift from level $m$ to level $m+1$
uses precisely two new independent bits. A random coordinate-refresh chain
has the explicit Boolean-cube spectrum

$$
1-\frac j{2m-1}
\quad\text{with multiplicity}\quad
\binom{2m-1}{j},
$$

and total-variation cutoff at

$$
\frac{2m-1}{2}\log(2m-1).
$$

The translation-coordinate updates are images of the dyadic Dehn twists.
This is a classical mixing calculation on the exact affine quotient, not a
claim about mixing in the full outer automorphism group.

### 6. A fixed-generator cyclotomic walk

Coordinate refresh uses direct access to the binary lift coordinates. There
is also a genuine right Cayley walk using only the fixed generators

$$
\mathcal T_1,\quad\mathcal T_{-1},\quad5,\quad5^{-1},\quad-1.
$$

For the one-half-lazy symmetric walk on $G_m$, $m\geq4$, its spectral gap
$\gamma_m$ satisfies

$$
\frac15\left(1-\cos\frac{2\pi}{2^m}\right)
\leq\gamma_m\leq
\frac15\left(1-\cos\frac{2\pi}{2^{m-2}}\right).
$$

The unit eigenvalues are traces of $2^{m-2}$-th roots of unity:

$$
\frac{\zeta^k+\zeta^{-k}+(-1)^s}{3}.
$$

Thus the calculation is cyclotomic, and the relaxation time is
$\Theta(4^m)$. This quantifies the algorithmic price of restricting the
sampler to fixed local group operations.

### 7. Grammar and twist almost periodicity

Writing $T_b=M(1,b)$ and $U_u=M(u,0)$ gives the exact rewrite rule

$$
U_uT_b=T_{ub}U_u.
$$

Every affine word therefore has a unique translation-first normal form
$T_bU_u$. On a fixed unit fiber, averaging any bounded observable over a
dense set $A$ of twist parameters is exactly additive convolution on
$\mathbb Z/2^m\mathbb Z$.

Wigderson's finite-group almost-periodicity theorem then gives a set $X$ of
density at least

$$
\alpha^{Cp/\varepsilon^2}
$$

such that every $c\in X-X$ is an $\ell^p$-almost period, with error at most
$\varepsilon$, for the averaged observable. Fourier characters identify
these approximate symmetries with cyclotomic phases. This is a specialization
of an existing theorem, not a new priority claim or an improvement of the
Cayley spectral gap.

## Source boundary

| Item | Status |
| --- | --- |
| Dyadic Demushkin presentation and orientation | Roe--Turturean |
| HNN rewriting and the shear $\Theta_b$ | Roe--Turturean, equation (3.9) and Proposition 3.9 |
| Arithmetic-Dehn-twist framework | [Gropper][Gropper] |
| Exact exponent class and proof that its limit is nonintegral | Deduction recorded here |
| Identification of the shear's outer class with the HNN Dehn twist | Deduction recorded here |
| Exact affine commutator and lower-central filtration | Deduction recorded here |
| Equivariance on the Appendix C.5 defect stages | Deduction recorded here |
| Optimal lift-bit sampler and coordinate-refresh spectrum | Elementary deduction recorded here; classical finite-probability machinery |
| Fixed-generator Cayley walk and cyclotomic gap bounds | Elementary deduction recorded here; priority not claimed |
| Affine normal-form grammar | Elementary deduction recorded here |
| Twist almost-periodicity estimate | Direct specialization of Wigderson/Croot--Sisask; no novelty claim |

This project does not claim to correct Roe--Turturean's presentation theorem.
It does not claim a new A183068 supercongruence. Literature novelty is not
asserted without a separate priority review.

## Verification

The exact checker currently verifies:

- 30 compatible exponent classes through precision $2^{32}$;
- 5,024 finite-level Dehn-twist identities; and
- 349,578 finite-level affine and commutator-filtration identities.

The sampler checker additionally verifies every binary parametrization and
four-element lift fiber through modulus $2^8$, the Walsh eigenvalue identity,
and the exact chi-square formula.

The Cayley-walk checker constructs the full transition matrices through
modulus $2^5$ and verifies symmetry, stochasticity, irreducibility,
nonnegative spectrum, the cyclotomic unit eigenfunction, and both gap bounds.

The grammar checker verifies more than 2.4 million exact rewrite identities,
all unique normal forms through modulus $2^7$, and 10,912 exact
twist-convolution identities.

The conjugacy checker verifies every translation shell and centralizer through
modulus \(2^8\). It also checks the exact adjacent depth-moment identity

$$
D_{m+1,j}-2D_{m,j}=2^{jm}
$$

through \(m=16\) and \(j=8\).

A second exact checker independently reproduces the manuscript's Proposition
C.10 norm calculations and the Appendix D counts for $S_3$ and $S_4$. See the
[current-PDF audit](related-results/GQ2CurrentPdfAudit.md).

Run:

```text
python verification/related/verify_gq2_orientation_lifts.py
python verification/related/verify_dyadic_dehn_twist_sampler.py
python verification/related/verify_dyadic_dehn_twist_cayley.py
python verification/related/verify_dyadic_twist_grammar.py
python verification/related/verify_dyadic_dehn_twist_conjugacy.py
```

## Next theorem target

Proposition 3.9 gives a surjection

$$
\mathrm{Out}(D_0)\twoheadrightarrow
\mathbb Z_2\rtimes\mathbb Z_2^\times.
$$

The translation subgroup already has the explicit Dehn-twist section above.
The next genuine question is whether the entire affine quotient has a
continuous group-theoretic section. If $K$ is the kernel, choices of
unit-scaling lifts produce a generally nonabelian, $K$-valued factor set.
Killing that factor set, compatibly with the translation section, is the
actual splitting problem.

The natural linear proxy is not automatically zero:

$$
H^2_{\mathrm{cont}}(\mathbb Z_2^\times,\mathbb Z_2(1))
\cong\mathbb Z/2.
$$

Here $\mathbb Z_2(1)$ means the additive module on which a unit acts by
multiplication. This calculation does not yet identify the actual
kernel-valued extension class; a compatible abelian pushout from $K$ would
still have to be constructed.

No answer is claimed yet. A splitting theorem or a nonzero obstruction would
be a materially stronger result than the present structural extraction.
