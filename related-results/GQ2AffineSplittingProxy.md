# The affine splitting proxy for the dyadic Demushkin tower

## Status

This note completes the **linear obstruction calculation** advertised in
[`ROE_2ADIC.md`](../ROE_2ADIC.md).  It does not decide whether the actual
surjection

$$
\mathrm{Out}(D_0)\longrightarrow
\mathbb Z_2\rtimes\mathbb Z_2^\times
$$

splits.  It does three more limited things:

1. it derives the continuous cohomology group used as the first abelian
   proxy;
2. it constructs both proxy extension classes explicitly and proves a
   parity criterion for splitting;
3. it identifies the datum that must be extracted from the genuine kernel
   before the proxy can obstruct a section of
   $\mathrm{Out}(D_0)$.

The calculation is standard continuous group cohomology.  Its value here is
diagnostic: the possible obstruction is a **cross-commutator parity** between
the sign direction and the procyclic $5$-adic direction.  It is not an
obstruction to lifting either direction separately.

## 1. The coefficient calculation

Put

$$
U=\mathbb Z_2^\times,\qquad M=\mathbb Z_2(1),
$$

where $u\in U$ acts on the additive group $M$ by multiplication by $u$.
Write

$$
U=\{\pm1\}\times\Gamma,\qquad
\Gamma=1+4\mathbb Z_2=\langle5\rangle\cong\mathbb Z_2.
$$

Continuous cohomology here means continuous cochains with compact
$\mathbb Z_2$-coefficients, equivalently the cohomology computed by the
two-term completed group-ring resolution for the procyclic factor.

### Theorem 1

There is an isomorphism

$$
H^2_{\mathrm{cont}}(U,M)\cong\mathbb Z/2.
$$

### Proof

For the procyclic group $\Gamma$, the completed two-term resolution gives

$$
H^0_{\mathrm{cont}}(\Gamma,M)
=\ker(5-1)=0,
$$

$$
H^1_{\mathrm{cont}}(\Gamma,M)
=M/(5-1)M
=\mathbb Z_2/4\mathbb Z_2,
$$

and $H^q_{\mathrm{cont}}(\Gamma,M)=0$ for $q\ge2$.

The nontrivial element of $C_2=\{\pm1\}$ acts by $-1$ on
$H^1(\Gamma,M)$.  The Hochschild--Serre spectral sequence for

$$
1\longrightarrow\Gamma\longrightarrow U\longrightarrow C_2
\longrightarrow1
$$

therefore has only one nonzero term of total degree two:

$$
H^2_{\mathrm{cont}}(U,M)
\cong
H^1\!\left(C_2,(\mathbb Z/4)_{\mathrm{sign}}\right).
$$

For a cyclic group of order two,

$$
H^1(C_2,A)=\ker(1+s)/(s-1)A.
$$

On the sign module $A=\mathbb Z/4$, $1+s=0$ and $s-1=-2$, so

$$
H^1(C_2,A)=A/2A\cong\mathbb Z/2.
\qquad\square
$$

The location of the surviving term matters.  The class lies in the
$H^1(C_2,H^1(\Gamma,M))$ cross-term.  It is therefore a compatibility
obstruction between the two factors, not an obstruction visible on either
$C_2$ or $\Gamma$ alone.

## 2. Explicit representatives

The preceding $\mathbb Z/2$ can be seen without a spectral sequence.
For $n\in\mathbb Z_2$, define

$$
q(n)=\frac{5^n-1}{4}\in\mathbb Z_2.
$$

It satisfies

$$
q(n+m)=q(n)+5^nq(m).
\tag{1}
$$

Let

$$
H=M\rtimes\Gamma
$$

with coordinate law

$$
(x,n)(y,m)=(x+5^ny,n+m).
\tag{2}
$$

For $z\in\mathbb Z_2$, set

$$
\tau_z(x,n)=(-x+zq(n),n).
\tag{3}
$$

Equation (1) shows that $\tau_z$ is an automorphism of $H$, and direct
substitution gives $\tau_z^2=1$.  Hence

$$
E_z=H\rtimes_{\tau_z}C_2
\tag{4}
$$

is a profinite group fitting into an extension

$$
1\longrightarrow M\longrightarrow E_z
\longrightarrow C_2\times\Gamma\longrightarrow1
\tag{5}
$$

with the prescribed $U$-action on $M$.

Let $a^x$ denote the element $(x,0)\in H$, let $g=(0,1)$ be the
topological generator in the $5$-direction, and let $s$ denote the
nontrivial element of the final $C_2$.  Then

$$
s\,g\,s^{-1}=a^z g.
\tag{6}
$$

Thus $z$ measures the failure of the two distinguished quotient directions
to commute upstairs.

### Theorem 2

