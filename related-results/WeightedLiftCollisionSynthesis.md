# An all-degree collision theorem for weighted-lift Keller maps

## Status

This note extracts the common theorem behind the finite-field collision
counts for the degree-three, degree-four, and degree-five Jacobian
counterexamples.

For every normalized member of Gallagher's weighted-lift family, it proves
that ordered collisions are controlled by one explicit second
divided-difference curve.  A degree-\(n\) inverse equation produces a plane
curve of degree \(n-2\), hence arithmetic genus

\[
\frac{(n-3)(n-4)}2.
\]

The complete collision zeta function splits into a Tate factor, the
Frobenius factor of that curve, and finite permutation factors. Removing
the latter two packets leaves a universal adjacent-extension valuation of
\(2r-2\).

The weighted-lift construction is due to Gallagher.  The all-degree
collision formula and zeta decomposition below are new to this repository.
They have exact cross-degree checks for generic fiber degrees \(3\) through
\(7\). Literature priority remains provisional.

**Source-status label:** this is a structural follow-on theorem, not a
claimed solution of a named open conjecture. The source explicitly leaves
several classification and boundary questions open, but does not state
Theorems 1 or 2 as conjectures.

## 1. Normalized weighted lifts

Let \(K\) be a field of characteristic different from \(2\), and let
\(\rho(w)\in K[w]\) satisfy

\[
\rho(0)=0,\qquad
\rho(1)=-1,\qquad
\int_0^1\rho(w)\,dw=0.
\tag{1}
\]

Define \(\theta(0)=0\) by

\[
\theta'(w)=w\rho'(w).
\tag{2}
\]

Put

\[
\kappa=\rho'(1),\qquad
a=-\frac{1+\kappa}{2+\kappa},
\tag{3}
\]

and assume \(\kappa\ne-2\).  With

\[
u=1+xy,\qquad
\gamma=1+a\,xy+x^2z,\qquad
w=u\gamma,
\tag{4}
\]

Gallagher's normalized lift is

\[
F_\rho(x,y,z)=
\left(
\frac{u+\theta(w)/\gamma^2}{x^2},
\frac{1+\rho(w)/\gamma}{x},
x\gamma
\right).
\tag{5}
\]

The conditions in (1) make the apparent quotients cancel. Thus \(F_\rho\)
is polynomial and

\[
\det JF_\rho=1.
\tag{6}
\]

Finally put

\[
\Phi(w)=w\rho(w)-\theta(w)=\int_0^w\rho(s)\,ds.
\tag{7}
\]

If \(\rho\) has degree \(n-1\), then \(\Phi\) and the generic inverse
equation have degree \(n\).

## 2. One curve controls every nonzero-target collision

For a target \((A,B,C)\) with \(C\ne0\), set

\[
P=BC,\qquad Q=AC^2.
\]

The inverse equation is

\[
\Phi(w)=wP-Q.
\tag{8}
\]

Its derivative at a root is

\[
\Phi'(w)-P=\rho(w)-P=-\gamma.
\tag{9}
\]

Hence finite source points correspond exactly to simple roots of (8).

For \(r\ne t\), the chord through
\((r,\Phi(r))\) and \((t,\Phi(t))\) is tangent at \(r\) if and only if

\[
\Phi(t)-\Phi(r)-(t-r)\Phi'(r)=0.
\]

The numerator is divisible by \((t-r)^2\). Define the polynomial

