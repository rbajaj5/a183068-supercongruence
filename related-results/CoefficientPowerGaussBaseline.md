# Integral coefficient roots and the universal Gauss baseline

**Status:** complete elementary theorem and exact applications; the cubic
conjectures on A008978 and A113424 remain open.

Several records in the Bala census introduce an apparently integral series
$F(x)$ by requiring

```math
[x^n]F(x)^{cn}=A(n),
\tag{1}
```

and then conjecture that the more general coefficients
$[x^n]F(x)^{kn}$ satisfy a cubic Frobenius tower.  This note separates
three logically different questions:

1. whether the displayed series $F$ is actually integral;
2. how $F$ is related to the exponential series occurring on A008978; and
3. how much congruence follows from integrality alone.

The first two questions have exact answers.  Integrality alone supplies a
universal $p^r$ tower.  The additional two powers in the conjectural
$p^{3r}$ tower require arithmetic beyond this general mechanism.

## 1. The normalized Gauss criterion

Let $B(1),B(2),\ldots$ be integers.  Say that $B$ has the Gauss property
if, for every prime $p$ and positive integers $m,r$,

```math
B(mp^r)\equiv B(mp^{r-1})\pmod {p^r}.
\tag{2}
```

### Lemma 1

If $B$ has the Gauss property, then

```math
E(x)=
\exp\left(\sum_{n\ge1}\frac{B(n)}n x^n\right)
\tag{3}
```

belongs to $1+x\mathbb Z[[x]]$.

#### Proof

Define

```math
e_m=
\frac1m\sum_{d\mid m}\mu(m/d)B(d).
\tag{4}
```

Fix $p^r\mid m$ with $p^{r+1}\nmid m$, and write $m=p^rq$,
$p\nmid q$.  Pairing the divisors with $p$-adic exponents $r$ and
$r-1$ rewrites the numerator in (4) as

```math
\sum_{d\mid q}\mu(q/d)
\left(B(dp^r)-B(dp^{r-1})\right).
```

It is divisible by $p^r$ by (2).  This holds for every prime power
dividing $m$, so $e_m$ is an integer.  Möbius inversion now gives

```math
E(x)=\prod_{m\ge1}(1-x^m)^{-e_m}.
\tag{5}
```

Every exponent in this formal Euler product is integral, proving the
claim. $\square$

## 2. The canonical coefficient root

Let $A(n)$ be integers for $n\ge1$, put $c=A(1)>0$, and assume:

- $c$ divides $A(n)$ for every $n\ge1$; and
- $B(n)=A(n)/c$ has the Gauss property.

Let $E$ be the integral series in (3), and define

```math
Y=xE(x)^c.
\tag{6}
```

The series $Y=x+O(x^2)$ has an integral compositional inverse.  Therefore
there is a unique $F\in1+x\mathbb Z[[x]]$ satisfying

```math
E(x)=F\!\left(xE(x)^c\right).
\tag{7}
```

### Theorem 2

The series $F$ satisfies

```math
[x^n]F(x)^{cn}=A(n)
\qquad(n\ge1).
\tag{8}
```

Moreover, for every positive integer $k$,

```math
(k+c)[x^n]E(x)^{kn}
=
k[x^n]F(x)^{(k+c)n}.
\tag{9}
```

#### Proof

Equation (7) says that $Y=xF(Y)^c$.  Lagrange inversion gives

```math
\begin{aligned}
[x^n]\log E(x)
&=[x^n]\log F(Y)\\
&=\frac1n[x^{n-1}]
\frac{F'(x)}{F(x)}F(x)^{cn}\\
&=\frac1{cn}[x^n]F(x)^{cn}.
\end{aligned}
\tag{10}
```

The left side is $B(n)/n=A(n)/(cn)$, proving (8).

Apply Lagrange inversion once more, now to $F(Y)^{kn}$:

```math
\begin{aligned}
[x^n]E(x)^{kn}
&=\frac1n[x^{n-1}]
knF(x)^{kn-1}F'(x)F(x)^{cn}\\
&=\frac{k}{k+c}[x^n]F(x)^{(k+c)n}.
\end{aligned}
```

