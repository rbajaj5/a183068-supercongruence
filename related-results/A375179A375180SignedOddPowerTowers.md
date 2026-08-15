# The complete signed odd-power towers A375179 and A375180

**Status:** complete elementary proof candidate for every odd exponent;
exact checks pass; independent review and literature priority remain open

For a nonzero integer $A$ and an odd integer $q\geq3$, put

```math
S_{A,q}(N)=
\sum_{k=0}^{N-1}(-1)^{N+k+1}\binom{AN}{k}^{q}.
\tag{1}
```

The sequences A375179 and A375180 are respectively $S_{2,3}$ and
$S_{3,3}$. Their prime boundary was proved, for arbitrary $A$, in the
[first queue note](BalaOeisSupercongruenceQueue.md#the-signed-arbitrary-dilation-companion).
This note proves the remaining higher tower uniformly in the dilation.

## Theorem

Let $A$ be a nonzero integer, let $q\geq3$ be odd, and let $p\geq q+4$ be
prime with $p\nmid A$. For every $r\geq2$,

```math
\boxed{
S_{A,q}(p^r)\equiv S_{A,q}(p^{r-1})\pmod {p^{3r+q}}.
}
\tag{2}
```

Writing $q=2m+1$ gives exactly the modulus $p^{3r+2m+1}$ conjectured on
A375179 and A375180.

## 1. The hidden generalized-binomial family

For an integer $x$ define

```math
F_{x,N}(j)=\binom{xN+j-1}{j},
\qquad
C_{x,q}(N)=\sum_{j=0}^{N-1}F_{x,N}(j)^q.
\tag{3}
```

The generalized-binomial identity

```math
\binom{-AN+j-1}{j}=(-1)^j\binom{AN}{j}
\tag{4}
```

and the oddness of $q$ give

```math
S_{A,q}(N)=(-1)^{N+1}C_{-A,q}(N).
\tag{5}
```

For odd $p$, the signs at $p^r$ and $p^{r-1}$ agree. It is therefore
enough to prove the stronger statement that, for every integer $x\ne0$
with $p\nmid x$,

```math
C_{x,q}(p^r)\equiv C_{x,q}(p^{r-1})\pmod {p^{3r+q}}.
\tag{6}
```

This is not a formal consequence of the $x=1$ theorem: the low-level
residues carry powers of $x$. The point is that every cancellation used
there is homogeneous in those powers.

## 2. Exact lift and shell budget

Put $e=r-1$ and $N=p^e$. Cancellation of the factors whose indices are
divisible by $p$ gives

```math
F_{x,pN}(pj)=F_{x,N}(j)W_{x,e,j},
\qquad
W_{x,e,j}=\prod_{\substack{1\leq h<pj\\p\nmid h}}
\left(1+\frac{xpN}{h}\right).
\tag{7}
```

If $t=v_p(j)$, unit-block inversion and complementary pairing yield

```math
v_p(F_{x,N}(j))=e-t,
\qquad
v_p(W_{x,e,j}-1)\geq e+2t+3.
\tag{8}
```

The assumption $p\nmid x$ is used in the first equality; multiplication
by powers of $x$ does not alter the second estimate. Consequently

```math
v_p\!\left(F_{x,N}(j)^q(W_{x,e,j}^q-1)\right)
\geq(q+1)e-(q-2)t+3.
\tag{9}
```

Separating indices divisible by $p$ gives

```math
\begin{aligned}
C_{x,q}(pN)-C_{x,q}(N)
={}&\sum_{\substack{1\leq k<pN\\p\nmid k}}F_{x,pN}(k)^q\\
&+\sum_{j=1}^{N-1}F_{x,N}(j)^q(W_{x,e,j}^q-1).
\end{aligned}
\tag{10}
```

For $q\geq5$, (9) is deep enough off the final shell $t=e-1$. For
$q=3$, only the penultimate shell $t=e-2$ is additionally visible.

## 3. The unscaled shell

The two-digit unit-shell calculation used for A112028 remains valid after
replacing every occurrence of $p^s$ by $xp^s$. To make the dependence on
the slope explicit, write $k=a+pb$ at $s=2$. Then

```math
\frac{F_{x,p^2}(a+pb)}{p^2}
\equiv\frac xa\left(1+pA^{(x)}_{a,b}+p^2B^{(x)}_{a,b}\right)
\pmod {p^3},
```

where

```math
A^{(x)}_{a,b}=xH_b-\frac ba
```

and

```math
B^{(x)}_{a,b}=
\frac{x^2}{2}(H_b^2-H_b^{(2)})+xH_{a-1}
-\frac{xbH_b}{a}+\frac{b^2}{a^2}.
```

After cubing, each coefficient of each power of $x$ is killed by the same
inverse power sums and the same identities for $\sum_bH_b$, $\sum_b b$,
$\sum_b bH_b$, and $\sum_b b^2$ as in the $x=1$ proof. For $s\geq3$ the
corresponding formula is

```math
\frac{F_{x,p^s}(a+pb)}{p^s}
\equiv\frac{xP_{x,s-1}(b)}{a+pb}\pmod {p^3},
\qquad
P_{x,s-1}(b)=\prod_{\ell=1}^{b}
\left(1+\frac{xp^{s-1}}\ell\right).
```

Since $P_{x,s-1}(b)\equiv1\pmod p$, the three power-sum cancellations are
again unchanged. Hence, for $s\geq2$,

```math
\sum_{\substack{1\leq k<p^s\\p\nmid k}}
\left(\frac{F_{x,p^s}(k)}{p^s}\right)^3
\equiv0\pmod {p^3}.
\tag{11}
```

For negative $x$, the alternating sign is already part of the generalized
binomial in (11). This proves the unscaled contribution for $q=3$. For
$q\geq7$ the obvious factor $p^{q(e+1)}$ suffices. At the sole boundary
$q=5,e=1$, division by $p^{10}$ leaves a unit multiple of
$\sum_{p\nmid k<p^2}k^{-5}$ modulo $p$; every nonzero residue occurs $p$
times, so the sum vanishes.

## 4. The cubic penultimate shell

When $q=3$ and $e\geq2$, write $j=p^{e-2}a$, where
$1\leq a<p^2$ and $p\nmid a$. If

```math
\tau_{e-1}=p^{-(e-1)}
\sum_{\substack{1\leq u<p^{e-1}\\p\nmid u}}u^{-2},
```

then block expansion gives, modulo $p$ after normalization,

```math
\frac{F_{x,N}(p^{e-2}a)}{p^2}\equiv\frac{x}{a},
\qquad
\frac{W_{x,e,p^{e-2}a}^{3}-1}{p^{3e-1}}
\equiv-\frac32x\tau_{e-1}a^2.
\tag{12}
```

The normalized summand is a fixed unit multiple of $a^{-1}$. Every
nonzero residue occurs $p$ times among the admissible $a$, giving the one
missing power.

## 5. The universal critical shell

Write $j=p^{e-1}a$, $1\leq a<p$, and set

```math
\tau_e=p^{-e}
\sum_{\substack{1\leq u<p^e\\p\nmid u}}u^{-2}.
```

Retaining the first two logarithmic terms in (7) and the first two digits
of the binomial factor gives

```math
W_{x,e,p^{e-1}a}^{q}-1
\equiv
-\frac q2xp^{3e+1}\tau_e a(a+xp)
\pmod {p^{3e+3}},
\tag{13}
```

```math
\frac{F_{x,N}(p^{e-1}a)}p
\equiv
\frac xa(1+xpH_{a-1})\pmod {p^2}.
\tag{14}
```

After division by $p^{3e+q+1}$, the critical shell is a fixed unit
multiple of

```math
\sum_{a=1}^{p-1}\left(
a^{-(q-2)}+xp\,a^{-(q-1)}+qxpH_{a-1}a^{-(q-2)}
\right)
\pmod {p^2}.
\tag{15}
```

Put $m=q-2$, which is odd. The finite-field power sums give

```math
\sum_a a^{-m}\equiv0\pmod {p^2},
\qquad
\sum_a a^{-(m+1)}\equiv0\pmod p.
\tag{16}
```

For $D_m=\sum_{j<a}j^{-1}a^{-m}$, the involution
$(j,a)\mapsto(p-a,p-j)$ gives

```math
2D_m=
\left(\sum_a a^{-1}\right)\left(\sum_a a^{-m}\right)
-\sum_a a^{-(m+1)}
\equiv0\pmod p.
\tag{17}
```

Thus (15) vanishes at the required precision, independently of $x$.
Equations (9)--(17) prove (6), hence (2). QED

## Verification and source boundary

Run

```text
python verification/related/verify_a375179_a375180_signed_towers.py
```

The checker verifies the generalized-binomial conversion, exact lift,
valuation budget, slope-dependent critical formulas, shell cancellation,
and full adjacent towers for positive and negative slopes. It records sharp
instances for both named dilations and every tested exponent.

The conjectures are recorded on [OEIS A375179](https://oeis.org/A375179)
and [OEIS A375180](https://oeis.org/A375180). The first-queue note proves
their prime boundary. No literature-priority claim is made.