\[
\boxed{
\mathcal T_\Phi(r,t)
=
\frac{\Phi(t)-\Phi(r)-(t-r)\Phi'(r)}{(t-r)^2}.}
\tag{10}
\]

On the diagonal,

\[
\mathcal T_\Phi(r,r)=\frac{\rho'(r)}2.
\tag{11}
\]

If \(\deg\Phi=n\), then

\[
\deg\mathcal T_\Phi=n-2.
\tag{12}
\]

Let \(\overline{\mathcal T}_\Phi\) be its projective closure.

## 3. Exact collision formula

Let \(q\) be an odd prime power over which all coefficients in (5) are
defined.  For \(t\in\mathbb F_q^3\), put

\[
m_q(t)=\#F_\rho^{-1}(t)(\mathbb F_q)
\]

and

\[
\mathcal V_\rho(q)
=\sum_t m_q(t)\bigl(m_q(t)-1\bigr).
\tag{13}
\]

Define

\[
\tau(q)=q+1-\#
\overline{\mathcal T}_\Phi(\mathbb F_q).
\tag{14}
\]

Let

\[
\begin{aligned}
I(q)&=\#\{\text{points of }\overline{\mathcal T}_\Phi
                 \text{ at infinity over }\mathbb F_q\},\\
D(q)&=\#\{r\in\mathbb F_q:\mathcal T_\Phi(r,r)=0\},\\
H(q)&=\#\{(r,t)\in\mathbb F_q^2:
 r\ne t,\ 
 \mathcal T_\Phi(r,t)=\mathcal T_\Phi(t,r)=0\}.
\end{aligned}
\tag{15}
\]

Set

\[
c(q)=-2+2I(q)+2D(q)+H(q)
\tag{16}
\]

and let

\[
\lambda=\rho'(0),\qquad
\delta(q)=
\begin{cases}
1,&\lambda=0\text{ in }\mathbb F_q,\\
0,&\lambda\ne0\text{ in }\mathbb F_q.
\end{cases}
\tag{17}
\]

### Theorem 1

For every normalized weighted lift as above,

\[
\boxed{
\mathcal V_\rho(q)
=(q-1)\left(q^2-\delta(q)q+2\tau(q)+c(q)\right).}
\tag{18}
\]

### Proof

For \(C\ne0\), every ordered pair \(r\ne t\) determines a unique chord and
hence a unique pair \((P,Q)\). It reconstructs two finite source points
unless the chord is tangent at one of its endpoints.

The number tangent at the first endpoint is

\[
\#
\overline{\mathcal T}_\Phi(\mathbb F_q)-I(q)-D(q)
=q+1-\tau(q)-I(q)-D(q).
\tag{19}
\]

The same count holds at the second endpoint, and their intersection has
size \(H(q)\). Therefore the number of good ordered pairs for each nonzero
\(C\) is

\[
M(q)
=q(q-1)
-2\bigl(q+1-\tau(q)-I(q)-D(q)\bigr)
+H(q).
\tag{20}
\]

The nonzero-\(C\) stratum contributes \((q-1)M(q)\).

It remains to count the plane \(C=0\).  The equation \(x\gamma=0\) splits
the source into \(x=0\) and \(\gamma=0\).

On \(x=0\), the map has the triangular form

\[
(y,z)\longmapsto
\left(\mu y^2+(\kappa+2)z,\,
-\frac{y}{\kappa+2},\,0\right)
\tag{21}
\]

for a seed-dependent constant \(\mu\).  This is a bijection onto the
target plane.

On \(\gamma=0\), only the first nonzero coefficients of \(\rho\) and
\(\theta\) survive:

\[
B=\frac{1+\lambda u}{x},\qquad
A=\frac{u+\lambda u^2/2}{x^2}.
\tag{22}
\]

If \(\lambda\ne0\), then

\[
B^2-2\lambda A=\frac1{x^2}.
\tag{23}
\]

Exactly \(q(q-1)/2\) targets admit two curved preimages. Together with their
one flat preimage, they contribute

\[
3q(q-1)
\tag{24}
\]

ordered collisions.

If \(\lambda=0\), then

\[
B=\frac1x,\qquad A=\frac{u}{x^2}.
\tag{25}
\]

There are \(q(q-1)\) targets with one curved and one flat preimage, so the
boundary contributes

\[
2q(q-1).
\tag{26}
\]

Adding (20) to (24) or (26) gives (18). \(\square\)

## 4. The genus ladder

The projective tangent curve has degree \(n-2\). Its arithmetic genus is

\[
\boxed{
g_{\mathrm{arith}}(n)
=\frac{(n-3)(n-4)}2.}
\tag{27}
\]

If the curve is smooth, this is its geometric genus.  The first degrees are:

| Generic fiber degree \(n\) | Tangent-curve degree | Genus when smooth | Frobenius type |
| ---: | ---: | ---: | --- |
| 3 | 1 | 0 | Tate / polynomial |
| 4 | 2 | 0 | finite quadratic Artin corrections |
| 5 | 3 | 1 | elliptic |
| 6 | 4 | 3 | genus-three Jacobian |
| 7 | 5 | 6 | genus-six Jacobian |

For Gallagher's canonical seeds

\[
\rho_d(w)
=2w-3w^2+w(1-w)
\left(w^{d-2}-\frac6{d(d+1)}\right),
\qquad d=n-1,
\tag{28}
\]

the tangent curves for \(3\le n\le7\) have smooth reduction modulo \(101\).
Consequently, they are smooth in characteristic zero, and the genera in the
table are attained.

For example, the degree-six member produces the smooth quartic

\[
\begin{aligned}
0={}&-25r^4-20r^3t+24r^3-15r^2t^2+18r^2t\\
&-10rt^3+12rt^2-56r-5t^4+6t^3-28t+27,
\end{aligned}
\tag{29}
\]

whose smooth projective model has genus \(3\).

This is the structural transition hidden by looking at only one
counterexample: higher weighted lifts naturally generate higher-genus
Frobenius packets.

## 5. Local zeta factorization

Fix a prime \(p\) of good reduction for the lift, the tangent curve, and the
finite schemes in (15). Write

\[
\tau_r
=p^r+1-\#
\overline{\mathcal T}_\Phi(\mathbb F_{p^r})
\tag{30}
\]

and

\[
c_r=-2+2I_r+2D_r+H_r.
\tag{31}
\]

Let

\[
P_{\mathcal T,p}(T)
=\det\left(1-\mathrm{Frob}_pT
\mid H^1_{\mathrm{et}}
(\overline{\mathcal T}_\Phi,\mathbb Q_\ell)\right)
\tag{32}
\]

and let \(P_{\mathrm{fin},p}(T)\) be the characteristic polynomial of the
virtual finite permutation representation

\[
-2\mathbf 1+2[I]+2[D]+[H].
\tag{33}
\]

If \(\delta_p=1\) when \(\lambda=0\pmod p\) and \(0\) otherwise, then the
local zeta function of the self-fiber product is

\[
\boxed{
Z_{F_\rho,p}(T)
=
\frac{1-p^2T}{(1-p^3T)^2}
\cdot
\frac{P_{\mathcal T,p}(T)^2}
     {P_{\mathcal T,p}(pT)^2}
\cdot
\frac{P_{\mathrm{fin},p}(T)}
     {P_{\mathrm{fin},p}(pT)}
\cdot
\left(\frac{1-p^2T}{1-pT}\right)^{\delta_p}.}
\tag{34}
\]

Indeed, Theorem 1 gives

\[
\begin{aligned}
\#(\mathbb A^3\times_{F_\rho}\mathbb A^3)
(\mathbb F_{p^r})
={}&2p^{3r}-p^{2r}
+2p^r\tau_r-2\tau_r\\
&+p^rc_r-c_r
-\delta_p(p^{2r}-p^r),
\end{aligned}
\tag{35}
\]

and (34) follows by exponentiating the point counts.

## 6. The universal corrected tower

Let

\[
V_r(p)=\mathcal V_\rho(p^r)
\]

and define the complete non-Tate packet

\[
B_r(p)=2\tau_r+c_r-\delta_pp^r.
\tag{36}
\]

Then

\[
V_r(p)=(p^r-1)\bigl(p^{2r}+B_r(p)\bigr).
\tag{37}
\]

The raw adjacent congruence is controlled exactly by the Frobenius packet:

\[
V_r(p)-V_{r-1}(p)
\equiv B_{r-1}(p)-B_r(p)\pmod p.
\tag{38}
\]

Define

\[
\widehat V_r(p)
=V_r(p)-(p^r-1)B_r(p).
\tag{39}
\]

### Theorem 2

For every good odd prime and every \(r\ge2\),

\[
\widehat V_r(p)=p^{3r}-p^{2r}
\tag{40}
\]

and

\[
\boxed{
v_p\left(
\widehat V_r(p)-\widehat V_{r-1}(p)
\right)=2r-2.}
\tag{41}
\]

The correction is canonical at the level of the zeta decomposition: it
removes the weight-one curve packet and the weight-zero finite packet,
leaving the Tate contribution.

## 7. What is new here

This theorem organizes the first three worked examples:

1. degree three has only genus-zero data and a polynomial collision count;
2. degree four introduces finite quadratic monodromy;
3. degree five introduces a non-CM elliptic trace; and
4. degree six already carries a genus-three curve.

The result is not a cryptographic construction and does not assert
pseudorandomness. It gives an exact arithmetic hierarchy of the collision
schemes attached to the weighted-lift counterexamples.

## 8. Verification

The companion script
[`verify_weighted_lift_collision_synthesis.py`](../verification/related/verify_weighted_lift_collision_synthesis.py)
checks:

1. the chord/tangency inclusion-exclusion identity for degrees \(3\) through
   \(7\) over two prime fields;
2. the ordinary and \(\lambda=0\) boundary formulas;
3. the genus ladder;
4. smooth reduction modulo \(101\) for the five canonical tangent curves;
   and
5. forty-two exact corrected-tower valuations.

These are regression checks. The proof of Theorems 1 and 2 is the displayed
algebra.

## 9. References and priority

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  Sections 7--9.
- A. Gallagher,
  [Weighted lifts from the Jacobian counterexample](https://github.com/algal/jacobianfun/blob/main/RESEARCH.md).

The source proves the weighted-lift construction and every-degree generic
fiber statement, but does not state the finite-field collision theorem,
genus ladder, or zeta factorization above. A targeted search found no prior
version of those formulas. This is evidence only; historical priority still
requires specialist review.
