# One Cartier-square obstruction behind four cubic Euler-product towers

**Status:** exact all-level reduction; every logarithmic term of degree at
least three is discharged; the two weighted moments reduce further to one
coefficientwise Cartier-square estimate, which remains to be proved

This note sharpens the quadratic baseline in
[the modular-product packet](ModularProductPrimeCoefficientPacket.md) for
the conjectures attached to
[A023871](https://oeis.org/A023871),
[A023873](https://oeis.org/A023873),
[A206622](https://oeis.org/A206622), and
[A283271](https://oeis.org/A283271).  The four conjectures are not four
unrelated problems.  After one Frobenius factorization, all of them first
reduce to the same two coefficient estimates, and a second exact argument
reduces those two estimates to one unweighted Cartier-square condition.

The reduction is exact.  It is not a proof of the final Cartier-square
condition, and the four records therefore remain classified `partial`.

## 1. The four products

For a finite list

```math
\mathscr S=((\epsilon_\nu,h_\nu,d))_\nu,
\qquad \epsilon_\nu\in\{1,-1\},\quad h_\nu\in\mathbb Z,
\tag{1}
```

in which the degree `d` is common, put

```math
G_{\mathscr S}(x)
=\prod_{\nu}\prod_{m\ge1}
(1-\epsilon_\nu x^m)^{h_\nu m^d}.
\tag{2}
```

The four source products are obtained from

```math
\begin{array}{c|c|c}
\text{record}&\mathscr S&d\\ \hline
\text{A023871}&((1,-1,2))&2\\
\text{A023873}&((1,-1,4))&4\\
\text{A206622}&((-1,1,2),(1,-1,2))&2\\
\text{A283271}&((1,1,4))&4.
\end{array}
\tag{3}
```

For an integer framing parameter `c`, define

```math
a_c(N)=[x^N]G_{\mathscr S}(x)^{cN}.
\tag{4}
```

This is the form used in the live OEIS conjectures.  Negative `c` causes no
problem: all calculations take place in the ring of formal power series.
The case `c=0` is identically constant and hence trivial; below, whenever
`v_p(c)` is written, we assume `c` is nonzero.

## 2. The reduced Frobenius logarithm

Fix an odd prime `p` and write

```math
\Lambda_p(x)
=\log G_{\mathscr S}(x)-\frac1p\log G_{\mathscr S}(x^p).
\tag{5}
```

Let `C_p` be the Cartier operator

```math
C_p\!\left(\sum_{n\ge0}u_nx^n\right)
=\sum_{n\ge0}u_{pn}x^n.
\tag{6}
```

### Lemma 1 (integrality and exact Cartier scaling)

The series `Lambda_p` belongs to `x Z_(p)[[x]]`, and

```math
\boxed{C_p(\Lambda_p)=p^d\Lambda_p.}
\tag{7}
```

#### Proof

Expand one logarithm as

```math
-h\sum_{m,j\ge1}\frac{m^d\epsilon^j}{j}x^{mj}.
```

There is a more useful exact cancellation.  In the first logarithm, the
terms with `p|j` are precisely the terms removed by the second logarithm:
because `p` is odd, `epsilon^(pj)=epsilon^j`.  Hence

```math
\boxed{
\Lambda_p(x)
=-\sum_\nu h_\nu\sum_{m\ge1}
 \sum_{\substack{j\ge1\\p\nmid j}}
 \frac{m^d\epsilon_\nu^j}{j}x^{mj}.}
\tag{7a}
```

Every denominator in (7a) is a `p`-adic unit, which proves integrality
directly.  Moreover, applying `C_p` to (7a) forces `p|m`; replacing `m` by
`pm` supplies exactly a factor `p^d`.  Thus

```math
\boxed{C_p(\Lambda_p)=p^d\Lambda_p.}
\tag{7}
```

This is additive over the list (1).  QED

For the reciprocal one-color products this can also be read coefficient by
coefficient.  If `n=p^a u` and `p` does not divide `u`, then, up to the
fixed sign in (2),

```math
[x^n]\Lambda_p=p^{da}\frac{\sigma_{d+1}(u)}{u}.
\tag{8}
```

Thus (7) is literal scaling, not merely a congruence.

## 3. Exact adjacent-level identity

Put `N=n p^(r-1)` and `e=v_p(N)`.  Equation (5) gives

```math
G(x)^{cpN}=G(x^p)^{cN}\exp(cpN\Lambda_p(x)).
\tag{9}
```

Taking the coefficient of `x^(pN)` and applying (6) gives the exact
identity

```math
\boxed{
a_c(pN)-a_c(N)
=\sum_{k\ge1}\frac{(cpN)^k}{k!}
[x^N]G(x)^{cN}C_p(\Lambda_p^k).}
\tag{10}
```

Only finitely many summands affect the coefficient in (10).

### Lemma 2 (the logarithmic tail is already cubic)

If `p>=5`, every term of (10) with `k>=3` is divisible by

```math
p^{3(e+1)}.
\tag{11}
```

#### Proof

Both `G^(cN)` and every `C_p(Lambda_p^k)` are `p`-integral.  If
`q=v_p(c)`, the scalar in the `k`-th term has valuation at least

```math
k(e+q+1)-v_p(k!).
```

For `p>=5` this is at least `3(e+1)` for every `k>=3`: the case `k=3`
is immediate, and for `k>=4` use
`v_p(k!) <= (k-1)/(p-1) <= k-3`.  QED

Therefore no cubic proof needs estimates for the infinite logarithmic
tail.  Only `k=1,2` survive.

## 4. The two-moment criterion

Define

```math
M_1(p,N,c)=[x^N]G(x)^{cN}\Lambda_p(x),
\tag{12}
```

and

```math
M_2(p,N,c)=[x^N]G(x)^{cN}C_p(\Lambda_p(x)^2).
\tag{13}
```

By Lemmas 1 and 2, (10) becomes

```math
a_c(pN)-a_c(N)
\equiv
cp^{d+1}N M_1(p,N,c)
+\frac{c^2p^2N^2}{2}M_2(p,N,c)
\pmod {p^{3(e+1)}}.
\tag{14}
```

### Theorem 3 (cubic Cartier-moment criterion)

Let `p>=5`, `q=v_p(c)`, and `e=v_p(N)`.  The adjacent cubic congruence

```math
a_c(pN)\equiv a_c(N)\pmod {p^{3(e+1)}}
\tag{15}
```

follows from the two estimates

```math
v_p(M_1(p,N,c))\ge
\max\{0,\,2e+2-d-q\},
\tag{16}
```

and

```math
v_p(M_2(p,N,c))\ge
\max\{0,\,e+1-2q\}.
\tag{17}
```

This is immediate from (14).  In the hardest unit-framing, degree-two
case, (16)--(17) read

```math
v_p(M_1)\ge2e,
\qquad
v_p(M_2)\ge e+1.
\tag{18}
```

This already reduces the full OEIS towers to two weighted moments, not to
an uncontrolled exponential expansion.  The next theorem removes the
linear moment and the weight from the remaining obligation.

## 5. Collapse to one coefficientwise obstruction

Put

```math
Q_p(x)=C_p(\Lambda_p(x)^2).
```

Consider the coefficientwise estimate

```math
\boxed{
v_p([x^j]Q_p)\ge v_p(j)+1
\quad(j\ge1).}
\tag{19}
```

This is stronger than mere divisibility of `Q_p` by `p`, but it is
unweighted: neither `N` nor the framing parameter `c` occurs in it.

### Formal-derivative interpretation

Let

```math
\theta=x\frac{d}{dx}.
```

For an integral `p`-adic series `F(x)=sum_(n>=1) f_n x^n`, the elementary
coefficient criterion

```math
F\in\theta\mathbb Z_p[[x]]
\quad\Longleftrightarrow\quad
v_p(f_n)\ge v_p(n)\quad(n\ge1)
\tag{19a}
```

says exactly when `F` has an integral Euler antiderivative.  This is the
one-variable case of the formal-derivative criterion used by Beukers and
Vlasenko in
[Dwork Crystals I](https://doi.org/10.1093/imrn/rnaa119), Lemmas 2.2 and
3.1.  Since the coefficient of `x^j` in `C_p(Lambda_p^2)` is the
coefficient of `x^(pj)` in `Lambda_p^2`, integrality handles indices prime
to `p` and (19) is equivalent to

```math
\boxed{\Lambda_p(x)^2\in\theta\mathbb Z_p[[x]].}
\tag{19b}
```

Equivalently, the iterated Cartier criterion in the same reference reads

```math
C_p^s(\Lambda_p^2)\in p^s\mathbb Z_p[[x]]
\qquad(s\ge1).
\tag{19c}
```

Thus the last obstruction is not merely a first-layer congruence.  It is
the vanishing of `Lambda_p^2` in the one-variable formal de Rham quotient.
This reformulation does not prove that vanishing, but it identifies the
precise cohomological statement that a modular-form or Lambert-series
argument must establish.

### Lemma 4 (coefficients of a large integral power)

Let `H(x)` belong to `1+x Z_(p)[[x]]`, let `A` be a nonzero integer, and
put `E=v_p(A)`.  Then, for every `m>=1`,

```math
v_p([x^m]H(x)^A)\ge
\max\{0,E-v_p(m)\}.
\tag{20}
```

#### Proof

Write `A=p^E u` and replace `H` by `H^u`; this is still an integral unit
series even when `u` is negative.  The elementary Frobenius congruence

```math
H(x)^{p^E}\equiv H(x^p)^{p^{E-1}}\pmod {p^E}
```

follows by raising `H(x)^p=H(x^p)+pR(x)` to the power `p^(E-1)`.
Induction on `E` now proves (20): if `p` does not divide `m`, the comparison
series has no `x^m` term; if `p` divides `m`, its `x^m` coefficient is the
coefficient at `m/p` one level lower.  QED

### Theorem 5 (one-obstruction criterion)

Assume `d>=2`, `p>=5`, and (19).  Then both estimates (16)--(17) hold for
every nonzero integral framing `c` and every `N>=1`.  Consequently the full
adjacent cubic congruence (15) holds.

#### Proof

Write

```math
G(x)^{cN}=\sum_{m\ge0}h_mx^m,
\qquad
Q_p(x)=\sum_{j\ge1}q_jx^j,
```

and put `e=v_p(N)`, `q=v_p(c)`.  Then

```math
M_2=\sum_{j=1}^{N}h_{N-j}q_j.
```

If `v_p(j)=t<e`, then `v_p(N-j)=t`.  Lemma 4 and (19) give

```math
v_p(h_{N-j}q_j)\ge(e+q-t)+(t+1)\ge e+1.
```

If `t>=e`, condition (19) alone gives the same bound.  Hence the stronger
uniform estimate

```math
v_p(M_2)\ge e+1
\tag{21}
```

holds, and in particular implies (17).

It remains to recover `M_1`.  When `e=0`, its required bound is just
integrality.  If `e>=1`, factor (9) with `N` in place of `pN`, extract the
coefficient of degree `N`, and use (7).  This gives the exact recursion

```math
\begin{aligned}
M_1(p,N,c)
={}&p^dM_1(p,N/p,c)+cN M_2(p,N/p,c)\\
&+\sum_{k\ge2}\frac{(cN)^k}{k!}
[x^{N/p}]G(x)^{cN/p}C_p(\Lambda_p^{k+1}).
\end{aligned}
\tag{22}
```

The first term has the required valuation by induction and `d>=2`.  The
second has valuation at least `e+q+e`, by (21) one level lower.  Every tail
term has valuation at least `k(e+q)-v_p(k!)>=2e`; here `p>=5`, `e>=1`, and
`k>=2`.  These three bounds imply (16).  Theorem 3 now proves (15).  QED

Thus the four OEIS towers no longer have two independent weighted
obligations.  They have one common coefficientwise obligation, (19).

## 6. The quadratic Cartier boundary

The first necessary contraction behind (17) is

```math
C_p(\Lambda_p^2)\in p\mathbb Z_{(p)}[[x]].
\tag{23}
```

Exact arithmetic exhibits the source prime ranges cleanly:

- for A023871, (23) holds throughout the checked range for `p>=7` and
  fails already at `p=5`;
- for A206622, the plus/minus combination restores (23) at `p=5`;
- for the two degree-four products, (23) holds in the checked range already
  at `p=5`, although the live OEIS statements only ask for `p>=7`.

The failure for A023871 is not cosmetic.  Its adjacent differences at
`p=5` attain valuations `2,5` at the first two levels rather than the
cubic targets `3,6`.  Conversely, the exact checks suggest that the two
degree-four conjectures may extend from `p>=7` to `p>=5`; `p=3` fails at
the first level.

These observations are not promoted to theorems.  The stronger stratum
estimate (19), rather than (23) alone, is what supplies all further powers
in the weighted coefficient.  This is precisely the horizontal scalar
cancellation that the coefficientwise colored theorem cannot see.

## 7. What is now finished and what is not

The following obligations are closed uniformly for all four records:

1. the Frobenius factorization;
2. `p`-integrality of the reduced logarithm;
3. exact Cartier scaling (7);
4. every logarithmic degree `k>=3`;
5. reduction of every adjacent level and every integral framing parameter
   to (16)--(17); and
6. reduction of both weighted moments to the single coefficientwise
   estimate (19).

What remains is one common **Cartier-square lemma**: prove (19) for the
constant exponent profiles in (3), with the stated prime ranges.  A proof
may use the Eisenstein-series descriptions

```math
n[x^n]\log G=\pm\sigma_3(n),\quad
\pm\sigma_5(n),\quad\text{or}\quad
\frac{\sigma_3(2n)-\sigma_3(n)}4.
\tag{24}
```

Theorem 5 shows that no further weighted estimate is then necessary.

The two degree-four records have opposite logarithms, so their squares and
hence their remaining obstruction are literally identical.  Consequently
only three profile calculations remain: the reciprocal degree-two profile,
its plus/minus level-two modification, and the common degree-four profile.

## 8. Verification and source boundary

The exact checker
[`verify_euler_product_cubic_cartier_moments.py`](../verification/related/verify_euler_product_cubic_cartier_moments.py)

1. verifies the depleted expansion (7a) and exact scaling (7) for all four
   products;
2. verifies (14) directly against the defining Euler products;
3. checks the two moment bounds on several `p`-adic strata;
4. checks the large-power coefficient lemma and the recursion (22);
5. checks the stronger estimate (19) coefficientwise on several strata;
6. checks (23) coefficientwise through a finite but broad degree range;
7. records the sharp A023871 failure at `p=5`; and
8. records the degree-four `p=5` evidence and `p=3` failure.

The conjectures and product definitions come from the four linked OEIS
pages.  Searches of the cited Euler-product, Gauss-congruence, and Dwork
literature did not locate a theorem that directly proves (19).
That negative search is not a priority claim.
