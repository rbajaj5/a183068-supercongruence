# The dyadic hypercube defect of an Euler-product tower

**Status.** Complete elementary theorem and exact finite checks. The
quadratic operator below is standard \(2\)-derivation infrastructure; no
priority claim is made for that operator. Its application gives the sharp
universal binary replacement for the odd-prime Euler-product theorem at the
first level and a uniform \(2^{2r-1}\) tower. A possible extra power above
the first level remains a separate target.

## 1. Setup

For finitely many colors \(\nu\), integers \(h_{\nu,m}\), and \(d\geq1\), put

```math
P_N(x,\mathbf Z)
=
\prod_{\nu}\prod_{m\geq1}
(1-Z_\nu x^m)^{N h_{\nu,m}m^d}
```

and

```math
\mathcal E_N(\mathbf Z)=[x^N]P_N(x,\mathbf Z).
\qquad\text{(1)}
```

The odd-prime theorem in
[Colored Euler-product Frobenius towers](EulerProductGaussianTower.md)
proves

```math
\mathcal E_{np^r}(\mathbf Z)
\equiv
\mathcal E_{np^{r-1}}(\mathbf Z^p)
\pmod {p^{2r}}
```

for every odd prime \(p\). The same statement is false at \(p=2,r=1\).
This note identifies exactly what replaces it.

## 2. A universal quadratic operator

Let \(R\) be an integral formal power-series ring in finitely many variables,
with the usual degreewise finiteness condition. Let

```math
\phi\!\left(\sum_{\alpha}a_\alpha X^\alpha\right)
=
\sum_{\alpha}a_\alpha X^{2\alpha}.
\qquad\text{(2)}
```

Thus \(\phi\) doubles monomial exponents but does not square integer
coefficients. Define

```math
\mathfrak q(F)
=
\frac{F^2-\phi(F)}2\pmod2.
\qquad\text{(3)}
```

### Theorem 1 (dyadic quadratic defect)

The numerator in (3) has even coefficients, so \(\mathfrak q\) is defined.
For all \(F,G\in R\),

```math
\mathfrak q(F+G)
=
\mathfrak q(F)+\mathfrak q(G)+FG
\pmod2.
\qquad\text{(4)}
```

In particular, \(\mathfrak q\) is a quadratic refinement of multiplication.

Choose any total order on the monomials and write, modulo \(4\),

```math
a_\alpha=\epsilon_\alpha+2\eta_\alpha,
\qquad
\epsilon_\alpha,\eta_\alpha\in\mathbb F_2.
```

Then

```math
\mathfrak q(F)
=
\sum_\alpha\eta_\alpha X^{2\alpha}
+
\sum_{\alpha<\beta}
\epsilon_\alpha\epsilon_\beta X^{\alpha+\beta}
\pmod2.
\qquad\text{(5)}
```

Thus on any finite truncation, \(\mathfrak q\) is an explicit degree-two
Boolean map on the two bit layers of the coefficient vector. Its domain is
the hypercube \(\mathbb F_2^{2M}\), where \(M\) is the number of retained
monomials.

#### Proof

In the square of \(F\), distinct monomials occur in symmetric pairs and
therefore have even coefficients. On the diagonal,
\(a_\alpha^2-a_\alpha\) is even. This proves integrality of (3).
Expanding \((F+G)^2\) and using additivity of \(\phi\) proves (4).

For (5), the diagonal coefficient is

```math
\frac{a_\alpha^2-a_\alpha}{2}
\equiv\eta_\alpha\pmod2,
```

while the unordered pair \(\{\alpha,\beta\}\) contributes
\(a_\alpha a_\beta\equiv
\epsilon_\alpha\epsilon_\beta\pmod2\). \(\square\)

## 3. Exact first-level obstruction

Since the exponent in \(P_N\) is linear in \(N\),

```math
P_{2n}(x,\mathbf Z)=P_n(x,\mathbf Z)^2.
\qquad\text{(6)}
```

Moreover,

```math
[x^{2n}]\phi(P_n)
=
\mathcal E_n(\mathbf Z^2).
\qquad\text{(7)}
```

Equations (3), (6), and (7) give the following exact classification.

### Theorem 2 (hypercube criterion for the modulus \(4\))

For every \(n\geq1\),

