# Walsh-chaos congruences for planar noise observables

## 1. Result and boundary

Critical planar percolation and the Brownian web are two-dimensional black
noises. Their finite approximations are functions of many independent bits,
so their sensitivity can be studied through the Walsh--Fourier levels of
those functions.

There is an exact arithmetic statement at this finite level:

> If an observable changes sign when every input bit is flipped, its Walsh
> noise-stability polynomial has only odd degrees. Removing the linear
> scaling contribution forces an adjacent-scale congruence of order
> $3r-2$.

The statement works over every discrete valuation ring. In particular, it
can be evaluated at every Gaussian prime, including the ramified prime
$1+i$.

This is a finite Walsh-chaos congruence. It does **not** prove that a scaling
limit is black, and it does not turn the Brownian web or Schramm--Loewner
evolution into an arithmetic object. Blackness concerns the decay of
normalized Fourier mass in a real or complex Hilbert norm. The theorem below
concerns divisibility in a nonarchimedean valuation. Neither conclusion
implies the other without an additional comparison theorem.

## 2. A lacunary-polynomial theorem

Let $R$ be a discrete valuation ring with uniformizer $\varpi$ and
valuation $v_\varpi$. Let

$$
  P(T)=\sum_{j\geq 0} A_jT^j
  \qquad(A_j\in R).
$$

### Theorem 1 -- spectral-lacunarity lift

Suppose that every nonzero coefficient of $P$ has degree

$$
  j\equiv d\pmod h,
  \qquad j\geq d,
$$

where $d\geq0$ and $h\geq1$. Then, for every $r\geq1$,

$$
  P(\varpi^r)
  \equiv
  \varpi^dP(\varpi^{r-1})
  \pmod{\varpi^{(d+h)r-h}}.
  \tag{1}
$$

#### Proof

The degree-$d$ term cancels. For every remaining supported degree
$j\geq d+h$,

$$
\begin{aligned}
  \varpi^{rj}-\varpi^d\varpi^{(r-1)j}
  &=
  \varpi^{d+(r-1)j}
  \bigl(\varpi^{j-d}-1\bigr).
\end{aligned}
\tag{2}
$$

The last factor is a unit. Therefore the valuation of the $j$-term is at
least

$$
  d+(r-1)j
  \geq
  d+(r-1)(d+h)
  {}=
  (d+h)r-h.
$$

Summing proves (1). $\square$

The estimate also identifies the first surviving spectral level. Suppose
$j_{\ast}>d$ is the least supported degree and that, for every supported
$j>j_{\ast}$,

$$
  v_\varpi(A_j)+(r-1)j
  {}>
  v_\varpi(A_{j_{\ast}})+(r-1)j_{\ast}.
  \tag{3}
$$

Then the $j_{\ast}$-term is uniquely minimal, and hence

$$
  v_\varpi\!\left(
    P(\varpi^r)-\varpi^dP(\varpi^{r-1})
  \right)
  {}=
  v_\varpi(A_{j_{\ast}})+d+(r-1)j_{\ast}.
  \tag{4}
$$

Because $P$ has finite degree, condition (3) holds for all sufficiently
large $r$. Thus the eventual slope of the valuation is exactly the first
spectral degree left after the degree-$d$ subtraction.

## 3. Walsh noise-stability polynomials

Let

$$
  g:\lbrace-1,1\rbrace^m\longrightarrow\mathbb Z[i].
$$

For $S\subseteq[m]$, put

$$
  \chi_S(x)=\prod_{j\in S}x_j,
  \qquad
  H_g(S)=\sum_{x\in\lbrace-1,1\rbrace^m}g(x)\chi_S(x).
$$

Define the integral spectral masses

$$
  W_j(g)=
  \sum_{\lvert S\rvert=j}
  H_g(S)\overline{H_g(S)}
  \in\mathbb Z_{\geq0}
$$

and the unnormalized noise-stability polynomial

$$
  \mathcal N_g(T)=\sum_{j=0}^m W_j(g)T^j.
  \tag{5}
$$

If $X,Y$ are uniform correlated Boolean strings with
$\mathbb E[X_kY_k]=\rho$, then the usual Walsh calculation gives

$$
  \mathbb E\!\left[g(X)\overline{g(Y)}\right]
  {}=
  2^{-2m}\mathcal N_g(\rho).
  \tag{6}
$$

Thus (5) is the ordinary noise-stability polynomial with its dyadic
denominators cleared.

### Lemma 2 -- color reversal removes every even chaos

If

$$
  g(-x)=-g(x)
  \qquad\text{for all }x,
  \tag{7}
$$

then

$$
  H_g(S)=0
  \qquad\text{whenever }\lvert S\rvert\text{ is even}.
  \tag{8}
