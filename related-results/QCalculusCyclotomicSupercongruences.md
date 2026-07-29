# A q-calculus lift of the Landau-depth program

**Status:** complete elementary deductions from published q-binomial
congruences, with exact polynomial checks. Literature priority is preliminary;
no novelty claim is made for the general machinery.

## 1. What q-calculus adds

The useful deformation is not obtained by replacing every integer with a
q-integer and hoping that an old congruence survives. The useful fact is that
q-factorials remember every carry level separately.

Put

```math
(q;q)_n=\prod_{j=1}^{n}(1-q^j)
```

and define the q-multinomial polynomial

```math
M_q(b_1,\ldots,b_m)
=
\frac{(q;q)_{b_1+\cdots+b_m}}
     {(q;q)_{b_1}\cdots(q;q)_{b_m}}.
\qquad\text{(1)}
```

Its value at $q=1$, interpreted as a polynomial limit, is the ordinary
multinomial coefficient $M_1(b_1,\ldots,b_m)$.

Let

```math
F_q(N,k)
=
\prod_a
M_q\!\left(B_{a,1}(N,k),\ldots,B_{a,m_a}(N,k)\right),
\qquad
A_q(N)=\sum_{k=0}^{N}F_q(N,k),
\qquad\text{(2)}
```

where the $B_{a,j}$ are homogeneous integer linear forms, nonnegative on
$0\leq k\leq N$. Write

```math
T_a(N,k)=\sum_j B_{a,j}(N,k).
```

As in the Landau-depth note, define the fiber function

```math
\Lambda(y)
=
\sum_a\left(
\left\lfloor T_a(0,y)\right\rfloor
-\sum_j\left\lfloor B_{a,j}(0,y)\right\rfloor
\right),
\qquad 0<y<1,
\qquad\text{(3)}
```

and let $d=\min_{0<y<1}\Lambda(y)$.

## 2. Exact cyclotomic Landau filtration

### Theorem 1

For every integer $m\geq2$,

```math
v_{\Phi_m(q)}\!\left(F_q(N,k)\right)
=
\sum_a\left(
\left\lfloor\frac{T_a(N,k)}m\right\rfloor
-\sum_j\left\lfloor\frac{B_{a,j}(N,k)}m\right\rfloor
\right).
\qquad\text{(4)}
```

If $m\mid N$, this becomes the exact fiber identity

```math
v_{\Phi_m(q)}\!\left(F_q(N,k)\right)
=
\Lambda\!\left(\left\{\frac{k}{m}\right\}\right).
\qquad\text{(5)}
```

#### Proof

The cyclotomic factorization

```math
(q;q)_n
=
\prod_{m\geq1}\Phi_m(q)^{\lfloor n/m\rfloor}
\qquad\text{(6)}
```

gives (4) immediately. If $m\mid N$, split $k/m$ into its integer
and fractional parts. Homogeneity and
$T_a=\sum_jB_{a,j}$ cancel all integer contributions, leaving (5).

Thus the p-adic carry filtration is the specialization of a finer
cyclotomic filtration:

```math
v_p(F_1(N,k))
=
\sum_{i\geq1}
v_{\Phi_{p^i}(q)}(F_q(N,k)),
\qquad\text{(7)}
```

because $\Phi_{p^i}(1)=p$.

### The A183068 summand

For

```math
F_q(N,k)
=
M_q(k,k,k,k,N-k,N-k),
\qquad\text{(8)}
```

suppose $p^t\mid N$, put $s=v_p(k)<t$, and write
$u_i=k\bmod p^i$ for $s<i\leq t$. Then (5) gives the exact exponent

```math
v_{\Phi_{p^i}(q)}(F_q(N,k))
=
2+\left\lfloor\frac{2u_i}{p^i}\right\rfloor.
\qquad\text{(9)}
```

Consequently,

