# The two remaining A376 Apéry companions

**Status:** the A376458 nested sum is collapsed to one signed
four-binomial sum, its full ordinary cubic tower is proved, and its
conjectured prime-level `p^5` congruence is proved for every `p>=7`;
A376466 has a homogeneous negative-coordinate row identity, while its
proposed shifted tower is refuted by an exact counterexample; the ordinary
A376466 tower and the higher A376458 bonus remain open

The last two records treated in this packet are
[A376458](https://oeis.org/A376458) and
[A376466](https://oeis.org/A376466). Both are transforms of the crystal-ball
triangle [A108625](https://oeis.org/A108625), but the occurrence of `N-1`
initially hides the homogeneous coordinates needed for Straub's theorem.
For A376466, the identity in Section 7 restores homogeneous coordinates for
the shifted row, but a separate aggregate unit-shell cancellation is still
needed for the outer sum.

This note gives a common exact representation and closes the strongest
first-level assertion on A376458.

## 1. The common row polynomial

Write

```math
T(m,k)=sum_{j=0}^k
\binom mj^2\binom{m+k-j}{k-j}.
\tag{1}
```

The row generating function on A108625 gives the equivalent identity

```math
T(m,k)=sum_{j=0}^m
\binom mj\binom{m+j}{j}\binom kj.
\tag{2}
```

For completeness, both sides of (2), summed over `k>=0` with weight `x^k`,
are

```math
\frac{1}{1-x}
P_m\!\left(\frac{1+x}{1-x}\right)
=\frac{\sum_j\binom mj^2x^j}{(1-x)^{m+1}},
\tag{3}
```

where `P_m` is the Legendre polynomial.

Define

```math
H_N(X)=sum_{j=0}^{N-1}
\binom{N-1}{j}\binom{N+j-1}{j}X^j.
\tag{4}
```

This shifted row is the common factor in both records.

## 2. A376458 collapses to one sum

The OEIS definition is

```math
A(N)=sum_{k=0}^N(-1)^{N+k}
\binom Nk\binom{N+k}{k}T(N-1,N-k).
\tag{5}
```

### Theorem 1 (binomial-transform collapse)

For every `N>=1`,

```math
\boxed{
A(N)=sum_{j=0}^{N-1}(-1)^j
\binom Nj^2\binom{N-1}{j}\binom{N+j-1}{j}.}
\tag{6}
```

Equivalently, if

```math
R_N(X)=sum_{j=0}^N(-1)^j\binom Nj^2X^j,
\tag{7}
```

then

```math
A(N)=\operatorname{CT}_X H_N(X^{-1})R_N(X).
\tag{8}
```

#### Proof

Insert (2) into (5) and interchange the finite sums. The coefficient of
`binom(N-1,j)binom(N+j-1,j)` is

```math
S_{N,j}=sum_{k=0}^N(-1)^{N+k}
\binom Nk\binom{N+k}{k}\binom{N-k}{j}.
\tag{9}
```

Use

```math
\binom Nk\binom{N-k}{j}
=\binom Nj\binom{N-j}{k}
```

and `(-1)^k binom(N+k,k)=binom(-N-1,k)`. Generalized Vandermonde gives

```math
S_{N,j}=(-1)^N\binom Nj
\binom{-j-1}{N-j}=(-1)^j\binom Nj^2.
\tag{10}
```

Substitution proves (6), and (8) is coefficient pairing. QED

The summand can also be written

```math
\binom Nj^2\binom{N-1}{j}\binom{-N}{j},
\tag{11}
```

so it is a four-block signed multivariate Apéry coefficient with the affine
vector `(N,N,N-1,-N)`. The `-1` is precisely why homogeneous scaling does
not close the full tower automatically.

## 3. The prime-level fifth power

### Theorem 2

For every prime `p>=7`,

```math
\boxed{A(p)\equiv A(1)\pmod {p^5}.}
\tag{12}
```

#### Proof

Here `A(1)=1`. For `1<=j<p`, let `t_j` be the `j`-th summand of (6).
The elementary product formulas for the four binomial coefficients give

```math
t_j=\frac{p^3}{j^3}
\left(1-\frac pj\right)
\prod_{h=1}^{j-1}
\left(1-\frac ph\right)^3
\left(1+\frac ph\right).
\tag{13}
```

Consequently, modulo `p^5`,

```math
t_j\equiv\frac{p^3}{j^3}
\left(1-p\left(2H_{j-1}+\frac1j\right)\right),
\qquad
H_m=\sum_{h=1}^m\frac1h.
\tag{14}
```

The complete reciprocal-cube sum satisfies

```math
\sum_{j=1}^{p-1}j^{-3}\equiv0\pmod {p^2}.
\tag{15}
```

Indeed, pair `j` with `p-j`; the pair is `-3p j^(-4)` modulo `p^2`, and
the half reciprocal-fourth-power sum vanishes modulo `p` because `p>=7`.

For the coefficient of `p^4` in (14), put

```math
H(1,3)=\sum_{1<=h<j<=p-1}\frac{1}{h j^3}.
```

Reversal gives `H(1,3)=H(3,1)` modulo `p`, while the shuffle identity gives

```math
H(1)H(3)=H(1,3)+H(3,1)+H(4).
```

All three single harmonic sums on the two sides vanish modulo `p`, so
`H(1,3)=0` modulo `p`. Summing (14), and using (15), proves (12). QED

The lower boundary is sharp:

```math
A(5)-A(1)=-3750=-6\cdot5^4.
\tag{16}
```

Thus the `p>=7` range on the OEIS record is essential.

## 4. A376466 as the same coefficient pairing

Define the signed Apéry polynomial

```math
Q_N(Y)=sum_{k=0}^N(-1)^{N+k}
\binom Nk\binom{N+k}{k}^2Y^k
\tag{17}
```

and its translated coefficients

```math
U_N(j)=[X^j]Q_N(1+X)
=sum_{k=j}^N(-1)^{N+k}
\binom Nk\binom{N+k}{k}^2\binom kj.
\tag{18}
```

These coefficients have a sign-free bivariate representation.

### Lemma 3 (finite-difference form)

For `0<=j<=N`,

```math
\boxed{
U_N(j)=\binom Nj[x^Ny^N]
(1+x)^{N+j}(1+y)^{N+j}(x+y+xy)^{N-j}.}
\tag{18a}
```

#### Proof

Put `k=N-l` in (18) and use

```math
\binom Nl\binom{N-l}{j}
=\binom Nj\binom{N-j}{l}.
```

This gives

```math
U_N(j)=\binom Nj\sum_{l=0}^{N-j}(-1)^l
\binom{N-j}{l}\binom{2N-l}{N}^2.
```

Write each squared binomial as the coefficient of `x^Ny^N` in
`(1+x)^(2N-l)(1+y)^(2N-l)` and perform the binomial sum over `l`.
The factor in parentheses becomes

```math
\left(1-\frac1{(1+x)(1+y)}\right)^{N-j},
```

which proves (18a). QED

The OEIS definition of A376466 and (2) immediately give the following.

### Theorem 3 (common pairing)

For every `N>=1`,

```math
\boxed{
B(N)=\sum_{j=0}^{N-1}
\binom{N-1}{j}\binom{N+j-1}{j}U_N(j)
=\operatorname{CT}_X H_N(X^{-1})Q_N(1+X).}
\tag{19}
```

Thus A376458 and A376466 differ only in the second polynomial paired with
the same shifted row `H_N`:

```math
A(N)=\langle H_N,R_N\rangle,
\qquad
B(N)=\langle H_N,Q_N(1+X)\rangle.
\tag{20}
```

This is an exact structural relation, not a proof that their defects are
equal.

Lemma 3 also turns (19) into one constant term of adjacent powers. Define

```math
L=\frac{(1+x)(1+y)(x+y+xy)}{xy},
\qquad
R=\frac{(1+x)(1+y)}{x+y+xy},
```

and the Laurent polynomials

```math
P=(1+w)\left(1+z^{-1}+z^{-1}w^{-1}\right),
```

```math
Q=L(1+Rz)
=\frac{(1+x)(1+y)}{xy}
\left(x+y+xy+z(1+x)(1+y)\right).
```

Then (18a), followed by coefficient pairing first in `z` and then in `w`,
gives

```math
\boxed{
B(N)=\operatorname{CT}_{x,y,z,w}Q^N P^{N-1}.}
\tag{20a}
```

Unlike a diagonal `CT((PQ)^N)`, (20a) retains one adjacent exponent. It
therefore identifies the surviving ordinary A376466 problem as a shifted
Cartier problem; it does not put the sequence directly under the
homogeneous multivariate theorem.

### Theorem 4 (the proposed shifted A376466 tower is false)

The A376466 page proposes, in particular,

```math
B(np-1)\equiv B(n-1)\pmod {p^3}
\tag{21}
```

for every `p>=5` and positive `n`. At the first composite-index instance,
`p=5,n=2`, its own sequence values give

```math
B(9)-B(1)
=18063466831218981-3
=18063466831218978
\equiv3\pmod 5.
\tag{22}
```

Thus the claimed congruence fails even modulo `p`, not only at the proposed
cubic depth. Even the pure-prime line does not iterate: exact arithmetic
gives

```math
v_5(B(24)-B(4))=4<6.
\tag{23}
```

The displayed first-level examples (`n=r=1`) are therefore isolated
boundary phenomena; they do not imply either the all-`n` or the all-level
shifted tower.

## 5. The remaining Frobenius shell

For either `V_N=R_N` or `V_N=Q_N(1+X)`, write `v_N(j)=[X^j]V_N` and
`h_N(j)=[X^j]H_N`. At an adjacent level `N=pM`, (20) gives the exact split

```math
\begin{aligned}
\langle H_{pM},V_{pM}\rangle-
\langle H_M,V_M\rangle
={}&\sum_j\bigl(h_{pM}(pj)v_{pM}(pj)-h_M(j)v_M(j)\bigr)\\
&+\sum_{p\nmid j}h_{pM}(j)v_{pM}(j).
\end{aligned}
\tag{24}
```

The first line is the scaled shell; the second is the unit shell. For
A376458, Section 6 handles these shells using the product formula (26).
For A376466, Section 7 exposes the shifted row as a homogeneous
negative-coordinate coefficient but also records why that observation does
not by itself close the unit shell. The remaining pure-prime A376458
conjecture asks for `3r+3` when `r>=2`.
A376466's proposed all-`n` shifted companion has already been disposed of by
Theorem 4.

For A376466 the exact checker shows that the unit shell is not termwise
cubic, so its completion needs aggregate cancellation. For A376458,
however, the single-sum collapse exposes three copies of the same `N/j`
divisibility. That extra structure closes the ordinary tower termwise,
as follows.

## 6. The ordinary A376458 tower

Put

```math
f(X)=(1-X)^3(1+X).
\tag{25}
```

The product identity (13), now used with arbitrary `N`, says that the
`j`-th nonconstant summand in (6) is

```math
t_N(j)=\frac{N^3}{j^3}\left(1-\frac Nj\right)
\prod_{h=1}^{j-1}f\left(\frac Nh\right).
\tag{26}
```

We first record the elementary unit-block estimate that supplies the
missing adjacent-level comparison.

### Lemma 5 (unit-block product)

Let `p>=5` be prime, let `N,k>=1`, and put `e=v_p(N)`, `q=v_p(k)`.
Then

```math
W_{p,N}(k)=
\prod_{\substack{1\le h<pk\\p\nmid h}}
f\left(\frac{pN}{h}\right)
\tag{27}
```

satisfies

```math
v_p(W_{p,N}(k)-1)\ge
\begin{cases}
e+2q+3,&q\le e,\\
3e+3,&q>e.
\end{cases}
\tag{28}
```

#### Proof

Let

```math
S_m(p,k)=\sum_{\substack{1\le h<pk\\p\nmid h}}h^{-m}.
```

If `q=v_p(k)`, decomposition into complete residue blocks modulo
`p^(q+1)` and inversion in the unit group give

```math
v_p(S_2(p,k))\ge q+1.
\tag{29}
```

Indeed, modulo `p^(q+1)` the inverse-square sum is a unit multiple of
the sum of the squares of all units modulo `p^(q+1)`. The latter is the
difference between the sum of all squares and `p^2` times the sum of
the squares modulo `p^q`; the usual formula for a sum of squares makes
both terms divisible by `p^(q+1)` because `p>=5`.

Pairing `h` with `pk-h` and expanding the resulting geometric series
then gives

```math
v_p(S_1(p,k))\ge 2q+2.
\tag{30}
```

Finally, `f(X)=1-2X+2X^3-X^4`. In the expansion of (27), the total
degree-one part is `-2pN S_1(p,k)`, and the degree-two part is

```math
2(pN)^2\bigl(S_1(p,k)^2-S_2(p,k)\bigr).
```

Their valuations are at least `e+2q+3` and `2e+q+3`, respectively.
Every term of total degree at least three has valuation at least
`3e+3`. Taking the minimum gives (28). QED

### Theorem 6 (ordinary cubic tower)

For every prime `p>=5` and all positive integers `n,r`,

```math
\boxed{
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}.}
\tag{31}
```

#### Proof

Set `N=np^(r-1)` and `e=v_p(N)`, so `e>=r-1`. Split (6) at level
`pN` according to whether `p` divides the summation index.

If `p` does not divide `j`, the identities

```math
\binom{pN}{j}=\frac{pN}{j}\binom{pN-1}{j-1},
\qquad
\binom{pN+j-1}{j}=\frac{pN}{j}\binom{pN+j-1}{j-1}
```

show directly that `v_p(t_{pN}(j))>=3(e+1)`.

For `j=pk`, equation (26) gives the exact factorization

```math
t_{pN}(pk)=t_N(k)W_{p,N}(k).
\tag{32}
```

If `q=v_p(k)<=e`, the same two displayed binomial identities give

```math
v_p(t_N(k))\ge3(e-q).
```

Combining this with the first line of (28) yields

```math
v_p(t_{pN}(pk)-t_N(k))
\ge4e-q+3\ge3e+3.
```

If `q>e`, integrality gives `v_p(t_N(k))>=0`, and the second line of
(28) again gives valuation at least `3e+3`. Thus every unit-index term
vanishes and every scaled-index term matches its predecessor modulo
`p^(3e+3)`. Summation proves the stronger adjacent-level modulus
`p^(3e+3)`, hence (31). QED

This proof is deliberately separate from the `p^5` boundary in Theorem 2.
The ordinary tower is termwise after unit-block compression; the extra
two powers on the pure-prime line require cancellation between strata and
remain an explicit obligation.

## 7. The ordinary A376466 tower

The apparent affine shift in `H_N` is itself a homogeneous multivariate
Apéry coefficient after negative-coordinate continuation. Let

```math
\mathcal B(r,s,t)=
\sum_{j\in\mathbb Z}
\binom rj\binom{r+s-j}{r}\binom tj,
\tag{33}
```

with integer binomial coefficients interpreted as in Straub.

### Lemma 7 (negative-coordinate row identity)

For all `N>=1` and `K>=0`,

```math
\boxed{T(N-1,K)=\mathcal B(-N,K,-N).}
\tag{34}
```

#### Proof

In (33), with `(r,s,t)=(-N,K,-N)`, the only nonzero indices are
`0<=j<=K`. The negation identity for binomial coefficients gives

```math
\mathcal B(-N,K,-N)
=\sum_{j=0}^K(-1)^{K-j}
\binom{N+j-1}{j}^2\binom{N-1}{K-j}.
\tag{35}
```

Consequently its ordinary generating function in `K` is

```math
(1-x)^{N-1}\sum_{j\ge0}\binom{N+j-1}{j}^2x^j
=\frac{1}{(1-x)^N}
 \sum_{j=0}^{N-1}\binom{N-1}{j}^2x^j.
\tag{36}
```

The equality is Euler's elementary transformation of the displayed
binomial series. On the other hand, (2) and
`sum_{K>=j} binom(K,j)x^K=x^j/(1-x)^(j+1)` show that

```math
\sum_{K\ge0}T(N-1,K)x^K
=\frac{1}{1-x}\sum_{j=0}^{N-1}
 \binom{N-1}{j}\binom{N+j-1}{j}
 \left(\frac{x}{1-x}\right)^j.
\tag{37}
```

The finite form of the same Euler transformation turns (37) into the
right-hand side of (36). Coefficients of `x^K` therefore agree. QED

Lemma 7 does prove the exact scaled-row estimate. If `p>=5`,
`e=v_p(N)`, `q=v_p(K)`, and `s=min(e,q)`, Straub's theorem applied to
`p^(-s)(-N,K,-N)` gives

```math
T(pN-1,pK)\equiv T(N-1,K)
\pmod {p^{3(s+1)}}.
\tag{38}
```

This completely controls the shifted row on divisible indices. It does not
make the outer unit shell termwise cubic. In fact, with

```math
c_N(k)=(-1)^{N+k}\binom Nk\binom{N+k}{k}^2,
\tag{39}
```

the first unit-index witness is

```math
v_5\bigl(c_5(1)T(4,1)\bigr)=1,
\qquad
v_5\bigl(B(5)-B(1)\bigr)=3.
\tag{40}
```

Thus two additional powers arise only after summing the unit shell. The
ordinary A376466 conjecture has now been reduced more sharply: its divisible
shell is governed by the proved homogeneous estimate (38), and its only
remaining obstruction is an aggregate unit-shell cancellation.

## 8. Verification and source boundary

[`verify_a376_apery_companions.py`](../verification/related/verify_a376_apery_companions.py)
checks (1)--(2), (5)--(10), (13), (17)--(24), and (34)--(40), both OEIS
initial sequences, the exact A376458 `p=5` boundary, the proved prime-level
theorem through a broad prime range, Lemma 5 across every divisibility
stratum in a finite audit box, Theorem 6 term by term, the negative-row
identity and its homogeneous scaled-row estimate, the sharp unit-shell
witness, the shifted A376466 counterexample, and sampled ordinary A376466
and pure-prime A376458 towers.

The definitions and conjectures come from the linked OEIS records. Equation
(2) is also recorded on A108625. Generalized Vandermonde and the harmonic
congruences used above are classical. No literature-priority claim is made
for the collapse, the `p^5` proof, or the pairing formulation.
