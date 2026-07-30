# Apéry odd moments at the prime boundary

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

This note resolves the prime conjecture on
[OEIS A357510](https://oeis.org/A357510) and proves an exact
prime-by-prime classification for the odd-moment family recorded on
[OEIS A357512](https://oeis.org/A357512).

For an integer $q\geq1$, define

**(1)** $U_q(n)=\displaystyle\sum_{k=0}^{n}k^q
\binom{n}{k}^{2}\binom{n+k}{k}^{2}$.

The result comes from expanding one Apéry summand at $n=p-1$. No
recurrence or unproved property of the Apéry numbers is needed.

## 1. The local product

Let $p$ be an odd prime and $1\leq k\leq p-1$. Directly from the
factorial products,

**(2)** $\displaystyle
\binom{p-1}{k}\binom{p-1+k}{k}
=(-1)^k\frac pk\left(1-\frac pk\right)
\prod_{j=1}^{k-1}\left(1-\frac{p^2}{j^2}\right).$

All denominators in (2) are $p$-adic units. Squaring and discarding
terms of valuation at least four gives, for every $q\geq1$,

**(3)** $\displaystyle
k^q\binom{p-1}{k}^{2}\binom{p-1+k}{k}^{2}
\equiv p^2k^{q-2}-2p^3k^{q-3}\pmod {p^4}.$

For negative exponents, the powers on the right are interpreted in
$\mathbb Z_{(p)}$. Put

**(4)** $\displaystyle S_j(p)=\sum_{k=1}^{p-1}k^j.$

Summing (3) yields the master congruence

**(5)** $\displaystyle
U_q(p-1)\equiv p^2S_{q-2}(p)-2p^3S_{q-3}(p)\pmod {p^4}.$

## 2. A357510

### Theorem 1

For every prime $p\geq5$,

**(6)** $\displaystyle U_1(p-1)\equiv0\pmod {p^4}.$

This is exactly the conjecture printed on A357510.

### Proof

For $q=1$, equation (5) reads

**(7)** $\displaystyle
U_1(p-1)\equiv
p^2\sum_{k=1}^{p-1}\frac1k
-2p^3\sum_{k=1}^{p-1}\frac1{k^2}
\pmod {p^4}.$

Wolstenholme's congruence makes the first reciprocal sum zero modulo
$p^2$. The second is zero modulo $p$, since inversion permutes
$\mathbb F_p^\times$ and the sum of the squares in that field is zero.
Both terms in (7) therefore vanish modulo $p^4$. $\square$

The prime $3$ is a sharp boundary:
$U_1(2)=108$ has $3$-adic valuation $3$, not $4$.

## 3. Exact classification of every higher odd moment

Let $m\geq2$, and set

**(8)** $q=2m+1,\quad a=2m-1,\quad b=2m-2.$

Define $\delta_{p,m}$ to be $1$ if $p-1\mid 2m-2$, and $0$
otherwise.

### Theorem 2

For every odd prime $p$ and every integer $m\geq2$,

**(9)** $\displaystyle
\frac{U_{2m+1}(p-1)}{p^3}
\equiv
\delta_{p,m}\frac{5-2m}{2}
\pmod p.$

In particular,

**(10)** $\displaystyle
U_{2m+1}(p-1)\equiv0\pmod {p^4}$

if and only if

**(11)** $\displaystyle
p-1\nmid 2m-2
\quad\text{or}\quad
p\mid 2m-5.$

If neither condition in (11) holds, the valuation is exactly $3$.

### Proof

Pair $k$ with $p-k$. Since $a$ is odd,

**(12)** $\displaystyle
S_a(p)
\equiv
ap\sum_{k=1}^{(p-1)/2}k^b
\pmod {p^2}.$

The exponent $b$ is even. Therefore the full finite-field power sum is
twice its half sum, and

**(13)** $\displaystyle
\sum_{k=1}^{(p-1)/2}k^b
\equiv-\frac{\delta_{p,m}}2\pmod p,\qquad
S_b(p)\equiv-\delta_{p,m}\pmod p.$

Substitute (12)--(13) into (5):

**(14)** $\displaystyle
U_{2m+1}(p-1)
\equiv
p^3\delta_{p,m}
\left(-\frac a2+2\right)
=p^3\delta_{p,m}\frac{5-2m}{2}
\pmod {p^4}.$

This is (9). Since $2$ is invertible modulo every odd prime, (10)--(11)
follow immediately. $\square$

## 4. Consequences for A357512

The sequence A357512 is $U_5(n)$, the case $m=2$. For every prime
$p\geq5$, one has $p-1\nmid2$, so Theorem 2 proves

**(15)** $\displaystyle U_5(p-1)\equiv0\pmod {p^4}.$

Thus the prime slice of the displayed A357512 conjecture is complete.
The stronger claim for every composite $n\equiv1,5\pmod6$ remains open.

Theorem 2 also determines the *minimal* exceptional-prime set for every
odd moment at the prime boundary:

**(16)** $\displaystyle
E(m)=
\left\{p\ \text{odd prime}:
p-1\mid2m-2\ \text{and}\ p\nmid2m-5
\right\}.$

For the parameters listed on A357512, the exact sets are:

| $m$ | exponent $2m+1$ | exact $E(m)$ |
| ---: | ---: | --- |
| 2 | 5 | $\{3\}$ |
| 3 | 7 | $\{3,5\}$ |
| 4 | 9 | $\{7\}$ |
| 5 | 11 | $\{3\}$ |
| 6 | 13 | $\{3,11\}$ |
| 7 | 15 | $\{5,7,13\}$ |
| 8 | 17 | $\{3\}$ |
| 9 | 19 | $\{3,5,17\}$ |
| 10 | 21 | $\{7,19\}$ |

Some sets printed on the OEIS record were deliberately or accidentally
nonminimal. More importantly, its proposed set $P(9)=\{3\}$ misses two
prime failures. The smallest is the exact counterexample

**(17)** $\displaystyle U_{19}(4)\equiv5^3\not\equiv0\pmod {5^4}.$

This does not affect the present A357512 case $m=2$.

## 5. Source and literature boundary

- A357510 states (6) for primes $p\geq5$.
- A357512 states the $m=2$ composite conjecture and proposes finite
  exceptional-prime sets for the family $m\geq2$.
- A July 2026 preprint by Chen, Wang, and Feng studies a reciprocal-power
  Apéry numerator family associated with A357513. Its local expansion is
  related in spirit, but it is a different sequence from the positive
  moments in (1).

Targeted searches by both OEIS identifiers and by the exact odd-moment
formula did not locate Theorems 1--2 in a publication. This is preliminary
routing evidence, not a priority certificate.

## 6. Verification

Run:

```text
python verification/related/verify_apery_odd_moment_prime_classification.py
```

The checker verifies the exact product identity, the local congruence (3),
the master congruence (5), Theorem 1, the residue formula (9), every exact
exceptional set in the table, and the counterexample (17).