$$

#### Proof

Changing variables from $x$ to $-x$ gives

$$
\begin{aligned}
  H_g(S)
  &=
  \sum_x g(-x)\chi_S(-x) \\
  &=
  (-1)^{\lvert S\rvert+1}H_g(S).
\end{aligned}
$$

For even $\lvert S\rvert$, torsion-freeness gives (8). $\square$

### Corollary 3 -- the first-chaos filter

Under (7), for every Gaussian prime $\varpi$ and every $r\geq1$,

$$
  \mathcal N_g(\varpi^r)
  \equiv
  \varpi\,\mathcal N_g(\varpi^{r-1})
  \pmod{\varpi^{3r-2}}.
  \tag{9}
$$

Indeed, Lemma 2 puts the spectral support in the class
$1\pmod2$, so Theorem 1 applies with $d=1$ and $h=2$.

The subtraction in (9) cancels the first Walsh chaos exactly. The cubic
chaos is the first level that can remain. More precisely, for $r\geq2$,

$$
  \frac{
    \mathcal N_g(\varpi^r)
    {}-
    \varpi\mathcal N_g(\varpi^{r-1})
  }{\varpi^{3r-2}}
  \equiv
  {}-W_3(g)
  \pmod{\varpi}
  \tag{10}
$$

This holds without an extra hypothesis. Indeed, after division by
$\varpi^{3r-2}$, every degree above $3$ acquires the positive factor
$\varpi^{(r-1)(j-3)}$. In particular, if $W_3(g)$ is a
$\varpi$-adic unit, the valuation in (9) is exactly $3r-2$. When
$W_3(g)$ is divisible by $\varpi$, formula (4) determines the eventual
valuation from the first surviving level and its coefficient.

There are two useful dyadic forms:

$$
  \mathcal N_g(2^r)
  \equiv
  2\mathcal N_g(2^{r-1})
  \pmod{2^{3r-2}},
  \tag{11}
$$

and

$$
  \mathcal N_g((1+i)^r)
  \equiv
  (1+i)\mathcal N_g((1+i)^{r-1})
  \pmod{(1+i)^{3r-2}}.
  \tag{12}
$$

Equation (11) is a rational $2$-adic statement. Equation (12) is a
ramified Gaussian statement. They evaluate the same polynomial at different
arguments and should not be conflated.

## 4. Hex/Y renormalization

The classical topology of Hex supplies a particularly clean finite
observable. It is important to use the symmetry correctly. On a standard
Hex board the two colors are assigned different pairs of sides, so bare
color complementation does not negate the horizontal winner observable.
The equivalent triangular game of Y has the required symmetry without a
rotation.

For $n\geq1$, put

$$
  \Delta_n=
  \left\lbrace
    (a,b,c)\in\mathbb Z_{\geq0}^3:
    a+b+c=n-1
  \right\rbrace.
  \tag{13}
$$

Two cells are adjacent when their difference is a permutation of
$(1,-1,0)$. The three sides are $a=0$, $b=0$, and $c=0$. A monochromatic
component is a Y when it meets all three sides.

Color the cells by a vector
$x\in\lbrace-1,1\rbrace^{\Delta_n}$. Define
$Y_n(x)=1$ when the $1$-colored cells contain a Y and $Y_n(x)=-1$ when the
$(-1)$-colored cells contain a Y.

For $n\geq2$, define the majority reduction

$$
\begin{aligned}
  (R_nx)_{a,b,c}
  &=
  \mathrm{maj}\left(
    x_{a+1,b,c},
    x_{a,b+1,c},
    x_{a,b,c+1}
  \right),
  \qquad
  (a,b,c)\in\Delta_{n-1}.
\end{aligned}
  \tag{14}
$$

There is no tie because each local block has three cells.

### Theorem 4 -- exact Y renormalization

Every coloring of $\Delta_n$ contains a Y of exactly one color, and

$$
  Y_n(x)=Y_{n-1}(R_nx).
  \tag{15}
$$

Consequently,

$$
  Y_n(-x)=-Y_n(x).
  \tag{16}
$$

#### Proof

The reduction preserves a Y of either fixed color. In one direction,
push each monochromatic path through the chain of three-cell blocks that
it crosses; their majority-colored tips form the corresponding path on
the smaller board. Conversely, a path on the smaller board gives a chain
of overlapping majority-colored triples. If the common cell of two
successive triples has the required color, use it. If not, the other four
cells contain a monochromatic connection between the two triples. These
local connections lift each of the three arms of a Y.

Thus a color has a Y before reduction if and only if it has one after
reduction. Iterating reaches $\Delta_1$, where its unique cell gives a Y
of exactly one color. This proves existence, uniqueness, and (15).
Finally $R_n(-x)=-R_n(x)$; induction from $Y_1(-x)=-Y_1(x)$ proves
(16). $\square$

