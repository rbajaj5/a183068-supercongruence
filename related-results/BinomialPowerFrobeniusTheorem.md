# A polynomial Frobenius theorem for binomial-power sums

**Status:** complete elementary deduction from
Ljunggren--Jacobsthal--Kazandzidis scaling; exact checks pass; literature
priority not established

## 1. The unified statement

For an integer \(m\ge3\), define

```math
P_N^{(m)}(X)=\sum_{k=0}^N\binom Nk^mX^k\in\mathbb Z[X].
```

For a prime \(p\), put

```math
\varepsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\ge5,
\end{cases}
```

and

```math
E_{p,m}(r)=3r-\varepsilon_p+v_p(m).
\qquad\text{(1)}
```

### Theorem 1

For every prime \(p\), \(m\ge3\), and \(n,r\ge1\),

```math
P_{np^r}^{(m)}(X)
\equiv
P_{np^{r-1}}^{(m)}(X^p)
\pmod {p^{E_{p,m}(r)}}
\qquad\text{(2)}
```

coefficientwise in \(\mathbb Z[X]\).

The exponent in (1) has two parts: the usual small-prime loss
\(\varepsilon_p\), and a multiplicity bonus \(v_p(m)\).  At \(p=2\):

| exponent \(m\) | binary modulus in (2) |
| --- | --- |
| \(m\) odd | \(2^{3r-2}\) |
| \(m\equiv2\pmod4\) | \(2^{3r-1}\) |
| \(v_2(m)=t\ge2\) | \(2^{3r-2+t}\) |

Thus taking an even power is not cosmetic: it recovers powers of \(2\) lost
by the underlying scaling quotient.  The same phenomenon holds at every
prime dividing \(m\); for example, cubing recovers the one-power loss at
\(p=3\).

## 2. Gaussian and A005260 corollaries

At \(X=i\), Theorem 1 gives a Gaussian Frobenius law.  Split primes fix
\(i\), inert primes conjugate it, and the ramified prime sends \(i\) to
\(-1\):

```math
P_{np^r}^{(m)}(i)\equiv
\begin{cases}
P_{n2^{r-1}}^{(m)}(-1)
 \pmod {2^{\,3r-2+v_2(m)}},&p=2,\\
\overline{P_{n3^{r-1}}^{(m)}(i)}
 \pmod {3^{\,3r-1+v_3(m)}},&p=3,\\
P_{np^{r-1}}^{(m)}(i)
 \pmod {p^{\,3r+v_p(m)}},&p\equiv1\pmod4,\\
\overline{P_{np^{r-1}}^{(m)}(i)}
 \pmod {p^{\,3r+v_p(m)}},&p\equiv3\pmod4,\ p\ge7.
\end{cases}
\qquad\text{(3)}
```

For \(m=4\), \(P_N^{(4)}(1)\) is A005260.  In this case the binary loss
vanishes, so

```math
P_{np^r}^{(4)}(X)
\equiv
P_{np^{r-1}}^{(4)}(X^p)
\pmod {p^{e_p(r)}},
```

where \(e_3(r)=3r-1\) and \(e_p(r)=3r\) for \(p=2\) or \(p\ge5\).
This closes the first proof target produced by the
[Gaussian Bala-queue map](BalaGaussianGeneralizationMap.md).

## 3. Coefficients away from the surviving stratum

Let \(N=np^r\).  If \(p\nmid k\), the identity

```math
\binom Nk=\frac Nk\binom{N-1}{k-1}
```

gives

```math
v_p\binom Nk\ge r.
\qquad\text{(4)}
```

Consequently,

```math
p^{mr}\mid\binom Nk^m
\qquad(p\nmid k).
\qquad\text{(5)}
```

This is at least the modulus asserted in (1).  Indeed,

```math
mr-E_{p,m}(r)=(m-3)r+\varepsilon_p-v_p(m)\ge0.
```

For \(p=2,3\), use \(v_2(m)\le m-1\) and \(v_3(m)\le m-2\);
for \(p\ge5\), use \(v_p(m)\le m-3\).  These elementary bounds also
cover \(m=3,4\), when the relevant valuations vanish.

## 4. Scaling the surviving coefficients

Write

```math
a=np^{r-1},\qquad k=p\ell,\qquad
B=\binom a\ell,\qquad A=\binom{pa}{p\ell}.
```

Let \(s\) be the minimum \(p\)-adic valuation of the positive members of
\(\ell,a-\ell\).  The standard binomial specialization of the
Ljunggren--Jacobsthal--Kazandzidis quotient congruence gives

