# Exact $G_{\mathbb Q_2}$ surjection counts for generalized quaternion groups

## Status and source boundary

Roe and Turturean ask for explicit formulas for the number of surjections
from $G_{\mathbb Q_2}$ to a finite group. Their marked maximal pro-2
presentation turns the generalized-quaternion case into a short coordinate
calculation.

The numerical enumeration is not new. Yamagishi gave a general method for
counting local Galois $p$-extensions, and later work implemented that method
for $\mathbb Q_2$. In particular, published tables contain the $Q_8$ and
$Q_{16}$ cases. The contribution of this page is a direct proof from the
Roe--Turturean relator, a closed all-orders formula, and an executable exact
certificate.

[RT]: https://roed314.github.io/gq2/paper/paper.html
[Yamagishi]: https://doi.org/10.1090/S0002-9939-1995-1264832-0
[ABS]: https://facstaff.elon.edu/cawtrey/abs-galois2adic.pdf

## 1. The result

For $m\ge3$, write $Q_{2^m}$ for the generalized quaternion group of order
$2^m$.

### Theorem

The exact surjection count is

$$\boxed{\left|\mathrm{Sur}(G_{\mathbb Q_2},Q_{2^m})\right|=\begin{cases}144,&m=3,\\640,&m=4,\\2^{2m+1},&m\ge5.\end{cases}} \tag{1}$$

After quotienting by target automorphisms, the corresponding numbers of
Galois extensions of $\mathbb Q_2$ are:

| Target | Surjections | Automorphisms | Extension classes |
| --- | ---: | ---: | ---: |
| $Q_8$ | $144$ | $24$ | $6$ |
| $Q_{16}$ | $640$ | $32$ | $20$ |
| $Q_{2^m}$, $m\ge5$ | $2^{2m+1}$ | $2^{2m-3}$ | $16$ |

Thus the quaternion tower has two exceptional bottom levels and then
stabilizes at exactly $16$ extension classes.

## 2. Quaternion coordinates

Put $N=2^{m-1}$. Use the presentation

$$Q_{2^m}=\left\langle r,w\ \middle|\ r^N=1,\quad w^2=r^{N/2},\quad wrw^{-1}=r^{-1}\right\rangle. \tag{2}$$

Write every element uniquely as

$$(a,\alpha)=r^aw^\alpha,\qquad a\in\mathbb Z/N\mathbb Z,\quad\alpha\in\mathbb F_2. \tag{3}$$

The multiplication law is

$$(a,\alpha)(b,\beta)=\left(a+(-1)^\alpha b+\alpha\beta\frac N2,\ \alpha+\beta\right). \tag{4}$$

The final coordinate in (4) is taken modulo $2$. The extra central term
$\alpha\beta N/2$ is the only change from the dihedral calculation, but it
is exactly what creates the two low-order exceptions.

## 3. Evaluate the dyadic relator

Every map to a finite $2$-group factors through the marked maximal pro-2
quotient in Roe--Turturean Proposition 1.1:

$$D_0=\left\langle A,S,Y\ \middle|\ A^2S^4[S,Y]=1\right\rangle_{\mathrm{pro}\text{-}2},\qquad[S,Y]=S^{-1}Y^{-1}SY. \tag{5}$$

Choose

$$A=(a,\alpha),\qquad S=(s,\sigma),\qquad Y=(y,\tau). \tag{6}$$

The commutator has the same rotation coordinate as in the dihedral group:

$$[S,Y]_r=(-1)^\sigma\left((-1)^\tau-1\right)s+(-1)^\tau\left(1-(-1)^\sigma\right)y. \tag{7}$$

The quaternion square changes the other term:

$$A^2=\begin{cases}(2a,0),&\alpha=0,\\(N/2,0),&\alpha=1.\end{cases} \tag{8}$$

Consequently the eight reflection patterns reduce the relator to the
following congruences modulo $N$.

| $(\alpha,\sigma,\tau)$ | Quaternion relator |
| --- | --- |
| $(0,0,0)$ | $2a+4s=0$ |
| $(0,0,1)$ | $2(a+s)=0$ |
| $(0,1,0)$ | $2(a+y)=0$ |
| $(0,1,1)$ | $2(a+s-y)=0$ |
| $(1,0,0)$ | $N/2+4s=0$ |
| $(1,0,1)$ | $N/2+2s=0$ |
| $(1,1,0)$ | $N/2+2y=0$ |
| $(1,1,1)$ | $N/2+2(s-y)=0$ |

## 4. Generation is a two-bit condition

The Frattini quotient is

$$Q_{2^m}/\Phi(Q_{2^m})\cong C_2\times C_2, \tag{9}$$

and the image of $(a,\alpha)$ is $(a\bmod2,\alpha)$. By the Burnside basis
theorem, the triple in (6) generates $Q_{2^m}$ exactly when its three
two-bit vectors span $\mathbb F_2^2$.

The all-rotation pattern $(0,0,0)$ therefore contributes nothing. What
remains is an elementary count in the other seven patterns.

## 5. Count the seven patterns

The three patterns with $\alpha=0$ contribute $N^2$ each for every
$m\ge3$:

