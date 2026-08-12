# A uniform rational diagonal for every row of A331562

**Status:** exact reduction of the named cubic tower; the transfer-matrix
identity is proved below and exact checks pass; the cubic Cartier estimate
in (12) remains open

[OEIS A331562](https://oeis.org/A331562) counts words with `k` copies of
each letter in `{1,...,d}` such that consecutive letters differ by at most
one.  The record conjectures that every fixed-`d` row satisfies

```math
a_d(np^r)\equiv a_d(np^{r-1})\pmod {p^{3r}}
\qquad(p\ge5).
\tag{1}
```

Rows `d=2,3,4` reduce to familiar binomial or Apery-type sequences.  This
note gives one representation that is uniform in `d`.  It turns the
remaining conjecture into a finite rational-function coefficient estimate,
rather than a search for a separate binomial sum for each row.

## 1. The weighted language

Let `A_d` be the `d` by `d` zero-one matrix

```math
(A_d)_{ij}=1_{|i-j|\le1},
```

let `J_d` be the all-one matrix, and put

```math
X=\operatorname{diag}(x_1,\ldots,x_d).
```

For a word `w=w_1\cdots w_m`, write
`x^w=x_{w_1}\cdots x_{w_m}`.  Define the multivariate generating function

```math
F_d(x_1,\ldots,x_d)
=1+\sum_{m\ge1}\ \sum_{\substack{w\in\{1,\ldots,d\}^m\\
|w_{j+1}-w_j|\le1}}x^w.
\tag{2}
```

### Theorem 1 (uniform determinant ratio)

For every `d>=1`,

```math
\boxed{
F_d(x)=
\frac{N_d(x)}{D_d(x)}
=
\frac{\det(I-(A_d-J_d)X)}{\det(I-A_dX)}.
}
\tag{3}
```

Consequently,

```math
\boxed{
a_d(k)=[x_1^k\cdots x_d^k]F_d(x).
}
\tag{4}
```

### Proof

The total weight of the nonempty admissible words of length `m` is

```math
\boldsymbol 1^T X(A_dX)^{m-1}\boldsymbol 1.
```

Summing the geometric series gives

```math
F_d=1+\boldsymbol 1^T X(I-A_dX)^{-1}\boldsymbol 1.
\tag{5}
```

Apply the matrix determinant lemma to `B=I-A_dX`,
`u=\boldsymbol 1`, and `v^T=\boldsymbol 1^TX`:

```math
\det(B+uv^T)=\det(B)(1+v^TB^{-1}u).
```

Since

```math
B+uv^T=I-A_dX+J_dX=I-(A_d-J_d)X,
```

(3) follows.  Extracting the monomial in which every letter occurs exactly
`k` times proves (4).  QED

## 2. A continuant denominator

The denominator in (3) is especially small.  Let `D_j` denote the leading
`j` by `j` determinant, with `D_0=1`.  Tridiagonal expansion gives

```math
D_1=1-x_1,
\qquad
D_j=(1-x_j)D_{j-1}-x_{j-1}x_jD_{j-2}.
\tag{6}
```

Thus the entire infinite row family is encoded by a numerator determinant
and a second-order continuant.  For example,

```math
F_2=\frac1{1-x_1-x_2},
\tag{7}
```

whose diagonal is the central binomial sequence.  For `d=3`,

```math
F_3=
\frac{1-x_1x_3}
{1-x_1-x_2-x_3+x_1x_3+x_1x_2x_3}.
\tag{8}
```

Its diagonal begins `1,2,12,92,780,...`, the row A103882.  Formula (3)
continues without a change of language or a guessed hypergeometric identity
for every `d`.

## 3. Exact Frobenius reduction

Write `x^p=(x_1^p,...,x_d^p)`.  From (4), for every positive integer `K`,

```math
a_d(pK)-a_d(K)
=[x_1^{pK}\cdots x_d^{pK}]
\left(F_d(x)-F_d(x^p)\right).
\tag{9}
```

Using (3), the difference is the explicit rational function

```math
F_d(x)-F_d(x^p)
=\frac{R_{d,p}(x)}{D_d(x)D_d(x^p)},
\tag{10}
```

where the finite Frobenius numerator is

```math
R_{d,p}(x)
=N_d(x)D_d(x^p)-N_d(x^p)D_d(x).
\tag{11}
```

Therefore the A331562 conjecture is equivalent to the single uniform
estimate

```math
v_p\!\left(
[x_1^{np^r}\cdots x_d^{np^r}]
\frac{R_{d,p}(x)}{D_d(x)D_d(x^p)}
\right)\ge3r
\tag{12}
```

for every `d,n,r>=1` and prime `p>=5`.

Equation (12) is the remaining obligation.  The rational-diagonal
representation by itself does **not** prove a cubic supercongruence: generic
rational diagonals have only the ordinary Frobenius/Dwork depth.  A proof
must exploit the path-continuant structure in (6), or an equivalent
cancellation in (11).

## 4. Exact verification

[`verify_a331562_uniform_rational_diagonal.py`](../verification/related/verify_a331562_uniform_rational_diagonal.py)
checks independently that:

1. the determinant denominator agrees with the continuant (6);
2. the formal identity `D_d F_d=N_d` holds coefficientwise in finite boxes;
3. diagonal extraction reproduces the OEIS rows through `d=6`;
4. direct word dynamic programming agrees with (4); and
5. sampled cubic towers for the first previously untreated rows have the
   asserted valuation, including sharp cases.

These checks support the reduction and guard its indexing.  They are not a
proof of (12).

## 5. Source boundary

- The counting problem and the all-row conjecture are from
  [OEIS A331562](https://oeis.org/A331562).
- The use of a transfer matrix and the matrix determinant lemma is standard;
  no priority claim is made for (3).
- The OEIS page identifies rows `2`, `3`, and `4` with previously treated
  sequences.  The result here is the uniform rational model and exact
  obstruction for arbitrary row number.
- No theorem about arbitrary rational diagonals is invoked to claim (1).

