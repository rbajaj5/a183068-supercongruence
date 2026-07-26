# Degree-four Jacobian collisions and the Frobenius obstruction

## Status

This note proves an exact collision count and local zeta function for the
degree-four Keller map in Gallagher's weighted-lift family. It then determines
exactly when ordinary adjacent-extension supercongruences fail, and shows how
the quadratic Frobenius packet supplies the canonical correction.

The map and its one-variable inverse equation are established in the source
construction. The collision count and all congruence statements below are
new to this repository. Direct checks over prime fields and quadratic
extensions accompany the proof. A targeted search found no prior occurrence
of these formulas; literature priority remains provisional.

## 1. The degree-four map

Put

\[
u=1+3xy,\qquad \gamma=1-4xy-x^2z.
\]

Gallagher's degree-four map is

\[
G(x,y,z)=
\left(
\frac{2u+u^2-3u^4\gamma^2}{x^2},
\frac{1+u-2u^3\gamma^2}{x},
x\gamma
\right).
\tag{1}
\]

The displayed numerators are divisible by the indicated powers of \(x\), so
(1) is a polynomial map over \(\mathbb Z\). Its Jacobian determinant is
\(-6\), and its generic fiber degree is \(4\).

Throughout, let \(q\) be a prime power of characteristic at least \(5\). For
a target \(t\in\mathbb F_q^3\), write

\[
m_q(t)=\#G^{-1}(t)(\mathbb F_q)
\]

and define the off-diagonal collision count

\[
\mathcal V_4(q)=
\sum_{t\in\mathbb F_q^3}m_q(t)\bigl(m_q(t)-1\bigr).
\tag{2}
\]

Because the diagonal in
\(\mathbb A^3\times_G\mathbb A^3\) has \(q^3\) rational points, this is also

\[
\mathcal V_4(q)
=\#(\mathbb A^3\times_G\mathbb A^3)(\mathbb F_q)-q^3.
\tag{3}
\]

Let \(\chi_q\) denote the quadratic character of \(\mathbb F_q\), extended by
\(\chi_q(0)=0\), and set

\[
\kappa(q)=
3+\chi_q(2)+2\chi_q(-2)+2\chi_q(6).
\tag{4}
\]

## 2. The exact collision formula

### Theorem 1

For every prime power \(q\) of characteristic at least \(5\),

\[
\boxed{\mathcal V_4(q)=(q-1)\bigl(q^2+\kappa(q)\bigr).}
\tag{5}
\]

Equivalently,

\[
\#(\mathbb A^3\times_G\mathbb A^3)(\mathbb F_q)
=2q^3-q^2+\kappa(q)q-\kappa(q).
\tag{6}
\]

### Proof

We split according to whether the third target coordinate \(C\) is nonzero.

#### Nonzero \(C\)

For \(C\ne0\), the change from target coordinates \((A,B,C)\) to the two
line parameters is bijective, and the inverse equation is

\[
\Phi(w)=wP-Q,\qquad
\Phi(w)=\frac{w^2-w^4}{2}.
\tag{7}
\]

An affine preimage corresponds to a simple root. Thus ordered off-diagonal
collisions correspond to ordered pairs \(r\ne s\) for which the chord joining
\((r,\Phi(r))\) and \((s,\Phi(s))\) is tangent at neither endpoint.

The chord slope is

\[
D(r,s)=
-\frac{(r+s)(r^2+s^2-1)}2.
\tag{8}
\]

For \(r\ne s\), tangency at \(r\) is equivalent to

\[
3r^2+2rs+s^2=1,
\tag{9}
\]

and tangency at \(s\) is equivalent to

\[
r^2+2rs+3s^2=1.
\tag{10}
\]

The nondegenerate binary quadratic form in (9) has determinant \(2\).
The standard finite-field quadratic-form count gives

\[
\#\{(r,s):3r^2+2rs+s^2=1\}=q-\chi_q(-2).
\tag{11}
\]

Its diagonal contains \(1+\chi_q(6)\) points. Hence the number of ordered
distinct pairs tangent at the first endpoint is

\[
E=q-1-\chi_q(-2)-\chi_q(6).
\tag{12}
\]

The two tangency conditions hold simultaneously precisely when

\[
s=-r,\qquad 2r^2=1,
\]

so their intersection has \(1+\chi_q(2)\) points. Inclusion-exclusion now
gives

\[
\begin{aligned}
M(q)
&=q(q-1)-2E+1+\chi_q(2)\\
&=q^2-3q+3+\chi_q(2)+2\chi_q(-2)+2\chi_q(6)
\end{aligned}
\tag{13}
\]

good ordered pairs. There are \(q-1\) choices of \(C\ne0\), so the nonzero
stratum contributes \((q-1)M(q)\).

#### The plane \(C=0\)

The equation \(C=x\gamma=0\) splits the source into two pieces. On \(x=0\),
the polynomial map restricts to

\[
(y,z)\longmapsto(87y^2+6z,\ y,\ 0),
\tag{14}
\]

which is a bijection onto the target plane \(C=0\).

On \(\gamma=0\), one has \(x\ne0\), and (1) reduces to

\[
B=\frac{1+u}{x},\qquad
A=\frac{u(u+2)}{x^2}.
\]

Therefore

\[
B^2-A=\frac1{x^2}.
\tag{15}
\]

For each \(B\), exactly \((q-1)/2\) values of \(A\) make \(B^2-A\) a nonzero
square. Those \(q(q-1)/2\) targets have two points on \(\gamma=0\), in
addition to their unique point on \(x=0\), and hence contribute six ordered
off-diagonal pairs each. The plane \(C=0\) contributes

