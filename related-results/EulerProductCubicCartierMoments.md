# The two Cartier moments behind four cubic Euler-product towers

**Status:** exact all-level reduction; every logarithmic term of degree at
least three is discharged; two explicit weighted Cartier moments remain to
be proved

This note sharpens the quadratic baseline in
[the modular-product packet](ModularProductPrimeCoefficientPacket.md) for
the conjectures attached to
[A023871](https://oeis.org/A023871),
[A023873](https://oeis.org/A023873),
[A206622](https://oeis.org/A206622), and
[A283271](https://oeis.org/A283271).  The four conjectures are not four
unrelated problems.  After one Frobenius factorization, all of them reduce
to the same two coefficient estimates.

The reduction is exact.  It is not a proof of those two estimates, and the
four records therefore remain classified `partial`.

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

The coefficient of `x^n` in (5) is `p`-integral: if `p` divides `n`,
the two ghost coefficients differ by a complete new `p`-divisor stratum;
if `p` does not divide `n`, its denominator is a unit.

For (7), apply `C_p` and split `p | mj` into `p | m` and
`p | j` with `p` not dividing `m`.  The first part is `p^d log G(x)`.
The second part, after subtracting `(1/p) log G(x)`, removes exactly the
`p | m` portion, namely `p^(d-1) log G(x^p)`.  The result is

```math
p^d\log G(x)-p^{d-1}\log G(x^p)=p^d\Lambda_p(x).
```

The same calculation is valid for `epsilon=-1` because `p` is odd, and it
is additive over the list (1).  QED

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

The full OEIS towers are therefore reduced to two weighted moments, not to
an uncontrolled exponential expansion.

## 5. The quadratic Cartier boundary

The first necessary contraction behind (17) is

```math
C_p(\Lambda_p^2)\in p\mathbb Z_{(p)}[[x]].
\tag{19}
```

Exact arithmetic exhibits the source prime ranges cleanly:

- for A023871, (19) holds throughout the checked range for `p>=7` and
  fails already at `p=5`;
- for A206622, the plus/minus combination restores (19) at `p=5`;
- for the two degree-four products, (19) holds in the checked range already
  at `p=5`, although the live OEIS statements only ask for `p>=7`.

The failure for A023871 is not cosmetic.  Its adjacent differences at
`p=5` attain valuations `2,5` at the first two levels rather than the
cubic targets `3,6`.  Conversely, the exact checks suggest that the two
degree-four conjectures may extend from `p>=7` to `p>=5`; `p=3` fails at
the first level.

These observations are not promoted to theorems.  Even (19) alone is not
enough at higher levels: after dividing it by `p`, the weighted coefficient
in (17) still has to supply `e` further powers.  This is precisely the
horizontal scalar cancellation that the coefficientwise colored theorem
cannot see.

## 6. What is now finished and what is not

The following obligations are closed uniformly for all four records:

1. the Frobenius factorization;
2. `p`-integrality of the reduced logarithm;
3. exact Cartier scaling (7);
4. every logarithmic degree `k>=3`; and
5. reduction of every adjacent level and every integral framing parameter
   to (16)--(17).

What remains is one common **Cartier-moment lemma**: prove (16)--(17) for
the constant exponent profiles in (3), with the stated prime ranges.  A
proof may use the Eisenstein-series descriptions

```math
n[x^n]\log G=\pm\sigma_3(n),\quad
\pm\sigma_5(n),\quad\text{or}\quad
\frac{\sigma_3(2n)-\sigma_3(n)}4,
\tag{20}
```

but it must control the weighted coefficient after multiplication by
`G^(cN)`.  A congruence for the ghost coordinates alone does not supply
that step.

## 7. Verification and source boundary

The exact checker
[`verify_euler_product_cubic_cartier_moments.py`](../verification/related/verify_euler_product_cubic_cartier_moments.py)

1. verifies the exact scaling (7) for all four products;
2. verifies (14) directly against the defining Euler products;
3. checks the two moment bounds on several `p`-adic strata;
4. checks (19) coefficientwise through a finite but broad degree range;
5. records the sharp A023871 failure at `p=5`; and
6. records the degree-four `p=5` evidence and `p=3` failure.

The conjectures and product definitions come from the four linked OEIS
pages.  Searches of the cited Euler-product, Gauss-congruence, and Dwork
literature did not locate a theorem that directly proves (16)--(17).
That negative search is not a priority claim.
