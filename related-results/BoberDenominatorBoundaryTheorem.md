# Closing the denominator-three and denominator-four Bober cases

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open

This note closes the four fractional-index integrality cases left after the
uniform half-index theorem:

```text
A295456 at N/3,  A295458 at N/3,
A295460 at N/4,  A295477 at N/4.
```

Together with the rational gamma-ratio transfer theorem, it completes every
fractional formula currently visible in Peter Bala's Bober packet.

## 1. Translated Landau valuations away from the denominator

Let

```math
F(n)=\frac{\prod_i(u_i n)!}{\prod_j(v_j n)!},
\qquad
\Delta(x)=\sum_i\lfloor u_i x\rfloor-
\sum_j\lfloor v_jx\rfloor
\tag{1}
```

be a balanced integral factorial ratio. Fix $q\ge2$ and suppose the slope
multiplicities balance in every nonzero residue class modulo $q$. Define

```math
F_q(N)=
\frac{\prod_i\Gamma(u_iN/q+1)}
     {\prod_j\Gamma(v_jN/q+1)}.
\tag{2}
```

For $a\in\mathbb Z$, let $\rho_q(a)$ be its representative in
$\{1,\ldots,q\}$. If $p\nmid q$, put
$z_a\equiv Np^{-a}\pmod q$. Counting the multiples of $p^a$ in the
arithmetic progressions defining the gamma factors gives

```math
v_p(F_q(N))=
\sum_{a\ge1}\Phi_{z_a}\!\left(\frac{N}{qp^a}\right),
\tag{3}
```

where

```math
\Phi_z(x)=
\sum_i\left\lfloor u_ix+1-\frac{\rho_q(u_iz)}q\right\rfloor-
\sum_j\left\lfloor v_jx+1-\frac{\rho_q(v_jz)}q\right\rfloor.
\tag{4}
```

The key point is the exact translation identity

```math
\Phi_z(x)=\Delta(x-z/q)-\Delta(-z/q).
\tag{5}
```

Residue balance and slope balance give $\Delta(-z/q)=0$. Bober's ordinary
integrality theorem gives $\Delta\ge0$, including after translation because
$\Delta$ is one-periodic. Thus every summand in (3) is nonnegative. This
proves integrality at every prime not dividing $q$ without a new floor table.

## 2. The denominator primes

Only $p=3$ for $q=3$ and $p=2$ for $q=4$ remain. Write $s_b(m)$ for the
sum of the base-$b$ digits of $m$. Directly applying Legendre's formula to
the three residue classes modulo three gives the following exact valuations
when $3\nmid N$:

```math
v_3(F_{3,\mathrm{A295456}}(N))=
\frac{3N-s_3(10N)+s_3(5N)+s_3(4N)}2,
\tag{6}
```

```math
v_3(F_{3,\mathrm{A295458}}(N))=
\frac{9N-s_3(10N)+s_3(5N)+s_3(2N)}2.
\tag{7}
```

For $N=1$, (6) is nonnegative directly. For $N\ge2$,

```math
s_3(10N)\le2(\lfloor\log_3(10N)\rfloor+1)\le3N.
```

Equations (6)--(7) are therefore nonnegative. When $3\mid N$, the values
are ordinary integral values of the original Bober ratios.

For the denominator-four cases, Legendre's binary digit formula gives

```math
v_2(F_{4,\mathrm{A295460}}(N))=
\begin{cases}
N+s_2(N),&N\text{ odd},\\
6N-s_2(15N/2)-s_2(N/2)+s_2(5N/2)+s_2(3N/2)+s_2(N),
 &N\equiv2\pmod4,
\end{cases}
\tag{8}
```

and

```math
v_2(F_{4,\mathrm{A295477}}(N))=
\begin{cases}
3N+s_2(N),&N\text{ odd},\\
2N+s_2(N),&N\equiv2\pmod4.
\end{cases}
\tag{9}
```

All quantities in (8)--(9) are nonnegative. In the second line of (8), use

```math
s_2(15N/2)+s_2(N/2)
\le \lfloor\log_2(15N/2)\rfloor+
   \lfloor\log_2(N/2)\rfloor+2
\le6N
```

for $N\ge2$. If $4\mid N$, the values are again ordinary integral values.
This proves global integrality in all four cases.

## 3. Cubic towers and disposition

The four slope systems are residue-balanced. The rational gamma-ratio
transfer theorem therefore combines with global integrality to give, for
every prime $p\ge5$ and positive integers $n,r$,

```math
\boxed{F_q(np^r)\equiv F_q(np^{r-1})\pmod {p^{3r}}.}
\tag{10}
```

Hence every one of the 15 fractional variants currently visible in the
Bober packet is now integral and has its complete adjacent cubic tower for
$p\ge5$. The reported but not yet source-visible A295464 comment remains a
source-admission issue, not a mathematical exception.

## Verification and source boundary

Run

```text
python verification/related/verify_bober_denominator_boundary.py
```

The checker verifies (3)--(5), all four boundary formulas, exact integrality,
and adjacent towers. The general proof uses Bober's classification as the
ordinary-integrality input. No claim of literature priority is made.
