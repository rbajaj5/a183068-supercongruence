# The enhanced A376458 pure-prime tower

**Status:** complete elementary proof candidate for every prime `p>=5`
and every level `r>=2`; exact shell and tower checks pass; independent
review and literature priority remain open

Let

```math
A(N)=\sum_{j=0}^{N-1}(-1)^j
\binom Nj^2\binom{N-1}{j}\binom{N+j-1}{j}.
\tag{1}
```

The single-sum identity (1), the ordinary cubic tower, and the prime-level
congruence `A(p)=A(1) mod p^5` for `p>=7` are proved in the
[companion reduction](A376AperyCompanionReduction.md).  This note closes
the remaining higher-level conjecture on OEIS A376458.

## Theorem

For every prime `p>=5` and every integer `r>=2`,

```math
\boxed{A(p^r)\equiv A(p^{r-1})\pmod {p^{3r+3}}.}
\tag{2}
```

The proof uses the same three-shell architecture as the enhanced A112028
tower, but the local polynomial is

```math
f(X)=(1-X)^3(1+X).
\tag{3}
```

The outer unit shell is a two-digit calculation.  The penultimate scaled
shell gains one power because every nonzero residue occurs `p` times.  The
critical scaled shell gains two powers from Wolstenholme's congruences and
one depth-two harmonic identity.

## 1. Exact quotient and the noncritical shells

For `1<=j<N`, put

```math
t_N(j)=(-1)^j
\binom Nj^2\binom{N-1}{j}\binom{N+j-1}{j}.
```

The elementary product formula is

```math
t_N(j)=\frac{N^3}{j^3}\left(1-\frac Nj\right)
\prod_{h=1}^{j-1}f\!\left(\frac Nh\right).
\tag{4}
```

Set `N=p^e`, where `e=r-1>=1`.  Cancelling the factors whose indices are
divisible by `p` gives

```math
t_{pN}(pj)=t_N(j)W_{e,j},
\qquad
W_{e,j}=\prod_{\substack{1\le h<pj\\p\nmid h}}
f\!\left(\frac{pN}{h}\right).
\tag{5}
```

If `q=v_p(j)`, the unit-block estimate proved in Lemma 5 of the companion
reduction says

```math
v_p(W_{e,j}-1)\ge e+2q+3\qquad(q\le e).
\tag{6}
```

The three visible factors `N/j` in (4) also give

```math
v_p(t_N(j))\ge3(e-q).
\tag{7}
```

Therefore

```math
v_p\bigl(t_N(j)(W_{e,j}-1)\bigr)\ge4e-q+3.
\tag{8}
```

The target in (2) is `3e+6`.  Every shell with `q<=e-3` is consequently
negligible term by term.  Only `q=e-2` and `q=e-1` remain.

## 2. The outer unit shell

The following local lemma supplies the three powers missing after the
obvious factor `p^(3s)`.

### Lemma 1

For `p>=5` and `s>=2`,

```math
\sum_{\substack{1\le k<p^s\\p\nmid k}}
\frac{t_{p^s}(k)}{p^{3s}}\equiv0\pmod {p^3}.
\tag{9}
```

#### Proof

First take `s=2` and write `k=a+pb`, where `1<=a<p` and `0<=b<p`.
Splitting the product in (4) into indices divisible and not divisible by
`p`, and expanding modulo `p^3`, gives

```math
\frac{t_{p^2}(a+pb)}{p^6}
=\frac1{a^3}\bigl(1+pL_{a,b}+p^2M_{a,b}\bigr)
\pmod {p^3},
\tag{10}
```

where

```math
L_{a,b}=-\frac{3b}{a}-2H_b
```

and

```math
M_{a,b}=
\frac{6b^2}{a^2}+\frac{6bH_b}{a}+2H_b^2-2H_b^{(2)}
-2H_{a-1}-\frac1a.
\tag{10a}
```

Summing these expressions over `b` reduces the constant term to
`p sum a^(-3)`, the coefficient of `p` to a linear combination of
`sum a^(-3)` and `sum a^(-4)`, and the coefficient of `p^2` to a linear
combination of `sum a^(-m)` with `3<=m<=5`, with an additional factor
`p` on the inverse-fourth-power boundary.  The standard finite-field
power-sum identities, together with

```math
\sum_{a=1}^{p-1}a^{-3}\equiv0\pmod {p^2}
```

for `p>=7`, make all three coefficients vanish at the required precision.
For `p=5`, the inverse-cube boundary has only one power of `5`, but direct
substitution in (10) gives the same zero modulo `5^3`.  This is a finite
four-residue boundary, not an additional hypothesis.

For `s>=3`, write `k=a+pb` with `0<=b<p^(s-1)`.  Factors having unit
index are `1` modulo `p^3`, so (4) has the form

