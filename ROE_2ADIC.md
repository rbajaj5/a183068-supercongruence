# Public 2-adic Roe-inspired follow-on

This is the public landing page for the $2$-adic project prompted by David
Roe and David Turturean's
[*A Presentation of the Absolute Galois Group of $\mathbb Q_2$*][RT].

The detailed proofs and checker are:

- [orientation lifts, Dehn twists, and affine symmetry](related-results/GQ2OrientationLifts.md);
- [`verify_gq2_orientation_lifts.py`](verification/related/verify_gq2_orientation_lifts.py).

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
$\operatorname{Out}(D_0)$. These are the pro-$2$ HNN Dehn twists. Their
depth on the abelianization is exactly $v_2(b)$.

### 3. The affine shadow

The full orientation-preserving abelian shadow is

$$
\operatorname{Aut}(B_{\mathrm{ab}},\chi)
\cong
\mathbb Z_2\rtimes\mathbb Z_2^\times,
$$

with matrices

$$
M(u,b)=
\begin{pmatrix}u&b\\0&1\end{pmatrix}.
$$

Roe--Turturean Proposition 3.9 makes the natural map from
$\operatorname{Out}(D_0)$ onto this affine group surjective. The twists
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

This project does not claim to correct Roe--Turturean's presentation theorem.
It does not claim a new A183068 supercongruence. Literature novelty is not
asserted without a separate priority review.

## Verification

The exact checker currently verifies:

- 30 compatible exponent classes through precision $2^{32}$;
- 5,024 finite-level Dehn-twist identities; and
- 349,578 finite-level affine and commutator-filtration identities.

A second exact checker independently reproduces the manuscript's Proposition
C.10 norm calculations and the Appendix D counts for $S_3$ and $S_4$. See the
[current-PDF audit](related-results/GQ2CurrentPdfAudit.md).

Run:

```text
python verification/related/verify_gq2_orientation_lifts.py
```

## Next theorem target

Proposition 3.9 gives a surjection

$$
\operatorname{Out}(D_0)\twoheadrightarrow
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
