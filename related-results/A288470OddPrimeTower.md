# The A288470 double-binomial tower at every odd prime

**Status:** complete proof candidate; exact checks supplied; conventional
review and a full priority search are pending

The [OEIS entry A288470](https://oeis.org/A288470) defines

```math
a(N)=\sum_{k=0}^{N}\binom Nk\binom{2N}{2k}
```

and conjectures

```math
a(mp^r)\equiv a(mp^{r-1})\pmod {p^{2r}}
```

for primes $p\ge 5$ and positive integers $m,r$.

The restriction $p\ge5$ is not the natural boundary. The proof below works
for every odd prime, including $p=3$. The excluded prime $2$ really is
different: the proposed modulus already fails for $m=1,r=2$.

## Theorem

For every odd prime $p$ and all integers $m,r\ge1$,

```math
\boxed{
a(mp^r)\equiv a(mp^{r-1})\pmod {p^{2r}}.
}
```

Thus the conjecture on A288470 holds, and its prime range strengthens from
$p\ge5$ to every odd prime.

The proof uses exactly the two-stratum mechanism of the A183068 theorem:
terms with $p\nmid k$ vanish, while terms with $p\mid k$ transfer to the
preceding scale.

## 1. Two carries at every missed digit level

Write

```math
F(N,k)=\binom Nk\binom{2N}{2k}.
```

Let $N=mp^r$ and suppose $s=v_p(k)<r$. At every level
$q=p^i$ with $s<i\le r$, write

```math
k=qa+u,\qquad 0<u<q.
```

Because $q\mid N$, the summand at level $q$ in Legendre's formula for
$\binom Nk$ is

```math
\left\lfloor\frac Nq\right\rfloor
-\left\lfloor\frac kq\right\rfloor
-\left\lfloor\frac{N-k}{q}\right\rfloor
=1.
```

The prime $p$ is odd, so $q\nmid 2k$. Applying the same calculation to
$\binom{2N}{2k}$ supplies a second carry at the same level. Summing over the
$r-s$ missed levels gives

```math
v_p(F(mp^r,k))\ge 2(r-s).
```

In particular,

```math
p\nmid k
\quad\Longrightarrow\quad
F(mp^r,k)\equiv0\pmod {p^{2r}}.
```

This is the entire vanishing stratum.

## 2. Transfer of the divisible stratum

We use the standard adjacent Jacobsthal--Kazandzidis estimate. For an odd
prime $p$, put

```math
\varepsilon_p=
\begin{cases}
1,&p=3,\\
0,&p\ge5.
\end{cases}
```

If $0<B<A$ and

```math
t=\min\{v_p(B),v_p(A-B)\},
```

then

```math
\frac{\binom{pA}{pB}}{\binom AB}
\equiv1\pmod {p^{3(t+1)-\varepsilon_p}}.
```

The endpoint quotients are exactly $1$.

Now write $k=p\ell$ and $N'=mp^{r-1}$. The ratio

```math
\frac{F(pN',p\ell)}{F(N',\ell)}
```

is the product of the two adjacent binomial quotients

```math
\frac{\binom{pN'}{p\ell}}{\binom{N'}{\ell}}
\quad\text{and}\quad
\frac{\binom{2pN'}{2p\ell}}{\binom{2N'}{2\ell}}.
```

For $\ell=0$ or $\ell=N'$, both quotients are exactly $1$, so the
termwise transfer is an equality. Assume henceforth that $0<\ell<N'$, and
let $s=v_p(\ell)$.

### Case 1: $s<r-1$

Because $p^{r-1}\mid N'$,

```math
v_p(N'-\ell)=s.
```

The transfer quotient is therefore $1$ modulo
$p^{3(s+1)-\varepsilon_p}$. The carry estimate at the lower level gives

```math
v_p(F(N',\ell))\ge2(r-1-s).
```

Consequently

```math
\begin{aligned}
v_p\!\left(F(pN',p\ell)-F(N',\ell)\right)
&\ge 2(r-1-s)+3(s+1)-\varepsilon_p\\
&=2r+s+1-\varepsilon_p\\
&\ge2r.
\end{aligned}
```

The final inequality includes $p=3$, where $\varepsilon_3=1$.

### Case 2: $s\ge r-1$

Both lower positive binomial parts have valuation at least $r-1$, so the
scaling estimate alone gives

```math
v_p\!\left(F(pN',p\ell)-F(N',\ell)\right)
\ge3r-\varepsilon_p
\ge2r.
```

Hence, in every case,

```math
F(mp^r,p\ell)\equiv F(mp^{r-1},\ell)\pmod {p^{2r}}.
```

Split the defining sum for $a(mp^r)$ according to whether $p$ divides
$k$. The nondivisible terms vanish by Section 1, and the substitution
$k=p\ell$ identifies the divisible terms with the complete sum at the
preceding scale. This proves the theorem. $\square$

## 3. Gaussian Frobenius-twist corollary

For a fourth root of unity $\zeta\in\mathbb Z[i]$, define

```math
a_\zeta(N)=
\sum_{k=0}^{N}
\zeta^k\binom Nk\binom{2N}{2k}.
```

The proof above is termwise. If $p\nmid k$, the summand still vanishes
modulo $p^{2r}$. If $k=p\ell$, then

```math
\zeta^{p\ell}=(\zeta^p)^\ell.
```

Therefore, for every odd rational prime $p$,

```math
\boxed{
a_\zeta(mp^r)
\equiv
a_{\zeta^p}(mp^{r-1})
\pmod {p^{2r}\mathbb Z[i]}.
}
```

For $\zeta=i$, this specializes to

```math
\begin{cases}
a_i(mp^r)\equiv a_i(mp^{r-1})\pmod {p^{2r}},
&p\equiv1\pmod4,\\
a_i(mp^r)\equiv a_{-i}(mp^{r-1})\pmod {p^{2r}},
&p\equiv3\pmod4.
\end{cases}
```

Thus split Gaussian primes give a fixed twist and inert rational primes give
the conjugate twist. This is a formal Frobenius corollary of the termwise
integer proof; it is not a separate claim of literature priority.

## 4. The binary boundary is real

The first values are

```math
a(1)=2,\qquad a(2)=14,\qquad a(4)=646.
```

Thus

```math
a(4)-a(2)=632=2^3\cdot79,
```

so

```math
v_2(a(4)-a(2))=3<4.
```

Therefore the analogous assertion at $p=2$, $m=1$, $r=2$ is false. The
oddness assumption in the theorem is structural: only for odd $p$ does
$p\nmid k$ imply $p\nmid2k$, forcing the second carry at every level.

## 5. What is new and what is classical

The ingredients are classical:

- Legendre's digit-carry formula for binomial valuations; and
- the adjacent Jacobsthal--Kazandzidis scaling congruence.

The contribution of this note is the short assembly for A288470 and the
sharpened prime range. No literature-priority claim is made until the exact
sequence and its constant-term representation have been checked against
the general Dwork and constant-term literature.

## 6. Exact verification

Run

```text
python verification/related/verify_a288470_odd_prime_tower.py
```

The checker verifies:

1. the adjacent congruence on a grid of odd primes, levels, and
   multipliers;
2. every termwise carry bound on a systematic finite grid;
3. every divisible-stratum transfer on that grid;
4. the Gaussian Frobenius-twist corollary; and
5. the exact binary counterexample above.

These checks guard transcription and boundary arithmetic. The proof is the
valuation argument in Sections 1--2.
