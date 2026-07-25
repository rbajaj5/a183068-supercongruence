# Gaussian and cyclotomic Frobenius twists

**Status:** complete elementary deduction from the termwise transfer theorem;
unchecked for priority and independent mathematical review.

## 1. The general lift

Let $F(N,k)\in\mathbb Z$, with $F(N,k)=0$ outside
$0\leq k\leq N$, and let

```math
T_z(N)=\sum_{k=0}^N z^kF(N,k)
```

for an element $z$ of a commutative ring.  Fix a prime $p$, integers
$n,r\geq1$, and an exponent $e$.  Suppose that

```math
F(np^r,k)\equiv0\pmod {p^e}\qquad(p\nmid k)
\tag{1}
```

and

```math
F(np^r,p\ell)\equiv F(np^{r-1},\ell)\pmod {p^e}.
\tag{2}
```

Then

```math
\boxed{
T_z(np^r)\equiv T_{z^p}(np^{r-1})\pmod {p^e}.
}
\tag{3}
```

Indeed, the terms with $p\nmid k$ vanish by (1), while the remaining
terms are

```math
\begin{aligned}
T_z(np^r)
&\equiv
\sum_{\ell=0}^{np^{r-1}}z^{p\ell}F(np^r,p\ell)\\
&\equiv
\sum_{\ell=0}^{np^{r-1}}(z^p)^\ell
F(np^{r-1},\ell)
=T_{z^p}(np^{r-1})
\pmod {p^e}.
\end{aligned}
```

Thus every supercongruence proved by the discard-and-rescale method has
cyclotomic companions.  If $z=\zeta_m$ and $p\nmid m$, the map
$\zeta_m\mapsto\zeta_m^p$ is the Frobenius automorphism of the
cyclotomic coefficient ring modulo $p$.

## 2. Gaussian specialization

For the Hanna--Bala summand

```math
F(N,k)=\frac{(2N+2k)!}{k!^4(N-k)!^2},
```

define the Gaussian integer

```math
G(N)=\sum_{k=0}^N i^kF(N,k)\in\mathbb Z[i].
```

The proved termwise argument for A183068 supplies (1)--(2) with
$e=2r$.  Consequently, for every odd prime $p$,

```math
G(np^r)\equiv
\begin{cases}
G(np^{r-1})&p\equiv1\pmod4,\\
\overline{G(np^{r-1})}&p\equiv3\pmod4
\end{cases}
\pmod {p^{2r}}.
\tag{4}
```

This is the split/inert dichotomy in $\mathbb Z[i]$:

- if $p\equiv1\pmod4$, then $p=\pi\bar\pi$, Frobenius fixes $i$,
  and (4) holds simultaneously modulo $\pi^{2r}$ and
  $\bar\pi^{2r}$;
- if $p\equiv3\pmod4$, then $p$ is inert and Frobenius acts on the
  residue field by complex conjugation.

The ramified prime also has a precise cross-twist.  Since $i^2=-1$,

```math
G(n2^r)\equiv
\sum_{\ell=0}^{n2^{r-1}}(-1)^\ell
F(n2^{r-1},\ell)
\pmod {2^{2r}}.
\tag{5}
```

Equation (5) is not an automorphism statement: $2$ ramifies in
$\mathbb Z[i]$.

## 3. What this does and does not say about Gaussian primes

The lift is a genuine Gaussian-integer supercongruence, and it exposes
Frobenius functoriality that is invisible after setting $z=1$.  It is
also reusable for any Landau-depth family for which the two termwise
hypotheses have been proved.

It does **not**:

1. prove anything about the spatial distribution of Gaussian primes;
2. distinguish the two factors $\pi$ and $\bar\pi$ when a rational
   prime splits; or
3. provide a new cryptographic algorithm by itself.

For comparison, established hypergeometric congruences can recover the
real coordinate $x$ when

```math
p=x^2+y^2,\qquad p\equiv1\pmod4.
```

For example, Sun proved a binomial sum congruent modulo $p^2$ to a
signed $x$.  That is closer to constructing the primary Gaussian prime
$x+iy$, whereas (4) records the Frobenius action on a twisted
supercongruence.

The stronger research target is therefore a **one-sided unit-root
refinement**: find a twisted factorial-ratio or constant-term sequence
coming from a CM elliptic curve with $j=1728$, and prove a congruence
modulo a chosen power of $\pi$, rather than merely modulo the rational
ideal $(p)$.  Such a theorem could connect the carry filtration to the
Frobenius eigenvalue used in point counting.  Until that motive/curve
identification is supplied, the cryptographic connection is conceptual,
not deployable.

## 4. Exact checks

The companion script verifies:

- 40 instances of (4), for
  $p\in\{3,5,7,11,13\}$, $r\in\{1,2\}$, and $1\leq n\leq4$;
- 12 instances of (5), for $1\leq r\leq3$ and $1\leq n\leq4$.

Run:

```text
python verification/related/verify_gaussian_twists.py
```

These computations are regression checks, not a substitute for checking
the deduction from the A183068 termwise lemmas.

## 5. Literature positioning

The cyclotomic lift above is an elementary formal consequence of a
termwise supercongruence.  A targeted search did not locate this exact
Gaussian specialization, but polynomial, multivariate, and
hypergeometric supercongruences already provide a large nearby
literature.  No novelty claim should be made before a specialist search.

Primary comparison sources:

- Z.-W. Sun, *On sums involving products of three binomial
  coefficients*, arXiv:1012.3141.
- A. Straub, *Multivariate Apéry numbers and supercongruences of rational
  functions*, arXiv:1401.0854.
- A. Straub, *Supercongruences for polynomial analogs of the Apéry
  numbers*, arXiv:1803.07146.
