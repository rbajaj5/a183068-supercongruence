# The enhanced A219562 shifted-binomial tower

**Status:** complete elementary proof candidate for every prime (p\ge5)
at levels (r\ge2); exact checks pass; independent review and literature
priority remain open

Put

```math
B(N)=\sum_{k=0}^{N-1}\binom{N+k-1}{k}^{4}.
\tag{1}
```

Thus (B(N)=\operatorname{A219562}(N-1)). The prime-level fifth-power
congruence is proved in the
[Bala queue note](BalaOeisSupercongruenceQueue.md#the-even-power-boundary-and-a112028--a219562).
This note proves the remaining higher-level conjecture.

## Theorem

For every prime (p\ge5) and every (r\ge2),

```math
\boxed{B(p^r)\equiv B(p^{r-1})\pmod {p^{3r+3}}.}
\tag{2}
```

Equivalently,

```math
\operatorname{A219562}(p^r-1)
\equiv
\operatorname{A219562}(p^{r-1}-1)
\pmod {p^{3r+3}}.
```

The argument isolates one critical shell. Its last cancellation is the
finite-field identity

```math
\sum_{a\in\mathbb F_p^\times}a^{-2}=0.
\tag{3}
```

## 1. The unit-block quotient

For (N,j\ge1), write

```math
F_N(j)=\binom{N+j-1}{j}.
```

Let (N=p^e), (1\le j<N), and (t=v_p(j)). Cancelling the factors whose
indices are divisible by (p) gives

```math
F_{pN}(pj)=F_N(j)W_{e,j},
\qquad
W_{e,j}=
\prod_{\substack{1\le h<pj\\p\nmid h}}
\left(1+\frac{pN}{h}\right).
\tag{4}
```

### Lemma 1

If (p\ge5) and (0\le t<e), then

```math
v_p(W_{e,j}-1)\ge e+2t+3.
\tag{5}
```

#### Proof

Put

```math
S_m(j)=\sum_{\substack{1\le h<pj\\p\nmid h}}h^{-m}.
```

Complete unit blocks and the involution (h\mapsto pj-h) give the standard
estimates

```math
v_p(S_2(j))\ge t+1,
\qquad
v_p(S_1(j))\ge2t+2.
\tag{6}
```

For completeness, the first estimate follows by reducing modulo
(p^{t+1}): inversion permutes the units and their square sum vanishes.
For the second, pair (h) with (pj-h) and expand

```math
2S_1(j)=-\sum_{m\ge1}(pj)^mS_{m+1}(j).
```

Now

```math
\log W_{e,j}
=\sum_{m\ge1}\frac{(-1)^{m+1}}m(pN)^mS_m(j).
\tag{7}
```

The first two terms have valuations at least (e+2t+3) and
(2e+t+3). Every term of degree at least three has valuation at least
(3e+3). Since (t<e), all three bounds are at least the right side of
(5). Exponentiating preserves the bound. QED

Also,

```math
v_p(F_N(j))=e-t,
\tag{8}
```

because

```math
F_N(j)=\frac Nj\prod_{h=1}^{j-1}\left(1+\frac Nh\right)
```

and every factor in the product is a (p)-adic unit.

## 2. All noncritical shells

Set (e=r-1\ge1) and (N=p^e). Splitting the upper sum according to
whether (p) divides its index gives

```math
\begin{aligned}
B(pN)-B(N)
={}&\sum_{\substack{1\le k<pN\\p\nmid k}}F_{pN}(k)^4\\
&+\sum_{j=1}^{N-1}F_N(j)^4\bigl(W_{e,j}^4-1\bigr).
\end{aligned}
\tag{9}
```

For the second line, (5) and (8) give

```math
v_p\!\left(F_N(j)^4(W_{e,j}^4-1)\right)
\ge5e-2t+3.
\tag{10}
```

If (t\le e-2), this is at least (3e+7), one power beyond the target
(3r+3=3e+6). Thus only (t=e-1) can contribute.

For the first line of (9), every summand has valuation (4(e+1)). This is
at least (3e+6) when (e\ge2). When (e=1), division by (p^8) and
reduction modulo (p) leaves

```math
\sum_{\substack{1\le k<p^2\\p\nmid k}}k^{-4}.
```

Each nonzero residue modulo (p) occurs (p) times, so this sum is zero
modulo (p). Hence the first line always meets the target as well.

## 3. The critical shell

Write the critical indices as (j=p^{e-1}a), (1\le a<p), and put

```math
T_e=\sum_{\substack{1\le u<p^e\\p\nmid u}}u^{-2}.
\tag{11}
```

The complete unit-block identity gives

```math
v_p(T_e)\ge e.
\tag{12}
```

Let (S_2(a)) denote the inverse-square sum over the units below
(ap^e). Decomposing this interval into (a) blocks of length (p^e)
and expanding ((bp^e+u)^{-2}) gives

```math
S_2(a)\equiv aT_e\pmod {p^{e+1}}.
\tag{13}
```

The possible linear correction contains a complete inverse-cube sum, which
vanishes modulo (p).

Pairing (h) with (ap^e-h) gives, modulo (p^{2e+1}),

```math
S_1(a)\equiv-\frac{ap^e}{2}S_2(a).
\tag{14}
```

Substitution into (7), now modulo (p^{3e+2}), yields

```math
\log W_{e,p^{e-1}a}
\equiv
-\frac{a^2}{2}p^{2e+1}T_e
\pmod {p^{3e+2}}.
\tag{15}
```

The square of this logarithm is beyond the displayed precision, so

```math
W_{e,p^{e-1}a}^{,4}-1
\equiv
-2a^2p^{2e+1}T_e
\pmod {p^{3e+2}}.
\tag{16}
```

Finally,

```math
\frac{F_N(p^{e-1}a)}p\equiv a^{-1}\pmod p.
\tag{17}
```

Equations (12), (16), and (17) therefore give

```math
\sum_{a=1}^{p-1}
F_N(p^{e-1}a)^4
\bigl(W_{e,p^{e-1}a}^{,4}-1\bigr)
\equiv
-2p^{2e+5}T_e\sum_{a=1}^{p-1}a^{-2}
\pmod {p^{3e+6}}.
\tag{18}
```

The last sum is zero modulo (p) by (3), while (T_e) already supplies
(p^e). Hence (18) vanishes modulo (p^{3e+6}). Together with Section 2,
this proves (2). QED

## 4. Verification and source boundary

Run

```text
python verification/related/verify_a219562_enhanced_tower.py
```

The checker verifies the exact quotient (4), the shell bounds (5), (8),
and (10), the critical congruences (13)--(18), and the final tower on a
finite grid. These checks support transcription and boundary control; the
unit-block argument above is the proof.

The conjecture is recorded on [OEIS A219562](https://oeis.org/A219562).
Coster proves the ordinary (p^{3r}) baseline, not the three additional
powers proved here. No literature-priority claim is made.
