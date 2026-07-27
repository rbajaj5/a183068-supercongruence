# From an isosceles triangulation to a Hamming-scheme supercongruence

## Status

The 2008 USAMO Problem 4 classifies the regular polygons admitting a
triangulation entirely by isosceles triangles. This note strengthens the
classification to an exact enumeration, identifies its binary support with a
radius-two Hamming ball, diagonalizes that ball by the Walsh transform, and
extracts a new polynomial supercongruence family.

The USAMO problem and its dyadic descent are established. Krawtchouk/Walsh
analysis of Hamming balls is classical. The exact enumeration and the
assembled supercongruence package are new deductions within this repository;
literature priority remains provisional.

## 1. Exact enumeration of the USAMO triangulations

Let \(T(n)\) be the number of triangulations of a fixed labeled regular
\(n\)-gon in which every triangle is isosceles. Rotations are counted as
different whenever they give different diagonal sets.

Write

\[
n=2^a m,
\qquad
m\ \text{odd}.
\tag{1}
\]

### Theorem 1

For \(n\geq3\),

\[
\boxed{
T(n)=
\begin{cases}
n/2,&m=1,\\
2^a=n/3,&m=3,\\
n,&m=2^b+1\text{ for some }b\geq2,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{2}
\]

Consequently \(T(n)>0\) exactly when the binary expansion of \(n\) has at
most two nonzero digits, recovering the USAMO classification.

### Proof

Call a polygon edge a *short side*. In an even regular \(2u\)-gon, an
isosceles triangle containing a short side must use the adjacent short side:
there is no opposite vertex on the perpendicular bisector of a short side.
Thus the short sides are paired into ears. The cycle of \(2u\) short sides
has exactly two alternating perfect matchings. Removing the corresponding
ears leaves a regular \(u\)-gon, and every admissible triangulation of that
central polygon lifts through either matching. Hence

\[
T(2u)=2T(u)
\qquad(u\geq3),
\tag{3}
\]

with \(T(4)=2\).

Now let \(m\geq5\) be odd. A short side can lie either in a small ear or in
the unique *big* isosceles triangle whose apex is the opposite vertex. The
odd cycle cannot be completely paired into small ears, so a big triangle is
necessary. Every big triangle contains the center, so there can be only one.

After its base short side is selected, the two remaining regions are forced
by the maximal-chord argument from the USAMO solution. To make the counting
precise, let \(R(k)\) count admissible triangulations of a region bounded by
an arc of \(k\) short sides and its spanning chord, with that chord maximal.
The chord must be the base of the adjacent isosceles triangle. Its apex is
the midpoint of the arc, so no triangulation exists when \(k>1\) is odd,
whereas

\[
R(1)=1,
\qquad
R(2k)=R(k)^2.
\]

It follows that \(R(k)=1\) when \(k\) is a power of two and \(R(k)=0\)
otherwise. The two sides of a fixed big triangle both have
\(k=(m-1)/2\). Hence a completion exists exactly when

\[
m-1=2^b.
\tag{4}
\]

When (4) holds, both regions have a unique completion, so each of the \(m\)
choices of the big triangle's base gives exactly one triangulation. Thus
\(T(m)=m\). If (4) fails, \(T(m)=0\). Finally \(T(3)=1\). Iterating (3)
gives every line of (2). \(\square\)

The first values are

\[
1,2,5,2,0,4,9,10,0,4,0,0,0,8,17,\ldots
\]

for \(n=3,4,\ldots\).

## 2. The binary support is a Hamming ball

Fix a bit length \(d\). Integers in \([0,2^d)\) are identified with the
group

\[
G_d=(\mathbf F_2)^d.
\]

The USAMO support condition “a sum of at most two powers of two” becomes

\[
H_d=\{x\in G_d:|x|\leq2\},
\tag{5}
\]

the Hamming ball of radius two. Let \(h_d=1_{H_d}\).

For \(y\in G_d\), write \(s=|y|\). Its Walsh coefficient is

\[
\widehat h_d(y)
=
\sum_{x\in H_d}(-1)^{x\cdot y}.
\tag{6}
\]

### Theorem 2 (complete Walsh spectrum)

The coefficient (6) depends only on \(s\), and

\[
\boxed{
\lambda_{d,s}
=
1+(d-2s)+\frac{(d-2s)^2-d}{2}.
}
\tag{7}
\]

### Proof

Split (6) according to Hamming weight \(0,1,2\). Weight zero contributes
\(1\). At weight one, \(d-s\) coordinates contribute \(+1\) and \(s\)
contribute \(-1\), giving \(d-2s\). At weight two, the contribution is

\[
\binom{d-s}{2}+\binom{s}{2}-s(d-s)
=
\frac{(d-2s)^2-d}{2}.
\]

Adding the three terms proves (7). \(\square\)

Thus the \(2^d\)-point Walsh transform has only \(d+1\) distinct values.
The orbit-spectrum compiler reduces arbitrary convolution powers from the
full Boolean cube to the Hamming association scheme.

## 3. Exact XOR-convolution powers

For \(\ell\geq1\) and \(z\in G_d\), let

\[
C_{\ell,d}(z)
=
\#\{(x_1,\ldots,x_\ell)\in H_d^\ell:
x_1+\cdots+x_\ell=z\}.
\tag{8}
\]

