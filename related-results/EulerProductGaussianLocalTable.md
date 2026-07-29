# The complete Gaussian local table for colored Euler-product towers

**Status.** Complete corollary of the odd-prime colored Euler-product
theorem and the restored dyadic theorem; exact local-valuation checks pass.
This is a prime-ideal formulation of those coefficientwise results, not a
theorem about Gaussian factorials or rectangular Gaussian binomial
coefficients.

## 1. Setup

For finitely many colors \(\nu\), integral exponent rules \(h_{\nu,m}\), and
\(d\geq1\), put

```math
\mathcal E_N(\mathbf Z)
=
[x^N]\prod_{\nu}\prod_{m\geq1}
(1-Z_\nu x^m)^{N h_{\nu,m}m^d}.
\qquad\text{(1)}
```

Let

```math
e_2(r)=
\begin{cases}
1,&r=1,\\
2r,&r\geq2.
\end{cases}
\qquad\text{(2)}
```

The two inputs are:

```math
\mathcal E_{np^r}(\mathbf Z)
\equiv
\mathcal E_{np^{r-1}}(\mathbf Z^p)
\pmod {p^{2r}}
\qquad(p\ {\rm odd}),
\qquad\text{(3)}
```

from the
[colored Euler-product theorem](EulerProductGaussianTower.md), and

```math
\mathcal E_{n2^r}(\mathbf Z)
\equiv
\mathcal E_{n2^{r-1}}(\mathbf Z^2)
\pmod {2^{e_2(r)}},
\qquad\text{(4)}
```

from the
[dyadic hypercube theorem](DyadicHypercubeDefect.md).

## 2. Gaussian specialization

Specialize every color variable to \(i\). For one color, write

```math
D_{p,r}
=
\mathcal E_{np^r}(i)
-
\mathcal E_{np^{r-1}}(i^p)
\in\mathbb Z[i].
\qquad\text{(5)}
```

The multicolored statement is identical, with each \(i\) replaced by the
chosen fourth root of unity.

### Theorem 1 (complete local table)

For every \(n,r\geq1\):

1. If \(p\equiv3\pmod4\), then \(p\) is a Gaussian prime and

   ```math
   v_p(D_{p,r})\geq2r.
   \qquad\text{(6)}
   ```

   Here \(i^p=-i\), so the lower value is the complex conjugate of the
   untwisted \(i\)-value when the coefficients are real.

2. If \(p\equiv1\pmod4\) and
   \(p=\pi\overline\pi\), then

   ```math
   v_\pi(D_{p,r})\geq2r,
   \qquad
   v_{\overline\pi}(D_{p,r})\geq2r.
   \qquad\text{(7)}
   ```

   Here \(i^p=i\), so this is an adjacent-scale congruence at both split
   Gaussian prime ideals.

3. At the ramified prime, put \(\varpi=1+i\). Then

   ```math
   v_\varpi(D_{2,r})
   \geq
   2e_2(r)
   =
   \begin{cases}
   2,&r=1,\\
   4r,&r\geq2.
   \end{cases}
   \qquad\text{(8)}
   ```

   The lower twist is \(i^2=-1\). Thus the binary statement is a
   ramified cross-twist, not a same-value congruence.

#### Proof

Evaluation at fourth roots of unity is a ring homomorphism

```math
\mathbb Z[\mathbf Z]\longrightarrow\mathbb Z[i].
```

Therefore (3) gives

```math
D_{p,r}\in p^{2r}\mathbb Z[i]
\qquad(p\ {\rm odd}).
\qquad\text{(9)}
```

If \(p\equiv3\pmod4\), the ideal \((p)\) stays prime in
\(\mathbb Z[i]\), which proves (6). If \(p\equiv1\pmod4\), then

```math
(p)=(\pi)(\overline\pi)
```

with coprime prime ideals. Equation (9) is therefore simultaneous
divisibility by \(\pi^{2r}\) and \(\overline\pi^{2r}\), proving (7).

Finally,

