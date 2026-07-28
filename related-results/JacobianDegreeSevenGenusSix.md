# A genus-six Frobenius automaton in degree seven

## Status

This note gives an explicit generic-degree-seven member of Gallagher's
weighted-lift family with good reduction at \(p=5\). Its tangent
divided-difference curve is a smooth plane quintic of genus six. We compute
the complete local \(L\)-polynomial, the finite orbit packet, and the exact
periodic obstruction to a raw adjacent collision congruence.

Raw divisibility by \(5\) occurs in exactly \(28\) of the \(156\) level
classes. After removing the complete Frobenius packet, the corrected tower
again has exact adjacent valuation \(2r-2\).

This is a **structural follow-on**, not the solution of a named conjecture.
The general collision formula comes from the all-degree theorem in this
repository. The explicit genus-six packet and obstruction automaton appear
to be new; literature priority remains provisional.

## 1. An integral seed with good reduction at five

Take

\[
\rho(w)=-w+4w^3+3w^5-7w^6.
\tag{1}
\]

Then

\[
\rho(0)=0,\qquad
\rho(1)=-1,\qquad
\int_0^1\rho(w)\,dw=0.
\]

Moreover,

\[
\kappa=\rho'(1)=-16,\qquad
-\frac{1+\kappa}{2+\kappa}=-\frac{15}{14},
\]

so every denominator in the weighted-lift construction is a unit modulo
\(5\). The inverse polynomial is

\[
\Phi(w)=\int_0^w\rho(s)\,ds
=-\frac12w^2+w^4+\frac12w^6-w^7.
\tag{2}
\]

The resulting Keller map has constant nonzero Jacobian and generic fiber
degree \(7\).

Twice its tangent divided difference is the integral plane quintic

\[
\begin{aligned}
\mathcal T(r,t)={}&
-12r^5-10r^4t+5r^4-8r^3t^2+4r^3t\\
&-6r^2t^3+3r^2t^2+6r^2-4rt^4+2rt^3+4rt\\
&-2t^5+t^4+2t^2-1.
\end{aligned}
\tag{3}
\]

Modulo \(5\), the affine singular ideal of (3) has Gröbner basis
\(\{1\}\), and the projective partial derivatives have no common zero at
infinity. Therefore its projective closure \(\mathcal C\) is a smooth plane
quintic over \(\mathbb F_5\), of genus

\[
g=\frac{(5-1)(5-2)}2=6.
\tag{4}
\]

## 2. Exact point counts and the local factor

For

\[
\tau_r=5^r+1-\#\mathcal C(\mathbb F_{5^r}),
\tag{5}
\]

exact root counting gives

\[
\begin{array}{c|r|r}
r&\#\mathcal C(\mathbb F_{5^r})&\tau_r\\ \hline
1&6&0\\
2&26&0\\
3&132&-6\\
4&654&-28\\
5&3046&80\\
6&15410&216.
\end{array}
\tag{6}
\]

Newton's identities and the genus-six functional equation give

\[
\boxed{
\begin{aligned}
P_5(T)={}&1+2T^3+7T^4-16T^5-34T^6-80T^7\\
&+175T^8+250T^9+15625T^{12}.
\end{aligned}}
\tag{7}
\]

The reciprocal characteristic polynomial

\[
\begin{aligned}
Q_5(X)={}&X^{12}+2X^9+7X^8-16X^7-34X^6\\
&-80X^5+175X^4+250X^3+15625
\end{aligned}
\tag{8}
\]

is irreducible over \(\mathbb Q\). One short certificate uses
\(Y=X+5/X\):

\[
X^{-6}Q_5(X)
=Y^6-30Y^4+2Y^3+232Y^2-46Y-354.
\tag{9}
\]

The polynomial on the right is irreducible modulo \(23\). The norm of the
quadratic discriminant \(Y^2-20\) is

\[
81076=2^2\cdot20269,
\]

which is not a square. Thus (8) is irreducible. The genus-six packet does
not split into a rational product of lower-degree Frobenius packets.

## 3. The finite orbit correction

Let \(I_r,D_r,H_r\) be the infinity, diagonal, and ordered bitangency counts
over \(\mathbb F_{5^r}\). Exact factorization gives the Frobenius orbit
degrees

\[
\begin{array}{c|c}
\text{scheme}&\text{orbit degrees}\\ \hline
I&1,4\\
D&5\\
H&2,4,4,10.
\end{array}
\tag{10}
\]

For example, in \(\mathbb F_5[r]\),

\[
\begin{aligned}
I(r)&\doteq
(r+2)(r^4-2r^3-2r^2+2r-2),\\
D(r)&\doteq r^5-r^2-2.
\end{aligned}
\tag{11}
\]

The off-diagonal resultant factors have degrees \(2,4,4,10\). Consequently

\[
\begin{aligned}
I_r&=1+4[4\mid r],\\
D_r&=5[5\mid r],\\
H_r&=2[2\mid r]+8[4\mid r]+10[10\mid r].
\end{aligned}
\tag{12}
\]

Put

\[
c_r=-2+2I_r+2D_r+H_r.
\tag{13}
\]

Then

\[
\boxed{
c_r=
2[2\mid r]+16[4\mid r]+10[5\mid r]+10[10\mid r].}
\tag{14}
\]

## 4. Exact collision formula

