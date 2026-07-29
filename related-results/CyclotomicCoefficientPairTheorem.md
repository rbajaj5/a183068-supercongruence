# A coefficientwise theorem for A228960 and A350383

**Status:** complete elementary proof candidate; exact checks pass; two named
OEIS conjectures are obtained as specializations; conventional review and a
full literature-priority search remain pending

## 1. The paired coefficient sequences

The two cyclotomic identities

```math
1+x+x^3+x^4=(1+x)(1+x^3)
```

and

```math
(1+x+x^2)^{-1}=\frac{1-x}{1-x^3}
```

lead to the polynomial families

```math
\mathcal C_N(X)=
\sum_{0\le k\le N/3}
\binom Nk\binom N{3k}X^k
\qquad\text{(1)}
```

and

```math
\mathcal D_N(X)=
\sum_{0\le k\le N/3}
(-1)^{N-k}
\binom{N+k-1}k\binom N{3k}X^k
\qquad(N\ge1).
\qquad\text{(2)}
```

Consequently,

```math
\mathcal C_N(1)=[x^N](1+x+x^3+x^4)^N
```

is [OEIS A228960](https://oeis.org/A228960), and

```math
\mathcal D_N(1)=[x^N](1+x+x^2)^{-N}
```

is [OEIS A350383](https://oeis.org/A350383).

## 2. The coefficientwise theorem

### Theorem 1

Let \(p\ge5\) be prime and let \(n,r\ge1\). Then

```math
\mathcal C_{np^r}(X)
\equiv
\mathcal C_{np^{r-1}}(X^p)
\pmod {p^{2r}}
\qquad\text{(3)}
```

and

```math
\mathcal D_{np^r}(X)
\equiv
\mathcal D_{np^{r-1}}(X^p)
\pmod {p^{2r}}
\qquad\text{(4)}
```

coefficientwise in \(\mathbb Z[X]\).

Setting \(X=1\) proves the \(p^{2r}\) supercongruences proposed on the two
OEIS entries.  The polynomial statement is stronger: it retains the
summation-index grading and exposes the Frobenius substitution
\(X\mapsto X^p\).

## 3. Coefficients outside the surviving stratum

Put \(N=np^r\).  Suppose \(p\nmid k\).

For (1), the identities

```math
\binom Nk=\frac Nk\binom{N-1}{k-1},
\qquad
\binom N{3k}=\frac N{3k}\binom{N-1}{3k-1}
```

show that both binomial factors have \(p\)-adic valuation at least \(r\).
Here \(p\ge5\) is used to ensure \(p\nmid3k\).  Therefore

```math
p^{2r}\mid\binom Nk\binom N{3k}.
\qquad\text{(5)}
```

For (2), use

```math
\binom{N+k-1}k
=\frac Nk\binom{N+k-1}{k-1}
```

together with the second identity above.  Again, each factor supplies at
least \(p^r\), so

```math
p^{2r}\mid
\binom{N+k-1}k\binom N{3k}.
\qquad\text{(6)}
```

Thus every coefficient whose exponent is not divisible by \(p\) vanishes
at the required precision.

## 4. Scaling the surviving coefficients

Write

```math
N=pa,\qquad k=p\ell,\qquad a=np^{r-1},
```

and put

```math
t=\min\{v_p(\ell),r-1\}.
```

For \(\mathcal C\), the quotient between the upper and lower coefficients is
the product

```math
Q_C=
\frac{\binom{pa}{p\ell}}{\binom a\ell}
\cdot
\frac{\binom{pa}{3p\ell}}{\binom a{3\ell}}.
\qquad\text{(7)}
```

For \(\mathcal D\), the identity

```math
\frac{\binom{p(a+\ell)-1}{p\ell}}
     {\binom{a+\ell-1}{\ell}}
=
\frac{\binom{p(a+\ell)}{p\ell}}
     {\binom{a+\ell}{\ell}}
```

gives

```math
Q_D=
\frac{\binom{p(a+\ell)}{p\ell}}
     {\binom{a+\ell}{\ell}}
\cdot
\frac{\binom{pa}{3p\ell}}{\binom a{3\ell}}.
\qquad\text{(8)}
```

The Ljunggren--Jacobsthal--Kazandzidis scaling congruence, applied to each
fraction, yields

```math
Q_C\equiv Q_D\equiv1\pmod {p^{3(t+1)}}.
\qquad\text{(9)}
```

Indeed, if \(t<r-1\), the relevant lower parts
\(\ell,a-\ell\), \(3\ell,a-3\ell\), or \(\ell,a\) all have minimum
valuation \(t\).  If \(t=r-1\), all positive lower parts have valuation at
least \(r-1\).  Multiplication by \(3\) causes no valuation loss because
\(p\ge5\).

The signs in (2) also transfer exactly:

```math
(-1)^{pa-p\ell}=(-1)^{a-\ell},
\qquad(p\ \text{odd}).
\qquad\text{(10)}
```

## 5. The valuation budget

Let \(B_C\) or \(B_D\) be the corresponding lower-level coefficient.
If \(t<r-1\), then \(v_p(\ell)=t\).  The identities used in Section 3 give

```math
v_p\binom a\ell,\quad
v_p\binom a{3\ell},\quad
v_p\binom{a+\ell-1}\ell
\ge r-1-t.
```

Hence, in either family,

```math
v_p(B_C),\ v_p(B_D)\ge2(r-1-t).
\qquad\text{(11)}
```

Combining (9) and (11),

```math
v_p\bigl(B(Q-1)\bigr)
\ge2(r-1-t)+3(t+1)
=2r+t+1
\ge2r.
\qquad\text{(12)}
```

If \(t=r-1\), equation (9) alone supplies \(3r\ge2r\).  The coefficient
with \(\ell=0\) transfers directly.  Equations (5)--(6) kill every other
coefficient.  This proves (3)--(4).

## 6. Gaussian split and inert specializations

Set

```math
\mathcal C_N^{(i)}=\mathcal C_N(i),
\qquad
\mathcal D_N^{(i)}=\mathcal D_N(i).
```

For either family \(\mathcal F\), Theorem 1 gives

```math
\mathcal F_{np^r}(i)\equiv
\begin{cases}
\mathcal F_{np^{r-1}}(i),&p\equiv1\pmod4,\\
\overline{\mathcal F_{np^{r-1}}(i)},&p\equiv3\pmod4
\end{cases}
\pmod {p^{2r}}
\qquad\text{in }\mathbb Z[i].
\qquad\text{(13)}
```

This is the ordinary split/inert Frobenius dichotomy: \(i^p=i\) for split
primes and \(i^p=-i\) for inert primes.  Equation (13) is a formal Gaussian
specialization of the coefficient theorem; it is not a statement about the
distribution of Gaussian primes.

## 7. Small-prime and literature boundaries

The lower bound in Theorem 1 is real.  At \(p=3,r=n=k=1\), both coefficient
differences equal \(3\), so the claimed modulus \(3^2\) fails.  For
\(\mathcal D\), the coefficient with \(p=2,r=n=1,k=0\) differs by \(2\),
so the analogous modulus \(2^2\) also fails.  A possible separate binary
refinement for \(\mathcal C\) is not claimed here.

The [A228960 entry](https://oeis.org/A228960) records a much broader proposed
principle for coefficients of powers of cyclotomic rational functions.
Theorem 1 proves the displayed A228960 and A350383 instances, not that
general principle.

Exact formula and A-number searches located the live conjectures but no
earlier proof of these two complete towers.  That negative search is not a
priority certificate.  The proof uses classical binomial scaling, surveyed
for example in:

- R. Meštrović,
  [*Wolstenholme's theorem: its generalizations and extensions in the last 150 years*](https://arxiv.org/abs/1111.3057).

The contribution requiring review is therefore the pairing of the two
cyclotomic coefficient formulas with the coefficientwise valuation budget,
not a new scaling lemma.

## 8. Exact checks

The checker verifies the defining sequence values, both coefficientwise
congruences, their \(X=1\) consequences, and the Gaussian split/inert
specializations at \(p=5,7,11,13\) through three adjacent levels.  It also
records equality witnesses and the small-prime counterexamples above.

Run:

```text
python verification/related/verify_cyclotomic_coefficient_pair.py
```