\[
3q(q-1).
\tag{16}
\]

Adding (13) and (16) gives

\[
(q-1)\left(M(q)+3q\right)
=(q-1)\left(q^2+\kappa(q)\right),
\]

which proves (5). \(\square\)

## 3. The quadratic Artin factors

Fix a prime \(p\ge5\), and put

\[
\epsilon_a=\left(\frac ap\right),
\qquad a\in\{2,-2,6\},
\tag{17}
\]

where the symbol is Legendre's. Over \(\mathbb F_{p^r}\),

\[
\chi_{p^r}(a)=\epsilon_a^r.
\tag{18}
\]

Consequently, the local zeta function of the collision scheme is

\[
\boxed{
Z_{G,p}(T)=
\frac{(1-p^2T)(1-T)^3}
{(1-p^3T)^2(1-pT)^3}
\prod_{(a,e)\in\{(2,1),(-2,2),(6,2)\}}
\left(\frac{1-\epsilon_aT}{1-\epsilon_apT}\right)^e.}
\tag{19}
\]

Unlike the cubic Fable map, whose collision zeta function has only Tate
factors, the degree-four map contains three explicit quadratic Artin
packets. They are exactly the obstruction to a uniform adjacent-extension
congruence.

## 4. Failure and repair of adjacent supercongruence

For \(r\ge1\), set

\[
V_r(p)=\mathcal V_4(p^r),\qquad
\kappa_r(p)=\kappa(p^r).
\tag{20}
\]

The odd-level value depends only on \(p\bmod24\):

| \(p\bmod24\) | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(\kappa_1(p)\) | 8 | 2 | 0 | 2 | -2 | 4 | 6 | 4 |

At every even level, \(\kappa_r(p)=8\).

### Theorem 2

For \(r\ge2\),

\[
v_p\left(V_r(p)-V_{r-1}(p)\right)=
\begin{cases}
r-1,&p\equiv1\pmod {24},\\
0,&p\not\equiv1\pmod {24}.
\end{cases}
\tag{21}
\]

Thus the raw adjacent supercongruence fails completely at seven of the eight
prime residue classes because a quadratic Frobenius sign changes.

For the two-step tower and \(r\ge3\),

\[
\boxed{
v_p\left(V_r(p)-V_{r-2}(p)\right)=
\begin{cases}
2r-4,&p\equiv7\pmod {24}\text{ and }r\text{ is odd},\\
r-2,&\text{otherwise}.
\end{cases}}
\tag{22}
\]

Finally define the Frobenius-corrected sequence

\[
\widetilde V_r(p)=V_r(p)+\kappa_r(p).
\tag{23}
\]

Then

\[
\boxed{
v_p\left(\widetilde V_r(p)-\widetilde V_{r-1}(p)\right)=
\begin{cases}
r,&p\equiv7\pmod {24}\text{ and }r\text{ is even},\\
r-1,&\text{otherwise}.
\end{cases}}
\tag{24}
\]

### Proof

Equation (5) is

\[
V_r(p)=p^{3r}-p^{2r}+\kappa_r(p)p^r-\kappa_r(p).
\tag{25}
\]

If \(p\equiv1\pmod {24}\), all three quadratic characters are \(1\) at every
level, so \(\kappa_r=8\), and the lowest term in the adjacent difference is
\(8p^{r-1}(p-1)\). If \(p\not\equiv1\pmod {24}\), the displayed table shows
that \(8-\kappa_1(p)\) is nonzero modulo \(p\): this is immediate for
\(p=5,7\), and its absolute value is less than \(p\) for every remaining
prime. The constant terms in (25) therefore make every adjacent difference a
\(p\)-adic unit. This proves (21).

In a two-step difference, \(\kappa_r=\kappa_{r-2}\). The lowest term is

\[
\kappa_r p^{r-2}(p^2-1).
\]

It is a unit multiple of \(p^{r-2}\) unless \(p\equiv7\pmod {24}\) and \(r\)
is odd, when \(\kappa_r=0\). In that case the next term has exact valuation
\(2r-4\). This proves (22).

Adding \(\kappa_r\) to (25) removes the parity-changing constant term:

\[
\widetilde V_r(p)=p^{3r}-p^{2r}+\kappa_r(p)p^r.
\]

Its adjacent difference has exact valuation \(r-1\) unless
\(\kappa_{r-1}=0\), which occurs precisely in the exceptional case of (24).
There the first surviving term is \(8p^r\), of exact valuation \(r\).
\(\square\)

## 5. Interpretation

The cubic and quartic counterexamples now exhibit two distinct arithmetic
regimes:

1. the cubic collision scheme has a purely polynomial point count and an
   ordinary adjacent-extension law;
2. the quartic collision scheme has finite quadratic monodromy, visible as
   three Artin factors, and raw adjacency fails until that Frobenius packet is
   either held fixed by a two-step extension or removed by correction.

This is the concrete organizational role of supercongruences here. They
separate stable polynomial/Tate contributions from finite-monodromy data.
No ultrafilter or geometric-Langlands machinery is involved.

Reference:

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  Sections 7--9.

## 6. Verification

The companion script
[`verify_jacobian_degree_four.py`](../verification/related/verify_jacobian_degree_four.py)
checks:

1. direct collision counts over prime fields;
2. direct counts over quadratic extensions;
3. the quadratic-character formula;
4. the zeta-count expansion; and
5. every exact valuation statement on a larger parameter grid.
