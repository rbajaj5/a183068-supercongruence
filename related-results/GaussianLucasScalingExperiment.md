# Adjacent-scale Gaussian Lucas experiment

## Status

**Exact computational evidence.** A subsequent
[prime-power proof candidate](GaussianLucasPrimePowerTheorem.md) now explains
the observed exponents; that argument still requires independent review and
a priority search.

This experiment asks whether the inert-prime Gaussian Lucas congruence has a
Dwork-style strengthening across adjacent prime-power scales.

For Kalinin's rectangular Gaussian coefficient $Q(A,B;C,D)$, define

```math
\Delta_{p,r}(A,B;C,D)
=
Q(p^rA,p^rB;p^rC,p^rD)
-
Q(p^{r-1}A,p^{r-1}B;p^{r-1}C,p^{r-1}D).
```

The current proof candidate establishes only the $r=1$ lower bound
$v_p(\Delta_{p,1})\ge3$ for inert primes $p>5$.

## Experimental finding

Every tested nontrivial rectangle supports the stronger conjecture

```math
v_p\bigl(\Delta_{p,r}(A,B;C,D)\bigr)\ge3r
\qquad
(p>5,\ p\equiv3\pmod4).
```

The bound was usually attained exactly.

The principal exact grids were:

| Prime and scale | Rectangles | Observed valuations |
| --- | ---: | --- |
| $p=7$, $r=1,2,3$ | 27 at each scale | exactly $3r$ in all 81 cases |
| $p=11$, $r=1,2$ | 27 at each scale | exactly $3r$ in all 54 cases |
| $p=19$, $r=1,2$ | 27 at each scale | exactly $3r$ in all 54 cases |
| $p=7,11$, $r=2$ | 84 larger rectangles per prime | exactly $6$ in all 168 cases |
| $p=23,31,43$, $r=1$ | 27 per prime | exactly $3$ in all 81 cases |

Additional deeper witnesses gave

```math
v_7(\Delta_{7,4}(1,2;1,1))=12,\qquad
v_{11}(\Delta_{11,3}(1,2;1,1))=9,
```

and the expensive calibration

```math
v_{19}(\Delta_{19,3}(1,2;1,1))=9.
```

Literal Gaussian-integer products independently reproduced selected modular
valuations at $r=1$ and $r=2$.

## The exceptional prime 3

On the full 27-rectangle grid, the minimum was instead $3r-1$:

| Scale | Valuation distribution |
| --- | --- |
| $r=1$ | $2$ in 17 cases, $3$ in 6, $4$ in 4 |
| $r=2$ | $5$ in 17 cases, $6$ in 6, $7$ in 4 |
| $r=3$ | $8$ in 17 cases, $9$ in 6, $10$ in 4 |

This recovers the known boundary
$v_3(\Delta_{3,1}(1,2;1,1))=2$ and suggests a separate sharp
$3^{3r-1}$ statement.

## Split primes

The naive split-prime analogue fails immediately. For
$p=5,13,17,29$, the two valuations $v_\pi(\Delta_{p,1})$ and
$v_{\bar\pi}(\Delta_{p,1})$ were tested separately over the same
27-rectangle grid. Many values were zero or negative, because these
rectangular coefficients need not be integral at either prime above $p$.

Any useful split-prime theorem therefore needs an integrality hypothesis,
normalization, or a different formulation. Merely replacing $p$ by
$\pi$ in the inert congruence is false.

## Reproduction

The default experiment takes several seconds:

```text
python verification/related/experiment_gaussian_lucas_scaling.py
```

The deep calibration includes the roughly two-minute $p=19,r=3$ case:

```text
python verification/related/experiment_gaussian_lucas_scaling.py --deep
```

The script uses exact modular Gaussian arithmetic for inert primes and two
separate Hensel embeddings of $\mathbb Q(i)$ into $\mathbb Q_p$ for split
primes. It does not use floating-point complex arithmetic or Gaussian
$q$-binomials.

## Next mathematical task

The companion proof candidate replaces the fixed block by the complete unit
block modulo $p^r$. Its two reciprocal-sum estimates produce the
scale-sensitive translation bound. The remaining task is independent review,
not further blind computation.
