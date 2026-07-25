# Landau fiber depth and termwise supercongruences

**Status:** unchecked research draft, 2026-07-25.

This note extracts the reusable mechanism behind the proof of the
Hanna--Bala A183068 supercongruence.  The ingredients are classical:
Landau's step function counts carries and a
Ljunggren--Jacobsthal--Kazandzidis congruence controls the effect of scaling
all entries of a multinomial coefficient by a prime.  The synthesis below is
a simple criterion that makes the interaction, including the losses at
$p=2,3$, explicit.

The criterion proves two infinite families:

1. a quadratic all-prime family containing A183068; and
2. a cubic all-prime family with no exceptional primes.

The proof should be independently checked before either family is claimed as
new.  A preliminary search found the ingredients and substantially broader
$p$-adic frameworks, but not these exact statements.

## 1. Homogeneous multinomial sums

For each $a$, let

$$
B_{a,j}(N,k)=\alpha_{a,j}N+\beta_{a,j}k
$$

be integer linear forms, nonnegative in the summation range
$0\leq k\leq N$, and put

$$
T_a(N,k)=\sum_j B_{a,j}(N,k).
$$

Consider the integer summand

$$
F(N,k)=
\prod_a
\binom{T_a(N,k)}
      {B_{a,1}(N,k),\ldots,B_{a,m_a}(N,k)}
$$

and

$$
A(N)=\sum_{k=0}^N F(N,k).
$$

Assume that one of the bottom entries is $k$.  This harmless-looking
condition makes the minimum valuation of the scaled entries exactly
$v_p(k)$ whenever $v_p(k)<v_p(N)$.

Define the one-dimensional Landau fiber

$$
\Lambda(y)=
\sum_a\left(
\left\lfloor T_a(0,y)\right\rfloor
-\sum_j\left\lfloor B_{a,j}(0,y)\right\rfloor
\right),
\qquad 0<y<1.
\tag{1}
$$

Negative $k$-coefficients are allowed.  In particular
$\lfloor-y\rfloor=-1$ for $0<y<1$.  The false shortcut
"$\Lambda(y)=0$ near $0$" applies only when all coefficients on the
fiber are nonnegative.

Let the **fiber depth** be the largest integer $d$ such that

$$
\Lambda(y)\geq d\qquad(0<y<1).
\tag{2}
$$

Only $d\leq3$ is relevant to the elementary transfer theorem below,
because the available multinomial scaling congruence has cubic depth.

## 2. Landau depth is termwise vanishing depth

### Lemma 1

Let $p^t\mid N$ and $s=v_p(k)<t$.  Then

$$
v_p(F(N,k))\geq d(t-s).
\tag{3}
$$

More precisely, the contribution of the $p^i$-level, for
$s<i\leq t$, is

$$
\Lambda\!\left(\left\{\frac{k}{p^i}\right\}\right).
\tag{4}
$$

#### Proof

Legendre's formula writes the valuation of each multinomial as a sum of
floor differences.  At level $p^i$, $N/p^i$ is an integer.  Splitting
$k/p^i$ into its integer and fractional parts, all integer contributions
cancel because each top entry is the sum of its bottom entries.  What
remains is exactly (4).  There are $t-s$ such levels, and each is at
least $d$.  $\square$

For $p=2$, the first active level always has fractional part $1/2$.
Thus

$$
\Lambda(1/2)\geq d+c
\quad\Longrightarrow\quad
v_2(F(N,k))\geq d(t-s)+c.
\tag{5}
$$

The analogous statement at $p=3$ uses both residues $1/3$ and $2/3$.

## 3. The transfer budget

Set

$$
\varepsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\geq5.
\end{cases}
\tag{6}
$$

The standard multinomial scaling congruence says that, if $s$ is the
minimum $p$-adic valuation of the positive bottom entries, then

$$
\frac{
\binom{pT}{pB_1,\ldots,pB_m}
}{
\binom{T}{B_1,\ldots,B_m}
}
\equiv1\pmod {p^{\,3(s+1)-\varepsilon_p}}.
\tag{7}
$$

The $p=2$ statement has a possible sign in its strongest source form.
At $s\geq1$ the exceptional parity pattern cannot occur; at $s=0$
the modulus in (7) is $2$, where $1\equiv-1$.  Hence (7) is valid in
the form needed here.  Products of multinomials inherit the same lower
bound.

For $1\leq d\leq3$, define the small-prime deficit

$$
c_p(d)=\max(0,d+\varepsilon_p-3).
\tag{8}
$$

The values are

| depth $d$ | $c_2(d)$ | $c_3(d)$ | $c_p(d),\ p\geq5$ |
| ---: | ---: | ---: | ---: |
| 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 3 | 2 | 1 | 0 |

### Theorem 2: generic termwise transfer

