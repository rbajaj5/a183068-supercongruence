# The dyadic hypercube defect of an Euler-product tower

**Status.** Complete elementary theorem and exact finite checks. The
quadratic operator below is standard \(2\)-derivation infrastructure; no
priority claim is made for that operator. Its application gives the sharp
universal binary replacement for the odd-prime Euler-product theorem: the
first lift has modulus \(2\), while every later lift recovers the full
quadratic modulus \(2^{2r}\).

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

## 4. Closed logarithmic form of the defect

The hypercube formula can be compressed further for products.  If \(F\)
has constant coefficient \(1\), define its normalized defect

```math
\Lambda(F)=\frac{\mathfrak q(F)}{\phi(F)}
\quad\text{in }R/2R.
\qquad\text{(10)}
```

The denominator is a unit.

### Theorem 3 (logarithmic dyadic defect)

For units \(F,G\) with constant coefficient \(1\),

```math
\Lambda(FG)=\Lambda(F)+\Lambda(G).
\qquad\text{(11)}
```

For the Euler product in Section 1,

```math
\Lambda(P_n)
=
(n\bmod2)
\sum_{\nu,m}
(h_{\nu,m}m^d\bmod2)
\frac{Z_\nu x^m}{1+Z_\nu x^m}.
\qquad\text{(12)}
```

Since \(d\geq1\), only odd part sizes with odd \(h_{\nu,m}\) contribute.
Equivalently,

```math
\frac{P_{2n}(x,\mathbf Z)-P_n(x^2,\mathbf Z^2)}2
\equiv
\phi(P_n)
(n\bmod2)
\sum_{\substack{\nu,\ m\ {\rm odd}\\h_{\nu,m}\ {\rm odd}}}
\frac{Z_\nu x^m}{1+Z_\nu x^m}
\pmod2.
\qquad\text{(13)}
```

Thus:

1. if \(n\) is even, the full series difference in (13) is divisible by
   \(4\), not merely its central coefficient;
2. if \(n\) is odd, the obstruction depends only on the odd part sizes
   whose product multiplicities are odd; and
3. the apparent high-dimensional hypercube map is the coefficient form of
   one additive logarithmic defect.

#### Proof

Direct expansion gives the exact product rule

```math
\mathfrak q(FG)
=
F^2\mathfrak q(G)+\phi(G)\mathfrak q(F).
\qquad\text{(14)}
```

Modulo \(2\), \(F^2=\phi(F)\), so division by
\(\phi(F)\phi(G)\) proves (11).  It follows for every integer \(e\) that
\(\Lambda(F^e)=e\Lambda(F)\).

Put \(M=Z_\nu x^m\).  Since

```math
\mathfrak q(1-M)=M^2-M
```

and \(1-M^2=(1+M)^2\) modulo \(2\),

```math
\Lambda(1-M)
=
\frac{M+M^2}{1+M^2}
=
\frac{M}{1+M}.
```

Additivity over all Euler factors proves (12), and multiplying by
\(\phi(P_n)\) gives (13). \(\square\)

## 5. The restored binary tower

The occupation-stratum proof first gives a uniform bound one power below
the odd-prime theorem. The logarithmic defect then restores the missing
power at every level above the first.

### Theorem 4 (sharp binary Euler-product tower)

For every \(n,r\geq1\),

```math
\mathcal E_{n2^r}(\mathbf Z)
\equiv
\mathcal E_{n2^{r-1}}(\mathbf Z^2)
\pmod {2^{\,e(r)}},
\qquad
e(r)=
\begin{cases}
1,&r=1,\\
2r,&r\geq2.
\end{cases}
\qquad\text{(15)}
```

#### Proof

We first prove the uniform modulus \(2^{2r-1}\).
The argument of Sections 3--4 of
[the odd-prime theorem](EulerProductGaussianTower.md) is repeated with the
binary Ljunggren--Jacobsthal--Kazandzidis depth

```math
3(\min\{b,s\}+1)-2.
\qquad\text{(16)}
```

The possible sign in the strongest binary scaling statement causes no
loss: for \(s\geq1\) the negative-sign case is excluded in the equal-index
application, while at \(s=0\) the modulus in (16) is \(2\), where the two
signs agree.

