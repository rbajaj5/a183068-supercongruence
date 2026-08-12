# Full cubic towers for the index-dependent companions

**Status:** complete proof for every prime $p\ge5$ and every level

## 1. The two surviving August families

Define

```math
V(N)=\sum_{k=0}^{N}
\binom{-N}{k}\binom Nk\binom{2k}{N}\binom{N+k}{k}
tag{1}
```

and, for a positive integer $c$,

```math
W_c(N)=\sum_{k=0}^{cN}
\binom{-N}{k}^2\binom{2k}{N}\binom{N+k}{k}.
tag{2}
```

The August mixed-binomial note recorded cubic evidence for these two
sign-opposite companions.  They are not covered by the fixed-slope theorem:
$\binom{2k}{N}$ and $\binom{N+k}{k}$ depend on the index in their upper
arguments.  Also, a unit-index summand generally has valuation only two,
so a termwise cubic proof is impossible.

### Theorem 1 (full companion towers)

For every prime $p\ge5$ and positive integers $n,c,r$,

```math
\boxed{V(np^r)\equiv V(np^{r-1})\pmod {p^{3r}}}
tag{3}
```

and

```math
\boxed{W_c(np^r)\equiv W_c(np^{r-1})\pmod {p^{3r}}.}
tag{4}
```

The missing power is an aggregate reciprocal-square cancellation.  At the
first level it is the half-residue identity in Section 3.  At every level it
is supplied by the parity-doubling block lemma in Section 6.

## 2. The scaled stratum at every level

For $k=pq$, every factor at $(pM,pq)$ is an adjacent scaling of the
corresponding factor at $(M,q)$.  For the negative binomial, oddness of $p$
and cancellation of the rational prefactor give

```math
\frac{\binom{-pM}{pq}}{\binom{-M}{q}}
=\frac{\binom{p(M+q)}{pq}}{\binom{M+q}{q}}.
tag{5}
```

The other three quotients are attached to

```math
\binom{pM}{pq},\qquad
\binom{2pq}{pM},\qquad
\binom{p(M+q)}{pq}.
```

The four lower-scale binomials are therefore

```math
\binom{-M}{q},\quad \binom Mq,\quad
\binom{2q}{M},\quad \binom{M+q}{q}.
```

### Theorem 2 (all-level scaled transfer)

Let $p\ge5$, $N=np^r$, $M=N/p$, and $q\ge0$.  Then

```math
\boxed{
v_N(pq)\equiv v_M(q)\pmod {p^{3r}},\qquad
w_N(pq)\equiv w_M(q)\pmod {p^{3r}}.
}
tag{6}
```

Here a binomial that is zero at one scale is zero at the other, so the
display includes the support boundary.

To prove the theorem, put $s=v_p(q)$ and first suppose $s<r-1$.  The
factors $\binom{-M}{q}$ and $\binom Mq$ each have valuation at least
$r-1-s$.  The finite summand contains one of each; the cutoff summand
contains two copies of the first.  Hence either lower summand has valuation
at least

```math
2(r-1-s).
tag{6a}
```

For each of the four adjacent quotients, the full
Jacobsthal--Kazandzidis modulus contains the factor

```math
p^3ab(a-b).
```

For example, the quotient attached to $\binom Mq$ has valuation bound

```math
3+v_p(M)+v_p(q)+v_p(M-q)=r+2s+2.
tag{6b}
```

The other three quotients have the same bound: their triples are
$(M+q,q,M)$, $(M,q,M-q)$, and $(2q,M,2q-M)$, respectively, and
$v_p(M\pm q)=v_p(2q-M)=s$.  A product of quantities congruent to one
modulo $p^{r+2s+2}$ is again congruent to one to that precision.  Combining
(6a) and (6b) gives

```math
2(r-1-s)+(r+2s+2)=3r.
```

If $s\ge r-1$, the same Jacobsthal modulus is already at least $3r$;
integrality of the lower summand finishes the proof.  The case $q=0$ is
an equality.  This proves (6).

Thus the scaled stratum transfers at full cubic precision.  It remains to
prove that the sum of indices prime to $p$ vanishes to the same precision.

## 3. The half-residue lemma

Put $h=(p-1)/2$.  In $\mathbb F_p$,

```math
\sum_{s=1}^{h}\frac1{s^2}
=\sum_{s=h+1}^{p-1}\frac1{s^2}=0.
tag{7}
```

Indeed, $s\mapsto p-s$ identifies the two sums, while their sum is
$\sum_{s\in\mathbb F_p^\times}s^{p-3}=0$ for $p\ge5$.

This elementary identity is exactly the aggregate cancellation absent from
a termwise valuation count.

## 4. Unit blocks for the cutoff family

Write a unit index uniquely as

```math
k=pq+s,qquad 1\le s\le p-1.
```

Modulo $p$, Lucas' theorem and

```math
\binom{-np}{k}
=(-1)^k\frac{np}{np+k}\binom{np+k}{k}
```

give

```math
\frac1p\binom{-np}{pq+s}
\equiv
(-1)^{q+s}\frac ns\binom{n+q}{q}.
tag{8}
```

