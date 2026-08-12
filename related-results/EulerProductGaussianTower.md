# A coefficientwise tower for colored Euler products

**Status:** complete elementary proof candidate; exact checks pass; proves the
quadratic baseline in Peter Bala's product-family note; the cubic A380290
conjecture remains open

## 1. The universal product

Fix an integer \(d\ge 1\), a finite number of colors \(c\), and arbitrary
integers

```math
h_{\nu,m}\in\mathbb Z
\qquad
(1\le \nu\le c,\ m\ge1).
```

Introduce independent variables \(\mathbf Z=(Z_1,\ldots,Z_c)\), and define

```math
\mathcal E_N(\mathbf Z)
=
[x^N]
\prod_{\nu=1}^{c}\prod_{m\ge1}
(1-Z_\nu x^m)^{N h_{\nu,m}m^d}.
\qquad\text{(1)}
```

Negative exponents are expanded as formal power series.  Only factors with
\(m\le N\) affect the displayed coefficient, so
\(\mathcal E_N\in\mathbb Z[\mathbf Z]\).

### Theorem 1

For every odd prime \(p\) and all \(n,r\ge1\),

```math
\mathcal E_{np^r}(\mathbf Z)
\equiv
\mathcal E_{np^{r-1}}(\mathbf Z^p)
\pmod {p^{2r}}
\qquad\text{(2)}
```

coefficientwise, where

```math
\mathbf Z^p=(Z_1^p,\ldots,Z_c^p).
```

The theorem allows positive and negative exponents, arbitrary omissions of
part sizes, and several independently marked product factors.  The hypothesis
\(d\ge1\) is the source of the second power in (2).

## 2. Occupation-vector expansion

Put

```math
M=np^r,\qquad N=np^{r-1},
```

so that \(M=pN\).  Expand the product in (1), and let
\(j_{\nu,m}\) be the occupation number selected from the factor
\((\nu,m)\).  The coefficient condition is

```math
\sum_{\nu,m}m j_{\nu,m}=M.
\qquad\text{(3)}
```

If \(h_{\nu,m}>0\), the factor contributed by \(j=j_{\nu,m}\)
has magnitude

```math
\binom{M h_{\nu,m}m^d}{j}.
\qquad\text{(4)}
```

If \(h_{\nu,m}<0\), its magnitude is

```math
\binom{M|h_{\nu,m}|m^d+j-1}{j}.
\qquad\text{(5)}
```

The signs in (4) are carried by \((-Z_\nu)^j\).  Because \(p\) is odd,
the sign at \(j=p\ell\) agrees with the lower-level sign after the
substitution \(Z_\nu\mapsto Z_\nu^p\).

For either (4) or (5), write

```math
B=M|h_{\nu,m}|m^d.
```

The elementary identities

```math
\binom Bj=\frac Bj\binom{B-1}{j-1},
\qquad
\binom{B+j-1}j=\frac Bj\binom{B+j-1}{j-1}
\qquad\text{(6)}
```

give the common valuation estimate

```math
v_p(\text{factor at }j)
\ge
\max\{v_p(B)-v_p(j),0\}.
\qquad\text{(7)}
```

## 3. Occupations not all divisible by \(p\)

Suppose first that at least two occupations \(j_{\nu,m}\) are not divisible
by \(p\).  Each corresponding factor has valuation at least \(r\) by
(6), because \(p^r\mid M\).  Their product is therefore divisible by
\(p^{2r}\).

It remains to consider the case with exactly one such occupation.  Let its
part size be \(m_0\), put

```math
q=v_p(m_0),
```

and write every other occupation as \(p\ell_{\nu,m}\).  Reducing (3)
modulo \(p\) shows that \(q\ge1\).  The exceptional factor contributes at
least

```math
r+dq
\qquad\text{(8)}
```

powers of \(p\).

If \(q\ge r\), (8) is already at least \(2r\).  If \(q<r\), divide (3)
by \(p\).  The exceptional summand now has valuation \(q-1<r-1\),
whereas \(v_p(N)\ge r-1\).  Hence some other term
\(m\ell_{\nu,m}\) has valuation

```math
t=v_p(m)+v_p(\ell_{\nu,m})\le q-1.
\qquad\text{(9)}
```

The corresponding upper-level occupation is \(p\ell_{\nu,m}\).  Equation
(7) gives its factor valuation at least

```math
r-1+d\,v_p(m)-v_p(\ell_{\nu,m})
\ge r-q.
\qquad\text{(10)}
```

Equations (8) and (10) total

```math
r+dq+r-q=2r+(d-1)q\ge2r.
\qquad\text{(11)}
```

Thus every occupation vector not wholly divisible by \(p\) vanishes
coefficientwise modulo \(p^{2r}\).

## 4. Scaling the divisible occupations

Now write every occupation as

```math
j_{\nu,m}=p\ell_{\nu,m}.
```

The size condition becomes

