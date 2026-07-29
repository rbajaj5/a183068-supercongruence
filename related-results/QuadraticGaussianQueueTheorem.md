# Quadratic Frobenius towers for A005259 and the A333592 family

**Status:** complete elementary deduction from
Ljunggren--Jacobsthal--Kazandzidis scaling; exact checks pass; presented as
a literature-aligned corollary, not as a priority claim

## 1. Two polynomial families

Define

```math
\mathcal A_N(X)=
\sum_{k=0}^{N}
\left(\binom Nk\binom{N+k}k\right)^2X^k
```

and, for \(N\ge1\) and positive integers \(u,v\),

```math
\mathcal B_N^{u,v}(X)=
\sum_{k=0}^{uN}\binom{vN+k-1}k^2X^k.
```

The values \(\mathcal A_N(1)\) are the Apéry numbers A005259, while
\(\mathcal B_N^{1,1}(1)\) are A333592.  The two-parameter family is the
positive-\((u,v)\) part of the broader family proposed on that OEIS entry.

### Theorem 1

For every prime \(p\) and all \(n,r\ge1\),

```math
\mathcal A_{np^r}(X)
\equiv
\mathcal A_{np^{r-1}}(X^p)
\pmod {p^{2r}}
\qquad\text{(1)}
```

and

```math
\mathcal B_{np^r}^{u,v}(X)
\equiv
\mathcal B_{np^{r-1}}^{u,v}(X^p)
\pmod {p^{2r}}
\qquad\text{(2)}
```

coefficientwise in \(\mathbb Z[X]\), for every \(u,v\ge1\).