```math
\prod_{i=s+1}^{t}\Phi_{p^i}(q)^2
\quad\text{divides}\quad F_q(N,k).
\qquad\text{(10)}
```

At $p=2$, the first active residue is
$u_{s+1}=2^s$, so the first factor in (10) occurs to the third power.
Evaluating at $q=1$ recovers exactly the termwise valuation and binary
bonus used in the A183068 proof.

## 3. A universal square-cyclotomic q-congruence

Write $B_q(a,b)=M_q(b,a-b)$ for the q-binomial polynomial. Clark's
q-analogue of Babbage's congruence states that, for positive integers
$a,b,n$,

```math
B_q(an,bn)
\equiv
B_{q^{n^2}}(a,b)
\pmod{\Phi_n(q)^2},
\qquad\text{(11)}
```

with the boundary cases interpreted trivially. Factoring a q-multinomial
into q-binomials gives

```math
M_q(nb_1,\ldots,nb_m)
\equiv
M_{q^{n^2}}(b_1,\ldots,b_m)
\pmod{\Phi_n(q)^2}.
\qquad\text{(12)}
```

### Theorem 2

Let $e=\min(d,2)$. For every integer $n\geq2$ and every $N\geq0$,

```math
A_q(nN)
\equiv
A_{q^{n^2}}(N)
\pmod{\Phi_n(q)^e}.
\qquad\text{(13)}
```

In particular, every Landau-depth-$2$ family has a uniform
square-cyclotomic q-supercongruence.

#### Proof

Split the sum on the left according to whether $n\mid k$.
If $n\nmid k$, (5) shows that the summand is divisible by
$\Phi_n(q)^d$. If $k=n\ell$, every bottom entry is scaled by $n$,
so (12) replaces the summand with $F_{q^{n^2}}(N,\ell)$ modulo
$\Phi_n(q)^2$. Summing over $\ell$ proves (13).

When $n=p^r$, evaluation at $q=1$ turns the modulus into $p^e$.
The q-congruence is finer than that specialization because it retains
the primitive-root information before the carry levels are collapsed.

### The square theorem does not promote to a product modulus

For the A183068 case, it is tempting to conjecture the adjacent-scale
strengthening

```math
\mathcal A_{4,2}(Np^r;q)
\stackrel{?}{\equiv}
\mathcal A_{4,2}(Np^{r-1};q^{p^2})
\pmod{\prod_{i=1}^{r}\Phi_{p^i}(q)^2}.
\qquad\text{(13a)}
```

At $q=1$, its modulus would become $p^{2r}$. However, (13a) is false
already for $(p,r,N)=(2,2,1)$. Reducing at a primitive fourth root $q=i$
gives exactly

```math
\mathcal A_{4,2}(4;i)=26,
\qquad
\mathcal A_{4,2}(2;i^4)=3246,
```

so the difference is $-3220$, not zero. It is therefore not divisible even
by $\Phi_4(q)$.

This counterexample fixes the scope of Theorem 2. The exact cyclotomic
filtration still proves the entire vanishing stratum after specialization,
but the rescaling stratum needs the prime-sensitive integer
Ljunggren--Jacobsthal--Kazandzidis estimate. The one-level q-congruence is a
valid refinement; it is not an independent all-level proof of the classical
supercongruence.

## 4. The second q-jet and a corrected cubic theorem

For a tuple $\mathbf b=(b_1,\ldots,b_m)$ define its pair energy

```math
W(\mathbf b)=\sum_{1\leq i<j\leq m}b_i b_j.
\qquad\text{(14)}
```

Straub's q-analogue of Ljunggren's congruence implies, for primes
$p\geq5$,

```math
M_q(p\mathbf b)
\equiv
M_{q^{p^2}}(\mathbf b)
-
\frac{p^2-1}{24}
(q^p-1)^2
M_1(\mathbf b)W(\mathbf b)
\pmod{\Phi_p(q)^3}.
\qquad\text{(15)}
```

