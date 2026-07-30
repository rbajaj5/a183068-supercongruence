# A cubic tower for a two-parameter coefficient family

**Status:** complete elementary proof candidate; independent review pending

**Source boundary:** the coefficients have the formal shape considered in
L. Felipe Müller's 2021 framing preprint, but the general theorem there has an
[exact counterexample](RationalFramingCounterexample.md). The elementary proof
in Section 4 is therefore the controlling proof. Priority for the
two-parameter theorem is not established.

## 1. The family and theorem

For integers $\alpha,\beta$ and $N\geq1$, define

$$
A_{\alpha,\beta}(N)
=[x^N]\bigl((1+x)^\alpha(1-x)^\beta\bigr)^N.
$$

Generalized binomial coefficients show directly that
$A_{\alpha,\beta}(N)$ is an integer, even when one or both parameters are
negative.

**Theorem.** Let $\alpha,\beta$ be arbitrary integers and let $n,r\geq1$.
Then

$$
A_{\alpha,\beta}(np^r)
\equiv A_{\alpha,\beta}(np^{r-1})
\pmod {p^{3r}}
$$

for every prime $p\geq5$. At the exceptional odd prime $p=3$, the uniform
conclusion is

$$
A_{\alpha,\beta}(n3^r)
\equiv A_{\alpha,\beta}(n3^{r-1})
\pmod {3^{3r-1}}.
$$

No binary assertion is made here. The proof uses division by $2$, and the
period-two input is precisely where the framing theorem treats $p=2$
separately.

## 2. Six OEIS consequences

The following records are instances of the same family.

