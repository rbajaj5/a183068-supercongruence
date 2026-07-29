# Joint Walsh spectra for the dyadic defect

**Status.** Complete finite-dimensional theorem with exhaustive exact
checks. It extends the
[single-coordinate matching analysis](DyadicHypercubeWalshAnalysis.md)
to arbitrary XOR tests and exact joint distributions of several defect
coordinates. The quadratic-form Fourier theorem used in the proof is
classical.

## 1. A finite defect map

Let $A\subset\mathbb N^d$ be a finite monomial support and write

```math
F=\sum_{\alpha\in A}
(\epsilon_\alpha+2\eta_\alpha)X^\alpha
\pmod4,
\qquad
\epsilon_\alpha,\eta_\alpha\in\mathbb F_2.
\qquad\text{(1)}
```

For a finite target set $\Gamma\subset\mathbb N^d$, define

```math
Q_\Gamma(\epsilon,\eta)
=
\left(
[X^\gamma]\frac{F^2-\phi(F)}2
\right)_{\gamma\in\Gamma}
\pmod2.
\qquad\text{(2)}
```

Here $\phi(X^\alpha)=X^{2\alpha}$, extended coefficientwise; it doubles
monomial exponents without squaring the integer coefficients.

Thus

```math
Q_\Gamma:
\mathbb F_2^{\,2|A|}
\longrightarrow
\mathbb F_2^{\,|\Gamma|}.
```

The preceding note gives a disjoint matching for one coordinate. Different
coordinates can share variables, so the joint map is not generally a
product of matchings.

## 2. The alternating convolution matrix

Let $\lambda=(\lambda_\gamma)_{\gamma\in\Gamma}$ be a linear functional
on the output, extended by zero outside $\Gamma$. The scalar test

```math
Q_\lambda
=
\lambda(Q_\Gamma)
```

is

```math
Q_\lambda(\epsilon,\eta)
=
\sum_{\alpha\in A}\lambda_{2\alpha}\eta_\alpha
+
\sum_{\substack{\alpha,\beta\in A\\\alpha<\beta}}
\lambda_{\alpha+\beta}\epsilon_\alpha\epsilon_\beta.
\qquad\text{(3)}
```

Define the alternating matrix $B_\lambda$, indexed by $A$, by

```math
(B_\lambda)_{\alpha,\beta}
=
\begin{cases}
\lambda_{\alpha+\beta},&\alpha\ne\beta,\\
0,&\alpha=\beta.
\end{cases}
\qquad\text{(4)}
```

It is the polar form of the low-bit quadratic in (3). Its rank is even;
write

```math
\mathrm{rank}\,B_\lambda=2s_\lambda.
\qquad\text{(5)}
```

On the full input space

```math
W=\mathbb F_2^A\oplus\mathbb F_2^A
```

the polar radical is

```math
R_\lambda
=
\ker B_\lambda\oplus\mathbb F_2^A.
\qquad\text{(6)}
```

Because the polar form vanishes on $R_\lambda$, the restriction

```math
r_\lambda=Q_\lambda|_{R_\lambda}
\qquad\text{(7)}
```

is linear.

## 3. Plateaued spectrum theorem

For a covector $\xi\in W^*$, use the normalized Walsh transform

```math
\widehat g_\lambda(\xi)
=
2^{-2|A|}
\sum_{w\in W}
(-1)^{Q_\lambda(w)+\xi(w)},
\qquad
g_\lambda=(-1)^{Q_\lambda}.
\qquad\text{(8)}
```

### Theorem 1 (rank controls every XOR test)

The Walsh coefficient in (8) is nonzero exactly when

```math
\xi|_{R_\lambda}=r_\lambda.
\qquad\text{(9)}
```

Consequently:

1. exactly $2^{2s_\lambda}$ Walsh coefficients are nonzero;
2. every nonzero coefficient has absolute value $2^{-s_\lambda}$;
3. $Q_\lambda$ is balanced exactly when
   $r_\lambda\ne0$; and
4. if $r_\lambda=0$, then

   ```math
   \mathbb E(-1)^{Q_\lambda}
   =
   \sigma_\lambda2^{-s_\lambda},
   \qquad
   \sigma_\lambda\in\{1,-1\}.
   \qquad\text{(10)}
   ```

