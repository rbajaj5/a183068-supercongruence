# Semidihedral and modular counts from the $G_{\mathbb Q_2}$ relator

## Status and prior work

Ito and Yamagishi already calculated the numbers of semidihedral and modular
extensions of a local field. For $\mathbb Q_2$, their Example 7 gives
exactly the extension counts recovered below. Awtrey, Beuerle, and Schrader
also list the order 16 cases in their complete table of degree 16
$2$-adic fields.

The contribution of this page is therefore **not a new enumeration**. It is
a short direct derivation from the Roe--Turturean three-generator relator,
together with an executable all-orders certificate. It completes the
maximal-cyclic nonabelian families adjacent to the
[dihedral](GQ2DihedralCounts.md) and
[generalized-quaternion](GQ2QuaternionCounts.md) calculations.

[RT]: https://roed314.github.io/gq2/paper/paper.html
[IY]: https://doi.org/10.3792/pjaa.83.10
[ABS]: https://facstaff.elon.edu/cawtrey/abs-galois2adic.pdf

## 1. The result

For $m\ge4$, let $SD_{2^m}$ and $M_{2^m}$ denote the semidihedral and
modular groups of order $2^m$.

### Theorem

The semidihedral surjection count is

$$
\boxed{
\left|\mathrm{Sur}(G_{\mathbb Q_2},SD_{2^m})\right|=
\begin{cases}
576,&m=4,\\
2^{2m+1},&m\ge5.
\end{cases}}
$$

The modular surjection count is

$$
\boxed{
\left|\mathrm{Sur}(G_{\mathbb Q_2},M_{2^m})\right|
=9\cdot2^{2m-2}.}
$$

After division by target automorphisms, the corresponding extension counts
are:

| Family | Surjections | Automorphisms | Extension classes |
| --- | ---: | ---: | ---: |
| $SD_{16}$ | $576$ | $16$ | $36$ |
| $SD_{2^m}$, $m\ge5$ | $2^{2m+1}$ | $2^{2m-4}$ | $32$ |
| $M_{2^m}$, $m\ge4$ | $9\cdot2^{2m-2}$ | $2^m$ | $9\cdot2^{m-2}$ |

These extension counts agree exactly with Ito--Yamagishi Example 7.

## 2. One coordinate model for both families

Put

$$
N=2^{m-1},\qquad h=N/2.
$$

For a unit $u$ satisfying $u^2=1$ modulo $N$, write

$$
G_u(N)=
\left\langle r,w\ \middle|\
r^N=w^2=1,\quad wrw^{-1}=r^u
\right\rangle .
$$

The two families are

$$
SD_{2^m}=G_{h-1}(N),\qquad
M_{2^m}=G_{h+1}(N).
$$

Write elements as

$$
(a,\alpha)=r^aw^\alpha,
\qquad a\in\mathbb Z/N\mathbb Z,\quad\alpha\in\mathbb F_2.
$$

Multiplication is

$$
(a,\alpha)(b,\beta)=
\left(a+u^\alpha b,\alpha+\beta\right).
$$

The Frattini quotient is $C_2^2$, with

$$
(a,\alpha)\longmapsto(a\bmod2,\alpha).
$$

Thus, by the Burnside basis theorem, three elements generate precisely when
their three two-bit images span $\mathbb F_2^2$.

## 3. The common relator calculation

Every map to a finite $2$-group factors through the Roe--Turturean maximal
pro-2 quotient

$$
D_0=
\left\langle A,S,Y\ \middle|\ A^2S^4[S,Y]=1\right\rangle_{\mathrm{pro}\text{-}2}.
$$

Choose

$$
A=(a,\alpha),\qquad S=(s,\sigma),\qquad Y=(y,\tau).
$$

With $[S,Y]=S^{-1}Y^{-1}SY$, direct multiplication gives

$$
[S,Y]_r=
u^\sigma(u^\tau-1)s
+u^\tau(1-u^\sigma)y.
$$

The other two rotation coordinates are

$$
(A^2)_r=
\begin{cases}
2a,&\alpha=0,\\
(1+u)a,&\alpha=1,
\end{cases}
$$

and

$$
(S^4)_r=
\begin{cases}
4s,&\sigma=0,\\
2(1+u)s,&\sigma=1.
\end{cases}
$$

For each of the eight patterns $(\alpha,\sigma,\tau)$, the source relator
therefore becomes one linear congruence modulo $N$.

## 4. Semidihedral count

For $u=h-1$,

$$
1+u=h,\qquad
u(u-1)=h+2,\qquad
u(1-u)=-(h+2)
\pmod N.
$$

The relator table is:

| Pattern | Congruence modulo $N$ | Generating count |
| --- | --- | ---: |
| $000$ | $2a+4s=0$ | $0$ |
| $001$ | $2a+(h+2)s=0$ | $N^2$ |
| $010$ | $2a+(h+2)y=0$ | $N^2$ |
| $011$ | $2a+(h+2)(s-y)=0$ | $N^2$ |
| $100$ | $ha+4s=0$ | $3N^2$ if $N=8$; $2N^2$ if $N\ge16$ |
| $101$ | $ha+(h+2)s=0$ | $N^2$ |
| $110$ | $ha+(h+2)y=0$ | $N^2$ |
| $111$ | $ha+(h+2)(s-y)=0$ | $N^2$ |

