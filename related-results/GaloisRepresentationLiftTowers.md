# Compatible Galois lift towers and their cohomological defects

## Status

This note extracts the elementary lift-tower skeleton behind several
approaches to Galois representations by $p$-adic approximation. It was
prompted by the work of Chandrashekhar Khare, especially his approximation
method, the torsion-lifting work with Ravi Ramakrishna, and the relative
deformation theory developed with Najmuddin Fakhruddin and Stefan Patrikis.

The inverse-limit and square-zero obstruction theorems below are standard
deformation-theoretic infrastructure. No novelty claim is made. The point is
to state them in the same lift/defect language used elsewhere in this
repository and to mark the boundary between a scalar supercongruence and a
genuine Galois-representation lift.

## 1. Compatible finite lifts

Let $\mathcal O$ be a complete separated discrete valuation ring with
uniformizer $\varpi$, and put

$$
\mathcal O_n=\mathcal O/\varpi^n.
$$

Let $\Gamma$ be a profinite group.

### Theorem 1 - compatible lifts are a $p$-adic representation

Reduction induces a bijection

$$
\boxed{
\mathrm{Hom}_{\mathrm{cont}}
\bigl(\Gamma,\mathrm{GL}_d(\mathcal O)\bigr)
\cong
\varprojlim_n
\mathrm{Hom}_{\mathrm{cont}}
\bigl(\Gamma,\mathrm{GL}_d(\mathcal O_n)\bigr).
}
\tag{1}
$$

Thus a compatible family

$$
\rho_n:\Gamma\longrightarrow\mathrm{GL}_d(\mathcal O_n)
$$

has a unique continuous limit

$$
\rho=\varprojlim_n\rho_n:
\Gamma\longrightarrow\mathrm{GL}_d(\mathcal O).
$$

#### Proof

Completeness and separatedness give

$$
\mathcal O\cong\varprojlim_n\mathcal O_n
$$

as topological rings. Taking matrices commutes with this inverse limit. A
compatible matrix lies in $\mathrm{GL}_d(\mathcal O)$ precisely when its
reduction modulo $\varpi$ is invertible, so

$$
\mathrm{GL}_d(\mathcal O)
\cong
\varprojlim_n\mathrm{GL}_d(\mathcal O_n)
$$

as topological groups.

Taking the inverse limit of the identities
$\rho_n(gh)=\rho_n(g)\rho_n(h)$ gives the homomorphism identity for $\rho$.
Continuity follows because every finite-level reduction is continuous and
the inverse-limit topology is initial with respect to those reductions.
Uniqueness follows from separatedness. $\square$

### Corollary 2 - finite lift-tree compactness

Suppose $\mathcal L_n$ is a nonempty finite set of continuous
$\mathcal O_n$-valued representations and reduction maps

$$
\mathcal L_{n+1}\longrightarrow\mathcal L_n.
$$

Then there is a compatible sequence

$$
\rho_n\in\mathcal L_n
$$

and hence an $\mathcal O$-valued representation.

#### Proof

Make a rooted tree whose level-$n$ vertices are $\mathcal L_n$ and whose
edges are reductions. It is infinite and finitely branching. Konig's lemma
gives an infinite compatible path, and Theorem 1 gives its limit. $\square$

Surjectivity of every reduction map is sufficient but not necessary. What is
essential is that the conditions defining $\mathcal L_n$ are stable under
reduction, so that they really form one inverse system.

## 2. The one-step defect

Let

$$
A'\longrightarrow A
$$

be a surjection of finite local Artinian rings with square-zero kernel $I$.
Let

$$
\bar\rho:\Gamma\longrightarrow\mathrm{GL}_d(A)
$$

be a continuous representation. The additive group
$M_d(I)$ becomes a $\Gamma$-module by conjugation through $\bar\rho$; denote
it by $\mathrm{ad}(\bar\rho)\otimes I$.

Choose arbitrary set-theoretic matrix lifts