Indeed, factor the multinomial into q-binomials and apply Straub's
formula to each factor. The relative correction from a split
$a=b+(a-b)$ is

```math
\frac{p^2-1}{24}\,b(a-b)(q^p-1)^2.
```

Adding over the successive splits gives
$\sum_{i<j}b_i b_j$, independently of the chosen factorization order.

For the product in (2), set

```math
W(N,k)
=
\sum_a\sum_{1\leq i<j\leq m_a}
B_{a,i}(N,k)B_{a,j}(N,k)
\qquad\text{(16)}
```

and

```math
D(N)=\sum_{k=0}^{N}F_1(N,k)W(N,k).
\qquad\text{(17)}
```

### Theorem 3

If the Landau depth is at least $3$, then for every prime $p\geq5$,

```math
A_q(pN)
\equiv
A_{q^{p^2}}(N)
-
\frac{p^2-1}{24}
(q^p-1)^2D(N)
\pmod{\Phi_p(q)^3}.
\qquad\text{(18)}
```

#### Proof

Terms with $p\nmid k$ vanish modulo $\Phi_p(q)^3$ by (5).
For $k=p\ell$, apply (15) to every multinomial factor. Since
$(q^p-1)^2$ is already divisible by $\Phi_p(q)^2$, all other factors
in a first correction term may be reduced modulo $\Phi_p(q)$, where
they become their ordinary multinomial values. Products of two
correction terms vanish modulo $\Phi_p(q)^4$. The surviving
first-order corrections therefore add to (17), proving (18).

At $q=1$, the correction itself vanishes and
$\Phi_p(1)^3=p^3$. Thus (18) specializes to the classical one-step
congruence

```math
A_1(pN)\equiv A_1(N)\pmod {p^3}.
\qquad\text{(19)}
```

The new information in (18) is the explicit second cyclotomic jet.
It also gives a manufacturing rule: signed or weighted families for which
$D(N)$ cancels acquire an uncorrected cubic q-congruence; otherwise (18)
identifies the unique counterterm required to produce one.

## 5. The explicit two-parameter family

For positive integers $u,v$, define

```math
\mathcal A_{u,v}(N;q)
=
\sum_{k=0}^{N}
M_q(
\underbrace{k,\ldots,k}_{u\ \mathrm{times}},
\underbrace{N-k,\ldots,N-k}_{v\ \mathrm{times}}
).
\qquad\text{(20)}
```

Its fiber depth is $\min(u,v)$. Hence for $u,v\geq2$,

```math
\mathcal A_{u,v}(nN;q)
\equiv
\mathcal A_{u,v}(N;q^{n^2})
\pmod{\Phi_n(q)^2}
\qquad(n\geq2).
\qquad\text{(21)}
```

The case $(u,v)=(4,2)$ is a square-cyclotomic q-lift of A183068.

For $u,v\geq3$, Theorem 3 applies with

```math
W_{u,v}(N,k)
=
\binom{u}{2}k^2
+
\binom{v}{2}(N-k)^2
+
uvk(N-k).
\qquad\text{(22)}
```

It supplies an explicit corrected cubic q-congruence for every member of
this infinite family and every prime $p\geq5$.

## 6. What came from Kac--Cheung

Kac and Cheung organize q-derivatives, q-Taylor expansion, q-binomial
coefficients, finite-field interpretations, and basic hypergeometric
functions as one calculus. For this project the useful lesson is to treat a
power of $\Phi_n(q)$ as a jet condition at primitive $n$th roots of unity:

- the Landau function gives the zeroth-order vanishing multiplicity exactly;
- Clark's theorem identifies the first surviving scaled jet;
- Straub's theorem computes the second defect;
- higher q-Taylor coefficients suggest a hierarchy of computable defect
  moments beyond $D(N)$.

This is compatible with the creative q-microscope of Guo and Zudilin, which
proves supercongruences by constructing q-congruences and examining them at
roots of unity. The present note isolates the balanced multinomial subclass,
where the first two steps are algorithmic.

