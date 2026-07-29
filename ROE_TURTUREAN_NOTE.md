# A finite-target follow-on to the $G_{\mathbb Q_2}$ presentation

## Short note for David Roe and David Turturean

Your paper,
[*A Presentation of the Absolute Galois Group of
Q₂*](https://roed314.github.io/gq2/paper/paper.html),
asks in Section 11 for explicit formulas for

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},G)\right|
$$

for finite groups $G$.

We worked out a closed formula for every **finite abelian $2$-group**
target. This is only a special case of your question, but it is complete and
provides a simple test case for the broader Fourier-inversion program.

## Result

Write

$$
H\cong (C_2)^e\oplus\bigoplus_{j=1}^{h}C_{2^{\lambda_j}},\qquad \lambda_j\ge2.
$$

Put

$$
d=e+h,\qquad q=|2H|,
$$

and define

$$
P_0=1,\qquad P_1=3,\qquad P_2=6,\qquad P_j=0\quad(j>2).
$$

Then

$$
\boxed{\left|\mathrm{Sur}(G_{\mathbb Q_2},H)\right|=q^2\,2^h\left(P_d+(2^e-1)4P_{d-1}\right)}
$$

Consequently the count vanishes when
$\dim_{\mathbb F_2}(H/2H)>3$, as expected from the three-generator
maximal pro-2 quotient.

For cyclic targets this becomes

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},C_{2^m})\right|=\begin{cases}7,&m=1,\\3\cdot2^{2m-1},&m\ge2.\end{cases}
$$

After division by
$\left|\mathrm{Aut}(C_{2^m})\right|$, the number of cyclic
$2^m$-extensions of $\mathbb Q_2$ is therefore

$$
\begin{cases}7,&m=1,\\3\cdot2^m,&m\ge2.\end{cases}
$$

The first value recovers the seven quadratic extensions of
$\mathbb Q_2$.

## Why the formula is short

Your marked Demushkin presentation gives

$$
D_0=\left\langle A,S,Y\ \middle|\ A^2S^4[S,Y]=1\right\rangle_{\mathrm{pro}\text{-}2}.
$$

In the abelianization, writing

$$
t=\bar A+2\bar S
$$

gives

$$
D_0^{\mathrm{ab}}\cong C_2\oplus\mathbb Z_2^2.
$$

A homomorphism to $H$ is therefore a triple

$$
(z,x,y)\in H[2]\times H\times H.
$$

It is surjective precisely when the images of $z,x,y$ span the Frattini
quotient $H/2H$. The map

$$
H[2]\longrightarrow H/2H
$$

has image equal to the $e$-dimensional subspace contributed by the direct
$C_2$-factors and kernel of size $2^h$. Counting spanning triples in
that finite vector space and then multiplying by the uniform lift
multiplicity $q^2 2^h$ gives the displayed formula.

The [complete proof](related-results/GQ2FiniteAbelianCounts.md) includes the
vector-space count and the cyclic and elementary-abelian specializations.

## Verification and status

The accompanying
[`verify_gq2_finite_abelian_counts.py`](verification/related/verify_gq2_finite_abelian_counts.py)
exhaustively enumerates every candidate triple for all 66 abelian
invariant-factor types of order at most $2^8$. It also checks the cyclic
formula through exponent $2^{16}$ and the elementary-abelian generator-rank
boundary through rank $8$.

This calculation is an elementary consequence of your abelianization.
We are **not** claiming:

- a solution of the general finite-target counting problem;
- a correction to your presentation theorem;
- a new classification of local extensions; or
- literature priority for the abelian formula.

Its value is as a compact, fully explicit first case of Section 11's
counting direction.

## Nonabelian follow-on now completed

The first nonabelian boundary is now also explicit. If $D_{2^m}$ denotes
the dihedral group of order $2^m$, then

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},D_{2^m})\right|=\begin{cases}144,&m=3,\\2^{2m+1},&m\ge4.\end{cases}
$$

Thus there are $18$ $D_8$-extensions of $\mathbb Q_2$ and $16$
$D_{2^m}$-extensions for every $m\ge4$. The
[complete dihedral proof](related-results/GQ2DihedralCounts.md) reduces the
source relator to seven linear congruences indexed by the nonzero reflection
patterns and checks every triple through $D_{128}$.

This is the first place where the commutator in the source relator changes
the count; it is invisible in the abelian formula.

## Next boundary

The same presentation suggests treating quaternion and extraspecial
$2$-groups by:

1. fixing the induced map on the abelian or Frattini quotient;
2. evaluating the relator on the central commutator layer; and
3. using the resulting linear or quadratic obstruction to count lifts.

Quaternion groups are the immediate next family. Extraspecial groups should
then be the smallest targets on which the full quadratic Gauss-sign layer,
rather than only a linearized commutator correction, becomes visible.

## Authors of this follow-on

Ravi Andrew Bajaj and Alexander Burns.

