# The A229452 coefficient root is integral

**Status:** complete elementary proof of the all-$m$ integrality conjecture
and an all-prime baseline for both parameter families; the proposed cubic
towers remain open

## 1. The family on the source page

The [OEIS A229452](https://oeis.org/A229452) comments define, for every
positive integer $m$,

```math
B_m(n)=\frac{(mn)!}{m!(n!)^m},
\qquad
E_m(x)=
\exp\left(\sum_{n\ge1}\frac{B_m(n)}n x^n\right),
\tag{1}
```

and then

```math
b_m(N)=[x^N]E_m(x)^N.
\tag{2}
```

The record conjectures that $b_m(N)$ is integral and satisfies a
$p^{3r}$ adjacent prime-power tower for $p\ge5$. Its displayed sequence
is the case $m=3$. It also proposes, for that displayed series, the
two-parameter family

```math
b_{R,S}(N)=[x^{RN}]E_3(x)^{SN},
\qquad R\ge1,\quad S\in\mathbb Z.
\tag{2a}
```

This note proves integrality for every $m$, supplies an exact
coefficient-root interpretation, and proves the universal all-prime
$p^r$ tower for both families. It does not claim the remaining two powers.

## 2. A strong Gauss property for the seed

The integer

```math
B_m(n)=\frac1{m!}\binom{mn}{n,\ldots,n}
\tag{3}
```

counts partitions of an $mn$-element labeled set into $m$ unlabeled
blocks of size $n$.

For a prime $p$, define

```math
\kappa_p(r)=
\begin{cases}
3r-2,&p=2,\\
3r-1,&p=3,\\
3r,&p\ge5.
\end{cases}
\tag{4}
```

### Lemma 1

For every prime $p$, positive integers $m,n,r$,

```math
B_m(np^r)\equiv B_m(np^{r-1})
\pmod {p^{\kappa_p(r)}}.
\tag{5}
```

### Proof

Put $N=np^{r-1}$ and

```math
M_m(N)=\binom{mN}{N,\ldots,N}=m!B_m(N).
```

The Ljunggren--Jacobsthal--Kazandzidis multinomial scaling congruence,
specialized to $m$ equal positive parts, gives

```math
\frac{M_m(pN)}{M_m(N)}
\equiv1\pmod {p^{\kappa_p(r)}}.
\tag{6}
```

The usual binary sign ambiguity causes no loss here.  If
$v_2(N)\ge1$, the equal lower entries exclude the negative-sign case; if
$v_2(N)=0$, the modulus in (6) is $2$, where the two signs agree.

Writing the quotient in (6) as $1+p^{\kappa_p(r)}u$ in
$\mathbb Z_p$ gives

```math
B_m(pN)-B_m(N)
=B_m(N)p^{\kappa_p(r)}u.
```

Since $B_m(N)$ is an integer, this proves (5). $\square$

In particular, $B_m$ has the ordinary Gauss property at every prime:

```math
B_m(np^r)\equiv B_m(np^{r-1})\pmod {p^r}.
\tag{7}
```

## 3. Integrality of the exponential root

### Theorem 2

For every positive integer $m$,

```math
E_m(x)\in1+x\mathbb Z[[x]].
\tag{8}
```

### Proof

Define

```math
e_m(d)=
\frac1d\sum_{c\mid d}\mu(d/c)B_m(c).
\tag{9}
```

For every prime power $p^s\Vert d$, pairing divisors whose $p$-adic
exponents are $s$ and $s-1$ shows that the numerator in (9) is divisible
by $p^s$, using (7).  Hence every $e_m(d)$ is integral.  Möbius
inversion gives the formal Euler product

```math
E_m(x)=\prod_{d\ge1}(1-x^d)^{-e_m(d)},
\tag{10}
```

which proves (8). $\square$

Consequently every coefficient $b_m(N)$ in (2) is an integer. This proves
the all-$m$ integrality conjecture on A229452, not just the displayed
$m=3$ instance.

## 4. The canonical coefficient root

There is a unique $F_m(x)\in1+x\mathbb Z[[x]]$ such that

```math
E_m(x)=F_m\bigl(xE_m(x)\bigr).
\tag{11}
```

Lagrange inversion gives two exact identities:

```math
[x^n]F_m(x)^n=B_m(n)
\tag{12}
```

and

```math
2[x^n]E_m(x)^n=[x^n]F_m(x)^{2n}.
\tag{13}
```

Thus A229452 is not an isolated exponential construction: it is the
two-power coefficient transform of the canonical integral root whose
diagonal coefficients are the equal-block multinomial numbers (3).

## 5. The universal adjacent tower

### Theorem 3

Fix $m,R\ge1$ and $S\in\mathbb Z$, and put

```math
c_{m;R,S}(N)=[x^{RN}]E_m(x)^{SN}.
\tag{14}
```

For every prime $p$ and positive integers $n,r$,

```math
c_{m;R,S}(np^r)\equiv
c_{m;R,S}(np^{r-1})\pmod {p^r}.
\tag{15}
```

### Proof

Theorem 2 makes $H(x)=E_m(x)^S$ an integral formal power series, including
when $S<0$, because $E_m(0)=1$. Apply the
cyclic-word orbit theorem from
[the coefficient-power baseline](CoefficientPowerGaussBaseline.md#3-a-universal-congruence-for-variable-powers)
to the coefficient of $x^{RN}$ in $H(x)^N$. A word of length $N$ and
total degree $RN$, when it has period $d\mid N$, is the repetition of a
block of length $d$ and total degree $Rd$. Thus the same primitive-orbit
decomposition applies without alteration. Every orbit newly appearing at
level $np^r$ has size divisible by $p^r$; the old orbits transfer by the
lifting-the-exponent estimate. This proves (15). $\square$

Taking $R=S=1$ gives the all-$m$ sequence $b_m$. Taking $m=3$ gives the
full $b(R,S;N)$ parameter range proposed on A229452.

The theorem is deliberately stated with modulus $p^r$.  Although the
logarithmic seed $B_m$ has the much stronger property (5), the general
coefficient-power orbit argument retains only one power per level.  A proof
of the proposed $p^{3r}$ tower must use additional cancellation among
orbits or a stronger Dwork/Cartier structure.

## 6. Exact checks and boundary

The checker:

1. verifies the set-partition integrality of $B_m(n)$;
2. checks the sharp seed congruence (5) at $p=2,3,5,7$;
3. constructs $E_m$ by its exact logarithmic-derivative recurrence;
4. verifies integral coefficients for $1\le m\le8$;
5. checks (12) and (13);
6. checks the full $(m,R,S)$ adjacent tower (15), including negative
   values of $S$; and
7. records the stronger cubic congruence only as experimental evidence.

Run:

```text
python verification/related/verify_a229452_coefficient_root.py
```

The proof uses the classical multinomial scaling congruence.  No priority
claim is made for the application or the coefficient-root packaging.
