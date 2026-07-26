# The \(2\times2\times2\) hyperdeterminant: Fourier splitting and a supercongruence

## Status

This note proves exact discriminant-fiber counts for Cayley's
\(2\times2\times2\) hyperdeterminant over every finite field of odd
cardinality. Its additive Fourier coefficient contains a quadratic Gauss
sum. Pairing the coefficients attached to the two quadratic-character
classes removes that obstruction and gives a sharp integer
adjacent-extension supercongruence.

The matrix-pencil and quadratic-form ingredients are classical. A targeted
search did not locate the paired Fourier product or its exact
adjacent-\(p^r\) valuation. Those formulations are recorded as apparently
new, with literature priority provisional.

## Hyperdeterminant as a pencil discriminant

Write a \(2\times2\times2\) tensor as a pair \(T=(A,B)\) of
\(2\)-by-\(2\) matrices. Define

\[
\det(xA+yB)=a x^2+bxy+c y^2
\]

and

\[
\Delta(T):=b^2-4ac.
\tag{1}
\]

This is Cayley's hyperdeterminant, up to the harmless choice of tensor
coordinates.

Let \(q\) be odd and let \(\chi\) be the quadratic character of
\(\mathbf F_q^\times\). For \(t\in\mathbf F_q\), put

\[
N_t(q):=\#\{T\in M_2(\mathbf F_q)^2:\Delta(T)=t\}.
\]

## Exact fibers

### Theorem 1

For every odd prime power \(q\),

\[
\boxed{N_0(q)=q^7+q^4-q^3.}
\tag{2}
\]

For \(t\neq0\),

\[
\boxed{
N_t(q)=
\begin{cases}
q^3(q-1)(q+1)^3,&\chi(t)=1,\\[2mm]
q^3(q-1)^3(q+1),&\chi(t)=-1.
\end{cases}}
\tag{3}
\]

### Proof

We split according to the rank of \(A\).

If \(A\) is invertible, write \(B=AC\). Then

\[
\Delta(A,B)=(\det A)^2
\left((\operatorname{tr}C)^2-4\det C\right).
\tag{4}
\]

For any fixed nonzero \(\delta\), the number of \(C\in M_2(\mathbf F_q)\)
with

\[
(\operatorname{tr}C)^2-4\det C=\delta
\]

is

\[
q(q^2+q\chi(\delta)).
\tag{5}
\]

Indeed, after the invertible change of coordinates

\[
u=a+d,\qquad x=a-d,\qquad y=2b,\qquad z=2c,
\]

the discriminant becomes \(x^2+yz\), while \(u\) is free. For fixed \(x\),
the equation \(yz=\delta-x^2\) has \(q-1\) solutions unless its right side
is zero, in which case it has \(2q-1\). Since
\(x^2=\delta\) has \(1+\chi(\delta)\) solutions, (5) follows.

There are

\[
|\operatorname{GL}_2(\mathbf F_q)|
=q(q-1)^2(q+1)
\]

choices for invertible \(A\).

If \(A\) has rank one, left-right equivalence reduces it to
\(\operatorname{diag}(1,0)\). Writing

\[
B=\begin{pmatrix}e&f\\g&h\end{pmatrix},
\]

the pencil discriminant is \(h^2\). Thus a fixed nonzero square value has
\(2q^3\) preimages in \(B\), while a nonsquare has none. The number of
rank-one \(2\)-by-\(2\) matrices is

\[
\frac{(q^2-1)^2}{q-1}=(q-1)(q+1)^2.
\]

Finally, \(A=0\) contributes only to the zero fiber.

Combining the invertible and rank-one contributions gives (3). Subtracting
all nonzero fibers from the total \(q^8\) gives (2). \(\square\)

As a consistency check, summing (3) over all nonzero \(t\) gives

\[
q^8-N_0(q)=(q^4-1)(q^4-q^3),
\]

the known Musiker--Yu count of nondegenerate \(2\times2\times2\) tensors.

## The Fourier coefficient

Let

\[
\psi:(\mathbf F_q,+)\longrightarrow\mathbf C^\times
\]

be nontrivial and define

\[
\mathcal H_q(\psi)
:=\sum_{T\in M_2(\mathbf F_q)^2}\psi(\Delta(T)).
\tag{6}
\]

Let

\[
G_q(\chi,\psi)
:=\sum_{t\in\mathbf F_q^\times}\chi(t)\psi(t)
\]

be the quadratic Gauss sum.

### Theorem 2

For every odd prime power \(q\),

\[
\boxed{
\mathcal H_q(\psi)
=q^4\left(1+2(q^2-1)G_q(\chi,\psi)\right).
}
\tag{7}
\]

### Proof

The additive-character sums over the nonzero squares and nonsquares are