The remaining factors satisfy

```math
\binom{np+pq+s}{pq+s}\equiv\binom{n+q}{q}pmod p
tag{9}
```

and

```math
\binom{2pq+2s}{np}
\equiv
\begin{cases}
\binom{2q}{n},&1\le s\le h,\\
\binom{2q+1}{n},&h<s<p
\end{cases}
\pmod p.
tag{10}
```

Consequently the complete $q$-block of unit terms in (2), divided by
$p^2$, is congruent to

```math
n^2\binom{n+q}{q}^3
\left(
\binom{2q}{n}\sum_{s=1}^{h}s^{-2}
+\binom{2q+1}{n}\sum_{s=h+1}^{p-1}s^{-2}
\right),
tag{11}
```

which vanishes by (7).  The range $0\le k\le cnp$ contains the complete
unit blocks $0\le q<cn$; the endpoint $k=cnp$ belongs to the scaled
stratum.  Hence all discarded terms in $W_c(np)$ sum to zero modulo $p^3$.
Together with (6), this proves the case $r=1$ of (4).

## 5. Unit blocks for the finite family

For $1\le s<p$, a second Lucas calculation gives

```math
\frac1p\binom{np}{pq+s}
\equiv
\frac ns(-1)^{s-1}\binom{n-1}{q}pmod p.
tag{12}
```

Multiplying (8), (9), (10), and (12), the unit $q$-block in (1), divided by
$p^2$, becomes

```math
(-1)^{q-1}n^2
\binom{n-1}{q}\binom{n+q}{q}
\left(
\binom{2q}{n}\sum_{s=1}^{h}s^{-2}
+\binom{2q+1}{n}\sum_{s=h+1}^{p-1}s^{-2}
\right).
tag{13}
```

It also vanishes by (7).  Here $0\le q<n$, exactly the complete unit blocks
inside $0\le k\le np$.  Combining this with (6) proves the case $r=1$ of
(3).

## 6. The parity-doubling block lemma

We use the following aggregate induction of Beukers and Straub.  Suppose
$a_j\in\mathbb Z_p$ has

```math
\sum_{\lfloor j/p^s\rfloor=L}a_j\equiv0\pmod {p^s}
\qquad(0\le s\le r),
tag{17}
```

and a kernel $C$ has the Cartier descent

```math
C(p^t m;j)\equiv C(p^{t-1}m;\lfloor j/p\rfloor)
\pmod {p^t}.
tag{18}
```

Then

```math
\sum_{\lfloor j/p^r\rfloor=L}a_jC(p^r m;j)
\equiv0\pmod {p^r}.
tag{19}
```

For completeness, the induction groups a $p^r$-block into $p$-blocks,
uses (18), and writes

```math
b_q={1\over p}\sum_{\lfloor j/p\rfloor=q}a_j.
```

Condition (17) for $a$ becomes the same condition, one level lower, for
$b$.  This proves (19) by induction on $r$.

### Lemma 3 (parity-doubling reciprocal blocks)

Let $p\ge5$, let $P=p^s$ divide $N$, and let $L\ge0$.  Then

```math
\boxed{
\sum_{\substack{LP\le k<(L+1)P\\p\nmid k}}
{1\over k^2}\binom{2k}{N}\equiv0\pmod P.
}
tag{20}
```

To prove this, define on the integer index $j$

```math
a_j=
\begin{cases}
4/j^2,&j\text{ even and }p\nmid j,\\
0,&\text{otherwise}.
\end{cases}
tag{21}
```

This sequence satisfies (17) at every level.  Indeed, put $P=p^s$ and
write $j=LP+u$, $0\le u<P$.  Because $P$ is odd, the parity condition on
$u$ is even when $L$ is even and odd when $L$ is odd.  In the even case,
$u=2v$ reduces the block sum modulo $P$ to

```math
H_s=\sum_{\substack{1\le v\le(P-1)/2\\p\nmid v}}v^{-2}.
tag{22}
```

In the odd case, $u\mapsto P-u$ gives the same sum.  The full reduced
residue sum is twice $H_s$ and vanishes modulo $P$: inversion permutes the
units modulo $P$, while

```math
\sum_{\substack{1\le v<P\\p\nmid v}}v^2
=\sum_{v=1}^{P-1}v^2-p^2\sum_{v=1}^{P/p-1}v^2
\equiv0\pmod P.
tag{23}
```

Since $2$ is a unit, $H_s\equiv0\pmod P$.

Now take $C(N;j)=\binom jN$.  Straub's shifted-binomial congruence gives

```math
\binom{j}{p^t m}\equiv
\binom{\lfloor j/p\rfloor}{p^{t-1}m}\pmod {p^t},
tag{24}
```

so (19) applies.  Finally, $j=2k$ maps the $k$-block in (20) onto the even
indices in the two consecutive $j$-blocks numbered $2L$ and $2L+1$, and
$4/j^2=1/k^2$.  Adding those two instances of (19) proves (20).

This is the promised resolution of the two Lucas carry states: doubling
does not remove the carry, but turns it into two ordinary Cartier blocks.

