# Cooper's level-11 rare-prime supercongruence

**Status:** exact computation and proof target, not a proof, 2026-07-25.

Let $T(0)=1$ and

```math
\begin{aligned}
(n+1)^3T(n+1)
={}&2(2n+1)(5n^2+5n+2)T(n)\\
&-8n(7n^2+1)T(n-1)\\
&+22n(2n-1)(n-1)T(n-2).
\end{aligned}
\qquad\text{(1)}
```

Cooper conjectures that

```math
T(pn)\equiv T(n)\pmod {p^2}
\quad(n\ge1)
\qquad\text{(2)}
```

for $p=2,59,5581$.  His search found no other prime below $10^4$.

## 1. The $n=1$ obstruction is already selective

Define

```math
q_p=\frac{T(p)-T(1)}p\pmod p.
\qquad\text{(3)}
```

The Lucas congruence predicts the numerator is divisible by $p$, while
(2) forces $q_p=0$.

An exact scan of every odd prime below $30,000$ found

```math
q_p=0
\quad\Longleftrightarrow\quad
p\in\{59,5581\}.
\qquad\text{(4)}
```

Thus Cooper's rare primes are already singled out by the first instance of
the conjecture throughout a range three times larger than the published
search.  This strongly suggests that the right object to understand is the
single Frobenius obstruction $q_p$, rather than separate congruences for
every $n$.

## 2. A first-order Frobenius law

Put

```math
D_p(n)=\frac{T(pn)-T(n)}p\pmod p.
\qquad\text{(5)}
```

An independent exact computation found the stronger pattern

```math
D_p(n)\equiv nT(n-1)q_p\pmod p
\qquad\text{(6)}
```

in all 350 tested pairs consisting of every odd prime $p\le103$ with
$p\ne11$ and every $1\le n\le14$. In particular, the right side vanishes
at $p=59$, as it should.

Equation (6) is presently a **computational theorem target**, not a proved
identity. If it holds for a fixed prime $p$ and every $n\ge1$, then it gives
the exact equivalence

```math
q_p=0
\quad\Longleftrightarrow\quad
T(pn)\equiv T(n)\pmod {p^2}
\ \text{for every }n\ge1.
\qquad\text{(7)}
```

The reverse implication already follows from $n=1$, because
$1\cdot T(0)=1$. Thus (6), rather than a separate congruence for every
$n$, is the natural strengthening of the target formerly stated below.

The factor

```math
U(n)=nT(n-1)
\qquad\text{(8)}
```

has the form of a formal derivative coefficient. The general
[Frobenius-quotient identity](FrobeniusQuotientConstantTerms.md) proves this
shape more precisely for any fixed Laurent-polynomial model
$T(n)=\mathrm{CT}(\Lambda_{11}^n)$. If

```math
R_{p,11}=
\frac{\Lambda_{11}(\mathbf x)^p-\Lambda_{11}(\mathbf x^p)}p,
```

then

```math
D_p(n)\equiv
n\mathrm{CT}\!\left(
\Lambda_{11}(\mathbf x^p)^{n-1}R_{p,11}
\right)
\pmod p.
```

Thus (6) would follow from one explicit rank-one pairing identity for
$R_{p,11}$. The standard Newton-polytope Dwork theorem does not state that
pairing automatically. A recurrence linearization, a stronger unit-root
argument, or a direct constant-term proof is still required.

The analogous second-level defect is not naively proportional to $q_p$.
Reported tests found a different invariant which can vanish at
$p=7,13,17,19$ even when $q_p\ne0$. Consequently (6), even if proved,
must not be iterated to claim the $r\ge2$ congruence.

## 3. A rejected modular-form shortcut

Level $11$ makes the weight-two newform
$\eta(z)^2\eta(11z)^2$, equivalently the curve
[$X_0(11)$](https://www.lmfdb.org/EllipticCurve/Q/11a1/), a natural object
to test. However, the simplest proposed identification of the obstruction
with $a_p-2$ is false.

For the model

```math
E:\quad y^2+y=x^3-x^2-10x-20,
\qquad a_p=p+1-\#E(\mathbb F_p),
\qquad\text{(9)}
```

exact point counts give

```math
q_{59}=0,\quad a_{59}=5,
\qquad\text{and}\qquad
q_{101}=91,\quad a_{101}=2.
\qquad\text{(10)}
```

Either witness rules out
$q_p=u_p(a_p-2)$ with $u_p$ a $p$-adic unit, and together they rule out
equality of the two vanishing loci in both directions. Modular structure
may still control $D_p$, but not through this trace-$2$ shortcut.

## 4. Extended checks at the exceptional primes

A $p$-adic recurrence evaluator avoids constructing the enormous exact
integers.  It tracks enough precision to divide by every factor
$(n+1)^3$ and finishes with precision $p^2$.

The following exact checks passed:

| Prime | Checked range | Previously stated range |
| ---: | ---: | ---: |
| $59$ | $1\le n\le2,000$ | $1\le n\le1,694$ |
| $5581$ | $1\le n\le100$ | $1\le n\le17$ |

These computations strengthen the evidence, especially at $5581$, but do
not prove (2).

## 5. Research direction

The next useful theorem is the first-order law (6). It would imply the
formerly proposed equivalence

```math
q_p=0
\quad\Longrightarrow\quad
T(pn)\equiv T(n)\pmod {p^2}\ \text{for every }n,
\qquad\text{(11)}
```

from the level-11 modular parametrization or a Frobenius matrix. This would
turn an infinite family of congruences into one computable prime-local
condition and explain why exceptional primes can be rare.

The carry-depth method does not directly prove (11): recurrence (1) has no
known balanced factorial-ratio summand whose strata transfer termwise.
This is the boundary where the project genuinely becomes a Dwork/Frobenius
problem.

Source: S. Cooper,
*Apéry-like sequences defined by four-term recurrence relations*,
<https://arxiv.org/abs/2302.00757>, Conjecture 11.1.

Run the reproducibility script with

```text
python verification/related/verify_cooper_level11.py
```

and add `--extended` to reproduce the larger ranges in the table and the
prime scan through $30,000$. The repository checker does not yet reproduce
the separately reported 350 cases of (6); they are recorded as external exact
evidence rather than silently folded into the checker count.