The value depends only on \(|z|\). Walsh inversion and (7) give an
\(O(d^2+d\log\ell)\) compressed algorithm for all \(d+1\) orbit values,
rather than a \(2^d\)-point Walsh--Hadamard transform.

At \(z=0\), the formula simplifies to

\[
\boxed{
Z_\ell(d):=C_{\ell,d}(0)
=
2^{-d}\sum_{s=0}^{d}\binom ds\lambda_{d,s}^{\ell}.
}
\tag{9}
\]

### Theorem 3 (polynomiality)

For fixed \(\ell\), \(Z_\ell(d)\) is an integer-valued polynomial in \(d\)
of degree at most \(\ell\). More precisely,

\[
\boxed{
Z_\ell(d)
=
\sum_{v=0}^{\ell}c_{\ell,v}\binom dv,
}
\tag{10}
\]

where \(c_{\ell,v}\) is the number of ordered \(\ell\)-tuples of subsets of
\([v]\), each of size at most two, whose symmetric difference is empty and
whose union is all of \([v]\).

### Proof

Interpret each \(x_j\) as a subset of \([d]\) of size at most two. Their XOR
is zero exactly when every used coordinate occurs an even number of times.
There are at most \(2\ell\) incidences, and every used coordinate contributes
at least two, so at most \(\ell\) coordinates are used.

If exactly \(v\) coordinates are used, choose them in \(\binom dv\) ways.
After relabeling them increasingly by \([v]\), there are
\(c_{\ell,v}\) full-support configurations. Summing over \(v\) proves
(10). \(\square\)

This proof also explains why a superficially exponential convolution count
becomes a degree-\(\ell\) polynomial.

## 4. The adjacent-extension supercongruence

Define the integer

\[
A_\ell=\ell!\,Z_\ell'(0).
\tag{11}
\]

It is integral because (10) has degree at most \(\ell\) in the binomial
basis.

### Theorem 4

Let \(\ell\geq2\), let \(p>\ell\) be prime, and let \(r\geq2\). Then

\[
\boxed{
Z_\ell(p^r)
\equiv
Z_\ell(p^{r-1})
\pmod {p^{r-1}}.
}
\tag{12}
\]

Moreover, if \(p\nmid A_\ell\), then the exponent is sharp:

\[
\boxed{
v_p\!\left(
Z_\ell(p^r)-Z_\ell(p^{r-1})
\right)
=r-1.
}
\tag{13}
\]

### Proof

