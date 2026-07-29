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
  g:\{-1,1\}^m\longrightarrow\mathbb Z[i].
$$

For $S\subseteq[m]$, put

$$
  \chi_S(x)=\prod_{j\in S}x_j,
  \qquad
  H_g(S)=\sum_{x\in\{-1,1\}^m}g(x)\chi_S(x).
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

## 4. Finite planar percolation

Let $f_H(x)$ be the indicator that the open sites in a finite triangular
lattice patch contain a left-to-right crossing. Define the signed
color-reversal contrast

$$
  g_H(x)=f_H(x)-f_H(-x).
  \tag{13}
$$

Then $g_H(-x)=-g_H(x)$, so (9)--(12) apply. A vertical or rotated crossing
contrast $g_V$ may be included in one Gaussian-valued observable

$$
  g(x)=g_H(x)+i\,g_V(x).
  \tag{14}
$$

This is the clean role for Gaussian integers: they package two planar
channels while their prime ideals provide split, inert, and ramified
valuations.

For the real observable (13), exact enumeration gives:

| triangular patch | nonzero $W_j(g_H)$ |
| --- | --- |
| $2\times2$ | $W_1=160,\ W_3=32$ |
| $3\times2$ | $W_1=1816,\ W_3=592,\ W_5=24$ |
| $3\times3$ | $W_1=124240,\ W_3=51584,\ W_5=5920,\ W_7=512,\ W_9=16$ |
| $4\times2$ | $W_1=17312,\ W_3=8672,\ W_5=1120,\ W_7=32$ |

Every even level vanishes exactly, and every listed polynomial satisfies
(9) at $1+i$, $2+i$, and the inert Gaussian prime $3$.

## 5. Brownian-web discretizations

The Brownian web is the scaling limit of systems of coalescing random walks.
In a finite space-time cylinder, an arrow field can be encoded by Boolean
variables: each arrow chooses the left or right successor. Any finite
observable $F$ of this arrow field has a Walsh expansion.

Its antisymmetrization

$$
  g(x)=F(x)-F(-x)
  \tag{15}
$$

is complement-odd and therefore satisfies Corollary 3. Identifying a
space-time site $(u,t)$ with $u+it$ supplies a convenient Gaussian
coordinate system, and a pair of real observables can again be combined as
in (14).

This gives an exact congruence for every finite arrow-field approximation.
It does not survive passage to the Brownian web automatically. A scaling
limit requires tightness and control of normalized spectral measures, while
(9) is an identity after substituting a prime-adic argument into a finite
polynomial.

## 6. What blackness contributes

The finite spectral sample assigns mass proportional to
$\lvert\widehat g(S)\rvert^2$ to subsets $S$ of input bits. Noise
sensitivity and blackness concern the movement of that mass away from every
fixed finite chaos as the mesh tends to zero.

The arithmetic operation

$$
  \mathcal N_g(\varpi^r)
  {}-
  \varpi\mathcal N_g(\varpi^{r-1})
  \tag{16}
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

## 7. Verification

Run:

```text
python verification/related/verify_black_noise_chaos_filter.py
```

The checker performs:

- 1,800 exact lacunary-polynomial tests over
  $\mathbb Z[i]$;
- 1,944 exact tests of random complement-odd Gaussian-valued observables,
  including the normalized cubic residue (10); and
- 146 exact triangular-crossing regression, congruence, and cubic-residue
  checks.

All 3,890 checks pass without floating-point arithmetic.

## 8. Literature and priority boundary

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

The lacunary-polynomial proof is elementary. The searches conducted for this
note found no source stating the particular adjacent-scale congruence
(1) or its Walsh specialization (9), but this is not a priority certificate.
The theorem should presently be treated as a proved structural observation
with provisional novelty and conventional review still required.
