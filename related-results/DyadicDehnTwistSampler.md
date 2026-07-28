# Exact sampling and mixing on the dyadic Dehn-twist shadow

## Status

This note is an algorithmic corollary of the affine quotient in
[Exact dyadic orientation lifts](GQ2OrientationLifts.md). The binary
parametrization and its interpretation through the Dehn-twist coordinate are
specific to that quotient. Perfect sampling by independent lift bits and the
coordinate-refresh spectrum are classical finite-probability arguments.

No literature-novelty claim is made. In particular, Ayyer--Steinberg give a
general representation-theoretic spectrum theory for random affine maps on
finite rings and modules. The point here is narrower: the Roe--Turturean
affine shadow admits an optimal exact sampler whose translation bits are
literally dyadic Dehn-twist parameters.

## 1. The finite affine shadow

For $m\geq3$, put

$$
R_m=\mathbb Z/2^m\mathbb Z,
\qquad
G_m=R_m\rtimes R_m^\times,
$$

with matrices

$$
M(u,b)=
\begin{pmatrix}
u&b\\
0&1
\end{pmatrix}.
$$

The translation $M(1,b)$ is the image of the pro-$2$ Dehn twist
$\mathcal T_b$. The standard decomposition

$$
R_m^\times
=
\langle-1\rangle\times\langle5\rangle
\cong
C_2\times C_{2^{m-2}}
$$

gives a unique expression

$$
u=(-1)^\sigma5^a,
\qquad
\sigma\in\{0,1\},
\quad
a\in\mathbb Z/2^{m-2}\mathbb Z.
$$

Writing $a$ and $b$ in binary identifies $G_m$ with a Boolean cube of
dimension

$$
N_m=1+(m-2)+m=2m-1.
$$

This is a bijection of sets, not a claim that the nonabelian group law becomes
coordinatewise addition.

## 2. An information-theoretically optimal exact sampler

### Theorem 1

A fixed-length exact sampler for the uniform distribution on $G_m$ requires
and is achieved by exactly $2m-1$ independent unbiased bits.

More compatibly, reduction

$$
\rho_m:G_{m+1}\longrightarrow G_m
$$

has four-element fibers. If $M((-1)^\sigma5^a,b)$ is uniform on $G_m$ and
$\epsilon,\delta$ are independent unbiased bits, then

$$
\widetilde a=a+\epsilon2^{m-2},
\qquad
\widetilde b=b+\delta2^m
$$

defines a uniform lift

$$
M((-1)^\sigma5^{\widetilde a},\widetilde b)
\in G_{m+1}.
$$

#### Proof

The displayed unit decomposition and the binary expansions of $a$ and $b$
give

$$
|G_m|
=
2\cdot2^{m-2}\cdot2^m
=
2^{2m-1}.
$$

Choosing all $2m-1$ coordinates independently therefore produces every
element once with probability $2^{-(2m-1)}$. Conversely, an exact sampler
driven by unbiased bits needs at least $\log_2|G_m|=2m-1$ bits of entropy.

At the next level, the two displayed choices are precisely the two lifts of
the exponent $a$ and the two lifts of the translation $b$. Hence every fiber
of $\rho_m$ has four elements and choosing the two new high bits uniformly
preserves uniformity. $\square$

Thus the projective tower supports exact generation; no Markov-chain burn-in
or approximate-counting reduction is needed.

## 3. A coordinate-refresh chain

There is nevertheless a natural mixing problem. In the $N=N_m$ binary
coordinates, choose one coordinate uniformly and replace it by an independent
unbiased bit. Translation-coordinate refreshes are random dyadic
Dehn-twist updates; the remaining coordinates refresh the affine unit
parameter.

### Theorem 2

The coordinate-refresh chain is irreducible, aperiodic, and reversible with
respect to the uniform distribution on $G_m$. Its eigenvalues are

$$
\lambda_j=1-\frac jN,
\qquad
0\leq j\leq N,
$$

with multiplicity $\binom Nj$. In particular, its spectral gap is $1/N$.

If the chain starts from a fixed state and $\mu_t$ is its law at time $t$,
then its exact chi-square distance from uniform is

$$
\chi^2(\mu_t\Vert\pi)
=
\sum_{j=1}^{N}
\binom Nj
\left(1-\frac jN\right)^{2t}.
$$

Consequently, as $m\to\infty$, this family has total-variation cutoff at

$$
\frac N2\log N
$$

with a window of order $N$.

#### Proof

Under the binary parametrization, the chain is the random-scan heat-bath
chain on the Boolean cube. For a subset $S$ of the coordinates, let

$$
\chi_S(x)=(-1)^{\sum_{j\in S}x_j}.
$$

Refreshing a coordinate outside $S$ leaves $\chi_S$ unchanged, while
refreshing one inside $S$ gives conditional mean zero. Hence

$$
P\chi_S
=
\left(1-\frac{|S|}{N}\right)\chi_S.
$$

The Walsh characters form an orthogonal basis, proving the spectrum and,
by Parseval, the chi-square identity.

For the upper cutoff bound, use

$$
\chi^2(\mu_t\Vert\pi)
\leq
\left(1+e^{-2t/N}\right)^N-1.
$$

At $t=(N/2)(\log N+c)$ this is at most
$\exp(e^{-c})-1$.

For the lower bound, start at the all-zero coordinate vector and put
$Z(x)=\sum_{j=1}^N(-1)^{x_j}$. Then

$$
\mathbb E_{\mu_t}Z
=
N\left(1-\frac1N\right)^t,
\qquad
\mathrm{Var}_{\mu_t}Z\leq N,
$$

while $\mathbb E_\pi Z=0$ and $\mathrm{Var}_\pi Z=N$. At
$t=((N-1)/2)(\log N-c)$, Chebyshev's inequality applied at half the first
mean gives

$$
\|\mu_t-\pi\|_{\mathrm{TV}}
\geq
1-8e^{-c}.
$$

These upper and lower bounds give the stated cutoff location and window.
$\square$

## 4. What this does and does not answer

This is a direct application of the randomized-generation and mixing
questions emphasized by Motwani--Raghavan. It also provides an exact
finite-level model on which the Dehn-twist coordinate is visible.

It does **not** answer open questions about mapping-class-group quotients by
powers of Dehn twists. The group here is the affine abelian shadow of a
dyadic Demushkin outer automorphism group. Funar's questions concern much
larger mapping-class-group quotients and their representations.

It also does not produce a new A183068 congruence. Its connection with the
supercongruence program is the exact lift filtration: each new precision
level contributes two independent digits, and the same level-by-level
discipline prevents finite congruence data from being mistaken for global
mixing.

## 5. Verification

Run:

```text
python verification/related/verify_dyadic_dehn_twist_sampler.py
```

The checker verifies the unit-coordinate bijection, every four-element
reduction fiber through modulus $2^8$, the Walsh eigenvalue identity, and the
chi-square formula by exact rational arithmetic.

## References

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of $\mathbb Q_2$*][RT].
- R. Motwani and P. Raghavan,
  [*Randomized Algorithms*][MR], especially the random-walk and approximate
  generation chapters.
- A. Ayyer and B. Steinberg,
  [*Random walks on rings and modules*][AS].
- L. Funar,
  [*On mapping class group quotients by powers of Dehn twists and their
  representations*][Funar].

[RT]: https://roed314.github.io/gq2/paper.pdf
[MR]: https://doi.org/10.1017/CBO9780511814075
[AS]: https://arxiv.org/abs/1708.04223
[Funar]: https://arxiv.org/abs/2009.05961
