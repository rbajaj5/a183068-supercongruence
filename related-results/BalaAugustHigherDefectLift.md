# The higher August defect: an exact three-level reduction

**Status:** exact reduction and sharp computational boundary; the final
higher-Frobenius estimate remains open

## 1. The remaining conjecture

Put

```math
u(N)=\sum_{k=0}^{N}\binom{-N}{k}\binom{-2N}{k},
\qquad
D_{p,r}(n)=u(np^r)-u(np^{r-1}),
```

and

```math
Q_{p,r}(n)=\frac{D_{p,r}(n)}{p^{3r}}.
tag{1}
```

The cubic tower and integrality of (1) are proved for every odd prime in
the preceding notes.  The one August claim still not proved is

```math
Q_{p,r}(n)\equiv Q_{p,r-1}(n)
\pmod {p^{2r-2-\delta_p}},
\qquad
\delta_p=\begin{cases}1,&p=5,\\0,&p\ge7.
\end{cases}
tag{2}
```

The modulus is sharp: for every tested prime except occasional irregular
extra gains, $n=1,r=2$ attains the displayed exponent.  Thus (2) cannot be
replaced by a routine extra-power observation.

## 2. Equivalent three-level congruence

### Proposition 1

For $r\ge2$, congruence (2) is equivalent to

```math
\boxed{
u(np^r)-(1+p^3)u(np^{r-1})+p^3u(np^{r-2})
\equiv0\pmod {p^{5r-2-\delta_p}}.
}
tag{3}
```

Indeed, multiplying the difference in (2) by $p^{3r}$ gives exactly the
left side of (3).  This formulation is preferable for proof work: it has
no division and makes clear that the conjecture is a second-order
Frobenius relation, not another two-term cubic tower.

## 3. Exact valuation-shell decomposition

Write

```math
f_N(k)=\binom{N+k-1}{k}\binom{2N+k-1}{k}.
tag{4}
```

Let $N=np^r$, $M=N/p$, and $L=M/p$.  Partitioning the three sums in (3)
by the valuation of the high-scale index gives the exact identity

```math
E_{p,r}(n)=A_0+A_1+A_2,
tag{5}
```

where

```math
\begin{aligned}
A_0&=\sum_{\substack{0\le k\le N\\p\nmid k}}f_N(k),\\
A_1&=\sum_{\substack{1\le q\le M\\p\nmid q}}
\left(f_N(pq)-(1+p^3)f_M(q)\right),\\
A_2&=\sum_{q=0}^{L}
\left(f_N(p^2q)-(1+p^3)f_M(pq)+p^3f_L(q)\right).
\end{aligned}
tag{6}
```

Here $E_{p,r}(n)$ denotes the left side of (3).  Formula (6) is merely a
partition, but it rules out two tempting incomplete proofs.  Neither the
unit shell nor the once-scaled shell is generally divisible by the target
modulus.  Their leading pieces cancel, and at the next level the twice-
scaled shell participates as well.  The conjecture is intrinsically a
three-shell statement.

For example, at $n=1,r=2$ the respective valuations are

```text
             v_p(A0)   v_p(A1)   v_p(A2)   v_p(E)
p = 5            6         6         7          7
p = 7            6         6         8          8
p = 11           6         6         8          8
```

where the target exponents are $7,8,8$.  A proof that estimates the three
rows separately therefore cannot work.

## 4. Exact logarithmic form

Retain the notation $H,G,L_p$ and $\mathcal C_p$ from the
[first-defect note](BalaAugustFirstDefectKernel.md), and put

```math
\mathscr A_j=\frac1{j!}\mathcal C_p(HL_p^j).
tag{7}
```

The proof of the first-defect theorem actually gives the exact convergent
expansion

```math
Q_{p,r}(n)=
n^3\operatorname{CT}(\mathscr B_{p;1,2,1}G^{np^{r-1}})
+\sum_{j\ge4}n^jp^{r(j-3)}
\operatorname{CT}(\mathscr A_jG^{np^{r-1}}).
tag{8}
```

This identifies the two remaining obligations without suppressing the
tail:

