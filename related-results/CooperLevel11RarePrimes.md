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
\tag{1}
```

Cooper conjectures that

```math
T(pn)\equiv T(n)\pmod {p^2}
\quad(n\ge1)
\tag{2}
```

for $p=2,59,5581$.  His search found no other prime below $10^4$.

## 1. The $n=1$ obstruction is already selective

Define

```math
q_p=\frac{T(p)-T(1)}p\pmod p.
\tag{3}
```

The Lucas congruence predicts the numerator is divisible by $p$, while
(2) forces $q_p=0$.

An exact scan of every odd prime below $30,000$ found

```math
q_p=0
\quad\Longleftrightarrow\quad
p\in\{59,5581\}.
\tag{4}
```

Thus Cooper's rare primes are already singled out by the first instance of
the conjecture throughout a range three times larger than the published
search.  This strongly suggests that the right object to understand is the
single Frobenius obstruction $q_p$, rather than separate congruences for
every $n$.

## 2. Extended checks at the exceptional primes

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

## 3. Research direction

The next useful theorem would be an equivalence of the form

```math
q_p=0
\quad\Longrightarrow\quad
T(pn)\equiv T(n)\pmod {p^2}\ \text{for every }n,
\tag{5}
```

derived from the level-11 modular parametrization or a Frobenius matrix.
That would turn an infinite family of congruences into one computable
prime-local condition and explain why exceptional primes can be rare.

The carry-depth method does not directly prove (5): recurrence (1) has no
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
prime scan through $30,000$.
