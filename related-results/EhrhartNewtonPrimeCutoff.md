# An Ehrhart cutoff for Newton-polytope rank primes

**Status:** exact elementary deduction from the sharp Ehrhart-volume theorem
in Chapter 8 of OpenAI's August 2026 collection. The source theorem is accepted
here as an external result with a public Lean certificate; the implication
below is proved in this repository.

## 1. Source input

The source theorem states that if a full-dimensional compact convex body
$K\subset\mathbb R^d$ has barycenter $0$ and

```math
\operatorname{int}(K)\cap\mathbb Z^d=\{0\},
```

then

```math
\operatorname{vol}(K)\le \frac{(d+1)^d}{d!}.
```

This note extracts the finite arithmetic consequence relevant to
constant-term and Frobenius calculations.

## 2. Determinant cutoff

### Theorem

Let $K$ satisfy the source theorem's hypotheses and let
$m_0,\ldots,m_d\in K\cap\mathbb Z^d$.  Put

```math
D(m_0,\ldots,m_d)
=\det(m_1-m_0,\ldots,m_d-m_0)\in\mathbb Z.
```

Then either $D=0$ or

```math
1\le |D|\le (d+1)^d.
```

Consequently, for every prime $p>(d+1)^d$,

```math
D\not=0\text{ in }\mathbb Q
\quad\Longleftrightarrow\quad
D\not\equiv0\pmod p.
```

Thus reduction modulo such a prime preserves full-dimensional affine
independence among lattice points of $K$.

### Proof

The simplex

```math
S=\operatorname{conv}(m_0,\ldots,m_d)
```

lies in $K$, and

```math
\operatorname{vol}(S)=\frac{|D|}{d!}.
```

If $D\ne0$, integrality gives $|D|\ge1$, while monotonicity of volume and the
source theorem give

```math
\frac{|D|}{d!}
\le \operatorname{vol}(K)
\le \frac{(d+1)^d}{d!}.
```

Hence $|D|\le(d+1)^d$.  A prime larger than this bound cannot divide a
nonzero $D$.  The reverse implication is automatic because an integer that is
zero is zero after reduction.  This proves the result.

The same conclusion holds after reduction modulo any prime ideal of a number
field whose residue characteristic exceeds $(d+1)^d$.

## 3. Sharpness of the uniform number

Let

```math
K_d=(d+1)\operatorname{conv}(0,e_1,\ldots,e_d)-(1,\ldots,1).
```

Its barycenter is $0$.  Its integral interior points satisfy
$x_i\ge0$ and $\sum_i x_i\le0$, so the origin is the only one.  Its edge
matrix is $(d+1)I_d$, and therefore its vertex determinant is exactly

```math
(d+1)^d.
```

So the determinant bound cannot be lowered uniformly.

| Dimension $d$ | Uniform cutoff $(d+1)^d$ |
| ---: | ---: |
| 1 | 2 |
| 2 | 9 |
| 3 | 64 |
| 4 | 625 |
| 5 | 7,776 |
| 6 | 117,649 |

## 4. What this changes in congruence audits

Let

```math
\Lambda=\sum_{m\in A}c_mx^m
```

be a Laurent polynomial whose Newton polytope $K=\operatorname{conv}(A)$
satisfies the source hypotheses.  Any Frobenius, face, or collision argument
whose bad reduction is detected by a full-dimensional exponent determinant
now has a finite exceptional-prime search:

```math
p\le(d+1)^d.
```

Above that cutoff, reduction cannot manufacture a new full-dimensional affine
dependence in the exponent configuration.  This is useful when a congruence
proof first separates a generic-rank case from finitely many singular primes.

The conclusion is deliberately limited:

- it controls rank degeneration, not a $p$-adic error exponent;
- it does not prove a Dwork congruence by itself;
- it does not control lower-dimensional minors from the volume estimate alone;
  and
- it does not apply to the displayed A183068 Laurent polynomial, whose Newton
  polytope has three interior lattice points rather than one.

## 5. Verification boundary

The exact checker verifies the centered-simplex sharpness family, the interior
lattice-point calculation through dimension six, and the displayed cutoff
table. These checks validate the arithmetic deduction. The source theorem is
certified separately by `EhrhartVolumeInequality.lean` in OpenAI's public
`ten-proofs` repository.

## Reference

- OpenAI, [*Ten Advances in Mathematics and Theoretical Computer Science*](https://cdn.openai.com/pdf/ten-proofs-oai.pdf),
  Chapter 8, "The Sharp Inequality in Ehrhart's Volume Conjecture," 2026.
