# Catalan and Schröder Taylor truncations as two coefficient families

**Status:** exact all-parameter reduction and exact computational audit;
the two Cartier estimates in Section 4 remain unproved

**OEIS records:**
[A333090](https://oeis.org/A333090),
[A333091](https://oeis.org/A333091),
[A333092](https://oeis.org/A333092),
[A333093](https://oeis.org/A333093),
[A333095](https://oeis.org/A333095),
[A333096](https://oeis.org/A333096), and
[A333097](https://oeis.org/A333097)

The seven records above are not seven independent conjectures. This note
reduces them, for every integral power parameter, to two explicit rational
prefactors multiplying powers of elementary polynomials. It also isolates
the two estimates that would prove the complete Catalan family. No cubic
supercongruence is declared proved here.

## 1. The two truncation families

Let

```math
C(x)=\frac{1-\sqrt{1-4x}}{2x},
\qquad
S(x)=\frac{1-x-\sqrt{1-6x+x^2}}{2x}.
```

Thus `C` and `S` are the Catalan and large-Schröder generating series. For
an integer `m` and `N >= 0`, put

```math
\mathcal C_m(N)=\sum_{k=0}^N[x^k]C(x)^{mN},
\qquad
\mathcal S_m(N)=\sum_{k=0}^N[x^k]S(x)^{mN}.
\tag{1}
```

The OEIS conjectures assert, for every integer `m`, every prime `p >= 5`,
and positive `n,r`, that

```math
\mathcal X_m(np^r)\equiv\mathcal X_m(np^{r-1})\pmod {p^{3r}},
\qquad \mathcal X\in\{\mathcal C,\mathcal S\}.
\tag{2}
```

The named Catalan records use `m=1,3,4,5`; the named Schröder records use
`m=1,2,3`.

## 2. Exact Catalan reduction

Write `y=C(x)-1`. The Catalan equation gives

```math
x=\frac{y}{(1+y)^2}.
\tag{3}
```

Since a partial coefficient sum is a single coefficient after division by
`1-x`, residue substitution in (1) gives

```math
\begin{aligned}
\mathcal C_m(N)
&=[x^N]\frac{C(x)^{mN}}{1-x}\\
&=[y^N]\frac{(1-y)(1+y)^{(m+2)N+1}}
                    {1+y+y^2}.
\end{aligned}
\tag{4}
```

Consequently, with

```math
Q_C(y)=\frac{1-y^2}{1+y+y^2},
\tag{5}
```

we obtain the uniform identity

```math
\boxed{\mathcal C_m(N)
=[y^N]Q_C(y)(1+y)^{(m+2)N}.}
\tag{6}
```

This holds for every integer `m`; negative powers are interpreted in the
usual formal power-series sense. The prefactor is especially rigid:

```math
[y^j]Q_C(y)=
\begin{cases}
1,&j=0,\\
2,&j>0\text{ and }3\mid j,\\
-1,&j>0\text{ and }3\nmid j.
\end{cases}
\tag{7}
```

If `C_p` denotes Cartier extraction,
`C_p(\sum b_jy^j)=\sum b_{pj}y^j`, then (7) yields the exact identity

```math
C_p(Q_C)=Q_C\qquad(p\ne3).
\tag{8}
```

Equation (8), rather than periodicity by itself, is the useful Frobenius
feature. The repository contains an exact period-four counterexample to a
general rational-framing claim, so no theorem is inferred merely from the
fact that (7) is periodic.

## 3. Exact Schröder reduction and its Gaussian boundary

Now write `y=S(x)-1`. The Schröder equation gives

```math
x=\frac{y}{(1+y)(2+y)}.
\tag{9}
```

The same residue calculation gives

```math
\boxed{\mathcal S_m(N)
=[y^N]\frac{2-y^2}{y^2+2y+2}
        (1+y)^{(m+1)N}(2+y)^N.}
\tag{10}
```

After `y=2u`, the powers of two cancel from coefficient extraction, so an
integer-friendly form is

```math
\boxed{\mathcal S_m(N)
=[u^N]Q_S(u)(1+2u)^{(m+1)N}(1+u)^N,}
\tag{11}
```

where

```math
Q_S(u)=\frac{1-2u^2}{1+2u+2u^2}.
\tag{12}
```

If `q_j=[u^j]Q_S(u)`, then

```math
q_0=1,\quad q_1=-2,\quad q_2=0,
\qquad q_j=-2q_{j-1}-2q_{j-2}\quad(j\ge3).
\tag{13}
```

The denominator in (12) has roots `(-1+i)/2` and `(-1-i)/2`. Thus the
Schröder packet really does meet the Gaussian split/inert boundary; this is
not a metaphor imported from the separate Gaussian-binomial project. It
also explains why the exact Cartier fixed-point (8) does not carry over
unchanged. Exact tests in Section 5 cover primes on both sides of
`p mod 4`.

## 4. The two remaining Catalan estimates

The reduction (6) makes the missing proof small enough to state exactly.
Put `a=m+2`,

```math
G_a(y)=\frac{(1+y)^a}{y},
\qquad
V_p(y)=\sum_{\substack{j\ge1\\p\nmid j}}
              \frac{(-1)^{j+1}y^j}{j}.
\tag{14}
```

For every odd prime,

```math
\frac{G_a(y)^p}{G_a(y^p)}=\exp\bigl(paV_p(y)\bigr).
\tag{15}
```

Let `M` be positive and set `e=v_p(M)`. In view of (8), expansion of
(15) shows that the complete Catalan conjecture for `p >= 5` follows from
the following two uniform estimates:

```math
v_p\!\left(\operatorname{CT}
 G_a(y)^M C_p\!\left(Q_CV_p\right)\right)
\ge 2(e+1),
\tag{16}
```

```math
v_p\!\left(\operatorname{CT}
 G_a(y)^M C_p\!\left(Q_CV_p^2\right)\right)
\ge e+1.
\tag{17}
```

Indeed, the linear exponential term in (15) then has valuation at least
`3(e+1)`, as does the quadratic term. Every term of degree `h >= 3` has
that valuation because

```math
h(e+1)-v_p(h!)\ge3(e+1)\qquad(p\ge5).
\tag{18}
```

The checker verifies (16)--(17) on an exact grid including negative `a`,
but those finite checks are evidence, not a proof. This is the precise
remaining obligation; a vague appeal to Dwork theory or to rational
framing is not being counted as closure.

## 5. Verification

Run

```text
python verification/related/verify_taylor_truncation_reduction.py
```

The checker independently verifies the two residue identities against the
original Taylor truncations, all seven named initial segments, the
periodic and Gaussian prefactor laws, the proposed cubic towers over a
grid of positive and negative parameters, both split and inert primes in
the Schröder family, and exact finite instances of (16)--(17).

This changes the campaign bookkeeping from seven unrelated `open-target`
records to seven `partial` records controlled by one explicit proof packet.
