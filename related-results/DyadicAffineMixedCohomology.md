# The mixed dyadic obstruction in the Roe affine shadow

## Status and scope

This note closes the linear cohomology calculation stated as a target in the
[public Roe-inspired \(2\)-adic packet](../ROE_2ADIC.md). It is an elementary
calculation for the affine quotient

\[
\mathbb Z_2\rtimes\mathbb Z_2^\times.
\]

The source presentation and outer-automorphism quotient are from David Roe
and David Turturean,
[*A Presentation of the Absolute Galois Group of \(\mathbb Q_2\)*][RT].

It does **not** compute the kernel of
\(\mathrm{Out}(D_0)\twoheadrightarrow
\mathbb Z_2\rtimes\mathbb Z_2^\times\), identify the extension class carried
by that kernel, or decide whether the full quotient map splits. No novelty
claim is made.

[RT]: https://roed314.github.io/gq2/paper.pdf

We use continuous cohomology in the category of profinite
\(\mathbb Z_2\)-modules. Put

\[
G=\mathbb Z_2^\times,\qquad M=\mathbb Z_2(1),
\]

where \(M\) is the additive group \(\mathbb Z_2\) and \(u\in G\) acts by
multiplication by \(u\).

## 1. The cohomology calculation

### Theorem 1

There is a canonical isomorphism

\[
\boxed{
H^2_{\mathrm{cont}}(G,M)\cong\mathbb Z/2\mathbb Z.
}
\tag{1}
\]

Moreover, the nonzero class is mixed: its restrictions to both factors in

\[
G=\{\pm1\}\times(1+4\mathbb Z_2)
\tag{2}
\]

vanish.

### Proof

Write

\[
C_2=\{\pm1\},\qquad
\Gamma=1+4\mathbb Z_2.
\]

The group \(\Gamma\) is procyclic, with topological generator
\(\gamma=5\). Its completed group-ring resolution gives

\[
H^0_{\mathrm{cont}}(\Gamma,M)
=\ker(\gamma-1)=\ker(4:M\to M)=0,
\tag{3}
\]

\[
H^1_{\mathrm{cont}}(\Gamma,M)
=M/(\gamma-1)M
=\mathbb Z_2/4\mathbb Z_2,
\tag{4}
\]

and \(H^q_{\mathrm{cont}}(\Gamma,M)=0\) for \(q\ge2\).

The sign element in \(C_2\) commutes with \(\Gamma\), but acts on \(M\) by
\(-1\). It therefore acts by \(-1\) on the quotient in (4). The
Hochschild--Serre spectral sequence for

\[
1\longrightarrow\Gamma\longrightarrow G\longrightarrow C_2
\longrightarrow1
\]

has only the row \(q=1\). In total degree two it gives

\[
H^2_{\mathrm{cont}}(G,M)
\cong
H^1\!\left(C_2,\mathbb Z/4\mathbb Z\; \text{with sign action}\right).
\tag{5}
\]

If \(s\) is the nontrivial element of \(C_2\), the standard cyclic complex
alternates the maps \(s-1=-2\) and \(1+s=0\). Hence

\[
H^1(C_2,\mathbb Z/4\mathbb Z)
=
\frac{\ker(1+s)}{(s-1)(\mathbb Z/4\mathbb Z)}
=
\frac{\mathbb Z/4\mathbb Z}{2\mathbb Z/4\mathbb Z}
\cong\mathbb Z/2\mathbb Z.
\tag{6}
\]

This proves (1).

The restriction to \(\Gamma\) vanishes because
\(H^2_{\mathrm{cont}}(\Gamma,M)=0\). On \(C_2\), the action is again the
sign action, so

\[
H^2(C_2,M)
=
\frac{M^{C_2}}{(1+s)M}
=0,
\tag{7}
\]

because \(M\) is \(2\)-torsion-free and therefore \(M^{C_2}=0\).
Thus the nonzero class disappears on either factor separately. \(\square\)

## 2. An explicit representative

The mixed nature of (1) has a concrete group-theoretic model.