This is (9). $\square$

Equation (9) is an exact bridge, not an unconditional equivalence of the
cubic conjectures: at primes dividing $k(k+c)$, its scalar factor can
change the available $p$-adic precision.

## 3. A universal congruence for variable powers

### Theorem 3

Let

```math
H(x)=\sum_{j\ge0}h_jx^j\in\mathbb Z[[x]]
```

and fix a positive integer $k$.  Define

```math
b_k(N)=[x^N]H(x)^{kN}.
\tag{11}
```

For every prime $p$ and positive integers $n,r$,

```math
\boxed{
b_k(np^r)\equiv b_k(np^{r-1})\pmod {p^r}.
}
\tag{12}
```

#### Proof

Replace $H(x)^k$ by

```math
G(x)=\sum_{j\ge0}g_jx^j.
```

Then $b_k(N)$ is the total weight of all words

```math
(j_1,\ldots,j_N)\in\mathbb Z_{\ge0}^{N},
\qquad
j_1+\cdots+j_N=N,
```

where the word has weight $\prod_i g_{j_i}$.  Rotate the words
cyclically.  A word of minimal period $d\mid N$ is the repetition
$N/d$ times of a primitive word of length $d$ whose entries sum to $d$.
If $\mathcal R_d$ is a set of primitive cyclic-orbit representatives
and $w(\omega)$ is the weight of one primitive block, then

```math
b_k(N)=
\sum_{d\mid N}
d\sum_{\omega\in\mathcal R_d}
w(\omega)^{N/d}.
\tag{13}
```

Put $N=np^r$, $M=N/p$, and $e=v_p(N)\ge r$.  If $d\mid N$ but
$d\nmid M$, then $p^e\mid d$, so the corresponding term in (13) is
already divisible by $p^e$.

For $d\mid M$, put $q=N/d$.  The difference of the corresponding
summands in (13) contains

```math
d\left(w^q-w^{q/p}\right).
```

For every integer $w$,

```math
v_p\left(w^{pm}-w^m\right)\ge1+v_p(m).
\tag{14}
```

For $p\nmid w$, this is Fermat's theorem followed by the
lifting-the-exponent lemma; for $p\mid w$ it is immediate, and the
binary odd-unit case follows from the usual two-adic lifting formula.
Taking $m=q/p$ shows that the last display has valuation at least

```math
v_p(d)+v_p(q)=e.
```

Thus every orbit contribution to $b_k(N)-b_k(M)$ is divisible by
$p^e$, hence by $p^r$. $\square$

Theorem 3 is sharp for a general integral $H$.  It does not by itself
explain a cubic tower.

## 4. Three factorial-ratio applications

Consider

```math
\begin{aligned}
A_2(n)&=\binom{2n}{n}^{3},
&c_2&=8,\\
A_5(n)&=\frac{(5n)!}{(n!)^5},
&c_5&=120,\\
A_6(n)&=\frac{(6n)!}{(3n)!(2n)!n!},
&c_6&=60.
\end{aligned}
\tag{15}
```

These are A002897, A008978, and A113424.

### Lemma 4

For $s\in\{2,5,6\}$, the quotient $A_s(n)/c_s$ is an integer and has
the Gauss property.

#### Proof

The central binomial coefficient is even for $n\ge1$, so
$8\mid A_2(n)$.  The symmetric group on five letters acts freely by
relabeling the words counted by the five-part multinomial coefficient
$A_5(n)$, so $120\mid A_5(n)$.

For $A_6$, Legendre's formula uses

```math
\lambda_q(n)=
\left\lfloor\frac{6n}{q}\right\rfloor
-\left\lfloor\frac{3n}{q}\right\rfloor
-\left\lfloor\frac{2n}{q}\right\rfloor
-\left\lfloor\frac{n}{q}\right\rfloor.
\tag{16}
```

If $n=\ell^a u$ with $\ell\nmid u$, then the level
$q=\ell^{a+1}$ contributes one carry for $\ell=3$ and for $\ell=5$.
For $\ell=2$, the two consecutive levels
$q=2^{a+1},2^{a+2}$ each contribute one carry.  These statements reduce
respectively to the nonzero residue classes modulo $3$, $5$, and $4$.
Hence

