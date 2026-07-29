# The Bala version

## Completing the proposed proof routes for A183068

This companion note is organized around the proof routes forwarded by Peter
Bala after he was copied on correspondence about the proposed A183068
supercongruence. Its purpose is constructive: retain the useful mathematical
recognition in the AI-generated sketches, correct their incomplete formulas,
and show exactly where the completed routes meet the proof in
[`PROOF.md`](PROOF.md).

It is not a criticism of Peter Bala or Paul D. Hanna. Both explicitly
declined to certify an argument outside their expertise, and Peter warned
that AI-generated proofs may contain errors.

## 1. The theorem and the shared idea

Define

```math
a(n)=
\sum_{k=0}^{n}
\frac{(2n+2k)!}{k!^4(n-k)!^2}.
```

The conjecture recorded in [OEIS A183068](https://oeis.org/A183068) is

```math
a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}}
```

for every prime \(p\) and all positive integers \(n,r\).

The forwarded ChatGPT sketch, the quoted Claude preamble, and the repository
proof all recognize the same useful decomposition:

1. split the sum according to whether \(p\mid k\);
2. prove that the \(p\nmid k\) terms vanish;
3. rescale \(k=p\ell\) to the preceding level; and
4. reassemble the sum.

That recognition is correct. The mathematical work lies in making steps
2--3 uniform in \(r\) and valid at the exceptional primes \(2\) and \(3\).
The treatment of \(2\) also instantiates the repository-wide
[dyadic audit policy](DYADIC_POLICY.md): normalization, sign, exponent loss,
and the first lifting level are separate proof obligations.

## 2. Completing the digit-counting route

Put

```math
F(N,k)=
\frac{(2N+2k)!}{k!^4(N-k)!^2}
=
\binom{2N+2k}{k,k,k,k,N-k,N-k}.
```

This six-part multinomial representation makes both integrality and the carry
structure explicit.

### The diagnostic correction

The forwarded sketch used the identity

```math
s_p(np^r-k)=s_p(k-1)+(p-1)r
```

for \(p\nmid k\). It is not valid for general \(n\). For example, with
\(p=3,n=2,r=1,k=1\),

```math
s_3(6-1)=s_3(5)=3
\ne
2=s_3(0)+(3-1).
```

The intended carry idea nevertheless has an exact replacement.

### Exact carry calculation

Suppose \(p^t\mid N\) and \(s=v_p(k)<t\). For \(s<i\le t\), set
\(q=p^i\) and write

```math
N=qM,\qquad k=qa+u,\qquad0<u<q.
```

The contribution of level \(i\) to Legendre's formula is

```math
\begin{aligned}
\lambda_i
&=
\left\lfloor\frac{2N+2k}{q}\right\rfloor
-4\left\lfloor\frac{k}{q}\right\rfloor
-2\left\lfloor\frac{N-k}{q}\right\rfloor\\
&=
2+\left\lfloor\frac{2u}{q}\right\rfloor
\ge2.
\end{aligned}
```

There are \(t-s\) active levels. Hence

```math
v_p(F(N,k))\ge2(t-s).
```

At \(p=2\), the first active residue is \(u=2^s\), so one level contributes
\(3\) rather than \(2\):

```math
v_2(F(N,k))\ge2(t-s)+1.
```

Taking \(t=r\) and \(p\nmid k\) proves

```math
F(np^r,k)\equiv0\pmod {p^{2r}}.
```

This completes the useful digit-counting idea without the incorrect
digit-sum identity.

## 3. Completing the Morita \(p\)-adic gamma interpretation

The quoted Claude preamble suggested Morita's \(p\)-adic gamma function and a
block decomposition. That suggestion has a precise formulation.

For a tuple \(\mathbf b=(b_1,\ldots,b_m)\), put \(B=\sum_i b_i\) and define

```math
Q_p(\mathbf b)
=
\frac{\displaystyle\binom{pB}{pb_1,\ldots,pb_m}}
{\displaystyle\binom{B}{b_1,\ldots,b_m}}.
```

Let

```math
U_p(M)=
\prod_{\substack{1\le j\le M\\p\nmid j}}j.
```

Removing the multiples of \(p\) from every factorial gives the exact block
identity

```math
Q_p(\mathbf b)
=
\frac{U_p(pB)}{\prod_iU_p(pb_i)}.
```

For positive integral arguments, Morita's function satisfies

```math
U_p(pm)=(-1)^{pm+1}\Gamma_p(pm+1).
```

Consequently,

```math
\boxed{
Q_p(\mathbf b)
=
(-1)^{1-m}
\frac{\Gamma_p(pB+1)}
{\prod_i\Gamma_p(pb_i+1)}.
}
```

For the A183068 summand there are six parts, so the sign in this display is
\(-1\). This is an exact gamma-function version of the multinomial scaling
quotient.

### What the gamma notation still has to prove

Let \(s\) be the minimum valuation among the positive \(b_i\). The required
estimate is

```math
Q_p(\mathbf b)
\equiv1
\pmod {p^{\,3(s+1)-\epsilon_p}},
\qquad
\epsilon_p=
\begin{cases}
2,&p=2,\\
1,&p=3,\\
0,&p\ge5.
\end{cases}
```

This is precisely the multinomial
Ljunggren--Jacobsthal--Kazandzidis scaling lemma used in `PROOF.md`.
Expressing its quotient through \(\Gamma_p\) is legitimate, but does not
remove the hard estimate or the small-prime losses.

The factorial-quotient congruence printed in the forwarded ChatGPT sketch
cannot replace this lemma. As printed, \(p=2,a=2,b=1\) gives

```math
\frac{(pa)!}{(pb)!}-\frac{a!}{b!}
=12-2=10,
```

which is not divisible by its claimed modulus \(8\).

Thus the gamma-function autocomplete reaches the same valid scaling lemma as
the termwise proof. It is a useful interpretation, not an independent
shortcut.

## 4. Completing the rescaling step

Set \(N'=np^{r-1}\) and consider

```math
F(pN',p\ell)-F(N',\ell).
```

If \(s<r-1\), the carry estimate supplies

```math
v_p(F(N',\ell))\ge2(r-1-s),
```

with one extra power at \(p=2\). The scaling quotient minus \(1\) supplies
\(3(s+1)-\epsilon_p\) further powers. Adding the two budgets gives at least
\(2r\) for every prime.

If \(s\ge r-1\), scaling alone suffices except potentially at
\(p=2,r=1\). In that final case the multinomial \(F(N',\ell)\) is even:
two equal positive components split off a central binomial coefficient
\(\binom{2b}{b}\). This restores the missing power.

Therefore

```math
F(pN',p\ell)\equiv F(N',\ell)\pmod {p^{2r}}
```

for every prime. Combined with the vanishing result, summing over \(\ell\)
proves the conjecture.

## 5. Closing the creative-microscoping route

Guo and Zudilin's creative-microscoping method is a genuine but different
route: it constructs specialized \(q\)-analogues and proves congruences
modulo powers of cyclotomic polynomials.

For the present sequence, the suggestion can be resolved completely without
leaving a further theorem as an open obligation. Define

```math
F_q(N,k)=M_q(k,k,k,k,N-k,N-k).
```

Its exact cyclotomic carry exponent is

```math
v_{\Phi_{p^i}(q)}(F_q(N,k))
=
2+\left\lfloor\frac{2(k\bmod p^i)}{p^i}\right\rfloor
```

at every active level. Therefore, if \(p^r\mid N\) and \(p\nmid k\),

```math
\prod_{i=1}^{r}\Phi_{p^i}(q)^2
\quad\text{divides}\quad F_q(N,k).
```

Evaluating at \(q=1\) gives \(p^{2r}\mid F_1(N,k)\). Thus creative
microscoping supplies a complete cyclotomic proof of the vanishing half of
the argument.

The project also proves the valid single-level square-cyclotomic lift

```math
\mathcal A_{4,2}(nN;q)
\equiv
\mathcal A_{4,2}(N;q^{n^2})
\pmod{\Phi_n(q)^2}.
```

See
[Q-calculus and cyclotomic supercongruences](related-results/QCalculusCyclotomicSupercongruences.md).

There is a tempting way to try to promote this lift to the whole theorem:

```math
\mathcal A_{4,2}(Np^r;q)
\stackrel{?}{\equiv}
\mathcal A_{4,2}(Np^{r-1};q^{p^2})
\pmod{
  \prod_{i=1}^{r}\Phi_{p^i}(q)^2
}.
\qquad\text{(CM)}
```

At \(q=1\), the proposed modulus becomes \(p^{2r}\), so (CM) would be
exactly the desired all-level creative-microscope proof.

However, (CM) is false. Take \(p=2\), \(r=2\), and \(N=1\). At a primitive
fourth root \(q=i\), exact Gaussian-multinomial evaluation gives

```math
\mathcal A_{4,2}(4;i)=26,
\qquad
\mathcal A_{4,2}(2;i^4)=\mathcal A_{4,2}(2;1)=3246.
```

Their difference is

```math
26-3246=-3220\ne0.
```

Hence the difference is not even divisible by \(\Phi_4(q)\), whereas the
proposed modulus contains \(\Phi_4(q)^2\). This is an exact counterexample,
not a failure of numerical precision.

The outcome is therefore definitive:

1. the cyclotomic filtration completely proves the vanishing of the
   \(p\nmid k\) stratum;
2. the square-cyclotomic theorem is a valid one-level \(q\)-refinement;
3. the natural all-level promotion that would independently imply
   \(p^{2r}\) is false; and
4. the \(p\mid k\) stratum must use the prime-sensitive multinomial scaling
   lemma from Sections 3--4.

Thus creative microscoping closes into the same termwise proof rather than
leaving a separate extension open. A differently normalized or corrected
\(q\)-analogue could be studied on its own, but no such conjecture is needed
or asserted here.

## 6. Completed route map

| Proposed idea | Useful content | Completion | Present status |
| --- | --- | --- | --- |
| Legendre digit counting | Kill \(p\nmid k\) terms | Replace the false digit identity by the exact floor/carry formula | Complete |
| Factorial scaling | Rescale \(k=p\ell\) | Use the prime-sensitive multinomial Kazandzidis lemma | Complete |
| Morita \(\Gamma_p\) | Express the scaling quotient through unit blocks | Exact identity above; required estimate is the same scaling lemma | Complete interpretation, not a second proof |
| Block decomposition | Separate surviving and vanishing strata | Implemented by the \(p\mid k\) split and valuation filtration | Complete |
| Exceptional primes | Account for losses at \(2,3\) | Explicit \(\epsilon_p\) plus the \(p=2,r=1\) parity endgame | Complete |
| Creative microscoping | Resolve the cyclotomic interpretation | Exact q-carry proof of vanishing; square one-level lift; exact counterexample to the natural multilevel promotion | Complete; no open claim is used |
| Generic Dwork shortcut | Explain the result through a Laurent polynomial | The displayed polynomial has three interior lattice points | Standard unique-interior shortcut does not apply |

## 7. Verification and review target

The exact A183068 checker verifies 105 congruence cases, including samples at
\(r=3\). The broader Landau-depth checker verifies 79,983 exact carry,
transfer, small-prime, and family identities.

Run:

```text
python verification/verify_a183068.py
python verification/related/verify_landau_supercongruence.py
```

These computations are regression evidence, not replacements for proof.

For a focused human review, the two load-bearing points are:

1. the prime-sensitive multinomial scaling lemma, especially its \(p=2\)
   sign qualification; and
2. the central-binomial parity repair at \(p=2,r=1\).

The complete linear argument is in [`PROOF.md`](PROOF.md). This Bala version
records how the forwarded suggestions autocomplete into that argument. It
also separates the valid square-cyclotomic theorem from the false natural
multilevel promotion, so none of the forwarded proof routes is left as an
unresolved obligation.

## References

1. G. S. Kazandzidis,
   [*Congruences on the binomial coefficients*](https://eudml.org/doc/238547).
2. R. Osburn, B. Sahu, and A. Straub,
   [*Supercongruences for sporadic sequences*](https://arxiv.org/abs/1312.2195).
3. E. Delaygue,
   [*Arithmetic properties of Apéry-like numbers*](https://arxiv.org/abs/1310.4131).
4. V. J. W. Guo and W. Zudilin,
   [*Dwork-type supercongruences through a creative q-microscope*](https://arxiv.org/abs/2001.02311).
5. A. Straub,
   [*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854).