## 7. The Scholze connection, precisely delimited

Bhatt and Scholze's q-crystalline prism is

```math
\left(
\mathbb Z_p[[q-1]],
([p]_q)
\right),
\qquad
[p]_q=\frac{q^p-1}{q-1},
\qquad
\varphi(q)=q^p.
\qquad\text{(23)}
```

For prime $p$, $[p]_q=\Phi_p(q)$. Therefore (13) and (18) are,
respectively, second- and third-order congruences in the prismatic ideal,
and the substitution $q\mapsto q^{p^2}$ is the second Frobenius iterate
$\varphi^2$ on the coordinate.

This is a conceptual interpretation, not a claim that the proof uses
prismatic cohomology. No prismatic object has yet been attached to the
multinomial sums. A serious next step would be to identify families whose
defect moments arise as Frobenius data of an actual q-de Rham or prismatic
complex. Until then, the elementary polynomial proof is the theorem.

## 8. Literature boundary

The components are established:

- q-factorials, q-Taylor formulas, and q-binomial calculus are standard;
- the exact cyclotomic factorization of q-factorial ratios is known;
- Clark proves the square-cyclotomic q-Babbage congruence;
- Straub proves the cubic q-Ljunggren congruence;
- Adamczewski--Bell--Delaygue--Jouhet prove broad cyclotomic and q-Lucas
  results for q-factorial multisums;
- Guo--Zudilin's q-microscope reaches deep hypergeometric
  supercongruences.

The candidate contribution here is the packaging: fiber depth gives a
mechanical square-congruence generator, while the pair energy gives a
closed corrected cubic theorem for the same balanced multinomial class.
A preliminary search did not locate equations (13) and (18) in this exact
generality, but that is not a priority certificate.

Primary references:

1. V. Kac and P. Cheung, *Quantum Calculus*,
   <https://link.springer.com/book/10.1007/978-1-4613-0071-7>.
2. W. E. Clark, *q-Analogue of a Binomial Coefficient Congruence*,
   <https://doi.org/10.1155/S016117129500024X>.
3. A. Straub, *A q-analog of Ljunggren's binomial congruence*,
   <https://arxiv.org/abs/1103.3258>.
4. B. Adamczewski, J. P. Bell, E. Delaygue, and F. Jouhet,
   *Congruences modulo cyclotomic polynomials and algebraic independence
   for q-series*, <https://arxiv.org/abs/1701.06378>.
5. B. Adamczewski, J. P. Bell, E. Delaygue, and F. Jouhet,
   *Cyclotomic valuation of q-Pochhammer symbols and q-integrality of
   basic hypergeometric series*,
   <https://doi.org/10.4064/aa230428-19-9>.
6. V. J. W. Guo and W. Zudilin, *A q-microscope for supercongruences*,
   <https://arxiv.org/abs/1803.01830>.
7. V. J. W. Guo and W. Zudilin,
   *Dwork-type supercongruences through a creative q-microscope*,
   <https://arxiv.org/abs/2001.02311>.
8. B. Bhatt and P. Scholze, *Prisms and Prismatic Cohomology*,
   <https://arxiv.org/abs/1905.08229>.

## 9. Exact checks

Run

```text
python verification/related/verify_q_calculus_supercongruence.py
```

The dependency-free checker verifies:

- 44,590 exact cyclotomic Landau identities;
- 1,567 active A183068 cyclotomic levels, including the binary bonus;
- 24 square-cyclotomic polynomial congruences at scales $2,3,4,5$;
- the exact $-3220$ obstruction to the natural multilevel promotion; and
- 12 corrected cubic polynomial congruences for $p=5,7$.

The program performs arithmetic in
$\mathbb Z[q]/(\Phi_n(q)^e)$ directly; it does not infer polynomial
divisibility from numerical evaluation.