Occupation vectors not wholly divisible by \(2\) still vanish modulo
\(2^{2r}\), exactly as in the odd-prime proof. For a divisible occupation
with notation \(b,s,q\) from that proof, the lower factor and scaling error
supply

```math
b-s+3s+1
\geq r+dq+2s.
\qquad\text{(17)}
```

If this is below \(2r-1\), the size constraint forces a second occupied
factor at valuation at most \(q+s\). It supplies at least
\(r-1-q-s\) additional powers. The total is

```math
2r-1+(d-1)q+s\geq2r-1.
\qquad\text{(18)}
```

If \(s\geq b\), (16) has depth at least
\(3(r-1)+1=3r-2\geq2r-1\). Expanding the product of scaling quotients one
factor at a time proves the uniform bound.

It remains to recover one power when \(r\geq2\). Put

```math
N=n2^{r-1},\qquad
c_{\nu,m}=h_{\nu,m}m^d,\qquad
M_{\nu,m}=Z_\nu x^m.
```

There is an exact identity of formal series

```math
\frac{P_{2N}}{\phi(P_N)}
=
\prod_{\nu,m}
\left(\frac{1-M_{\nu,m}}{1+M_{\nu,m}}\right)^{Nc_{\nu,m}}
=
\exp(-2NS),
\qquad\text{(19)}
```

where

```math
S=
\sum_{\nu,m}c_{\nu,m}
\sum_{\substack{k\geq1\\k\ {\rm odd}}}
\frac{M_{\nu,m}^k}{k}.
\qquad\text{(20)}
```

All coefficients of \(S\) are \(2\)-adic integers. Hence

```math
P_{2N}-\phi(P_N)
=
\phi(P_N)
\sum_{j\geq1}\frac{(-2N)^j}{j!}S^j.
\qquad\text{(21)}
```

We estimate the coefficient of \(x^{2N}\), coefficientwise in the color
variables.

First record a divisibility lemma. For \(L>0\),

```math
v_2\!\left([x^L\mathbf Z^\alpha]P_N\right)
\geq
\max\{v_2(N)-v_2(L),0\}.
\qquad\text{(22)}
```

Indeed, in any occupation vector of size \(L\), choose an occupied pair
\((m,j)\) minimizing \(v_2(mj)\). This minimum is at most \(v_2(L)\).
Writing \(q=v_2(m)\), the corresponding binomial factor has valuation at
least

```math
v_2(N)+dq-v_2(j)
\geq v_2(N)-v_2(L).
```

This proves (22) term by term.

Consider the \(j=1\) term in (21). A monomial \(M_{\nu,m}^k\) in \(S\)
has odd \(k\). Since \(\phi(P_N)\) has only even \(x\)-degrees, a nonzero
contribution forces \(m\) to be even. Put \(q=v_2(m)\geq1\). If \(q\geq r\),
the factor \(m^d\) supplies at least \(r\) powers in addition to the \(r\)
powers in \(2N\). If \(q<r\), write

```math
2L=2N-mk.
```

Then \(v_2(L)=q-1\), so (22) supplies at least \(r-q\) powers from the
coefficient of \(P_N\), while \(m^d\) supplies at least \(q\). Again the
total is at least \(2r\).

For \(j=2\), the scalar \((2N)^2/2\) has valuation at least \(2r-1\).
It remains to show that the relevant coefficient of \(\phi(P_N)S^2\) is
even. Modulo \(2\), the series \(\phi(P_N)\) has \(x\)-degrees divisible
by \(2^r\). The series \(S\) is supported only in odd \(x\)-degrees, and
in characteristic \(2\) every degree in \(S^2\) is congruent to \(2\)
modulo \(4\). Since \(r\geq2\), such a degree cannot complement a multiple
of \(2^r\) to the target degree \(2N\), itself a multiple of \(2^r\).
The coefficient is therefore even.

Finally, for \(j\geq3\),

```math
v_2\!\left(\frac{(2N)^j}{j!}\right)
\geq rj-(j-1)\geq2r
```

because \(r\geq2\). Every term in (21) is therefore divisible by
\(2^{2r}\), proving (15). \(\square\)