### Corollary 5 -- Y-game Walsh congruence

For every $n\geq1$, Gaussian prime $\varpi$, and $r\geq1$,

$$
  \mathcal N_{Y_n}(\varpi^r)
  \equiv
  \varpi\,\mathcal N_{Y_n}(\varpi^{r-1})
  \pmod{\varpi^{3r-2}}.
  \tag{17}
$$

For $r\geq2$, its normalized leading residue is

$$
  \frac{
    \mathcal N_{Y_n}(\varpi^r)
    -
    \varpi\mathcal N_{Y_n}(\varpi^{r-1})
  }{\varpi^{3r-2}}
  \equiv
  -W_3(Y_n)
  \pmod{\varpi}.
  \tag{18}
$$

This is Corollary 3 applied to (16). The topological theorem makes
$Y_n$ a total $\lbrace-1,1\rbrace$-valued observable, while (15) gives an exact
finite-scale renormalization certificate. Because the majority triples
overlap, (15) does not by itself give a scalar recurrence for
$\mathcal N_{Y_n}$, and no stronger valuation is inferred from it.

Exact enumeration gives:

| side length | nonzero spectral masses |
| --- | --- |
| 1 | `W1=4` |
| 2 | `W1=48, W3=16` |
| 3 | `W1=2496, W3=1408, W5=192` |
| 4 | `W1=549568, W3=377600, W5=107136, W7=14080, W9=192` |
| 5 | `W1=501212928, W3=377104896, W5=151252224, W7=38476800, W9=5370112, W11=317952, W13=6912` |
| 6 | `W1=1869439264128, W3=1473803873408, W5=722690237952, W7=256856418816, W9=63332709632, W11=10667093760, W13=1171385856, W15=82137600, W17=3330432, W19=59520` |

The exact side-six spectrum gives

$$
  \frac{W_1(Y_6)}{2^{42}}
  =0.4250612765\ldots,
  \qquad
  \frac{\mathcal N_{Y_6}(1/2)}{2^{42}}
  =0.2600392981\ldots.
  \tag{19}
$$

A seeded Monte Carlo experiment evaluates the exact renormalization circuit
on 200,000 colorings at each larger side length. Parentheses below contain
two estimated standard errors:

| side length | cells | normalized first chaos | stability at correlation 1/2 |
| --- | ---: | ---: | ---: |
| 8 | 36 | `0.364095 (0.004783)` | `0.225620 (0.004269)` |
| 10 | 55 | `0.324826 (0.004086)` | `0.203060 (0.003386)` |
| 12 | 78 | `0.301345 (0.004328)` | `0.185910 (0.004377)` |
| 16 | 136 | `0.262262 (0.004976)` | `0.165860 (0.004480)` |
| 20 | 210 | `0.232544 (0.003155)` | `0.151380 (0.004665)` |

The observed decrease is consistent with low-level Fourier mass moving to
higher chaos as the board grows. Five Monte Carlo points do not prove
noise sensitivity or blackness, and they supply no additional
$\varpi$-adic divisibility.

The standard game of Hex is recovered from Y by fixing appropriate
boundary cells. That reduction proves the usual existence and uniqueness
of the Hex winner. The arithmetic corollary above is stated for the
unconditioned Y cube because that is where global color complementation is
an endomorphism of the sample space.

## 5. Finite planar percolation

Let $f_H(x)$ be the indicator that the open sites in a finite triangular
lattice patch contain a left-to-right crossing. Define the signed
color-reversal contrast

$$
  g_H(x)=f_H(x)-f_H(-x).
  \tag{20}
$$

Then $g_H(-x)=-g_H(x)$, so (9)--(12) apply. A vertical or rotated crossing
contrast $g_V$ may be included in one Gaussian-valued observable

$$
  g(x)=g_H(x)+i\,g_V(x).
  \tag{21}
$$

This is the clean role for Gaussian integers: they package two planar
channels while their prime ideals provide split, inert, and ramified
valuations.

For the real observable (20), exact enumeration gives:

| triangular patch | nonzero $W_j(g_H)$ |
| --- | --- |
| $2\times2$ | $W_1=160,\ W_3=32$ |
| $3\times2$ | $W_1=1816,\ W_3=592,\ W_5=24$ |
| $3\times3$ | $W_1=124240,\ W_3=51584,\ W_5=5920,\ W_7=512,\ W_9=16$ |
| $4\times2$ | $W_1=17312,\ W_3=8672,\ W_5=1120,\ W_7=32$ |

Every even level vanishes exactly, and every listed polynomial satisfies
(9) at $1+i$, $2+i$, and the inert Gaussian prime $3$.