```math
\frac{t_{p^s}(a+pb)}{p^{3s}}
\equiv\frac{G_{s-1}(b)}{(a+pb)^3}\pmod {p^3},
\tag{11}
```

where

```math
G_{s-1}(b)=(-1)^b\binom{p^{s-1}-1}{b}^3
\binom{p^{s-1}+b}{b}.
```

Expanding `(a+pb)^(-3)` reduces the total to the three products

```math
\left(\sum_a a^{-3}\right)\sum_bG_{s-1}(b),
```

```math
-3p\left(\sum_a a^{-4}\right)\sum_b bG_{s-1}(b),
```

and

```math
6p^2\left(\sum_a a^{-5}\right)\sum_b b^2G_{s-1}(b).
\tag{12}
```

The same complete-block calculation used at `s=2` (applied also after
multiplication by `b` or `b^2`) gives

```math
v_p\!\left(\sum_b b^dG_{s-1}(b)\right)\ge s-1
\qquad(0\le d\le2).
\tag{13}
```

The first two inverse power sums have valuations at least `2` and `1`;
the last term already contains `p^2`, while (13) supplies its remaining
power. Thus every term in (12) vanishes modulo `p^3`. This proves
Lemma 1. QED

Taking `s=e+1` proves that the outer shell in `A(pN)-A(N)` is divisible
by `p^(3e+6)`.

## 3. The penultimate shell

Assume `e>=2` and write

```math
j=p^{e-2}a,
\qquad1\le a<p^2,\quad p\nmid a.
```

Let

```math
T_{e-1}=\sum_{\substack{1\le u<p^{e-1}\\p\nmid u}}u^{-2},
\qquad
\tau_{e-1}=p^{-(e-1)}T_{e-1}\in\mathbb Z_{(p)}.
\tag{14}
```

The unit-block expansion in (5), reduced modulo `p` after normalization,
gives

```math
\frac{t_N(p^{e-2}a)}{p^6}\equiv a^{-3},
\qquad
\frac{W_{e,p^{e-2}a}-1}{p^{3e-1}}
\equiv c_e\tau_{e-1}a^2\pmod p,
\tag{15}
```

where the constant `c_e` is independent of `a`.  Hence the normalized
summand is a constant multiple of `a^(-1)`.  Every nonzero residue modulo
`p` occurs exactly `p` times in `1<=a<p^2`, so the entire shell gains the
one extra power required by (8).

## 4. The critical shell

Write `j=p^(e-1)a`, where `1<=a<p`, and put

```math
T_e=\sum_{\substack{1\le u<p^e\\p\nmid u}}u^{-2},
\qquad
\tau_e=p^{-e}T_e\in\mathbb Z_{(p)}.
\tag{16}
```

Expanding (4) through two digits gives

```math
\frac{t_N(p^{e-1}a)}{p^3}
\equiv
\frac1{a^3}
\left(1-\frac pa-2pH_{a-1}\right)
\pmod {p^2}.
\tag{17}
```

Pairing complementary units in (5), and retaining its reciprocal-first-
and reciprocal-second-power terms, then yields, after multiplication by
(17),

```math
\frac{t_N(p^{e-1}a)(W_{e,p^{e-1}a}-1)}{p^{3e+4}}
\equiv
\tau_e\left(
\frac1a-\frac{3p}{a^2}-\frac{2pH_{a-1}}a
\right)\pmod {p^2}.
\tag{18}
```

For `p>=7`, summing (18) gives zero modulo `p^2`: Wolstenholme's
congruences give

```math
\sum_{a=1}^{p-1}a^{-1}\equiv0\pmod {p^2},
\qquad
\sum_{a=1}^{p-1}a^{-2}\equiv0\pmod p,
```

and

```math
\sum_{a=1}^{p-1}\frac{H_{a-1}}a
=\frac12\left[
\left(\sum_{a=1}^{p-1}\frac1a\right)^2
-\sum_{a=1}^{p-1}\frac1{a^2}
\right]
\equiv0\pmod p.
\tag{19}
```

Thus the critical shell gains the two missing powers.  The formula is also
valid at `p=5` once `e>=2`.  The sole remaining corner is `p=5,e=1`, or
equivalently `p=5,r=2`; exact evaluation gives

```math
A(25)-A(5)
=2^2\,3^2\,5^9\,67\,97\,7741\,49223\,129289.
\tag{20}
```

Equations (8)--(20) prove (2). QED

## 5. Verification and source boundary

Run

```text
python verification/related/verify_a376458_enhanced_tower.py
```

The checker verifies the exact quotient (5), the shell bounds, the outer
two-digit cancellation, the normalized penultimate and critical formulas,
the three harmonic identities, the exact exceptional corner (20), and the
full tower on a finite prime/level grid.  These checks support transcription
and boundary control; the shell argument above is the proof.

The conjecture is stated on [OEIS A376458](https://oeis.org/A376458).
No literature-priority claim is made.