The extension (5) admits a continuous group-theoretic section if and only if
$z$ is even.  Moreover, $E_z$ and $E_{z'}$ define the same extension class
if and only if

$$
z\equiv z'\pmod2.
$$

Consequently, $E_0$ and $E_1$ are explicit representatives of the two
elements of $H^2_{\mathrm{cont}}(U,M)$.

### Proof

Every lift of the two standard quotient generators has the form

$$
G'=a^b g,\qquad S'=a^c s
$$

for some $b,c\in\mathbb Z_2$.  One always has $(S')^2=1$.  Using (2),
(3), and (6) gives

$$
S'G'(S')^{-1}=a^{z-b-4c}g.
$$

The lifts commute precisely when this equals $G'=a^bg$, or equivalently

$$
z=2b+4c.
\tag{7}
$$

Equation (7) is soluble in $\mathbb Z_2$ exactly when $z$ is even.  If it is
soluble, $G'$ extends continuously from the topological generator to
$\Gamma\cong\mathbb Z_2$, and the commuting pair $(S',G')$ gives a section.
If $z$ is odd, every choice of lifts has odd cross-commutator parameter, so
no section exists.

For completeness, suppose $z'-z=2b+4c$.  The assignment that is the identity
on $M$ and sends the distinguished generators of $E_z$ to

$$
g_z\longmapsto a^bg_{z'},\qquad
s_z\longmapsto a^cs_{z'}
$$

respects (6) and gives an equivalence of extensions.  Thus every even change
of $z$ is cohomologically trivial.  Conversely, equivalent extensions have
the same splitting behavior; since the even class splits and the odd class
does not, parity is the complete extension invariant in this family.
$\square$

### Corollary 3: first-level detection

The nonzero proxy class is already detected modulo $2$.  In particular, it
is not a phenomenon that appears only after a long $2$-adic tower has been
constructed.

This is useful for an audit: once a compatible pushout of the genuine kernel
has been found, one cross-commutator calculation modulo $2$ decides the
linear proxy class.

## 3. What remains for the Roe--Turturean quotient

Roe--Turturean Proposition 3.9 proves surjectivity onto the affine abelian
shadow and constructs individual lifts of its unit and translation
coordinates.  Individual lifts do not by themselves form a group section:
their products may differ from the chosen lift of the product by an element
of the nonabelian kernel.

Let

$$
1\longrightarrow K\longrightarrow
\mathrm{Out}(D_0)\longrightarrow
\mathbb Z_2\rtimes\mathbb Z_2^\times
\longrightarrow1
$$

denote the genuine extension.  To apply Theorems 1--2, one still needs:

1. a continuous equivariant abelian quotient or subquotient
   $K\twoheadrightarrow M=\mathbb Z_2(1)$;
2. compatibility with the already explicit translation section;
3. the parity of the resulting sign--$5$ cross-commutator.

If that parity is odd, the pushed-out extension is nonsplit, hence the
original extension cannot split.  If it is even, this particular proxy is
silent: a nonabelian or deeper abelian obstruction may remain.

The source paper is
[Roe--Turturean, *A Presentation of the Absolute Galois Group of
$\mathbb Q_2$*](https://roed314.github.io/gq2/paper.pdf).

## 4. A possible-worlds boundary: Yablo towers are different

Yablo's
[*Paradox without Self-Reference*](https://www.mit.edu/~yablo/pwsr.pdf)
gives an exact warning about finite approximations.  Let $Y_N$ be the set of
truth assignments $(t_1,\ldots,t_N)\in\{0,1\}^N$ satisfying

$$
t_n=1
\quad\Longleftrightarrow\quad
t_k=0\ \text{for every }k>n.
\tag{8}
$$

Then

$$
Y_N=\{(0,\ldots,0,1)\}.
$$

Every finite truncation is therefore soluble.  But the restriction map from
$N+1$ coordinates to $N$ coordinates sends the unique point of $Y_{N+1}$ to
$(0,\ldots,0)$, which is not in $Y_N$.  The sets of possible worlds do not
form an inverse system under restriction, so compactness has nothing to
assemble.

This separates three lifting failures that can otherwise sound similar:

| Example | Finite-level status | What fails |
| --- | --- | --- |
| Yablo truth assignments | Every truncation is soluble | Solutions are not compatible under restriction |
| Roe--Turturean Remark C.7 | Compatible congruence classes exist | The profinite limit lies outside the nonclosed discrete subset $\mathbb Z$ |
| The odd class $E_1$ above | A quotient extension exists | Cross-commutator parity forbids a group section |

The distinction is the practical content of the possible-worlds viewpoint:
one must specify both the worlds and the bonding maps before an inverse-limit
argument has mathematical force.

## 5. Exact checks

The accompanying checker verifies:

- the cocycle identity (1) at finite $2$-power precision;
- the automorphism and involution identities for $\tau_z$;
- the splitting equation (7) and its parity classification;
- the two-element sign-cohomology quotient;
- the unique finite Yablo assignment and failure of restriction
  compatibility.

Run:

```text
python verification/related/verify_gq2_affine_splitting_proxy.py
```

These computations check the formulas; they do not identify the genuine
kernel quotient required in Section 3.
