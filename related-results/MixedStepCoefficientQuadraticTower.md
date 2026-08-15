# A mixed-step coefficient tower and A246437

**Status:** complete elementary proof candidate; exact checks supplied;
literature priority not searched beyond the source record

This note proves the supercongruence conjectured on [OEIS A246437] and places
it in a three-parameter family. The essential observation is that its
algebraic-looking coefficient has a two-index binomial expansion whose
linear constraint synchronizes divisibility by (p).

## 1. The family

Let (u,v,c) be positive integers. For (N\ge1), define

\[
 A_{u,v,c}(N)
 =[x^{cN}]\left(\frac{1+x^u}{1-x^v}\right)^N.
 \tag{1}
\]

Expanding both factors gives the finite sum

\[
 A_{u,v,c}(N)
 =\sum_{\substack{0\le j\le N,\ k\ge0\\uj+vk=cN}}
 \binom Nj\binom{N+k-1}{k}.
 \tag{2}
\]

### Theorem

Let (p) be an odd prime with (p\nmid uv). For all positive integers
(n,r),

\[
 A_{u,v,c}(np^r)
 \equiv A_{u,v,c}(np^{r-1})
 \pmod {p^{2r}}.
 \tag{3}
\]

The parameter (c) is unrestricted; in particular, primes dividing (c)
are allowed.

## 2. Divisibility synchronization

Set

\[
 N=np^r,qquad M=N/p.
\]

Every index pair in (2) satisfies

\[
 uj+vk=cN.
 \tag{4}
\]

Because (u) and (v) are units modulo (p), equation (4) has the useful
dichotomy

\[
 p\mid j\quad\Longleftrightarrow\quad p\mid k.
 \tag{5}
\]

Thus a pair is either wholly scalable or both of its coordinates are units.

## 3. The unscaled terms

For (p\nmid j),

\[
 v_p\binom Nj\ge r
\]

from (inom Nj=(N/j)inom{N-1}{j-1}). Similarly, if (p\nmid k),

\[
 \binom{N+k-1}{k}
 =\frac Nk\binom{N+k-1}{k-1}
\]

has valuation at least (r). By (5), every unscaled summand in (2) is
therefore divisible by (p^{2r}).

## 4. Exact reduction of the shifted factor

Write a scaled pair as ((j,k)=(pj',pk')). The first factor is ordinary:

\[
 \frac{\binom{pM}{pj'}}{\binom M{j'}}.
\]

The shifted negative-binomial factor has exactly the same kind of quotient.
Indeed, with (D=M+k'),

\[
 \frac{\binom{pM+pk'-1}{pk'}}{\binom{M+k'-1}{k'}}
 =
 \frac{\binom{pD}{pk'}}{\binom D{k'}}.
 \tag{6}
\]

To see (6), use

\[
 \binom{pD-1}{pk'}=\frac{M}{D}\binom{pD}{pk'},
 \qquad
 \binom{D-1}{k'}=\frac{M}{D}\binom D{k'}.
\]

Thus both factors are governed by the ordinary adjacent
Ljunggren--Jacobsthal--Kazandzidis estimate.

## 5. Valuation budget for the scaled terms

Let (epsilon_3=1) and (epsilon_p=0) for (p\ge5). Suppose first that

\[
 s=\min(v_p(j'),v_p(k'))<r-1.
\]

Equation

\[
 uj'+vk'=cM
\]

forces (v_p(j')=v_p(k')=s): unequal valuations could not cancel to a
multiple of (p^{r-1}). The two lower-level binomial factors in (2) then
each have valuation at least (r-1-s). Their product has valuation at least

\[
 2(r-1-s).
 \tag{7}
\]

The two adjacent quotients in Section 4 are each (1) modulo
(p^{3(s+1)-\epsilon_p}). Their product has the same property, so the
difference between the high- and low-level summands has valuation at least

\[
 2(r-1-s)+3(s+1)-\epsilon_p
 =2r+s+1-\epsilon_p
 \ge2r.
 \tag{8}
\]

If both (j') and (k') are divisible by (p^{r-1}), the adjacent
quotients are (1) modulo (p^{3r-\epsilon_p}), which is again at least
(p^{2r}). Zero-coordinate boundary terms lie in this second case and
transfer exactly or with the same bound.

The scalable pairs in (2) correspond bijectively to the pairs at level
(M), after division by (p). Combining their termwise transfer with the
vanishing of every unscaled term proves (3). (square)

## 6. A246437

The source record gives

\[
 a(N)=[x^N]\left(\frac{1-x+x^2}{1-x}\right)^N.
\]

The cyclotomic factorization

\[
 1-x+x^2=\frac{1+x^3}{1+x}
\]

turns this into

\[
 a(N)=[x^N]\left(\frac{1+x^3}{1-x^2}\right)^N
 =A_{3,2,1}(N).
 \tag{9}
\]

Every prime (p\ge5) is coprime to (uv=6). The theorem therefore gives

\[
 a(np^r)\equiv a(np^{r-1})\pmod {p^{2r}},
\]

which is exactly the supercongruence on A246437.

## 7. Verification and scope

The exact checker
[`verify_mixed_step_coefficient_tower.py`](../verification/related/verify_mixed_step_coefficient_tower.py)
performs:

- 16 direct matches to the initial A246437 values; and
- 782 adjacent-level checks across five ((u,v,c))-families, four primes,
  and as many as three levels.

All checks pass, with 511 witnesses where the exponent (2r) is exact.

The proof is elementary and self-contained modulo the classical adjacent
binomial scaling theorem. No claim of literature priority is made. The
restriction (p\nmid uv) records the actual proof boundary; ramified step
sizes require a separate analysis.

[OEIS A246437]: https://oeis.org/A246437
