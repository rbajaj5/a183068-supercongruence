# Adams operations, Haar projection, and representation-ring Gauss towers

**Status date:** August 5, 2026

**Status:** complete structural deduction with exact checks. The ingredients
are classical: normalized Haar measure, Peter--Weyl theory, spectral radius,
Perron--Frobenius theory, and the Frobenius congruence for Adams operations.
No claim of literature priority is made for their combination below.

## 1. The algebraic master theorem

Let $A$ be a commutative unital $\mathbb Z$-algebra. Fix a prime $p$ and a
ring endomorphism $\psi_p:A\to A$ satisfying the Frobenius congruence

```math
\psi_p(y)\equiv y^p\pmod {pA}
\qquad(y\in A).
\tag{1}
```

Let $\tau:A\to\mathbb Z$ be a $\mathbb Z$-linear map such that

```math
\tau\circ\psi_p=\tau.
\tag{2}
```

### Theorem 1 (Frobenius-fixed trace tower)

For every $x\in A$ and all positive integers $n,r$,

```math
\boxed{
\tau(x^{np^r})\equiv\tau(x^{np^{r-1}})\pmod {p^r}.
}
\tag{3}
```

No norm, topology, semisimplicity, or positivity hypothesis is required.

### Proof

We first record the amplification hidden in (1). If $a^p=b+pc$ and
$m=p^{r-1}$, then

```math
(b+pc)^m-b^m
=\sum_{k=1}^{m}\binom{m}{k}b^{m-k}(pc)^k.
\tag{4}
```

Since

```math
v_p\binom{p^{r-1}}k
\ge r-1-v_p(k),
```

the $k$-th term of (4) is divisible by

```math
p^{r-1-v_p(k)+k}.
```

The elementary inequality $k-v_p(k)\ge1$ shows that every term lies in
$p^rA$. Consequently,

```math
a^{p^r}\equiv b^{p^{r-1}}\pmod {p^rA}.
\tag{5}
```

Apply this with $a=x^n$ and $b=\psi_p(x^n)$. Because $\psi_p$ is a ring
endomorphism,

```math
x^{np^r}
\equiv\psi_p(x^n)^{p^{r-1}}
=\psi_p(x^{np^{r-1}})
\pmod {p^rA}.
\tag{6}
```

Applying $\tau$ and then (2) gives (3). $\square$

## 2. Compact-group representations

Let $K$ be a compact group and let $R(K)$ be its complex representation
ring. The irreducible representations form a $\mathbb Z$-basis of $R(K)$ by
complete reducibility. Define

```math
\tau([W])=\dim W^K.
\tag{7}
```

Normalized Haar measure and character orthogonality give the exact projection
formula

```math
\tau([W])=\int_K\chi_W(g)\,d\mu(g).
\tag{8}
```

Peter--Weyl theory places (8) in the full orthogonal decomposition of
$L^2(K)$ into finite-dimensional matrix-coefficient spaces: $\tau$ selects
the trivial isotypic component.

The $p$-th Adams operation $\psi^p$ is a ring endomorphism of $R(K)$ with

```math
\chi_{\psi^p W}(g)=\chi_W(g^p).
\tag{9}
```

If the eigenvalues of $W(g)$ are formally $z_1,\ldots,z_d$, then

```math
(z_1+\cdots+z_d)^p-(z_1^p+\cdots+z_d^p)
```

has all coefficients divisible by $p$. Expressing this symmetric polynomial
in the exterior powers of $W$ proves the representation-ring Frobenius law

```math
\psi^p(y)\equiv y^p\pmod {pR(K)}.
\tag{10}
```

Thus Theorem 1 applies whenever

```math
\int_K\chi_W(g^p)\,d\mu(g)
=\int_K\chi_W(g)\,d\mu(g)
\qquad(W\in R(K)).
\tag{11}
```

### Corollary 2 (Adams--Haar Gauss tower)

Assume (11), let $V$ be a finite-dimensional continuous representation of
$K$, and put

```math
a_N=\dim(V^{\otimes N})^K.
\tag{12}
```

Then for all positive $n,r$,

```math
\boxed{
a_{np^r}\equiv a_{np^{r-1}}\pmod {p^r}.
}
\tag{13}
```

This is a genuine representation-theoretic extension of the constant-term
viewpoint: it applies to tensor-invariant multiplicities rather than only to
Laurent-polynomial coefficients.

## 3. Two unconditional families

### 3.1 Compact abelian groups

Let $K$ be compact abelian with discrete character group $\widehat K$. If
$\widehat K$ has no element of order $p$, multiplication by $p$ on
$\widehat K$ is injective. Equivalently, the power homomorphism
$g\mapsto g^p$ on $K$ is surjective, hence preserves normalized Haar measure.
Condition (11) follows.

For a torus $K=\mathbb T^d$, $\widehat K\cong\mathbb Z^d$ has no torsion, so
(13) holds for every prime. If

```math
\chi_V(z)=\sum_{u\in S}c_u z^u,
```

then (8) becomes

```math
a_N=\operatorname{CT}(\chi_V^N).
\tag{14}
```

Thus Corollary 2 recovers the ordinary all-prime constant-term Gauss tower
from Fourier duality, while the earlier cyclic-word proof gives its exact
$p$-torsion boundary.