```math
v_2(A_6(n))\ge2,\qquad
v_3(A_6(n))\ge1,\qquad
v_5(A_6(n))\ge1,
```

so $60\mid A_6(n)$.

It remains to prove the Gauss property.  Each $A_s$ is a product of
ordinary binomial or multinomial coefficients with all entries scaled
by $n$.  The adjacent Ljunggren--Jacobsthal--Kazandzidis estimate gives

```math
\frac{A_s(N)}{A_s(N/p)}
\equiv1\pmod {p^{3e-\varepsilon_p}},
\qquad
e=v_p(N),
\tag{17}
```

where $\varepsilon_2=2$, $\varepsilon_3=1$, and
$\varepsilon_p=0$ for $p\ge5$.  Since
$3e-\varepsilon_p\ge e$ for every $e\ge1$, multiplication by the
integer $A_s(N/p)/c_s$ proves (2) for $A_s/c_s$.

At $p=2$, the scaling theorem is sometimes stated with a possible
sign.  Here that sign causes no gap: when $e=1$ the modulus in (17) is
$2$, so $-1\equiv1$; when $e\ge2$, every positive lower component in
the extracted one-step quotient contains the factor $2^{e-1}$, and the
exceptional odd-lower-entry sign case is impossible. $\square$

Theorems 2 and 3 now give the following exact conclusions.

### Corollary 5

For each of A002897, A008978, and A113424, the canonical coefficient
root $F$ in (8) has integer coefficients.  Its Lagrange companion $E$
also has integer coefficients, and (9) relates their variable-power
families exactly.

Every sequence

```math
[x^n]F(x)^{kn}
\quad\text{or}\quad
[x^n]E(x)^{kn}
```

satisfies the all-prime $p^r$ tower (12).

For example, the construction recovers the coefficients printed on the
OEIS pages:

```text
A002897 F: 1, 1, 6, 111, 2806, 84456, ...
A008978 F: 1, 1, 353, 318986, 408941594, ...
A008978 E: 1, 1, 473, 467606, 637121154, ...
A113424 F: 1, 1, 56, 7355, 1290319, ...
```

## 5. Exact source boundary

- On A002897, the former rational-diagonal conjecture is now marked
  proved and linked to a Lean file.  The coefficient-root integrality
  above is an additional exact deduction, but there is no remaining
  explicit Bala supercongruence on the live record.
- On A008978, the source conjectures a $p^{3r}$ tower for both the $E$
  and $F$ variable-power families.  This note proves their integrality,
  relates them by (9), and supplies the universal $p^r$ baseline.  The
  extra $2r$ powers remain open.
- On A113424, the base $p^{3r}$ tower is already a classical
  binomial-scaling consequence.  This note proves the displayed $F$
  integral and supplies the universal $p^r$ baseline for its
  variable-power family.  Its conjectural $p^{3r}$ tower remains open.

Thus this note closes the integrality obligations and consolidates the
remaining cubic work; it does not claim to prove the two cubic
coefficient-power conjectures.

## 6. References

- [OEIS A002897](https://oeis.org/A002897).
- [OEIS A008978](https://oeis.org/A008978).
- [OEIS A113424](https://oeis.org/A113424).
- [Meštrović, *Wolstenholme's theorem: Its Generalizations and
  Extensions in the last hundred and fifty years
  (1862--2012)*](https://arxiv.org/abs/1111.3057), for the adjacent
  binomial scaling estimates.

## 7. Verification

Run:

```text
python verification/related/verify_coefficient_power_gauss_baseline.py
```

The checker reconstructs all three integral roots, checks the printed
coefficients, verifies (7)--(9), tests the normalized Gauss criterion,
and checks the cyclic-orbit congruence on a finite family of integral
series.  It reports 1,819 exact checks, including 140 cases attaining the
universal exponent exactly.  These computations are regression evidence;
the proofs above do not depend on a finite search.
