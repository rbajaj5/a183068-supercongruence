# Primitive collision orbits and the Bala supercongruence exponents

**Status:** complete elementary synthesis and exact obstruction theorem.
The Dold/Gauss dictionary is classical. Its application to the finite-field
collision counts in this repository, and its use as a boundary test for the
110-record Bala census, are new to this repository. No literature-priority
claim is made.

This note concerns the **Jacobian conjecture**, not a conjecture bearing
Jacobson's name.

## 1. The genuine bridge

The Bala census and the finite-field Jacobian-collision program both produce
integer sequences indexed by positive integers. Their first common layer is
not a particular factorial sum. It is the Euler product

```math
Z_a(T)
=
\exp\left(\sum_{n\geq1}a_n\frac{T^n}{n}\right)
=
\prod_{d\geq1}(1-T^d)^{-b_d}.
\tag{1}
```

Logarithmic differentiation gives

```math
a_n=\sum_{d\mid n}d\,b_d,
\qquad
n b_n=\sum_{e\mid n}\mu(e)a_{n/e}.
\tag{2}
```

The numbers \(a_n\) are the ghost components and \(b_d\) are the Euler
exponents. In dynamics, \(a_n\) can count fixed points of the \(n\)-th
iterate and \(b_d\) counts primitive orbits of length \(d\). For a scheme
over a finite field, \(a_n\) can count points over the degree-\(n\)
extension and \(b_d\) counts closed points of degree \(d\).

This is the precise sense in which a supercongruence can be read as a
statement about arithmetic dynamics.

## 2. Exact higher-Dold criterion

Fix an integer \(h\geq1\).

### Theorem 1

For an integer sequence \((a_n)_{n\geq1}\), the following are equivalent.

1. For every prime \(p\), every \(r\geq1\), and every \(m\geq1\),

```math
a_{mp^r}\equiv a_{mp^{r-1}}\pmod {p^{hr}}.
\tag{3}
```

2. The Euler exponents in (1) are integers and, whenever \(p\nmid m\),

```math
b_{mp^r}\equiv0\pmod {p^{(h-1)r}}.
\tag{4}
```

It is enough in (3) to use \(m\) coprime to \(p\).

### Proof

Assume first that the \(b_d\) are integers. If \(p\nmid m\), equation (2)
gives the exact identity

```math
a_{mp^r}-a_{mp^{r-1}}
=
p^r\sum_{d\mid m}d\,b_{dp^r}.
\tag{5}
```

Thus (4) implies (3). If the original \(m\) contains \(p^s\), apply the
coprime case at level \(r+s\); the resulting modulus \(p^{h(r+s)}\) is at
least the required \(p^{hr}\).

Conversely, suppose (3) holds. Ordinary Gauss congruences follow because
\(h\geq1\). For \(n=mp^r\), with \(p\nmid m\), Mobius inversion gives

```math
n b_n
=
\sum_{e\mid m}\mu(e)
\left(a_{mp^r/e}-a_{mp^{r-1}/e}\right).
\tag{6}
```

The right side is divisible by \(p^r\). Applying this at every prime-power
divisor of \(n\) proves \(b_n\in\mathbb Z\).

Now divide (5) by \(p^r\). Congruence (3) says that

```math
\sum_{d\mid m}d\,b_{dp^r}
\equiv0\pmod {p^{(h-1)r}}.
\tag{7}
```

Mobius inversion on the divisor lattice of \(m\) shows that
\(m b_{mp^r}\) has the same divisibility. Since \(p\nmid m\), this is
equivalent to (4). \(\square\)

For \(h=1\), Theorem 1 is the classical Dold/Gauss criterion. The extra
content of a quadratic or cubic supercongruence is now transparent:

| Adjacent tower | Primitive-orbit divisibility |
| --- | --- |
| modulo \(p^r\) | \(b_{mp^r}\in\mathbb Z\) |
| modulo \(p^{2r}\) | \(p^r\mid b_{mp^r}\) |
| modulo \(p^{3r}\) | \(p^{2r}\mid b_{mp^r}\) |

## 3. Collision schemes of polynomial maps

Let

```math
F:\mathbb A^d\longrightarrow\mathbb A^d
```