```math
Q:=\frac AB
\equiv1\pmod {p^{3(s+1)-\varepsilon_p}},
\qquad\text{(6)}
```

where

```math
\varepsilon_2=2,\qquad
\varepsilon_3=1,\qquad
\varepsilon_p=0\quad(p\ge5).
```

The quotient is a \(p\)-adic unit.  Endpoint cases \(\ell=0,a\) give
\(A=B=1\) and may be omitted.

The binary sign qualification in the strongest source form of (6) causes
no ambiguity here.  In the equal-index specialization it cannot occur at
\(s\ge1\); at \(s=0\), the modulus is \(2\), where the two signs agree.  This
is the same point isolated in the repository's
[A183068 proof](../PROOF.md#3-multinomial-scaling).

For odd \(p\), the ordinary lifting-the-exponent identity and (6) imply

```math
v_p(Q^m-1)
\ge3(s+1)-\varepsilon_p+v_p(m).
\qquad\text{(7)}
```

At \(p=2\), put \(t=v_2(m)\).  If \(m\) is odd, factor
\(Q^m-1\) by \(Q-1\) and obtain

```math
v_2(Q^m-1)\ge3s+1.
```

If \(m\) is even, the \(2\)-adic lifting-the-exponent identity gives

```math
v_2(Q^m-1)
=v_2(Q-1)+v_2(Q+1)+t-1.
\qquad\text{(8)}
```

For \(s\ge1\), equation (6) gives
\(v_2(Q-1)\ge3s+1\) and \(Q\equiv1\pmod {16}\), hence
\(v_2(Q+1)=1\).  For \(s=0\), every odd \(2\)-adic unit
satisfies

```math
v_2(Q-1)+v_2(Q+1)\ge3.
```

Both cases yield the uniform bound

```math
v_2(Q^m-1)
\ge3(s+1)-2+v_2(m).
\qquad\text{(9)}
```

Equations (7) and (9) are the common multiplicity bonus in (1).

## 5. Completing the transfer

Suppose first that \(s<r-1\).  Since \(p^{r-1}\mid a\),

```math
v_p(\ell)=v_p(a-\ell)=s.
```

The identity used in (4) gives

```math
v_p(B)\ge r-1-s.
\qquad\text{(10)}
```

Since

```math
A^m-B^m=B^m(Q^m-1),
```

equations (7), (9), and (10) yield

```math
v_p(A^m-B^m)
\ge
m(r-1-s)+3(s+1)-\varepsilon_p+v_p(m),
\qquad\text{(11)}
```

The right side of (11) is smallest at \(s=r-2\) when \(m>3\), and is
constant in \(s\) when \(m=3\).  Since \(m\ge3\), it is at least
\(E_{p,m}(r)\).

If \(s\ge r-1\), the quotient estimates (7) and (9) alone give exactly the
required lower bounds.  Therefore the coefficient of \(X^{p\ell}\) in

```math
P_{np^r}^{(m)}(X)-P_{np^{r-1}}^{(m)}(X^p)
```

is divisible by \(p^{E_{p,m}(r)}\).  The other coefficients satisfy (5).
This proves Theorem 1.

## 6. Literature boundary

The untwisted \(p^{3r}\) tower at primes \(p\ge5\) belongs to the established
generalized Apéry literature.  The sums \(P_N^{(m)}(1)\) are the
\((\lambda,\mu)=(m,0)\) members of the family discussed by Straub in
[*Supercongruences for polynomial analogs of the Apéry numbers*](https://arxiv.org/abs/1803.07146).

The variable \(X\) above is an ordinary summand weight, not Straub's
\(q\)-binomial deformation.  The proof here is a coefficientwise deduction
from classical scaling and records the exact small-prime multiplicity law.
Exact-fingerprint searches did not locate this formulation, but that is not
a priority certificate; this note makes no novelty claim.

Its immediate use is as a reusable route-T theorem:

- every root-of-unity specialization is automatic;
- the split/inert action is explicit;
- the prime \(2\) is included rather than inferred from an odd-prime
  argument; and
- the prime-specific multiplicity bonus \(v_p(m)\) is explicit.

## 7. Exact checks

The checker tests powers \(3\le m\le8\), all binary multiplicity
classes, the \(p=3\) boundary and bonus, and split and inert odd primes.  It verifies
the coefficientwise theorem and the Gaussian specialization, and records
equality witnesses at the stated exponents.

Run:

```text
python verification/related/verify_binomial_power_frobenius.py
```
