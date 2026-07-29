# Walsh analysis of the dyadic hypercube defect

**Status.** Complete combinatorial corollary of the dyadic quadratic-defect
formula; exhaustive finite checks pass. The Boolean Fourier tools are
classical. No priority claim is made for the matching-spectrum calculation.

## 1. One output coefficient is a matching quadratic

Let $A\subset\mathbb N^d$ be finite and write

```math
F=\sum_{\alpha\in A}a_\alpha X^\alpha,
\qquad
a_\alpha=\epsilon_\alpha+2\eta_\alpha\pmod4,
\qquad
\epsilon_\alpha,\eta_\alpha\in\mathbb F_2.
\qquad\text{(1)}
```

The dyadic defect is

```math
\mathfrak q(F)=\frac{F^2-\phi(F)}2\pmod2,
\qquad
\phi(X^\alpha)=X^{2\alpha}.
\qquad\text{(2)}
```

Fix a target monomial $X^\gamma$. Let $P_\gamma$ be the set of
unordered pairs

```math
P_\gamma=
\left\{
\{\alpha,\beta\}\subset A:
\alpha\ne\beta,\ \alpha+\beta=\gamma
\right\},
\qquad
k_\gamma=|P_\gamma|,
\qquad\text{(3)}
```

and put

```math
\delta_\gamma=
\begin{cases}
1,&\gamma=2\alpha\text{ for some }\alpha\in A,\\
0,&\text{otherwise}.
\end{cases}
\qquad\text{(4)}
```

The pairs in $P_\gamma$ are disjoint: once $\alpha$ is chosen, its
possible partner is uniquely $\gamma-\alpha$. Thus $P_\gamma$ is a
matching, not an arbitrary graph.

### Theorem 1 (matching normal form)

The target coordinate

```math
q_\gamma(F)=[X^\gamma]\mathfrak q(F)
```

has the Boolean normal form

```math
q_\gamma(F)
=
\delta_\gamma\eta_{\gamma/2}
+
\sum_{\{\alpha,\beta\}\in P_\gamma}
\epsilon_\alpha\epsilon_\beta
\pmod2.
\qquad\text{(5)}
```

After relabeling its active variables,

```math
q_\gamma
=
\delta z+\sum_{j=1}^{k}x_jy_j
\pmod2,
\qquad
k=k_\gamma,\quad\delta=\delta_\gamma.
\qquad\text{(6)}
```

All other coefficient bits are spectators for this output coordinate.

#### Proof

The coefficient formula from the
[dyadic hypercube theorem](DyadicHypercubeDefect.md) is

```math
\mathfrak q(F)
=
\sum_{\alpha\in A}\eta_\alpha X^{2\alpha}
+
\sum_{\alpha<\beta}
\epsilon_\alpha\epsilon_\beta X^{\alpha+\beta}.
```

Extracting $X^\gamma$ gives (5). The uniqueness of
$\gamma-\alpha$ proves that its quadratic graph is a matching.
$\square$

## 2. Exact counts on the coefficient cube

Choose the residues $a_\alpha\bmod4$ independently and uniformly. Then:

```math
\Pr(q_\gamma=0)
=
\begin{cases}
\dfrac12,&\delta_\gamma=1,\\[6pt]
\dfrac12+\dfrac1{2^{k_\gamma+1}},
&\delta_\gamma=0.
\end{cases}
\qquad\text{(7)}
```

Equivalently, among the $4^{|A|}$ coefficient arrays modulo $4$, the
number with vanishing target defect is

```math
\#\{F:q_\gamma(F)=0\}
=
\begin{cases}
2^{2|A|-1},&\delta_\gamma=1,\\[4pt]
2^{2|A|-1}+2^{2|A|-k_\gamma-1},
&\delta_\gamma=0.
\end{cases}
\qquad\text{(8)}
```

When $k_\gamma=0=\delta_\gamma$, the second line gives all
$4^{|A|}$ arrays, as it should.

Indeed, each product $x_jy_j$ equals $1$ with probability $1/4$.
Therefore

```math
\mathbb E(-1)^{\sum_jx_jy_j}
=
\left(1-\frac{2}{4}\right)^k
=2^{-k}.
\qquad\text{(9)}
```

A free linear bit $z$ makes the expectation zero. Equation (7) follows
from

```math
\Pr(q_\gamma=0)
=
\frac{1+\mathbb E(-1)^{q_\gamma}}2.
```

This is an exact counting law, not a heuristic claim that Euler-product
coefficients are random.

## 3. Complete Walsh spectrum

For a Boolean variable $u$, write

```math
\chi_u=(-1)^u.
```

The sign function of one matching edge satisfies

```math
(-1)^{xy}
=
\frac{1+\chi_x+\chi_y-\chi_x\chi_y}{2}.
\qquad\text{(10)}
```

### Theorem 2 (flat matching spectrum)

