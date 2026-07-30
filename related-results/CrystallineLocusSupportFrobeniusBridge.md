# Crystalline-locus inclusions as Frobenius support packets

## 1. Status and source boundary

Kansal, Levin, and Savitt classify inclusions among reduced special fibers
\(\mathcal Z(\mathbf r)\) of two-dimensional \(p\)-bounded crystalline loci,
for odd \(p\) and an unramified extension of degree \(f>1\).  Their paper
also proves that, with one explicit exception, these inclusions can be
detected on closed points, equivalently on semisimple mod-\(p\) Galois
representations.

This note records the exact way in which that result enters the repository's
Frobenius-packet framework:

1. their theorem supplies an **order on Frobenius-stable supports**;
2. orbit decomposition converts each nested pair of supports into a
   nonnegative Dold sequence;
3. the ordinary Gauss congruences follow automatically; and
4. a stronger \( \ell^{hr} \) supercongruence is equivalent to extra
   \(\ell\)-divisibility of the primitive degree strata.

Here \(p\) is the residue characteristic in the crystalline-locus paper,
whereas \(\ell\) is an index prime in the Dold/Gauss tower.  They need not be
the same prime.

The final point of the note is equally important: the exceptional
Barsotti--Tate/Steinberg pair has identical semisimple support but distinct
stack geometry.  Therefore no invariant built only from closed-point support,
including the support ghost below, can classify all stack inclusions.

This is an exact synthesis of the cited classification with the classical
Frobenius-orbit/Dold dictionary.  It is not a claim that the cited paper proves
a new supercongruence, and no literature-priority claim is made for the
dictionary.

## 2. The local crystalline moves

Write

```math
u_i=r_{i,1}-r_{i,2}\in\{0,1,\ldots,p\},
\qquad
z(\mathbf u)=\#\{i:u_i=0\}.
```

The cited paper proves

```math
\operatorname{codim}\mathcal Z(\mathbf r)=z(\mathbf u).
```

At two cyclically adjacent positions, the difference-word shadows of its
three operations are

```math
\begin{array}{c|c|c}
\text{move}&\text{valid input}&\text{output}\\ \hline
\mu&(a,0),\ a>0&(a-1,p)\\
\theta&(a,0),\ a<p&(a+1,p)\\
\nu&(0,b)&(1,p-b).
\end{array}
```

Every valid move gives an inclusion of crystalline loci.  The paper then
classifies which moves are invertible, which inclusions are simple, and the
two degenerate families that require separate treatment.

### Proposition 1: the local codimension budget

For the three valid moves, the change
\(\Delta z=z(\mathbf u_{\mathrm{after}})-z(\mathbf u_{\mathrm{before}})\)
is:

```math
\begin{array}{c|c}
\text{move and input}&\Delta z\\ \hline
\mu:(1,0)\mapsto(0,p)&0\\
\mu:(a,0)\mapsto(a-1,p),\ a>1&-1\\
\theta:(0,0)\mapsto(1,p)&-2\\
\theta:(a,0)\mapsto(a+1,p),\ 0<a<p&-1\\
\nu:(0,p)\mapsto(1,0)&0\\
\nu:(0,0)\mapsto(1,p)&-2\\
\nu:(0,b)\mapsto(1,p-b),\ 0<b<p&-1.
\end{array}
```

In particular, the codimension-preserving cases are exactly the mutually
inverse boundary moves

```math
(1,0)\mathrel{\mathop{\longleftrightarrow}^{\mu}_{\nu}}(0,p).
```

The only local operations capable of changing codimension by two are
\(\theta\) and \(\nu\) at \((0,0)\).  This explains why the neighboring
conditions in the paper's exceptional cases occur precisely at that input:
the codimension count detects a possible missing intermediate stratum, while
the paper's full support classification decides whether such an intermediate
actually exists.

#### Proof

Only the two displayed coordinates can change.  Counting zero coordinates
before and after each move gives the table.  The inverse assertion follows
from

```math
\mu(1,0)=(0,p),
\qquad
\nu(0,p)=(1,0).
```

\(\square\)

## 3. Relative support ghosts

Let \(S\subseteq T\) be Frobenius-stable, locally finite sets of geometric
points over \(\mathbb F_q\).  Equivalently, assume that only finitely many
Frobenius orbits of any fixed length occur.  Let

```math
b_d=\#\{\text{Frobenius orbits of length }d\text{ in }T\setminus S\}.
```

Define the relative support ghost

```math
a_n=\#(T\setminus S)^{F^n}.
```

Orbit decomposition gives

```math
a_n=\sum_{d\mid n}d\,b_d. \tag{1}
```

For schemes this is the ordinary difference of point counts of the two
reduced supports.  For stacks, (1) is deliberately only a **support count**:
it does not include automorphism weights and should not be confused with a
groupoid cardinality.

### Theorem 2: support inclusions produce Gauss towers

For every prime \(\ell\), every \(m\ge1\), and every \(r\ge1\),

```math
a_{m\ell^r}\equiv
a_{m\ell^{r-1}}
\pmod{\ell^{\,r+v_\ell(m)}}. \tag{2}
```

In particular,

```math
a_{m\ell^r}\equiv
a_{m\ell^{r-1}}
\pmod{\ell^r}. \tag{3}
```

Moreover, fix \(h\ge1\).  The stronger tower