Because \(p>\ell\), the polynomial \(Z_\ell(X)\) has coefficients in
\(\mathbf Z_{(p)}\). For \(x=p^r\) and \(y=p^{r-1}\),

\[
Z_\ell(x)-Z_\ell(y)
=(x-y)Z_\ell'(0)+O(y^2).
\tag{14}
\]

The first term is divisible by \(p^{r-1}\), and the error is divisible by
\(p^{2r-2}\), hence by \(p^r\). This proves (12). After division by
\(p^{r-1}\), equation (14) is congruent modulo \(p\) to

\[
-Z_\ell'(0).
\]

Since \(\ell!\) is a \(p\)-adic unit, this residue is nonzero exactly when
\(p\nmid A_\ell\), proving (13). \(\square\)

For \(\ell=2,3,4,5\), the values

\[
A_\ell=1,\ 3,\ 96,\ -3840
\]

have no prime divisor exceeding \(\ell\), so (13) holds for every allowed
prime. At \(\ell=6\),

\[
A_6=474120
=2^3\cdot3^3\cdot5\cdot439.
\tag{15}
\]

Thus \(p=439\) is the first exceptional prime in this tower.

### Corollary 5 (the first exceptional lift)

For every \(r\geq2\),

\[
\boxed{
v_{439}\!\left(
Z_6(439^r)-Z_6(439^{r-1})
\right)
=r.
}
\tag{16}
\]

### Proof

Interpolation from (10), or direct expansion of (9), gives

\[
\begin{aligned}
Z_6(d)=\frac18(&755d^6-3639d^5+6695d^4-1505d^3\\
&-7326d^2+5268d+8).
\end{aligned}
\tag{17}
\]

Its linear coefficient is

\[
\frac{1317}{2}=\frac{3\cdot439}{2}.
\]

For \(r\geq3\), the linear term in (14) has valuation \(r\), while the
quadratic and higher terms have valuation at least \(2r-2>r\). For \(r=2\),
dividing the difference by \(439^2\) gives residue

\[
-\frac32+\frac{3663}{4}
=\frac{3657}{4}
\equiv146\not\equiv0\pmod {439}.
\]

This proves (16). \(\square\)

## 5. Interpretation and boundary

The chain of ideas is:

\[
\text{forced halving in a polygon}
\longrightarrow
\text{binary Hamming support}
\longrightarrow
\text{Krawtchouk/Walsh packets}
\longrightarrow
\text{polynomial convolution counts}
\longrightarrow
\text{\(p\)-adic adjacent towers}.
\]

The algorithmic gain is real for this structured input: the orbit
description replaces \(2^d\) spectral coefficients by \(d+1\). It is not an
improvement to the general FFT or Walsh--Hadamard transform. An audio or
circadian application would first need to identify the corresponding
low-weight or low-orbit spectral model.

## 6. Verification and literature boundary

The checker
[`verify_usamo_hamming_supercongruence.py`](../verification/related/verify_usamo_hamming_supercongruence.py)
verifies:

1. the triangulation recurrence and formula (2);
2. the complete Walsh spectrum (7);
3. direct XOR convolution against (9);
4. the binomial-basis polynomial (10);
5. the congruence and sharpness criteria (12)--(13); and
6. the exceptional \(p=439\) valuation (16).

Run:

```text
python verification/related/verify_usamo_hamming_supercongruence.py
```

Sources and neighboring literature:

- [2008 USAMO Problem 4 and the dyadic
  solution](https://artofproblemsolving.com/wiki/index.php?title=2008_USAMO_Problems/Problem_4);
- the Walsh/Krawtchouk theory of Hamming association schemes, which supplies
  the classical ambient language for (7)--(9).

A targeted search found the USAMO existence classification and general
polygon-triangulation counting literature, but no direct match for the exact
enumeration (2) or the supercongruence tower (12)--(16). This is preliminary
priority evidence, not a novelty certificate.
