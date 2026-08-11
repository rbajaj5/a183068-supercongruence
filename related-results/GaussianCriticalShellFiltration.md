# The affine-depth filtration of the ramified Gaussian product

## Status

This note proves a sharper reciprocal-square estimate for the mixed Gaussian
block and uses it to resolve several successive layers of the weighted
critical shell. It is a local consequence of the four-coset recurrence in
the [ramified Gaussian theorem](GaussianLucasRamifiedTwoTheorem.md), not a
claim about the still-open split-prime normalization problem. Literature
priority has not been established.

## 1. Setup

Put

\[
\mathcal O=\mathbb Z_2[i],
\qquad
\varpi=1+i,
\]

and, for \(r\ge2\), let

\[
U_r=
\{a+bi:1\le a,b\le2^r,\ a,b\text{ not both even}\}.
\]

Write

\[
S_{r,k}=\sum_{\xi\in U_r}\xi^{-k},
\qquad
c_{r,k}=\frac{(-1)^{k+1}}{k}2^{rk}S_{r,k}.
\tag{1}
\]

The known four-coset argument gives

\[
v_\varpi(S_{r,1})=4r-3,
\qquad
v_\varpi(S_{r,k})\ge4r-2k\quad(k\ge2).
\tag{2}
\]

The general estimate in (2) is not optimal at \(k=2\). Recovering the two
missing powers is what makes the deeper weighted filtration visible.

## 2. The reciprocal-square improvement

### Theorem 1

For every \(r\ge2\),

\[
v_\varpi(S_{r,2})\ge4r-2.
\tag{3}
\]

### Proof

At \(r=2\), the exact mixed-block table gives
\(v_\varpi(S_{2,2})=6\), so (3) holds with equality.

For the induction, use

\[
T=\{0,1,i,1+i\},
\qquad
M_j=\sum_{t\in T}t^j.
\]

Besides \(v_\varpi(M_1)=3\), one has

\[
M_2=2i,
\qquad
v_\varpi(M_2)=2.
\tag{4}
\]

The four-coset recurrence at \(k=2\) is

\[
S_{r+1,2}
=
\sum_{j\ge0}
(-1)^j(j+1)2^{rj}M_jS_{r,2+j}.
\tag{5}
\]

Assume (3) at level \(r\). The \(j=0\) term has valuation at least

\[
4+(4r-2)=4r+2,
\]

which is the target at level \(r+1\). For \(j=1\), the factor \(j+1=2\)
contributes two powers of \(\varpi\), and (2) gives the lower bound

\[
2+2r+3+(4r-6)=6r-1\ge4r+2.
\tag{6}
\]

For \(j=2\), equation (4) and (2) give

\[
4r+2+(4r-8)=8r-6\ge4r+2.
\tag{7}
\]

Finally, every \(j\ge3\) term has valuation at least

\[
2rj+4r-2(2+j)
=4r-4+2j(r-1)
\ge4r+2.
\tag{8}
\]

The lower bound tends to infinity with \(j\), so the tail converges and the
whole sum satisfies (3) at level \(r+1\). This proves the theorem. \(\square\)

### Corollary 2 (uniform higher-moment gap)

For every \(r\ge2\) and \(k\ge2\),

\[
v_\varpi(c_{r,k})\ge8r-4.
\tag{9}
\]

For \(k=2\), this follows from (3) and
\(v_\varpi(2^{2r}/2)=4r-2\). For \(k\ge3\), equations (1)--(2) give

\[
v_\varpi(c_{r,k})
\ge
4r+2k(r-1)-2v_2(k).
\tag{10}
\]

After subtracting \(8r-4\), the right side becomes

\[
2\bigl((k-2)(r-1)-v_2(k)\bigr)\ge0,
\]

because \(k-2\ge v_2(k)\) for \(k\ge3\).

## 3. The exact affine defect

For \(\xi\in U_r\), put \(e_\xi=v_\varpi(\xi)\in\{0,1\}\), and consider
the one-step enlargement of the sharp weighted polydisc:

\[
a_\xi=1+\varpi^{4r-3+e_\xi}u_\xi,
\qquad
u_\xi\in\mathcal O.
\tag{11}
\]

Define its normalized affine defect by

\[
\Lambda_r(\mathbf u)
=
\frac{c_{r,1}}{\varpi^{6r-3}}
+(-i)^r
\sum_{\xi\in U_r}
u_\xi\frac{\varpi^{e_\xi}}{\xi}.
\tag{12}
\]

