# Gaussian angular X-ray spectrum and the Kakeya boundary

**Status:** complete elementary spectral calculation and planar incidence
corollary; no novelty claim.  The higher-dimensional structured-direction
problem isolated in Section 6 is open in this project.

## 1. Why spectral theory is the right language

The useful Bourbaki-style move is not to rename the Kakeya problem.  It is to
place all line-averaging operators in one commutative operator algebra, find
its spectral idempotents, and state exactly where the nonlinear Kakeya choice
escapes that algebra.

This calculation does that in the Gaussian plane.  It produces three exact
spectral packets:

1. the constant character;
2. frequencies of square Gaussian norm; and
3. frequencies of nonsquare Gaussian norm.

The split is the harmonic-analytic form of the radial/angular distinction
used elsewhere in this repository.

## 2. Gaussian directions

Let \(p\equiv3\pmod4\) be an odd prime and put

```math
V=\mathbb F_p^2,\qquad
Q(x,y)=x^2+y^2.
```

The form \(Q\) is anisotropic.  Identifying \(V\) with
\(\mathbb F_{p^2}=\mathbb F_p[i]\), it is the norm.

Let

```math
U=\{u\in V:Q(u)=1\},
\qquad
\mathcal D=U/\{\pm1\}.
\tag{1}
```

The norm map
\(\mathbb F_{p^2}^{\times}\to\mathbb F_p^{\times}\) is surjective with
kernel of order \(p+1\).  Hence

```math
|U|=p+1,\qquad |\mathcal D|=\frac{p+1}{2}.
\tag{2}
```

The set \(\mathcal D\) consists exactly of the projective directions
\([v]\in\mathbb P^1(\mathbb F_p)\) for which \(Q(v)\) is a square.  Indeed,
\([v]\) contains a unit-norm representative precisely when
\(t^2Q(v)=1\) is soluble.

Thus \(\mathcal D\) is a genuinely angular half of the directions in the
finite Gaussian plane.

## 3. The commuting X-ray projections

For \(d=[u]\in\mathcal D\), define the normalized line average

```math
(P_df)(x)=\frac1p\sum_{t\in\mathbb F_p}f(x+tu).
\tag{3}
```

The definition is independent of the representative \(u\).  Each \(P_d\)
is a self-adjoint idempotent on \(\ell^2(V)\), and the family commutes because
every \(P_d\) is convolution by the uniform measure on a subgroup.

Fix a nontrivial additive character \(\psi\) and write

```math
e_\xi(x)=\psi(\xi\mathbin{\cdot}x).
```

Character orthogonality gives

```math
P_de_\xi=
\begin{cases}
e_\xi,&\xi\mathbin{\cdot}u=0,\\
0,&\xi\mathbin{\cdot}u\ne0.
\end{cases}
\tag{4}
```

Define the angular X-ray normal operator

```math
\mathcal A=\sum_{d\in\mathcal D}P_d.
\tag{5}
```

### Theorem 1 (three-packet spectrum)

The spectrum of \(\mathcal A\) is

```math
\frac{p+1}{2},\quad1,\quad0.
\tag{6}
```

More precisely,

```math
\mathcal A e_\xi=
\begin{cases}
\dfrac{p+1}{2}e_\xi,&\xi=0,\\[2mm]
e_\xi,&\xi\ne0\text{ and }Q(\xi)\text{ is a square},\\
0,&Q(\xi)\text{ is a nonsquare}.
\end{cases}
\tag{7}
```

The multiplicities are

```math
1,\qquad\frac{p^2-1}{2},\qquad\frac{p^2-1}{2}.
\tag{8}
```

### Proof

For \(\xi\ne0\), there is a unique projective direction perpendicular to
\(\xi\), represented by

```math
J\xi=(-\xi_2,\xi_1).
```

Since \(Q(J\xi)=Q(\xi)\), that direction lies in \(\mathcal D\) exactly
when \(Q(\xi)\) is a square.  Equation (4) proves (7).

Every nonzero norm value has \(p+1\) preimages under
\(Q:V\setminus\{0\}\to\mathbb F_p^\times\).  Half of the nonzero elements
of \(\mathbb F_p\) are squares and half are nonsquares, proving (8).
\(\square\)

Let \(E_0,E_+,E_-\) be the orthogonal projections onto the three spaces in
(7).  The entire result can be compressed into the functional-calculus
identity

```math
\mathcal A=\frac{p+1}{2}E_0+E_+,
\qquad
I=E_0+E_++E_-.
\tag{9}
```

This is the precise spectral-theory formulation: the geometry has become a
three-idempotent commutative algebra.