For $g_\gamma=(-1)^{q_\gamma}$,

```math
g_\gamma
=
\chi_z^\delta
\prod_{j=1}^{k}
\frac{
1+\chi_{x_j}+\chi_{y_j}-\chi_{x_j}\chi_{y_j}
}{2}.
\qquad\text{(11)}
```

Consequently:

1. exactly $4^k$ Walsh coefficients are nonzero;
2. every nonzero coefficient has absolute value $2^{-k}$;
3. the constant coefficient is $2^{-k}$ if $\delta=0$, and $0$
   if $\delta=1$;
4. each matching variable has influence $1/2$;
5. the diagonal high bit, when present, has influence $1$; and
6. the total influence is

   ```math
   \mathrm{Inf}(g_\gamma)=k+\delta.
   \qquad\text{(12)}
   ```

The formula also gives the exact noise stability. If two hypercube points
are $\rho$-correlated in the standard Fourier sense, then

```math
\mathrm{Stab}_\rho(g_\gamma)
=
\rho^\delta
\left(\frac{(1+\rho)^2}{4}\right)^k.
\qquad\text{(13)}
```

#### Proof

Multiplying (10) over the disjoint matching edges proves (11). Each edge
offers four Walsh characters with coefficients of magnitude $1/2$, so
the product has $4^k$ coefficients of magnitude $2^{-k}$. Multiplying
by $\chi_z$ shifts every Fourier set by $z$, proving the first three
claims.

Flipping $x_j$ changes $x_jy_j$ exactly when $y_j=1$, which has
probability $1/2$; similarly for $y_j$. Flipping $z$ always changes
the output. This proves (12).

Finally, noise stability is

```math
\sum_S\widehat g_\gamma(S)^2\rho^{|S|}.
```

For each edge, the four squared Fourier weights contribute

```math
\frac{1+2\rho+\rho^2}{4}
=
\frac{(1+\rho)^2}{4}.
```

The optional character $\chi_z$ contributes $\rho^\delta$, proving
(13). $\square$

## 4. Every affine face has the same normal form

Fix any subset of the active bits to constants. An intact matching edge
remains $xy$. If one endpoint is fixed to $0$, its term disappears. If
one endpoint is fixed to $1$, the other endpoint becomes a linear term.
Fixing both endpoints contributes a constant. The same alternatives hold
for the diagonal bit $z$.

### Theorem 3 (face closure)

On every affine face of the coefficient hypercube, the target defect is,
after relabeling,

```math
c+\sum_{j=1}^{k'}x_jy_j+\sum_{\ell=1}^{t}z_\ell
\pmod2.
\qquad\text{(14)}
```

If $t>0$, the restricted function is balanced. If $t=0$, its signed
bias has absolute value $2^{-k'}$. Hence the number of zeros on every
face is known exactly.

This closure property is useful for partial coefficient information:
revealing coefficient bits never creates a complicated interaction graph.
It only deletes matching edges or converts them into linear constraints.

## 5. CSP and verification interpretation

For one target coefficient, the modulus-$4$ obstruction is an
XOR-of-ANDs constraint on a matching. It has:

- an exact model count from (8);
- a closed Walsh representation from (11);
- constant-time updates per affected matching edge when a coefficient bit
  is changed; and
- the face reduction (14) under partial assignments.

Several target coefficients can share input bits, so a simultaneous system
need not remain a disjoint matching. The correct finite object is then a
sparse quadratic Boolean CSP. It can be stored in a ZDD, BDD, SAT, or
algebraic-normal-form representation without expanding the original
integer Euler product. The
[joint-spectrum theorem](DyadicHypercubeJointSpectrum.md) solves the
ambient model-counting problem exactly by reducing every output XOR test
to the rank and radical of an alternating convolution matrix. No claim is
made here that arbitrary quadratic systems outside this defect family are
easy.

For the Euler-product tower, the coefficient array in (1) is not uniformly
random: it is generated by a structured product. Theorems 1--3 therefore
describe the exact ambient obstruction geometry. The
[logarithmic defect formula](DyadicHypercubeDefect.md#4-closed-logarithmic-form-of-the-defect)
describes the much smaller structured subset actually reached by Euler
products.

## 6. Exact checks and provenance

Run:

```text
python verification/related/verify_dyadic_hypercube_walsh.py
```

The checker:

1. compares (5) with the integral definition (2) on one- and
   two-dimensional monomial supports;
2. verifies the exact zero counts (8);
3. computes every Walsh coefficient for the canonical matching forms;
4. verifies all influences and the noise-stability polynomial; and
5. exhausts every affine face through three matching edges.

The Fourier vocabulary and identities are standard; see Ryan O'Donnell,
[*Analysis of Boolean Functions*](https://arxiv.org/abs/2105.10386).
The repository-specific point is that the coefficient coordinate of the
dyadic Frobenius defect has the unusually simple matching graph (3).