1. the moments of the canonical cubic kernel $\mathscr B$ must contract by
   two powers under each additional Cartier level (one power is lost at
   $p=5$);
2. the quartic moment must contract compatibly with (8).

Terms of logarithmic degree at least five then have enough explicit powers
of $p$: for $j\ge5$, $r\ge2$, and $p\ge5$,

```math
(r-1)(j-5)+\delta_p\ge v_p(j!).
tag{9}
```

Thus the degree-four term is the only tail term on the numerical boundary.
The first-residue theorem proves the reduction of (8) modulo $p$, but does
not by itself provide the growing precision in (2).

## 5. One exact residual Cartier operator

The cancellation in (6) can be packaged without separating the shells.
For a positive integer $X$, define

```math
\mathscr K_X
=\mathcal C_p\!\left(H(\exp(XL_p)-1)\right).
\tag{10}
```

If $N=np^r$, $M=N/p$, and $R=M/p$, the exact defect formula gives

```math
D_{p,r}(n)=\operatorname{CT}(\mathscr K_NG^M).
\tag{11}
```

Since $M=pR$, identity $G^p/G(x^p,t^p)=\exp(pL_p)$ and one more
Cartier extraction yield

```math
\operatorname{CT}(\mathscr K_NG^M)
=\operatorname{CT}
\mathcal C_p\!\left(\mathscr K_N\exp(ML_p)\right)G^R.
\tag{12}
```

Consequently the entire left side of (3), including all three shell
cancellations, is the single moment

```math
\boxed{
E_{p,r}(n)=\operatorname{CT}(\mathscr S_MG^R),
\qquad
\mathscr S_M=
\mathcal C_p\!\left(\mathscr K_{pM}\exp(ML_p)\right)-p^3\mathscr K_M.
}
\tag{13}
```

This is a stricter target than the qualitative phrase "excellent
Frobenius": it gives the exact residual series whose moments must be
estimated.

There is also a universal homogeneous expansion.  The linear coefficient
of $\mathscr K_X$ vanishes, because no monomial of $HL_p$ has both
exponents divisible by $p$.  Therefore

```math
\mathscr S_M=\sum_{d\ge2}M^d\mathscr S_d,
\tag{14}
```

where

```math
\boxed{
\mathscr S_d=
\sum_{j=2}^{d}
\frac{p^j}{j!(d-j)!}
\mathcal C_p\!\left(\mathcal C_p(HL_p^j)L_p^{d-j}\right)
-\frac{p^3}{d!}\mathcal C_p(HL_p^d).
}
\tag{15}
```

In particular,

```math
\mathscr S_2=
\frac{p^2}{2}\left(\mathcal C_p^2(HL_p^2)
-p\mathcal C_p(HL_p^2)\right).
\tag{16}
```

Thus the last conjecture has been reduced to a concrete sequence of
Cartier-coefficient estimates.  The quadratic and cubic pieces of
(14), after formal integration by parts, are exactly the cubic-kernel
contraction in Section 4; $\mathscr S_4$ is the boundary correction.
Formula (15) prevents a proof from silently dropping the mixed terms
created when $G^{pR}$ is pulled through Cartier.

## 6. Why excellent Frobenius is a guide, not a proof

Beukers and Vlasenko prove coefficient supercongruences from excellent
Frobenius lifts in their
[*Dwork crystals III*](https://arxiv.org/abs/2105.14841).  They also state
the corresponding modulo-$p^{2s}$ quotient phenomenon as a conjecture in
their symmetric Calabi--Yau setting.  No theorem there applies directly
to (8): our fixed prefix factor $H$, the Newton data, and the required
Hasse--Witt/excellent-lift hypotheses have not been matched.  Equation (8)
and the three-shell identity (6) are the concrete arithmetic obligations
for this family.

## 7. Verification

Run

```text
python verification/related/verify_bala_august_higher_defect.py
```

The checker verifies (3), (5)--(6), the conjectured exponent over a broad
modular grid, and sharp witnesses.  These checks certify the reduction and
the reported boundary; they are not a proof of (2).
