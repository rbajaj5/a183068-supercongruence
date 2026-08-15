# A244973 and the linear--quadratic Frobenius obstruction

**Status:** exact reduction of Zhi-Wei Sun's remaining conjecture; the final
combined Cartier cancellation is not proved.

**Source boundary:** [OEIS A244973](https://oeis.org/A244973) records the
conjecture and cites Sun's
[*Supercongruences involving Lucas sequences*](https://arxiv.org/abs/1610.03384).
Theorem 1.3 of that paper proves the weaker exponent displayed below, while
Conjecture 5.6 states the target.  The signed multinomial identity was added
to the OEIS record by Peter Bala on August 5, 2026.  No priority claim is made
for the vertex normalization or the reduction in this note.

## 1. The exact published boundary

Put

```math
a(N)=g_N(-1)=
\sum_{k=0}^{N}(-1)^k\binom Nk^2\binom{2k}{k}.
\tag{1}
```

For every prime `p > 5` and positive integer `M`, Sun proves

```math
v_p\bigl(a(pM)-a(M)\bigr)\ge 3+2v_p(M).
\tag{2}
```

His Conjecture 5.6, and the conjecture on A244973, asks for

```math
\boxed{
v_p\bigl(a(pM)-a(M)\bigr)\ge 3+3v_p(M).
}
\tag{3}
```

Writing `M=np^(r-1)` turns (3) into the adjacent cubic tower

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}.
\tag{4}
```

The prime restriction is real: `a(5)-a(1)=50`, so the first level has
5-adic valuation two rather than three.

## 2. Signed multinomials and a Laurent period

The identity on the live OEIS record is

```math
a(N)=
\sum_{i+j+k=N}(-1)^{i+j}
\binom{N}{i,j,k}^{\!2}.
\tag{5}
```

It gives the constant term

```math
a(N)=\operatorname{CT}_{x,y,z}
\left((x+y+z)(-x^{-1}-y^{-1}+z^{-1})\right)^N.
\tag{6}
```

The polynomial in (6) is two-dimensional after quotienting by simultaneous
scaling.  Set `u=x^(-1)` and `v=y` after choosing the vertex `-x/y`.  Direct
division at that vertex gives

```math
\phi(u,v)=(1+u+uv)(1-v+uv)
          =1+u-v+uv-uv^2+u^2v+u^2v^2,
\tag{7}
```

and hence the exact diagonal form

```math
\boxed{
a(N)=(-1)^N[u^Nv^N]\phi(u,v)^N.
}
\tag{8}
```

Equivalently, `a(N)=CT G(u,v)^N` for
`G=-phi/(uv)`.  Formula (8) is useful because `phi(0,0)=1`, so all formal
logarithms below live in the ordinary power-series cone and every requested
coefficient is finite.

## 3. The exact two-term Dwork reduction

Fix an odd prime `p` and define the integral reduced logarithm

```math
L_p(u,v)=\frac1p\log
\frac{\phi(u,v)^p}{\phi(u^p,v^p)}
\in\mathbb Z_p[[u,v]].
\tag{9}
```

Integrality follows immediately from
`phi(u,v)^p/phi(u^p,v^p) in 1+p Z_p[[u,v]]` and the p-adic logarithm.
For `N=pM`, oddness of `p` and (8) give the exact identity

```math
\begin{aligned}
a(pM)-a(M)
=(-1)^M[u^{pM}v^{pM}]\phi(u^p,v^p)^M
\left(\exp(pM L_p)-1\right).
\end{aligned}
\tag{10}
```

Every exponential term of degree at least three belongs to
`p^3 M^3 Z_p[[u,v]]` when `p > 5`.  Therefore (3) is equivalent to the
single combined estimate

```math
\boxed{
\begin{aligned}
v_p\Bigl([u^{pM}v^{pM}]\phi(u^p,v^p)^M
\bigl(pM L_p+\tfrac{(pM)^2}{2}L_p^2\bigr)\Bigr)
\ge 3+3v_p(M).
\end{aligned}
}
\tag{11}
```

Thus no logarithmic tail remains.  The whole conjecture is one explicit
linear--quadratic Cartier cancellation.

## 4. Why ordinary Jacobsthal estimates stop one power short

The two factors in (7) have logarithms

```math
\log(1+u+uv)
=\sum_{a\ge1}\sum_{b=0}^{a}
\frac{(-1)^{a+1}}a\binom ab u^av^b,
\tag{12}
```

and

```math
\log(1-v+uv)
=-\sum_{a\ge1}\sum_{b=0}^{a}
\frac{(-1)^b}{a}\binom ab u^bv^a.
\tag{13}
```

Let `C_p` be the bivariate Cartier operator.  If `L_p=L_p^+ + L_p^-`
according to (12)--(13), then

```math
[u^av^b]C_p(L_p^+)
=\frac{(-1)^{a+1}}{pa}
\left(\binom{pa}{pb}-\binom ab\right),
\tag{14}
```

and

```math
[u^bv^a]C_p(L_p^-)
=-\frac{(-1)^b}{pa}
\left(\binom{pa}{pb}-\binom ab\right).
\tag{15}
```

The Ljunggren--Jacobsthal--Kazandzidis estimate makes the interior
coefficients in (14)--(15) divisible by
`p^2 b(a-b)`.  After formal integration by parts this recovers the
`p^3 M^2` depth in Sun's theorem.  It does not by itself supply the final
factor of `M` in (3).

Nor can the two terms in (11) be estimated separately.  At `p=7, M=7`,
exact rational coefficient extraction gives

```text
valuation of the linear term       = 5
valuation of the quadratic term    = 5
valuation of their sum             = 6
required valuation                 = 6
```

The missing power is therefore a real cancellation between the two lowest
Frobenius terms.  A proof of (11) must preserve that pair, rather than bound
the unit shell or the linear logarithm in isolation.

## 5. Reproducibility and campaign effect

Run

```text
python verification/related/verify_a244973_frobenius_reduction.py
```

The checker verifies (1), (5), (6), and (8), the coefficient formulas
(12)--(15), Sun's proved bound and the conjectured tower on an exact finite
grid, the sharp `p=5` obstruction, the two-term reduction (10)--(11), and
the `p=7, M=7` cancellation above.

This note moves A244973 from `open-target` to `partial` in the 110-record
Bala ledger.  The target itself is not declared proved: the remaining task
is exactly (11).
