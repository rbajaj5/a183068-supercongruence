# The complete enhanced A375178 odd-power tower

**Status:** complete elementary proof candidate for every odd exponent
$q\geq3$ and every prime $p\geq q+4$; exact checks pass; independent review
and literature priority remain open

For an odd integer $q\geq3$, define

```math
B_q(N)=\sum_{k=0}^{N-1}\binom{N+k-1}{k}^{q}.
\tag{1}
```

The sequence A375178 is the case $q=3$.  Peter Bala's OEIS comment proposes
one enhanced tower for every odd exponent.  The prime boundary was proved in
the [first queue note](BalaOeisSupercongruenceQueue.md#3-the-full-prime-level-odd-power-theorem-for-a375178).

## Theorem

For every odd $q\geq3$, every prime $p\geq q+4$, and every $r\geq2$,

```math
\boxed{
B_q(p^r)\equiv B_q(p^{r-1})\pmod {p^{3r+q}}.
}
\tag{2}
```

Writing $q=2m+1$, the modulus is exactly $p^{3r+2m+1}$, as conjectured on
A375178.

## 1. Common shell estimates

Put $e=r-1$, $N=p^e$, and

```math
F_N(j)=\binom{N+j-1}{j}.
```

For $1\leq j<N$ with $t=v_p(j)$, exact cancellation of the $p$-divisible
factors gives

```math
F_{pN}(pj)=F_N(j)W_{e,j},
\qquad
W_{e,j}=\prod_{\substack{1\leq h<pj\\p\nmid h}}
\left(1+\frac{pN}{h}\right).
\tag{3}
```

The reciprocal-square unit-block sum and complementary-unit pairing imply

```math
v_p(F_N(j))=e-t,
\qquad
v_p(W_{e,j}-1)\geq e+2t+3.
\tag{4}
```

Consequently a scaled-index summand has valuation at least

```math
v_p\!\left(F_N(j)^q(W_{e,j}^q-1)\right)
\geq(q+1)e-(q-2)t+3.
\tag{5}
```

The target in (2) is $3e+q+3$.  If $q\geq5$ and $t\leq e-2$, the difference
between (5) and the target is

```math
(q-2)(e-t)-q\geq q-4>0.
```

Thus for $q\geq5$ only the final shell $t=e-1$ can contribute.  The case
$q=3$ has one additional penultimate shell and is proved in full in the
[A112028 theorem](A112028EnhancedTower.md).

## 2. The outer unit shell

For $p\nmid k$, the summand $F_{p^{e+1}}(k)^q$ contains $p^{q(e+1)}$.
This already reaches $p^{3e+q+3}$ if either $q\geq7$, or $q=5$ and
$e\geq2$.

At the sole remaining boundary $q=5,e=1$, division by $p^{10}$ and
reduction modulo $p$ leaves

```math
\sum_{\substack{1\leq k<p^2\\p\nmid k}}k^{-5}.
```

Every nonzero residue occurs $p$ times, so this is zero modulo $p$.
For $q=3$, the stronger two-digit unit-shell lemma in the A112028 theorem
supplies the three missing powers.

## 3. The universal critical shell

Write the last shell as $j=p^{e-1}a$, $1\leq a<p$, and put

```math
T_e=\sum_{\substack{1\leq u<p^e\\p\nmid u}}u^{-2},
\qquad
\tau_e=p^{-e}T_e\in\mathbb Z_{(p)}.
\tag{6}
```

The block expansion and complementary-unit pairing used in (4) give the
two-digit formulas

```math
W_{e,p^{e-1}a}^{q}-1
\equiv
-\frac q2p^{3e+1}\tau_e a(a+p)
\pmod {p^{3e+3}}
\tag{7}
```

and

```math
\frac{F_N(p^{e-1}a)}p
\equiv
\frac1a(1+pH_{a-1})\pmod {p^2}.
\tag{8}
```

The square of the logarithm in (7) lies beyond the displayed precision.
After multiplying (7) and the $q$-th power of (8), the critical shell,
divided by $p^{3e+q+1}$, is a unit multiple of

```math
\sum_{a=1}^{p-1}\left(
a^{-(q-2)}+pa^{-(q-1)}+qpH_{a-1}a^{-(q-2)}
\right)
\pmod {p^2}.
\tag{9}
```

Set $m=q-2$, which is odd.  Since $m+1=q-1<p-1$, the standard finite-field
power sums give

```math
\sum_a a^{-m}\equiv0\pmod {p^2},
\qquad
\sum_a a^{-(m+1)}\equiv0\pmod p.
\tag{10}
```

For the harmonic term, let

```math
D_m=\sum_{1\leq j<a<p}j^{-1}a^{-m}.
```

The involution $(j,a)\mapsto(p-a,p-j)$ sends this sum to
$\sum_{j<a}a^{-1}j^{-m}$ because $m$ is odd.  Hence

```math
2D_m=
\left(\sum_a a^{-1}\right)\left(\sum_a a^{-m}\right)
-\sum_a a^{-(m+1)}
\equiv0\pmod p.
\tag{11}
```

Equations (9)--(11) supply the two powers absent from the individual
critical-shell bound.  Together with Sections 1--2 and the cubic companion
theorem, this proves (2). QED

## 4. Verification and boundary

Run

```text
python verification/related/verify_a375178_enhanced_odd_tower.py
```

The checker verifies the quotient estimates, the unit boundary, the general
critical expansions and harmonic involution, and complete towers for
$q=3,5,7,9$ on a finite exact grid.  It also records sharp instances for
each tested exponent.

The proof concerns the shifted positive-binomial family A375178.  The signed
dilation geometries A375179 and A375180 have the same proved prime boundary,
but their enhanced higher towers are not consequences of this theorem and
remain separate targets.  Coster supplies only the ordinary $p^{3r}$
baseline.  No literature-priority claim is made.
