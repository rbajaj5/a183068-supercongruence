# A183068 valuation-defect landscape

## Status

**Exact finite experiment; not a proof and not a spin-foam model.**

This note gives a statistical-mechanics visualization of the two local
congruences already proved in [PROOF.md](../PROOF.md).  It introduces no new
supercongruence claim.

## Local lattice

Write

```math
F(N,k)=\frac{(2N+2k)!}{k!^4(N-k)!^2}
```

and put $N=np^r$. Treat each tuple $(p,r,n,k)$ as a lattice site. The
site observable is the valuation of the applicable local defect:

```math
D_{p,r,n,k}=
\begin{cases}
F(np^r,k),&p\nmid k,\\[4pt]
F(np^r,k)-F(np^{r-1},k/p),&p\mid k.
\end{cases}
```

The target valuation is $2r$. Define the slack and violation energy by

```math
S_{p,r,n,k}=v_p(D_{p,r,n,k})-2r,
\qquad
E_{p,r,n,k}=\max(0,-S_{p,r,n,k}).
```

The proof says that every site has $E=0$. Sites with $S=0$ are sharp;
sites with $S>0$ contain unused divisibility. This makes the exact checker
a picture of where the proof spends its $p$-adic budget rather than another
verification of only the assembled sum.

This is analogous to a finite constraint Hamiltonian: the theorem asserts a
zero-violation configuration throughout the lattice.  It is **not** a spin
foam in the mathematical-physics sense: there are no face representations,
intertwiners, amplitudes, or state-sum invariance.

## Reproduction

Run:

```text
python verification/related/experiment_a183068_defect_lattice.py \
  --output data/a183068_defect_lattice.tsv
```

The committed sample covers $p\in\{2,3,5\}$, $1\le r\le2$, and
$1\le n\le3$. It records every summand site, separates the vanishing and
transfer strata, and independently checks the assembled congruence on the
same finite box.  All arithmetic is exact Python integer arithmetic.

## Interpretation boundary

The experiment can locate sharp sites and suggest where a stronger local
valuation might exist.  It cannot establish an unbounded theorem, replace the
carry and scaling lemmas, or justify importing quantum-gravity terminology.
