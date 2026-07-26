# Finite-field counts for the Fable Jacobian counterexample

## Status

This note proves exact finite-field fiber counts, an exact collision zeta
function, and an adjacent-extension valuation law for the three-dimensional
Jacobian-conjecture counterexample publicly credited to Claude Fable.

The proof uses the established identification of the map with the incidence
space of a binary cubic and a marked simple root. Everything new here after
that identification is elementary finite-field counting. Exact checks over
prime fields and quadratic extensions accompany the note.

The formulas are new to this repository. A targeted search found the recent
structural analyses of the counterexample, including an explicit statement
that its arithmetic counting theory had not been pursued, but did not find
these formulas. Literature priority is therefore provisional.

## 1. The map and its fiber cubic

Let

\[
F=(P,Q,R):\mathbb A^3\longrightarrow\mathbb A^3
\]

be given by

\[
\begin{aligned}
P&=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\tag{1}
\]

Its Jacobian determinant is \(-2\). For a target \(t=(a,b,c)\), define the
binary cubic

\[
B_t(U,V)=cU^3-2U^2V+bUV^2-2aV^3.
\tag{2}
\]

Over every field of characteristic different from \(2\), the points in
\(F^{-1}(t)\) are in bijection with the simple rational projective roots of
\(B_t\). For a finite root \(w\), put

