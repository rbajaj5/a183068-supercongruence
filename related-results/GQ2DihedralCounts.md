# Exact $G_{\mathbb Q_2}$ surjection counts for dihedral $2$-groups

## Status and source boundary

Roe and Turturean ask for explicit formulas for

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},G)\right|
$$

for finite groups $G$. The
[finite abelian $2$-target formula](GQ2FiniteAbelianCounts.md) treats the
abelian boundary. This note gives the first nonabelian family: every
dihedral $2$-group.

The marked maximal pro-$2$ presentation is due to Roe and Turturean. The
count below is a direct elementary calculation from their relator. It solves
one family within their broader counting question and makes no
literature-priority claim.

[RT]: https://roed314.github.io/gq2/paper/paper.html

## 1. Statement

For $m\ge3$, let $D_{2^m}$ denote the dihedral group of order $2^m$:

$$
D_{2^m}
=
\left\langle r,w\ \middle|\
r^{2^{m-1}}=w^2=1,\quad wrw=r^{-1}
\right\rangle.
\tag{1}
$$

### Theorem

$$
\boxed{
\left|\mathrm{Sur}(G_{\mathbb Q_2},D_{2^m})\right|
=
\begin{cases}
144,&m=3,\\
2^{2m+1},&m\ge4.
\end{cases}
}
\tag{2}
$$

Since

$$
\left|\mathrm{Aut}(D_{2^m})\right|
=2^{2m-3},
\tag{3}
$$

the number of $D_{2^m}$-extensions of $\mathbb Q_2$ is

$$
\boxed{
\frac{
|\mathrm{Sur}(G_{\mathbb Q_2},D_{2^m})|
}{
|\mathrm{Aut}(D_{2^m})|
}
=
\begin{cases}
18,&m=3,\\
16,&m\ge4.
\end{cases}
}
\tag{4}
$$

Here a $D_{2^m}$-extension means a Galois extension together with an
abstract identification of its Galois group only up to automorphism; hence
the division in (4).

## 2. Coordinates and the relator

Put

$$
N=2^{m-1}.
$$

Write elements of $D_{2^m}$ as pairs

$$
(a,\alpha)=r^aw^\alpha,
\qquad
a\in\mathbb Z/N\mathbb Z,\quad
\alpha\in\mathbb F_2.
\tag{5}
$$

Multiplication is

$$
(a,\alpha)(b,\beta)
=
\left(a+(-1)^\alpha b,\alpha+\beta\right).
\tag{6}
$$

Every map from $G_{\mathbb Q_2}$ to a finite $2$-group factors through
the Roe--Turturean maximal pro-$2$ quotient

$$
D_0=
\left\langle A,S,Y\ \middle|\
A^2S^4[S,Y]=1
\right\rangle_{\mathrm{pro}\text{-}2}.
\tag{7}
$$

Choose images

$$
A=(a,\alpha),\qquad
S=(s,\sigma),\qquad
Y=(y,\tau).
\tag{8}
$$

The commutator convention is
$[S,Y]=S^{-1}Y^{-1}SY$. A direct calculation from (6) gives

$$
[S,Y]
=
\left(
(-1)^\sigma\bigl((-1)^\tau-1\bigr)s
+(-1)^\tau\bigl(1-(-1)^\sigma\bigr)y,
0
\right).
\tag{9}
$$

Consequently the relator in (7) becomes one linear congruence modulo $N$.
The eight reflection patterns give:

| $(\alpha,\sigma,\tau)$ | Relator congruence |
| --- | --- |
| $(0,0,0)$ | $2a+4s=0$ |
| $(0,0,1)$ | $2(a+s)=0$ |
| $(0,1,0)$ | $2(a+y)=0$ |
| $(0,1,1)$ | $2(a+s-y)=0$ |
| $(1,0,0)$ | $4s=0$ |
| $(1,0,1)$ | $2s=0$ |
| $(1,1,0)$ | $2y=0$ |
| $(1,1,1)$ | $2(s-y)=0$ |

## 3. Generation occurs modulo the Frattini subgroup

The Frattini quotient of $D_{2^m}$ is