be a polynomial map over \(\mathbb F_q\). Its off-diagonal collision scheme
is

```math
\mathcal C_F
=
\{(x,y):F(x)=F(y),\ x\ne y\}.
\tag{8}
```

Put

```math
c_F(n)=\#\mathcal C_F(\mathbb F_{q^n}).
\tag{9}
```

The Hasse--Weil Euler product is

```math
Z_{\mathcal C_F}(T)
=
\exp\left(\sum_{n\geq1}c_F(n)\frac{T^n}{n}\right)
=
\prod_{x\in|\mathcal C_F|}
(1-T^{\deg x})^{-1}.
\tag{10}
```

Hence the exponent \(b_d\) in (1) is exactly the number of closed collision
points of degree \(d\). Theorem 1 gives the following concrete criterion.

### Corollary 2

Every finite-field collision sequence satisfies

```math
c_F(mp^r)\equiv c_F(mp^{r-1})\pmod {p^r}
\tag{11}
```

for every index prime \(p\), including \(p=\operatorname{char}\mathbb F_q\).
It satisfies the stronger modulus \(p^{hr}\) exactly when the number of
primitive closed collision points of degree \(mp^r\) is divisible by
\(p^{(h-1)r}\), for \(p\nmid m\).

Thus a cubic Bala-style tower for collision counts is not a formal
consequence of the Keller condition. It demands two extra powers per
prime-power level in the primitive collision orbits.

## 4. The degree-three Jacobian map is a sharp obstruction

For the degree-three map studied in
[the finite-field collision note](JacobianCounterexampleFiniteFieldCounts.md),
the off-diagonal collision count over an odd prime-power field \(Q\) is

```math
\mathcal V(Q)
=
\begin{cases}
(Q-1)(Q^2+2),&\operatorname{char}\mathbb F_Q\ne3,\\
Q^2(Q-1),&\operatorname{char}\mathbb F_Q=3.
\end{cases}
\tag{12}
```

Fix an odd prime \(q\ne3\), use \(\mathbb F_q\) as the base field, and set

```math
c(n)=\mathcal V(q^n)
=q^{3n}-q^{2n}+2q^n-2.
\tag{13}
```

### Theorem 3

At the index prime \(p=q\),

```math
v_q\bigl(c(q)-c(1)\bigr)=1.
\tag{14}
```

Consequently the collision sequence has the ordinary Gauss congruence at
this level, but it has neither a quadratic nor a cubic Bala-style
supercongruence.

### Proof

Factoring one \(q\) gives

```math
\begin{aligned}
c(q)-c(1)
=q\bigl(
&q^{3q-1}-q^{2q-1}+2q^{q-1}\\
&-q^2+q-2
\bigr).
\end{aligned}
\tag{15}
```

The parenthesized factor is congruent to \(-2\) modulo \(q\), and is
therefore a \(q\)-adic unit. \(\square\)

In characteristic \(3\), the corresponding first difference has valuation
exactly \(2\), still short of a cubic modulus.

This obstruction matters conceptually: a nontrivial collision scheme
automatically supplies a Gauss sequence, but the Keller condition does not
manufacture the additional orbit multiplicities seen in the Bala
supercongruences.

## 5. What the 110-record census gains

Theorem 1 supplies a second interpretation for every **linear** tower in the
census.

- The proposed A183068 modulus \(p^{2r}\) says that its formal primitive
  orbit multiplicities at lengths \(mp^r\) carry at least \(r\) extra
  powers of \(p\).
- The cubic coefficient, Apéry, Franel, and factorial-ratio towers say that
  the corresponding multiplicities carry at least \(2r\) powers.
- Geng-Rui Zhang proved that several of the relevant classical families,
  including Apéry and Franel numbers, are realizable periodic-point
  sequences. For those families the \(b_d\) are not merely formal integers:
  they are nonnegative primitive-orbit counts.
- The nonlinear Frobenius laws in the product route, such as
  \(a(np^r)\equiv a(np^{r-1})^p\), are not instances of Theorem 1. They
  require the multiplicative/Witt side of the repository's Frobenius-packet
  framework.
- The derived-defect records acquire an orbit interpretation only after the
  parent defect relation is proved; the dictionary does not close those
  open relations.

