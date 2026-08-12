# The first defect in Bala's negative-binomial tower

## Status and scope

Peter Bala's August update singled out

```math
u(N)=\sum_{k=0}^{N}\binom{-N}{k}\binom{-2N}{k}
```

and suggested a stronger-than-cubic tower.  The stronger exponent is false,
while the ordinary cubic tower

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{3r}}
```

is proved for every prime $p\geq5$ in
[the prefix-Cartier theorem](MixedNegativeBinomialCubicTower.md).  The August
computations also suggested that the normalized defect itself stabilizes.
This note isolates the exact first obstruction to that stabilization.

The result here proves the first-residue stabilization conjecture.  It shows
that every first normalized defect is a single Cartier moment, gives an exact
criterion for when the cubic exponent is sharp, and proves that its canonical
defect kernel is coefficientwise fixed by Cartier modulo $p$.  The last step
is an elementary Bernoulli calculation: a diagonal Moebius difference turns
the reciprocal-cube transgression into a piecewise-linear Green kernel.

## 1. Prefix constant term

It is useful to keep the positive-slope family during the calculation.  Put

```math
U_{a,b;c}(N)=
\sum_{k=0}^{cN}\binom{-aN}{k}\binom{-bN}{k},
```

where $a,b,c$ are positive integers, and set

```math
H(t)=\frac1{1-t},
\qquad
G(x,t)=\frac{t^{-c}}{(1-x)^a(1-t/x)^b}.
```

Then

```math
U_{a,b;c}(N)=\operatorname{CT}_{x,t}H(t)G(x,t)^N.
\tag{1}
```

For a prime $p\geq5$, let $\mathcal C_p$ be the two-variable Cartier
operator

```math
\mathcal C_p\!\left(\sum q_{i,j}x^it^j\right)
=\sum q_{pi,pj}x^it^j
```

and define

```math
V_p(z)=\sum_{\substack{j\geq1\\p\nmid j}}\frac{z^j}{j},
\qquad
L_p(x,t)=aV_p(x)+bV_p(t/x).
\tag{2}
```

The two identities driving the cubic proof are

```math
\frac{G(x,t)^p}{G(x^p,t^p)}=\exp(pL_p(x,t))
\tag{3}
```

and

```math
\mathcal C_p(HL_p^2)=p(E_xK_1+E_tK_2),
\qquad
E_x=x\partial_x,\quad E_t=t\partial_t,
\tag{4}
```

for $p$-integral Laurent series $K_1,K_2$.  Lemma 2 of the prefix-Cartier
note constructs such a pair monomial by monomial.  Fix any one such pair.

## 2. The defect kernel

Define the $p$-integral Laurent series

```math
\mathscr B_{p;a,b,c}
=\frac16\mathcal C_p(HL_p^3)
-\frac12\left(
K_1E_x\log G+K_2E_t\log G
\right).
\tag{5}
```

Although the displayed representative depends on the choice in (4), all
of its constant-term moments against powers of $G$ do not.  Indeed, formal
integration by parts gives

```math
\operatorname{CT}(E_xK_1)G^M
=-M\operatorname{CT}K_1G^M E_x\log G,
\tag{6}
```

and the analogous identity in $t$.  Thus only the divergence
$E_xK_1+E_tK_2$, which is fixed by (4), enters the moment.

For $M\geq0$ write

```math
\Theta_{p;a,b,c}(M)
=\operatorname{CT}_{x,t}
\mathscr B_{p;a,b,c}(x,t)G(x,t)^M
\pmod p.
\tag{7}
```

## 3. First-defect theorem

### Theorem 1

Let $p\geq5$ be prime and $a,b,c,n,r$ be positive integers.  Define

```math
D_{p,r}^{a,b;c}(n)
=U_{a,b;c}(np^r)-U_{a,b;c}(np^{r-1}).
```

Then $p^{3r}$ divides $D_{p,r}^{a,b;c}(n)$ and

```math
\boxed{
\frac{D_{p,r}^{a,b;c}(n)}{p^{3r}}
\equiv
n^3\Theta_{p;a,b,c}(np^{r-1})
\pmod p.
}
\tag{8}
```

Consequently,

```math
v_p\!\left(D_{p,r}^{a,b;c}(n)\right)=3r
```

if and only if the moment on the right of (8) is nonzero modulo $p$.
If the moment vanishes, the congruence gains at least one further power of
$p$.

### Proof

Put $N=np^r$ and $M=N/p$.  Equations (1)--(3), together with
$\mathcal C_p(H)=H$, give the exact defect expansion

```math
D_{p,r}^{a,b;c}(n)
=\operatorname{CT}
H(t)G(x^p,t^p)^M\bigl(\exp(NL_p)-1\bigr).
\tag{9}
```

The linear term has zero constant coefficient because every $x$-exponent
of $G(x^p,t^p)^M$ is divisible by $p$, whereas every monomial of $L_p$ has
$x$-exponent prime to $p$.

Apply Cartier to the quadratic term and use (4).  Formal integration by
parts yields

```math
\begin{aligned}
\frac{N^2}{2}
\operatorname{CT}\mathcal C_p(HL_p^2)G^M
&=\frac{N^2p}{2}
\operatorname{CT}(E_xK_1+E_tK_2)G^M\\
&=-\frac{N^2pM}{2}
\operatorname{CT}
\left(K_1E_x\log G+K_2E_t\log G\right)G^M\\
&=-\frac{n^3p^{3r}}2
\operatorname{CT}
\left(K_1E_x\log G+K_2E_t\log G\right)G^M.
\end{aligned}
\tag{10}
```

The cubic term is

```math
\frac{N^3}{6}
\operatorname{CT}\mathcal C_p(HL_p^3)G^M
=\frac{n^3p^{3r}}6
\operatorname{CT}\mathcal C_p(HL_p^3)G^M.
\tag{11}
```

Every exponential term of degree $j\geq4$ is divisible by
$p^{3r+1}$.  For $j=4$ this follows from
$v_p(N^4/4!)-3r\geq r\geq1$.  For $j\geq5$, Legendre's bound
$v_p(j!)\leq(j-1)/(p-1)$ gives the same conclusion.  Divide (9) by
$p^{3r}$ and combine (10)--(11).  This is (8).  The valuation statement is
immediate. $\square$

## 4. One obstruction to scale stability

The August stabilization conjecture begins with

```math
\frac{D_{p,r}^{1,2;1}(n)}{p^{3r}}
\equiv
\frac{D_{p,r-1}^{1,2;1}(n)}{p^{3r-3}}
\pmod p.
\tag{12}
```

Theorem 1 reduces (12) to a single moment identity.  In characteristic
$p$,

```math
G(x,t)^{pm}=G(x^p,t^p)^m,
```

so

```math
\Theta_{p;a,b,c}(pm)
=\operatorname{CT}\mathcal C_p(\mathscr B_{p;a,b,c})G^m.
\tag{13}
```

Combining (8) and (13) gives the following exact reduction.

### Corollary 2

For $r\geq2$ and $m=np^{r-2}$,

```math
\frac{D_{p,r}^{a,b;c}(n)}{p^{3r}}
-
\frac{D_{p,r-1}^{a,b;c}(n)}{p^{3r-3}}
\equiv
n^3\operatorname{CT}
\left(\mathcal C_p\mathscr B_{p;a,b,c}
-\mathscr B_{p;a,b,c}\right)G^m
\pmod p.
\tag{14}
```

Therefore the first residue of the normalized defect stabilizes at every
level once the single kernel class $\mathscr B_{p;a,b,c}$ is Cartier-fixed
in its moments against $G^m$.  No new estimate is required at every level:
the entire remaining problem is the horizontal identity

```math
\operatorname{CT}
\left(\mathcal C_p\mathscr B_{p;a,b,c}
-\mathscr B_{p;a,b,c}\right)G^m=0
\quad(m\geq0).
\tag{15}
```

This is the precise point at which the recent Gaussian-prime work is
useful methodologically.  There, a first affine defect and a uniformly
deeper logarithmic tail classify the critical shell.  Here, (5) is the
first defect kernel, terms of degree at least four form the uniformly
deeper tail, and (7) stratifies the sharp and exceptional parameter
values.  The analogy supplies a proof organization; it does not identify
Gaussian and rational primes.

## 5. A one-series tangent certificate

Identity (15) still quantifies over every $m$.  It has a stronger local
sufficient condition involving only one formal Laurent series.

For any $p$-integral Laurent series $J$, define its $G$-tangent divergence

```math
\mathcal T_G(J)=
E_x\!\left((E_t\log G)J\right)
-E_t\!\left((E_x\log G)J\right).
\tag{16}
```

### Lemma 3

For every $m\geq0$,

```math
\operatorname{CT}\mathcal T_G(J)G^m=0.
\tag{17}
```

### Proof

Formal integration by parts gives

```math
\operatorname{CT}
E_x\!\left((E_t\log G)J\right)G^m
=-m\operatorname{CT}
(E_t\log G)J(E_x\log G)G^m,
```

whereas

```math
-\operatorname{CT}
E_t\!\left((E_x\log G)J\right)G^m
=m\operatorname{CT}
(E_x\log G)J(E_t\log G)G^m.
```

The two terms cancel. $\square$

### Corollary 4

The family-level first-residue stabilization follows if one constructs a
$p$-integral $J_{p;a,b,c}$ satisfying

```math
\boxed{
\mathcal C_p\mathscr B_{p;a,b,c}
-\mathscr B_{p;a,b,c}
\equiv \mathcal T_G(J_{p;a,b,c})\pmod p.
}
\tag{18}
```

Thus the next proof obligation is finite and local: construct one tangent
certificate (18).  Such a certificate is stronger than the moment
identity (15), but it proves all bases and all levels simultaneously.

### 5.1 Unimodular transport normal form

The certificate equation becomes especially concrete after the monomial
change of variables

```math
y=t/x,
\qquad t=xy.
\tag{19}
```

The induced map on exponent lattices is unimodular.  Hence an exponent is
divisible by $p$ before the change exactly when it is divisible by $p$
after the change, so the Cartier operator remains the ordinary
two-variable Cartier operator.  In the new coordinates,

```math
H=\frac1{1-xy},
\qquad
G=\frac{x^{-c}y^{-c}}{(1-x)^a(1-y)^b},
\qquad
L_p=aV_p(x)+bV_p(y).
\tag{20}
```

Write $D_x=x\partial_x$ and $D_y=y\partial_y$.  The old Euler operators
become

```math
E_x=D_x-D_y,
\qquad E_t=D_y.
```

Consequently,

```math
E_t\log G=-c+\frac{by}{1-y},
\qquad
(E_x+E_t)\log G=-c+\frac{ax}{1-x}.
```

The cross-derivative terms in (16) cancel, leaving the transport normal
form

```math
\boxed{
\mathcal T_G(J)=
\left(-c+\frac{by}{1-y}\right)D_xJ
-\left(-c+\frac{ax}{1-x}\right)D_yJ.
}
\tag{21}
```

Thus (18) is a first-order coefficient recursion, not an unspecified
cohomological existence problem.  If

```math
J=\sum_{m,n}j_{m,n}x^my^n,
\qquad
R=\mathcal C_p\mathscr B_{p;a,b,c}-\mathscr B_{p;a,b,c}
=\sum_{m,n}r_{m,n}x^my^n,
```

then (21) is equivalent coefficientwise to

```math
r_{m,n}
=c(n-m)j_{m,n}
+bm\sum_{q\geq1}j_{m,n-q}
-an\sum_{q\geq1}j_{m-q,n}.
\tag{22}
```

On any cone where the Laurent expansion is bounded below, (22) is
triangular in total degree.  Away from the resonant classes
$c(n-m)\equiv0\pmod p$, it determines $j_{m,n}$ uniquely from earlier
coefficients.  The remaining proof obligation is therefore explicit:
show that the right side has the required cancellation on those resonant
classes.  This is the rational-prime analogue of isolating the critical
shell in the Gaussian calculation.

### 5.2 A stronger coefficientwise Frobenius target

The transport equation is more rigid than Lemma 3 requires.  Work in the
coordinates (19), and write

```math
\frac1p\mathcal C_p(HL_p^2)=D_xP+D_yQ.
\tag{23}
```

Choose $P,Q$ canonically, monomial by monomial: assign the coefficient at
$(m,n)$ to $D_xP$ when $m\ne0$ and
$v_p(m)\leq v_p(n)$, and otherwise assign it to $D_yQ$.  In these
coordinates the kernel (5) becomes

```math
\mathscr B_{p;a,b,c}
=\frac16\mathcal C_p(HL_p^3)
-\frac12\left(PD_x\log G+QD_y\log G\right).
\tag{24}
```

The coefficientwise strengthening is

```math
\boxed{
\mathcal C_p\mathscr B_{p;a,b,c}
\equiv\mathscr B_{p;a,b,c}\pmod p.
}
\tag{25}
```

Identity (25) implies Corollary 4 with $J=0$, and hence the first normalized
defect stabilizes for the full positive-slope prefix family.

The quadratic part of (25) reduces to the lifted reciprocal-square bound

```math
v_p\!\left(
[x^{p^2m}y^{p^2n}]HL_p^2
-p[x^{pm}y^{pn}]HL_p^2
\right)
\geq3+\min\{v_p(m),v_p(n)\}.
\tag{26}
```

This bound can in fact be proved by a second unit-block lift.

### Lemma 5 (lifted reciprocal square)

For every prime $p\geq5$ and $m,n\geq0$, (26) holds, with
$v_p(0)=+\infty$.

### Proof

For $j\geq2$ put

```math
R_j(pL)=
\sum_{\substack{1\leq u\leq pL\\p\nmid u}}u^{-j}.
```

First we prove

```math
R_2(p^2L)-pR_2(pL)\in p^{3+v_p(L)}\mathbb Z_p.
\tag{27}
```

The case $L=0$ is tautological, so assume $L>0$.
Write

```math
B(q)=\sum_{u=1}^{p-1}(pq+u)^{-2}.
```

If $\ell=v_p(L)$, grouping the $pL$ blocks as $q+jL$, with
$0\leq q<L$ and $0\leq j<p$, gives

```math
R_2(p^2L)-pR_2(pL)
=\sum_{q=0}^{L-1}\sum_{j=0}^{p-1}\bigl(B(q+jL)-B(q)\bigr).
\tag{28}
```

Expand each unit denominator $p$-adically.  The term of Taylor degree $h$
contains

```math
(pL)^h\left(\sum_{j=0}^{p-1}j^h\right)
\left(\sum_{u=1}^{p-1}(pq+u)^{-h-2}\right).
```

For $h=1$, the first power sum contributes a factor $p$, while the last
sum is also divisible by $p$ because it reduces to
$\sum_{u\in\mathbb F_p^\times}u^{-3}=0$.  Its valuation is therefore at
least $3+\ell$.  For $h\geq2$, the power sum in $j$ is divisible by $p$
unless $p-1\mid h$.  In the latter case $h\geq p-1\geq4$.  Thus every
remaining Taylor term also has valuation at least $3+\ell$.  The series
converges $p$-adically, proving (27).  The same finite-field power-sum
identity also gives

```math
R_3(pL)\in p\mathbb Z_p.
\tag{29}
```

Now define the common two-denominator block

```math
F_p(A,B;L)=
\sum_{\substack{1\leq u\leq pL\\p\nmid u}}
\frac1{(pA-u)(pB-u)}.
```

Writing $h_q(A,B)=\sum_{i=0}^qA^iB^{q-i}$, geometric expansion gives

```math
F_p(A,B;L)=
\sum_{q\geq0}p^q h_q(A,B)R_{q+2}(pL).
\tag{30}
```

Suppose $p^s$ divides $A,B,L$.  In the difference
$F_p(pA,pB;pL)-pF_p(A,B;L)$, the $q=0$ term is covered by (27).  The
$q=1$ term is

```math
p^2(A+B)\bigl(R_3(p^2L)-R_3(pL)\bigr),
```

which lies in $p^{3+s}\mathbb Z_p$ by (29).  For $q\geq2$, each of the
two terms has valuation at least

```math
q+1+qs\geq3+s.
```

Hence

```math
F_p(pA,pB;pL)-pF_p(A,B;L)\in p^{3+s}\mathbb Z_p.
\tag{31}
```

Finally, the mixed coefficient of $HV_p(x)V_p(y)$ at $(pM,pN)$ is
$F_p(M,N;\min\{M,N\})$.  The two pure-square boundary coefficients are
$[z^{p|M-N|}]V_p(z)^2$, which equals
$-F_p(0,|M-N|;|M-N|)$.  Apply (31) to these three pieces.  Since
$p^{\min\{v_p(m),v_p(n)\}}$ divides $m,n,m-n$, their linear combination
is exactly (26); the case $m=n=0$ is immediate. $\square$

Bound (26) makes both canonical primitives $P,Q$ Cartier-fixed modulo
$p$.  The only remaining part of (25) is therefore the reciprocal-cube
transgression obtained by applying Cartier to (24).  This is exactly where
the Frobenius lift, rather than generic compactness or recurrence machinery,
carries the problem.

### 5.3 The reciprocal-cube transgression

The last identity can be written without formal derivatives.  Let
$P_{m,n},Q_{m,n}$ denote the coefficients of the canonical primitives, and
put

```math
\begin{aligned}
\Delta^{(3)}_{m,n}
&=[x^{p^2m}y^{p^2n}]HL_p^3-[x^{pm}y^{pn}]HL_p^3,\\
U^P_{m,n}
&=\sum_{\substack{1\leq q\leq pm\\p\nmid q}}P_{pm-q,pn},\\
U^Q_{m,n}
&=\sum_{\substack{1\leq q\leq pn\\p\nmid q}}Q_{pm,pn-q}.
\end{aligned}
\tag{32}
```

Then coefficientwise Frobenius fixedness (25) is equivalent to

```math
\boxed{
\Delta^{(3)}_{m,n}
\equiv3aU^P_{m,n}+3bU^Q_{m,n}\pmod p
\quad(m,n\geq0).
}
\tag{33}
```

Indeed, in the coefficient of $PD_x\log G$ at $(pm,pn)$, split the
positive $x$-shifts into $q=pu$ and $p\nmid q$.  The divisible shifts
reduce to the corresponding coefficient at $(m,n)$ because
$P_{pr,ps}\equiv P_{r,s}\pmod p$; the constant term $-cP$ cancels for the
same reason.  Only $aU^P_{m,n}$ remains.  The $Q$ term is identical in the
$y$ coordinate.  Multiplying the difference of (24) by $6$ gives (33).

Thus the last step no longer contains $G$, $c$, a constant-term pairing, or
an unspecified tangent primitive.  It is the unit-shift identity (33) for
the quadratic block potentials.  In particular, its truth is independent of
the prefix slope $c$.

We now prove it.  Put $B=B_{p-3}$ and

```math
\lambda=\frac23B\pmod p.
\tag{34}
```

For $1\leq s\leq p-1$, write

```math
H_s=\sum_{j=1}^s\frac1j\pmod p,
\qquad H_0=0.
```

The elementary depth-two harmonic identity needed below is

```math
\sum_{s=1}^{p-1}\frac{H_{s-1}}{s^2}
=\sum_{s=1}^{p-1}\frac{H_s}{s^2}
=B_{p-3}\pmod p.
\tag{35}
```

Indeed, the two sums differ by $\sum s^{-3}=0$.  For the first, replace
$s^{-2}$ and $j^{-1}$ by $s^{p-3}$ and $j^{p-2}$ and use Faulhaber's
formula on $\sum_{j=1}^{s-1}j^{p-2}$.  After summing over
$s\in\mathbb F_p^\times$, every Bernoulli term vanishes except the term
with index $p-3$; its coefficient is

```math
\frac{-1}{p-1}\binom{p-1}{p-3}=1\pmod p.
```

Define the finite logarithm

```math
W(z)=\sum_{s=1}^{p-1}\frac{z^s}{s}\in\mathbb F_p[z].
```

Coefficient periodicity gives

```math
V_p(z)=\frac{W(z)}{1-z^p}\quad\text{in }\mathbb F_p[[z]].
\tag{36}
```

If $h_s=[z^s]W(z)^2$, then

```math
h_s=\frac{2H_{s-1}}s,
\qquad
h_{p-s}=-\frac{2H_s}s
\quad(1\leq s\leq p-1).
\tag{37}
```

The second equality follows from $H_{p-s-1}=H_s$ modulo $p$, while
$z^{2p}W(1/z)^2=W(z)^2$ also gives $h_{p+s}=h_{p-s}$.  Equations
(35)--(37) give

```math
\begin{aligned}
[z^p]W^3&=-2B,& [z^{2p}]W^3&=2B,\\
\sum_{s=1}^{p-1}\frac{h_s}{s}&=2B,&
\sum_{s=1}^{p-1}\frac{h_{p+s}}s&=-2B.
\end{aligned}
\tag{38}
```

Let $E(z)=1+z+\cdots+z^{p-1}$.  Since
$H=E(xy)/(1-x^py^p)$, applying Cartier to (36) and using (38) yields the
finite polynomial calculation

```math
\begin{aligned}
\mathcal C_p\!\left(E(xy)W(x)^3\right)&=2B(x^2-x),\\
\mathcal C_p\!\left(E(xy)W(x)^2W(y)\right)&=2Bxy(1-x),\\
\mathcal C_p\!\left(E(xy)W(x)W(y)^2\right)&=2Bxy(1-y),\\
\mathcal C_p\!\left(E(xy)W(y)^3\right)&=2B(y^2-y).
\end{aligned}
\tag{39}
```

Therefore

```math
\mathcal C_p(HL_p^3)
\equiv2BH\left(
-a^3\frac{x}{(1-x)^2}
-b^3\frac{y}{(1-y)^2}
+3ab(a+b)\frac{xy}{(1-x)(1-y)}
\right)\pmod p.
\tag{40}
```

Every coefficient of the parenthesized expression after multiplication by
$H$, at an exponent $(pm,pn)$, is divisible by $p$: the first two terms
give respectively $p(m-n)_+$ and $p(n-m)_+$, and the mixed term gives
$p\min\{m,n\}$.  Hence a second Cartier application annihilates (40).
It follows that

```math
\Delta^{(3)}_{m,n}\equiv
\begin{cases}
2B\bigl(a^3(m-n)-3ab(a+b)n\bigr),&m\geq n,\\
2B\bigl(b^3(n-m)-3ab(a+b)m\bigr),&n\geq m
\end{cases}
\pmod p.
\tag{41}
```

It remains to calculate the right side of (33).  Let

```math
R_{m,n}=\frac1p[x^{pm}y^{pn}]HL_p^2.
```

The standard harmonic congruences

```math
\sum_{s=1}^{p-1}\frac1s\equiv-\frac{p^2}{3}B\pmod {p^3},
\qquad
\sum_{s=1}^{p-1}\frac1{s^2}\equiv\frac{2p}{3}B\pmod {p^2},
\tag{42}
```

and $\sum s^{-3}\equiv0\pmod p$ imply, by splitting the interval into
blocks of length $p$,

```math
\frac1p[z^{pd}]V_p(z)^2\equiv-\lambda d,
\qquad
\frac1p\sum_{\substack{1\leq u<pM\\p\nmid u}}
\frac1{u(pD+u)}\equiv\lambda M\pmod p.
\tag{43}
```

For completeness, the first identity uses

```math
\sum_{\substack{1\leq u<pd\\p\nmid u}}\frac1u
\equiv-\frac{p^2d^2}{3}B\pmod {p^3},
```

and the second follows by replacing the summand by $u^{-2}$ modulo the
required $p^2$ precision.  Separating the two pure squares and the mixed
term of $L_p^2$ now gives the piecewise-linear Green kernel

```math
\boxed{
R_{m,n}\equiv\lambda\left(
-a^2(m-n)_+-b^2(n-m)_++2ab\min\{m,n\}
\right)\pmod p.
}
\tag{44}
```

In every summand defining $U^P_{m,n}$, the first index $pm-q$ is a
$p$-adic unit and the second is divisible by $p$, so the canonical rule
assigns that coefficient to $P$ and

```math
P_{pm-q,pn}=\frac{R_{pm-q,pn}}{pm-q}.
```

The analogous statement holds for $Q$.  There are $M(p-1)\equiv-M$
units in each interval $1\leq u<pM$.  Substituting (44) and counting the
units below and above the breakpoint gives, when $m\geq n$,

```math
\begin{aligned}
U^P_{m,n}&\equiv
-n\lambda b(b+2a)+(m-n)\lambda a^2,\\
U^Q_{m,n}&\equiv-n\lambda a(a+2b).
\end{aligned}
\tag{45}
```

For $n\geq m$ the formulas are obtained by interchanging
$(a,m,P)$ and $(b,n,Q)$.  Since $3\lambda=2B$, equation (45) gives

```math
3aU^P_{m,n}+3bU^Q_{m,n}
\equiv
2B\bigl(a^3(m-n)-3ab(a+b)n\bigr)
\pmod p
```

when $m\geq n$, and the second case of (41) when $n\geq m$.  This proves
(33), hence (25), and therefore (18) with $J=0$.

### Theorem 6 (first normalized-defect stabilization)

For every prime $p\geq5$ and positive integers $a,b,c,n$, the first
normalized defect is stable through every adjacent pair of levels:

```math
\boxed{
\frac{D_{p,r}^{a,b;c}(n)}{p^{3r}}
\equiv
\frac{D_{p,r-1}^{a,b;c}(n)}{p^{3r-3}}
\pmod p
\qquad(r\geq2).
}
\tag{46}
```

This follows immediately from (25) and Corollary 2.

## 6. Bala's specialization and computation

For $(a,b,c)=(1,2,1)$, exact arithmetic currently gives

```math
\frac{u(np^r)-u(np^{r-1})}{p^{3r}}
\equiv
\frac{u(np^{r-1})-u(np^{r-2})}{p^{3r-3}}
\pmod p
```

through the tested range.  At $n=1$ the common observed residue is

```math
2B_{p-3}\pmod p,
```

agreeing with the proved prime-level Bernoulli formula in the
[August coefficient packet](BalaAugustCoefficientPacket.md).  These
computations agree with Theorem 6.

The same first-residue stability has no failures in the broader exact grid

```math
p\in\{5,7,11\},\quad
1\leq a,b,n\leq4,\quad
1\leq c\leq3,
```

comprising 576 parameter configurations at levels one and two.  They check
the family-level theorem well beyond Bala's original specialization.

Run

```text
python verification/related/verify_bala_august_first_defect.py
python verification/related/verify_bala_august_kernel_frobenius.py
```

The first command runs 1,474 normalized-defect checks.  The second runs
2,428 exact coefficient checks of (25), its canonical primitives, the
lifted square bound (26), the Green-kernel formula (44), the closed cube
formula (41), and the unit-shift transgression (33).

## 7. Literature boundary

This note closes the expansion, tail bookkeeping, and first-residue
stabilization for the first defect.  The higher experimental modulus
recorded in the August follow-on requires further defect kernels beyond
(5), so it is not claimed here.  The separate
[higher-defect reduction](BalaAugustHigherDefectLift.md) rewrites it as an
exact three-level congruence, proves an exact three-shell decomposition,
proves the quartic contraction, and isolates the cubic-kernel contraction
still required.

The formal-derivative language is compatible with Beukers and Vlasenko's
[Dwork crystals III](https://doi.org/10.1093/imrn/rnad101), where higher
formal-derivative modules and Cartier-stable quotients organize
supercongruence mechanisms.  The pure constant-term congruences of Mellit
and Vlasenko
[apply to powers of a Laurent polynomial](https://arxiv.org/abs/1306.5811).
Neither result supplies (18) verbatim: the fixed prefix factor $H(t)$ is
part of the arithmetic here, and no Hasse--Witt or excellent-Frobenius
hypothesis has been verified for this family.  They identify the
cohomological language; equations (34)--(45) provide the elementary
certificate in this particular problem.
