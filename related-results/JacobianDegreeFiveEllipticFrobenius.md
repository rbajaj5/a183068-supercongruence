# Degree-five Jacobian collisions and a non-CM elliptic Frobenius packet

## Status

This note proves an exact finite-field collision formula for the degree-five
member of Gallagher's weighted-lift family.  The degree-four member produced
only quadratic-character corrections.  In degree five, the tangent locus is
a smooth plane cubic, and its non-CM elliptic Frobenius trace occurs in the
answer.

The weighted-lift construction and its inverse equation come from Gallagher.
The collision decomposition, elliptic model, local zeta factorization, and
corrected adjacent-extension law below are new to this repository.  Exact
checks over eight prime fields, one quadratic extension, and longer Frobenius
towers accompany the proof.  Literature priority remains provisional.

## 1. The degree-five map

Start with the seed

\[
\rho(w)=\frac{17}{10}w-\frac{27}{10}w^2+w^3-w^4
\tag{1}
\]

and put

\[
\theta(w)
=\int_0^w s\rho'(s)\,ds
=\frac{17}{20}w^2-\frac95w^3+\frac34w^4-\frac45w^5.
\tag{2}
\]

Set

\[
u=1+xy,\qquad
\gamma=1-\frac{37}{27}xy+x^2z,\qquad
w=u\gamma.
\tag{3}
\]

Gallagher's construction gives

\[
F_5(x,y,z)=
\left(
\frac{u+\theta(w)/\gamma^2}{x^2},
\frac{1+\rho(w)/\gamma}{x},
x\gamma
\right).
\tag{4}
\]

All apparent denominators in \(x\) and \(\gamma\) cancel.  Thus (4) is a
polynomial map over
\(\mathbb Z[1/2,1/3,1/5]\), its Jacobian determinant is \(1\), and its
generic fiber degree is \(5\).

Let

\[
\Phi(w)=\int_0^w\rho(s)\,ds
=-\frac{w^2(w-1)(4w^2-w+17)}{20}.
\tag{5}
\]

For a target \((A,B,C)\) with \(C\ne0\), define

\[
P=BC,\qquad Q=AC^2.
\]

The inverse equation is

\[
\Phi(w)=wP-Q.
\tag{6}
\]

Indeed,

\[
BC=\gamma+\rho(w),\qquad
AC^2=w\gamma+\theta(w),
\]

and \(w\rho(w)-\theta(w)=\Phi(w)\).

## 2. The tangent cubic

For distinct \(r,t\), the chord of the graph of \(\Phi\) through
\((r,\Phi(r))\) and \((t,\Phi(t))\) is tangent at \(r\) precisely when

\[
\begin{aligned}
\mathcal A(r,t)={}&
-16r^3-12r^2t+15r^2-8rt^2+10rt-36r\\
&-4t^3+5t^2-18t+17=0.
\end{aligned}
\tag{7}
\]

Tangency at \(t\) is the swapped equation
\(\mathcal A(t,r)=0\).

Let \(\mathcal C\) be the projective closure of (7):

\[
\begin{aligned}
\mathcal A_h(X,Y,Z)={}&
-16X^3-12X^2Y+15X^2Z-8XY^2+10XYZ-36XZ^2\\
&-4Y^3+5Y^2Z-18YZ^2+17Z^3.
\end{aligned}
\tag{8}
\]

The point \((0:1:1)\) lies on \(\mathcal C\).  Projection through that point,
using \(t=1+mr\), gives the quartic model

\[
v^2=-271m^4-1100m^3-2054m^2-2948m-2167.
\tag{9}
\]

The binary-quartic invariants are

\[
I=1537600,\qquad J=4922414080.
\]

Consequently, a Weierstrass model of the Jacobian is

\[
\boxed{
E:\quad y^2=x^3-2594700x-2076643440.}
\tag{10}
\]

Its discriminant and \(j\)-invariant are

\[
\Delta_E
=-2^{16}3^{13}5^2\cdot11\cdot43\cdot229\cdot2633
\tag{11}
\]

and

\[
j(E)
=-\frac{2218759202500}{855595983}
=-\frac{2^2 5^4 31^6}{3\cdot11\cdot43\cdot229\cdot2633}.
\tag{12}
\]

In particular, \(j(E)\) is not an algebraic integer, so \(E\) does not have
complex multiplication.

## 3. The exact collision count

Let \(q\) be a prime power of characteristic not in
\(\{2,3,5\}\).  For a target \(t\in\mathbb F_q^3\), put

\[
m_q(t)=\#F_5^{-1}(t)(\mathbb F_q)
\]

and define

\[
\mathcal V_5(q)
=\sum_{t\in\mathbb F_q^3}m_q(t)\bigl(m_q(t)-1\bigr).
\tag{13}
\]

This is the number of ordered off-diagonal collisions.

Define

