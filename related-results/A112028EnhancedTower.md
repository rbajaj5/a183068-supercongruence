# The enhanced A112028 shifted-binomial tower

**Status:** complete elementary proof candidate for every prime $p\geq7$
at levels $r\geq2$; exact checks pass; independent review and literature
priority remain open

Put

```math
C(N)=\sum_{k=0}^{N-1}\binom{N+k-1}{k}^{3}.
\tag{1}
```

Thus $C(N)=\operatorname{A112028}(N-1)$.  The prime-level congruence
$C(p)\equiv1\pmod {p^5}$ is proved in the
[Bala queue note](BalaOeisSupercongruenceQueue.md#the-even-power-boundary-and-a112028--a219562).
This note proves the remaining higher-level conjecture.

## Theorem

For every prime $p\geq7$ and every $r\geq2$,

```math
\boxed{C(p^r)\equiv C(p^{r-1})\pmod {p^{3r+3}}.}
\tag{2}
```

Equivalently,

```math
\operatorname{A112028}(p^r-1)
\equiv
\operatorname{A112028}(p^{r-1}-1)
\pmod {p^{3r+3}}.
```

The proof has three cancellations.  The outer unit shell is a two-digit
calculation.  The penultimate scaled shell cancels because every nonzero
residue occurs $p$ times.  The final shell reduces to Wolstenholme's harmonic
congruences and one elementary double harmonic sum.

## 1. Quotient estimates

Write

```math
F_N(j)=\binom{N+j-1}{j}.
```

Let $N=p^e$, $1\leq j<N$, and $t=v_p(j)$.  Cancelling the factors with
indices divisible by $p$ gives the exact identity

```math
F_{pN}(pj)=F_N(j)W_{e,j},
\qquad
W_{e,j}=\prod_{\substack{1\leq h<pj\\p\nmid h}}
\left(1+\frac{pN}{h}\right).
\tag{3}
```

The unit-block estimates

```math
v_p\!\left(\sum_{\substack{1\leq h<pj\\p\nmid h}}h^{-2}\right)
\geq t+1,
\qquad
v_p\!\left(\sum_{\substack{1\leq h<pj\\p\nmid h}}h^{-1}\right)
\geq2t+2
\tag{4}
```

follow respectively from inversion on complete unit blocks and from pairing
$h$ with $pj-h$.  Expanding the logarithm of (3) therefore gives

```math
v_p(W_{e,j}-1)\geq e+2t+3.
\tag{5}
```

Also

```math
v_p(F_N(j))=e-t.
\tag{6}
```

These are the same quotient estimates used in the
[quartic companion theorem](A219562EnhancedTower.md), but cubing rather than
taking a fourth power leaves two aggregate cancellations to prove.

## 2. Decomposition into shells

Set $e=r-1\geq1$ and $N=p^e$.  Separating indices divisible by $p$ yields

```math
\begin{aligned}
C(pN)-C(N)
={}&\sum_{\substack{1\leq k<pN\\p\nmid k}}F_{pN}(k)^3\\
&+\sum_{j=1}^{N-1}F_N(j)^3\bigl(W_{e,j}^3-1\bigr).
\end{aligned}
\tag{7}
```

By (5)--(6), a term in the second line with $v_p(j)=t$ has valuation at
least

```math
3(e-t)+(e+2t+3)=4e-t+3.
\tag{8}
```

The target is $3r+3=3e+6$.  Thus every shell with $t\leq e-3$ is already
termwise negligible.  Only $t=e-2$ and $t=e-1$ require cancellation.

## 3. The outer unit shell

The following elementary lemma supplies the three powers missing after the
obvious factor $(p^s)^3$.

### Lemma 1

For $p\geq7$ and $s\geq2$,

```math
\sum_{\substack{1\leq k<p^s\\p\nmid k}}
\left(\frac{F_{p^s}(k)}{p^s}\right)^3
\equiv0\pmod {p^3}.
\tag{9}
```

#### Proof

First take $s=2$ and write $k=a+pb$, where $1\leq a<p$ and
$0\leq b<p$.  Put

```math
H_b=\sum_{j=1}^{b}\frac1j,
\qquad H_b^{(2)}=\sum_{j=1}^{b}\frac1{j^2}.
```

Splitting the defining product for $F_{p^2}(k)/p^2$ into indices divisible
and not divisible by $p$ gives, modulo $p^3$,

```math
\frac{F_{p^2}(a+pb)}{p^2}
\equiv
\frac1a\left(1+pA_{a,b}+p^2B_{a,b}\right),
\tag{10}
```

where

```math
A_{a,b}=H_b-\frac ba
```

and

```math
B_{a,b}=
\frac{H_b^2-H_b^{(2)}}2+H_{a-1}
-\frac{bH_b}{a}+\frac{b^2}{a^2}.
```

Indeed, the complete unit blocks contribute zero to their reciprocal sum
modulo $p$, leaving only $H_{a-1}$ in the unit part.

After cubing (10), the constant contribution to the double sum is
$p\sum_a a^{-3}$, which is zero modulo $p^3$.  The coefficient of $p$ is

```math
3p\left(
\sum_a a^{-3}\sum_bH_b-
\sum_a a^{-4}\sum_b b
\right),
```

and is also zero modulo $p^3$, since

```math
\sum_bH_b=pH_{p-1}-(p-1),
\qquad
\sum_b b=\frac{p(p-1)}2,
```

while the inverse-cube and inverse-fourth-power sums have valuations at
least $2$ and $1$.  In the coefficient of $p^2$, reduction modulo $p$
the expression

```math
\begin{aligned}
&\left(\sum_a a^{-3}\right)
 \sum_b\left(\frac32H_b^2-\frac12H_b^{(2)}\right)
+p\sum_a\frac{H_{a-1}}{a^3}\\
&\qquad
-3\left(\sum_a a^{-4}\right)\sum_b bH_b
+2\left(\sum_a a^{-5}\right)\sum_b b^2.
\end{aligned}
```

This is zero modulo $p$: the first, third, and fourth terms vanish by the
finite-field power-sum identity, and the second contains the displayed
factor $p$.  This proves (9) for $s=2$.

Now let $s\geq3$.  Again write $k=a+pb$, now with
$0\leq b<p^{s-1}$.  All factors with unit index are $1$ modulo $p^3$, so

```math
\frac{F_{p^s}(a+pb)}{p^s}
\equiv
\frac{P_{s-1}(b)}{a+pb}\pmod {p^3},
\qquad
P_{s-1}(b)=\prod_{\ell=1}^{b}
\left(1+\frac{p^{s-1}}\ell\right).
\tag{11}
```

Expanding $(a+pb)^{-3}$ reduces the sum to

```math
\left(\sum_a a^{-3}\right)\sum_bP_{s-1}(b)^3
-3p\left(\sum_a a^{-4}\right)\sum_b bP_{s-1}(b)^3
+6p^2\left(\sum_a a^{-5}\right)\sum_b b^2P_{s-1}(b)^3.
```

The first term is divisible by $p^3$ because the inverse-cube sum has
valuation at least two and

```math
\sum_bP_{s-1}(b)^3\equiv0\pmod p.
```

For the second term, the inverse-fourth-power sum contributes one power of
$p$ and the sum over $b$ contributes another: when $s\geq3$,
$P_{s-1}(b)\equiv1\pmod p$, so
$\sum_b bP_{s-1}(b)^3\equiv\sum_b b\equiv0\pmod p$.
The inverse-fifth-power sum in the last term is itself divisible by $p$.
Consequently all three displayed terms vanish modulo $p^3$.  QED

Taking $s=e+1$ in Lemma 1 proves that the first line of (7) is divisible
by $p^{3e+6}$.

## 4. The penultimate shell

Assume $e\geq2$ and write

```math
j=p^{e-2}a,
\qquad 1\leq a<p^2,\quad p\nmid a.
```

Let

```math
T_{e-1}=\sum_{\substack{1\leq u<p^{e-1}\\p\nmid u}}u^{-2},
\qquad
\tau_{e-1}=p^{-(e-1)}T_{e-1}\in\mathbb Z_{(p)}.
\tag{12}
```

Block expansion and the same $h\leftrightarrow ap^{e-1}-h$ pairing as in
(4) give, modulo $p$ after normalization,

```math
\frac{F_N(p^{e-2}a)}{p^2}\equiv a^{-1},
\qquad
\frac{W_{e,p^{e-2}a}^{3}-1}{p^{3e-1}}
\equiv-\frac32\tau_{e-1}a^2.
\tag{13}
```

Hence the summand in (7), divided by $p^{3e+5}$, is congruent to
$-(3/2)\tau_{e-1}a^{-1}$ modulo $p$.  Every nonzero residue $a\bmod p$
occurs exactly $p$ times in $1\leq a<p^2$.  The whole shell therefore
gains the one additional power required by (8).

## 5. The critical shell

Write $j=p^{e-1}a$, $1\leq a<p$, and put

```math
T_e=\sum_{\substack{1\leq u<p^e\\p\nmid u}}u^{-2},
\qquad
\tau_e=p^{-e}T_e\in\mathbb Z_{(p)}.
\tag{14}
```

Decomposing the interval below $ap^e$ into complete blocks gives

```math
S_2(a)\equiv aT_e\pmod {p^{e+2}},
\tag{15}
```

at the precision needed below.  Pairing complementary units and retaining
the first two terms of the logarithm in (3) then yields

```math
W_{e,p^{e-1}a}^{3}-1
\equiv
-\frac32p^{3e+1}\tau_e a(a+p)
\pmod {p^{3e+3}}.
\tag{16}
```

The two summands in $a(a+p)$ come respectively from the reciprocal-first
and reciprocal-second-power terms.  All higher logarithmic terms and the
square of the logarithm lie beyond the displayed precision.

The remaining binomial factor has the two-digit expansion

```math
\frac{F_N(p^{e-1}a)}p
\equiv
\frac1a\left(1+pH_{a-1}\right)\pmod {p^2}.
\tag{17}
```

Combining (16)--(17), the critical shell divided by $p^{3e+4}$ is,
modulo $p^2$, a unit multiple of

```math
\sum_{a=1}^{p-1}\left(
\frac1a+\frac p{a^2}+\frac{3pH_{a-1}}a
\right).
\tag{18}
```

Now Wolstenholme's harmonic congruences give

```math
\sum_{a=1}^{p-1}a^{-1}\equiv0\pmod {p^2},
\qquad
\sum_{a=1}^{p-1}a^{-2}\equiv0\pmod p.
```

Finally,

```math
\sum_{a=1}^{p-1}\frac{H_{a-1}}a
=\sum_{1\leq j<a<p}\frac1{ja}
=\frac12\left[
\left(\sum_{a=1}^{p-1}\frac1a\right)^2
-\sum_{a=1}^{p-1}\frac1{a^2}
\right]
\equiv0\pmod p.
\tag{19}
```

Thus (18) vanishes modulo $p^2$.  The critical shell gains both powers
missing from the individual estimate (8).  Sections 2--5 prove (2). QED

## 6. Verification and source boundary

Run

```text
python verification/related/verify_a112028_enhanced_tower.py
```

The checker verifies the exact quotient, the unit-shell lemma, both scaled
shell cancellations, the critical expansions (16)--(19), and the final
tower on a finite grid.  These checks are for transcription and boundary
control; the argument above is the proof.

The conjecture is recorded on [OEIS A112028](https://oeis.org/A112028).
Coster proves the ordinary $p^{3r}$ baseline, not the three additional
powers proved here.  No literature-priority claim is made.
