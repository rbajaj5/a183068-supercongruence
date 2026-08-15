# The two A005725 supercongruences

**Status:** complete elementary proof candidate; exact checks supplied;
literature priority not searched beyond the source record

The [OEIS A005725] page records two conjectures. This note proves both:

1. the adjacent quadratic tower for the quadrinomial coefficient at every
   odd prime; and
2. the separate prime-level cubic congruence for the coefficient built from
   (F(x)/F(-x)).

The two arguments are related only by their source page. The first is a
carry-and-scaling proof. The second collapses to a one-variable rational
function and uses Wolstenholme's theorem.

## 1. Statement for the quadrinomial coefficient

Put

\[
 A(N)=[x^N](1+x+x^2+x^3)^N.
\]

Because

\[
 1+x+x^2+x^3=(1+x)(1+x^2),
\]

we have the finite sum

\[
 A(N)=\sum_{k=0}^{\lfloor N/2\rfloor}
 \binom Nk\binom N{2k}.
 \tag{1}
\]

### Theorem 1

For every odd prime (p) and all positive integers (n,r),

\[
 A(np^r)\equiv A(np^{r-1})\pmod {p^{2r}}.
 \tag{2}
\]

This proves the first supercongruence conjectured on A005725, including its
stated (p=3) boundary.

## 2. The scaling input

We use the standard adjacent Ljunggren--Jacobsthal--Kazandzidis estimate in
the following form. Let (p) be odd, let (a,b) be nonnegative, and suppose
every positive member of (b,a-b) is divisible by (p^s). Then

\[
 \binom{pa}{pb}
 =\binom ab\left(1+p^{,3(s+1)-\epsilon_p}u\right),
 \qquad u\in\mathbb Z_p,
 \tag{3}
\]

where (epsilon_3=1) and (epsilon_p=0) for (p\ge5). A zero lower
entry gives the exact quotient (1). This is the binomial specialization of
the scaling lemma used in the [A183068 proof].

## 3. Proof of Theorem 1

Set

\[
 N=np^r,qquad M=N/p=np^{r-1},qquad
 G_N(k)=\binom Nk\binom N{2k}.
\]

Split (1) according to whether (pmid k).

### 3.1 The unscaled stratum

For (0<j<N),

\[
 \binom Nj=\frac Nj\binom{N-1}{j-1},
\]

so

\[
 v_p\binom Nj\ge r-v_p(j).
 \tag{4}
\]

If (p\nmid k), then (p\nmid2k) because (p) is odd. Equation (4)
therefore gives

\[
 v_p(G_N(k))\ge2r.
 \tag{5}
\]

Every term missed by the rescaling is already zero modulo (p^{2r}).

### 3.2 The scaled stratum

Write (k=p\ell). Multiples of (p) in the range
(0\le k\le\lfloor N/2\rfloor) correspond exactly to
(0\le\ell\le\lfloor M/2\rfloor).

The term (ell=0) transfers exactly. Suppose first that

\[
 s=v_p(\ell)<r-1.
\]

Then (M-\ell) and (M-2\ell) also have valuation (s). Applying (3) to
both binomial factors gives

\[
 G_N(p\ell)
 =G_M(\ell)\left(1+p^{,3(s+1)-\epsilon_p}u\right)
 \tag{6}
\]

for some (u\in\mathbb Z_p). Meanwhile (4), now at level (M), gives

\[
 v_p(G_M(\ell))\ge2(r-1-s).
\]

Consequently,

\[
\begin{aligned}
v_p\bigl(G_N(p\ell)-G_M(\ell)\bigr)
&\ge2(r-1-s)+3(s+1)-\epsilon_p\\
&=2r+s+1-\epsilon_p\\
&\ge2r.
\end{aligned}
\tag{7}
\]

If (v_p(\ell)\ge r-1), every positive lower component in both binomial
coefficients is divisible by (p^{r-1}). Equation (3) instead gives (6)
with modulus (p^{3r-\epsilon_p}). Since

\[
3r-\epsilon_p\ge2r
\]

for every odd prime and (r\ge1), the same conclusion follows. This case
also covers the possible endpoint (2\ell=M).

Thus every scaled term agrees with its preceding-level term modulo
(p^{2r}), while (5) removes every unscaled term. Summing proves (2). (square)

## 4. The separate ratio coefficient

Let

\[
 F(x)=1+x+x^2+x^3
\]

and define

\[
 B(N)=[x^N]\left(\frac{F(x)}{F(-x)}\right)^N.
\]

The apparent quadrinomial input cancels:

\[
 \frac{F(x)}{F(-x)}
 =\frac{(1+x)(1+x^2)}{(1-x)(1+x^2)}
 =\frac{1+x}{1-x}.
 \tag{8}
\]

Hence

\[
 B(N)=\sum_{k=0}^{N}
 \binom Nk\binom{2N-k-1}{N-k}.
 \tag{9}
\]

### Theorem 2

For every prime (p\ge5),

\[
 B(p)\equiv2\pmod {p^3}.
 \tag{10}
\]

### Proof

The endpoint (k=p) in (9) equals (1). The endpoint (k=0) is

\[
 \binom{2p-1}{p}=\binom{2p-1}{p-1}\equiv1\pmod {p^3}
 \tag{11}
\]

by Wolstenholme's theorem.

For (1\le k\le p-1), the first factor satisfies

\[
 \binom pk\equiv(-1)^{k-1}\frac pk\pmod {p^2}.
 \tag{12}
\]

For the second factor, isolate its unique numerator multiple of (p):

\[
 \binom{2p-k-1}{p-k}
 =\binom{2p-k-1}{p-1}
 =\frac pk
 \prod_{\substack{1\le j\le p-1\\j\ne k}}
 \frac{p-k+j}{j}.
\]

Modulo (p), the numerator product runs through every nonzero residue except
(-k), whereas the denominator product runs through every nonzero residue
except (k). Wilson's theorem therefore gives

\[
 \binom{2p-k-1}{p-k}\equiv-\frac pk\pmod {p^2}.
 \tag{13}
\]

Multiplying (12) and (13), the interior of (9) is

\[
 p^2\sum_{k=1}^{p-1}\frac{(-1)^k}{k^2}\pmod {p^3}.
 \tag{14}
\]

The sum in (14) is zero modulo (p): the terms indexed by (k) and (p-k)
cancel because (p) is odd. Combining this cancellation with the two
endpoints (11) proves (10). (square)

## 5. Exact verification and scope

The checker
[`verify_quadrinomial_coefficient_tower.py`](../verification/related/verify_quadrinomial_coefficient_tower.py)
uses Python integers only. It performs:

- 433 adjacent-level tests of (2), over
  (p\in\{3,5,7,11,13,17,19\}), (1\le r\le3), (1\le n\le40), and
  (np^r\le900); and
- 12 tests of (10), for primes (5\le p\le43).

All checks pass. The exact displayed exponent occurs in both families, so
neither modulus can be uniformly increased on the tested ranges.

This note proves exactly the two conjectures printed on A005725. It does not
claim a literature-priority result: the proof uses classical binomial
scaling and Wolstenholme's theorem, and only the source record has been
checked for provenance.

[OEIS A005725]: https://oeis.org/A005725
[A183068 proof]: ../PROOF.md#3-multinomial-scaling