| Record | $(\alpha,\beta)$ | Coefficient formula |
| --- | ---: | --- |
| [A002003](https://oeis.org/A002003) | $(1,-1)$ | $\lbrack x^N\rbrack ((1+x)/(1-x))^N$, for $N>0$ |
| [A348410](https://oeis.org/A348410) | $(-1,-2)$ | $\lbrack x^N\rbrack ((1-x)(1-x^2))^{-N}$ |
| [A351857](https://oeis.org/A351857) | $(-2,-4)$ | $\lbrack x^N\rbrack ((1-x)(1-x^2))^{-2N}$ |
| [A352373](https://oeis.org/A352373) | $(-1,-3)$ | $\lbrack x^N\rbrack ((1-x)^2(1-x^2))^{-N}$ |
| [A370101](https://oeis.org/A370101) | $(4,-3)$ | $\lbrack x^N\rbrack ((1+x)^4/(1-x)^3)^N$ |
| [A370102](https://oeis.org/A370102) | $(4,-4)$ | $\lbrack x^N\rbrack ((1+x)^4/(1-x)^4)^N$ |

Each page proposes the $p^{3r}$ tower for $p\geq5$; A352373 also states the
full two-parameter conjecture. The theorem therefore proves all six displayed
towers at once, and it proves the general A352373 parameter family.

## 3. The formal framing match and the source gap

Put

$$
\phi(z)=(1+z)^\alpha(1-z)^\beta
$$

and consider the rational series

$$
V(z)=z\frac{d}{dz}\log\phi(z)
=\frac{\alpha z}{1+z}-\frac{\beta z}{1-z}.
$$

Its coefficient sequence is

$$
[z^m]V(z)=\alpha(-1)^{m+1}-\beta,
$$

which has period two. For every odd prime, multiplication of the index by a
power of that prime preserves its parity, so this is locally a rational
2-sequence. If one wants a literal global input to the number-field statement,
one may work over $\mathbb Q(i)$: the only problematic rational prime, $2$, is
then ramified and excluded.

Equation (5.3) of
[Müller, *Wolstenholme Type Congruences and Framing of Rational
2-Functions*](https://arxiv.org/abs/2104.10754) says that the coefficient of
the plus-framing with parameter one is

$$
[z^N]\exp\left(N\int V(z)\right)
=[z^N]\phi(z)^N
=A_{\alpha,\beta}(N).
$$

This is the intended input shape of Müller's Theorem 1.1. However, the
[counterexample note](RationalFramingCounterexample.md) shows that Theorems
1.1 and 1.2 are false as printed for a different rational period-four
2-sequence. The preprint therefore cannot serve as a valid source closure for
the present theorem without a repaired hypothesis and proof. The
self-contained argument below uses the special form of the period-two
coefficients and proves exactly what is needed here.

The same identification may be written in Lagrange form. If
$y=x\phi(y)$, then

$$
\log\frac yx
=\sum_{N\geq1}\frac{A_{\alpha,\beta}(N)}{N}x^N.
$$

That identity explains why coefficient powers, reversion, and framing appear
together on the OEIS pages.

## 4. An elementary proof of the specialization

The argument below isolates the one-variable mechanism hidden inside the
general framing theorem.

### 4.1 The reduced logarithm

Let $p$ be odd and write

$$
U_p(x)=\sum_{\substack{j\geq1\\p\nmid j}}\frac{x^j}{j},
\qquad
V_p(x)=\sum_{\substack{j\geq1\\p\nmid j}}
\frac{(-1)^{j+1}x^j}{j},
$$

and

$$
L_p(x)=\alpha V_p(x)-\beta U_p(x).
$$

Cancellation of the terms whose exponent is divisible by $p$ gives the exact
formal identity

$$
\frac{\phi(x)^p}{\phi(x^p)}=\exp\bigl(pL_p(x)\bigr).
$$

Set $N=np^r$, $M=N/p$, and $G(x)=\phi(x)/x$. Then

$$
A_{\alpha,\beta}(N)-A_{\alpha,\beta}(M)
=[x^0]G(x^p)^M\left(\exp(NL_p(x))-1\right).
$$

The linear term has zero constant coefficient: every exponent of
$G(x^p)^M$ is divisible by $p$, while $L_p$ contains no exponent divisible
by $p$.

### 4.2 The quadratic Cartier estimate

For $T\geq1$, define the reduced harmonic sums

$$
H_T=\sum_{\substack{1\leq j<T\\p\nmid j}}\frac1j,
\qquad
H_T^\pm=\sum_{\substack{1\leq j<T\\p\nmid j}}
\frac{(-1)^{j+1}}j.
$$

If $e=v_p(T)\geq1$, standard reduced-residue pairing gives

$$
v_p(H_T)\geq
\begin{cases}
2e,&p\geq5,\\
2e-1,&p=3.
\end{cases}
$$

When $T$ is even, the alternating sum satisfies the stronger bound
$v_p(H_T^\pm)\geq2e$.

For completeness, partition the summation into blocks of length $p^e$ and
expand

$$
\frac1{ap^e+u}
\equiv\frac1u-\frac{ap^e}{u^2}\pmod {p^{2e}}.
$$

Pairing $u$ with $p^e-u$ reduces the first moment to the sum of inverse
squares of the units modulo $p^e$. Inversion permutes those units. Their
square sum is $0$ modulo $p^e$ for $p\geq5$ and modulo $p^{e-1}$ for
$p=3$. For the alternating sum, pair two consecutive blocks; the leading
inverse-square sums cancel under $u\mapsto p^e-u$.

Direct convolution gives

$$
[x^T]U_p(x)^2=\frac{2H_T}{T},
$$

$$
[x^T]V_p(x)^2=(-1)^T\frac{2H_T}{T},
$$

and

$$
[x^T]U_p(x)V_p(x)
=\frac{1+(-1)^T}{T}H_T^\pm.
$$

Consequently, if $\epsilon_p=0$ for $p\geq5$ and $\epsilon_3=1$, then

$$
v_p\bigl([x^T]L_p(x)^2\bigr)\geq e-\epsilon_p.
$$

Let $C_p$ denote the Cartier operator
$C_p(\sum c_jx^j)=\sum c_{pj}x^j$. The last estimate is equivalent to

$$
C_p(L_p^2)=p^{1-\epsilon_p}xK'(x)
$$

for a series $K$ with $p$-integral coefficients.

### 4.3 Integration by parts supplies the third block of powers

Cartier extraction and formal integration by parts now give

$$
[x^0]G(x^p)^M L_p(x)^2
=p^{1-\epsilon_p}[x^0]G(x)^M xK'(x),
$$

and

$$
[x^0]G(x)^M xK'(x)
=-M[x^0]K(x)G(x)^{M-1}xG'(x).
$$

The right side is divisible by $M$ in the local integer ring. Therefore the
quadratic term in the exponential has valuation at least

$$
v_p\left(\frac{N^2}{2}\,p^{1-\epsilon_p}M\right)
\geq3r-\epsilon_p.
$$

For every exponential term of degree $j\geq3$,

$$
v_p\left(\frac{N^j}{j!}\right)\geq3r-\epsilon_p.
$$

Only finitely many degrees can contribute to the constant coefficient,
because $G(x^p)^M$ has lowest exponent $-N$ and $L_p(x)^j$ has lowest
exponent $j$. Thus the whole difference has valuation at least $3r$ for
$p\geq5$ and at least $3r-1$ for $p=3$, as claimed.

## 5. Verification

Run

```text
python verification/related/verify_coefficient_framing_cubic_tower.py
```

The exact checker performs:

- 30 source-identification checks for the six sequences;
- 50 reduced-harmonic checks;
- 2,940 quadratic Cartier checks;
- 2,430 tower checks across a parameter grid;
- 18 named level-three checks; and
- 5 sharp boundary checks.

All 5,473 checks pass. These computations test transcription and boundaries;
the proof and the published theorem, not the finite grid, establish the
general result.

## 6. What this changes in the 110-record campaign

This single family moves six records from `queued` to `proved-here`.
It also shows that the earlier separation of these records between a
finite-sum route and a coefficient route was artificial: the controlling
object is the period-two logarithmic derivative of the coefficient kernel.
That is exactly the kind of consolidation the campaign is intended to find.