## 6. Sharp boundary

Take one color, \(d=1\), and \(h_m=-1\) for every \(m\). At \(n=r=1\),

```math
[Z^2]\mathcal E_2(Z)=3,
\qquad
[Z^2]\mathcal E_1(Z^2)=1.
```

Their difference is \(2\), not a multiple of \(4\). Hence \(e(1)=1\) is
sharp for the stated unrestricted family.
Formula (8) records the missing bit as

```math
[x^2Z^2]\mathfrak q(P_1)=1.
```

For the same family and every \(r\geq2\), the coefficient of \(Z\) in the
adjacent difference equals \(2^{2r}\). Thus the restored exponent
\(e(r)=2r\) is also sharp.

## 7. Relation to dyadic lifting theory

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

## 8. The exact A380290 first-lift obstruction

The first-lift problem can be made completely explicit for Bala's
A380290 product. Put

```math
F(y)=\prod_{m\geq1}(1-y^m)^{-m^2},
\qquad
a(n)=[y^n]F(y)^n,
\qquad\text{(23)}
```

and define the binary theta series

```math
\Theta_2(y)
=
\sum_{\substack{a\geq0\\s\geq1\ {\rm odd}}}
y^{2^a s^2}
\quad\text{in }\mathbb F_2[[y]].
\qquad\text{(24)}
```

### Theorem 5 (A380290 binary theta obstruction)

If \(n\) is even, then

```math
a(2n)\equiv a(n)\pmod4.
\qquad\text{(25)}
```

If \(n\) is odd, then

```math
\frac{a(2n)-a(n)}2
\equiv
[y^n]F(y)^n\Theta_2(y)
\pmod2.
\qquad\text{(26)}
```

Consequently, for odd \(n\),

```math
a(2n)\equiv a(n)\pmod4
\quad\Longleftrightarrow\quad
[y^n]F(y)^n\Theta_2(y)=0
\quad\text{in }\mathbb F_2.
\qquad\text{(27)}
```

#### Proof

For A380290, formula (13) has one color, \(Z=1\), \(d=2\), and
\(h_m=-1\). If \(n\) is even, the factor \(n\bmod2\) makes the entire
first defect vanish, proving (25).

Now suppose that \(n\) is odd. The logarithmic factor in (13) is

```math
B(x)=\sum_{m\ {\rm odd}}\frac{x^m}{1+x^m}
=
\sum_{\substack{m\ {\rm odd}\\k\geq1}}x^{mk}
\quad\text{in }\mathbb F_2[[x]].
\qquad\text{(28)}
```

Only the even-degree part of \(B\) can contribute against
\(\phi(P_n)=F(x^2)^n\). The coefficient of \(x^{2t}\) in \(B\) is the
number of odd divisors of \(t\), modulo \(2\). A positive integer has an
odd number of divisors exactly when it is a square. Hence this coefficient
is \(1\) exactly when the odd part of \(t\) is a square, equivalently when

```math
t=2^a s^2
\qquad(a\geq0,\ s\ {\rm odd}).
```

Thus the even-degree part of \(B(x)\) is
\(\Theta_2(x^2)\). Taking the coefficient of \(x^{2n}\) in (13) and
putting \(y=x^2\) proves (26), and (27) follows. \(\square\)

The first 64 defect bits are \(1\) precisely at

```text
1, 3, 7, 13, 15, 19, 25, 27, 29, 31, 37, 43, 45,
51, 53, 57, 61, 63.
```

This list is a finite certificate, not a claimed periodicity or density
law.

## 9. Next target

The universal binary classification problem is now confined to the first
lift: determine which exponent patterns make the explicit logarithmic
defect (13) vanish in central degree. For A380290, Theorem 5 reduces that
question to the diagonal parity problem (27). One can then ask which
special families gain powers beyond the sharp universal exponent \(2r\).

The checker verifies the universal quadratic and polarization identities,
the coefficient formula (5), the exact Euler-product identity (8), the
closed logarithmic formula (13), both sharp boundary regimes, and finite
instances of the restored Theorem 4.

Run:

```text
python verification/related/verify_dyadic_hypercube_defect.py
```
