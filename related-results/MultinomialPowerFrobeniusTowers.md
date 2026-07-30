# Multinomial-power Frobenius towers

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

This note proves Peter Bala's supercongruence on
[OEIS A141057](https://oeis.org/A141057) and strengthens it in two ways:

1. the three-part cubic sum is placed in a family with any number of parts
   and any exponent at least three; and
2. the scalar congruence is lifted coefficientwise to a multivariate
   Frobenius congruence.

The mechanism is the same carry-and-transfer budget used in the
[A183068 proof](../PROOF.md): missed residue classes acquire enough
multinomial carries to vanish, while the classes divisible by the prime
rescale to the preceding level.

## 1. The family

For integers $d\geq2$, $q\geq3$, and $N\geq0$, define

```math
\mathcal P_{d,q,N}(X_1,\ldots,X_d)
=
\sum_{\substack{b_1+\cdots+b_d=N\\b_i\geq0}}
\binom{N}{b_1,\ldots,b_d}^{q}
X_1^{b_1}\cdots X_d^{b_d}.
\tag{1}
```

Its scalar specialization is

```math
A_{d,q}(N)=\mathcal P_{d,q,N}(1,\ldots,1).
\tag{2}
```

### Theorem 1 (multinomial-power Frobenius tower)

Let $n,r\geq1$. If $p\geq5$ is prime and $q\geq3$, then

```math
\mathcal P_{d,q,np^r}(X_1,\ldots,X_d)
\equiv
\mathcal P_{d,q,np^{r-1}}(X_1^p,\ldots,X_d^p)
\pmod {p^{3r}}.
\tag{3}
```

- The same conclusion holds for $p=3$ when $3\mid q$.
- It also holds for $p=2$ when $4\mid q$.

The congruence in (3) is coefficientwise in
$\mathbb Z[X_1,\ldots,X_d]$.

Consequently,

```math
A_{d,q}(np^r)\equiv A_{d,q}(np^{r-1})\pmod {p^{3r}}
\tag{4}
```

under the same hypotheses.

## 2. Carry depth for one multinomial

Write

```math
M(\mathbf b)=
\binom{b_1+\cdots+b_d}{b_1,\ldots,b_d}.
```

### Lemma 2 (one carry at every missed level)

Suppose $p^t\mid b_1+\cdots+b_d$, and let

```math
s=\min_{b_i>0}v_p(b_i)<t.
```

Then

```math
v_p(M(\mathbf b))\geq t-s.
\tag{5}
```

#### Proof

Legendre's formula gives

```math
v_p(M(\mathbf b))
=
\sum_{j\geq1}
\left(
\left\lfloor\frac{\sum_i b_i}{p^j}\right\rfloor
-\sum_i\left\lfloor\frac{b_i}{p^j}\right\rfloor
\right).
\tag{6}
```

For every $s<j\leq t$, the first fraction in (6) is an integer.
At least one $b_i/p^j$ has nonzero fractional part. Since the sum of
all those fractional parts is itself an integer, it is at least one.
Thus every one of the $t-s$ indicated levels contributes at least one
to (6).

## 3. Adjacent scaling

The multinomial form of the
Ljunggren--Jacobsthal--Kazandzidis congruence used in
[Lemma 2 of the A183068 proof](../PROOF.md#3-multinomial-scaling) says
that

```math
Q_p(\mathbf c):=\frac{M(p\mathbf c)}{M(\mathbf c)}
\equiv1\pmod {p^{3(s+1)-\epsilon_p}},
\tag{7}
```

where $s=\min_{c_i>0}v_p(c_i)$ and

```math
\epsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\geq5.
\end{cases}
```

Zero components simply contribute trivial binomial factors.

### Lemma 3 (powered transfer)

Suppose $\sum_i c_i=np^{r-1}$. Under any of the three hypotheses in
Theorem 1,

```math
M(p\mathbf c)^q\equiv M(\mathbf c)^q\pmod {p^{3r}}.
\tag{8}
```

#### Proof for $p\geq5$

If $s<r-1$, Lemma 2 gives

```math
v_p(M(\mathbf c))\geq r-1-s.
```

By (7),

```math
\begin{aligned}
v_p\!\left(M(p\mathbf c)^q-M(\mathbf c)^q\right)
&\geq q(r-1-s)+3(s+1)\\
&=3r+(q-3)(r-1-s)\\
&\geq3r.
\end{aligned}
\tag{9}
```

If $s\geq r-1$, equation (7) alone supplies
$3(s+1)\geq3r$. The cases with only one positive component are
identities.

#### The prime $3$

Now (7) loses one power, but $3\mid q$ restores it. Indeed, for
$Q\equiv1\pmod3$,

```math
v_3(Q^q-1)\geq v_3(Q-1)+v_3(q).
\tag{10}
```

Since $v_3(q)\geq1$, the same calculation as (9) applies.

#### The prime $2$

If $Q$ is odd and $4\mid q$, the binary lifting-the-exponent identity
gives

```math
v_2(Q^q-1)
=v_2(Q-1)+v_2(Q+1)+v_2(q)-1.
\tag{11}
```

Because one of $Q-1,Q+1$ is divisible by $4$, (11) restores at
least the two powers lost in (7). The calculation in (9) again gives
$3r$.

## 4. Proof of Theorem 1

Set $N=np^r$. Consider the coefficient of
$X_1^{b_1}\cdots X_d^{b_d}$ in the left side of (3).

If the $b_i$ are not all divisible by $p$, their minimum valuation is
zero. Lemma 2 with $t=r$ yields

```math
v_p(M(\mathbf b)^q)\geq qr\geq3r.
\tag{12}
```

That coefficient therefore vanishes modulo $p^{3r}$.

Otherwise write $\mathbf b=p\mathbf c$. Lemma 3 replaces its coefficient
by $M(\mathbf c)^q$ modulo $p^{3r}$, and its monomial is

```math
X_1^{pc_1}\cdots X_d^{pc_d}
=(X_1^p)^{c_1}\cdots(X_d^p)^{c_d}.
```

These are exactly the coefficients and monomials on the right side of
(3). This proves the coefficientwise congruence. Setting every variable
equal to one proves (4).

## 5. A141057

The OEIS formula is

```math
a(N)=
\sum_{b_1+b_2+b_3=N}
\binom{N}{b_1,b_2,b_3}^{3}.
\tag{13}
```

Thus $a(N)=A_{3,3}(N)$. Theorem 1 proves Bala's stated conjecture
for every prime $p\geq5$:

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{3r}}.
\tag{14}
```

It also adds the previously unstated prime $p=3$. The binary analogue
does not hold: for $n=1,r=2$,

```math
a(4)-a(2)=6192,\qquad v_2(6192)=4<6.
\tag{15}
```

The first values produced by (13) are

```text
1, 3, 27, 381, 6219, 111753, 2151549, 43497891,
```

matching A141057.

## 6. Cyclotomic and Gaussian specializations

Equation (3) is stronger than the scalar theorem. For roots of unity
$\zeta_1,\ldots,\zeta_d$, it gives

```math
\mathcal P_{d,q,np^r}(\boldsymbol\zeta)
\equiv
\mathcal P_{d,q,np^{r-1}}(\boldsymbol\zeta^{\,p})
\pmod {p^{3r}}.
\tag{16}
```

For fourth roots of unity this is a congruence in $\mathbb Z[i]$:
primes $p\equiv1\pmod4$ preserve the twists, while primes
$p\equiv3\pmod4$ conjugate them. This is the natural Gaussian extension;
it is a Frobenius-twisted theorem, not a claim that rational primes and
Gaussian prime elements are interchangeable.

## 7. Source boundary

- [A141057](https://oeis.org/A141057) states (14) as a conjecture for
  $p\geq5$.
- The scaling input is classical; references and the small-prime
  qualifications are recorded in the
  [A183068 proof](../PROOF.md#3-multinomial-scaling).
- Zhi-Wei Sun's
  [*p-adic valuations of some sums of multinomial coefficients*](https://arxiv.org/abs/0910.3892)
  concerns different multinomial sums and valuation questions.

A preliminary exact-formula search did not locate Theorem 1 or the A141057
specialization in a publication. That negative search is not a priority
certificate. The mathematical proof and the literature-priority claim both
require independent review.

## 8. Verification

Run

```text
python verification/related/verify_multinomial_power_towers.py
```

The checker uses exact integers. It verifies the OEIS initial values,
coefficientwise discard and transfer at all three prime regimes, scalar
towers, the $p=3$ strengthening, and the explicit binary counterexample.