\[
a(q)=q+1-\#\mathcal C(\mathbb F_q).
\tag{14}
\]

We also need three finite corrections:

\[
\begin{aligned}
I(q)&=\#\{x\in\mathbb F_q:4x^3+3x^2+2x+1=0\},\\
D(q)&=\#\{x\in\mathbb F_q:40x^3-30x^2+54x-17=0\},\\
H(q)&=\#\{(r,t)\in\mathbb F_q^2:
  r\ne t,\ \mathcal A(r,t)=\mathcal A(t,r)=0\}.
\end{aligned}
\tag{15}
\]

Here \(I(q)\) counts the points of \(\mathcal C\) at infinity,
\(D(q)\) counts diagonal points on the tangent cubic, and \(H(q)\) counts
ordered bitangencies.  Put

\[
c(q)=-2+2I(q)+2D(q)+H(q).
\tag{16}
\]

### Theorem 1

If the characteristic is not \(17\), then

\[
\boxed{
\mathcal V_5(q)
=(q-1)\bigl(q^2+2a(q)+c(q)\bigr).}
\tag{17}
\]

In characteristic \(17\),

\[
\boxed{
\mathcal V_5(q)
=(q-1)\bigl(q^2-q+2a(q)+c(q)\bigr).}
\tag{18}
\]

### Proof

We again split according to the third target coordinate \(C\).

#### Nonzero \(C\)

An ordered pair \(r\ne t\) gives two source points over the same target
exactly when the chord through the corresponding points of the graph of
\(\Phi\) is tangent at neither endpoint.  There are \(q(q-1)\) ordered
distinct pairs in total.

The number tangent at the first endpoint is

\[
\begin{aligned}
\#\{(r,t):r\ne t,\ \mathcal A(r,t)=0\}
&=\#\mathcal C(\mathbb F_q)-I(q)-D(q)\\
&=q+1-a(q)-I(q)-D(q).
\end{aligned}
\tag{19}
\]

The same count holds at the second endpoint, and their intersection has
size \(H(q)\).  Inclusion-exclusion gives

\[
M(q)
=q(q-1)-2\bigl(q+1-a(q)-I(q)-D(q)\bigr)+H(q)
\tag{20}
\]

good ordered pairs.  There are \(q-1\) choices of \(C\ne0\), so this stratum
contributes \((q-1)M(q)\).

#### The plane \(C=0\)

The source equation \(C=x\gamma=0\) has a flat part \(x=0\) and a curved
part \(\gamma=0\).

On \(x=0\), the map is

\[
(y,z)\longmapsto
\left(
\frac{10871y^2-6561z}{2430},
\frac{10y}{27},
0
\right),
\tag{21}
\]

which is a bijection onto the target plane.

On \(\gamma=0\), one obtains

\[
B=\frac{17u+10}{10x},
\qquad
A=\frac{u(17u+20)}{20x^2}.
\]

If the characteristic is not \(17\), these equations satisfy

\[
B^2-\frac{17}{5}A=\frac1{x^2}.
\tag{22}
\]

Exactly \(q(q-1)/2\) targets have a nonzero-square value on the left.
Each has two curved preimages in addition to its unique flat preimage, so
the boundary contributes

\[
3q(q-1).
\tag{23}
\]

Adding (20) and (23) gives (17).

In characteristic \(17\), the curved formulas reduce to

\[
B=\frac1x,\qquad A=\frac{u}{x^2}.
\]

Thus every target with \(B\ne0\) has one curved preimage rather than two.
There are \(q(q-1)\) such targets, each with one additional flat preimage,
so the boundary contribution is \(2q(q-1)\).  This is smaller than (23) by
\(q(q-1)\), proving (18). \(\square\)

## 4. The elliptic and Artin packets

Now fix a prime

\[
p\notin\{2,3,5,11,43,229,2633\}.
\tag{24}
\]

The cubic \(\mathcal C\) has good reduction and is isomorphic to the
reduction of (10).  Let

\[
a_r=p^r+1-\#E(\mathbb F_{p^r}).
\tag{25}
\]

Thus, if \(a_1=a_p\),

\[
a_0=2,\qquad a_r=a_pa_{r-1}-pa_{r-2}.
\tag{26}
\]

For the three finite root schemes in (15), write their extension-field
counts as \(I_r,D_r,H_r\), and set

\[
c_r=-2+2I_r+2D_r+H_r.
\tag{27}
\]

For primes in (24), the bitangency count may equivalently be computed as
the number of roots in \(\mathbb F_{p^r}\) of

\[
\begin{aligned}
h(X)={}&6400X^6-9600X^5+33280X^4-34600X^3\\
&+47269X^2-29679X+13550.
\end{aligned}
\tag{28}
\]

The excluded primes are exactly the small denominator primes together with
the primes at which the displayed elliptic or bitangency models cease to be
étale.

Let