Let \(\mathcal V_r\) count ordered pairs of distinct source points over
\(\mathbb F_{5^r}\) with the same image. Since
\(\rho'(0)=-1\ne0\pmod5\), there is no boundary-exception term. The
all-degree collision theorem gives

\[
\boxed{
\mathcal V_r
=(5^r-1)\left(5^{2r}+2\tau_r+c_r\right).}
\tag{15}
\]

Define the non-Tate packet

\[
B_r=2\tau_r+c_r.
\tag{16}
\]

As always,

\[
\mathcal V_r-\mathcal V_{r-1}
\equiv B_{r-1}-B_r\pmod5.
\tag{17}
\]

## 5. The obstruction is a finite automaton

Modulo \(5\), equation (7) yields

\[
\tau_r+2\tau_{r-3}+2\tau_{r-4}
+4\tau_{r-5}+\tau_{r-6}=0
\qquad(r>6).
\tag{18}
\]

Starting from

\[
(\tau_1,\ldots,\tau_6)
\equiv(0,0,4,2,0,1)\pmod5,
\tag{19}
\]

the six-state trace vector has exact period \(39\). Meanwhile (14) reduces
modulo \(5\) to

\[
c_r\equiv2[2\mid r]+[4\mid r]\pmod5,
\tag{20}
\]

which has period \(4\). Since \(\gcd(39,4)=1\), the complete obstruction has
period \(156\).

Let

\[
\begin{aligned}
\mathcal R=\{&
1,10,16,30,32,33,36,38,42,48,49,55,64,69,\\
&71,75,77,81,84,87,92,98,103,118,123,131,137,150
\}\subset\mathbb Z/156\mathbb Z.
\end{aligned}
\tag{21}
\]

### Theorem 1

For every \(r\ge2\),

\[
\boxed{
5\mid\mathcal V_r-\mathcal V_{r-1}
\quad\Longleftrightarrow\quad
r\bmod156\in\mathcal R.}
\tag{22}
\]

Thus the raw adjacent congruence holds at exactly

\[
\frac{28}{156}=\frac7{39}
\tag{23}
\]

of the levels. At every other level,

\[
v_5(\mathcal V_r-\mathcal V_{r-1})=0.
\tag{24}
\]

The first five adjacent differences, at \(r=2,\ldots,6\), are all
\(5\)-adic units.

This is not statistical behavior. It is an exact finite-state consequence
of Frobenius on a genus-six curve coupled to a finite permutation packet.

## 6. The corrected supercongruence

Define

\[
\widehat{\mathcal V}_r
=\mathcal V_r-(5^r-1)B_r.
\tag{25}
\]

Equation (15) gives

\[
\widehat{\mathcal V}_r=5^{3r}-5^{2r}.
\tag{26}
\]

### Theorem 2

For every \(r\ge2\),

\[
\boxed{
v_5\left(
\widehat{\mathcal V}_r-\widehat{\mathcal V}_{r-1}
\right)=2r-2.}
\tag{27}
\]

The first six corrected values are

\[
100,\ 15000,\ 1937500,\ 243750000,\
30507812500,\ 3814453125000.
\tag{28}
\]

The contrast is exact:

- the raw tower is governed by a \(156\)-state obstruction;
- the corrected tower is a pure Tate expression with a linear valuation
  law.

## 7. Place in the collision ladder

\[
\begin{array}{c|c|c}
\text{fiber degree}&\text{non-Tate packet}&\text{raw behavior}\\ \hline
3&\text{none}&\text{polynomial}\\
4&\text{quadratic Artin}&\text{sign obstruction}\\
5&\text{non-CM elliptic}&\text{elliptic trace obstruction}\\
6&\text{genus three}&\text{permanent obstruction at }13\\
7&\text{genus six}&\text{period-156 automaton at }5.
\end{array}
\tag{29}
\]

This is a useful formulation for a broader supercongruence synthesis:
adjacent divisibility is a property of the complete Frobenius packet, not
merely of the leading point-count polynomial.

## 8. Verification

The exact checker
[`verify_jacobian_degree_seven.py`](../verification/related/verify_jacobian_degree_seven.py)
verifies:

1. algebraic smoothness of the projective quintic over \(\mathbb F_5\);
2. the orbit-degree factorizations in (10);
3. the six extension-field point counts in (6);
4. the local \(L\)-polynomial and its rational irreducibility;
5. the exact periods \(39\) and \(156\);
6. all \(28\) divisibility classes; and
7. the corrected exact valuations through \(r=6\).

The point counter does not enumerate \(q^2\) pairs. For each
\(r\in\mathbb F_q\), it computes

\[
\deg\gcd\left(\mathcal T(r,t),t^q-t\right),
\]

so the \(\mathbb F_{5^6}\) calculation remains exact and small.

Run:

```text
python verification/related/verify_jacobian_degree_seven.py
```

## 9. References and priority boundary

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  for the general weighted-lift construction in every generic degree.
- T. Shaska,
  [Graded Keller maps and the Jacobian Conjecture](https://arxiv.org/abs/2607.20210),
  for the graded quotient and arithmetic thin-image viewpoint.
- [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md),
  for the general collision formula specialized here.

The cited sources do not compute finite-field collision zeta functions,
higher-genus Frobenius packets, or adjacent-level obstruction automata.
Targeted searches found no prior occurrence of (7), (22), or this seed.
That is preliminary evidence only; specialist priority review remains
necessary.
