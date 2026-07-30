# A prime-coefficient packet for modular products

**Status:** complete elementary proof candidate for seven named OEIS records;
quadratic baselines for four further records; two route-M records remain
without a proved baseline

## 1. The source claims

This note records the exact disposition of the 14 modular or infinite-product
records in the repository's Bala census.  The claims below were read from the
live OEIS pages on July 29, 2026.

| Record | Claim relevant to this packet | Disposition |
| --- | --- | --- |
| [A008485](https://oeis.org/A008485) | $a(p)\equiv p+1\pmod {p^2}$, $p\ge3$ | proved in Corollary 2 |
| [A008705](https://oeis.org/A008705) | $a(p)\equiv-1-p$ and $a(2p)\equiv p-1\pmod {p^2}$, $p\ge3$ | proved in Corollary 2 and Theorem 3 |
| [A008793](https://oeis.org/A008793) | $a(np^r)\equiv a(np^{r-1})^p\pmod {p^{4r}}$ | still open |
| [A023871](https://oeis.org/A023871) | the derived coefficient sequence has a $p^{3r}$ tower for $p\ge7$ | $p^{2r}$ baseline proved |
| [A023873](https://oeis.org/A023873) | every integral-power derived sequence has a $p^{3r}$ tower for $p\ge7$ | $p^{2r}$ baseline proved |
| [A049505](https://oeis.org/A049505) | three prime-power congruences for symmetric plane partitions | still open |
| [A206622](https://oeis.org/A206622) | every integral-power derived sequence has a $p^{3r}$ tower for $p\ge5$ | $p^{2r}$ baseline proved |
| [A229452](https://oeis.org/A229452) | a coefficient-power $p^{3r}$ tower and a parameterized extension | integrality and $p^r$ baseline proved in a follow-on |
| [A255672](https://oeis.org/A255672) | $a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}$, $p\ge3$ | proved by Theorem 4 |
| [A270913](https://oeis.org/A270913) | $a(p)\equiv p+1\pmod {p^2}$ | proved in Corollary 2 |
| [A270919](https://oeis.org/A270919) | $a(p)\equiv2p+2\pmod {p^2}$ | proved in Corollary 2 |
| [A270922](https://oeis.org/A270922) | $a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}$, $p\ge3$ | proved by Theorem 4 |
| [A270924](https://oeis.org/A270924) | $a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}$, $p\ge3$ | proved by Theorem 4 |
| [A283271](https://oeis.org/A283271) | every integral-power derived sequence has a $p^{3r}$ tower for $p\ge7$ | $p^{2r}$ baseline proved |

The table is a claim-level classification.  It does not say that every
comment on a record labeled “proved” has been settled.

## 2. A universal first-prime coefficient

Let

```math
F(x)=\prod_{m\ge1}(1-x^m)^{h_m},
\qquad h_m\in\mathbb Z.
\tag{1}
```

Negative powers are interpreted in the formal power-series ring.

### Theorem 1

For every odd prime $p$,

```math
[x^p]F(x)^p\equiv-h_1-ph_p\pmod {p^2}.
\tag{2}
```

### Proof

In $\mathbb Q[[x]]$, put $L(x)=\log F(x)$.  Direct expansion gives

```math
[x^p]L(x)=-h_p-\frac{h_1}{p},
\tag{3}
```

because the only factorizations $p=mj$ are $(m,j)=(p,1)$ and
$(1,p)$.

Now $F(x)^p=\exp(pL(x))$.  In the coefficient of $x^p$, the linear
term contributes

```math
p[x^p]L(x)=-ph_p-h_1.
\tag{4}
```

Every term with $k\ge2$ factors from $L$ uses only coefficients of
degrees strictly below $p$, hence coefficients in the localization
$\mathbb Z_{(p)}$.  Its scalar factor is $p^k/k!$, whose $p$-adic
valuation is at least two for every $k\ge2$ and odd $p$.  All nonlinear
terms therefore vanish modulo $p^2$, proving (2). $\square$

### Corollary 2

The prime-level conjectures on A008485, A008705, A270913, and A270919 hold.

Indeed, write the four underlying products in the form (1):

```math
\begin{array}{c|cc}
F(x)&h_1&h_p\quad(p\text{ odd})\\ \hline
\prod_{m\ge1}(1-x^m)^{-1}&-1&-1\\
\prod_{m\ge1}(1-x^m)&1&1\\
\prod_{m\ge1}(1+x^m)&-1&-1\\
\prod_{m\ge1}\dfrac{1+x^m}{1-x^m}&-2&-2.
\end{array}
\tag{5}
```

For the third and fourth rows, use

```math
1+x^m=\frac{1-x^{2m}}{1-x^m}.
```

Theorem 1 gives, respectively,

```math
p+1,\qquad -p-1,\qquad p+1,\qquad 2p+2
\pmod {p^2},
```

which are exactly the four displayed OEIS claims.

## 3. The second A008705 congruence

Let

```math
E(x)=\prod_{m\ge1}(1-x^m).
```

The A008705 definition is $a(N)=[x^N]E(x)^N$.

### Theorem 3

For every odd prime $p$,

```math
a(2p)\equiv p-1\pmod {p^2}.
\tag{6}
```

### Proof

Put $G(x)=E(x)^2$.  Splitting the logarithm according to whether the
logarithmic summation index is divisible by $p$ gives the exact identity

```math
p\log G(x)=\log G(x^p)+pD_p(x),
\tag{7}
```

where

```math
D_p(x)=-2\sum_{\substack{m,j\ge1\\p\nmid j}}\frac{x^{mj}}{j}
\in\mathbb Z_{(p)}[[x]].
\tag{8}
```

Consequently,

```math
G(x)^p=G(x^p)\exp(pD_p(x))
\equiv G(x^p)(1+pD_p(x))\pmod {p^2}.
\tag{9}
```

Euler's pentagonal theorem, or direct multiplication through degree two,
gives

```math
[x]G(x)=-2,\qquad [x^2]G(x)=-1.
\tag{10}
```

For odd $p$, equation (8) gives

```math
[x^p]D_p(x)=-2,\qquad
[x^{2p}]D_p(x)=-2\left(1+\frac12\right)=-3.
\tag{11}
```

Taking the coefficient of $x^{2p}$ in (9) therefore yields

```math
a(2p)\equiv
-1+p\bigl((-3)+(-2)(-2)\bigr)
=p-1\pmod {p^2}.
```

This proves the second A008705 conjecture. $\square$

## 4. Three complete quadratic towers

The repository's
[colored Euler-product theorem](EulerProductGaussianTower.md) proves that,
for every odd prime $p$, $n,r\ge1$, and every integral product whose
part-$m$ exponent is an integral multiple of $Nm^d$ with $d\ge1$,

```math
[x^{np^r}]H(x)^{np^r}
\equiv
[x^{np^{r-1}}]H(x)^{np^{r-1}}
\pmod {p^{2r}}.
\tag{12}
```

Taking $d=1$ proves the full conjectured towers on:

```math
\begin{array}{c|c}
\text{record}&\text{coefficient product}\\ \hline
\text{A255672}&[x^N]\prod_{m\ge1}(1-x^m)^{-mN}\\
\text{A270922}&[x^N]\prod_{m\ge1}(1+x^m)^{mN}\\
\text{A270924}&[x^N]\prod_{m\ge1}
\left(\dfrac{1+x^m}{1-x^m}\right)^{mN}.
\end{array}
\tag{13}
```

Thus A255672, A270922, and A270924 are not merely checked at the first
prime level: their stated $p^{2r}$ towers hold for every odd prime and
every positive $n,r$.

## 5. Four rigorous quadratic baselines

The same theorem applies with $d=2$ or $d=4$ to the derived sequences
on A023871, A023873, A206622, and A283271.  It proves

```math
u(np^r)\equiv u(np^{r-1})\pmod {p^{2r}}
\qquad(p\text{ odd})
\tag{14}
```

for all the integral powers specified on their OEIS pages.  Their proposed
modulus is $p^{3r}$, so these four records are classified `partial`, not
`proved-here`.

The distinction is real.  The exact logarithmic ghost coordinates at
degree weight $m^2$ have a cubic Frobenius defect, but the general
occupation-vector transfer retains only two powers.  The unresolved step is
an additional cancellation after setting the marking variables equal to
one; the coefficientwise Gaussian twist already has sharp quadratic
witnesses.

## 6. The remaining route-M targets

This packet does not prove:

1. the nonlinear $p^{4r}$ MacMahon-product tower on A008793;
2. the three symmetric-plane-partition congruences on A049505; or
3. the coefficient-power $p^{3r}$ gain on A229452.

The [A229452 coefficient-root follow-on](A229452CoefficientRootBaseline.md)
now proves the all-$m$ integrality conjecture, gives an exact Lagrange bridge,
and establishes all-prime $p^r$ towers for both source parameter families.
Its cubic gains remain open. Thus A008793 and A049505 are the only route-M records without
either a complete proof or a proved baseline. Their factorial-product
normalizations are not instances of (1). Merely calling these products
modular does not supply the missing powers.

## 7. Provenance and verification

The OEIS pages above are the sources of the named conjectures.  The general
Gauss-congruence background is classical; Theorem 1 is included with proof
because it gives the exact first correction needed here.  No literature
priority claim is made for that lemma or for this packaging.

The exact checker:

1. verifies Theorem 1 on many finite exponent vectors;
2. checks both A008705 congruences for odd primes through $31$;
3. checks all four prime-level records;
4. checks the three complete quadratic towers through two adjacent levels;
5. checks the four partial quadratic baselines; and
6. evaluates every named sequence directly from its displayed product.

Run:

```text
python verification/related/verify_modular_product_prime_packet.py
```