The sign $\sigma_\lambda$ is the ordinary quadratic Gauss-sum sign
(equivalently, the Arf sign after quotienting by the radical).

#### Proof

Let $r\in R_\lambda$. Since $r$ is in the polar radical,

```math
Q_\lambda(w+r)
=
Q_\lambda(w)+Q_\lambda(r).
\qquad\text{(11)}
```

Translate the sum (8) by $r$. A nonzero Walsh coefficient must satisfy

```math
Q_\lambda(r)+\xi(r)=0
```

for every $r\in R_\lambda$, which is exactly (9).

Conversely, choose a complement $U$ to $R_\lambda$. The induced polar
form on $U$ is nondegenerate and has dimension $2s_\lambda$. When (9)
holds, summing first over the radical contributes $|R_\lambda|$, while
the remaining nondegenerate quadratic Gauss sum on $U$ has absolute
value $2^{s_\lambda}$. After the normalization in (8), the magnitude is
$2^{-s_\lambda}$.

The covectors satisfying (9) form an affine space of dimension
$2s_\lambda$, proving the first two claims. The zero-frequency
coefficient is nonzero exactly when $r_\lambda=0$, proving the balance
criterion and (10). $\square$

## 4. Exact joint output distribution

Let $m=|\Gamma|$, and for $y\in\mathbb F_2^\Gamma$ put

```math
N_\Gamma(y)
=
\#\left\{
(\epsilon,\eta)\in\mathbb F_2^{2|A|}:
Q_\Gamma(\epsilon,\eta)=y
\right\}.
\qquad\text{(12)}
```

Define the scalar bias

```math
b_\lambda
=
\mathbb E(-1)^{Q_\lambda}.
\qquad\text{(13)}
```

By Theorem 1, $b_\lambda$ is either $0$ or
$\sigma_\lambda2^{-s_\lambda}$.

### Theorem 2 (joint model-count formula)

For every output $y$,

```math
N_\Gamma(y)
=
\frac{2^{2|A|}}{2^m}\!
\sum_{\lambda\in\mathbb F_2^\Gamma}
(-1)^{\lambda\cdot y}b_\lambda.
\qquad\text{(14)}
```

In particular, $Q_\Gamma$ is uniformly distributed on its full output
cube exactly when

```math
b_\lambda=0
\qquad
\text{for every nonzero }\lambda,
\qquad\text{(15)}
```

or equivalently, when every nonzero scalar test $Q_\lambda$ restricts
nontrivially to its polar radical.

#### Proof

The indicator of $Q_\Gamma(w)=y$ has the finite Fourier expansion

```math
\mathbf{1}_{Q_\Gamma(w)=y}
=
2^{-m}
\sum_{\lambda\in\mathbb F_2^\Gamma}
(-1)^{\lambda\cdot(Q_\Gamma(w)+y)}.
```

Sum over $w\in W$ and use (13). This proves (14). Fourier inversion
also proves the equivalence (15). $\square$

An immediate deviation bound is

```math
\left|
\Pr(Q_\Gamma=y)-2^{-m}
\right|
\le
2^{-m}\!
\sum_{\lambda\ne0}|b_\lambda|
=
2^{-m}\!
\sum_{\substack{\lambda\ne0\\r_\lambda=0}}
2^{-s_\lambda}.
\qquad\text{(16)}
```

The exact formula (14), rather than this bound, is usually preferable.

## 5. Exact collision and nonuniformity certificates

Let $P_\Gamma(y)=N_\Gamma(y)/2^{2|A|}$ be the output distribution under
uniform coefficient bits, and let $U(y)=2^{-m}$ be the uniform distribution
on the output cube. We use

```math
\chi^2(P_\Gamma\|U)
=
\sum_y\frac{(P_\Gamma(y)-U(y))^2}{U(y)}.
```

### Theorem 3 (rank-profile identities)

The collision probability is

```math
\begin{aligned}
\mathrm{Col}(P_\Gamma)
&=
\sum_y P_\Gamma(y)^2\\
&=
2^{-m}
\left(
1+
\sum_{\substack{\lambda\ne0\\r_\lambda=0}}
2^{-2s_\lambda}
\right).
\end{aligned}
\qquad\text{(17)}
```