The theorem proves the two remaining quadratic observations in the
[Bala Gaussian-twist pilot](BalaGaussianTwistPilot.md).  It does not prove
the stronger untwisted \(p^{3r}\) conjecture recorded on the
[A333592 OEIS entry](https://oeis.org/A333592).

## 2. A common coefficient lemma

Put

```math
H_1(N,k)=\binom Nk\binom{N+k}k
=\frac{(N+k)!}{k!^2(N-k)!}
```

and

```math
H_{2,v}(N,k)=\binom{vN+k-1}k.
```

Thus the coefficients in (1) and (2) are \(H_1(N,k)^2\) and
\(H_{2,v}(N,k)^2\), respectively.  The parameter \(u\) only changes the
support bound from \(k\le N\) to \(k\le uN\), and that bound scales
compatibly under \(N\mapsto pN\).

Let \(N=np^r\).  If \(p\nmid k\), then

```math
\binom Nk=\frac Nk\binom{N-1}{k-1}
```

and

```math
\binom{vN+k-1}k
=\frac {vN}k\binom{vN+k-1}{k-1}.
```

Therefore

```math
v_p(H_1(N,k)),\ v_p(H_{2,v}(N,k))\ge r,
\qquad
p^{2r}\mid H_1(N,k)^2,\ H_{2,v}(N,k)^2
\qquad(p\nmid k).
\qquad\text{(3)}
```

This disposes of every coefficient whose exponent is not divisible by
\(p\).

## 3. Scaling the surviving coefficients

Write

```math
N=pa,\qquad k=p\ell,\qquad
A=H(pa,p\ell),\qquad B=H(a,\ell),
```

where \(H\) is whichever of \(H_1,H_{2,v}\) is under consideration.

For \(H_1\), the quotient \(Q=A/B\) is the scaling quotient of the
three-part multinomial with lower parts

```math
\ell,\quad\ell,\quad a-\ell.
```

For \(H_{2,v}\), the identity

```math
\binom{p(va+\ell)-1}{p\ell}
=\frac{va}{va+\ell}\binom{p(va+\ell)}{p\ell}
```

and its unscaled version show that

```math
Q=
\frac{\binom{p(va+\ell)}{p\ell}}
     {\binom{va+\ell}{\ell}}.
```

In the first case let \(s\) be the minimum \(p\)-adic valuation of the
positive members of \(\ell,a-\ell\); in the second let it be the minimum
valuation of the positive members of \(\ell,va\).  The classical scaling
congruence gives

```math
Q\equiv1\pmod {p^{3(s+1)-\varepsilon_p}}
\qquad(p\ \text{odd}),
\qquad\text{(4)}
```

where \(\varepsilon_3=1\) and \(\varepsilon_p=0\) for \(p\ge5\).
At \(p=2\), the strongest source form permits a sign and has exponent
\(3s+1\).  Squaring removes the sign.  In every case,

```math
v_p(Q^2-1)\ge
\begin{cases}
3s+2,&p=2,\\
3s+2,&p=3,\\
3s+3,&p\ge5.
\end{cases}
\qquad\text{(5)}
```

For \(p=2,s=0\), (5) uses only the elementary fact that
\(v_2(u-1)+v_2(u+1)\ge3\) for every odd \(2\)-adic unit \(u\).
For \(s\ge1\), it follows from the signed scaling congruence and the
opposite factor of \(Q^2-1\).  This is precisely where the binary case
needs separate handling.

## 4. The valuation budget

Suppose \(s<r-1\).  For \(H_1\), both
\(v_p(\ell)\) and \(v_p(a-\ell)\) equal \(s\), and the factor
\(\binom a\ell\) gives

```math
v_p(B)\ge r-1-s.
```

For \(H_{2,v}\), \(v_p(\ell)=s\), and

```math
B=\frac {va}\ell\binom{va+\ell-1}{\ell-1}
```

gives the same bound.  Since

```math
A^2-B^2=B^2(Q^2-1),
```

equation (5) yields

```math
v_p(A^2-B^2)\ge2(r-1-s)+
\begin{cases}
3s+2,&p=2,3,\\
3s+3,&p\ge5,
\end{cases}
\ge2r.
\qquad\text{(6)}
```

If \(s\ge r-1\), equation (5) alone is at least \(2r\).  The coefficient
with \(\ell=0\) has \(A=B=1\).  Thus every coefficient of \(X^{p\ell}\)
transfers modulo \(p^{2r}\), while (3) kills all remaining coefficients.
This proves Theorem 1.

## 5. Gaussian specialization

Set

```math
\mathcal A_N^{(i)}=\mathcal A_N(i),
\qquad
\mathcal B_N^{u,v,(i)}=\mathcal B_N^{u,v}(i).
```

Equations (1)--(2) imply, for either family \(\mathcal F\),

```math
\mathcal F_{np^r}(i)\equiv
\begin{cases}
\mathcal F_{n2^{r-1}}(-1),&p=2,\\
\mathcal F_{np^{r-1}}(i),&p\equiv1\pmod4,\\
\overline{\mathcal F_{np^{r-1}}(i)},&p\equiv3\pmod4
\end{cases}
\pmod {p^{2r}}.
\qquad\text{(7)}
```

The odd-prime cases are the split/inert Frobenius dichotomy in
\(\mathbb Z[i]\).  The binary case is a ramified cross-twist, not a
Frobenius automorphism.

## 6. Literature boundary

The Apéry polynomials \(\mathcal A_N(X)\) are classical.  Deutsch and
Sagan prove the untwisted one-step cubic congruence for the generalized
family containing A005259, and Straub proves broad multivariate
supercongruences using the same termwise valuation and scaling mechanism:

- E. Deutsch and B. Sagan,
  [*Congruences for Catalan and Motzkin numbers and related sequences*](https://users.math.msu.edu/users/sagan/papers/old/ccm.pdf),
  especially Theorem 5.10;
- A. Straub,
  [*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854);
- Z.-W. Sun,
  [*On sums of Apéry polynomials and related congruences*](https://arxiv.org/abs/1101.1946).

The contribution of this note is organizational: it spells out the
coefficientwise \(X\mapsto X^p\) consequence, includes the ramified binary
case, and applies the same proof to the positive two-parameter A333592
family.  It should be treated as a transparent corollary of classical
machinery unless a specialist priority check shows otherwise.

## 7. Exact checks

The checker verifies both base polynomial congruences and all three Gaussian
local behaviors at \(p=2,3,5,7,11\), through three adjacent levels.  It
also tests \(1\le u,v\le3\) in the generalized A333592 family and records
equality witnesses showing that the coefficientwise exponent \(2r\) is
sharp in the tested range.

Run:

```text
python verification/related/verify_quadratic_gaussian_queue.py
```
