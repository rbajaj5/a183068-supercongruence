# Odd-unit block Frobenius towers

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

This note proves the full supercongruence conjectures recorded on
[OEIS A091527](https://oeis.org/A091527) and
[OEIS A262732](https://oeis.org/A262732).  Both are instances of one
coefficient family, so the proof closes more than two isolated sequences.

## 1. The family

For integers $m\geq2$ and $N\geq0$, define

```math
A_m(N)
=
[x^N]\left(\frac{(1+x)^m}{(1-x)^{m-2}}\right)^N.
\tag{1}
```

The coefficient definition shows immediately that $A_m(N)$ is an
integer.  A residue calculation gives two useful alternative forms:

```math
A_m(N)
=
4^N\binom{(mN-1)/2}{N}
=
\frac{2^N}{N!}
\prod_{j=0}^{N-1}\bigl(mN-(2j+1)\bigr).
\tag{2}
```

### Theorem 1 (odd-unit block tower)

For every integer $m\geq2$, every prime $p\geq5$, and all
$n,r\geq1$,

```math
A_m(np^r)\equiv A_m(np^{r-1})\pmod {p^{3r}}.
\tag{3}
```

The cases $m=3$ and $m=5$ are respectively A091527 and A262732.
Thus (3) proves the full adjacent-level conjecture on both live OEIS
records.

This theorem deliberately excludes $p=2,3$.  That is a real boundary,
not an omission in the proof:

```math
A_3(3)-A_3(1)=256-4=252,\qquad v_3(252)=2<3,
\tag{4}
```

and

```math
A_5(3)-A_5(1)=2240-8=2232,\qquad v_3(2232)=2<3.
\tag{5}
```

## 2. The coefficient identity

Starting from (1), write the coefficient as a residue and make the
successive substitutions

```math
z=\frac{1+x}{1-x},
\qquad
w=z^2-1.
```

Since

```math
x=\frac{z-1}{z+1},
\qquad
dx=\frac{2\,dz}{(z+1)^2},
\qquad
\frac{(1+x)^m}{(1-x)^{m-2}}
=
\frac{4z^m}{(z+1)^2},
```

we obtain

```math
\begin{aligned}
A_m(N)
&=
\mathop{\mathrm{Res}}_{x=0}
\left(\frac{(1+x)^m}{(1-x)^{m-2}}\right)^N
\frac{dx}{x^{N+1}}\\
&=
\mathop{\mathrm{Res}}_{z=1}
\frac{2\cdot4^N z^{mN}}{(z^2-1)^{N+1}}\,dz\\
&=
\mathop{\mathrm{Res}}_{w=0}
\frac{4^N(1+w)^{(mN-1)/2}}{w^{N+1}}\,dw\\
&=
4^N\binom{(mN-1)/2}{N}.
\end{aligned}
\tag{6}
```

Expanding the generalized binomial coefficient gives the product in
(2).

## 3. Two harmonic cancellations in an odd unit block

Fix $p\geq5$, let $e\geq1$, and put $P=p^e$.  Define

```math
\mathcal O_P
=
\{t:1\leq t<2P,\ t\text{ odd},\ p\nmid t\}.
\tag{7}
```

This is a complete residue system modulo $P$ for
$(\mathbb Z/P\mathbb Z)^\times$: exactly one of $u$ and $u+P$
is odd.

### Lemma 2 (odd-block reciprocal sums)

In the localization $\mathbb Z_{(p)}$,

```math
\sum_{t\in\mathcal O_P}\frac1t\equiv0\pmod {P^2},
\qquad
\sum_{t\in\mathcal O_P}\frac1{t^2}\equiv0\pmod P.
\tag{8}
```

#### Proof

The second sum is the sum of $u^{-2}$ over all units modulo $P$.
Choose a unit $c$ whose square is not $1$ modulo $p$.
Multiplication by $c$ permutes the units, so

```math
\sum_u u^{-2}
\equiv
c^{-2}\sum_u u^{-2}\pmod P.
```

Because $1-c^{-2}$ is a unit, the sum is $0$ modulo $P$.

For the first sum, pair $t$ with $2P-t$.  Modulo $P^2$,

```math
\frac1t+\frac1{2P-t}
=
\frac{2P}{t(2P-t)}
\equiv
-\frac{2P}{t^2}.
\tag{9}
```

The sum of $t^{-2}$ over one representative from each pair is
$0$ modulo $P$: twice that half-sum is the full inverse-square
sum in (8), and $2$ is a unit.  Equation (9) proves the first
congruence.

### Corollary 3 (any number of odd blocks)

If $N=hP$, then

```math
\sum_{\substack{1\leq t<2N\\t\text{ odd}\\p\nmid t}}\frac1t
\equiv0\pmod {P^2},
\qquad
\sum_{\substack{1\leq t<2N\\t\text{ odd}\\p\nmid t}}\frac1{t^2}
\equiv0\pmod P.
\tag{10}
```

Indeed, partition the range into the $h$ blocks
$\mathcal O_P+2bP$.  For $t\in\mathcal O_P$,

```math
\frac1{t+2bP}
\equiv
\frac1t-\frac{2bP}{t^2}\pmod {P^2},
\qquad
\frac1{(t+2bP)^2}\equiv\frac1{t^2}\pmod P,
\tag{11}
```

and apply Lemma 2 in every block.

## 4. Splitting off the divisible factors

Put

```math
N=np^r,\qquad M=N/p.
```

In the numerator product in (2), the factor indexed by the odd integer
$t=2j+1$ is divisible by $p$ precisely when $p\mid t$.
Writing $t=pu$ identifies all such factors with

```math
mN-pu=p(mM-u),
```

where $u$ runs over the odd integers $1\leq u<2M$.
The divisible factors in $N!$ similarly reproduce $M!$.  Therefore

```math
\frac{A_m(N)}{A_m(M)}
=
\frac{2^{N-M}
\displaystyle\prod_{\substack{1\leq t<2N\\t\text{ odd}\\p\nmid t}}
(mN-t)}
\displaystyle{\prod_{\substack{1\leq k\leq N\\p\nmid k}}k}.
\tag{12}
```

There are $N-M=M(p-1)$ factors in the numerator of (12), an even
number.  Extracting $-t$ from each factor gives

```math
\frac{A_m(N)}{A_m(M)}
=
J_p(N)\,H_m(N),
\tag{13}
```

where

```math
J_p(N)
=
\frac{\binom{2N}{N}}{\binom{2M}{M}}
\tag{14}
```

and

```math
H_m(N)
=
\prod_{\substack{1\leq t<2N\\t\text{ odd}\\p\nmid t}}
\left(1-\frac{mN}{t}\right).
\tag{15}
```

To see (14), let

```math
U_p(L)=\prod_{\substack{1\leq k\leq L\\p\nmid k}}k.
```

The odd unit product in (12) is

```math
\frac{U_p(2N)}{2^{N-M}U_p(N)},
```

so its contribution is $U_p(2N)/U_p(N)^2$, exactly the quotient
of the two central binomial coefficients in (14).

## 5. The two factors in (13)

The Ljunggren--Jacobsthal--Kazandzidis congruence gives

```math
J_p(N)\equiv1\pmod {p^{\,3+3v_p(M)}}.
\tag{16}
```

Since $v_p(M)\geq r-1$, this is $1$ modulo $p^{3r}$.

It remains to treat $H_m(N)$.  Let $e=v_p(N)$, $P=p^e$, and
write

```math
S_j=
\sum_{\substack{1\leq t<2N\\t\text{ odd}\\p\nmid t}}\frac1{t^j}.
```

Corollary 3 says

```math
S_1\in P^2\mathbb Z_{(p)},
\qquad
S_2\in P\mathbb Z_{(p)}.
\tag{17}
```

Expand the finite product (15) in elementary symmetric functions.
Its linear term is $-mNS_1$, hence is divisible by $P^3$.
Its quadratic term is

```math
(mN)^2\frac{S_1^2-S_2}{2},
\tag{18}
```

which is also divisible by $P^3$.  Every term of degree at least
three contains $N^3$.  Consequently

```math
H_m(N)\equiv1\pmod {p^{3e}},
\tag{19}
```

and therefore modulo $p^{3r}$.

Equations (13), (16), and (19) show that

```math
\frac{A_m(N)}{A_m(M)}\equiv1\pmod {p^{3r}}.
```

Since $A_m(M)$ is an integer, multiplying through proves Theorem 1.
$\square$

## 6. What has and has not been proved

This note proves:

- the complete $p^{3r}$ conjecture on A091527;
- the complete $p^{3r}$ conjecture on A262732; and
- the same theorem for every coefficient sequence $A_m$ in (1).

It does not claim:

- a $p=2$ or $p=3$ extension;
- that every half-integral factorial ratio has this property; or
- literature priority for the family theorem.

The proof uses only a coefficient identity, the classical central-binomial
scaling congruence, and the explicit odd-unit harmonic cancellation in
Lemma 2.

## 7. Literature boundary

Targeted searches by both OEIS identifiers and by the exact formula
$4^N\binom{(mN-1)/2}{N}$ located Bala's prime-level argument and the
stated higher-level conjectures, but did not locate a proof of the full
adjacent-level theorem above.  This is useful routing evidence, not a
priority certificate; a specialist search is still required before any
novelty claim.

## 8. Verification

Run:

```text
python verification/related/verify_odd_unit_block_towers.py
```

The checker verifies the coefficient identity, the exact block
factorization (13), both harmonic congruences, the family tower over a
range of $m,n,p,r$, the two OEIS initial sequences, and the stated
small-prime boundary failures.
