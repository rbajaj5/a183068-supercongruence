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

### 3.1 It is enough to treat $p$-adic unit values of $n$

Write $n=p^tm$ with $p\nmid m$.  Directly from the definitions,

```math
D_{p,r}(n)=D_{p,r+t}(m),
\qquad
Q_{p,r}(n)=p^{3t}Q_{p,r+t}(m).
\tag{6a}
```

Hence the unit case at level $r+t$ gives

```math
v_p\!\left(Q_{p,r}(n)-Q_{p,r-1}(n)\right)
\ge 2r+5t-2-\delta_p,
\tag{6b}
```

which is stronger than (2).  Thus no separate induction on the valuation
of $n$ is required: the unresolved case has $p\nmid n$.

### 3.2 Exact higher-Jacobsthal factorization

Put

```math
J_p(A,B)=\frac{\binom{pA}{pB}}{\binom AB}.
\tag{6c}
```

The scaled summands in (6) admit the exact factorization

```math
\boxed{
f_{pM}(pq)=f_M(q)J_p(M+q,q)J_p(2M+q,q).
}
\tag{6d}
```

Indeed,

```math
f_M(q)=
\frac{M}{M+q}\frac{2M}{2M+q}
\binom{M+q}{q}\binom{2M+q}{q},
```

and the rational prefactor is unchanged by simultaneous multiplication
of $M,q$ by $p$.  Formula (6d) identifies the once- and twice-scaled
pieces of (6) with products of ordinary Jacobsthal quotients.  It is the
precise point at which higher-order binomial approximation can enter.
Aidagulov and Alekseyev's
[*On p-adic approximation of sums of binomial coefficients*](https://arxiv.org/abs/1602.02632)
gives arbitrarily high approximations for suitable fixed-lower-index
linear combinations.  Their theorem does not directly settle (3), since
here the lower index $q$ runs through the shell and the unit shell $A_0$
must cancel its leading term.  Formula (6d), rather than a generic appeal
to Jacobsthal, records the exact specialization still needed.

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

This initially identifies two obligations without suppressing the tail:

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

The next lemma closes the second obligation.

### Lemma 2 (quartic coefficient lift)

Work in the coordinates $y=t/x$, so that

```math
H=\frac1{1-xy},
\qquad
L_p=V_p(x)+2V_p(y).
```

For $p\ge5$, put $\delta_p=1$ at $p=5$ and $0$ otherwise.  Then

```math
\boxed{
v_p\!\left([x^{pm}y^{pn}]HL_p^4\right)
\ge 1-\delta_p+\min\{v_p(m),v_p(n)\}
}
\tag{9a}
```

for $(m,n)\ne(0,0)$, with $v_p(0)=+\infty$.

#### Proof

Let

```math
W(z)=\sum_{a=1}^{p-1}\frac{z^a}{a},
\qquad E(z)=1+z+\cdots+z^{p-1}.
```

Modulo $p$ one has

```math
V_p(z)=\frac{W(z)}{1-z^p},
\qquad H=\frac{E(xy)}{1-x^py^p}.
\tag{9b}
```

For $p\ge7$, direct coefficient extraction gives the five weight-four
finite-logarithm identities

```math
\mathcal C_p\!\left(E(xy)W(x)^iW(y)^{4-i}\right)=0
\qquad(0\le i\le4).
\tag{9c}
```

Here is a short verification that does not invoke an analytic logarithm.
If $h_j(s)=[z^s]W(z)^j$, differentiate $W^j$ to obtain

```math
s h_j(s)=j\sum_{a=1}^{p-1}h_{j-1}(s-a),
\tag{9d}
```

with $h_1(a)=a^{-1}$ on $1\le a<p$, and use
$h_j(jp-s)=(-1)^jh_j(s)$.  Substitution in the coefficient of
$x^{pu}y^{pv}$ on the left of (9c) reduces each of the five cases to a
complete reciprocal sum of total weight four.  Faulhaber's formula
annihilates every residue power sum except the possible weight-four term;
its coefficient is $B_{p-4}=0$ because $p-4>1$ is odd.  This proves
(9c).  At $p=5$ the condition $p-1\mid4$ is exactly the exceptional
residue power sum, so only integrality remains.

For the lift, set

```math
C_s(m,n)=[x^{p^{s+1}m}y^{p^{s+1}n}]HL_p^4.
```

Split each of the four unit denominators into its residue modulo $p$ and
group the diagonal exponent of $H$ in blocks of length $p$.  Expanding
$(pq+a)^{-e}$ in $pq/a$ gives

```math
v_p\!\left(C_{s+1}(m,n)-pC_s(m,n)\right)
\ge s+2-\delta_p
\tag{9e}
```

whenever $p\nmid(m,n)$.  Indeed, the Taylor-degree-zero block is (9c),
and therefore gains two powers of $p$ for $p\ge7$ and one at $p=5$;
every positive Taylor degree contains the additional factor $p^{s+1}$,
while its complete residue power sum is divisible by $p$ unless
$p-1\mid4$, the same exceptional case already recorded by $\delta_p$.
This is the four-denominator analogue of the lifted reciprocal-square
calculation in Lemma 5 of the first-defect note.

Identity (9c) starts the induction, and (9e) gives
$v_p(C_s(m,n))\ge s+1-\delta_p$.  Removing the common power of $p$ from
the original pair $(m,n)$ proves (9a). $\square$

### Corollary 3 (the quartic term is complete)

Let $\mathscr A_4=\mathcal C_p(HL_p^4)/4!$.  The coefficient bound (9a)
allows the canonical monomial-by-monomial assignment

```math
\mathscr A_4=p^{1-\delta_p}(E_xP_4+E_yQ_4)
\tag{9f}
```

with $p$-integral Laurent series $P_4,Q_4$.  Formal integration by parts
therefore gives

```math
v_p\!\left(\operatorname{CT}(\mathscr A_4G^{np^{r-2}})\right)
\ge r-1-\delta_p.
\tag{9g}
```

After multiplication by the explicit factor $p^{r-1}$ in the difference
of the two degree-four terms in (8), this is exactly
$2r-2-\delta_p$.  The term at the higher level has one additional power.
Thus the quartic term satisfies (2).  Terms of degree at least five are
covered by (9), leaving only the cubic-kernel contraction.

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

### 5.1 The single remaining cubic certificate

Put $M=np^{r-2}$ and abbreviate
$\mathscr B=\mathscr B_{p;1,2,1}$.  The cubic contribution at the two
adjacent levels differs by

```math
n^3\operatorname{CT}
\left(\mathcal C_p(\mathscr B\exp(pML_p))-\mathscr B\right)G^M.
\tag{21}
```

Expanding the exponential separates the genuinely critical part:

```math
\begin{aligned}
\mathcal C_p(\mathscr B\exp(pML_p))-\mathscr B
={}&\mathcal C_p\mathscr B-\mathscr B
+pM\mathcal C_p(\mathscr B L_p)\\
&+\sum_{h\ge2}\frac{(pM)^h}{h!}
\mathcal C_p(\mathscr B L_p^h).
\end{aligned}
\tag{22}
```

For $h\ge2$ and $p\ge5$,

```math
v_p\!\left(\frac{(pM)^h}{h!}\right)
\ge 2v_p(M)+2,
\tag{23}
```

so the tail already exceeds the required precision.  The whole August
conjecture is therefore equivalent, after the proved reductions above, to
the one estimate

```math
\boxed{
v_p\!\left(
\operatorname{CT}
\left(\mathcal C_p\mathscr B-\mathscr B
+pM\mathcal C_p(\mathscr B L_p)\right)G^M
\right)
\ge2v_p(M)+2-\delta_p.
}
\tag{24}
```

The coefficientwise theorem
$\mathcal C_p\mathscr B\equiv\mathscr B\pmod p$ proves only the first
power in (24).  Moreover, the two displayed summands should not be
estimated separately: they are the Frobenius and connection pieces of one
second-order tangent class.  Equation (24) is the remaining proof
obligation, not a claimed consequence of the first-residue theorem.

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