$$
D_{2^m}/\Phi(D_{2^m})
\cong C_2\times C_2.
\tag{10}
$$

In the coordinates (5), the image of $(a,\alpha)$ is

$$
(a\bmod2,\alpha).
\tag{11}
$$

By the Burnside basis theorem, $A,S,Y$ generate $D_{2^m}$ precisely
when the three vectors in (11) span $\mathbb F_2^2$.

The all-rotation pattern $(0,0,0)$ never generates. The remaining seven
patterns can be counted independently.

## 4. The seven counts

Assume first that $m\ge4$, so $8\mid N$.

### Six regular patterns

For each of

$$
(0,0,1),\ (0,1,0),\ (0,1,1),\
(1,0,1),\ (1,1,0),\ (1,1,1),
\tag{12}
$$

the relator table and the spanning condition leave exactly

$$
N^2
\tag{13}
$$

generating triples.

For example, in pattern $(0,0,1)$ the relation is

$$
a+s=0\pmod{N/2}.
$$

The reflection supplied by $Y$ means generation requires a nonzero
rotation vector. Because $N/2$ is even, the congruence forces $a$ and
$s$ to have the same parity, so both must be odd. There are $N/2$
choices for $a$, two compatible choices for $s$, and $N$ choices for
$y$, giving $N^2$. The other five patterns give the same count by the
same parity calculation.

### Exceptional pattern

For $(\alpha,\sigma,\tau)=(1,0,0)$, the relator is

$$
4s=0\pmod N.
\tag{14}
$$

When $8\mid N$, equation (14) has four solutions, all even. Thus the
rotation $Y$ must have odd exponent. The choices are:

$$
N\ \text{for }a,\qquad
4\ \text{for }s,\qquad
\frac N2\ \text{for }y,
$$

for a total of

$$
2N^2.
\tag{15}
$$

Combining (13) and (15) gives

$$
6N^2+2N^2=8N^2=2^{2m+1},
$$

proving (2) for $m\ge4$.

### The group $D_8$

When $N=4$, equation (14) is automatic. Generation requires at least one
of $s,y$ to be odd. Three of their four parity patterns qualify, giving

$$
N\cdot\frac34N^2=3N^2
$$

triples in the exceptional pattern. The other six patterns still contribute
$N^2$ each. Hence

$$
6N^2+3N^2=9N^2=144.
$$

This proves (2). $\square$

## 5. Automorphisms and extension counts

Every automorphism has the form

$$
r\longmapsto r^u,\qquad
w\longmapsto r^vw,
\tag{16}
$$

where $u\in(\mathbb Z/N\mathbb Z)^\times$ and
$v\in\mathbb Z/N\mathbb Z$. Therefore

$$
|\mathrm{Aut}(D_{2^m})|
=N\varphi(N)
=N\frac N2
=2^{2m-3}.
$$

Equations (2) and (3) give (4).

## 6. What becomes visible beyond the abelian case

The finite abelian formula only sees
$D_0^{\mathrm{ab}}\cong C_2\oplus\mathbb Z_2^2$. The dihedral count is
the first point where the commutator in the source relator contributes.
Equation (9) converts it into a parity-sensitive linear correction.

This is the same dyadic architecture emphasized in the repository's
supercongruence work:

1. reduce to a finite binary shadow;
2. isolate the exceptional first-level pattern; and
3. count uniform higher lifts after that pattern is fixed.

The objects and conclusions are different: this comparison does not turn
the dihedral count into a supercongruence or make either result imply the
other.

## Verification

The exact checker
[`verify_gq2_dihedral_counts.py`](../verification/related/verify_gq2_dihedral_counts.py)

- evaluates the group law and Roe--Turturean relator directly;
- tests generation in the Frattini quotient;
- exhaustively enumerates all triples through $D_{128}$;
- verifies every reflection-pattern subtotal; and
- checks the closed count and automorphism quotient through $D_{2^{16}}$.

Run:

```text
python verification/related/verify_gq2_dihedral_counts.py
```

## Reference

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of
  $\mathbb Q_2$*][RT], especially Proposition 1.1 and Section 11,
  item 4.
