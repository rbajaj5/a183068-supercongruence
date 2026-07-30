# An exact \(2\times2\) counterexample to Zhang's four-matrix inequality

## Status

This note gives an exact counterexample to Conjecture 4.1 in Teng Zhang's
*A Matrix Inequality and Its Application*. The example consists of four
real rank-one orthogonal projectors, violates the proposed bound by the
factor \(1+\sqrt2\), and has the smallest possible matrix dimension. The
failure persists on an explicit interval of positive-definite perturbations.

All algebra below is independently reproduced by the exact-arithmetic
checker linked at the end. A targeted literature search through July 29,
2026 found no earlier resolution of this exact conjecture, but that negative
search is not a priority certificate. The result should be treated as a
candidate new counterexample pending specialist review and author feedback.

## 1. The conjectured inequality

For positive semidefinite matrices \(A,B,C,D\) of the same size, Zhang
conjectured

```math
\left\|A(BC+CB)D+D(BC+CB)A\right\|
\leq
\frac1{64}\left\|A+B+C+D\right\|^4,
\tag{Z}
```

where \(\|\cdot\|\) is the spectral norm. The source presents (Z) as a
possible route to the four-factor case of the Recht--Ré noncommutative
arithmetic--geometric mean program and reports supporting simulations.

Source:
[arXiv:1411.5058](https://arxiv.org/abs/1411.5058);
[published article and DOI](https://journals.uwyo.edu/index.php/ela/article/view/1879).

## 2. Four rank-one projectors disprove (Z)

Let

```math
A=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
B=\begin{pmatrix}0&0\\0&1\end{pmatrix},
```

and

```math
C=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad
D=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}.
```

Writing \(e_1=(1,0)^T\), \(e_2=(0,1)^T\),
\(u=(e_1-e_2)/\sqrt2\), and \(v=(e_1+e_2)/\sqrt2\), these matrices are

```math
A=e_1e_1^*,\qquad B=e_2e_2^*,\qquad C=uu^*,\qquad D=vv^*.
```

Thus each is a nonzero rank-one orthogonal projector and in particular is
positive semidefinite. Moreover,

```math
A+B=C+D=I_2,
\qquad
A+B+C+D=2I_2.
```

The right-hand side of (Z) is therefore

```math
\frac1{64}\|2I_2\|^4=\frac14.
```

On the other hand,

```math
BC+CB=
\begin{pmatrix}
0&-\frac12\\
-\frac12&1
\end{pmatrix},
```

and direct multiplication gives

```math
X:=A(BC+CB)D+D(BC+CB)A
=
\begin{pmatrix}
-\frac12&-\frac14\\
-\frac14&0
\end{pmatrix}.
```

The eigenvalues of \(X\) are

```math
\lambda_\pm=\frac{-1\pm\sqrt2}{4}.
```

Consequently

```math
\|X\|=\frac{1+\sqrt2}{4}>\frac14,
```

and the ratio of the two sides of (Z) is exactly

```math
\frac{\|X\|}{\frac1{64}\|A+B+C+D\|^4}=1+\sqrt2.
```

This disproves Conjecture 4.1.

## 3. Dimension two is minimal

In dimension one, write \(A=a,B=b,C=c,D=d\) with
\(a,b,c,d\geq0\). The left-hand side of (Z) is \(4abcd\). Scalar AM--GM
gives

```math
(a+b+c+d)^4\geq 256abcd,
```

so

```math
4abcd\leq\frac1{64}(a+b+c+d)^4.
```

Thus no scalar counterexample exists and the \(2\times2\) construction is
dimension-minimal. It is also componentwise rank-minimal: a zero factor
makes the left-hand side vanish, while every nonzero positive semidefinite
matrix has rank at least one.

## 4. An interval of positive-definite counterexamples

The failure is not a boundary effect caused by singular matrices. For
\(t>0\), put

```math
A_t=A+tI_2,\quad B_t=B+tI_2,\quad
C_t=C+tI_2,\quad D_t=D+tI_2.
```

Every one of these matrices is positive definite, with eigenvalues \(t\)
and \(1+t\). Set \(y=2t+1\). Their sum is \(2yI_2\), so the conjectured
right-hand side is \(y^4/4\).

Exact multiplication gives

```math
X_t=
\begin{pmatrix}
4t^4+8t^3+4t^2-\frac t2-\frac12&
-\frac t2-\frac14\\[1mm]
-\frac t2-\frac14&
4t^4+8t^3+4t^2+\frac t2
\end{pmatrix}.
```

Its eigenvalues are

```math
\lambda_\pm(t)
=
\frac{y^2(y^2-2)}4
\pm\frac{\sqrt2\,y}{4}.
```

The exact bracket below gives \(\tau<63/500<1/5\). Thus throughout
\(0<t<\tau\), one has \(y^2<(7/5)^2<2\); the eigenvalue center is negative,
so the negative eigenvalue has the larger absolute value. Subtraction of the
conjectured bound then yields

```math
\|X_t\|-\frac{y^4}{4}
=
\frac y4\left(
\sqrt2-16t^3-24t^2-8t
\right).
```

The polynomial \(16t^3+24t^2+8t\) is strictly increasing for \(t\geq0\).
Hence, if \(\tau\) is its unique positive solution of

```math
16\tau^3+24\tau^2+8\tau=\sqrt2,
```

then every

```math
0<t<\tau,\qquad
\frac18<\tau<\frac{63}{500},\qquad
\tau\approx0.125539310791824,
```

gives four positive-definite \(2\times2\) counterexamples.

For a convenient rational instance, take \(t=1/10\). Then

```math
X_{1/10}
=
\begin{pmatrix}
-\frac{627}{1250}&-\frac3{10}\\
-\frac3{10}&\frac{123}{1250}
\end{pmatrix},
```

with eigenvalues

```math
-\frac{126}{625}\pm\frac{3\sqrt2}{10}.
```

Therefore

```math
\|X_{1/10}\|
=\frac{126}{625}+\frac{3\sqrt2}{10}
>
\frac{324}{625}
=
\frac1{64}\left\|\frac{12}{5}I_2\right\|^4.
```

The strict comparison is equivalent to
\(\sqrt2>132/125\), which follows after squaring because
\(2>(132/125)^2\).

## 5. Scope and literature boundary

Recht and Ré introduced the parent noncommutative AM--GM problem in
connection with sampling with and without replacement, randomized
coordinate descent, and randomized Kaczmarz methods
([PMLR 2012](https://proceedings.mlr.press/v23/recht12.html)).
Lai and Lim later disproved the general Recht--Ré conjecture, with their
failure beginning at five factors
([arXiv:2006.01510](https://arxiv.org/abs/2006.01510)).

The calculation here resolves Zhang's separately stated auxiliary
Conjecture 4.1. Because Zhang proposed (Z) as a sufficient route to the
four-factor parent inequality, refuting (Z) removes that route; it does
**not** by itself disprove or prove the parent four-factor case.

## Verification

Run

```text
python verification/related/verify_zhang_four_matrix_counterexample.py
```

The checker uses rational arithmetic only. It verifies the projector
identities, the counterexample matrix and characteristic polynomial, the
positive-definite example, the general perturbation polynomial, a rational
bracket for \(\tau\), and a finite scalar AM--GM sanity grid.
