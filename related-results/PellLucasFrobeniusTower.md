# Pell--Lucas Frobenius towers and the abc/IUT boundary

**Status date:** August 3, 2026

**Status:** complete elementary specialization of the classical Lucas-sequence
congruence, with exact checks.  The inter-universal Teichmuller/abc discussion
is a scope boundary, not a proof input and not a novelty claim.

Pell equations provide a useful two-dimensional test case for the same local
Frobenius distinction that occurs for Gaussian primes.  They do not, however,
turn the global height inequalities associated with the abc conjecture into
the local valuation estimates required by a supercongruence.

## 1. A signed adjacent tower from a Pell unit

Let $D>1$ be nonsquare and let $y_1\ne0$ in

```math
\varepsilon=x_1+y_1\sqrt D\in\mathbb Z[\sqrt D],
\qquad x_1^2-Dy_1^2=1.
```

Define integers $x_m,y_m$ by

```math
\varepsilon^m=x_m+y_m\sqrt D.
```

For an odd prime $p\nmid D$, put

```math
\chi_p=\left(\frac Dp\right)\in\{1,-1\}.
```

### Theorem 1 (Pell--Frobenius tower)

For all positive integers $n,r$,

```math
\boxed{
x_{np^r}\equiv x_{np^{r-1}}
\pmod {p^{r+v_p(n)}}
}
```

and

```math
\boxed{
y_{np^r}\equiv \chi_p y_{np^{r-1}}
\pmod {p^{r+v_p(n)}}.
}
```

Thus a split prime preserves the two Pell coordinates, whereas an inert
prime preserves the radial coordinate $x_m$ and reverses the angular
coordinate $y_m$.  This is the real-quadratic analogue of a split/inert
Frobenius twist over the Gaussian integers.

### Proof

Set $R=\mathbb Z[\sqrt D]$.  The freshman's-dream congruence and Euler's
criterion give

```math
\varepsilon^p
\equiv x_1+y_1D^{(p-1)/2}\sqrt D
\equiv x_1+\chi_p y_1\sqrt D
\pmod {pR}.
```

If $\chi_p=1$, the last member is $\varepsilon$.  If $\chi_p=-1$, it is
$\overline\varepsilon=\varepsilon^{-1}$ because the norm is one.  Hence

```math
q_p(\varepsilon):=\varepsilon^p\varepsilon^{-\chi_p}
\in 1+pR.
```

Write $m=np^{r-1}$.  Then

```math
\varepsilon^{np^r}
=\varepsilon^{\chi_pm}q_p(\varepsilon)^m.
```

For every $q\in1+pR$ and odd $p$, the binomial theorem gives

```math
q^m\equiv1\pmod {p^{1+v_p(m)}R}.
```

Indeed,
$v_p\!\binom mj\ge v_p(m)-v_p(j)$ and
$j-v_p(j)\ge1$ for $j\ge1$.  Since
$1+v_p(m)=r+v_p(n)$,

```math
\varepsilon^{np^r}
\equiv\varepsilon^{\chi_pnp^{r-1}}
\pmod {p^{r+v_p(n)}R}.
```

For $\chi_p=-1$, the right side is the conjugate of
$\varepsilon^{np^{r-1}}$.  Comparing the coefficients of $1$ and
$\sqrt D$ proves both congruences.  $\square$

### Refined exponent

Let

```math
t_p(\varepsilon)=
\max\{t\ge1:q_p(\varepsilon)\in1+p^tR\}.
```

The same proof gives the stronger modulus

```math
p^{t_p(\varepsilon)+r-1+v_p(n)}.
```

Primes with $t_p(\varepsilon)>1$ are the Pell/Lucas analogue of Wieferich
primes.  The extra exponent comes from a local Fermat quotient, not from a
global height inequality.

This theorem is also a direct all-level specialization of the published
Lucas-sequence congruence

```math
\frac{U_{pn}(P,Q)-
\left(\frac{P^2-4Q}{p}\right)U_n(P,Q)}{pn}
\in\mathbb Z_p.
```