### Theorem 3

Let

\[
F_{r,\mathbf a}(Z)
=
\prod_{\xi\in U_r}
\left(1+a_\xi\frac{2^rZ}{\xi}\right),
\qquad
\log F_{r,\mathbf a}(Z)
=
\sum_{k\ge1}b_k(\mathbf a)Z^k.
\]

Then

\[
b_1(\mathbf a)
=
\varpi^{6r-3}\Lambda_r(\mathbf u)
\tag{13}
\]

exactly, and

\[
v_\varpi(b_k(\mathbf a))\ge8r-4
\qquad(k\ge2).
\tag{14}
\]

### Proof

Equation (13) follows by substituting (11) into the first coefficient and
using \(2^r/\varpi^{2r}=(-i)^r\).

For (14), first note the elementary local estimate

\[
v_\varpi((1+\delta)^k-1)
\ge
v_\varpi(\delta)+2v_2(k)
\qquad(v_\varpi(\delta)\ge5).
\tag{15}
\]

Indeed, the \(k\delta\) term has the displayed valuation. For \(j\ge2\),
the identity

\[
\binom{k}{j}=\frac{k}{j}\binom{k-1}{j-1}
\]

shows that the \(j\)-th binomial term lies at least
\((j-1)v_\varpi(\delta)-2v_2(j)>0\) levels deeper.

Apply (15) to
\(\delta=a_\xi-1\), whose valuation is at least
\(4r-3+e_\xi\). The \(\xi\)-summand of
\(b_k(\mathbf a)-c_{r,k}\) therefore has valuation at least

\[
2rk+4r-3-(k-1)e_\xi.
\tag{16}
\]

For \(k\ge2\) and \(e_\xi\in\{0,1\}\), this is at least \(8r-4\);
the smallest case is \(k=2\), \(e_\xi=1\). Corollary 2 and the
ultrametric inequality now prove (14). \(\square\)

## 4. Certified isometry layers

### Theorem 4

Suppose \(\Lambda_r(\mathbf u)\ne0\), and put

\[
t=v_\varpi(\Lambda_r(\mathbf u)).
\]

If

\[
0\le t\le2r-2,
\tag{17}
\]

then for all distinct \(Z,W\in\mathcal O\),

\[
v_\varpi\bigl(
F_{r,\mathbf a}(Z)-F_{r,\mathbf a}(W)
\bigr)
=
6r-3+t+v_\varpi(Z-W).
\tag{18}
\]

Consequently

\[
Z\longmapsto
\frac{F_{r,\mathbf a}(Z)-1}{b_1(\mathbf a)}
\tag{19}
\]

is a bijective analytic isometry of \(\mathcal O\).

### Proof

By (13), the first coefficient has valuation \(6r-3+t\). Condition (17)
and (14) give

\[
v_\varpi(b_k(\mathbf a))
\ge8r-4
\ge6r-2+t
=v_\varpi(b_1(\mathbf a))+1
\qquad(k\ge2).
\]

Thus the first logarithmic moment is dominant. The standard
difference-logarithm argument proves (18), and the contraction lifting
argument proves bijectivity of (19). \(\square\)

Reduction of (12) modulo \(\varpi\) recovers the critical-shell parity law:

\[
\Lambda_r(\mathbf u)
\equiv
1+\sum_{\xi\in U_r}\overline{u}_\xi
\pmod{\varpi}.
\]

The parity-zero class is the depth-\(0\) layer. Theorem 4 shows that the
parity-one side is not merely a failure set: its next \(2r-2\) affine-depth
strata are also exact isometry chambers, with successively smaller
similarity ratios. No assertion is made here once
\(v_\varpi(\Lambda_r)\ge2r-1\); at that boundary, higher logarithmic moments
can occur at the same certified valuation as the first.

## 5. Exact checks

The checker
[`verify_gaussian_critical_shell.py`](../verification/related/verify_gaussian_critical_shell.py)
verifies the reciprocal-square improvement and the \(8r-4\) tail through
\(r=5\), constructs critical-shell witnesses of every certified depth for
\(r=2,3\), checks the stronger tail throughout the uniform and anisotropic
neighborhood samples, and verifies the predicted similarity law on exact
pairs in \(\mathbb Q(i)\).
