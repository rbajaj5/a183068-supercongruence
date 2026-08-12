# All eleven Bober half-index variants are integral

**Status date:** August 12, 2026

**Status:** complete elementary proof candidate.  The argument proves the
eleven global integrality conjectures at index `N/2` currently recorded in
the Bober sporadic packet.  Combined with the repository's rational
gamma-ratio theorem, it also proves their full adjacent cubic towers for
every prime `p >= 5`.  Exact checks are supplied as a regression certificate;
specialist review and literature priority remain pending.

## 1. Statement

Let

```math
A(N)=\frac{\prod_{u\in U}(uN)!}{\prod_{v\in V}(vN)!}
```

be one of the following eleven Bober sporadic factorial ratios, and define
fractional factorials by `x! = Gamma(x+1)`:

```math
B(N)=A(N/2)
=\frac{\prod_{u\in U}\Gamma(uN/2+1)}
       {\prod_{v\in V}\Gamma(vN/2+1)}.
\tag{1}
```

| OEIS record | `U` | `V` |
| --- | --- | --- |
| [A295456](https://oeis.org/A295456) | `30, 5, 4` | `15, 12, 10, 2` |
| [A295458](https://oeis.org/A295458) | `30, 5, 4` | `15, 10, 8, 6` |
| [A295460](https://oeis.org/A295460) | `30, 3, 2` | `15, 10, 6, 4` |
| [A295465](https://oeis.org/A295465) | `30, 5, 3` | `15, 12, 10, 1` |
| [A295468](https://oeis.org/A295468) | `30, 5, 3, 2` | `15, 10, 8, 6, 1` |
| [A295470](https://oeis.org/A295470) | `20, 6, 1` | `12, 10, 3, 2` |
| [A295471](https://oeis.org/A295471) | `20, 1` | `10, 8, 3` |
| [A295475](https://oeis.org/A295475) | `20, 3` | `10, 9, 4` |
| [A295477](https://oeis.org/A295477) | `24, 1` | `12, 8, 5` |
| [A295479](https://oeis.org/A295479) | `24, 4, 1` | `12, 8, 7, 2` |
| [A295481](https://oeis.org/A295481) | `24, 4, 3` | `12, 9, 8, 2` |

### Theorem 1

For every record in the table and every integer `N >= 0`,

```math
B(N)\in\mathbb Z.
\tag{2}
```

Moreover, for every prime `p >= 5` and positive integers `n,r`,

```math
\boxed{
B(np^r)\equiv B(np^{r-1})\pmod {p^{3r}}.
}
\tag{3}
```

The proof of (2) is new work in this note.  Formula (3) is then a direct
application of the already proved rational gamma-ratio transfer theorem.

## 2. A parity-transfer lemma

Write `epsilon_a` for the multiplicity of `a` in `U` minus its multiplicity
in `V`.  All eleven rows have

```math
\sum_a a\epsilon_a=0,
\qquad
\sum_{a\text{ odd}}\epsilon_a=0.
\tag{4}
```

The first identity is ordinary balance.  The second is residue balance
modulo `2`.

For an odd index `N=2m+1`, apply

```math
\Gamma(k+1/2)=\frac{(2k)!}{4^k k!}\sqrt\pi
```

to every odd coefficient.  The square roots cancel by (4), giving

```math
B(2m+1)=2^{\lambda(2m+1)}R(m),
\qquad
\lambda=-\sum_{a\text{ odd}}a\epsilon_a,
\tag{5}
```

where `R(m)` is the rational factorial ratio obtained by replacing each
factor of coefficient `a` by

```math
T_a(m)=
\begin{cases}
(am+a/2)!,&a\text{ even},\\[3pt]
\dfrac{(2am+a+1)!}{(am+(a+1)/2)!},&a\text{ odd}.
\end{cases}
\tag{6}
```

Thus `R(m) = product_a T_a(m)^{epsilon_a}`.

Let

```math
\Delta(x)=\sum_a\epsilon_a\lfloor ax\rfloor
\tag{7}
```

be the Landau step function of the original Bober ratio.  Bober's
integrality classification gives

```math
\Delta(x)\ge 0\qquad(x\in\mathbb R).
\tag{8}
```

### Lemma 2 (odd-prime transfer)

For every odd integer `d >= 3`, the contribution at modulus `d` to the
Legendre valuation of `R(m)` is

```math
\Delta\!\left(\frac{t}{d}\right),
\qquad
t=m+\frac{d+1}{2}.
\tag{9}
```

#### Proof

For a coefficient `a`, let `D_a(m,d)` be its contribution before
multiplication by `epsilon_a`.  Formula (6) gives

```math
D_a(m,d)=
\begin{cases}
\left\lfloor\dfrac{am+a/2}{d}\right\rfloor,&a\text{ even},\\[8pt]
\left\lfloor\dfrac{2am+a+1}{d}\right\rfloor
-\left\lfloor\dfrac{am+(a+1)/2}{d}\right\rfloor,&a\text{ odd}.
\end{cases}
```

A direct two-case floor calculation gives

```math
D_a(m,d)=
\left\lfloor\frac{at}{d}\right\rfloor-\left\lfloor\frac a2\right\rfloor.
\tag{10}
```

For odd `a`, the only observation needed is that, for `0 <= s < d` and odd
`d`,

```math
\left\lfloor\frac{2s}{d}\right\rfloor
=\left\lfloor\frac{s+(d-1)/2}{d}\right\rfloor.
```

After multiplying (10) by `epsilon_a` and summing, the constant disappears:

```math
\sum_a\epsilon_a\left\lfloor\frac a2\right\rfloor
=\frac12\left(
\sum_a a\epsilon_a-
\sum_{a\text{ odd}}\epsilon_a
\right)=0
```

by (4).  This proves (9).  `square`

For an odd prime `ell`, Legendre's formula and (9) now give

```math
v_\ell(R(m))
=\sum_{j\ge1}\Delta\!\left(
\frac{m+(\ell^j+1)/2}{\ell^j}
\right)\ge0.
\tag{11}
```

So only the prime `2` remains.

## 3. The entire dyadic obstruction is a digit-sum inequality

Let `s_2(k)` denote the number of ones in the binary expansion of `k`.
Legendre's identity

```math
v_2(k!)=k-s_2(k)
\tag{12}
```

applied to (6) has no linear remainder: both the slopes and intercepts of
the signed factorial arguments balance.  Using only

```math
s_2(2k)=s_2(k),
\tag{13}
```

the eleven rows reduce as follows, with `N=2m+1`.

| records | exact value of `v_2(R(m))` |
| --- | --- |
| A295456, A295458, A295460, A295465, A295468 | `s_2(3N) + s_2(5N) - s_2(15N)` |
| A295470, A295471, A295475, A295477, A295479, A295481 | `s_2(N)` |

The second row is nonnegative.  For the first row, binary digit sums are
subadditive:

```math
s_2(x+y)\le s_2(x)+s_2(y).
```

Since

```math
15N=3N+4(3N)=5N+2(5N),
```

we have

```math
s_2(15N)\le 2s_2(3N),
\qquad
s_2(15N)\le 2s_2(5N).
```

Therefore

```math
s_2(15N)
\le\min\{2s_2(3N),2s_2(5N)\}
\le s_2(3N)+s_2(5N).
\tag{14}
```

Thus `v_2(R(m)) >= 0` in every row.  Equation (11) handles every odd
prime, so `R(m)` is an integer.  The displayed values of `lambda` are

| record | A295456 | A295458 | A295460 | A295465 | A295468 | A295470 | A295471 | A295475 | A295477 | A295479 | A295481 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `lambda` | 10 | 10 | 12 | 8 | 8 | 2 | 2 | 6 | 4 | 6 | 6 |

and are all positive.  Hence (5) proves integrality at odd indices.  At
even indices, `B(2m)=A(m)`, which is integral by Bober's classification.
This proves (2).

## 4. Cubic towers

The slopes `a/2` in (1) are balanced.  The second identity in (4) is exactly
the nonzero residue-class balance required by the repository's
[rational gamma-ratio cubic-tower theorem](RationalGammaRatioCubicTowers.md).
For every prime `p >= 5`, that theorem gives

```math
\frac{B(np^r)}{B(np^{r-1})}\equiv1\pmod {p^{3r}}.
```

The integrality just proved allows multiplication by the lower value, which
yields (3).

## 5. What remains in the fractional Bober packet

This theorem closes every approved `N/2` integrality claim in the packet.
The four fractional-index claims not covered here are

- A295456 and A295458 at `N/3`;
- A295460 and A295477 at `N/4`.

Their odd-prime quotient congruences are already covered by the rational
gamma-ratio theorem.  Their global integrality is the remaining obligation.
A295464 currently has no approved fractional-index comment on its public
OEIS record and is therefore not assigned an unverified formula here.

## 6. Verification

Run

```text
python verification/related/verify_bober_half_index.py
```

The checker:

1. reconstructs (5)--(6) from the eleven coefficient vectors;
2. verifies balance and the exact digit-sum certificate symbolically;
3. tests the floor identity (9) at 57,200 points;
4. checks exact gamma-ratio values, integrality, and valuations; and
5. tests two adjacent cubic levels for `p = 5, 7, 11`.

It reports 59,467 exact checks.  The script is a transcription and
counterexample screen; Sections 2--4 contain the proof.

## 7. Sources and boundary

- J. W. Bober,
  [*Factorial ratios, hypergeometric series, and a family of step functions*](https://arxiv.org/abs/0709.1977),
  *J. London Math. Soc.* 79 (2009), 422--444.
- The eleven linked OEIS records above, whose approved comments state the
  fractional-index integrality conjectures.
- [The Bober sporadic factorial-ratio packet](BoberSporadicFactorialRatioPacket.md),
  for the 52 ordinary ratios and all fractional variants.

No claim is made here for a cubic tower at `p=2` or `p=3`.  Those primes are
outside the stated OEIS conjectures and the rational-binomial unit-block
theorem.  No literature-priority claim is made before independent search and
specialist review.
