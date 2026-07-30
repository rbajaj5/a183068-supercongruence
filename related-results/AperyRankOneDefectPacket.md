# The Apéry enhanced-congruence packet

**Status:** complete algebraic reduction of five OEIS records to three
linear defect congruences; the three congruences remain open.

Five records in the Bala census are built from the two Apéry sequences

```math
\begin{aligned}
Z(n)&=\sum_{k=0}^{n}\binom nk^2\binom{n+k}{k}
&&\text{(A005258)},\\
W(n)&=\sum_{k=0}^{n}\binom nk^2\binom{n+k}{k}^2
&&\text{(A005259)}.
\end{aligned}
\tag{1}
```

They look like separate linear and nonlinear conjectures.  They are not.
After the classical cubic Apéry towers are removed, all five records ask
for the same three-component cancellation.  For primes $p\ge7$, the
surviving first defect is one-dimensional.

This note proves that reduction.  It does not prove the three remaining
defect congruences.

## 1. The four adjacent defects

Fix a prime $p\ge5$ and $r\ge1$.  Put

```math
N=p^r,\qquad M=p^{r-1},
\tag{2}
```

and define

```math
\begin{aligned}
\alpha_r&=Z(N)-Z(M),&
\beta_r&=Z(N-1)-Z(M-1),\\
\gamma_r&=W(N)-W(M),&
\delta_r&=W(N-1)-W(M-1).
\end{aligned}
\tag{3}
```

The established Apéry baselines give

```math
\alpha_r,\beta_r,\gamma_r,\delta_r
\equiv0\pmod {p^{3r}}.
\tag{4}
```

The enhanced exponent appearing on the five source records is

```math
L_r=
\begin{cases}
5,&r=1,\\
3r+3,&r\ge2.
\end{cases}
\tag{5}
```

Consider the following three relations:

```math
\begin{aligned}
R_{1,r}&:\quad \alpha_r+\beta_r\equiv0\pmod {p^{L_r}},\\
R_{2,r}&:\quad 5\gamma_r-14\alpha_r\equiv0\pmod {p^{L_r}},\\
R_{3,r}&:\quad 5\delta_r-2\beta_r\equiv0\pmod {p^{L_r}}.
\end{aligned}
\tag{6}
```

For $p\ge7$, division by $5$ is legitimate, and (6) says that the
four-coordinate defect is proportional to

```math
(\alpha_r,\beta_r,\gamma_r,\delta_r)
\sim
(5,-5,14,-2)
\pmod {p^{L_r}}.
\tag{7}
```

At $p=5$, the integral relations (6), rather than the divided vector
form (7), are the correct statement.

## 2. The exact source reduction

### Theorem 1

Assume the cubic baselines (4).  For $p\ge5$, the enhanced
supercongruence claims on A352655, A357506, A357567, A357956, and A357959,
including the nonlinear companion claims printed on A357567 and A357959,
all follow from (6).

Conversely, the three linear source claims on A352655, A357567, and
A357956 are exactly $R_{1,r}$, $R_{2,r}$, and $R_{3,r}$.
Consequently the complete five-record packet is equivalent to the three
relations (6), apart from the isolated $p=3$ first-level assertion on
A357506.

#### Proof

The A352655 sequence is

```math
S(n)=\frac{Z(n)+Z(n-1)}2.
\tag{8}
```

Since $2$ is a unit modulo $p^{L_r}$,

```math
S(N)-S(M)=\frac{\alpha_r+\beta_r}{2}.
\tag{9}
```

Thus its conjecture is exactly $R_{1,r}$.

The A357567 and A357956 sequences are

```math
5W(n)-14Z(n),
\qquad
5W(n)-2Z(n),
\tag{10}
```

the second evaluated at $n=N-1$.  Their adjacent differences are
exactly the left sides of $R_{2,r}$ and $R_{3,r}$.

The remaining linear A357959 sequence is

```math
5W(n-1)+2Z(n).
\tag{11}
```

Its adjacent difference satisfies the exact identity

```math
5\delta_r+2\alpha_r
=
(5\delta_r-2\beta_r)+2(\alpha_r+\beta_r).
\tag{12}
```

Hence $R_{1,r}$ and $R_{3,r}$ imply the A357959 claim.

It remains to show that the nonlinear records add no new defect direction.
Write

```math
x=Z(M),\qquad y=Z(M-1).
```

At $r=1$, $(x,y)=(3,1)$.  At $r\ge2$, the cubic baselines imply

```math
x\equiv3,\qquad y\equiv1\pmod {p^3}.
\tag{13}
```

Taylor expansion of the A357506 product gives

```math
(x+\alpha_r)^3(y+\beta_r)-x^3y
\equiv
27(\alpha_r+\beta_r)
\pmod {p^{L_r}}.
\tag{14}
```