```math
a_{m\ell^r}\equiv
a_{m\ell^{r-1}}
\pmod{\ell^{hr}}
\qquad(\ell\nmid m,\ r\ge1) \tag{4}
```

holds for every \(m,r\) if and only if

```math
\ell^{(h-1)r}\mid b_{m\ell^r}
\qquad(\ell\nmid m,\ r\ge1). \tag{5}
```

#### Proof

Subtract (1) at \(m\ell^r\) and \(m\ell^{r-1}\).  Every surviving divisor
\(d\) has

```math
v_\ell(d)=v_\ell(m)+r,
```

so each summand \(d\,b_d\) is divisible by
\(\ell^{r+v_\ell(m)}\).  This proves (2).

The equivalence of (4) and (5) is the higher-Dold criterion.  In one
direction, (5) supplies \(hr\) powers in every newly appearing summand.  In
the other, fix \(r\) and apply Möbius inversion over the divisors of \(m\)
to the differences in (4).  This isolates
\(m\ell^r b_{m\ell^r}\).  Dividing by \(m\ell^r\), with
\(\ell\nmid m\), yields (5).
\(\square\)

The theorem cleanly separates two questions:

- support inclusion guarantees the baseline Gauss exponent;
- a Bala-style exponent \(h>1\) asks for extra divisibility of the primitive
  closed-point multiplicities.

## 4. Application to the crystalline-locus poset

For a valid inclusion

```math
\mathcal Z(\mathbf r)\subseteq\mathcal Z(\mathbf r'),
```

the closed-point theorem of Kansal--Levin--Savitt usually supplies a nested
pair

```math
\mathcal Z_{\mathrm{ss}}(\mathbf r)
\subseteq
\mathcal Z_{\mathrm{ss}}(\mathbf r').
```

Because the loci are defined over a finite field, the relative semisimple
support decomposes into Frobenius orbits.  Theorem 2 therefore assigns the
inclusion a canonical nonnegative support packet

```math
b_d(\mathbf r,\mathbf r')
=\#\{\text{primitive degree-}d\text{ semisimple points added}\},
```

and its ghost sequence satisfies the ordinary Gauss congruences.

This does not prove a stronger crystalline supercongruence.  It turns that
question into an exact target:

> For which valid \(\mu,\theta,\nu\) moves are the primitive support
> multiplicities \(b_{m\ell^r}\) divisible by
> \(\ell^{(h-1)r}\)?

The local codimension budget in Proposition 1 is a first stratification of
that problem.  It says how many geometric equations can disappear under a
move; it does not by itself determine the arithmetic of the degree strata.

## 5. The exact support-level obstruction

The paper proves an exceptional equality

```math
\mathcal Z_{\mathrm{ss}}(\mathrm{St}+\lambda)
=
\mathcal Z_{\mathrm{ss}}(\mathrm{BT}+\lambda),
```

while at stack level

```math
\mathcal Z(\mathrm{BT}+\lambda)
\subsetneq
\mathcal Z(\mathrm{St}+\lambda)
```

and the reverse inclusion fails.

For this pair,

```math
b_d=0
\quad\text{and}\quad
a_n=0
```

for every \(d,n\), even though the stack inclusion is nontrivial.  Thus:

### Corollary 3: support ghosts are not complete stack invariants

Neither the relative support ghost, its zeta/Euler product, nor any
supercongruence satisfied by that ghost can recover the full inclusion order
of the crystalline stacks.

This is not a weakness of Theorem 2.  It is a precise boundary between
set-theoretic Frobenius data and stack geometry, exhibited by the source
paper itself.

## 6. Position in the 110-record program

The two programs occupy different axes:

| Input | Primary information | Arithmetic question |
| --- | --- | --- |
| Bala/OEIS sequence | weighted multiplicities in an index tower | how much \(p\)-adic divisibility survives rescaling? |
| crystalline-locus poset | which semisimple supports are nested | which primitive Frobenius orbits are added? |
| combined packet | support plus degree multiplicity | when do the added degree strata have higher Dold divisibility? |

Accordingly, this paper does not close another item of the 110-record Bala
census.  It contributes a rigorous **support-before-multiplicity** layer that
the existing arithmetic Frobenius framework did not previously state.

## 7. Exact verification

The companion script

```text
python verification/related/verify_crystalline_locus_support_bridge.py
```

checks:

- every local codimension change in Proposition 1 for several odd residue
  characteristics;
- the invertible \(\mu/\nu\) boundary pair;
- exact Möbius recovery of primitive orbit multiplicities;
- the baseline Gauss tower for deterministic random support packets; and
- the higher-Dold criterion on manufactured packets of depths
  \(h=1,2,3,4\).

The script verifies the deductions in this note; it does not machine-check
the classification theorems of Kansal--Levin--Savitt.

## 8. Sources

- Kalyani Kansal, Brandon Levin, and David Savitt,
  [*Inclusions between \(p\)-bounded crystalline loci in dimension two*](https://arxiv.org/abs/2607.26305),
  arXiv:2607.26305 (2026).
- The repository's
  [arithmetic Frobenius packet framework](ArithmeticFrobeniusPacketFramework.md)
  and
  [primitive collision-orbit bridge](JacobianCollisionEulerOrbitBridge.md)
  contain the orbit and higher-Dold formulations used here.
