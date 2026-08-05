# A364176: an affine-Landau integrality proof and cubic tower

**Status date:** August 5, 2026

**Status:** complete elementary proof candidate. The proof closes both the
integrality conjecture and, for every prime $p\ge 5$, the all-level cubic
supercongruence conjecture recorded at OEIS A364176. Exact checks are supplied
as a regression certificate; independent review and literature priority remain
pending.

## 1. Statement

Define fractional factorials by $x!=\Gamma(x+1)$ and put

```math
B(n)=
\frac{(15n)!(5n/2)!(2n)!}
     {(15n/2)!(6n)!(5n)!n!}.
\tag{1}
```

This is [OEIS A364176](https://oeis.org/A364176), equivalently
$A295456(n/2)$.

### Theorem 1

For every $n\ge0$, $B(n)$ is an integer. Moreover, for every prime $p\ge5$
and all positive integers $n,r$,

```math
\boxed{
B(np^r)\equiv B(np^{r-1})\pmod {p^{3r}}.
}
\tag{2}
```

The integrality statement was listed as conjectural on A364176. Once it is
proved, the congruence follows from the repository's rational gamma-ratio
transfer theorem. The new work is therefore the integrality proof.

## 2. Even and odd indices

For $n=2m$, (1) is the ordinary Bober ratio

```math
B(2m)=
\frac{(30m)!(5m)!(4m)!}
     {(15m)!(12m)!(10m)!(2m)!}
=A295456(m),
\tag{3}
```

which is integral by the Vasyunin--Bober classification.

For $n=2m+1$, the half-integer gamma identity

```math
\Gamma\!\left(k+\frac12\right)
=\frac{(2k)!}{4^k k!}\sqrt\pi
```

gives, after cancelling the two square-root factors,

```math
B(2m+1)=2^{20m+10}R(m),
\qquad
R(m)=
\frac{(15m+7)!(4m+2)!}
     {(5m+2)!(12m+6)!(2m+1)!}.
\tag{4}
```

It remains to prove that $R(m)$ is integral.

## 3. The affine floor lemma

For $d\ge2$ define

```math
\Phi_d(m)=
\left\lfloor\frac{15m+7}{d}\right\rfloor
+\left\lfloor\frac{4m+2}{d}\right\rfloor
-\left\lfloor\frac{5m+2}{d}\right\rfloor
-\left\lfloor\frac{12m+6}{d}\right\rfloor
-\left\lfloor\frac{2m+1}{d}\right\rfloor.
\tag{5}
```

### Lemma 2

For all $m\ge0$ and $d\ge2$,

```math
\Phi_d(m)\in\{0,1\}.
\tag{6}
```

### Proof

The coefficients and the constant terms in (5) separately balance, so

```math
\Phi_d(m+d)=\Phi_d(m).
\tag{7}
```

It is enough to take $0\le m<d$. Write

```math
5m+2=qd+s,
\qquad 0\le s<d.
\tag{8}
```

Then $q\in\{0,1,2,3,4\}$. Set

```math
\alpha=\frac{2s+1}{d}\in(0,2),
\qquad
y=\frac{2q+\alpha}{5}=\frac{2m+1}{d}.
\tag{9}
```

The identities

```math
15m+7=3(5m+2)+1,
\quad 4m+2=2(2m+1),
\quad 12m+6=6(2m+1)
```

reduce (5) to

```math
\Phi_d(m)=E_q(\alpha),
```

where

```math
E_q(\alpha)=
2q+\left\lfloor\frac{3\alpha}{2}\right\rfloor
+\lfloor2y\rfloor-\lfloor6y\rfloor-\lfloor y\rfloor.
\tag{10}
```

Here

```math
\left\lfloor\frac{3s+1}{d}\right\rfloor
=\left\lfloor\frac{3\alpha}{2}\right\rfloor:
```

the two arguments differ by $1/(2d)$, while the fractional part of the first
is an integral multiple of $1/d$, so this shift cannot cross an integer.

The remaining verification is a five-row floor calculation. On $0<\alpha<2$,
$E_q(\alpha)=1$ exactly on the intervals below and is zero elsewhere.

| $q$ | intervals on which $E_q(\alpha)=1$ |
| ---: | --- |
| $0$ | $[2/3,5/6)\cup[4/3,5/3)$ |
| $1$ | $[2/3,2)$ |
| $2$ | $(0,1/6)\cup[2/3,1)\cup[4/3,11/6)$ |
| $3$ | $[4/3,2)$ |
| $4$ | $(0,1/3)\cup[2/3,7/6)\cup[4/3,2)$ |

Thus $E_q(\alpha)\in\{0,1\}$ in every case, proving the lemma. $\square$

## 4. Integrality

For a prime $\ell$, Legendre's formula applied to (4) gives

```math
v_\ell(R(m))=
\sum_{j\ge1}\Phi_{\ell^j}(m).
\tag{11}
```

Every summand is nonnegative by Lemma 2, and the sum is finite. Hence
$v_\ell(R(m))\ge0$ for every prime $\ell$, so $R(m)\in\mathbb Z$. Equation
(4) proves integrality at odd indices; (3) proves it at even indices. This
completes the integrality part of Theorem 1.

## 5. The cubic tower

Regard (1) as the residue-balanced rational gamma ratio with positive slopes

```math
15,\quad \frac52,\quad 2
```

and negative slopes

```math
\frac{15}{2},\quad 6,\quad 5,\quad 1.
```

The slopes have equal total sum. Modulo denominator $2$, the only nonzero
fractional class occurs once on each side. The hypotheses of the
[rational gamma-ratio cubic-tower theorem](RationalGammaRatioCubicTowers.md)
therefore hold. For $p\ge5$,

```math
\frac{B(np^r)}{B(np^{r-1})}\equiv1\pmod {p^{3r}}.
\tag{12}
```

The denominator of the lower value is a $p$-adic unit by the theorem, and the
integrality just proved permits multiplication by $B(np^{r-1})$. This yields
(2).

## 6. Why the spectral-theory source is relevant but not load-bearing

Bourbaki's compact-group spectral theory supplies the exact projection
identity behind constant-term methods: normalized Haar integration kills every
nontrivial character and preserves the trivial character. Thus for a Laurent
polynomial $P$ on a compact torus,

```math
\operatorname{CT}(P^n)=\int_{\mathbb T^d}P(z)^n\,d\mu(z).
\tag{13}
```

Peter--Weyl theory replaces torus characters by irreducible matrix
coefficients for a compact nonabelian group. This is useful for organizing the
larger program of constant-term and representation-theoretic sequences.
It is not needed for Lemma 2: the A364176 proof is deliberately an elementary
gamma identity plus Legendre floor counting.

## 7. Verification

Run

```text
python verification/related/verify_a364176_affine_landau.py
```

The checker verifies the OEIS initial values, both parity formulas, the exact
five-case reduction, the floor lemma over a large rectangle, direct
integrality samples, Legendre valuation identities, and adjacent cubic towers.
It is a transcription and counterexample screen; Sections 2--5 contain the
proof.

## 8. Sources and boundary

- [OEIS A364176](https://oeis.org/A364176), formula, initial values, and the
  two conjectures closed here.
- J. W. Bober, [*Factorial ratios, hypergeometric series, and a family of step
  functions*](https://arxiv.org/abs/0709.1977), J. London Math. Soc. 79 (2009),
  422--444.
- N. Bourbaki, *Théories spectrales*, Chapters I--II, 2nd ed., Springer, 2019,
  Proposition 6 in Chapter II, Section 2.
- N. Bourbaki, *Théories spectrales*, Chapters III--V, Springer, 2023,
  Peter--Weyl theorem in Chapter V.

No result is asserted here for $p=2$ or $p=3$. No literature-priority claim is
made until an independent search and review of the affine floor lemma are
complete.
