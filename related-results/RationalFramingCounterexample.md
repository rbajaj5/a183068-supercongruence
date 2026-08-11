# An exact counterexample to the rational-framing theorem as printed

**Status:** complete elementary counterexample; specialist review and source
author notification remain appropriate

**Source:** L. Felipe Müller,
[*Wolstenholme Type Congruences and Framing of Rational
2-Functions*](https://arxiv.org/abs/2104.10754), especially Theorems 1.1 and
1.2.

This note concerns the statements as printed in the April 2021 arXiv
version. It is not a claim about the author's intentions or about a possible
corrected theorem.

## 1. A rational 2-sequence

Define

$$
V(z)=\frac{z}{1-z}+\frac{16z^4}{1-z^4}
=\sum_{n\geq1}a_nz^n.
$$

Then

$$
a_n=
\begin{cases}
17,&4\mid n,\\
1,&4\nmid n.
\end{cases}
$$

The sequence $(a_n)$ is a 2-sequence over $\mathbb Q$.

For every odd prime $p$, divisibility by four is unchanged under
$n\mapsto pn$, so $a_{mp^r}=a_{mp^{r-1}}$ exactly. At $p=2$:

- if $r=1$, the difference is either $0$ or $16$, hence is divisible by
  $2^2$;
- if $r=2$, the only nonzero difference is $17-1=16$, divisible by $2^4$;
  and
- if $r\geq3$, both indices are divisible by four and the difference is
  zero.

Thus

$$
a_{mp^r}\equiv a_{mp^{r-1}}\pmod {p^{2r}}
$$

for every prime $p$ and all $m,r\geq1$. The generating function $V$ is
rational and has period four, so it meets the stated input conditions of
Theorem 1.1.

## 2. Theorem 1.2 already fails

Theorem 1.2 asserts, for a periodic sequence of period $N$, a lower bound on

$$
\sum_{k=1,\;p\nmid k}^{n-1}\frac{a_{n-k}a_k}{k^2}.
$$

Take $N=4$, $p=n=5$. Since $5\nmid4$, the asserted exponent is one. But

$$
\sum_{k=1}^{4}\frac{a_{5-k}a_k}{k^2}
=17+\frac14+\frac19+\frac{17}{16}
=\frac{2653}{144}
\equiv2\pmod5.
$$

The claimed divisibility by $5$ therefore fails.

The reindexing step in the printed proof appears to lose track of wraparound.
Multiplication by the chosen unit permutes residues modulo $p^r$, but reducing
the product back to the standard interval adds a multiple of $p^r$. That
multiple need not vanish modulo the period $N$. Here $p^r=5$ is nonzero
modulo four, so the periodic weights are not preserved by the asserted
permutation.

## 3. The precise claim in Theorem 1.1 also fails

Formal integration gives

$$
\int V(z)
=-\log(1-z)-4\log(1-z^4).
$$

For framing parameter one, equation (5.3) of the paper therefore gives

$$
A(n)
=\lbrack x^n\rbrack\exp\left(n\int V(x)\right)
=\lbrack x^n\rbrack(1-x)^{-n}(1-x^4)^{-4n}.
$$

The coefficient has the finite formula

$$
A(n)=
\sum_{j=0}^{\lfloor n/4\rfloor}
\binom{4n+j-1}{j}
\binom{2n-4j-1}{n-4j}.
$$

In particular,

$$
A(1)=1,\qquad A(5)=226,
$$

so

$$
A(5)-A(1)=225=3^2\cdot5^2.
$$

The precise clause of Theorem 1.1 predicts divisibility by $5^3$, because
$5$ is unramified over $\mathbb Q$ and does not divide the period four.
The valuation is instead exactly two.

## 4. Consequence for this repository

The [two-parameter coefficient theorem](CoefficientFramingCubicTower.md)
remains valid: its elementary proof uses the special two-letter logarithm
coming from $(1+x)^\alpha(1-x)^\beta$, and 5,761 exact checks cover its
stated boundaries. What changes is provenance. The six OEIS records proved
there cannot be marked `published-source` on the strength of the 2021
framing theorem as printed. They are classified `proved-here` until a valid
published source or corrected theorem is identified.

This counterexample also warns against applying the framing theorem
automatically to the remaining coefficient-power queue. Periodicity of the
logarithmic derivative is not, by itself, enough for the cubic tower.

## 5. Verification

Run

```text
python verification/related/verify_rational_framing_counterexample.py
```

The checker verifies the 2-sequence law on 3,600 finite cases, the exact
weighted-harmonic failure, the exact framed coefficient failure, and an
independent coefficient expansion. All 3,620 checks pass.