There is also an important Catalan warning. Zhang proves that the Catalan,
Motzkin, and Schroder sequences themselves are not even almost realizable.
The Bala truncation sequences A333090--A333097 are different sequences.
Their conjectural cubic towers would prove strong divisibility of their
formal Euler exponents, but positivity of all those exponents is a separate
problem.

The exact checker finds positive integral exponents through \(n=49\) for
A333093. That is evidence, not a proof of realizability.

### Corollary 4: actual primitive-orbit multiplicities

Let

```math
A(n)=\sum_{k=0}^n
\binom nk^2\binom{n+k}{k}^2
\qquad\text{(A005259)}
\tag{16}
```

and

```math
F_4(n)=\sum_{k=0}^n\binom nk^4
\qquad\text{(A005260)}.
\tag{17}
```

Zhang proved that both sequences are realizable: there are self-maps whose
numbers of fixed points of the \(n\)-th iterates are \(A(n)\) and \(F_4(n)\).
Write \(O_A(d)\) and \(O_{F_4}(d)\) for the corresponding numbers of
primitive orbits of length \(d\). The published cubic supercongruences for
these Apéry--Franel families, together with Theorem 1, give

```math
p^{2r}\mid O_A(mp^r),
\qquad
p^{2r}\mid O_{F_4}(mp^r)
\tag{18}
```

for every prime \(p\geq5\), \(r\geq1\), and \(p\nmid m\).

The conclusion is independent of the chosen realizations because the
primitive-orbit counts are uniquely recovered by Möbius inversion. Thus two
established facts from different literatures combine to give a concrete
new interpretation: at every \(p\)-power stratum, the primitive cycles occur
in packets divisible by \(p^{2r}\).

Both sequences occur in the 110-record search corpus. This corollary does
not close a live Bala conjecture attached to either record; it identifies
what the already-established cubic towers mean dynamically.

## 6. Two Frobenius axes

The distinction below prevents a recurrent indexing error.

1. Existing Jacobian notes often fix the characteristic \(p\) and compare
   \(\#X(\mathbb F_{p^r})\) with \(\#X(\mathbb F_{p^{r-1}})\). This changes
   the extension degree additively from \(r-1\) to \(r\).
2. A Bala tower applied to a point-count sequence compares
   \(\#X(\mathbb F_{q^{mp^r}})\) with
   \(\#X(\mathbb F_{q^{mp^{r-1}}})\). This multiplies the extension degree
   by \(p\).

Only the second comparison is the Dold/Gauss ghost-component operation in
Theorem 1. Results on one axis cannot be transferred silently to the other.

## 7. Verification

The exact checker
[`verify_jacobian_euler_orbit_bridge.py`](../verification/related/verify_jacobian_euler_orbit_bridge.py)
performs 4,192 integer-arithmetic checks:

- 3,792 Mobius-inversion and ghost/orbit identities;
- 347 orbit-divisibility checks for A183068, the proved coefficient family
  A002003, the conjectural Catalan truncation A333093, and the realizable
  Apéry and fourth-order Franel sequences; and
- 53 exact closed-point and sharp-obstruction checks for the degree-three
  collision scheme.

The A333093 checks are explicitly regression evidence. They are not used to
claim its conjecture or realizability.

## 8. Sources

- J. Byszewski, G. Graff, and T. Ward,
  [Dold sequences, periodic points, and dynamics](https://arxiv.org/abs/2007.04031).
- G.-R. Zhang,
  [Realizability of Some Combinatorial Sequences](https://arxiv.org/abs/2302.09454),
  *Journal of Integer Sequences* 27 (2024), Article 24.3.3.
- F. Beukers, M. Houben, and A. Straub,
  [Gauss congruences for rational functions in several variables](https://arxiv.org/abs/1710.00423).
- A. Straub,
  [Multivariate Apéry numbers and supercongruences of rational functions](https://arxiv.org/abs/1401.0854).
- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained).

The first four references control the classical Gauss/Dold,
realizability, and cubic-supercongruence inputs. The last controls the
weighted-lift source boundary. The collision formulas used in Section 4 are
proved separately in this repository.