Equivalently, for independent uniform coefficient arrays $w,w'$,

```math
\Pr\!\left(Q_\Gamma(w)=Q_\Gamma(w')\right)
=
\mathrm{Col}(P_\Gamma).
\qquad\text{(18)}
```

The chi-squared distance from uniform is exactly

```math
\chi^2(P_\Gamma\|U)
=
\sum_{\substack{\lambda\ne0\\r_\lambda=0}}
2^{-2s_\lambda}.
\qquad\text{(19)}
```

Consequently,

```math
\left|\mathrm{supp}\,P_\Gamma\right|
\ge
\frac{2^m}
{1+\displaystyle
\sum_{\substack{\lambda\ne0\\r_\lambda=0}}
2^{-2s_\lambda}}
\qquad\text{(20)}
```

and

```math
\|P_\Gamma-U\|_{\mathrm{TV}}
\le
\frac12
\left(
\sum_{\substack{\lambda\ne0\\r_\lambda=0}}
2^{-2s_\lambda}
\right)^{1/2}.
\qquad\text{(21)}
```

#### Proof

The output Fourier transform is

```math
\widehat P_\Gamma(\lambda)
=
\sum_y P_\Gamma(y)(-1)^{\lambda\cdot y}
=b_\lambda.
```

Parseval on $\mathbb F_2^m$ gives

```math
\sum_y P_\Gamma(y)^2
=
2^{-m}\sum_\lambda b_\lambda^2.
```

Now use Theorem 1: $b_0=1$, while every nonzero $b_\lambda$ is either
zero or has square $2^{-2s_\lambda}$. This proves (17)--(19). The support
bound (20) is Cauchy--Schwarz:

```math
1
=
\left(\sum_{y\in\mathrm{supp}\,P_\Gamma}P_\Gamma(y)\right)^2
\le
\left|\mathrm{supp}\,P_\Gamma\right|
\sum_yP_\Gamma(y)^2.
```

Finally, Cauchy--Schwarz applied to
$\frac12\sum_y|P_\Gamma(y)-2^{-m}|$ and (19) gives (21).
$\square$

Equations (19)--(21) are deterministic statements about the image of the
uniform ambient coefficient cube. They do not assert pseudorandomness of
the structured coefficient vectors produced by an Euler product.
Unlike the pointwise count (14), these collision and distance certificates
do not require the Gauss-sum signs $\sigma_\lambda$: ranks and radical
restrictions alone determine them.

## 6. Why this is useful

Theorem 2 converts a simultaneous modulus-$4$ classification into finite
linear algebra:

1. choose the output coordinates $\Gamma$;
2. for each $\lambda$, build the Hankel-like convolution matrix (4);
3. row-reduce it over $\mathbb F_2$;
4. test the radical restriction (7);
5. compute the Gauss-sum sign when it survives; and
6. recover every joint count by (14).

This is an exact model-counting method for the quadratic CSP generated by
the dyadic defect. It can be much smaller than enumerating
$4^{|A|}$ coefficient arrays. It does not say that the structured
coefficient vectors arising from Euler products are uniformly distributed
inside the ambient cube.

The matrix (4) is a finite additive-convolution matrix: its entry depends
only on $\alpha+\beta$. That is the precise point where the hypercube
analysis meets the additive structure of monomial exponents.

## 7. Verification and provenance

The existing checker

```text
python verification/related/verify_dyadic_hypercube_walsh.py
```

now also:

- constructs multi-coordinate defect maps from one- and two-dimensional
  monomial supports;
- checks the rank, radical, Walsh-support, and plateau-height assertions
  for every output functional;
- compares (14) with exhaustive joint model counts;
- tests the uniform-output criterion; and
- compares the collision, chi-squared, support, and total-variation
  consequences with exhaustive output distributions.

The general rank theorem for quadratic Boolean functions is classical.
See Ryan O'Donnell,
[*Analysis of Boolean Functions*](https://arxiv.org/abs/2105.10386), for
the Fourier framework. The repository-specific contribution is the
explicit convolution matrix (4) for the dyadic Frobenius defect and its
use in the exact joint count (14).
