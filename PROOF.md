# A readable proof of the A183068 supercongruence

> **Result.** The congruence conjectured by Peter Bala for Paul D. Hanna's
> sequence A183068 holds for every prime, including the exceptional prime
> $2$. The proof is termwise: some summands vanish, and the others rescale to
> the preceding level.

## The theorem

The [OEIS entry A183068](https://oeis.org/A183068) gives

$$
a(n)=\sum_{k=0}^{n}\frac{(2n+2k)!}{k!^4(n-k)!^2}.
$$

For every prime $p$ and all positive integers $n,r$,

$$
\boxed{\;a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}.\;}
$$

## The proof in one screen

Set $N=np^r$ and call the $k$-th summand $F(N,k)$. Split the sum according
to whether $p$ divides $k$.

| Terms | What happens modulo $p^{2r}$ | Reason |
| --- | --- | --- |
| $p\nmid k$ | $F(N,k)$ vanishes | At each of the $r$ active base-$p$ digit levels, the multinomial addition forces at least two carries |
| $k=p\ell$ | $F(N,p\ell)$ becomes $F(N/p,\ell)$ | A Ljunggren--Jacobsthal--Kazandzidis scaling congruence controls the error |
| $p=2,\ r=1$ | The apparent one-power deficit disappears | A repeated multinomial part contributes an even central binomial coefficient |

Therefore the first group contributes zero and the second group is exactly the
sum defining $a(np^{r-1})$. That is the whole argument. The detailed proof
below verifies the carry count, the scaling exponent, and the binary edge case.

## Why multinomial carries appear

The summand can be rewritten as one multinomial coefficient:

$$
F(N,k)=\frac{(2N+2k)!}{k!^4(N-k)!^2}
=\binom{2N+2k}{k,k,k,k,N-k,N-k}.
$$

Consequently $F(N,k)$ is an integer. Legendre's formula computes its
$p$-adic valuation by counting the base-$p$ carries needed to add the six
bottom entries. When $p^r$ divides $N$ but $p$ does not divide $k$, each of
the first $r$ digit levels forces at least two carries. This gives the required
$p^{2r}$ before any cancellation between summands is considered.

## Notation

- $v_p(x)$ is the exponent of $p$ in the integer $x$.
- $N=np^r$ is the upper argument at the level being proved.
- $N'=N/p=np^{r-1}$ is the preceding level.
- $s$ denotes the smallest relevant $p$-adic valuation of a component.

## Detailed proof

### 1. Multinomial setup

Using the summand $F$ displayed above,

$$
a(N)=\sum_{k=0}^{N}F(N,k).
$$

### 2. Terms whose index is not divisible by $p$

#### Lemma 1

Suppose $p^t\mid N$, $0\le k\le N$, and $s=v_p(k)<t$.  Then

$$
v_p(F(N,k))\ge2(t-s).
$$

If $p=2$, the stronger bound

$$
v_2(F(N,k))\ge2(t-s)+1
$$

holds.

#### Proof

Legendre's formula expresses $v_p(F(N,k))$ as the sum, over $i\ge1$,
of

$$
\lambda_i=
\left\lfloor\frac{2N+2k}{p^i}\right\rfloor
-4\left\lfloor\frac{k}{p^i}\right\rfloor
-2\left\lfloor\frac{N-k}{p^i}\right\rfloor.
$$

Every $\lambda_i$ is nonnegative: it is the carry contribution at the
$p^i$ level for the multinomial coefficient displayed above.

Fix $s<i\le t$, put $q=p^i$, and write

$$
N=qM,\qquad k=qa+u,\qquad0<u<q.
$$

Then

$$
N-k=q(M-a-1)+(q-u),
$$

and direct substitution in the Legendre formula gives

$$
\lambda_i=2+\left\lfloor\frac{2u}{q}\right\rfloor\ge2.
$$

There are $t-s$ such indices, proving the first bound in Lemma 1.

For $p=2$ and $i=s+1$, the residue is $u=2^s$, so
$\lfloor2u/2^{s+1}\rfloor=1$.  This one level contributes $3$
instead of $2$, proving the stronger binary bound. $\square$

In particular, if $p^r\mid N$ and $p\nmid k$, then

$$
F(N,k)\equiv0\pmod {p^{2r}}.
$$

### 3. Multinomial scaling

We use the classical Ljunggren--Jacobsthal--Kazandzidis binomial
congruence in the following standard multinomial form.

#### Lemma 2 (multinomial scaling)

Let $\mathbf b=(b_1,\ldots,b_m)$ be nonnegative integers with positive
sum.  Suppose every positive $b_i$ is divisible by $p^s$.  Then, in
the $p$-adic units,

$$
\frac{\displaystyle
 \binom{p\sum b_i}{pb_1,\ldots,pb_m}}
{\displaystyle
 \binom{\sum b_i}{b_1,\ldots,b_m}}
\equiv1\pmod {p^{\,3(s+1)-\epsilon_p}},
$$

where

$$
\epsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\ge5.
\end{cases}
$$

This follows by factoring each multinomial coefficient into binomial
coefficients and applying the prime-power form of the
Ljunggren--Jacobsthal congruence to every nontrivial factor.  Zero
components contribute factors equal to $1$.