```math
\sum_{\nu,m}m\ell_{\nu,m}=N,
\qquad\text{(12)}
```

and the monomial \(\prod Z_\nu^{p\ell_{\nu,m}}\) is exactly the lower-level
monomial after \(\mathbf Z\mapsto\mathbf Z^p\).

For one fixed occupied factor, put

```math
B=N|h_{\nu,m}|m^d,\quad
b=v_p(B),\quad
s=v_p(\ell_{\nu,m}),\quad
q=v_p(m).
```

For a positive exponent, the upper-to-lower factor ratio is

```math
\frac{\binom{pB}{p\ell}}{\binom B\ell}.
\qquad\text{(13)}
```

For a negative exponent, it is

```math
\frac{\binom{p(B+\ell)}{p\ell}}{\binom{B+\ell}\ell}.
\qquad\text{(14)}
```

The Ljunggren--Jacobsthal--Kazandzidis congruence gives, in either case,

```math
Q_{\nu,m}\equiv1
\pmod {p^{\,3(\min\{b,s\}+1)-\epsilon_p}},
\qquad
\epsilon_p=
\begin{cases}
1,&p=3,\\
0,&p\ge5.
\end{cases}
\qquad\text{(15)}
```

The \(p=3\) loss is why it is useful to keep the whole valuation budget
rather than quote only a unit-level scaling statement.

Let \(L_{\nu,m}\) denote the lower-level factor.  If \(s\ge b\), (15)
alone has depth at least \(3r-1\), hence at least \(2r\).
Suppose \(s<b\).  Equations (7) and (15) give

```math
v_p(L_{\nu,m})+v_p(Q_{\nu,m}-1)
\ge
b-s+3s+2
\ge
r+1+dq+2s.
\qquad\text{(16)}
```

For \(p\ge5\), the right side can be increased by one, but it is not needed.

If (16) is at least \(2r\), this factor is finished.  Otherwise

```math
q+s<r-1.
\qquad\text{(17)}
```

In the sum (12), every term has to cancel through the lowest \(p\)-adic
stratum before a total divisible by \(p^{r-1}\) can remain.  Consequently
there is another occupied factor \((\mu,k)\) with

```math
v_p(k)+v_p(\ell_{\mu,k})\le q+s.
\qquad\text{(18)}
```

Its lower-level factor supplies, by (7), at least

```math
r-1-q-s
\qquad\text{(19)}
```

additional powers.  Adding (16) and (19) gives

```math
2r+(d-1)q+s\ge2r.
\qquad\text{(20)}
```

Finally, expand

```math
\prod_{\nu,m}Q_{\nu,m}-1
```

one factor at a time.  Every preceding quotient is a \(p\)-adic unit, and
(15)--(20) show that the product of all lower factors times each resulting
\(Q_{\nu,m}-1\) is divisible by \(p^{2r}\).  Therefore every divisible
occupation vector transfers to its lower-level counterpart modulo
\(p^{2r}\).  Together with Section 3, this proves Theorem 1.

## 5. The A281267 specialization