The quadratic-unit proof above is retained because it displays the
split/inert mechanism and the refined exponent transparently.

## 2. Why abc does not prove a supercongruence exponent

The abc conjecture compares the height of a coprime additive triple
$a+b=c$ with

```math
\operatorname{rad}(abc)=\prod_{\ell\mid abc}\ell.
```

A supercongruence instead asks for a lower bound such as

```math
v_p\bigl(A(np^r)-A(np^{r-1})\bigr)\ge er.
```

The two measurements discard different information.  If $p\nmid u$, then

```math
\operatorname{rad}(p^su)=p\operatorname{rad}(u)
\qquad(s\ge1).
```

Consequently radical data alone cannot distinguish divisibility by $p^r$,
$p^{2r}$, $p^{3r}$, or $p^{4r}$.  An abc inequality can constrain the
global size and prime support of a defect only *after* local arguments have
supplied its multiplicities.  It cannot replace carry counting, harmonic
unit blocks, $p$-adic gamma expansions, or Frobenius lifting.

This obstruction is particularly concrete for the Bober fractional-index
queue.  Its open assertion is integrality of a rational gamma ratio for
every index.  That is an exact floor-function/valuation-sign problem.  An
abc height bound neither proves the required nonnegativity prime by prime
nor supplies the missing $p$-adic multiplicities.

## 3. The conditional uses that survive the boundary

There are two legitimate, secondary applications.

1. **Exceptional-value equations.**  Once a factorial-ratio or defect
   sequence is proved integral, one can ask when it equals a polynomial,
   a perfect power, or another factorial product.  Such an equality can
   sometimes be converted into an additive Diophantine equation.  The abc
   conjecture is known to imply finiteness in related factorial equations,
   such as $n!=\prod_i a_i!$.  Every proposed application still needs its
   own reduction to an abc triple; it is not automatic for a
   supercongruence sequence.

2. **Elliptic parameter families.**  When a hypergeometric or Apéry family
   is attached to elliptic curves, an abc/Szpiro-type inequality can bound
   height or discriminant in terms of conductor.  That can restrict global
   exceptional parameters.  It does not determine the local unit-root
   expansion or the exponent of an individual prime.

Pell equations are useful here as a diagnostic.  Their identity

```math
1+Dy_m^2=x_m^2
```

is already an additive Diophantine triple with infinitely many solutions.
The abc conjecture is compatible with that infinity because the radical of
$D x_m y_m$ normally grows.  Meanwhile Theorem 1 gives a strong local tower
for the same points without using abc.  The example cleanly separates the
global and local jobs.

## 4. IUT-specific status and the dyadic warning

Mochizuki's fourth IUT paper states that its Diophantine inequalities imply
Vojta, abc, and Szpiro.  Scholze and Stix published a detailed contrary
assessment concluding that the proposed argument does not prove abc.  The
present repository therefore treats every abc consequence as conditional
and does not use IUT as an established proof input.

There is a thematic dyadic parallel: IUT IV explicitly restricts important
nonarchimedean parameters to odd residue characteristic and discusses a
theta-integral structure that works for odd $p$ but not for $p=2$.  That is
not a transfer theorem for this project.  It reinforces only the existing
policy that the binary or ramified prime must be proved separately.

## 5. Verification and sources

Run

```text
python verification/related/verify_pell_lucas_frobenius.py
```

The checker tests the baseline and refined moduli for four Pell equations,
split and inert primes, multiple initial indices, and four adjacent levels.

Sources:

- Z.-W. Sun, [*Supercongruences involving Lucas sequences*](https://arxiv.org/abs/1610.03384).
- S. Mochizuki, [*Inter-universal Teichmuller Theory IV*](https://ems.press/journals/prims/articles/201528).
- P. Scholze and J. Stix, [*Why abc is still a conjecture*](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf).
- F. Luca, [*On factorials which are products of factorials*](https://doi.org/10.1017/S0305004107000308).
