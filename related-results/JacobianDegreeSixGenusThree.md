# A genus-three Frobenius obstruction in degree six

## Status

This note specializes the all-degree weighted-lift collision theorem to
Gallagher's canonical generic-degree-six Keller map. At the good prime
\(p=13\), it computes the complete genus-three Frobenius packet and the
finite orbit correction. The raw adjacent collision congruence fails even
modulo \(13\) at every level. Removing the complete non-Tate packet restores
the exact adjacent valuation \(2r-2\).

This is a **structural follow-on**, not the solution of a named conjecture.
The collision formula is a specialization of the all-degree theorem in this
repository. The explicit local \(L\)-polynomial, permanent obstruction, and
corrected tower below appear to be new; literature priority remains
provisional.

## 1. The degree-six member

Take Gallagher's canonical degree-five seed

\[
\rho(w)=\frac95w-\frac{14}{5}w^2+w^4-w^5.
\tag{1}
\]

It satisfies

\[
\rho(0)=0,\qquad
\rho(1)=-1,\qquad
\int_0^1\rho(w)\,dw=0.
\]

The associated weighted lift has constant Jacobian \(1\) and generic fiber
degree \(6\). Its tangent divided-difference curve is the plane quartic

\[
\begin{aligned}
\mathcal C:\quad 0={}&
-25r^4-20r^3t+24r^3-15r^2t^2+18r^2t\\
&-10rt^3+12rt^2-56r-5t^4+6t^3-28t+27.
\end{aligned}
\tag{2}
\]

An exact Gröbner-basis calculation modulo \(13\) gives the unit ideal for
the affine singular locus, and the three projective partial derivatives
have no common zero at infinity. Thus \(\mathcal C\) is a smooth plane
quartic over \(\mathbb F_{13}\), hence a genus-three curve.

## 2. The local \(L\)-polynomial

Direct enumeration in the exact fields

\[
\begin{aligned}
\mathbb F_{13^2}
&=\mathbb F_{13}[u]/(u^2+3u+1),\\
\mathbb F_{13^3}
&=\mathbb F_{13}[v]/(v^3+4v^2+1)
\end{aligned}
\]

gives

\[
\#\mathcal C(\mathbb F_{13})=14,\qquad
\#\mathcal C(\mathbb F_{13^2})=202,\qquad
\#\mathcal C(\mathbb F_{13^3})=2120.
\tag{3}
\]

Put

\[
\tau_r=13^r+1-\#\mathcal C(\mathbb F_{13^r}).
\tag{4}
\]

Then

\[
\tau_1=0,\qquad \tau_2=-32,\qquad \tau_3=78.
\tag{5}
\]

Newton's identities and the genus-three functional equation give the local
\(L\)-polynomial

\[
\boxed{
P_{13}(T)
=1+16T^2-26T^3+208T^4+2197T^6.}
\tag{6}
\]

Equivalently, the trace sequence begins

\[
0,-32,78,-320,-2080,622,\ldots
\]

and, for \(r>6\), satisfies

\[
\tau_r+16\tau_{r-2}-26\tau_{r-3}
+208\tau_{r-4}+2197\tau_{r-6}=0.
\tag{7}
\]

The reciprocal characteristic polynomial

\[
X^6+16X^4-26X^3+208X^2+2197
\tag{8}
\]

is irreducible over \(\mathbb Q\). Thus this example carries a genuinely
degree-six Frobenius packet rather than the quadratic or elliptic packet
seen in the preceding rungs.

For a short certificate, divide (8) by \(X^3\) and put
\(Y=X+13/X\). The resulting cubic is

\[
Y^3-23Y-26.
\]

It is irreducible by the rational-root test. In its cubic field, the
quadratic \(X^2-YX+13\) has discriminant \(Y^2-52\), whose norm is

\[
-43056=-2^4\,3^2\,13\,23,
\]

not a rational square. Hence that discriminant is not a square in the cubic
field, proving the irreducibility of (8).

## 3. The finite orbit packet

Let \(I_r,D_r,H_r\) denote respectively the numbers of points over
\(\mathbb F_{13^r}\) in the infinity, diagonal, and ordered bitangency
schemes of the divided-difference curve.

Exact factorization over \(\mathbb F_{13}\) gives the following Frobenius
orbit degrees:

\[
\begin{array}{c|c}
\text{scheme}&\text{orbit degrees}\\ \hline
I&1,3\\
D&1,1,2\\
H&1,1,4,6.
\end{array}
\tag{9}
\]

For example, the infinity and diagonal polynomials factor as

\[
\begin{aligned}
I(r)&\doteq
(r+5)(r^3+r^2+6r-1),\\
D(r)&\doteq
(r-3)(r+6)(r^2+4r+6).
\end{aligned}
\tag{10}
\]

The resultant of
\(\mathcal T(r,t)\) and \(\mathcal T(t,r)\) has factor degrees

\[
1,1,1,1,2,4,6.
\]

Removing the diagonal factors \(1,1,2\) leaves the bitangency degrees in
(9). Consequently

