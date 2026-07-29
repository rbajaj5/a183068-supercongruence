# Closed surjection counts for finite abelian $2$-targets

## Status and source boundary

Roe and Turturean ask for explicit formulas for

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},G)\right|
$$

for finite groups $G$, starting from their presentation of
$G_{\mathbb Q_2}$. This note gives a closed answer when $G$ is a finite
abelian $2$-group.

The presentation and the marked maximal pro-$2$ quotient are due to Roe
and Turturean. The count below is an elementary consequence of their
abelianization. It is a solved special case of their broader counting
question, not a claim that the general finite-group problem is solved.
No literature-priority claim is made.

[RT]: https://roed314.github.io/gq2/paper/paper.html

## 1. The abelian source

Every homomorphism from $G_{\mathbb Q_2}$ to a finite $2$-group factors
through its maximal pro-$2$ quotient

$$
D_0= \left\langle A,S,Y\ \middle|\ A^2S^4[S,Y]=1 \right\rangle_{\mathrm{pro}\text{-}2}.
$$

After abelianization the relation is

$$
2\bar A+4\bar S=0.
$$

Writing

$$
t=\bar A+2\bar S
$$

gives

$$
D_0^{\mathrm{ab}} \cong C_2\oplus\mathbb Z_2\oplus\mathbb Z_2, \tag{1}
$$

with coordinates $t,\bar S,\bar Y$. Thus a homomorphism to a finite
abelian $2$-group $H$ is a triple

$$
(z,x,y)\in H[2]\times H\times H, \tag{2}
$$

and it is surjective exactly when $z,x,y$ generate $H$.

## 2. Closed formula

Write the invariant-factor decomposition in the form

$$
H\cong (C_2)^e\oplus \bigoplus_{j=1}^{h}C_{2^{\lambda_j}}, \qquad \lambda_j\ge2, \tag{3}
$$

and put

$$
d=e+h=\dim_{\mathbb F_2}(H/2H),\qquad q=|2H|. \tag{4}
$$

For $j\ge0$, define

$$
P_j= \begin{cases} \displaystyle\prod_{i=0}^{j-1}(4-2^i),&0\le j\le2,\\ 0,&j>2. \end{cases} \tag{5}
$$

Thus $P_0=1$, $P_1=3$, and $P_2=6$.

### Theorem

For every nontrivial finite abelian $2$-group $H$,

$$
\boxed{ \left|\mathrm{Sur}(G_{\mathbb Q_2},H)\right| = q^2\,2^h \left( P_d+(2^e-1)\,4P_{d-1} \right). } \tag{6}
$$

Here the second summand inside the parentheses is absent when $e=0$.
In particular, the count is zero if $d>3$.

### Proof

For a finite $2$-group, a set generates $H$ if and only if its image
generates the Frattini quotient

$$
V=H/2H\cong\mathbb F_2^d. \tag{7}
$$

The reduction map

$$
H[2]\longrightarrow V
$$

has kernel of size $2^h$. Its image is the $e$-dimensional subspace
$E\subseteq V$ contributed by the direct $C_2$-factors in (3).
Each ordered pair in $V^2$ has $q^2$ lifts to $H^2$.

It remains to count

$$
N(d,e)= \left|\{(\bar x,\bar y,\bar z)\in V^2\times E: \langle\bar x,\bar y,\bar z\rangle=V\}\right|. \tag{8}
$$

If $\bar z=0$, the ordered pair $(\bar x,\bar y)$ must span $V$.
There are $P_d$ such pairs.

If $\bar z\ne0$, there are $2^e-1$ choices for $\bar z$. The images
of $\bar x,\bar y$ must span $V/\langle\bar z\rangle$. There are
$P_{d-1}$ spanning ordered pairs in that quotient, and each pair has
four lifts to $V^2$. Therefore

$$
N(d,e)=P_d+(2^e-1)\,4P_{d-1}. \tag{9}
$$

Multiplying (9) by the lift multiplicity $q^2 2^h$ proves (6).
$\square$

## 3. Concrete consequences

For a cyclic target,

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},C_{2^m})\right| = \begin{cases} 7,&m=1,\\ 3\cdot2^{2m-1},&m\ge2. \end{cases} \tag{10}
$$

Dividing by
$\left|\mathrm{Aut}(C_{2^m})\right|=\varphi(2^m)$ gives the number
of cyclic $2^m$-extensions of $\mathbb Q_2$:

$$
\boxed{ \left|\{C_{2^m}\text{-extensions of }\mathbb Q_2\}\right| = \begin{cases} 7,&m=1,\\ 3\cdot2^m,&m\ge2. \end{cases} } \tag{11}
$$

The first value recovers the seven quadratic extensions of
$\mathbb Q_2$.

For elementary abelian targets,

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},(C_2)^d)\right| = \prod_{i=0}^{d-1}(8-2^i) \qquad(1\le d\le3), \tag{12}
$$

giving $7,42,168$ for $d=1,2,3$, and zero for $d>3$.

The possible Frattini ranks and the residual binary counts in (6) are:

| $d$ | $e$ | $N(d,e)$ |
| ---: | ---: | ---: |
| 1 | 0 | 3 |
| 1 | 1 | 7 |
| 2 | 0 | 6 |
| 2 | 1 | 18 |
| 2 | 2 | 42 |
| 3 | 1 | 24 |
| 3 | 2 | 72 |
| 3 | 3 | 168 |

## 4. Relation to the supercongruence program

This is not itself a supercongruence. Its relevance is structural: the
same binary lift decomposition used throughout this repository separates

1. a finite mod-$2$ generating condition, and
2. a uniform power-of-$2$ lift multiplicity.

Formula (6) is the resulting exact local count. It is a useful control
case for dyadic lifting arguments because every possible loss is visible
in the $C_2$-coordinate and the Frattini quotient.

## Verification

The exact checker
[`verify_gq2_finite_abelian_counts.py`](../verification/related/verify_gq2_finite_abelian_counts.py)
enumerates every triple in (2) for all invariant-factor types of order at
most $2^8$, compares the brute-force counts with (6), and separately
checks (10)--(12).

Run:

```text
python verification/related/verify_gq2_finite_abelian_counts.py
```

## Reference

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of
  $\mathbb Q_2$*][RT], especially Proposition 1.1, equation (3.2), and
  Section 11, Question 4.