\[
p_t(w)=cw^3-2w^2+bw-2a,\qquad
h=\frac{p_t'(w)}2.
\]

The corresponding source point is

\[
x=\frac1h,\qquad y=w-h,\qquad z=5h^2-3wh-ch^3.
\tag{3}
\]

The root at infinity occurs exactly when \(c=0\), and corresponds to

\[
(x,y,z)=(0,b,a-4b^2).
\tag{4}
\]

These formulas make the marked-root correspondence valid over finite fields,
not only over \(\mathbb C\).

## 2. Complete factorization statistics

Let \(q\) be an odd prime power. For \(j\in\{0,1,2,3\}\), define

\[
N_j(q)=
\#\left\{t\in\mathbb F_q^3:
  \#F^{-1}(t)(\mathbb F_q)=j\right\}.
\tag{5}
\]

### Theorem 1

If the characteristic is not \(3\), the five possible factorization strata
of \(B_t\) have the following cardinalities.

| Root pattern over \(\mathbb F_q\) | Fiber size | Number of targets |
| --- | ---: | ---: |
| three distinct rational roots | 3 | \((q-1)(q^2+2)/6\) |
| one rational root and an irreducible quadratic | 1 | \(q^2(q-1)/2\) |
| irreducible cubic | 0 | \((q-1)(q^2-1)/3\) |
| one double and one simple rational root | 1 | \(q^2-q+1\) |
| one triple rational root | 0 | \(q-1\) |

In characteristic \(3\), the corresponding table is

| Root pattern over \(\mathbb F_q\) | Fiber size | Number of targets |
| --- | ---: | ---: |
| three distinct rational roots | 3 | \(q^2(q-1)/6\) |
| one rational root and an irreducible quadratic | 1 | \(q^2(q-1)/2\) |
| irreducible cubic | 0 | \(q^2(q-1)/3\) |
| one double and one simple rational root | 1 | \(q^2\) |
| one triple rational root | 0 | \(0\) |

In particular, \(N_2(q)=0\) in every odd characteristic.

### Proof

A binary cubic with three distinct rational projective roots is determined,
up to nonzero scalar, by an unordered triple of distinct points of
\(\mathbb P^1(\mathbb F_q)\). There are

\[
\binom{q+1}{3}
\tag{6}
\]

such triples. It has a unique representative in the affine slice (2) unless
its \(U^2V\)-coefficient is zero.

A triple containing the point at infinity has nonzero \(U^2V\)-coefficient.
For a triple of finite roots \(r,s,t\), that coefficient vanishes precisely
when

\[
r+s+t=0.
\tag{7}
\]

If the characteristic is not \(3\), inclusion-exclusion gives
\((q-1)(q-2)\) ordered triples of distinct elements satisfying (7), hence
\((q-1)(q-2)/6\) unordered triples. Therefore the number of completely split
targets is

\[
\binom{q+1}{3}-\frac{(q-1)(q-2)}6
=\frac{(q-1)(q^2+2)}6.
\tag{8}
\]

In characteristic \(3\), the three pairwise-equality diagonals have a common
intersection of size \(q\), rather than size \(1\). There are consequently
\(q(q-1)\) ordered distinct zero-sum triples. Replacing the subtracted term
in (8) by \(q(q-1)/6\) gives \(q^2(q-1)/6\).

The discriminant locus has \(q^2\) points. Indeed, every multiple finite root
\(\rho\) and leading coefficient \(c\) determine the unique target

\[
(a,b,c)=\left(\rho^2-c\rho^3,\ 4\rho-3c\rho^2,\ c\right).
\tag{9}
\]

Outside characteristic \(3\), the triple-root locus contains \(q-1\) points.
In characteristic \(3\), a cube of a linear form has no mixed terms, so it
cannot have the fixed nonzero \(U^2V\)-coefficient in (2); the triple-root
locus is empty.

The source and target both have \(q^3\) rational points, so

\[
\sum_t\#F^{-1}(t)(\mathbb F_q)=q^3.
\tag{10}
\]

Together with the absence of two-point fibers, this forces
\(N_0=2N_3\). Subtracting the triple-root locus from \(N_0\) gives the
irreducible-cubic row in each table. Subtracting the triple-root locus from
the \(q^2\)-point discriminant gives the double-plus-simple row.

The total number of smooth targets is \(q^3-q^2\). A smooth cubic has
factorization type \((1,1,1)\), \((1,2)\), or \((3)\). Subtracting the split
and irreducible rows from \(q^3-q^2\) gives \(q^2(q-1)/2\) targets of type
\((1,2)\) in both cases. This proves every entry. \(\square\)

## 3. Image and collision counts

Define the collision variance

\[
\mathcal V(q)=
\sum_{t\in\mathbb F_q^3}
\left(\#F^{-1}(t)(\mathbb F_q)-1\right)^2.
\tag{11}
\]

### Corollary 2

For every odd prime power \(q\),

\[
\boxed{
\mathcal V(q)=
\begin{cases}
(q-1)(q^2+2),&\operatorname{char}\mathbb F_q\ne3,\\[2mm]
q^2(q-1),&\operatorname{char}\mathbb F_q=3.
\end{cases}}
\tag{12}
\]

Moreover,

\[
N_3(q)=\frac{\mathcal V(q)}6,\qquad
N_0(q)=\frac{\mathcal V(q)}3,\qquad
N_1(q)=q^3-\frac{\mathcal V(q)}2.
\tag{13}
\]

Hence

\[
\#F(\mathbb F_q^3)=q^3-\frac{\mathcal V(q)}3.
\tag{14}
\]

### Proof

Since the only fiber sizes are \(0,1,3\), equation (10) and the equality of
the source and target cardinalities give \(N_0=2N_3\). Thus

\[
\mathcal V(q)=N_0+4N_3=6N_3.
\]

The completely split row of Theorem 1 now proves (12), and the remaining
formulas follow immediately. \(\square\)

Let

\[
\mathcal C=\mathbb A^3\times_F\mathbb A^3
\tag{15}
\]

be the self-fiber product. Its rational points are ordered pairs of source
points having the same image, so

\[
\#\mathcal C(\mathbb F_q)
=\sum_t\#F^{-1}(t)(\mathbb F_q)^2
=q^3+\mathcal V(q).
\tag{16}
\]

Consequently,

\[
\#\mathcal C(\mathbb F_q)=
\begin{cases}
2q^3-q^2+2q-2,&\operatorname{char}\mathbb F_q\ne3,\\
2q^3-q^2,&\operatorname{char}\mathbb F_q=3.
\end{cases}
\tag{17}
\]

## 4. Frobenius tower and exact valuations

Fix an odd prime \(p\), and write

\[
\mathcal V_r(p)=\mathcal V(p^r),\qquad
\mathcal C_r(p)=\#\mathcal C(\mathbb F_{p^r}).
\tag{18}
\]

### Theorem 3

For \(r\ge2\),

\[
\boxed{
v_p\!\left(\mathcal V_r(p)-\mathcal V_{r-1}(p)\right)
=
v_p\!\left(\mathcal C_r(p)-\mathcal C_{r-1}(p)\right)
=
\begin{cases}
r-1,&p\ge5,\\
2r-2,&p=3.
\end{cases}}
\tag{19}
\]

Thus characteristic \(3\) gains one complete adjacent-extension layer.

### Proof

For \(p\ge5\),

\[
\mathcal V_r(p)
=p^{3r}-p^{2r}+2p^r-2.
\]

Therefore

\[
\begin{aligned}
\mathcal V_r(p)-\mathcal V_{r-1}(p)
={}&p^{3r-3}(p^3-1)-p^{2r-2}(p^2-1)\\
&+2p^{r-1}(p-1).
\end{aligned}
\tag{20}
\]

After division by \(p^{r-1}\), the last term is a unit modulo \(p\), while
the first two terms vanish modulo \(p\). This gives the first case of (19).

For \(p=3\),

\[
\mathcal V_r(3)=3^{3r}-3^{2r},
\]

and hence

\[
\mathcal V_r(3)-\mathcal V_{r-1}(3)
=3^{2r-2}\left(26\cdot3^{r-1}-8\right).
\tag{21}
\]

The parenthesized factor is a \(3\)-adic unit. Finally,
\(\mathcal C_r-\mathcal C_{r-1}\) differs from the corresponding variance
difference by \(p^{3r}-p^{3r-3}\), whose valuation is larger in both cases.
\(\square\)

## 5. Local collision zeta functions

Equation (17) holds over every finite extension of the prime field.
Therefore the local Hasse--Weil zeta function

\[
Z_{\mathcal C,p}(T)
=\exp\left(\sum_{r\ge1}
\frac{\#\mathcal C(\mathbb F_{p^r})}{r}T^r\right)
\tag{22}
\]

is

\[
\boxed{
Z_{\mathcal C,p}(T)=
\frac{(1-T)^2(1-p^2T)}
{(1-pT)^2(1-p^3T)^2}}
\qquad(p\ge5),
\tag{23}
\]

while

\[
\boxed{
Z_{\mathcal C,3}(T)=
\frac{1-3^2T}{(1-3^3T)^2}.}
\tag{24}
\]

The collision scheme is therefore arithmetically mixed Tate at the level of
its point-count zeta function. No ultraproduct or ultrafilter is involved:
the organizing operation is passage through the actual Frobenius tower
\(\mathbb F_p\subset\mathbb F_{p^2}\subset\cdots\).

## 6. The exact \(S_3\) Frobenius packet

On the smooth target locus, the three roots carry the permutation action of
the geometric monodromy group \(S_3\). The three smooth rows of Theorem 1
count the Frobenius conjugacy classes:

\[
\begin{array}{c|c|c}
\text{factorization}&\text{class in }S_3&
\text{number of targets}\\ \hline
(1,1,1)&1&A_1(q)\\
(1,2)&(12)&A_2(q)\\
(3)&(123)&A_3(q).
\end{array}
\tag{25}
\]

Let \(\operatorname{sgn}\) be the sign character and let
\(\chi_{\mathrm{std}}\) be the two-dimensional standard character. Their
values on the three displayed classes are

\[
\operatorname{sgn}=(1,-1,1),\qquad
\chi_{\mathrm{std}}=(2,0,-1).
\tag{26}
\]

### Corollary 4

For every odd prime power \(q\),

\[
\boxed{
\sum_{t:\Delta(t)\ne0}
\operatorname{sgn}(\operatorname{Frob}_t)=0.}
\tag{27}
\]

Equivalently, the quadratic character sum of the discriminant over the
smooth target slice vanishes exactly.

For the standard character,

\[
\boxed{
\sum_{t:\Delta(t)\ne0}
\chi_{\mathrm{std}}(\operatorname{Frob}_t)
=
\begin{cases}
q-1,&\operatorname{char}\mathbb F_q\ne3,\\
0,&\operatorname{char}\mathbb F_q=3.
\end{cases}}
\tag{28}
\]

### Proof

Insert the three smooth rows of Theorem 1 into

\[
A_1-A_2+A_3
\quad\text{and}\quad
2A_1-A_3.
\]

The first expression is zero in both characteristics. The second is \(q-1\)
outside characteristic \(3\), while the characteristic-\(3\) split and
irreducible rows occur in the exact ratio \(1:2\), giving zero. \(\square\)

For a fixed prime \(p\), define the corresponding trace series by

\[
L_p(\chi,T)=
\exp\left(\sum_{r\ge1}
\frac{\sum_t\chi(\operatorname{Frob}_t)}rT^r\right).
\tag{29}
\]

Then

\[
L_p(\operatorname{sgn},T)=1
\tag{30}
\]

for every odd \(p\), and

\[
L_p(\chi_{\mathrm{std}},T)=
\begin{cases}
\dfrac{1-T}{1-pT},&p\ge5,\\[3mm]
1,&p=3.
\end{cases}
\tag{31}
\]

Thus the characteristic-\(3\) valuation gain in Theorem 3 is the visible
shadow of an exact cancellation of the nontrivial standard Frobenius packet.

## 7. Relation to the current counterexample literature

The announced map was publicly credited to Akhil Mathew's prompt and Claude
Fable's work. Its determinant and three-point collision have independent
formal verification in Isabelle. Subsequent structural work identifies it
with the marked-simple-root incidence map used above.

Shaska's arithmetic discussion says that counting away from the coordinate
stratum should be governed by splitting of the fiber cubic and that no
result in that counting direction was proved there. Theorem 1 and Corollary 4
supply the complete unweighted finite-field and Frobenius-character versions
of that program. They do not solve the harder rational-height counting
problem.

References:

- A. Freitas Ramos, D. Barros Hulak, and R. J. G. Barretto de Queiroz,
  [Formal Verification of an Explicit Counterexample to the Jacobian Conjecture](https://isa-afp.org/entries/Jacobian_Counterexample.html).
- T. Shaska,
  [Graded Keller maps and the Jacobian Conjecture](https://arxiv.org/abs/2607.20210).
- [Exact audit and structural analysis of the three-dimensional Keller counterexample](https://nasqret.github.io/jacobian-counterexample/book/index.html).

## 8. Verification

The companion script
[`verify_jacobian_counterexample_counts.py`](../verification/related/verify_jacobian_counterexample_counts.py)
checks:

1. the complete fiber distribution by direct evaluation of (1) over small
   prime fields;
2. the same formulas over quadratic finite-field extensions;
3. every displayed counting identity;
4. the exact adjacent-extension valuations on a larger symbolic grid.