## 4. Selecting one line in every Gaussian direction

Choose an arbitrary affine line \(L_d\) in each direction
\(d\in\mathcal D\), and put

```math
w(x)=\sum_{d\in\mathcal D}1_{L_d}(x),
\qquad
K=\bigcup_{d\in\mathcal D}L_d.
\tag{10}
```

The centered line indicators

```math
g_d=1_{L_d}-\frac1p
\tag{11}
```

are pairwise orthogonal:

```math
\langle g_d,g_e\rangle=0\quad(d\ne e),
\qquad
\|g_d\|_2^2=p-1.
\tag{12}
```

Indeed, two nonparallel affine lines in a plane meet in exactly one point.
Equivalently, their nonzero Fourier supports are the disjoint lines
\(d^\perp\setminus\{0\}\).

Consequently,

```math
\sum_{x\in V}w(x)^2
=|\mathcal D|^2+|\mathcal D|(p-1).
\tag{13}
```

Cauchy--Schwarz now gives the restricted-direction Kakeya bound

```math
|K|
\ge
\frac{(|\mathcal D|p)^2}
{|\mathcal D|^2+|\mathcal D|(p-1)}
=
\frac{p^2(p+1)}{3p-1}.
\tag{14}
```

Thus any set containing one affine line in every Gaussian unit-norm
direction occupies asymptotically at least one third of the plane.

Equation (14) is a second-moment consequence, not a new solution of a Kakeya
problem.  Its value here is that the spectral packet and the incidence
calculation are literally the same orthogonality statement.

## 5. Where the hard Kakeya problem begins

In the plane, each nonzero frequency is perpendicular to only one projective
direction.  Translating the chosen lines changes Fourier phases but does not
create interference between distinct directions, which is why (13) is exact.

In dimension at least three, many directions lie in the hyperplane
\(\xi^\perp\).  Their translation phases then interact inside the same
spectral fiber.  Moreover, the Kakeya maximal operator takes a supremum over
translations and is nonlinear.  Neither operation belongs to the
commutative convolution algebra diagonalized above.

This gives a clean boundary:

```text
commuting line averages  -> exact spectrum
chosen translations      -> phase interaction
maximal selection         -> nonlinear Kakeya problem
```

Spectral theory organizes the easy part and identifies the missing datum; it
does not erase the geometric overlap problem.

## 6. The next structured-direction problem

The existing hyperdeterminant work studies a scalar Fourier pushforward

```math
\sum_T\psi(a\Delta(T)).
```

A genuine restriction/Kakeya extension must instead evaluate the ambient
normal-operator multiplier

```math
m(\xi)
=
\#\{d\in\mathcal D_{\mathrm{tensor}}:
\langle\xi,d\rangle=0\},
\tag{15}
```

where \(\mathcal D_{\mathrm{tensor}}\) is a projective orbit of structured
tensor directions.  The Bourbaki-style program is:

1. regard the orbit averages as an algebra of commuting convolution
   operators;
2. decompose the dual tensor space into group orbits;
3. compute (15) on every dual orbit; and
4. only then attack the translation phases or maximal operator.

For rank-one matrix directions, (15) already reduces to the rank of the dual
matrix.  For \(2\times2\times2\) tensors, the dual orbit stratification is
substantially richer.  Computing that orbit spectrum is the next honest
target connecting this repository's Fourier packets to Kakeya.

## 7. Verification and literature boundary

The checker verifies (1)--(8), pairwise centered-line orthogonality, the exact
second moment (13), and the support bound (14) for several translation
choices at every inert prime through \(43\).

Run:

```text
python verification/related/verify_gaussian_kakeya_spectrum.py
```

The operator-algebra viewpoint is classical, and no novelty is claimed for
Theorem 1 or (14).  The note is a rigorous bridge and a problem statement.
Relevant current sources include:

- J. M. Fraser,
  [*Fourier analytic properties of Kakeya sets in finite
  fields*](https://arxiv.org/abs/2505.09464), for the sharp
  \(q^{-1}\) Fourier decay of a suitable probability measure supported on a
  finite-field Kakeya set;
- M. Lewko,
  [*Finite field restriction estimates based on Kakeya maximal operator
  estimates*](https://arxiv.org/abs/1401.8011), for the formal
  restriction--Kakeya bridge; and
- T. Pham, A. Pinamonti, D. T. Tran, and B. Xue,
  [*Horizontal Kakeya maximal operators in finite Heisenberg
  groups*](https://arxiv.org/abs/2603.02111), for a recent exact-exponent
  Fourier-analytic treatment of a structured Kakeya operator.
