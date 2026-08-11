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

The result here is a **proved reduction**, not a proof of the full
stabilization conjecture.  It shows that every first normalized defect is a
single Cartier moment, gives an exact criterion for when the cubic exponent
is sharp, and reduces the next congruence to one Frobenius-fixed kernel
identity.

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
computations support (15), but they do not replace its proof.

The same first-residue stability has no failures in the broader exact grid

```math
p\in\{5,7,11\},\quad
1\leq a,b,n\leq4,\quad
1\leq c\leq3,
```

comprising 576 parameter configurations at levels one and two.  This is
evidence that (15) belongs to the whole positive-slope prefix family rather
than to one isolated sequence.

Run

```text
python verification/related/verify_bala_august_first_defect.py
```

for the standalone 1,474-check exact regression certificate.

## 7. Literature boundary and next obligation

This note closes the expansion and tail bookkeeping for the first defect.
The unresolved mathematical statement is now (15); the concrete stronger
certificate is (18).  The higher experimental modulus recorded in the
August follow-on requires further defect kernels beyond (5), so it is not
claimed here.

The formal-derivative language is compatible with Beukers and Vlasenko's
[Dwork crystals III](https://doi.org/10.1093/imrn/rnad101), where higher
formal-derivative modules and Cartier-stable quotients organize
supercongruence mechanisms.  The pure constant-term congruences of Mellit
and Vlasenko
[apply to powers of a Laurent polynomial](https://arxiv.org/abs/1306.5811).
Neither result proves (18) verbatim: the fixed prefix factor $H(t)$ is part
of the arithmetic here, and no Hasse--Witt or excellent-Frobenius
hypothesis has been verified for this family.  They identify the right
cohomological language; Lemma 3 isolates the elementary certificate still
needed in this particular problem.