### 3.2 Finite groups away from their order

Let $K$ be finite and suppose $p\nmid |K|$. If $e$ is the exponent of $K$,
choose $q$ with $pq\equiv1\pmod e$. The maps $g\mapsto g^p$ and
$g\mapsto g^q$ are inverse permutations of the underlying finite set.
Therefore they preserve normalized counting measure, so (11) holds and every
finite-dimensional representation satisfies (13).

Equivalently,

```math
a_N=\frac1{|K|}\sum_{g\in K}\chi_V(g)^N
\tag{15}
```

obeys the adjacent $p$-power congruence for every $p\nmid|K|$.

## 4. Spectral recurrence and asymptotics

For a finite group, list the irreducibles as
$\rho_0=\mathbf1,\rho_1,\ldots,\rho_{s-1}$. Let $M_V$ be the nonnegative
integer fusion matrix defined by

```math
V\otimes\rho_j=\sum_i(M_V)_{ij}\rho_i.
\tag{16}
```

With $e_0=(1,0,\ldots,0)^{\mathsf T}$,

```math
a_N=e_0^{\mathsf T}M_V^Ne_0,
\qquad
\sum_{N\ge0}a_Nz^N
=e_0^{\mathsf T}(I-zM_V)^{-1}e_0.
\tag{17}
```

This supplies two further consequences of the spectral framework:

1. Cayley--Hamilton makes $(a_N)$ an integral linear-recurrence sequence of
   order at most the number of irreducible representations of $K$.
2. The character table diagonalizes $M_V$ over $\mathbb C$; its eigenvalues
   are the values $\chi_V(C)$ on conjugacy classes $C$. Hence

   ```math
   \rho(M_V)=\dim V,
   \tag{18}
   ```

   and the poles of the rational function in (17) lie among
   $\chi_V(C)^{-1}$. Perron--Frobenius theory controls the positive dominant
   spectral sector, while (15) gives the exact spectral weights.

The same statements apply whenever the tensor subring generated by $V$ has
finite irreducible support, even if the original compact group is infinite.

## 5. The nonabelian boundary is real

Condition (11) is not automatic. Take $K=SU(2)$ and let $V$ be its standard
two-dimensional representation. Then

```math
a_1=\dim V^{SU(2)}=0,
\qquad
a_2=\dim(V^{\otimes2})^{SU(2)}=1.
```

Therefore

```math
a_2\not\equiv a_1\pmod2.
\tag{19}
```

At the Adams-operation level,

```math
\psi^2(V)=\operatorname{Sym}^2(V)-\bigwedge^2V
=\operatorname{Sym}^2(V)-\mathbf1,
```

so $\tau(\psi^2V)=-1\ne0=\tau(V)$. The failure of Haar invariance is exactly
visible before any congruence calculation.

## 6. The normalized Adams defect

Theorem 1 also isolates the extra input required for a supercongruence. Under
its hypotheses, define

```math
E_{p,r}(x;n)=
\frac{x^{np^r}-\psi_p(x^{np^{r-1}})}{p^r}\in A.
\tag{20}
```

Then

```math
\tau(x^{np^r})-\tau(x^{np^{r-1}})
=p^r\tau(E_{p,r}(x;n)).
\tag{21}
```

Consequently, a depth-$h$ tower

```math
\tau(x^{np^r})\equiv\tau(x^{np^{r-1}})\pmod {p^{hr}}
```

is equivalent to the explicit residual condition

```math
v_p\bigl(\tau(E_{p,r}(x;n))\bigr)\ge(h-1)r.
\tag{22}
```

For the cubic towers in the supercongruence portfolio, representation theory
supplies the first $p^r$ automatically when (11) holds; the remaining problem
is exactly $p^{2r}$ of cancellation in the normalized Adams defect. This is a
search reduction, not a claim that Peter--Weyl theory alone proves a cubic
tower.

## 7. Verification

Run

```text
python verification/related/verify_adams_haar_gauss_towers.py
```

The exact checker verifies the amplification lemma arithmetically, torus
constant terms, finite-group character averages and fusion recurrences for
$S_3$, and the $SU(2)$ binary counterexample. These checks are regression
tests; Sections 1--6 contain the proof.

## 8. Sources and priority boundary

- N. Bourbaki, *Théories spectrales*, Chapters I--II, 2nd ed., Springer,
  2019: spectral radius in Chapter I, Section 2, no. 3; normalized Haar
  measure and Fourier characters in Chapter II, Section 1.
- N. Bourbaki, *Théories spectrales*, Chapters III--V, Springer, 2023:
  Perron--Frobenius theory in Chapter III, Section 6, and the Peter--Weyl
  theorem in Chapter V, Section 4, no. 3.
- E. Meir and M. Szymik,
  [*Adams operations and symmetries of representation categories*](https://arxiv.org/abs/1704.03389),
  for Adams operations on representation rings.
- J.-P. Serre, *Linear Representations of Finite Groups*, Springer, 1977,
  for character orthogonality and the finite-group representation ring.

The targeted search found the standard ingredients but not this exact
Adams-fixed-trace formulation. That is not evidence of priority. The theorem
is recorded as a structural synthesis and should be cited through its
classical ingredients unless a specialist literature audit establishes a
separate history.