Under the hypotheses of Section 1, if the fiber depth is at least
$d\leq3$, then for every prime $p$ and $n,r\geq1$,

$$
A(np^r)\equiv A(np^{r-1})
\pmod {p^{\,dr-c_p(d)}}.
\tag{9}
$$

#### Proof

In $A(np^r)$, terms with $p\nmid k$ have valuation at least $dr$ by
Lemma 1.

For $k=p\ell$, compare $F(np^r,p\ell)$ with
$F(np^{r-1},\ell)$, and put $s=v_p(\ell)$ when $\ell>0$.
If $s<r-1$, Lemma 1 supplies $d(r-1-s)$ powers from the latter
summand, while (7) supplies $3(s+1)-\varepsilon_p$ powers from the
scaling error.  Their sum is

$$
dr+(3-d)(s+1)-\varepsilon_p
\geq dr-c_p(d).
\tag{10}
$$

If $\ell=0$, or if $s\geq r-1$, every positive bottom entry is
divisible by $p^{r-1}$, so (7) alone gives
$3r-\varepsilon_p$, again at least $dr-c_p(d)$.  Summing the
termwise congruences proves (9).
$\square$

### Theorem 3: compensated termwise transfer

Fix $p$.  Suppose in addition that

$$
\Lambda(a/p)\geq d+c_p(d)
\quad(1\leq a<p)
\tag{11}
$$

and

$$
p^{c_p(d)}\mid F(N,k)
\quad(N>0,\ 0\leq k\leq N).
\tag{12}
$$

Then the full congruence holds:

$$
A(np^r)\equiv A(np^{r-1})\pmod {p^{dr}}.
\tag{13}
$$

#### Proof

When $s<r-1$, the first active Landau level has fractional part
$a/p$, so (11) contributes the missing $c_p(d)$ powers in (10).
When $s\geq r-1$, (12) contributes them to the scaling difference.
The same residue bonus applies to the discarded $p\nmid k$ terms.
$\square$

For depth $2$, Theorem 3 says that the entire $p=2$ problem is reduced
to

$$
\Lambda(1/2)\geq3
\quad\text{and}\quad
2\mid F(N,k).
\tag{14}
$$

This is exactly the structure of the prime-2 endgame in the A183068
proof.

## 4. An explicit two-parameter family

Let $u,v$ be positive integers and define

$$
F_{u,v}(N,k)=
\frac{(uk+v(N-k))!}{k!^u(N-k)!^v}
\tag{15}
$$

and

$$
A_{u,v}(N)=\sum_{k=0}^N F_{u,v}(N,k).
\tag{16}
$$

The summand is the multinomial coefficient with $u$ copies of $k$
and $v$ copies of $N-k$.  Notice the symmetry
$A_{u,v}=A_{v,u}$.

Its Landau fiber has the closed form

$$
\Lambda_{u,v}(y)
=v+\lfloor(u-v)y\rfloor.
\tag{17}
$$

Consequently,

$$
\min_{0<y<1}\Lambda_{u,v}(y)=\min(u,v)
\tag{18}
$$

and

$$
\Lambda_{u,v}(1/2)=\left\lfloor\frac{u+v}{2}\right\rfloor.
\tag{19}
$$

### Corollary 4: an all-prime quadratic family

If

$$
u,v\geq2,\qquad u+v\geq6,
\tag{20}
$$

then, for every prime $p$ and $n,r\geq1$,

$$
A_{u,v}(np^r)\equiv A_{u,v}(np^{r-1})
\pmod {p^{2r}}.
\tag{21}
$$

#### Proof

Equations (18)--(20) give depth $2$ and
$\Lambda_{u,v}(1/2)\geq3$.  Every $F_{u,v}(N,k)$, with $N>0$,
is even: at least one of $k,N-k$ is positive and occurs at least
twice, so a factor $\binom{2b}{b}$ with $b>0$ splits off.  Apply
Theorems 2 and 3.  $\square$

The Hanna--Bala sequence A183068 is the case

$$
(u,v)=(4,2).
\tag{22}
$$

Thus its all-prime $p^{2r}$ theorem is one boundary point of an
infinite family rather than an isolated congruence.

### Corollary 5: an all-prime cubic family

If

$$
u,v\geq4,\qquad u+v\geq10,
\tag{23}
$$

then, for every prime $p$ and $n,r\geq1$,

$$
A_{u,v}(np^r)\equiv A_{u,v}(np^{r-1})
\pmod {p^{3r}}.
\tag{24}
$$

#### Proof

The depth is at least $3$.  At $p=3$,

$$
\min\bigl(\Lambda_{u,v}(1/3),\Lambda_{u,v}(2/3)\bigr)\geq4,
$$

and at $p=2$, (19) and (23) give
$\Lambda_{u,v}(1/2)\geq5$.

It remains to verify the divisibility in (12).  For $b>0$, the equal-part
multinomial

