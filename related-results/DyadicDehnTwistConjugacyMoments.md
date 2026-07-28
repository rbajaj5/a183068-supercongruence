# Conjugacy shells and exact depth moments for dyadic Dehn twists

## Status and scope

This note is an elementary deduction in the finite affine quotients appearing
in the [public Roe-inspired \(2\)-adic packet](../ROE_2ADIC.md). It is not a
new theorem about the full outer automorphism group and makes no novelty
claim.

For \(m\ge2\), write

\[
G_m=
(\mathbb Z/2^m\mathbb Z)
\rtimes
(\mathbb Z/2^m\mathbb Z)^\times
\]

as the matrix group

\[
M(u,a)=
\begin{pmatrix}
u&a\\
0&1
\end{pmatrix},
\qquad
M(u,a)M(v,b)=M(uv,a+ub).
\tag{1}
\]

The translation

\[
T_b=M(1,b)
\]

is the finite affine image of the dyadic HNN Dehn twist with parameter \(b\).
The word "conjugacy" below always means conjugacy inside \(G_m\).

## 1. Exact conjugacy classification

For nonzero \(b\in\mathbb Z/2^m\mathbb Z\), let
\(v_2(b)\in\{0,\ldots,m-1\}\) be its truncated \(2\)-adic valuation.

### Theorem 1

For every \(m\ge2\):

1. \(T_0\) is a singleton conjugacy class.
2. Two nonzero translations \(T_b,T_c\) are conjugate in \(G_m\) if and only
   if \(v_2(b)=v_2(c)\).
3. The class at depth \(v\) has size

   \[
   2^{m-v-1}.
   \tag{2}
   \]

4. The centralizer of a depth-\(v\) translation has size

   \[
   2^{m+v}.
   \tag{3}
   \]

Consequently, the translation subgroup splits into exactly \(m+1\) conjugacy
classes: the zero class and one class at each depth \(0,\ldots,m-1\).

### Proof

The inverse of \(M(u,a)\) is \(M(u^{-1},-u^{-1}a)\), so (1) gives

\[
M(u,a)T_bM(u,a)^{-1}=T_{ub}.
\tag{4}
\]

Multiplication by a unit preserves \(v_2(b)\). Conversely, if \(b\) and \(c\)
have the same depth \(v\), write \(b=2^v b_0\) and \(c=2^v c_0\), with
\(b_0,c_0\) odd modulo \(2^{m-v}\). Choose a unit \(u\) satisfying
\(u\equiv c_0b_0^{-1}\pmod {2^{m-v}}\). Then \(ub=c\pmod {2^m}\).
This proves the classification.

There are \(2^{m-v-1}\) residues of exact depth \(v\), proving (2).
Equation (4) shows that \(M(u,a)\) centralizes \(T_b\) exactly when

\[
(u-1)b\equiv0\pmod {2^m},
\]

or \(u\equiv1\pmod {2^{m-v}}\). There are \(2^v\) such units and \(2^m\)
unrestricted translations \(a\), proving (3). The orbit--stabilizer identity

\[
2^{2m-1}/2^{m+v}=2^{m-v-1}
\]

gives the same class size. \(\square\)

## 2. An exact adjacent-level valuation law

For integers \(j\ge0\), define the \(j\)-th nonzero twist-depth moment

\[
D_{m,j}
=
\sum_{\substack{b\pmod {2^m}\\b\ne0}}
2^{jv_2(b)}.
\tag{5}
\]

Because each valuation shell is one conjugacy class, this is equivalently a
conjugacy-class sum weighted by class size.

### Theorem 2

For \(m\ge1\) and \(j\ge0\),

\[
D_{m,j}
=
\sum_{v=0}^{m-1}2^{m-v-1+jv}
=
2^{m-1}\sum_{v=0}^{m-1}2^{(j-1)v}.
\tag{6}
\]

The adjacent levels satisfy the exact identity

\[
\boxed{D_{m+1,j}-2D_{m,j}=2^{jm}.}
\tag{7}
\]

In particular,

\[
D_{m+1,j}\equiv2D_{m,j}\pmod {2^{jm}},
\tag{8}
\]

and the valuation in (8) is exactly \(jm\).

### Proof

The depth-\(v\) shell has \(2^{m-v-1}\) elements by Theorem 1. Summing its
weight \(2^{jv}\) gives (6). The last shell in level \(m+1\) has depth \(m\);
all earlier shell sizes double. Hence

\[
\begin{aligned}
D_{m+1,j}
&=
2\sum_{v=0}^{m-1}2^{m-v-1+jv}+2^{jm}\\
&=2D_{m,j}+2^{jm},
\end{aligned}
\]

which proves (7)--(8). \(\square\)

For \(j=1\), formula (6) reduces to

\[
D_{m,1}=m2^{m-1},
\]

while (7) becomes

\[
D_{m+1,1}-2D_{m,1}=2^m.
\]

Thus the scaled adjacent congruence is sharp at every level, rather than only
asymptotically.

## 3. Relationship to the Roe-inspired tower

The Roe--Turturean shear has affine image \(T_b\), and the earlier packet
proves that its depth on the abelianization is exactly \(v_2(b)\). Theorem 1
therefore says that, after passing to the affine quotient, twist depth is the
complete conjugacy invariant among nonzero translation images.

Theorem 2 packages the sizes of those conjugacy shells into an exact
adjacent-level law. It resembles a supercongruence because a level-\(m+1\)
quantity descends to a scaled level-\(m\) quantity with a linearly growing
\(2\)-adic exponent. Here, however, the relation is the elementary identity
(7), not a new application of the multinomial machinery used for A183068.

Nothing here proves that two twists with the same affine depth are conjugate
in the full group \(\mathrm{Out}(D_0)\). The kernel of the surjection onto the
affine shadow may retain additional conjugacy data.

## Verification

The exact checker
[`verify_dyadic_dehn_twist_conjugacy.py`](../verification/related/verify_dyadic_dehn_twist_conjugacy.py)
enumerates the affine quotients through \(2^8\), verifies every translation
orbit and centralizer, and checks (6)--(7) through \(m=16\) and \(j=8\).

Run:

```text
python verification/related/verify_dyadic_dehn_twist_conjugacy.py
```
