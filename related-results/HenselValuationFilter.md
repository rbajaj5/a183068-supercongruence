# A Hensel valuation filter for Frobenius supercongruences

## Status

This note upgrades the finite precision-\(5^5\) and precision-\(5^6\)
tables for the degree-seven Frobenius obstruction into an exact formula at
every precision.

The general inputs—\(p\)-adic interpolation of constant-recursive
sequences and Hensel lifting—are standard. The explicit phase
factorization, the weighted root count

\[
25\cdot1+1\cdot5+2\cdot25=80,
\]

and the resulting all-precision partition polynomial are structural
follow-ons in this repository. Literature priority for this application is
preliminary.

The word *filter* is literal: the successful congruence classes form a
descending family of clopen sets. This is not an ultrafilter, which would
be a maximal set-theoretic choice of subsets.

## 1. The weighted Hensel mechanism

Let \(p\) be a prime and let \(c\geq0\). Suppose a congruence clock at
precision \(p^k\) has the form

\[
\mathcal X_k
=
\{1,\ldots,T\}\times\mathbf Z/p^{k-c}\mathbf Z
\tag{1}
\]

for all sufficiently large \(k\). For each phase \(a\), suppose the
corresponding defect has a \(p\)-adic analytic interpolation

\[
F_a(z)=p^{b_a}H_a(z),
\qquad
H_a:\mathbf Z_p\longrightarrow\mathbf Z_p,
\tag{2}
\]

where \(b_a\geq c\), and suppose that the reduction
\(\overline H_a\) has \(R_a\) simple zeros in \(\mathbf F_p\).

### Lemma 1 (weighted Hensel count)

For every \(k>b_a\), the number of classes
\(z\bmod p^{k-c}\) satisfying

\[
p^k\mid F_a(z)
\tag{3}
\]

is

\[
R_ap^{b_a-c}.
\tag{4}
\]

Consequently, once \(k>\max_a b_a\), the total number of successful clock
classes is

\[
\boxed{
\sum_aR_ap^{b_a-c}.
}
\tag{5}
\]

### Proof

Condition (3) is equivalent to

\[
H_a(z)\equiv0\pmod {p^{k-b_a}}.
\]

Each simple zero modulo \(p\) lifts uniquely, by Hensel's lemma, to one
zero modulo \(p^{k-b_a}\). A class modulo \(p^{k-b_a}\) has

\[
p^{(k-c)-(k-b_a)}=p^{b_a-c}
\]

representatives modulo \(p^{k-c}\). Multiplying by \(R_a\) proves (4), and
summing over phases proves (5). \(\square\)

The weight in (4) is important. A phase carrying two powers of \(p\)
beyond the clock normalization contributes \(p^2\) finite-precision
classes even though it contains only one inverse-limit root.

## 2. The degree-seven analytic phases

Let

\[
D_r=\mathcal V_{r-1}-\mathcal V_r
\tag{6}
\]

be the raw adjacent defect for the degree-seven example at \(p=5\).
The all-precision period theorem gives the clock

\[
L_k=156\cdot5^{k-1}
=780\cdot5^{k-2}
\qquad(k\geq2).
\tag{7}
\]

Let \(u_r\) be the trace of the six unit Frobenius roots. Once the six
nonunit roots vanish modulo the working precision,

\[
D_r
=
2(u_{r-1}-u_r)
+c_{r-1}-c_r,
\tag{8}
\]

where

\[
c_r
=
2\mathbf1_{2\mid r}
+16\mathbf1_{4\mid r}
+10\mathbf1_{5\mid r}
+10\mathbf1_{10\mid r}.
\tag{9}
\]

The correction has period \(20\). For \(1\leq a\leq780\), define the
eventual unit-packet interpolation

\[
F_a(z)
=
2\left(u_{a+780(z+1)-1}-u_{a+780(z+1)}\right)
+c_{a-1}-c_a.
\tag{10}
\]

Here the powers of the unit roots are interpreted \(5\)-adically. For an
integer clock class, \(F_a\) agrees modulo \(5^k\) with the raw defect on
every sufficiently late representative of that class: the complementary
six roots have the form \(5/\alpha\), with \(\alpha\) a unit, and their
\(r\)-th power sums vanish modulo \(5^k\) once \(r\geq k\).

Let \(A\) be the companion matrix of the degree-six Hensel unit-root
factor and put \(B=A^{780}\). The period certificate from the preceding
note gives