Indeed, the error in replacing the two linear coefficients by $27$
has valuation at least $3r+3$, while every term containing two defects
has valuation at least $6r$.  Both bounds reach $L_r$.  This proves
the A357506 tower from $R_{1,r}$.

For the nonlinear companion on A357567, set

```math
P(u,x)=3^{42}u^{25}-5^{25}x^{42}.
\tag{15}
```

The lower point is congruent to $(5,3)$ modulo $p^3$, and

```math
\nabla P(5,3)\mathbin{\cdot}(\gamma_r,\alpha_r)
=
3^{42}5^{25}(5\gamma_r-14\alpha_r).
\tag{16}
```

The same Taylor estimate as in (14) shows that $R_{2,r}$ implies the
claimed congruence for $P(W(n),Z(n))$.  This remains valid at $p=5$;
no division by $5$ was used.

Finally, the nonlinear A357959 companion is

```math
Q(v,x)=v^5x^6.
\tag{17}
```

At the lower point $(v,x)\equiv(1,3)\pmod {p^3}$,

```math
\nabla Q(1,3)\mathbin{\cdot}(\delta_r,\alpha_r)
=
3^6(5\delta_r+2\alpha_r).
\tag{18}
```

Equations (12) and (18), with the same quadratic-error bound, prove its
congruence.  This establishes every implication.  The converse follows
from (9) and (10). $\square$

The exceptional first-level statement on A357506 at $p=3$ is a finite
boundary check:

```math
Z(3)^3Z(2)-27
=
147^3\mathbin{\cdot}19-27
=
3^5\mathbin{\cdot}248370.
\tag{19}
```

## 3. A polynomial closure principle

The previous calculations are instances of one reusable fact.

### Theorem 2

Let $\mathbf a_r\in\mathbb Z^d$ satisfy

```math
\mathbf a_r-\mathbf a_{r-1}
\equiv0\pmod {p^{3r}},
\qquad
\mathbf a_{r-1}\equiv\mathbf a_0\pmod {p^3}
\quad(r\ge2).
\tag{20}
```

Let $L_r$ be (5), and let $F\in\mathbb Z[X_1,\ldots,X_d]$.  Then

```math
F(\mathbf a_r)-F(\mathbf a_{r-1})
\equiv
\nabla F(\mathbf a_0)\mathbin{\cdot}
(\mathbf a_r-\mathbf a_{r-1})
\pmod {p^{L_r}}.
\tag{21}
```

For $r=1$, assume simply that $\mathbf a_{r-1}=\mathbf a_0$.

#### Proof

The linear Taylor coefficients at $\mathbf a_{r-1}$ differ from those at
$\mathbf a_0$ by multiples of $p^3$.  Multiplying by a first
difference supplies $p^{3r+3}$.  Every Taylor monomial of degree at least
two in the first differences supplies $p^{6r}$.  For $r\ge2$,

```math
3r+3\le6r,
```

and for $r=1$ the coefficient-replacement error vanishes while
$6\ge L_1=5$. $\square$

Thus enhanced polynomial combinations are selected by a tangent-space
condition: their gradients annihilate the surviving defect direction.
This explains the otherwise opaque exponents $3,25,42,5,6$ in the two
nonlinear OEIS companions.

## 4. What remains to prove

The five records no longer constitute five independent proof searches.
The exact remaining target is (6).

There are two natural proof routes:

1. derive a common first-order Cartier or Dwork defect for the two Apéry
   diagonals and their shifted companions; or
2. expand the four Apéry sums blockwise through the first nonzero
   $p$-adic defect and prove that the coefficient vector satisfies (6).

The second route is closer to the elementary calculations already used
elsewhere in this repository.  The first may explain why the defect packet
has rank one for $p\ne5$.

## 5. Source boundary

- [A352655](https://oeis.org/A352655) supplies $R_1$.
- [A357567](https://oeis.org/A357567) supplies $R_2$ and its nonlinear
  companion.
- [A357956](https://oeis.org/A357956) supplies $R_3$.
- [A357506](https://oeis.org/A357506) is the product consequence of
  $R_1$, plus the finite $p=3$ boundary.
- [A357959](https://oeis.org/A357959) follows from $R_1$ and $R_3$,
  as does its nonlinear companion.

No literature-priority claim is made for Theorem 2.  It is an elementary
closure lemma used to identify the exact unresolved arithmetic.

## 6. Verification

Run:

```text
python verification/related/verify_apery_rank_one_defect.py
```

The checker evaluates the two Apéry sums exactly, verifies the three
relations and all seven source formulations on a finite prime-power grid,
checks the rank-one form where $5$ is invertible, and verifies the
isolated $p=3$ boundary.  These computations are evidence for (6), not
a proof of it.