\[
\sum_{\chi(t)=1}\psi(t)=\frac{-1+G_q(\chi,\psi)}2,
\qquad
\sum_{\chi(t)=-1}\psi(t)=\frac{-1-G_q(\chi,\psi)}2.
\]

Substitution of (2) and (3) gives (7). \(\square\)

Since \(|G_q(\chi,\psi)|=\sqrt q\), the normalized Fourier bias is of order
\(q^{-3/2}\). This differs from the integral \(q^{-2}\) and \(q^{-3}\)
behaviors of determinant and Pfaffian: the square-valued relative weight has
introduced a genuine Gauss-sum obstruction.

## Pairing the two character classes

Choose any nonsquare \(\nu\in\mathbf F_q^\times\) and set

\[
\psi_\nu(t):=\psi(\nu t).
\]

Then

\[
G_q(\chi,\psi_\nu)=-G_q(\chi,\psi).
\]

Define the paired Fourier product

\[
\mathcal K(q)
:=\mathcal H_q(\psi)\mathcal H_q(\psi_\nu).
\tag{8}
\]

It is independent of both choices.

### Theorem 3

Let

\[
\varepsilon(q):=\chi(-1)\in\{-1,1\}.
\]

Then

\[
\boxed{
\mathcal K(q)
=q^8\left(1-4\varepsilon(q)q(q^2-1)^2\right)
\in\mathbf Z.
}
\tag{9}
\]

### Proof

Multiply the two instances of (7) and use the standard identity

\[
G_q(\chi,\psi)^2=\chi(-1)q.
\]

This gives (9). \(\square\)

When the two Fourier coefficients are Galois conjugate, (8) is literally a
field norm. The phrase “paired Fourier product” is used because in even
extension degree the two values need not be conjugate over \(\mathbf Q\).

## Sharp adjacent-extension supercongruence

For an odd prime \(p\) and \(r\geq1\), write

\[
\mathcal K_{p,r}:=\mathcal K(p^r).
\]

Here

\[
\varepsilon(p^r)=
\begin{cases}
1,&p^r\equiv1\pmod4,\\
-1,&p^r\equiv3\pmod4.
\end{cases}
\]

### Theorem 4

For every odd prime \(p\) and every \(r\geq2\),

\[
\boxed{
v_p(\mathcal K_{p,r}-\mathcal K_{p,r-1})=8(r-1).
}
\tag{10}
\]

Thus

\[
\mathcal K_{p,r}
\equiv\mathcal K_{p,r-1}
\pmod {p^{8(r-1)}},
\tag{11}
\]

and the exponent is sharp.

### Proof

Equation (9) has the form

\[
\mathcal K_{p,r}=p^{8r}U_{p,r},
\qquad U_{p,r}\equiv1\pmod p.
\]

Therefore

\[
\mathcal K_{p,r}-\mathcal K_{p,r-1}
=p^{8(r-1)}(p^8U_{p,r}-U_{p,r-1}).
\]

The parenthesized factor is \(-1\) modulo \(p\), proving (10).
\(\square\)

## What this adds to the program

The first two relative invariants had surjective scaling weights, so all
nonzero fibers were uniform. Hyperdeterminant scales by a square:

\[
\Delta((g_1,g_2,g_3)\cdot T)
=(\det g_1\det g_2\det g_3)^2\Delta(T).
\]

Its nonzero fibers therefore split into two quadratic classes. The resulting
Gauss sum is not noise; it is the exact obstruction to an integer counting
polynomial. Pairing the two Fourier classes restores an integer invariant and
an exact supercongruence.

This suggests a broader relative-invariant program indexed by the cokernel of
the scaling character:

1. surjective weight: one uniform nonzero class;
2. square weight: quadratic Gauss packet;
3. higher-index weight: a packet of higher multiplicative-character sums.

The hyperdeterminant theorem proves the second branch in the smallest
nontrivial case.

## Literature boundary

The nearest general reference located was:

- T. Taniguchi and F. Thorne,
  [Orbital exponential sums for prehomogeneous vector spaces](https://arxiv.org/abs/1607.07827).
- S. Sam,
  [Counting matrices over finite fields](https://mathweb.ucsd.edu/~ssam/talks/2011/finitefield.pdf),
  reports the Musiker--Yu total nondegenerate count
  \((q^4-1)(q^4-q^3)\).

Searches by “finite-field hyperdeterminant exponential sum,” “Cayley
hyperdeterminant character sum,” the square/nonsquare refinement of the known
total count, and the adjacent-extension exponent found no direct match. This
does not settle priority.

## Verification

The companion
[`verify_hyperdeterminant_fourier.py`](../verification/related/verify_hyperdeterminant_fourier.py)

- exhaustively enumerates \(q^8\) tensors for \(q=3,5,7\);
- checks every individual discriminant fiber against (2) and (3);
- verifies the paired product (9);
- checks the exact valuation (10) on a larger prime-and-extension grid.
