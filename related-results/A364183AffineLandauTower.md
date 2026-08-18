# A364183: affine-Landau integrality and the complete cubic tower

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open

Define fractional factorials by $x!=\Gamma(x+1)$ and put

```math
A(N)=
\frac{(12N)!(2N)!(N/2)!}
     {(6N)!(4N)!(7N/2)!N!}.
\tag{1}
```

This is OEIS A364183, equivalently A295479 at the half-index.

## Theorem

For every $N\geq0$, $A(N)$ is an integer. For every prime $p\geq5$ and
positive integers $n,r$,

```math
\boxed{A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.}
\tag{2}
```

## 1. Parity reduction

For $N=2m$, equation (1) is the Bober ratio

```math
A(2m)=
\frac{(24m)!(4m)!m!}{(12m)!(8m)!(7m)!(2m)!}
=\operatorname{A295479}(m),
\tag{3}
```

which is integral by the Vasyunin--Bober classification.

For $N=2m+1$, the half-integer gamma formula gives

```math
A(2m+1)=2^{12m+6}R(m),
\tag{4}
```

where

```math
R(m)=
\frac{(24m+12)!(4m+2)!(2m+2)!(7m+4)!}
{(12m+6)!(8m+4)!(2m+1)!(m+1)!(14m+8)!}.
\tag{5}
```

## 2. The affine floor lemma

For $d\geq2$ set

```math
\begin{aligned}
\Phi_d(m)={}&
\left\lfloor\frac{24m+12}{d}\right\rfloor
+\left\lfloor\frac{4m+2}{d}\right\rfloor
+\left\lfloor\frac{2m+2}{d}\right\rfloor
+\left\lfloor\frac{7m+4}{d}\right\rfloor\\
&-\left\lfloor\frac{12m+6}{d}\right\rfloor
-\left\lfloor\frac{8m+4}{d}\right\rfloor
-\left\lfloor\frac{2m+1}{d}\right\rfloor
-\left\lfloor\frac{m+1}{d}\right\rfloor
-\left\lfloor\frac{14m+8}{d}\right\rfloor.
\end{aligned}
\tag{6}
```

### Lemma

For all $m\geq0$ and $d\geq2$,

```math
\Phi_d(m)\in\{0,1,2\}.
\tag{7}
```

In particular it is nonnegative.

### Proof

Both the coefficients of $m$ and the constant terms balance, so
$\Phi_d(m+d)=\Phi_d(m)$. It is enough to assume $0\leq m<d$. Put

```math
t=2m+1=qd+s,\qquad 0\leq s<d.
\tag{8}
```

Since $1\leq t<2d$, one has $q\in\{0,1\}$. Moreover, $s$ is odd when
$q=0$, while $d+s$ is odd when $q=1$. Define

```math
j=\left\lfloor\frac{12s}{d}\right\rfloor,\qquad
h=\left\lfloor\frac{7s+1}{d}\right\rfloor,\qquad
\epsilon=\left\lfloor\frac{s+1}{d}\right\rfloor.
\tag{9}
```

Thus $0\leq j\leq11$, $\epsilon$ is zero except when $s=d-1$, and

```math
C(j):=j+\left\lfloor\frac j6\right\rfloor
-\left\lfloor\frac j2\right\rfloor
-\left\lfloor\frac j3\right\rfloor
```

collects the four floors involving $12s,2s,6s,4s$. Substitution in (6)
now gives the two exact formulas

```math
\Phi_d(m)=
\begin{cases}
C(j)+\epsilon-\lceil h/2\rceil,&q=0,\\
-3+C(j)+\lfloor(7-h)/2\rfloor,&q=1.
\end{cases}
\tag{10}
```

For example, in the second line the two occurrences of $\epsilon$ cancel:

```math
\left\lfloor\frac{7d+7s+1}{2d}\right\rfloor
-\left\lfloor\frac{d+s+1}{2d}\right\rfloor
=\left\lfloor\frac{7+h}{2}\right\rfloor-\epsilon.
```

It remains only a twelve-row calculation. The inequalities

```math
jd\leq12s<(j+1)d,\qquad hd\leq7s+1<(h+1)d
```

give the possible values of $h$ in the third column below. The fourth column
is the first line of (10) with $\epsilon=0$; the exceptional value
$\epsilon=1$ can only increase it. The last column is the second line.

| $j$ | $C(j)$ | possible $h$ | $q=0$: $C(j)-\lceil h/2\rceil$ | $q=1$ |
| ---: | ---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0, 1 | 1, 0 | 1, 1 |
| 2 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1, 2 | 0, 0 | 1, 0 |
| 4 | 1 | 2, 3 | 0, $-1$ | 0, 0 |
| 5 | 2 | 2, 3 | 1, 0 | 1, 1 |
| 6 | 2 | 3, 4 | 0, 0 | 1, 0 |
| 7 | 3 | 4 | 1 | 1 |
| 8 | 3 | 4, 5 | 1, 0 | 1, 1 |
| 9 | 3 | 5 | 0 | 1 |
| 10 | 3 | 5, 6 | 0, 0 | 1, 0 |
| 11 | 4 | 6 | 1 | 1 |

There is one apparent negative entry. If $j=4$ and $h=3$, then

```math
4d\leq12s<5d,\qquad 3d\leq7s+1.
```

These inequalities imply $s<5$; checking $s=0,1,2,3,4$ leaves only
$(d,s)=(5,2)$. This has even $s$, so it cannot occur in the $q=0$ row.
Consequently (10) is always nonnegative. The table also gives an upper bound
of one before adding $\epsilon$, hence an upper bound of two altogether.
This proves (7). QED

For every prime $\ell$, Legendre's formula now gives

```math
v_\ell(R(m))=\sum_{a\geq1}\Phi_{\ell^a}(m)\geq0.
\tag{11}
```

Thus $R(m)$ is an integer. Equations (3)--(5) prove global integrality.

## 3. The cubic tower

For $c\geq3$ write

```math
B_c(N)=\binom{cN/2}{N}.
```

Cancellation of gamma factors gives the exact identity

```math
A(N)=
\frac{B_{14}(N)B_{16}(N)B_{18}(N)B_{20}(N)B_{22}(N)B_{24}(N)}
     {B_3(N)B_5(N)B_6(N)B_7(N)B_8(N)}.
\tag{12}
```

The half-binomial scaling theorem gives, for $p\geq5$, $N=pM$, and
$e=v_p(N)$,

```math
\frac{B_c(N)}{B_c(M)}\equiv1\pmod {p^{3e}}.
\tag{13}
```

Products and inverses of these $p$-adic units preserve the modulus, so (11)
implies $A(N)/A(M)\equiv1\pmod {p^{3e}}$. Taking $N=np^r$ gives
$e\geq r$. Multiplication by the integral lower-level value proves (2).
QED

## Verification and source boundary

Run

```text
python verification/related/verify_a364183_affine_landau.py
```

The checker verifies both parity formulas, the affine-floor breakpoint
classification, Legendre valuations, the eleven-factor half-binomial
identity, every factor transfer, and the complete tower on an exact grid.

The conjectures and formula are recorded on
[OEIS A364183](https://oeis.org/A364183); even-index integrality comes from
[Bober's classification](https://arxiv.org/abs/0709.1977). No assertion is
made for $p=2$ or $p=3$, and no literature-priority claim is made.