$$
M_m(b)=\frac{(mb)!}{b!^m}
$$

is divisible by $3$ for $m\geq3$ and by $4$ for $m\geq4$.
For the first statement, $M_3(b)$ has positive 3-adic valuation by
Legendre's digit-sum formula and splits off from $M_m(b)$.
For the second,

$$
M_4(b)=\binom{4b}{2b}\binom{2b}{b}^2
$$

is divisible by $4$, and it splits off from $M_m(b)$.
At least one of $k,N-k$ is positive, so
$3\mid F_{u,v}(N,k)$ and $4\mid F_{u,v}(N,k)$.
Theorem 3 now restores the one lost power at $p=3$ and the two lost
powers at $p=2$.  $\square$

## 5. What this organizes

The Landau fiber gives a fast, exact screen:

| sequence/summand | fiber behavior | what the termwise criterion sees |
| --- | --- | --- |
| Franel $\sum_k\binom Nk^q$ | $\Lambda=q$ | depth $q$, capped at cubic by scaling |
| Domb summand $\binom Nk^2\binom{2k}k\binom{2N-2k}{N-k}$ | depth $3$, value $4$ at $1/2$ | cubic away from small-prime transfer losses |
| A183068 | $2+\lfloor2y\rfloor$ | depth $2$, binary bonus $3$ |
| Apéry $\zeta(2)$ summand | depth $2$, no binary bonus | odd-prime quadratic congruence directly |
| Apéry $\zeta(3)$ summand | constant depth $2$ | cubic results require cancellation or additional structure |

The mechanism is therefore:

$$
\boxed{\text{Landau carries}}
\quad+\quad
\boxed{\text{multinomial scaling}}
\quad\Longrightarrow\quad
\boxed{\text{termwise supercongruence}}.
\tag{25}
$$

It is powerful when each summand is a balanced product of multinomials.
It is not a universal explanation of Apéry-like supercongruences:

- exponential factors create Fermat-quotient errors under scaling;
- borderline depth can require cancellation between summands;
- constant-term sequences outside this factorial-ratio class are naturally
  handled by Dwork congruences and Frobenius lifts.

This gives a useful division of labor.  Landau depth predicts which terms
vanish.  Kazandzidis-type congruences transfer the surviving strata.  Dwork
theory is needed when the congruence lives in aggregate cancellation rather
than individual terms.

## 6. Relation to the literature

This note does **not** claim to invent the ingredients.

- Landau's floor criterion is the classical integrality test for factorial
  ratios.
- Delaygue uses Landau functions to obtain $p$-adic valuation bounds for
  broad families of Apéry-like factorial-ratio sums.
- Osburn--Sahu--Straub use termwise valuation plus
  Kazandzidis-type scaling in supercongruence proofs, including delicate
  treatment of $p=2,3$.
- Gorodetsky's constant-term approach and Dwork-type results reach sequences
  where termwise depth is not the full explanation.
- Alinquant--Osburn explicitly note that no general framework currently
  explains all 15 sporadic supercongruences.  The criterion here should not
  be presented as such a framework: it covers the balanced termwise
  multinomial subclass and diagnoses when that method stops.

The candidate contribution here is narrower: equations (8)--(13) expose a
computable small-prime deficit and compensation rule, while Corollaries 4 and
5 package it into explicit infinite all-prime families.  A proper priority
search is still required.

Primary references:

1. E. Delaygue, *Arithmetic properties of Apéry-like numbers*,
   <https://arxiv.org/abs/1310.4131>.
2. R. Osburn, B. Sahu, and A. Straub, *Supercongruences for sporadic
   sequences*, <https://arxiv.org/abs/1312.2195>.
3. O. Gorodetsky, *New representations for all sporadic Apéry-like
   sequences, with applications to congruences*,
   <https://arxiv.org/abs/2102.11839>.
4. E. Delaygue, T. Rivoal, and J. Roques, *On Dwork's $p$-adic formal
   congruences theorem and hypergeometric mirror maps*,
   <https://arxiv.org/abs/1309.5902>.
5. B. Alinquant and R. Osburn, *On sporadic sequences*,
   <https://arxiv.org/abs/2312.07134>.

## 7. Exact checks

Run

```text
python verification/related/verify_landau_supercongruence.py
```

The script checks:

- formula (17), its minimum, and its value at $1/2$;
- the fibers of the Franel, Domb, and two Apéry summands;
- uniform divisibility of the equal-part multinomials;
- the quadratic family for every qualifying $2\leq u,v\leq6$, all
  $p\in\{2,3,5,7\}$, and $r\leq2$;
- the cubic family for every qualifying $4\leq u,v\leq7$, all
  $p\in\{2,3,5,7\}$, and $r\leq2$;
- the binary endgame modulo $4$.

These are exact integer checks.  They guard against algebraic and
small-prime mistakes but do not replace independent review of the proof.