\[
\Pi_p(T)=1-a_pT+pT^2
\tag{29}
\]

be the elliptic Frobenius polynomial.  If \(P_{I,p},P_{D,p},P_{H,p}\) are
the permutation characteristic polynomials of Frobenius on the roots of
the three polynomials in (15) and (28), define the virtual Artin polynomial

\[
P_{\mathrm{fin},p}(T)
=\frac{P_{I,p}(T)^2P_{D,p}(T)^2P_{H,p}(T)}{(1-T)^2}.
\tag{30}
\]

### Theorem 2

The local zeta function of the collision fiber product is

\[
\boxed{
Z_{F_5,p}(T)
=
\frac{1-p^2T}{(1-p^3T)^2}
\cdot\frac{\Pi_p(T)^2}{\Pi_p(pT)^2}
\cdot\frac{P_{\mathrm{fin},p}(T)}
     {P_{\mathrm{fin},p}(pT)}
\cdot\left(\frac{1-p^2T}{1-pT}\right)^{[p=17]}.}
\tag{31}
\]

Here the products in (31) are ordinary multiplication; line breaks merely
separate the Tate, elliptic, finite-Artin, and exceptional-\(17\) factors.
The bracket \([p=17]\) is \(1\) when \(p=17\) and \(0\) otherwise.

### Proof

Let \(N_r\) be the number of points on the fiber product over
\(\mathbb F_{p^r}\).  By (17)--(18),

\[
N_r
=2p^{3r}-p^{2r}
+2p^ra_r-2a_r
+p^rc_r-c_r
-[p=17](p^{2r}-p^r).
\tag{32}
\]

Exponentiating
\(\sum_{r\ge1}N_rT^r/r\) term by term gives (31). \(\square\)

The degree-four collision count was controlled by a finite quadratic
Galois packet.  Formula (31) is the first member of this sequence with a
genuinely elliptic factor.  Because (12) is nonintegral, this elliptic
factor is non-CM and cannot be replaced by a finite collection of quadratic
characters.

## 5. The adjacent-extension obstruction and correction

Put

\[
V_r(p)=\mathcal V_5(p^r)
\]

and define the complete non-Tate packet

\[
B_r(p)=2a_r+c_r-[p=17]p^r.
\tag{33}
\]

Then Theorem 1 is simply

\[
V_r(p)=(p^r-1)\bigl(p^{2r}+B_r(p)\bigr).
\tag{34}
\]

### Theorem 3

For every \(r\ge2\),

\[
V_r(p)-V_{r-1}(p)
\equiv B_{r-1}(p)-B_r(p)\pmod p.
\tag{35}
\]

Moreover,

\[
a_r\equiv a_p^r\pmod p.
\tag{36}
\]

Thus the raw adjacent congruence is obstructed by a non-CM elliptic
Frobenius sequence together with the finite permutation packet \(c_r\).

Define the Frobenius-corrected collision count

\[
\widehat V_r(p)
=V_r(p)-(p^r-1)B_r(p).
\tag{37}
\]

Then

\[
\widehat V_r(p)=p^{3r}-p^{2r},
\tag{38}
\]

and hence

\[
\boxed{
v_p\bigl(\widehat V_r(p)-\widehat V_{r-1}(p)\bigr)=2r-2.}
\tag{39}
\]

### Proof

Reducing (34) modulo \(p\) gives
\(V_r\equiv-B_r\pmod p\), which proves (35).
The recurrence (26) gives (36) by induction.
Equations (38) and (39) follow directly from (34) and (37); in the adjacent
difference the lowest term is the unit multiple
\(p^{2r-2}(1-p^2)\). \(\square\)

The correction in (37) is not being presented as pseudorandomness or as a
cryptographic construction.  Its role is organizational: it removes exactly
the weight-zero and weight-one Frobenius packets and exposes the stable Tate
tower underneath.

## 6. Verification

The companion script
[`verify_jacobian_degree_five.py`](../verification/related/verify_jacobian_degree_five.py)
checks:

1. direct three-dimensional collision counts over eight prime fields;
2. a direct collision count over \(\mathbb F_{7^2}\);
3. the plane-cubic and Weierstrass point counts over eleven prime fields and
   \(\mathbb F_{7^2}\);
4. eighty extension-tower formulas;
5. seventy raw obstruction residues; and
6. seventy exact corrected valuations.

The characteristic-\(17\) boundary exception is included in the direct
checks.

## 7. References and priority

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  especially the weighted-lift construction and the all-degree seed family.
- A. Gallagher,
  [derivation notes for the weighted lift](https://github.com/algal/jacobianfun/blob/main/RESEARCH.md).

A targeted search for the structural fingerprints “weighted lift,”
“finite-field collision,” “tangent cubic,” and “elliptic Frobenius” found no
prior collision formula of the form (17) or zeta factorization of the form
(31).  This is evidence, not a definitive priority determination.