\[
B\equiv I\pmod5.
\tag{11}
\]

Therefore

\[
B^z
=
\sum_{j\geq0}\binom zj(B-I)^j
\tag{12}
\]

converges for \(z\in\mathbf Z_5\). Equation (10) is consequently a
\(5\)-adic analytic function of \(z\). This is the concrete twisted
interpolation of the recurrence on each phase.

Modulo \(25\), the value of \(F_a(z)\) is independent of \(z\). Exactly
\(32\) of the \(780\) phases vanish modulo \(25\); the other \(748\)
phases never contribute to a congruence of precision at least \(25\).

For each of the \(32\) remaining phases, reduce the finite binomial
expansion (12) modulo one power of \(5\) beyond its common content. The
result is:

\[
\begin{array}{c|c|c|c}
b_a&
\#\text{ phases}&
\text{phases with no zero}&
\text{simple roots }a:z/H_a'(z)
\\ \hline
2&29&
33,204,657,761&
\begin{array}{l}
10:0/4,\ 36:0/3,\ 123:4/2,\ 157:4/2,\\
166:3/4,\ 186:4/3,\ 188:3/2,\ 194:1/4,\\
233:3/4,\ 237:3/1,\ 259:1/4,\ 274:1/2,\\
287:4/1,\ 350:0/4,\ 367:0/1,\ 387:1/3,\\
500:2/2,\ 506:0/4,\ 510:2/1,\ 537:2/3,\\
560:1/1,\ 591:2/2,\ 634:2/4,\ 640:3/1,\\
673:1/4
\end{array}
\\ \hline
3&2&189&672:0/3\\
4&1&\varnothing&48:0/4,\ 48:3/1
\end{array}
\tag{13}
\]

Here an entry \(a:z/d\) means

\[
H_a(z)\equiv0\pmod5,
\qquad
H_a'(z)\equiv d\not\equiv0\pmod5.
\]

For example, the exceptional phase \(48\) has

\[
5^{-4}F_{48}(z)
\equiv
2z(z+2)
\pmod5,
\tag{14}
\]

so its two zeros \(0\) and \(3\) are simple. Phase \(672\) has

\[
5^{-3}F_{672}(z)\equiv3z\pmod5.
\tag{15}
\]

All \(25\) root-bearing phases in the first row have one simple affine
zero. Thus the inverse-limit zero set has

\[
25+1+2=28
\tag{16}
\]

points.

## 3. Exact high-precision density

In Lemma 1, take

\[
p=5,\qquad c=2.
\]

The three rows of (13) contribute respectively

\[
25\cdot5^{2-2}=25,
\qquad
1\cdot5^{3-2}=5,
\qquad
2\cdot5^{4-2}=50.
\tag{17}
\]

### Theorem 2 (stable Hensel tail)

For every \(k\geq5\), exactly \(80\) classes in one period

\[
L_k=156\cdot5^{k-1}
\]

satisfy \(5^k\mid D_r\). Hence

\[
\boxed{
\delta_k
=
\frac{80}{156\cdot5^{k-1}}
=
\frac4{39\cdot5^{k-2}}
}
\qquad(k\geq5).
\tag{18}
\]

The intersection of all successful clopen sets consists of the \(28\)
points in (16), and therefore has Haar measure zero.

### Proof

The first assertion is (5) and (17). Division by the period gives (18).
Each simple root in (13) has one compatible lift in \(\mathbf Z_5\), so
there are \(28\) inverse-limit points. The phase-coordinate presentation is
the disjoint union of \(780\) copies of \(\mathbf Z_5\); equivalently, the
clock itself is
\(\mathbf Z/156\mathbf Z\times\mathbf Z_5\). A finite subset has Haar
measure zero.
\(\square\)

The count \(80\) is therefore not evidence that \(80\) simple roots have
stabilized. At finite precision the \(28\) roots carry the Hensel weights
\(1\), \(5\), and \(25\).

## 4. The all-precision partition polynomial

Let

\[
d_{k,r}=\min\{k,v_5(D_r)\}
\]

and let \(Z_k(u)\) be its valuation partition polynomial over one period
\(L_k\). The precision-\(5^5\) calculation gave

\[
(N_0,N_1,N_2,N_3,N_4,N_5)
=
(80000,13500,3000,725,195,80).
\tag{19}
\]

