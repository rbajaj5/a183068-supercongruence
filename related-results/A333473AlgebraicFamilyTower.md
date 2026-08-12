# The full A333473 algebraic family has a quadratic tower

**Status:** complete elementary proof candidate; independent review pending

## 1. Statement

Let

```math
F(x)=\frac{1-\sqrt{1-4x-4x^2}}{2x}.
```

Equivalently, $F(0)=1$ and

```math
F=1+x+xF^2.
tag{1}
```

For positive integers $R,S,N$, define

```math
A_{R,S}(N)=[x^{RN}]F(x)^{SN}.
tag{2}
```

The named OEIS sequence A333473 is the case $R=S=1$.  The August
mixed-binomial note proved that named case but left the two-parameter
algebraic family open.

### Theorem 1

For every odd prime $p$ and all positive integers $R,S,n,r$,

```math
\boxed{
A_{R,S}(np^r)\equiv A_{R,S}(np^{r-1})\pmod {p^{2r}}.
}
tag{3}
```

There are no exclusions when $p$ divides $R$ or $S$.

The proof is stronger than (3): after Lagrange inversion, every summand at
the upper level either vanishes modulo $p^{2r}$ or transfers termwise from
the preceding level.

## 2. Integral Lagrange normalization

Put $W=F-1$.  Equation (1) becomes

```math
W=x(W^2+2W+2).
tag{4}
```

Lagrange inversion gives

```math
A_{R,S}(N)
=\frac SR\sum_{j=0}^{RN}
\binom{RN}{j}\binom{SN+2j-1}{RN-1}.
tag{5}
```

The summand has the more useful form

```math
T_{R,S}(N,j)
=\frac{SN}{SN+2j}
 \binom{RN}{j}\binom{SN+2j}{RN}.
tag{6}
```

As usual, a binomial coefficient with nonnegative upper argument smaller
than its lower argument is zero.  Equations (5)--(6) imply

```math
A_{R,S}(N)=\sum_{j=0}^{RN}T_{R,S}(N,j).
tag{7}
```

Although (6) is written as a rational product, it is locally integral at
every odd prime.

### Lemma 2 (odd-local integrality)

For every odd prime $p$, $T_{R,S}(N,j)\in\mathbb Z_p$.

### Proof

Set $B=SN+2j$.  There is nothing to prove when $B<RN$.  Otherwise use

```math
\binom{RN}{j}\binom{B}{RN}
=\binom{B}{j}\binom{B-j}{RN-j}.
tag{8}
```

Write $h=v_p(SN)$ and $d=v_p(B)$.  If $d\le h$, the prefactor $SN/B$ in
(6) is $p$-integral.  If $d>h$, the identity $B=SN+2j$ and oddness of $p$
give $v_p(j)=h$.  Moreover,

```math
\binom Bj=\frac Bj\binom{B-1}{j-1},
```

so (8) has valuation at least $d-h$, exactly compensating the valuation
$h-d$ of $SN/B$.  This proves the lemma. $\square$

## 3. Termwise Frobenius transfer

We use the adjacent Jacobsthal--Kazandzidis binomial estimate in the
following form.  Put

```math
\epsilon_p=\begin{cases}1,&p=3,\\0,&p\ge5.\end{cases}
```

If $A,B,A-B$ are all divisible by $p^q$, then

```math
\frac{\binom{pA}{pB}}{\binom AB}
\equiv1\pmod {p^{3(q+1)-\epsilon_p}}.
tag{9}
```

Zero binomial coefficients are treated before taking the quotient.

Let $N=np^r$ and $M=N/p$.  First suppose $p\nmid j$.  Then $SN+2j$ is a
$p$-adic unit.  The prefactor in (6) contributes at least $p^r$, while

```math
\binom{RN}{j}=\frac{RN}{j}\binom{RN-1}{j-1}
```

contributes another $p^r$.  Hence

```math
T_{R,S}(N,j)\equiv0\pmod {p^{2r}}.
tag{10}
```

Now write $j=p\ell$.  When the two terms are nonzero, their quotient is
exactly

```math
\frac{T_{R,S}(pM,p\ell)}{T_{R,S}(M,\ell)}
=
\frac{\binom{pRM}{p\ell}}{\binom{RM}{\ell}}
\frac{\binom{p(SM+2\ell)}{pRM}}
     {\binom{SM+2\ell}{RM}}.
tag{11}
```

Let $q=v_p(\ell)$.  If $q<r-1$, the three arguments in each binomial
quotient in (11) have minimum valuation $q$.  Also

```math
v_p\!\left(\frac{SM}{SM+2\ell}\right)\ge r-1-q,
\qquad
v_p\!\binom{RM}{\ell}\ge r-1-q.
tag{12}
```

Therefore Lemma 2, (9), and (12) give

```math
\begin{aligned}
v_p\bigl(T_{R,S}(pM,p\ell)-T_{R,S}(M,\ell)\bigr)
&\ge 2(r-1-q)+3(q+1)-\epsilon_p\\
&=2r+q+1-\epsilon_p\\
&\ge2r.
\end{aligned}
tag{13}
```

If $q\ge r-1$ (including $\ell=0$), both quotients in (11) are $1$
modulo $p^{3r-\epsilon_p}$.  Lemma 2 now gives

```math
v_p\bigl(T_{R,S}(pM,p\ell)-T_{R,S}(M,\ell)\bigr)
\ge3r-\epsilon_p\ge2r.
tag{14}
```

Thus, coefficientwise in $\mathbb Z_p[X]$,

```math
\sum_{j=0}^{RN}T_{R,S}(N,j)X^j
\equiv
\sum_{\ell=0}^{RM}T_{R,S}(M,\ell)X^{p\ell}
\pmod {p^{2r}}.
tag{15}
```

Setting $X=1$ and using (7) proves Theorem 1. $\square$

## 4. What closes and what does not

Theorem 1 closes the entire positive $(R,S)$ family proposed around
A333473, not merely the named diagonal $R=S=1$.  Its mechanism is the same
discard/transfer split that controls many factorial-ratio
supercongruences, but the decisive normalization is the Lagrange summand
(6).  The extra prefix $-1$ in (5) is not harmless bookkeeping: it becomes
the factor $SN/(SN+2j)$, which supplies one of the two discarded-stratum
powers.

The theorem is rational-prime arithmetic.  The factorization

```math
t^2+2t+2=(t+1-i)(t+1+i)
```

explains why a Gaussian reformulation is available, but no Gaussian-prime
claim is needed for (3).

## 5. Verification

Run

```text
python verification/related/verify_a333473_algebraic_family_tower.py
```

The checker verifies the Lagrange identity against direct power-series
expansion, odd-local integrality of every tested summand, and the stronger
coefficientwise transfer (15), including primes dividing $R$ or $S$.

## 6. Source boundary

Peter Bala proposed the algebraic family in the OEIS comments and in the
August correspondence.  The external arithmetic input in this proof is the
classical adjacent Jacobsthal--Kazandzidis binomial congruence.  No
literature-priority claim is made for this packaging or for Theorem 1.