## 7. Shifted kernels and the unit shell

For $j\ge0$ define

```math
D_W(N;j)=\binom{N+j}{j}^3
tag{25}
```

and

```math
D_V(N;j)=(-1)^{j+1}
\binom{-N-1}{j}^2\binom{N-1}{j}.
tag{26}
```

Straub's two shifted-binomial congruences imply, for either kernel,

```math
D_\star(p^t m;j)\equiv
D_\star(p^{t-1}m;\lfloor j/p\rfloor)\pmod {p^t}.
tag{27}
```

For $D_W$ this is the descent of
$\binom{p^tm+j}{p^tm}^3$.  For $D_V$, the two negative-upper factors
remove the sign introduced by their descent, while the remaining sign and
$\binom{p^tm-1}{j}$ are exactly Straub's signed shifted factor.

If $p\nmid k$, then
$\lfloor(k-1)/p\rfloor=\lfloor k/p\rfloor$.  Applying (27) twice gives

```math
D_\star(N;k-1)\equiv D_\star(N;k)\pmod {p^r}
\qquad(N=np^r).
tag{28}
```

The elementary identity

```math
\binom{N+k}{k}=(-1)^k\left(1+{k\over N}\right)\binom{-N}{k}
tag{29}
```

now splits each unit summand into a termwise cubic part and one aggregate
part.  Explicitly,

```math
w_N(k)=(-1)^k\binom{-N}{k}^3\binom{2k}{N}
+{N^2\over k^2}D_W(N;k-1)\binom{2k}{N}
tag{30}
```

and

```math
v_N(k)=(-1)^k\binom{-N}{k}^2\binom Nk\binom{2k}{N}
+{N^2\over k^2}D_V(N;k-1)\binom{2k}{N}.
tag{31}
```

When $p\nmid k$, each of the first three generalized binomial factors in
the first term is divisible by $p^r$.  Thus the first term in either line
is zero modulo $p^{3r}$.

In the second term, replace $D_\star(N;k-1)$ by $D_\star(N;k)$ using
(28); multiplication by $N^2$ promotes the error to $p^{3r}$.  Lemma 3
says that

```math
a_k={1\over k^2}\binom{2k}{N}\quad(p\nmid k),
\qquad a_k=0\quad(p\mid k)
tag{32}
```

has vanishing block sums modulo $p^s$ for every $s\le r$.  Apply the
aggregate induction (19) a second time, now with $C=D_V$ or $D_W$.
Every complete unit block of length $p^r$ therefore vanishes modulo $p^r$
after division by $N^2$.  The ranges $0\le k\le N$ and
$0\le k\le cN$ consist of complete such blocks plus a $p$-divisible
endpoint.  Hence

```math
\sum_{\substack{0\le k\le N\\p\nmid k}}v_N(k)\equiv0\pmod {p^{3r}},
\qquad
\sum_{\substack{0\le k\le cN\\p\nmid k}}w_N(k)\equiv0\pmod {p^{3r}}.
tag{33}
```

Combining (33) with the all-level scaled transfer (6) proves Theorem 1.
$\square$

## 8. Quadratic coefficient form

The exact coefficient representation that first exposed the carry remains
useful.  Define

```math
F_N(X)=\sum_{k=0}^{N}
\binom{-N}{k}\binom Nk\binom{N+k}{k}X^k
tag{34}
```

and

```math
G_{c,N}(X)=\sum_{k=0}^{cN}
\binom{-N}{k}^2\binom{N+k}{k}X^k.
tag{35}
```

Since $[z^N](1+z)^{2k}=\binom{2k}{N}$, the two companions are exactly

```math
\boxed{
V(N)=[z^N]F_N((1+z)^2),\qquad
W_c(N)=[z^N]G_{c,N}((1+z)^2).
}
tag{36}
```

Thus the two Lucas states are the two halves of the coefficient extraction
through $X=(1+z)^2$.  Lemma 3 is the all-level arithmetic version of that
decomposition.  A generic unit summand still has valuation only $2r$, so
the cubic gain cannot be made termwise.

At $p=3$, the first-level half-residue sum in (7) is nonzero, and exact
examples attain valuation two.  The restriction $p\ge5$ is therefore
sharp for a uniform theorem of this form.

## 9. Verification

Run

```text
python verification/related/verify_index_dependent_companion_boundary.py
```

The checker verifies the half-residue identity, formulas (8)--(13) and
(29)--(36), the
parity-doubling block lemma, both shifted-kernel descents, every complete
unit shell, the all-level scaled transfer, and the full towers over an
extended exact grid.

## 10. Source boundary

Peter Bala proposed the substitution families in the August correspondence.
The proof uses Lucas' theorem, the classical adjacent
Jacobsthal--Kazandzidis congruence, and Lemmas 5.1--5.3 of Armin Straub's
[*Multivariate Apéry numbers and supercongruences of rational
functions*](https://arxiv.org/abs/1401.0854).  The new step is Lemma 3:
the substitution $j=2k$ resolves the doubling carry into two
parity-filtered blocks that meet Straub's published one-state hypothesis.
No priority claim is made.
