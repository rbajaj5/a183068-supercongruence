# Cooper's level-11 rare-prime supercongruence

**Status:** exact computation, conditional finite-state decision route, and
proof target; the first-order law remains unproved, 2026-07-26.

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

An exact computation found the stronger pattern

```math
D_p(n)\equiv nT(n-1)q_p\pmod p
\qquad\text{(6)}
```

in all 8,300 tested pairs consisting of every odd prime $p\le1,000$ with
$p\ne11$ and every $1\le n\le50$. In particular, the right side vanishes
at $p=59$, as it should. The repository checker now reproduces this larger
test directly.

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

### A three-branch refinement at $p=3$

There is an unexpectedly simple refinement of Cooper's first congruence in
Conjecture 11.2. Exact computation gives

```math
T(n)\equiv1\pmod3.
\qquad\text{(9)}
```

Define

```math
b(n)=\frac{T(n)-1}{3}\pmod3.
```

The data then obey all three base-$3$ branches

```math
\begin{aligned}
b(3n)&\equiv b(n)+n,\\
b(3n+1)&\equiv b(n)+1,\\
b(3n+2)&\equiv b(n)-n
\end{aligned}
\pmod3.
\qquad\text{(10)}
```

The first branch is exactly

```math
T(3n)\equiv T(n)+3n\pmod9,
\qquad\text{(11)}
```

which Cooper conjectured. The other two branches strengthen it to a
complete base-$3$ recursion for $T(n)$ modulo $9$. All 30,003 identities
in (10) with $0\le n\le10,000$ passed exact integer computation.

Equation (10) is still a **computational theorem target**. If proved, it
would give a finite digit formula for the entire sequence modulo $9$ and
would settle the $p=3$ part of Cooper's Conjecture 11.2. It is also
consistent with (6): here $q_3=1$, and the first branch says precisely
$D_3(n)\equiv n\pmod3$, since the data give $T(n-1)\equiv1\pmod3$.

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
\qquad\text{(12)}
```

exact point counts give

```math
q_{59}=0,\quad a_{59}=5,
\qquad\text{and}\qquad
q_{101}=91,\quad a_{101}=2.
\qquad\text{(13)}
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

## 5. What finite automata can decide

There is a useful but conditional route from diagonals to a finite proof.
Suppose an explicit rational function is found whose diagonal is the
generating function of $T$. The Rowland--Yassawi construction then produces,
for each fixed prime $p$ outside a finite exceptional set, a finite automaton
computing $T(n)$ modulo $p^2$ from the base-$p$ digits of $n$.

Under that premise, every sequence in

```math
T(pn),\qquad T(n),\qquad nT(n-1)q_p \pmod {p^2}
\qquad\text{(14)}
```

is $p$-automatic. Equality in (6) for every $n$ is therefore a finite-state
equivalence problem: form an automaton for the difference and check that no
reachable state has nonzero output. This would give a rigorous,
machine-checkable certificate for any one fixed prime, including $59$ or
$5581$.

The missing premise matters. Cooper gives recurrence (1) and a modular
parametrization, but not a rational-diagonal representation for this level-11
sequence. A $D$-finite recurrence by itself does not supply such a
representation. Thus the automaton is a concrete target, not something that
can presently be run.

This route is also prime-local. Separate automata modulo $p^\alpha$ do not
by themselves provide a modulus of continuity common to all $\alpha$, and
they do not overcome the global continuity obstruction described in
[the compactness note](PadicArzelaAscoliSupercongruenceTowers.md). The
Apéry-number congruences of Rowland--Yassawi--Krattenthaler are a valuable
model, but their differentiated-recurrence argument is specific additional
structure, not a theorem that every four-term recurrence inherits.

References:

- E. Rowland and R. Yassawi,
  [*Automatic congruences for diagonals of rational functions*](https://arxiv.org/abs/1310.8635).
- C. Krattenthaler, E. Rowland, and R. Yassawi,
  [*Lucas congruences for the Apéry numbers modulo $p^2$*](https://arxiv.org/abs/2005.04801).

## 6. Research direction

The next useful theorem is the first-order law (6). It would imply the
formerly proposed equivalence

```math
q_p=0
\quad\Longrightarrow\quad
T(pn)\equiv T(n)\pmod {p^2}\ \text{for every }n,
\qquad\text{(15)}
```

from the level-11 modular parametrization or a Frobenius matrix. This would
turn an infinite family of congruences into one computable prime-local
condition and explain why exceptional primes can be rare.

The carry-depth method does not directly prove either (6) or (10):
recurrence (1) has no known balanced factorial-ratio summand whose strata
transfer termwise.
This is the boundary where the project genuinely becomes a Dwork/Frobenius
problem.

Source: S. Cooper,
[*Apéry-like sequences defined by four-term recurrence relations*](https://arxiv.org/abs/2302.00757),
Conjecture 11.1.

Run the reproducibility script with

```text
python verification/related/verify_cooper_level11.py
```

and add `--extended` to reproduce the larger ranges in the table and the
prime scan through $30,000$, all 8,300 cases of (6), and all 30,003
base-$3$ identities in (10). The default run checks smaller ranges so that
routine repository verification stays quick.