Here is the parity count behind the table. In each of the six regular
nonzero patterns, division by $2$ leaves an odd coefficient. The relator
then fixes one coordinate modulo $N/2$, while the Frattini condition fixes
one parity. The remaining coordinate is free, giving $N^2$ solutions.

The $100$ pattern is the only boundary. For $N=8$, the relation says that
$a$ and $s$ have the same parity. Odd $s$ gives $2N^2$ generating triples;
even $s$ requires odd $y$ and gives another $N^2$.

For $N\ge16$, the equation has four choices of $s$ for each $a$, all with
$s$ even. Generation then requires $y$ odd, giving

$$
N\cdot4\cdot\frac N2=2N^2.
$$

Summing proves

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},SD_{16})\right|=9N^2=576
$$

and, for $m\ge5$,

$$
\left|\mathrm{Sur}(G_{\mathbb Q_2},SD_{2^m})\right|
=8N^2=2^{2m+1}.
$$

## 5. Modular count

For $u=h+1$,

$$
1+u=h+2,\qquad
u-1=1-u=u(u-1)=h
\pmod N.
$$

The relator table is:

| Pattern | Congruence modulo $N$ | Generating count |
| --- | --- | ---: |
| $000$ | $2a+4s=0$ | $0$ |
| $001$ | $2a+(h+4)s=0$ | $N^2$ |
| $010$ | $2a+4s+hy=0$ | $N^2$ |
| $011$ | $2a+4s+h(s-y)=0$ | $N^2$ |
| $100$ | $(h+2)a+4s=0$ | $3N^2/2$ |
| $101$ | $(h+2)a+(h+4)s=0$ | $3N^2/2$ |
| $110$ | $(h+2)a+4s+hy=0$ | $3N^2/2$ |
| $111$ | $(h+2)a+4s+h(s-y)=0$ | $3N^2/2$ |

To see the uniform count, put $c=h/2$. Since $c$ is even, each
$\alpha=0$ equation forces $a$ even. Generation then selects exactly half
of the relevant parity pairs, giving $N^2$ in each of the three nonzero
patterns.

For $\alpha=1$, division by $2$ makes the coefficient of $a$ equal to
$c+1$, which is odd, while every other coefficient is even. Thus $a$ is
again even. Each pattern has $2N^2$ relator solutions. Exactly one quarter
have both remaining rotation bits even and fail to generate, leaving

$$
\frac34\cdot2N^2=\frac{3N^2}{2}.
$$

The total is

$$
3N^2+4\left(\frac{3N^2}{2}\right)
=9N^2
=9\cdot2^{2m-2}.
$$

## 6. Automorphisms

For the semidihedral group, the rotation subgroup is characteristic.
An automorphism has

$$
r\longmapsto r^a,\qquad
w\longmapsto r^bw,
$$

where $a$ is odd and $b$ is even modulo $N$. Hence

$$
|\mathrm{Aut}(SD_{2^m})|
=\frac N2\cdot\frac N2
=\frac{N^2}{4}
=2^{2m-4}.
$$

For the modular group, there are exactly $N$ possible images of $r$ of
order $N$: the elements $(a,\alpha)$ with $a$ odd. For each such image,
the two admissible generating images of $w$ are $(0,1)$ and $(h,1)$.
Therefore

$$
|\mathrm{Aut}(M_{2^m})|=2N=2^m.
$$

Postcomposition by target automorphisms acts freely on surjections. Dividing
the two surjection formulas by these automorphism orders gives the extension
counts in the theorem.

## 7. What the four maximal-cyclic families show

Dihedral, quaternion, semidihedral, and modular $2$-groups all have a cyclic
subgroup of index two and the same two-dimensional Frattini shadow. The
source relation distinguishes them through only two pieces of target data:

1. the action exponent $u$ in $wrw^{-1}=r^u$; and
2. whether a reflection has a central square.

The finite shadow decides generation. One linear congruence then counts
the lifts. Exceptional low layers occur exactly when a coefficient such as
$4$ has not yet stabilized relative to the modulus $2^{m-1}$.

This is the same finite-shadow/uniform-lift architecture that motivates the
repository's dyadic supercongruence work. The result itself is a local
Galois enumeration, not a supercongruence.

## Verification

The exact checker
[`verify_gq2_maximal_cyclic_counts.py`](../verification/related/verify_gq2_maximal_cyclic_counts.py)

- verifies the group inverse and relator-coordinate identities;
- exhaustively enumerates every source triple through group order $128$;
- verifies every reflection-pattern subtotal;
- exhaustively counts automorphisms through group order $256$;
- checks the closed extension formulas through order $2^{16}$; and
- records the generator-rank obstruction for higher extraspecial targets.

Run:

```text
python verification/related/verify_gq2_maximal_cyclic_counts.py
```

## References

- D. Roe and D. Turturean,
  [*A Presentation of the Absolute Galois Group of Q₂*][RT],
  especially Proposition 1.1 and Section 11.
- M. Ito and M. Yamagishi,
  [*The number of semidihedral or modular extensions of a local field*][IY],
  Proc. Japan Acad. Ser. A 83 (2007), 10--14.
- C. Awtrey, J. Beuerle, and J. Schrader,
  [*Constructing Galois 2-extensions of the 2-adic Numbers*][ABS],
  North Carolina J. Math. Stat. 3 (2017).