$$
\widetilde\rho(g)\in\mathrm{GL}_d(A'),
\qquad
\widetilde\rho(1)=1.
$$

Define $C(g,h)\in M_d(I)$ by

$$
1+C(g,h)
=
\widetilde\rho(g)\widetilde\rho(h)
\widetilde\rho(gh)^{-1}.
\tag{2}
$$

### Theorem 3 - obstruction and correction spaces

The function $C$ is a normalized $2$-cocycle:

$$
C(g,h)+C(gh,k)
=
g\mathbin{\cdot}C(h,k)+C(g,hk).
\tag{3}
$$

Its class

$$
[C]\in
H^2\bigl(\Gamma,\mathrm{ad}(\bar\rho)\otimes I\bigr)
\tag{4}
$$

is independent of the chosen set-theoretic lifts. It vanishes if and only if
$\bar\rho$ lifts to a representation over $A'$.

When the obstruction vanishes:

- the set of homomorphic lifts is an affine space under the $1$-cocycles
  $Z^1(\Gamma,\mathrm{ad}(\bar\rho)\otimes I)$; and
- strict-equivalence classes of lifts form a torsor under
  $H^1(\Gamma,\mathrm{ad}(\bar\rho)\otimes I)$.

#### Proof

Because $I^2=0$, multiplication in $1+M_d(I)$ is addition:

$$
(1+X)(1+Y)=1+X+Y.
$$

Compute

$$
\bigl(\widetilde\rho(g)\widetilde\rho(h)\bigr)
\widetilde\rho(k)
$$

and

$$
\widetilde\rho(g)
\bigl(\widetilde\rho(h)\widetilde\rho(k)\bigr)
$$

using (2). Associativity gives exactly (3).

If the lifts are changed to

$$
\widetilde\rho'(g)
=(1+B(g))\widetilde\rho(g),
$$

then another direct multiplication gives

$$
C'(g,h)
=
C(g,h)+B(g)+g\mathbin{\cdot}B(h)-B(gh).
\tag{5}
$$

Thus the defect changes by a $2$-coboundary. It can be made zero precisely
when its cohomology class vanishes, and zero defect is exactly the
homomorphism condition. Formula (5) also identifies differences of
homomorphic lifts with $1$-cocycles. Conjugation by $1+X$ changes that
$1$-cocycle by a $1$-coboundary, giving the final assertion. $\square$

## 3. Normalized defects in a valuation tower

Take

$$
A'=\mathcal O/\varpi^{n+1},
\qquad
A=\mathcal O/\varpi^n.
$$

The kernel

$$
I=\varpi^n\mathcal O/\varpi^{n+1}\mathcal O
$$

is square-zero and is naturally a vector space over the residue field
$k=\mathcal O/\varpi$. Therefore an arbitrary lift of $\rho_n$ has a
normalized multiplicative defect

$$
\frac{
\widetilde\rho(g)\widetilde\rho(h)
\widetilde\rho(gh)^{-1}-1
}{\varpi^n}
\pmod\varpi,
\tag{6}
$$

and Theorem 3 says that (6) is a canonical $H^2$ obstruction up to
coboundary.

This is the general matrix-valued version of a normalized scalar defect:

$$
\text{failure at level }n+1
\quad\longrightarrow\quad
\text{residue-field obstruction}.
$$

Corrections live one degree lower, in $H^1$. The two cohomological degrees
are not optional terminology; they record the associativity condition on the
defect and the ambiguity in correcting it.

## 4. Relation to Khare's lifting program

Theorem 1 is only the compact final step. The difficult arithmetic problem is
to make the finite lift sets nonempty while imposing local conditions,
ramification control, geometricity, and automorphy.

- Khare's $p$-adic approximation method recovers modularity results from
  compatible finite approximations.
- Khare--Ramakrishna lift ordinary weight-two torsion representations over
  ramified discrete valuation rings under arithmetic hypotheses.
- Fakhruddin--Khare--Patrikis construct successive
  $\mathcal O/\varpi^n$-valued lifts using relative deformation and Selmer
  methods, then explicitly take their inverse limit.

The general lifting problem is not automatically soluble. Work of
Khare--Larsen identified positive cases and cohomological mechanisms, while
Merkurjev--Scavia subsequently produced non-liftable representations and
classified the dimensions and coefficient fields for which universal
lifting to length-two Witt vectors holds.

Accordingly, the existence of compatible scalar residues should never be
reported as a Galois-representation lift without constructing the
representation and checking its $H^2$ obstruction.

## 5. The supercongruence shadow

If a compatible representation tower exists, then every integral polynomial
matrix invariant is automatically compatible. For example,

$$
\mathrm{tr}\,\rho_{n+1}(g)
\equiv
\mathrm{tr}\,\rho_n(g)
\pmod{\varpi^n},
\tag{7}
$$

and the same holds for all characteristic-polynomial coefficients.

This is a congruence shadow of a lift tower, not a supercongruence theorem:
it supplies only the precision built into the coefficient reduction. A
stronger valuation requires additional cancellation, extra geometry, or a
more rigid Frobenius structure.

The genuine research target for the supercongruence program is therefore:

> Identify a sequence or Gaussian residue as a trace, period, or unit-root
> coordinate of a compatible Frobenius/Galois deformation, and then explain
> its surplus valuation through the deformation's local structure.

No such realization is claimed here for A183068 or for the Gaussian
prime-power products.

## 6. Comparison with the Roe tower

The Roe--Turturean orientation congruences form a scalar inverse system, and
the compatible exponent is recovered by completeness of $\mathbb Z_2$.
Their Appendix C proof also uses finite-level defects and corrections.

The analogy with Theorems 1 and 3 is therefore exact at the level of proof
architecture:

$$
\text{finite lift}
\longrightarrow
\text{normalized defect}
\longrightarrow
\text{correction}
\longrightarrow
\text{inverse limit}.
$$

But the objects differ. An orientation exponent is not itself a matrix-valued
Galois representation, and the scalar obstruction found in that tower is not
automatically the deformation class (4).

## 7. Verification

Run:

```text
python verification/related/verify_galois_lift_defects.py
```

The checker verifies compatible representations of a cyclic group through
six $3$-adic levels and checks the cocycle identity, change-of-lift formula,
and correction to an exact homomorphism for thousands of matrix-valued
one-step defects.

## References

- C. Khare,
  [*Modularity of $p$-adic Galois representations via $p$-adic
  approximations*][K02].
- C. Khare and R. Ramakrishna,
  [*Lifting torsion Galois representations*][KR].
- N. Fakhruddin, C. Khare, and S. Patrikis,
  [*Relative deformation theory, relative Selmer groups, and lifting
  irreducible Galois representations*][FKP].
- C. Khare and M. Larsen,
  [*Liftable groups, negligible cohomology and Heisenberg
  representations*][KL].
- A. Merkurjev and F. Scavia,
  [*The lifting problem for Galois representations*][MS].

[K02]: https://arxiv.org/abs/math/0210296
[KR]: https://arxiv.org/abs/1409.1834
[FKP]: https://arxiv.org/abs/1904.02374
[KL]: https://arxiv.org/abs/2009.01301
[MS]: https://arxiv.org/abs/2501.18906