```math
\frac{
\mathcal E_{2n}(\mathbf Z)
-
\mathcal E_n(\mathbf Z^2)
}{2}
\equiv
[x^{2n}]\mathfrak q(P_n)
\pmod2.
\qquad\text{(8)}
```

Consequently,

```math
\mathcal E_{2n}(\mathbf Z)
\equiv
\mathcal E_n(\mathbf Z^2)
\pmod4
\qquad\Longleftrightarrow\qquad
[x^{2n}]\mathfrak q(P_n)=0.
\qquad\text{(9)}
```

This is a finite system of quadratic equations over \(\mathbb F_2\) in
every fixed truncation. It is the precise sense in which the binary
boundary is a hypercube problem.

## 4. The universal binary tower

The occupation-stratum proof of the odd-prime theorem also has a sharp
binary version.

### Theorem 3 (binary Euler-product tower)

For every \(n,r\geq1\),

```math
\mathcal E_{n2^r}(\mathbf Z)
\equiv
\mathcal E_{n2^{r-1}}(\mathbf Z^2)
\pmod {2^{\,2r-1}}.
\qquad\text{(10)}
```

#### Proof

The argument of Sections 3--4 of
[the odd-prime theorem](EulerProductGaussianTower.md) is repeated with the
binary Ljunggren--Jacobsthal--Kazandzidis depth

```math
3(\min\{b,s\}+1)-2.
\qquad\text{(11)}
```

The possible sign in the strongest binary scaling statement causes no
loss: for \(s\geq1\) the negative-sign case is excluded in the equal-index
application, while at \(s=0\) the modulus in (11) is \(2\), where the two
signs agree.

Occupation vectors not wholly divisible by \(2\) still vanish modulo
\(2^{2r}\), exactly as in the odd-prime proof. For a divisible occupation
with notation \(b,s,q\) from that proof, the lower factor and scaling error
supply

```math
b-s+3s+1
\geq r+dq+2s.
\qquad\text{(12)}
```

If this is below \(2r-1\), the size constraint forces a second occupied
factor at valuation at most \(q+s\). It supplies at least
\(r-1-q-s\) additional powers. The total is

```math
2r-1+(d-1)q+s\geq2r-1.
\qquad\text{(13)}
```

If \(s\geq b\), (11) has depth at least
\(3(r-1)+1=3r-2\geq2r-1\). Expanding the product of scaling quotients one
factor at a time now proves (10). \(\square\)

## 5. Sharp boundary

Take one color, \(d=1\), and \(h_m=-1\) for every \(m\). At \(n=r=1\),

```math
[Z^2]\mathcal E_2(Z)=3,
\qquad
[Z^2]\mathcal E_1(Z^2)=1.
```

Their difference is \(2\), not a multiple of \(4\). Hence the exponent
\(2r-1\) in Theorem 3 is sharp for the stated unrestricted family.
Formula (8) records the missing bit as

```math
[x^2Z^2]\mathfrak q(P_1)=1.
```

## 6. Relation to dyadic lifting theory

The connection with Roe--Turturean's
[presentation of \(G_{\mathbb Q_2}\)](https://roed314.github.io/gq2/paper/paper.html)
is structural, not a transfer of results. Their dyadic lifting count is
not determined by linear duality data and requires a quadratic obstruction.
Here the odd-prime Frobenius budget likewise loses one binary power, and the
lost bit is measured by the quadratic refinement \(\mathfrak q\).

The operator in (3) is also the sign-reversed canonical \(2\)-derivation
attached to the Frobenius lift \(\phi\). This identifies the natural
language for a corrected modulus-\(4\) theorem: retain the quadratic defect
rather than demand that it vanish universally.

No connection to the Four-Colour Theorem is used in the proof. The
hypercube arises because a coefficient modulo \(4\) has two binary digits
and the first Frobenius defect has Boolean degree two.

## 7. Next target

Exact experiments find additional cancellation in many levels \(r\geq2\).
The next question is whether the normalized higher defect factors through
an iterated version of \(\mathfrak q\), and which exponent patterns force
that defect to vanish. This is deliberately not asserted here.

The checker verifies the universal quadratic and polarization identities,
the coefficient formula (5), the exact Euler-product identity (8), the
sharp boundary example, and finite instances of Theorem 3.

Run:

```text
python verification/related/verify_dyadic_hypercube_defect.py
```