[OEIS A281267](https://oeis.org/A281267) is the scalar sequence

```math
a(N)=[x^N]\prod_{m\ge1}(1-x^m)^{Nm}.
```

It is exactly the one-color specialization of Theorem 1 with

```math
d=1,\qquad h_{1,m}=1,\qquad Z_1=1.
```

Since \(1^p=1\), the Frobenius twist disappears. Hence, for every odd
prime \(p\) and all \(n,r\ge1\),

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.
```

This proves the conjecture displayed on the OEIS page, including its
boundary prime \(p=3\). No new estimate is needed: the apparent diagonal
coefficient problem is already one member of the universal Euler-product
family.

## 6. Bala's product families

Peter Bala's
[notes on A380290 and A380291](https://oeis.org/A380290/a380290.pdf)
consider

```math
F_{\pm,d}(x)=\prod_{m\ge1}(1\pm x^m)^{m^d},
\qquad
G_d(x)=\prod_{m\ge0}(1+x^{2m+1})^{(2m+1)^d},
\qquad\text{(21)}
```

their integral powers and mixed products, and the coefficient sequences

```math
[x^N]H(x)^N.
```

Take one color for each product in (21), set its variable to \(1\) or
\(-1\), and let \(h_{\nu,m}\) select all part sizes or only odd part sizes.
Theorem 1 proves, for every \(d\ge1\), every choice of integral powers in
the note, every odd prime \(p\), and all \(n,r\ge1\),

```math
[x^{np^r}]H(x)^{np^r}
\equiv
[x^{np^{r-1}}]H(x)^{np^{r-1}}
\pmod {p^{2r}}.
\qquad\text{(22)}
```

Thus the weaker congruence proposed in the note for \(d\ne2\) follows,
with \(p\ge3\) in place of \(p\ge7\).  For \(d=2\), (22) supplies a
quadratic baseline but not the conjectured cubic exponent.

In particular, [OEIS A380290](https://oeis.org/A380290) is

```math
a(N)=[x^N]\prod_{m\ge1}(1-x^m)^{-Nm^2}.
\qquad\text{(23)}
```

Theorem 1 proves

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}
\qquad(p\text{ odd}),
\qquad\text{(24)}
```

while the published \(p^{3r}\) conjecture for \(p\ge7\) remains open.

## 7. The exact logarithmic Frobenius identity at \(d=2\)

The special cubic A380290 target already appears in the logarithm of its
product.  Put

```math
C_s(Z)=\sum_{m\mid s}m^3Z^{s/m}.
\qquad\text{(25)}
```

Then

```math
x\frac{d}{dx}
\log\prod_{m\ge1}(1-Zx^m)^{-m^2}
=
\sum_{s\ge1}C_s(Z)x^s.
\qquad\text{(26)}
```

If \(s=p^a u\) with \(p\nmid u\), splitting the divisors of \(ps\) by
their \(p\)-adic valuation gives the exact identity

```math
C_{ps}(Z)-C_s(Z^p)
=p^{3(a+1)}C_u(Z).
\qquad\text{(27)}
```

Thus the logarithmic ghost coordinates have a literal cubic Frobenius
defect.  Theorem 1 shows that their coefficient-power transform always
retains two powers.  The open A380290 problem is to explain why evaluation
at \(Z=1\) retains the third power at every level, while the Gaussian
evaluation does not.

## 8. Gaussian and cyclotomic refinement

For the one-color reciprocal product, define

```math
\mathcal M_{d,A,N}(Z)
=
[x^N]\prod_{m\ge1}(1-Zx^m)^{-ANm^d}.
\qquad\text{(28)}
```

Theorem 1 gives the coefficientwise Frobenius law

```math
\mathcal M_{d,A,np^r}(Z)
\equiv
\mathcal M_{d,A,np^{r-1}}(Z^p)
\pmod {p^{2r}}.
\qquad\text{(29)}
```

At \(Z=i\), equation (29) becomes

```math
\mathcal M_{d,A,np^r}(i)
\equiv
\begin{cases}
\mathcal M_{d,A,np^{r-1}}(i),&p\equiv1\pmod4,\\
\overline{\mathcal M_{d,A,np^{r-1}}(i)},&p\equiv3\pmod4
\end{cases}
\pmod {p^{2r}}
\qquad\text{in }\mathbb Z[i].
\qquad\text{(30)}
```

This Gaussian twist is genuinely sharp at the quadratic exponent.  For
\(d=A=n=r=1\) the coefficient of \(Z\) in the difference in (29) is
\(p^2\).  For the A380290 exponent \(d=2\), exact Gaussian evaluations
also attain valuation \(2r\), for example at \(p=3,5,7\) and \(r=1,2\).
Thus the untwisted cubic conjecture cannot simply be transported to the
part-count twist.

Equation (30) is a split/inert Frobenius specialization over
\(\mathbb Z[i]\).  It is not a one-sided theorem at a selected prime
\(\pi\mid p\), and it makes no claim about the spatial distribution of
Gaussian primes.

## 9. Boundaries and provenance

The degree condition is substantive.  If \(d=0\), take one color with
\(h_m=-2\) for every \(m\).  At \(p=3,n=r=1\), the coefficient of \(Z\)
in the upper-minus-lower polynomial is \(6\), not divisible by \(3^2\).

The unmodified all-level statement at \(p=2\) fails at the first lift. For
\(d=1\), \(h_m=-1\), and \(n=r=1\), the coefficient of \(Z^2\) differs by
\(2\), not by a multiple of \(4\). The separate
[dyadic hypercube theorem](DyadicHypercubeDefect.md) proves that this is the
only universal loss: the first lift has sharp modulus \(2\), while every
level \(r\ge2\) recovers the full coefficientwise modulus \(2^{2r}\).

The scaling input is classical.  A convenient survey is R. Meštrović,
[*Wolstenholme's theorem: its generalizations and extensions in the last
150 years*](https://arxiv.org/abs/1111.3057).  The new item requiring
review is the occupation-stratum budget in Sections 3--4 and its
application to Bala's full product packet.  Formula searches located the
live conjectures and general literature on Gauss congruences, but that
negative search is not a priority certificate.

## 10. Exact checks

The checker:

1. reproduces the published initial values of A380290;
2. reproduces the first fifteen A281267 terms and checks 34 instances of
   its adjacent \(p^{2r}\) tower, including \(p=3\);
3. verifies (2) coefficientwise for positive, negative, omitted, and
   two-color exponent patterns at \(p=3,5,7\);
4. verifies the exact logarithmic identity (27);
5. verifies the split/inert Gaussian specialization;
6. records exact \(p^{2r}\) equality witnesses; and
7. confirms the \(d=0\) and \(p=2\) boundary counterexamples.

Run:

```text
python verification/related/verify_euler_product_gaussian_tower.py
```