For \(j<5\), passing from precision \(k\) to \(k+1\) simply repeats every
class five times. For \(5\leq j<k\), Theorem 2 gives

\[
\#\{r:v_5(D_r)\geq j\}=80\cdot5^{k-j}
\]

on the precision-\(k\) clock. Successive subtraction now yields the
complete formula.

### Corollary 3

For every \(k\geq5\),

\[
\boxed{
\begin{aligned}
Z_k(u)
={}&
5^{k-5}
\left(
80000+13500u+3000u^2+725u^3+195u^4
\right)\\
&+
\sum_{j=5}^{k-1}
320\cdot5^{k-j-1}u^j
+80u^k.
\end{aligned}
}
\tag{20}
\]

In the inverse limit, the exact valuation has rational probability
generating function

\[
\boxed{
\begin{aligned}
\mathcal Z(u)
={}&
\frac{32}{39}
+\frac9{65}u
+\frac2{65}u^2
+\frac{29}{3900}u^3
+\frac1{500}u^4\\
&+
\frac{16u^5}{24375(1-u/5)}.
\end{aligned}
}
\tag{21}
\]

Its mean and variance are

\[
\boxed{
\mathbf E[v_5(D)]=\frac{61}{260},
\qquad
\operatorname{Var}(v_5(D))=\frac{66577}{202800}.
}
\tag{22}
\]

### Proof

Equation (20) follows from the preceding threshold counts. Dividing its
coefficients by \(L_k\) and taking \(k\to\infty\) gives (21); for
\(j\geq5\),

\[
\Pr(v_5(D)=j)
=
\frac{16}{39\cdot5^{j-1}}.
\tag{23}
\]

Finally,

\[
\mathbf E[v]=\sum_{h\geq1}\Pr(v\geq h),
\qquad
\mathbf E[v^2]
=
\sum_{h\geq1}(2h-1)\Pr(v\geq h).
\]

Substitution of the four low-precision densities and the geometric tail
(18) gives

\[
\mathbf E[v]=\frac{61}{260},
\qquad
\mathbf E[v^2]=\frac{23}{60},
\]

which proves (22). \(\square\)

## 5. LTE, Hensel, and CRT as an assembly line

Three classical operations now have distinct roles.

1. **Lifting the exponent.** The matrix identity
   \[
   v_5(C^mx-x)=v_5(m)+2
   \]
   forces each additional precision digit to multiply the recurrence
   period by \(5\).
2. **Hensel lifting.** Once the clock is available, Lemma 1 classifies the
   nested successful classes and their weights.
3. **Chinese remaindering.** After local filters have been computed at
   distinct primes, CRT recombines compatible local residue classes for a
   composite modulus. It does not replace either of the first two steps.

This is the precise sense in which supercongruence can be used as a
reusable selection tool. The reusable object is a filtered family of local
conditions equipped with a lift law, not an ultrafilter and not a claim of
statistical independence between primes.

## 6. Verification and literature boundary

The checker
[`verify_hensel_valuation_filter.py`](../verification/related/verify_hensel_valuation_filter.py)
verifies:

1. all \(780\) phase classes modulo \(25\);
2. the \(32\)-phase content classification in (13);
3. every displayed zero and nonzero derivative;
4. the weighted count \(80\);
5. the complete partition polynomial at precision \(5^7\); and
6. the limiting generating function, mean, and variance.

Run:

```text
python verification/related/verify_hensel_valuation_filter.py
```

Relevant literature:

- E. Rowland and R. Yassawi,
  [\(p\)-adic asymptotic properties of constant-recursive
  sequences](https://arxiv.org/abs/1602.00176), prove analytic approximate
  twisted interpolation for constant-recursive sequences and relate
  high-precision residue behavior to Haar measure. Their framework is the
  natural general setting for (10)--(12).
- B. Poonen,
  [\(p\)-adic interpolation of iterates](https://doi.org/10.1112/blms/bdu010),
  gives a general analytic interpolation theorem for iterates sufficiently
  close to the identity.
- [Precision lifting and a \(p\)-adic valuation
  expansion](PadicValuationExpansion.md), for the unit-root factor, matrix
  period certificate, and the precision-\(5^5\) and \(5^6\) data used here.

The cited interpolation results are general infrastructure. The exact
weighted phase table and formula (20) are the specific arithmetic content
of this note.