Let

\[
N=M\rtimes\Gamma,
\]

where \(\gamma=5\) acts on \(M\) by multiplication by \(5\). Write \(t(m)\)
for an element of the normal copy of \(M\), and let \(y\) lift \(\gamma\).
For \(a\in\mathbb Z_2\), define a continuous involution \(\varphi_a\) of
\(N\) by

\[
\varphi_a(t(m))=t(-m),
\qquad
\varphi_a(y)=t(a)y.
\tag{8}
\]

To see the formula on all of \(\Gamma\), put

\[
q(n)=\frac{5^n-1}{4}\in\mathbb Z_2
\qquad(n\in\mathbb Z_2).
\tag{9}
\]

Then

\[
\varphi_a\!\left(t(m)y^n\right)
=t\!\left(-m+a\,q(n)\right)y^n.
\tag{10}
\]

The identity

\[
q(n+n')=q(n)+5^nq(n')
\tag{11}
\]

shows that \(\varphi_a\) is a homomorphism, and (10) immediately gives
\(\varphi_a^2=1\).

Define

\[
E_a=N\rtimes_{\varphi_a}C_2.
\tag{12}
\]

If \(x\) is the nontrivial element of the final \(C_2\), then

\[
xt(m)x^{-1}=t(-m),
\qquad
xyx^{-1}=t(a)y.
\tag{13}
\]

Modulo \(M\), the images of \(x\) and \(y\) commute, so (12) is an extension

\[
0\longrightarrow M\longrightarrow E_a\longrightarrow
C_2\times\Gamma\longrightarrow1
\tag{14}
\]

with the prescribed \(G\)-action on \(M\).

### Theorem 2

The extension \(E_a\) splits if and only if \(a\in2\mathbb Z_2\). Two
extensions \(E_a\) and \(E_{a'}\) represent the same class if and only if

\[
a\equiv a'\pmod2.
\tag{15}
\]

Thus \(E_0\) represents zero and \(E_1\) represents the unique nonzero class
in (1).

### Proof

Every lift of the sign generator has the form \(t(c)x\), and every lift of
\(\gamma\) has the form \(t(b)y\). From (13),

\[
(t(c)x)(t(b)y)(t(c)x)^{-1}
=t(a-2b-4c)(t(b)y).
\tag{16}
\]

The two chosen lifts commute precisely when

\[
a=2b+4c.
\tag{17}
\]

Equation (17) has a solution \(b,c\in\mathbb Z_2\) exactly when \(a\) is
even. This proves the splitting criterion. Changing the lifts changes \(a\)
by an element of \(2\mathbb Z_2\), proving (15). \(\square\)

The important point is that both restricted extensions split visibly:
\(y\) supplies a section over \(\Gamma\), and \(x\) supplies a section over
\(C_2\). For odd \(a\), those two sections cannot be made compatible.

## 3. Consequence for the Roe splitting question

The linear proxy has exactly one possible obstruction bit. It is not detected
on the orientation-preserving procyclic factor or on the sign factor alone;
it measures their failure to admit compatible lifts.

This sharpens the next-step question but does not answer it. For the actual
surjection

\[
\mathrm{Out}(D_0)\twoheadrightarrow
\mathbb Z_2\rtimes\mathbb Z_2^\times,
\]

one still needs a natural abelian pushout of its generally nonabelian kernel
to \(M=\mathbb Z_2(1)\), followed by a calculation of whether the resulting
class is \(0\) or \(1\) in (1). Without that map, the binary class above is a
model for the obstruction space, not the obstruction of the source
extension.

## Verification

The exact checker
[`verify_dyadic_affine_mixed_cohomology.py`](../verification/related/verify_dyadic_affine_mixed_cohomology.py)
verifies the \(C_2\)-cohomology quotient, the cocycle identity (11), the
finite-level involutions (10), and the parity splitting criterion through
modulus \(2^{10}\).

Run:

```text
python verification/related/verify_dyadic_affine_mixed_cohomology.py
```