| Pattern | Relation after division by $2$ | Generating condition | Count |
| --- | --- | --- | ---: |
| $(0,0,1)$ | $a+s=0\pmod{N/2}$ | $a$ and $s$ odd | $N^2$ |
| $(0,1,0)$ | $a+y=0\pmod{N/2}$ | $a$ and $y$ odd | $N^2$ |
| $(0,1,1)$ | $a+s-y=0\pmod{N/2}$ | $a$ odd | $N^2$ |

The four patterns with $\alpha=1$ detect the central square.

### Pattern 100

Here the relation is

$$\frac N2+4s=0\pmod N. \tag{10}$$

- If $N=4$, equation (10) is impossible, so the count is $0$.
- If $N=8$, equation (10) says that $s$ is odd. Generation is then
  automatic, and the count is $N\cdot(N/2)\cdot N=4N^2$.
- If $N\ge16$, equation (10) has four solutions for $s$, all even.
  Generation then requires $y$ odd, giving $N\cdot4\cdot(N/2)=2N^2$.

### Patterns 101 and 110

For $(1,0,1)$ the relation is

$$\frac N2+2s=0\pmod N. \tag{11}$$

It has two solutions for $s$. When $N=4$ they are odd, so the count is
$2N^2$. When $N\ge8$ they are even, and generation requires $a$ and $y$
to have opposite parity, so the count is $N^2$. The pattern $(1,1,0)$ is
identical with $s$ and $y$ exchanged.

### Pattern 111

Now

$$\frac N2+2(s-y)=0\pmod N. \tag{12}$$

When $N=4$, the difference $s-y$ is odd, so the two reflection vectors
already generate and the count is $2N^2$. When $N\ge8$, the difference is
even; $S$ and $Y$ have the same Frattini image, and $A$ must have the
opposite parity. The count is then $N^2$.

The complete pattern table is therefore:

| Pattern | $Q_8$ | $Q_{16}$ | $Q_{2^m}$, $m\ge5$ |
| --- | ---: | ---: | ---: |
| $(0,0,0)$ | $0$ | $0$ | $0$ |
| each of $(0,0,1),(0,1,0),(0,1,1)$ | $N^2$ | $N^2$ | $N^2$ |
| $(1,0,0)$ | $0$ | $4N^2$ | $2N^2$ |
| each of $(1,0,1),(1,1,0),(1,1,1)$ | $2N^2$ | $N^2$ | $N^2$ |

Summing the columns gives

$$9N^2=144,\qquad10N^2=640,\qquad8N^2=2^{2m+1}, \tag{13}$$

respectively. This proves (1).

## 6. Divide by automorphisms

The group $Q_8$ is exceptional: it has three cyclic subgroups of order
$4$, and its automorphism group has order $24$.

For $m\ge4$, the rotation subgroup is characteristic, and every
automorphism is uniquely of the form

$$r\longmapsto r^u,\qquad w\longmapsto r^vw, \tag{14}$$

where $u$ is odd modulo $N$ and $v$ is arbitrary modulo $N$. Hence

$$\left|\mathrm{Aut}(Q_{2^m})\right|=N\varphi(N)=\frac{N^2}{2}=2^{2m-3}. \tag{15}$$

Postcomposition by target automorphisms acts freely on surjections.
Dividing (1) by (15), with the separate order-24 calculation for $Q_8$,
gives $6$, $20$, and $16$ extension classes.

## 7. External checks

The independent tables of Awtrey--Beuerle--Schrader give $20$ fields with
Galois group $Q_{16}$ in their Table 3. Their octic tables list exactly six
fields with Galois group $Q_8$. These agree with the first two quotients
above.

Yamagishi's theorem supplies a general character-theoretic counting formula
for finite $p$-group targets over local fields and explicitly treats
generalized quaternion groups. The present argument is different in form:
it starts with the marked three-generator relator and reduces the entire
family to seven congruence fibers.

## 8. What the boundary teaches

The dihedral and quaternion towers have the same Frattini quotient and the
same commutator formula. They differ only in the square of a reflection:

$$w^2=1\quad\text{versus}\quad w^2=r^{N/2}. \tag{16}$$

At $Q_8$ and $Q_{16}$, that central half-turn changes the parity of the
relator fibers. From $Q_{32}$ onward it lies deep enough in the rotation
filtration that the count becomes uniform. This is a concrete instance of
the repository's dyadic principle: a stable lift law can begin only after
the first exceptional binary layers have been computed separately.

This analogy is structural. The result is a local Galois-group count, not a
supercongruence.

## Verification

The exact checker
[`verify_gq2_quaternion_counts.py`](../verification/related/verify_gq2_quaternion_counts.py)

- verifies the quaternion multiplication and inverse laws;
- verifies the coordinate formula for the Roe--Turturean relator;
- exhaustively enumerates all triples through $Q_{128}$;
- checks every reflection-pattern subtotal; and
- checks the closed automorphism quotients through $Q_{2^{16}}$.

Run:

```text
python verification/related/verify_gq2_quaternion_counts.py
```

## References

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of Q₂*][RT], especially
  Proposition 1.1 and Section 11.
- M. Yamagishi,
  [*On the number of Galois p-extensions of a local field*][Yamagishi],
  Proc. Amer. Math. Soc. 123 (1995), 2373--2380.
- C. Awtrey, J. Beuerle, and J. Schrader,
  [*Constructing Galois 2-extensions of the 2-adic Numbers*][ABS],
  North Carolina J. Math. Stat. 3 (2017).
