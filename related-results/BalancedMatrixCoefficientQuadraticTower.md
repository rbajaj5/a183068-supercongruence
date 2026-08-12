# Balanced matrix coefficients and the A124435 quadratic tower

**Status:** complete elementary proof candidate; exact checks pass;
literature priority is not established

This note proves the supercongruence conjectured on
[OEIS A124435](https://oeis.org/A124435).  The proof has two layers:

1. a coefficientwise quadratic Frobenius theorem for weighted balanced
   contingency tables; and
2. an Eisenstein matrix whose Frobenius twist is either itself or its
   transpose.

The second layer explains why a rational one-block diagonal can satisfy a
quadratic tower even though the general one-block family in Straub's
framework does not.

## 1. Balanced matrix coefficients

Let `d >= 1`, let `A=(a_ij)` be a `d` by `d` matrix of commuting
indeterminates, and define

```math
\mathcal F_N(A)=
[x_1^N\cdots x_d^N]
\prod_{i=1}^{d}\left(\sum_{j=1}^{d}a_{ij}x_j\right)^N.
\tag{1}
```

If `B=(b_ij)` is a nonnegative integral matrix whose row sums and column
sums all equal `N`, write

```math
M(B)=\prod_{i=1}^{d}
\binom{N}{b_{i1},\ldots,b_{id}},
\qquad
A^B=\prod_{i,j}a_{ij}^{b_{ij}}.
```

Expanding the linear forms gives

```math
\mathcal F_N(A)=\sum_B M(B)A^B.
\tag{2}
```

For a prime `p`, let `A^[p]=(a_ij^p)` denote entrywise Frobenius, not a
matrix power.

### Theorem 1 (balanced-matrix quadratic tower)

Let `p >= 5` be prime and `n,r >= 1`.  Then, coefficientwise in
`Z[a_ij]`,

```math
\boxed{
\mathcal F_{np^r}(A)
\equiv
\mathcal F_{np^{r-1}}(A^{[p]})
\pmod {p^{2r}}.
}
\tag{3}
```

### Lemma 2 (two-row carry bound)

Suppose every row sum and column sum of a nonnegative matrix `B` is
divisible by `p^t`.  If

```math
s=\min_{b_{ij}>0}v_p(b_{ij})<t,
```

then

```math
v_p(M(B))\ge 2(t-s).
\tag{4}
```

### Proof

At a digit level `h`, the contribution of row `i` to the Legendre
valuation of its multinomial coefficient is

```math
\lambda_i(h)=
\frac{\sum_j b_{ij}}{p^h}
-\sum_j\left\lfloor\frac{b_{ij}}{p^h}\right\rfloor.
\tag{5}
```

Because the row sum is divisible by `p^h`, this is the sum of the fractional
parts and is a nonnegative integer.  For every `s < h <= t`, an entry of
valuation `s` is nonzero modulo `p^h`, so its row has a carry.  Its column
sum is zero modulo `p^h`; therefore another entry in the same column, in a
different row, is also nonzero modulo `p^h`.  That second row has a carry as
well.  Thus `sum_i lambda_i(h) >= 2` at each of the `t-s` levels.  Summing
(5) proves (4).  QED

### Proof of Theorem 1

Put `N=np^r`.  First consider a matrix `B` in (2) whose entries are not all
divisible by `p`.  Lemma 2 with `t=r` and `s=0` gives

```math
p^{2r}\mid M(B),
```

so every such coefficient disappears modulo `p^(2r)`.

It remains to compare `B=pC` with the preceding level.  The matrix `C` has
all margins equal to `np^(r-1)`.  For a nontrivial row `c_i`, let `s_i` be
the minimum valuation of its positive entries.  Multinomial
Ljunggren--Jacobsthal--Kazandzidis scaling gives

```math
\frac{\binom{p\sum_jc_{ij}}{pc_{i1},\ldots,pc_{id}}}
     {\binom{\sum_jc_{ij}}{c_{i1},\ldots,c_{id}}}
\equiv1\pmod {p^{3(s_i+1)}}.
\tag{6}
```

Rows with one positive entry have quotient one exactly.  Let `s` be the
least `s_i` among the other rows.  If no such row exists, scaling is exact.
If `s >= r-1`, equation (6) is already stronger than required.  If
`s < r-1`, Lemma 2, applied at the levels above `s`, gives

```math
v_p(M(C))\ge2(r-1-s).
```

Consequently

```math
v_p(M(pC)-M(C))
\ge2(r-1-s)+3(s+1)
=2r+s+1\ge2r.
\tag{7}
```

Finally, `(A^B)` for `B=pC` is exactly `(A^[p])^C`.  The surviving terms in
(2) therefore assemble to the right side of (3).  QED

## 2. Transposition invariance

### Lemma 3

For every square matrix `A`,

```math
\mathcal F_N(A^T)=\mathcal F_N(A).
\tag{8}
```

### Proof

Transpose each contingency table in (2).  Since all row and column sums are
`N`,

```math
M(B)=\frac{(N!)^d}{\prod_{i,j}b_{ij}!}=M(B^T).
```

The weight for `A^T` at `B^T` is the weight for `A` at `B`.  QED

## 3. The Eisenstein realization of A124435

Let `tau` satisfy

```math
\tau^2-\tau+1=0.
```

Thus `tau` is a primitive sixth root of unity and
`tau^(-1)=1-tau`.  Work in the free integral ring
`R=Z[tau]`, and set

```math
A=\begin{pmatrix}
1&1&1\\
1&1&\tau\\
1&\tau^{-1}&1
\end{pmatrix}.
\tag{9}
```

Its diagonal entries are one, its three principal `2` by `2` minors vanish,
and its determinant is

```math
\det A=\tau+\tau^{-1}-2=-1.
```

Hence

```math
\det(I-\operatorname{diag}(x,y,z)A)
=1-x-y-z+xyz.
\tag{10}
```

MacMahon's Master Theorem and (1) now give

```math
\mathcal F_N(A)
=[x^Ny^Nz^N]\frac1{1-x-y-z+xyz}.
\tag{11}
```

For completeness, expanding the denominator directly gives

```math
\mathcal F_N(A)=
\sum_{j=0}^{N}(-1)^j
\frac{(3N-2j)!}{j!(N-j)!^3}.
\tag{12}
```

On replacing `j` by `N-k`, this becomes

```math
\sum_{k=0}^{N}(-1)^{N-k}
\binom Nk\binom{N+2k}{N}\binom{2k}{k},
\tag{13}
```

which is the formula on A124435.

## 4. The untwisted tower

Every prime `p >= 5` is congruent to `1` or `5` modulo `6`.  Therefore

```math
A^{[p]}=
\begin{cases}
A,&p\equiv1\pmod6,\\
A^T,&p\equiv5\pmod6.
\end{cases}
\tag{14}
```

Theorem 1 and Lemma 3 yield, in `R`,

```math
\mathcal F_{np^r}(A)
\equiv\mathcal F_{np^{r-1}}(A)
\pmod {p^{2r}}.
```

Both sides are rational integers by (12), and
`p^(2r)R intersect Z = p^(2r)Z`.  We have proved:

### Corollary 4 (A124435)

For every prime `p >= 5` and all positive integers `n,r`,

```math
\boxed{
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
}
```

This is exactly the conjecture on A124435.  The exponent is sharp already
at the first level for `p=5,7,11,13`; no cubic strengthening is claimed.

The prime `3` is genuinely outside this untwisting argument:
`tau^3=-1`, rather than `tau` or `tau^(-1)`, and
`v_3(a(3)-a(1))=1`.

## 5. Verification

Run

```text
python verification/related/verify_balanced_matrix_coefficient_tower.py
```

The checker verifies the OEIS values and single-sum identity, computes the
Eisenstein matrix coefficient independently in `Z[tau]`, checks the generic
twisted theorem on integer `2` by `2` and `3` by `3` matrices, and checks
the A124435 adjacent tower through two levels.  The computations use exact
integer and quadratic-ring arithmetic; the proof above establishes the
general theorem.

## 6. Campaign effect

A124435 moves from `open-target` to `proved-here` in the 110-record Bala
campaign.  The result also adds a reusable route: square balanced matrix
coefficients have a universal quadratic Frobenius tower, and cyclotomic
matrices turn that twisted statement into an ordinary supercongruence when
entrywise Frobenius is a symmetry such as transposition.
