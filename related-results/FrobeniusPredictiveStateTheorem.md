# Exact predictive-state complexity of a Frobenius obstruction cycle

## Status

This note applies standard finite-state and Markov-chain ideas to the
degree-seven Frobenius obstruction cycle already constructed in this
repository. The general state-minimization statements are classical. The
exact values $19{,}500$ and $1{,}824$, and the explicit witness below,
are deductions for this arithmetic cycle.

The result is a model-selection boundary, not a new proof of the underlying
supercongruence. It shows exactly how much information an exact predictive
model of the observed valuation process must retain.

## 1. The arithmetic word

Work at $p=5$ and precision $5^4$. Let $B_r$ be the degree-seven
Frobenius packet from
[the transfer-matrix note](FrobeniusTransferThermodynamics.md), and put

$$
d_r=\min\!\left\{4,\,
v_5(B_{r-1}-B_r)\right\}.
$$

Starting at $r=17$, this produces a cyclic word

$$
w=(d_{17},d_{18},\ldots,d_{19516})
$$

of length

$$
L=19{,}500.
$$

Let $T$ be cyclic shift of the phase and let $d$ be the displayed
valuation observable.

## 2. Exact model-selection theorem

For a phase $i$, write

$$
H_h(i)=
\bigl(d(T^{-h+1}i),\ldots,d(i)\bigr)
$$

for its length-$h$ valuation history.

### Theorem

The degree-seven valuation cycle has the following properties.

1. Its least output period is $19{,}500$.
2. The valuation partition is not a one-step Markov lumping. Its possible
   next values are

   $$
   \begin{array}{c|c}
   d(i)&\{d(Ti)\}\\ \hline
   0&\{0,1,2,3,4\}\\
   1&\{0,1,2\}\\
   2&\{0,1,3\}\\
   3&\{0,1,2,3,4\}\\
   4&\{0,1,2,3\}.
   \end{array}
   $$

3. The least history length that determines the next valuation exactly is

   $$
   \boxed{h_{\min}=1{,}824.}
   $$

4. At that length all $19{,}500$ histories are distinct. Consequently the
   coarsest deterministic quotient preserving the complete future valuation
   sequence has $19{,}500$ states: there is no nontrivial exact predictive
   compression.

### Exact minimality witness

The phases $r=11{,}856$ and $r=15{,}756$ have identical preceding
histories of length $1{,}823$, but their next valuations are respectively

$$
4\qquad\text{and}\qquad3.
$$

The common history contains

$$
1{,}498,\ 255,\ 52,\ 15,\ 3
$$

occurrences of $0,1,2,3,4$, respectively, and has SHA-256 digest

```text
7ddbcdcae2330f4f474659bbf0678d3213c1196f2c78d7557ddc9fc39a8d9d8e
```

Thus no history of length at most $1{,}823$ can predict the next value.
Direct enumeration shows that every length-$1{,}824$ history is unique,
which proves sufficiency and minimality.

Finally, two phases have the same complete future output precisely when
their difference is a period of $w$. Since the least period is $L$, all
future-equivalence classes are singletons. This proves the last assertion.

## 3. Mixing: what is true and what is not

Regard cyclic shift as the transition matrix

$$
P(i,j)=
\begin{cases}
1,&j=i+1\pmod L,\\
0,&\text{otherwise}.
\end{cases}
$$

The uniform distribution $\pi$ is stationary, but the chain does not mix:
for every phase $i$ and every time $t$,

$$
\left\|\delta_iP^t-\pi\right\|_{\mathrm{TV}}
=1-\frac1L.
$$

This is an exact obstruction to importing mixing terminology into the
deterministic arithmetic orbit.

One can deliberately add randomness by using the lazy kernel

$$
K=\frac12(I+P).
$$

This new chain is irreducible and aperiodic. If
$\zeta_L=e^{2\pi i/L}$, its eigenvalues are

$$
\lambda_j=\frac{1+\zeta_L^j}{2},
\qquad
0\le j<L,
$$

so its second-largest eigenvalue modulus is

$$
\cos\!\left(\frac{\pi}{L}\right).
$$

Its inverse absolute spectral gap is therefore

$$
t_{\mathrm{abs}}
=
\frac{1}{1-\cos(\pi/19500)}
\approx 77{,}054{,}760.46.
$$

That is a theorem about a chosen randomized sampler, not about the original
Frobenius recurrence.

## 4. Consequence for model selection

The scalar valuation $d_r$ is not a sufficient Markov state. Any exact
model must retain either

- the full $19{,}500$-phase state; or
- enough history to distinguish it, requiring $1{,}824$ scalar lags.

Approximate compression may still be useful, but then the approximation
error, lost threshold events, and mixing behavior must be measured rather
than inferred from the histogram alone.

This is the useful connection with the mixing-time framework of
Levin--Peres: first identify an actual stochastic kernel and an adequate
state, then ask about stationarity, spectral gap, coupling, or cutoff. A
histogram of a deterministic periodic observable supplies none of those
properties automatically.

The autonomous-engine framework of Alicki--Gelbwaser-Klimovsky--Jenkins is
relevant only if an external controller is introduced that spends
computational work to choose lifts or queries under noise and load. That
could model a counterexample-search algorithm. It is not an input to the
number-theoretic theorem above.

## 5. Verification

Run:

```text
python verification/related/verify_frobenius_predictive_state.py
```

The checker recomputes the arithmetic word from the trace recurrence, proves
its least period by the prefix-function algorithm, checks every one-step
transition, verifies the length-$1{,}823$ witness, and confirms that all
length-$1{,}824$ histories are distinct.

## References

- D. A. Levin and Y. Peres, with contributions by E. L. Wilmer,
  [*Markov Chains and Mixing Times*, second edition][LPW].
- R. Alicki, D. Gelbwaser-Klimovsky, and A. Jenkins,
  [*The problem of engines in statistical physics*][engine].

[LPW]: https://pages.uoregon.edu/dlevin/MARKOV/markovmixing.pdf
[engine]: https://arxiv.org/abs/2108.07428