## 6. Brownian-web discretizations

The Brownian web is the scaling limit of systems of coalescing random walks.
In a finite space-time cylinder, an arrow field can be encoded by Boolean
variables: each arrow chooses the left or right successor. Any finite
observable $F$ of this arrow field has a Walsh expansion.

Its antisymmetrization

$$
  g(x)=F(x)-F(-x)
  \tag{22}
$$

is complement-odd and therefore satisfies Corollary 3. Identifying a
space-time site $(u,t)$ with $u+it$ supplies a convenient Gaussian
coordinate system, and a pair of real observables can again be combined as
in (21).

This gives an exact congruence for every finite arrow-field approximation.
It does not survive passage to the Brownian web automatically. A scaling
limit requires tightness and control of normalized spectral measures, while
(9) is an identity after substituting a prime-adic argument into a finite
polynomial.

## 7. What blackness contributes

The finite spectral sample assigns mass proportional to
$\lvert\widehat g(S)\rvert^2$ to subsets $S$ of input bits. Noise
sensitivity and blackness concern the movement of that mass away from every
fixed finite chaos as the mesh tends to zero.

The arithmetic operation

$$
  \mathcal N_g(\varpi^r)
  {}-
  \varpi\mathcal N_g(\varpi^{r-1})
  \tag{23}
$$

has a parallel but different effect: it deletes the first chaos exactly and
orders the surviving levels by their $\varpi$-adic slopes. Consequently:

- the spectral theory identifies which chaos levels matter;
- the congruence turns gaps between those levels into valuation gains;
- blackness supplies no valuation bound by itself; and
- valuation growth supplies no proof of blackness by itself.

The missing theorem for a deeper bridge would compare real decay of
normalized low-level spectral mass with prime-adic divisibility of a
canonically normalized integral model. No such comparison is asserted here.

## 8. Verification

Run:

```text
python verification/related/verify_black_noise_chaos_filter.py
```

The exhaustive $2^{21}$-coloring side-six transform is opt-in:

```text
python verification/related/verify_black_noise_chaos_filter.py --extended
```

The seeded larger-board simulation is:

```text
python verification/related/verify_black_noise_chaos_filter.py --scaling
```

The checker performs:

- 1,800 exact lacunary-polynomial tests over
  $\mathbb Z[i]$;
- 1,944 exact tests of random complement-odd Gaussian-valued observables,
  including the normalized cubic residue (10); and
- exact Y-game uniqueness, majority-renormalization, Walsh-spectrum,
  congruence, and cubic-residue checks through side length $5$ by default,
  with the complete side-six spectrum in the extended run; and
- 146 exact triangular-crossing regression, congruence, and cubic-residue
  checks.

All 88,741 checks pass without floating-point arithmetic.

## 9. Literature and priority boundary

The Hex/Y crossing theorem and its majority reduction are presented in:

- Anna R. Karlin and Yuval Peres,
  [*Game Theory, Alive*](https://bookstore.ams.org/MBK/101),
  Sections 1.2.2--1.2.3, American Mathematical Society, 2017.

Schramm and Smirnov proved that any scaling limit in their class of critical
planar percolation models is a black noise:

- Oded Schramm and Stanislav Smirnov,
  [*On the scaling limits of planar percolation*](https://arxiv.org/abs/1101.5820).

Ellis and Feldheim proved the corresponding two-dimensional black-noise
statement for the Brownian web:

- Tom Ellis and Ohad Noy Feldheim,
  [*The Brownian web is a two-dimensional black noise*](https://arxiv.org/abs/1203.3585).

The detailed finite Fourier-spectrum input for critical percolation belongs
to:

- Christophe Garban, Gábor Pete, and Oded Schramm,
  [*The Fourier spectrum of critical percolation*](https://arxiv.org/abs/0803.3750);
- Oded Schramm and Jeffrey Steif,
  [*Quantitative noise sensitivity and exceptional times for percolation*](https://arxiv.org/abs/math/0504586).

Noise-stability polynomials also occur as mixture polynomials in random CSP
and spin-glass theory:

- Chris Jones, Kunal Marwaha, Juspreet Singh Sandhu, and Jonathan Shi,
  [*Random Max-CSPs Inherit Algorithmic Hardness from Spin Glasses*](https://doi.org/10.4230/LIPIcs.ITCS.2023.77).

The Hex/Y crossing and majority-reduction facts are classical; this note
claims no priority for them. The lacunary-polynomial proof is elementary.
The searches conducted for this note found no source stating the particular
adjacent-scale congruence (1), its Walsh specialization (9), or the Y-game
specialization (17), but this is not a priority certificate. The arithmetic
theorem should presently be treated as a proved structural observation with
provisional novelty and conventional review still required.