\[
\begin{aligned}
I_r&=1+3[3\mid r],\\
D_r&=2+2[2\mid r],\\
H_r&=2+4[4\mid r]+6[6\mid r].
\end{aligned}
\tag{11}
\]

Here \([S]\) is \(1\) when \(S\) is true and \(0\) otherwise. Define

\[
c_r=-2+2I_r+2D_r+H_r.
\tag{12}
\]

Then

\[
c_r=
6+4[2\mid r]+6[3\mid r]+4[4\mid r]+6[6\mid r].
\tag{13}
\]

## 4. Exact collision counts

Let \(\mathcal V_r\) be the number of ordered pairs of distinct source
points over \(\mathbb F_{13^r}\) with the same image. The all-degree
collision theorem specializes to

\[
\boxed{
\mathcal V_r
=(13^r-1)\left(13^{2r}+2\tau_r+c_r\right).}
\tag{14}
\]

There is no boundary-exception term: the seed's linear coefficient is
\(9/5\), which is nonzero modulo \(13\).

The first three values are

\[
\mathcal V_1=2100,\qquad
\mathcal V_2=4789176,\qquad
\mathcal V_3=10600041492.
\tag{15}
\]

## 5. A permanent raw obstruction

Put

\[
B_r=2\tau_r+c_r.
\tag{16}
\]

Modulo \(13\), equation (6) reduces to \(1+3T^2\), while \(c_r\) has period
\(12\). Therefore \(B_r\bmod 13\) has period \(12\). For
\(r=1,\ldots,12\), its values are

\[
\boxed{
6,11,12,11,6,5,6,0,12,0,6,4.}
\tag{17}
\]

No two consecutive entries are equal, including the cyclic pair
\((4,6)\).

Since

\[
\mathcal V_r-\mathcal V_{r-1}
\equiv B_{r-1}-B_r\pmod {13},
\tag{18}
\]

we obtain:

### Theorem 1

For every \(r\ge2\),

\[
\boxed{
v_{13}(\mathcal V_r-\mathcal V_{r-1})=0.}
\tag{19}
\]

Thus this natural collision sequence has no raw adjacent
supercongruence—not even divisibility by \(13\)—at any level. The
obstruction is the complete Frobenius packet, not numerical noise.

## 6. The corrected supercongruence

Define

\[
\widehat{\mathcal V}_r
=\mathcal V_r-(13^r-1)B_r.
\tag{20}
\]

Equation (14) gives the exact identity

\[
\widehat{\mathcal V}_r=13^{3r}-13^{2r}.
\tag{21}
\]

Hence:

### Theorem 2

For every \(r\ge2\),

\[
\boxed{
v_{13}\left(
\widehat{\mathcal V}_r-\widehat{\mathcal V}_{r-1}
\right)=2r-2.}
\tag{22}
\]

The first three corrected counts are

\[
2028,\qquad 4798248,\qquad 10599672564.
\tag{23}
\]

The correction is canonical: it removes the weight-one genus-three trace
and the weight-zero finite permutation packet from the collision zeta
function, leaving the Tate contribution.

## 7. Why this rung matters

The first four generic degrees now form an explicit arithmetic ladder:

\[
\begin{array}{c|c|c}
\text{fiber degree}&\text{collision packet}&\text{raw behavior}\\ \hline
3&\text{Tate}&\text{polynomial valuation law}\\
4&\text{quadratic Artin}&\text{periodic sign obstruction}\\
5&\text{non-CM elliptic}&\text{elliptic trace obstruction}\\
6&\text{genus-three Jacobian}&\text{permanent obstruction at }13.
\end{array}
\tag{24}
\]

This is the useful supercongruence perspective: it detects exactly which
cohomological packet prevents adjacent divisibility, then states the
corrected law after that packet is removed. It does not manufacture a
congruence by ignoring the obstruction.

## 8. Verification

The exact checker
[`verify_jacobian_degree_six.py`](../verification/related/verify_jacobian_degree_six.py)
verifies:

1. geometric smoothness modulo \(13\) by Gröbner and projective gcd
   certificates;
2. the orbit-degree factorizations in (9);
3. all curve and finite-packet counts over
   \(\mathbb F_{13}\), \(\mathbb F_{13^2}\), and
   \(\mathbb F_{13^3}\);
4. the local \(L\)-polynomial and its rational irreducibility;
5. the complete period-\(12\) obstruction table; and
6. the corrected exact valuations through \(r=12\).

Run:

```text
python verification/related/verify_jacobian_degree_six.py
```

## 9. References and priority boundary

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  especially the every-degree weighted-lift construction.
- T. Shaska,
  [Graded Keller maps and the Jacobian Conjecture](https://arxiv.org/abs/2607.20210),
  for the graded quotient and arithmetic thin-image viewpoint.
- [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md),
  for the general collision and corrected-tower formulas specialized here.

The cited sources do not compute finite-field collision zeta functions or
the degree-six genus-three packet. Searches for the structural fingerprints
of (6), (14), and (19) found no prior match. That is preliminary evidence,
not a priority certificate.