```math
2=-i(1+i)^2=-i\varpi^2.
\qquad\text{(10)}
```

Specializing (4) at \(i\) gives divisibility by \(2^{e_2(r)}\), which is
exactly divisibility by \(\varpi^{2e_2(r)}\). This proves (8).
\(\square\)

## 3. What the table completes

The result removes an ambiguity that recurs in Gaussian formulations:

| Rational prime | Local behavior in \(\mathbb Z[i]\) | Frobenius twist | Proved depth |
| --- | --- | --- | --- |
| \(p\equiv3\pmod4\) | inert | \(i\mapsto-i\) | \(p^{2r}\) |
| \(p\equiv1\pmod4\) | split as \(\pi\overline\pi\) | \(i\mapsto i\) | both \(\pi^{2r}\) and \(\overline\pi^{2r}\) |
| \(p=2\) | ramified as a unit times \((1+i)^2\) | \(i\mapsto-1\) | \((1+i)^2\) at \(r=1\), then \((1+i)^{4r}\) |

The split row is stronger than a one-sided congruence at a selected prime:
both conjugate prime ideals occur because the source congruence is over
\(\mathbb Z\). The ramified row is qualitatively different: the residue
field has only two elements and the fourth root \(i\) collapses to \(-1\)
under the binary Frobenius lift.

The table does **not** assert:

- a congruence for Kalinin's rectangular Gaussian coefficients;
- an intrinsic factorial theory in \(\mathbb Z[i]\);
- a statement about the spatial distribution of Gaussian primes; or
- the still stronger cubic exponent conjectured for the untwisted
  A380290 sequence.

## 4. Sharpness and exact checks

The odd-prime specialization attains the stated depth for the reciprocal
\(d=2\) product at inert primes \(3,7,11\) and split primes
\(5,13,17\) in the exact test range.

At the ramified prime, the unrestricted coefficientwise theorem has sharp
exponent \(e_2(1)=1\) and \(e_2(r)=2r\) for every \(r\geq2\).
After evaluation at \(i\), exact examples attain
\(v_{1+i}=2\) at \(r=1\), and the even-part exponent pattern

```math
h_m=
\begin{cases}
0,&m\ {\rm odd},\\
1,&m\ {\rm even}
\end{cases},
\qquad d=1,
\qquad\text{(11)}
```

attains \(v_{1+i}=4r\) for every tested \(2\leq r\leq5\). The latter is
recorded as a finite sharpness certificate, not an all-\(r\) theorem.

Run:

```text
python verification/related/verify_dyadic_hypercube_defect.py
```

The checker evaluates the Gaussian differences exactly, computes valuations
at inert primes, at both factors of split primes, and at \(1+i\), and
verifies the table and the displayed equality cases.

## 5. Literature boundary

The standard published context is the theory of Gauss congruences and their
higher-order variants. Beukers--Houben--Straub treat Gauss congruences for
multivariate rational functions, while Gorodetsky explicitly uses the term
"Gauss congruences of order \(s\)" for modulus \(p^{sr}\). Those frameworks
explain the vocabulary but do not, by citation alone, supply the
occupation-stratum proof or the exceptional binary law above.

A particularly close-looking 2025 preprint on Witt--Hadamard calculus,
number-field norm descent, and prime-ideal ladders has been withdrawn. Its
arXiv record states that major number-field Dold-congruence and norm-descent
claims contain errors. It is therefore not used as a proof input here.

References:

1. F. Beukers, M. Houben, and A. Straub,
   [*Gauss congruences for rational functions in several
   variables*](https://arxiv.org/abs/1710.00423).
2. O. Gorodetsky,
   [*New representations for all sporadic Apery-like sequences, with
   applications to congruences*](https://doi.org/10.1080/10586458.2021.1982080).
3. H. S. Bal,
   [*Dold--Gauss congruences, norm descent, and rational
   rigidity*](https://arxiv.org/abs/2509.25038), withdrawn; cited only as
   a literature boundary.
