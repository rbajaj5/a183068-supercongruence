# One Cartier defect for three exponential-coefficient records

**Status:** complete formal reduction for A060941, A362722, and A362733;
the identities and named specializations pass exact checks; the required
quadratic and cubic estimates on the Cartier defect remain open

Three records in the Bala census are defined by coefficients of powers of
Euler transforms:

- [A060941](https://oeis.org/A060941), including its iterated exponential
  family;
- [A362722](https://oeis.org/A362722), built from the odd-indexed Apery
  numbers; and
- [A362733](https://oeis.org/A362733), the second exponential iterate of the
  central trinomial factorial ratio.

The definitions look different, but their adjacent-level differences have
one exact form.

## 1. Universal exponential coefficients

Let `b_1,b_2,...` be rational numbers and set

```math
L_b(x)=\sum_{m\ge1}\frac{b_m}{m}x^m,
\qquad
E_b(x)=\exp L_b(x).
\tag{1}
```

For integers `c`, positive `s,N`, define

```math
T_{b;c,s}(N)=[x^{sN}]E_b(x)^{cN}.
\tag{2}
```

Let the Cartier operator be

```math
\mathcal C_p\left(\sum_{m\ge0}f_mx^m\right)
=\sum_{m\ge0}f_{pm}x^m.
\tag{3}
```

Finally define the Frobenius logarithm

```math
\Delta_{p,b}(x)=pL_b(x)-L_b(x^p).
\tag{4}
```

Its coefficients are completely explicit:

```math
\Delta_{p,b}(x)
=\sum_{p\nmid m}\frac{pb_m}{m}x^m
+\sum_{j\ge1}\frac{b_{pj}-b_j}{j}x^{pj}.
\tag{5}
```

The second sum is where Gauss or supercongruence information about the
source sequence enters.  The first sum is the off-Frobenius lattice and
cannot be discarded termwise.

### Theorem 1 (exact Cartier-defect identity)

For every prime `p` and all parameters for which the formal series are
defined,

```math
\boxed{
T_{b;c,s}(pN)-T_{b;c,s}(N)
=
[x^{sN}]E_b(x)^{cN}
\left(
\mathcal C_p\!\left(e^{cN\Delta_{p,b}(x)}\right)-1
\right).
}
\tag{6}
```

### Proof

Equation (4) gives

```math
E_b(x)^{cpN}
=E_b(x^p)^{cN}e^{cN\Delta_{p,b}(x)}.
\tag{7}
```

If `G` is any series, the elementary Cartier product rule is

```math
\mathcal C_p(F(x^p)G(x))=F(x)\mathcal C_p(G(x)).
\tag{8}
```

Take the coefficient of `x^(spN)` in (7), apply (8), and subtract the
coefficient at level `N`.  This proves (6).  QED

Thus no asymptotic, convergence, or analytic logarithm is involved: (6) is
an identity of formal power series over `Q`.

## 2. The exact proof obligation

Define

```math
\Theta_{p,b;c,N}(x)
=\mathcal C_p\!\left(e^{cN\Delta_{p,b}(x)}\right)-1.
\tag{9}
```

A proposed adjacent tower of depth `h(r)` for (2) is exactly the assertion

```math
v_p\left(
[x^{sn}]E_b(x)^{cn}\Theta_{p,b;c,n}(x)
\right)\ge h(r),
\qquad n=mp^{r-1}.
\tag{10}
```

This is stronger information than the ordinary integrality criterion for
`E_b`: a Gauss congruence controls the second sum in (5), but the first sum
can contribute through collections of off-grid exponents whose total is a
multiple of `p`.  Those Cartier cancellations are the unresolved part.

## 3. A060941

The exponential formula on the OEIS page is

```math
A(x)=E_b(x),
\qquad
b_m=\frac15\binom{5m}{2m}.
\tag{11}
```

Therefore the page's family

```math
[x^{sN}]A(x)^{cN}
```

is exactly `T_{b;c,s}(N)`, and its conjectured cubic tower is precisely
(10) with `h(r)=3r` for `p>=7`.

The lower prime is genuinely excluded:

```math
T_{b;1,1}(5)-T_{b;1,1}(1)=1300725=5^2\cdot52029.
\tag{12}
```

The same statement is stable under the page's recursive construction. If
`b^(0)_m` is the A060941 sequence and

```math
b^{(i+1)}_N=T_{b^{(i)};1,1}(N),
\tag{13}
```

then Theorem 1 applies at every iteration with `b=b^(i)`.  The iterates need
not be integral: the next generation already begins
`1,2,31,620,13951,1345389/4,...`.  The conjectured primes `p>=7` do not see
the displayed denominator, but any proof must retain denominator valuations
at later stages.  The identity proves a uniform reduction of the nonlinear
family; it does not prove that the valuation hypothesis propagates from one
iteration to the next.

## 4. A362722

Let `A_2(m)` denote A005258. Put

```math
b_m=
\begin{cases}
2A_2(m),&m\text{ odd},\\
0,&m\text{ even}.
\end{cases}
\tag{14}
```

The OEIS definition is exactly

```math
a(N)=T_{b;1,1}(N).
\tag{15}
```

Consequently its three conjectures become the same coefficient (10), with
the required depth respectively `2r+1` on `N=p^(r-1)`, `2` at the first
general level, and `2r` at later general levels.  The special support on odd
indices is preserved by every odd prime, but that support fact alone does
not prove the Cartier estimate.

## 5. A362733

Let

```math
b_m=\frac{(3m)!}{m!^3}.
\tag{16}
```

The alternative formula on the OEIS page gives, for `N>=1`,

```math
a(N)=\frac12T_{b;2,1}(N).
\tag{17}
```

Because `2` is a unit at every prime in the conjectured range, the desired
`p^(3r)` tower for `p>=3` is equivalent to (10) with `c=2,s=1,h(r)=3r`.
For `p>=5`, the source factorial ratio already has a cubic adjacent tower;
equation (5) shows exactly how that information enters.  The ternary case
and the off-grid Cartier cancellation still require separate proof.

## 6. Exact verification

[`verify_exponential_coefficient_cartier.py`](../verification/related/verify_exponential_coefficient_cartier.py)
uses rational formal-series arithmetic to check:

1. (5) directly from the two logarithms;
2. the universal identity (6) for unrelated synthetic source sequences;
3. the A060941 exponential formula against its published initial terms;
4. the A362722 and A362733 specializations against their OEIS initial terms;
5. one explicit A060941 exponential iteration; and
6. sampled conjectural towers, including the `p=3` boundary of A362733 and
   sharp cases.

The checks certify the algebraic reduction, not the unbounded estimates in
(10).

## 7. Source boundary

- Definitions and conjectured exponents are taken from the three linked
  OEIS pages.
- Formal Euler transforms and Cartier operators are classical.
- Straub's multivariate supercongruence theorem explains the source Apery
  and factorial-ratio inputs, but it does not state that the nonlinear
  operation (2) preserves a cubic exponent.
- No priority claim is made for Theorem 1 or for this packaging.
