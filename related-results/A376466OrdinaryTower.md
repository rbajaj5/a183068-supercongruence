# The ordinary A376466 cubic tower

**Status:** complete proof of the ordinary cubic tower for every prime
`p>=5`; the proposed shifted companion is false

Let

```math
T(m,k)=\sum_{j=0}^m
 \binom mj\binom{m+j}{j}\binom kj
```

and define A376466 by

```math
B(N)=\sum_{k=0}^N(-1)^{N+k}
 \binom Nk\binom{N+k}{k}^2T(N-1,k).
\tag{1}
```

The companion reduction proves that `T(N-1,k)` is a homogeneous
negative-coordinate Apéry coefficient.  That settles its scaled row, but a
single unit summand in (1) can have only one factor of `p`.  The point of
this note is that the missing two powers are aggregate reciprocal moments.

## Theorem

For every prime `p>=5` and positive integers `n,r`,

```math
\boxed{B(np^r)\equiv B(np^{r-1})\pmod {p^{3r}}.}
\tag{2}
```

The shifted conjecture on the OEIS record is different and is false; the
exact counterexample is retained in
[the companion reduction](A376AperyCompanionReduction.md#theorem-4-the-proposed-shifted-a376466-tower-is-false).

## 1. Two kernels

For `1<=k<=N`, extract the rational factor from the first binomial:

```math
\binom Nk=\frac Nk\binom{N-1}{k-1}.
```

Put

```math
K_N(k)=(-1)^{N+k}\binom{N-1}{k-1}
 \binom{N+k}{k}^2T(N-1,k),
\tag{3}
```

so that the `k`-th summand of (1) is `N K_N(k)/k`.  The descended kernel is

```math
D_M(q)=(-1)^{M+q-1}\binom{M-1}{q}
 \binom{M+q}{q}^2T(M-1,q)
\tag{4}
```

for `0<=q<M`, and zero otherwise.

We need two elementary lemmas.  They are stated at the precision used in
the proof; keeping the full product quotients gives slightly stronger
versions.

### Lemma 1 (two-moment unit expansion)

Let `N=np^r`, `M=N/p`, and let `p` not divide `k`.  With `q=floor(k/p)`,

```math
\boxed{
K_N(k)\equiv D_M(q)\left(1+\frac Nk\right)
\pmod {p^{2r}}.}
\tag{5}
```

### Proof

Write

```math
A_N(k)=(-1)^{N+k}\binom{N-1}{k-1}\binom{N+k}{k}^2.
```

Separating factors whose indices are divisible by `p` from the three
factorial products gives, with

```math
H_p(k)=\sum_{\substack{1\le h\le k\\p\nmid h}}\frac1h,
```

the first-order expansion

```math
A_N(k)\equiv
(-1)^{M+q-1}\binom{M-1}{q}\binom{M+q}{q}^2
\left(1+\frac Nk+NH_p(k)\right)
\pmod {p^{2r}}.
\tag{6}
```

Indeed every unit factor is of the form `1+cN/h`; products of two
nonconstant terms are divisible by `N^2`, while the multiples of `p`
give exactly the three displayed lower binomials.  The coefficients of the
linear logarithm are `+1` from `binom(N-1,k-1)` and `+2` from the two
copies of `binom(N+k,k)`; after the common multiples are removed they
combine to `N/k+NH_p(k)`.

For the shifted row, use its negative-coordinate form

```math
T(N-1,k)=\mathcal B(-N,k,-N).
```

The same separation of multiples of `p`, now in the three factors defining
`mathcal B`, gives

```math
T(N-1,k)\equiv T(M-1,q)(1-NH_p(k))
\pmod {p^{2r}}.
\tag{7}
```

The two linear harmonic terms in (6)--(7) cancel.  Their product is a
multiple of `N^2`; multiplication leaves (5). QED

The proof uses only finite products.  Thus (6)--(7) remain valid when a
lower binomial vanishes: perform the cancellation before reducing modulo
`p^(2r)`, or use the integer-binomial continuation in the displayed
negative-coordinate row.

### Lemma 2 (quadratic Cartier descent)

Let `R=v_p(N)>=1` and `M=N/p`. For every nonnegative `j`,

```math
\boxed{D_N(j)\equiv D_M(\lfloor j/p\rfloor)\pmod {p^{2R}}.}
\tag{8}
```

This is slightly stronger than the precision needed in the theorem when
`p` also divides `n`.

### Unit digits are already proved

There is an exact relation between the two kernels:

```math
K_N(j)=\frac{j}{j-N}D_N(j),
\qquad
D_N(j)=\left(1-\frac Nj\right)K_N(j).
\tag{8a}
```

If `p` does not divide `j`, write `N=up^R` with `p` not dividing `u` and
apply Lemma 1 with `r=R`. Multiply (5) by `1-N/j`. Since this factor is a
`p`-adic integer and

```math
\left(1+\frac Nj\right)\left(1-\frac Nj\right)
=1-\frac{N^2}{j^2}\equiv1\pmod {p^{2R}},
```

we obtain (8) immediately.  Thus no residue-by-residue induction is needed:
the two-moment expansion already proves every unit digit.

It remains to prove the scaled digits

```math
\boxed{D_N(pq)\equiv D_M(q)\pmod {p^{2R}}}.
\tag{8b}
```

The congruence will follow from an exact recurrence and a simultaneous
horizontal estimate.

### The shifted-row recurrence

Put `W_N(j)=T(N-1,j)`. Its ordinary generating function is

```math
\sum_{j\ge0}W_N(j)x^j
=\frac1{1-x}P_{N-1}\left(\frac{1+x}{1-x}\right),
\tag{8c}
```

where `P_m` is the Legendre polynomial. Indeed,

```math
\sum_{j\ge0}\binom j\ell x^j=\frac{x^\ell}{(1-x)^{\ell+1}}
```

and

```math
P_{N-1}(1+2y)=
\sum_{\ell=0}^{N-1}\binom{N-1}\ell
 \binom{N-1+\ell}\ell y^\ell.
```

Substituting (8c) in the Legendre differential equation and comparing the
coefficient of `x^j` gives

```math
(j+1)^2W_N(j+1)
-\big((j+1)^2+j^2+N(N-1)\big)W_N(j)
+j^2W_N(j-1)=0.
\tag{8d}
```

Write

```math
O_N(j)=(-1)^{N+j-1}\binom{N-1}j\binom{N+j}j^2,
```

so that `D_N(j)=O_N(j)W_N(j)`. The exact quotients

```math
\frac{O_N(j+1)}{O_N(j)}
=-\frac{(N-1-j)(N+j+1)^2}{(j+1)^3},
\qquad
\frac{O_N(j)}{O_N(j-1)}
=-\frac{(N-j)(N+j)^2}{j^3}
```

turn (8d), for `1<=j<=N-2`, into

```math
C_+D_N(j+1)+C_0D_N(j)+C_-D_N(j-1)=0,
\tag{8e}
```

where, with `A=(j+1)^2+j^2+N(N-1)`,

```math
C_+=j(j+1)^5,
```

```math
C_0=Aj(N-1-j)(N+j+1)^2,
```

and

```math
C_-=(N-j)(N+j)^2(N-1-j)(N+j+1)^2.
```

A direct expansion, also checked coefficientwise by the exact checker,
factors the constant solution's defect as

```math
C_++C_0+C_-=-N^3P_N(j),
\tag{8f}
```

with

```math
P_N(j)=-N^3-3N^2j-N^2+Nj+N
       +3j^3+7j^2+5j+1.
```

### Simultaneous induction

Together with (8), prove for every `R>=1` the horizontal estimate

```math
v_p\big(D_N(j)-D_N(j-1)\big)
\ge2\max\{R-v_p(j),0\}
\quad(1\le j<N).
\tag{8g}
```

Assume first that `j=pq`, put `t=v_p(j)`, and suppose `t>=R`. The identity

```math
\frac{\binom{N-1}{pq}}{\binom{M-1}q}
=\frac{\binom N{pq}}{\binom Mq}
```

reduces the first outer factor to an ordinary homogeneous binomial quotient.
The second outer factor is another such quotient, and

```math
T(N-1,pq)=\mathcal B(-N,pq,-N)
```

is the homogeneous negative-coordinate row. The
Jacobsthal--Kazandzidis estimate for the two binomials and Straub's
negative-coordinate estimate for the row each give precision
`p^(3 min(R,t))=p^(3R)`. The signs agree because `p` is odd. Thus (8b)
holds, with a stronger modulus, whenever `t>=R`.

Now suppose `t<R`. Here `A`, `N-1-j`, `N+j+1`, and `P_N(j)` are all
`p`-adic units: after reducing `N` and `j` modulo `p`, both `A` and
`P_N(j)` are `1`. Consequently

```math
v_p\left(\frac{C_-}{C_0}\right)=2t,
\qquad
v_p\left(\frac{C_++C_0+C_-}{C_0}\right)=3R-t.
\tag{8h}
```

Rearranging (8e) gives the cancellation in its useful form:

```math
D_N(j)-D_N(j+1)
=-\frac{C_-}{C_0}\big(D_N(j-1)-D_N(j+1)\big)
-\frac{C_++C_0+C_-}{C_0}D_N(j+1).
\tag{8i}
```

Both neighbors `j-1,j+1` are unit digits. Their already proved cases of
(8), followed by (8g) at level `R-1`, show that

```math
v_p\big(D_N(j-1)-D_N(j+1)\big)\ge2(R-t).
```

The first term on the right of (8i) therefore has valuation at least
`2t+2(R-t)=2R`; the second has valuation `3R-t>2R`. Hence
`D_N(j)=D_N(j+1) (mod p^(2R))`, and the unit case at `j+1` gives
`D_N(j)=D_M(q) (mod p^(2R))`. This proves every remaining scaled digit.

For `R=1`, the scaled digits all lie in the already treated range `t>=R`,
so the induction starts. Once (8) is known at level `R`, (8g) follows at
that level: if `p` does not divide `j`, the two floors in (8) agree; if
`p` divides `j`, descend both terms and apply (8g) at level `R-1` to
`q=j/p`. Finally `D_N(0)=D_M(0)` because `p` is odd, and both sides of
(8) vanish when `j>=N`. This completes the simultaneous induction and
proves Lemma 2. QED

## 2. Reciprocal block sums

For `s>=1`, `L>=0`, and `a=1,2`, put

```math
R_{a,s}(L)=
\sum_{\substack{Lp^s<k<(L+1)p^s\\p\nmid k}}\frac1{k^a}.
```

The complete reduced-residue calculation gives

```math
v_p(R_{1,s}(L))\ge2s,
\qquad
v_p(R_{2,s}(L))\ge s.
\tag{9}
```

For the second estimate, reduce modulo `p^s` and use that inversion
permutes the units, so the sum is congruent to the sum of their squares.
For the first, pair `u` with `p^s-u`; after division by `p^s` the residual
reciprocal-square sum vanishes once more.  Translation by `Lp^s` changes
only terms beyond the displayed precision.

Straub's weighted block induction says that if `C_t(j)` satisfies

```math
C_t(j)\equiv C_{t-1}(\lfloor j/p\rfloor)\pmod {p^{2t}},
\tag{10}
```

then the reciprocal-square estimate in (9), grouping a `p^t`-block into
`p` subblocks recursively, gives

```math
\sum_{\substack{Lp^t<k<(L+1)p^t\\p\nmid k}}
 \frac{C_{t-1}(\lfloor k/p\rfloor)}k\equiv0\pmod {p^{2t}},
\tag{11}
```

The reciprocal-first-moment analogue is

```math
\sum_{\substack{Lp^t<k<(L+1)p^t\\p\nmid k}}
 \frac{C_{t-1}(\lfloor k/p\rfloor)}{k^2}\equiv0\pmod {p^t}.
\tag{12}
```

For completeness, (11) needs the strengthened descent (8), not merely
ordinary mod-`p^t` descent.  Replace the weight on the first digit by its
parent using (8); the error is a multiple of `p^(2t)`.  The unweighted
reciprocal sum over each complete child block has valuation `2`, and
iteration through `t` digits gives `2t`.  Formula (12) is exactly Straub's
induction with `a_k=1/k^2` on the unit indices and zero otherwise.

## 3. The unit shell

Take `N=np^r` and `M=N/p`.  Lemma 1 gives

```math
\sum_{p\nmid k}\frac NkK_N(k)
\equiv
N\sum_{p\nmid k}\frac{D_M(\lfloor k/p\rfloor)}k
+N^2\sum_{p\nmid k}\frac{D_M(\lfloor k/p\rfloor)}{k^2}
\pmod {p^{3r}}.
\tag{13}
```

The range `1<=k<N` is a union of `n` complete blocks of length `p^r`.
Apply (11)--(12) with the descent (8).  The first sum in (13) is divisible
by `p^(2r)` and the second by `p^r`; the prefactors `N` and `N^2` therefore
make both terms divisible by `p^(3r)`.  Hence the entire unit shell
vanishes modulo `p^(3r)`.

## 4. The scaled shell

For `k=pq`, compare the corresponding summands at `N` and `M`.  The outer
triple is a product of adjacent binomial-scaling quotients, and the row is
the homogeneous coefficient `mathcal B(-N,pq,-N)`.  The
Jacobsthal--Kazandzidis valuation, together with the valuation of the lower
summand when `q` lies below the current scale, gives

```math
\frac N{pq}K_N(pq)\equiv\frac MqK_M(q)
\pmod {p^{3r}}.
\tag{14}
```

This is the composite scaled transfer already checked factor by factor in
the companion reduction: if `s=v_p(q)<r-1`, the lower summand supplies the
missing `2(r-1-s)` powers, while the scaling quotient supplies
`r+2s+2`; if `s>=r-1`, the scaling quotient alone reaches `3r`.
The endpoints are equal or covered by the same integer identity.

Summing (14) and adding the unit-shell result proves (2). QED

## 5. Verification and source boundary

Run

```text
python verification/related/verify_a376466_ordinary_tower.py
```

The checker tests (5)--(12), the exact unit-digit deduction (8a), the row
and kernel recurrences (8d)--(8f), the simultaneous-induction valuations
(8g)--(8i), the scaled boundary (8b), both shell congruences, and the full tower.
It includes primes through 19 at the first level, the second level for
`p=5,7`, and third-level scaled-boundary cases at `p=5`; 37 sampled tower
instances attain the claimed exponent exactly.

The sequence and conjecture are Peter Bala's OEIS contribution.  The
negative-coordinate row and scaled-shell reduction are proved in the
companion note.  The ingredients used here are finite binomial products,
the classical Jacobsthal--Kazandzidis congruence, and the weighted block
induction in Armin Straub's
[*Multivariate Apéry numbers and supercongruences of rational functions*](https://arxiv.org/abs/1401.0854).
The two-moment decomposition (5) and the recurrence proof of the scaled
boundary are the exact reductions recorded here. The checker is a
transcription and boundary audit, not a substitute for the proof. No
literature-priority claim is made.
