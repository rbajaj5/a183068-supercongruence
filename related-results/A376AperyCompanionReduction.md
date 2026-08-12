# The two remaining A376 Apéry companions

**Status:** the A376458 nested sum is collapsed to one signed
four-binomial sum and its conjectured prime-level `p^5` congruence is
proved for every `p>=7`; A376466 is placed in the same exact
coefficient-pairing framework and its proposed shifted tower is refuted by
an exact counterexample; the two ordinary cubic towers and the higher
A376458 bonus remain open

The last two wholly untreated records in the Bala 110-record census are
[A376458](https://oeis.org/A376458) and
[A376466](https://oeis.org/A376466). Both are transforms of the crystal-ball
triangle [A108625](https://oeis.org/A108625), but the occurrence of `N-1`
means that Straub's homogeneous multivariate theorem cannot simply be cited:
the parameter vector does not scale by `p`.

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

The first line is the scaled shell; the second is the unit shell. The
ordinary cubic conjectures are precisely the assertion that their sum has
valuation at least `3r` when `M=np^(r-1)`. For A376458, the remaining
pure-prime conjecture asks for `3r+3` when `r>=2`. A376466's proposed
all-`n` shifted companion has already been disposed of by Theorem 4.

The exact checker shows that the unit shells are not termwise cubic. Any
completion therefore needs the same kind of aggregate reciprocal-block
cancellation as the classical Apéry proof; a product of separate
coefficientwise estimates is insufficient.

## 6. Verification and source boundary

[`verify_a376_apery_companions.py`](../verification/related/verify_a376_apery_companions.py)
checks (1)--(2), (5)--(10), (13), and (17)--(24), both OEIS initial
sequences, the exact A376458 `p=5` boundary, the proved prime-level theorem
through a broad prime range, the shifted A376466 counterexample, and sampled
ordinary and pure-prime towers.

The definitions and conjectures come from the linked OEIS records. Equation
(2) is also recorded on A108625. Generalized Vandermonde and the harmonic
congruences used above are classical. No literature-priority claim is made
for the collapse, the `p^5` proof, or the pairing formulation.