For references, see G. S. Kazandzidis,
["Congruences on the binomial coefficients"](https://eudml.org/doc/238547)
(1968), and the discussion of the Jacobsthal refinement in Eric Rowland,
["Lucas' theorem modulo $p^2$"](https://ericrowland.github.io/papers/Lucas%27_theorem_modulo_p%5E2.pdf).
The prime-power quotient form, including the losses of one power at
$p=3$ and two at $p=2$, is recorded in Section 2 of Robert Osburn,
Brundaban Sahu and Armin Straub,
["Supercongruences for sporadic sequences"](https://arxiv.org/abs/1312.2195).

There is a small sign qualification at $p=2$ in their formulation: the
binomial quotient may be congruent to $\varepsilon\in\{1,-1\}$, rather
than always to $1$.  In the equal-index specialization used here, the
exceptional sign requires the lower scaled bottom entry $2^s b$ to be
odd.  This is impossible when $s\ge1$; when $s=0$, the modulus in
Lemma 2 is only $2$, and $-1\equiv1\pmod2$. Thus the flat
congruence to $1$ asserted in Lemma 2 is valid for every $s$.

The minimum-valuation hypothesis in Lemma 2 is intentional.  At $p=2$,
the superficially stronger bound obtained by replacing $3s$ with a sum
of the valuations of the binomial arguments is false in general.
Independent finite tests found the exponent in Lemma 2 sharp for each of
$p=2,3,5$.

### 4. Scaling an individual summand

#### Lemma 3

Let $N'=np^{r-1}$ and $0\le\ell\le N'$.  Then

$$
F(pN',p\ell)\equiv F(N',\ell)\pmod {p^{2r}}.
$$

#### Proof

Apply Lemma 2 to the six components

$$
\ell,\ell,\ell,\ell,N'-\ell,N'-\ell.
$$

Let $s$ be the minimum $p$-adic valuation among the positive
components displayed above. Because $p^{r-1}\mid N'$, either

$$
s<r-1
\quad\text{and then}\quad
s=v_p(\ell)=v_p(N'-\ell),
$$

or $s\ge r-1$.

First suppose $s<r-1$.  Lemma 1, applied to $F(N',\ell)$, gives

$$
v_p(F(N',\ell))\ge2(r-1-s).
$$

For $p=2$, it gives one additional power of $2$.  Lemma 2 says that
the scaling quotient minus $1$ has valuation at least
$3(s+1)-\epsilon_p$.  Hence

$$
v_p\bigl(F(pN',p\ell)-F(N',\ell)\bigr)\ge
\begin{cases}
[2(r-1-s)+1]+(3s+1)=2r+s,&p=2,\\
2(r-1-s)+(3s+2)=2r+s,&p=3,\\
2(r-1-s)+(3s+3)=2r+s+1,&p\ge5.
\end{cases}
$$

Every case is at least $2r$.

Now suppose $s\ge r-1$.  Lemma 2 alone supplies respectively

$$
3r-2,\qquad3r-1,\qquad3r
$$

powers for $p=2,3,$ and $p\ge5$.  These bounds are at least $2r$,
except potentially when $p=2,r=1$.

In that remaining case $F(N',\ell)$ is even.  Indeed, among the six
components, some positive component $b$ occurs at least twice:
take $b=\ell$ if $\ell>0$, and $b=N'$ otherwise.  Grouping two
copies first factors the multinomial coefficient as

$$
\binom{2b}{b}
\binom{2N'+2\ell}{2b,\ \text{the remaining components}}.
$$

The central binomial coefficient $\binom{2b}{b}$ is even for $b\ge1$.
The one power supplied by Lemma 2 therefore yields two powers in the
difference. This proves Lemma 3 in every case. $\square$

### 5. Assemble the sum

Set $N=np^r$. Split the summand expansion according to whether $p\mid k$:

$$
a(N)
=
\sum_{\substack{0\le k\le N\\p\nmid k}}F(N,k)
+
\sum_{\ell=0}^{N/p}F(N,p\ell).
$$

By Lemma 1's vanishing corollary, every term in the first sum is
$0\pmod {p^{2r}}$. Lemma 3
replaces every term in the second sum by $F(N/p,\ell)$ modulo
$p^{2r}$.  Therefore

$$
\begin{aligned}
a(np^r)
&\equiv
\sum_{\ell=0}^{np^{r-1}}F(np^{r-1},\ell)\\
&=a(np^{r-1})
\pmod {p^{2r}},
\end{aligned}
$$

This is the claimed congruence. $\square$

## Optional structural interpretation

The sequence also has the fixed-Laurent-polynomial representation

$$
a(n)=\operatorname{CT}_{w,x,y,z} P(w,x,y,z)^n,
$$

where

$$
P=
\frac{(1+w)^2}{w}\,
(1+y)^2(1+x)
\left(
1+
\frac{(1+y)^2(1+z)^2}{xy^2z}
\right).
$$

To verify this representation, extract successively the central coefficients giving
$\binom{2n}{n}$, $\binom nk^2$,
$\binom{2n+2k}{2k}$, and $\binom{2k}{k}$.  This representation
explains why a Dwork-type congruence is plausible, although it is not
needed for the proof above.

## Computational checks and provenance

After the proof was written, one exact computation rechecked the theorem in all
80 cases with $p\in\{2,3,5,7,11\}$, $r\in\{1,2\}$, and
$1\le n\le8$.  A separate audit expanded this to 105 cases, including
cases with $r=3$.  It also tested Lemmas 1--3 directly for
$p\in\{2,3,5\}$ through the stated small ranges, with no failures.
Exact Laurent-polynomial arithmetic verified the constant-term representation
for $n=1,2,3$.

The live OEIS record still labels the result as a conjecture. Exact-statement
searches did not locate an existing proof.  The proof method is directly
in the lineage of Osburn--Sahu--Straub's all-prime $p^{2r}$
supercongruences, including their delicate $p=2$ endgame.  Before
publication, priority should also be searched using the
${}_4F_3$ hypergeometric representation on the OEIS entry, not only
the A-number.
