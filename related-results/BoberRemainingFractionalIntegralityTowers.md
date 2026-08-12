# The four remaining Bober fractional-index towers

**Status date:** August 12, 2026

**Status:** complete elementary proof candidate.  This note proves the two
third-index and two quarter-index integrality conjectures left after the
uniform half-index theorem.  Consequently all 15 approved fractional-index
variants in the current Bober packet are integral and satisfy their full
adjacent cubic towers for every prime `p >= 5`.  Exact checks are supplied;
specialist review and literature priority remain pending.

## 1. Statement

For a balanced Bober factorial ratio

```math
A(M)=\frac{\prod_{a\in U}(aM)!}{\prod_{b\in V}(bM)!},
```

write

```math
B_q(N)=A(N/q)
=\frac{\prod_{a\in U}\Gamma(aN/q+1)}
       {\prod_{b\in V}\Gamma(bN/q+1)}.
\tag{1}
```

The four pairs considered here are

| OEIS record | `q` | `U` | `V` |
| --- | ---: | --- | --- |
| [A295456](https://oeis.org/A295456) | 3 | `30, 5, 4` | `15, 12, 10, 2` |
| [A295458](https://oeis.org/A295458) | 3 | `30, 5, 4` | `15, 10, 8, 6` |
| [A295460](https://oeis.org/A295460) | 4 | `30, 3, 2` | `15, 10, 6, 4` |
| [A295477](https://oeis.org/A295477) | 4 | `24, 1` | `12, 8, 5` |

### Theorem 1

For every row in the table and every integer `N >= 0`,

```math
B_q(N)\in\mathbb Z.
\tag{2}
```

For every prime `p >= 5` and positive integers `n,r`,

```math
\boxed{
B_q(np^r)\equiv B_q(np^{r-1})\pmod {p^{3r}}.
}
\tag{3}
```

Together with the
[uniform half-index theorem](BoberHalfIndexIntegralityTowers.md), this
closes all 15 approved fractional-index formulas in the packet.

## 2. A denominator-transfer lemma

Use signed multiplicities `epsilon_a`, positive on `U` and negative on `V`.
For each of the four rows,

```math
\sum_a a\epsilon_a=0,
\qquad
\sum_{a\equiv s\pmod q}\epsilon_a=0
\quad(1\le s<q).
\tag{4}
```

The first equality is slope balance; the others are residue-class balance.
Write `N=qm+r`, with `0 <= r < q`, and put

```math
k_a=am+\left\lfloor\frac{ar}{q}\right\rfloor,
\qquad
\rho_a\equiv ar\pmod q,
\quad 0\le\rho_a<q.
\tag{5}
```

Define the generalized factorial

```math
F_\rho(k)=q^{-k}\prod_{j=1}^{k}(qj+\rho).
\tag{6}
```

Thus `F_0(k)=k!` and

```math
\Gamma(k+\rho/q+1)=\Gamma(1+\rho/q)F_\rho(k).
```

Residue balance cancels the constant gamma factors, so

```math
B_q(N)=\prod_a F_{\rho_a}(k_a)^{\epsilon_a}\in\mathbb Q.
\tag{7}
```

Let

```math
\Delta(x)=\sum_a\epsilon_a\lfloor ax\rfloor
\tag{8}
```

be the Landau function of the original Bober ratio.  Bober's
classification gives `Delta(x) >= 0` for every real `x`.

### Lemma 2 (coprime-modulus transfer)

Let `d >= 2` be coprime to `q`.  Choose `0 <= c < d` with

```math
qc\equiv r\pmod d,
```

and set `t=m+c`.  The contribution at modulus `d` to the valuation of
the rational product (7) is exactly

```math
\Delta(t/d).
\tag{9}
```

#### Proof

For one coefficient `a`, the contribution is the number

```math
V_a(d)=\#\{1\le j\le k_a:d\mid qj+\rho_a\}.
```

Write `qc=r+hd`.  Since `q` is invertible modulo `d`,

```math
d\mid qj+\rho_a
\quad\Longleftrightarrow\quad
d\mid j-k_a+at.
```

Counting multiples of `d` in the resulting interval gives

```math
V_a(d)=
\left\lfloor\frac{at}{d}\right\rfloor-C_a,
\qquad
C_a=\left\lfloor
\frac{ac-\lfloor ar/q\rfloor}{d}
\right\rfloor.
\tag{10}
```

The constants obey `C_{a+q}=C_a+h`.  Hence, if `a=qL+s`, then
`C_a=hL+C_s`.  On summing with weights `epsilon_a`, every `C_s` term for
`s != 0` vanishes by residue balance, `C_0=0`, and

```math
\sum_a\epsilon_a\left\lfloor\frac aq\right\rfloor
=\frac1q\left(
\sum_a a\epsilon_a-
\sum_{s=1}^{q-1}s\sum_{a\equiv s\ (q)}\epsilon_a
\right)=0.
```

Therefore `sum_a epsilon_a C_a=0`, and (10) sums to (9). `square`

For every prime `ell` not dividing `q`, Legendre counting and (9) now give

```math
v_\ell(B_q(N))
=\sum_{j\ge1}\Delta\!\left(
\frac{m+c_{\ell^j}}{\ell^j}
\right)\ge0.
\tag{11}
```

Only the prime dividing `q` remains.

## 3. Exact denominator-prime valuations

Here `q=p^e`.  Formula (6) gives the complete local rule

```math
v_p(F_0(k))=v_p(k!),
\qquad
v_p(F_\rho(k))=(v_p(\rho)-e)k
\quad(0<\rho<q).
\tag{12}
```

Indeed, when `rho != 0`, every factor `qj+rho` has valuation
`v_p(rho)<e`.  Substitution of the four coefficient vectors into (12)
gives the following exact table whenever `q` does not divide `N`.

| record | residue of `N` | exact denominator-prime valuation |
| --- | --- | --- |
| A295456, `q=3` | `N != 0 (mod 3)` | `N + v_3((10N)!/((5N)!(4N)!))` |
| A295458, `q=3` | `N != 0 (mod 3)` | `3N + v_3((10N)!/((5N)!(2N)!))` |
| A295460, `q=4` | `N` odd | `2N - v_2(N!)` |
| A295460, `q=4` | `N=2s`, `s` odd | `3N + v_2((15s)!s!/((5s)!(3s)!(2s)!))` |
| A295477, `q=4` | `N` odd | `2N + v_2((6N)!/((3N)!(2N)!))` |
| A295477, `q=4` | `N=2s`, `s` odd | `N + v_2((6N)!/((3N)!(2N)!))` |

Every factorial quotient appearing here is an integer.  Explicitly,

```math
\frac{(10N)!}{(5N)!(jN)!}
=\binom{10N}{5N}\frac{(5N)!}{(jN)!}
\quad(j=2,4),
\tag{13}
```

```math
\frac{(15s)!s!}{(5s)!(3s)!(2s)!}
=\binom{15s}{5s,3s,2s,5s}(5s)!s!,
\tag{14}
```

and

```math
\frac{(6N)!}{(3N)!(2N)!}
=\binom{6N}{3N}\frac{(3N)!}{(2N)!}.
\tag{15}
```

Their valuations are therefore nonnegative.  The remaining expression is
also positive because `v_2(N!) <= N-1 < 2N`.  Thus the prime `3` or `2`
also has nonnegative valuation.  If `q` divides `N`, then
`B_q(N)=A(N/q)` is integral by the original Bober theorem.  Together with
(11), this proves (2).

## 4. Cubic towers and completion of the packet

The rational gamma-ratio theorem applies to (1): (4) is exactly its balance
hypothesis, and every prime `p >= 5` is coprime to `q=3,4`.  It gives

```math
\frac{B_q(np^r)}{B_q(np^{r-1})}\equiv1\pmod {p^{3r}}.
```

The integrality just proved permits multiplication by the lower value, so
(3) follows.

The packet now has no remaining approved integrality target:

- eleven `N/2` variants are closed by the uniform half-index theorem;
- the two `N/3` and two `N/4` variants are closed here;
- all 15 inherit the adjacent cubic tower for `p >= 5`.

A295464 still has no approved fractional-index formula visible on its public
OEIS record, so no additional claim is inferred for that record.

## 5. Verification

Run

```text
python verification/related/verify_bober_remaining_fractional.py
```

The checker verifies the coefficient hypotheses, tests (9) over 83,204
coprime-modulus instances, checks exact values and every displayed
denominator-prime valuation through `N=100`, and tests two adjacent cubic
levels.  It reports 84,338 exact checks.

The computation is a transcription and counterexample certificate;
Sections 2--4 contain the proof.

## 6. Sources and boundary

- J. W. Bober,
  [*Factorial ratios, hypergeometric series, and a family of step functions*](https://arxiv.org/abs/0709.1977),
  *J. London Math. Soc.* 79 (2009), 422--444.
- The four linked OEIS records above, whose approved comments state the
  fractional-index integrality conjectures.
- [The complete Bober packet](BoberSporadicFactorialRatioPacket.md), for
  source transcription and all 52 ordinary ratios.

No cubic-tower claim is made here at `p=2` or `p=3`.  No literature-priority
claim is made before independent search and specialist review.
