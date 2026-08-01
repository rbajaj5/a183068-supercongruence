# Symmetric-box plane partitions: a nonlinear all-prime tower

**Status:** complete elementary proof candidate; independent review and
literature-priority work remain

## 1. The theorem

For integers \(c\geq 1\) and \(N\geq 0\), let

```math
B_c(N)=\prod_{i,j=1}^{N}\frac{cN+i+j-1}{i+j-1}.
```

By MacMahon's formula, \(B_c(N)\) is the number of plane partitions in an
\(N\times N\times cN\) box.  Equivalently, if

```math
H(M)=\prod_{j=1}^{M-1}j!,
```

then

```math
B_c(N)=
\frac{H(N)^2H(cN)H((c+2)N)}{H(2N)H((c+1)N)^2}.
```

### Theorem

For every prime \(p\), every \(c,n,r\geq1\),

```math
B_c(np^r)\equiv B_c(np^{r-1})^p\pmod {p^{4r}}.
```

The case \(c=1\) proves the nonlinear tower conjectured on
[OEIS A008793](https://oeis.org/A008793).  The case \(c=2\) proves
Conjecture 3 on [OEIS A352656](https://oeis.org/A352656), and \(c=3\)
proves Conjecture 2 on [OEIS A352657](https://oeis.org/A352657). Thus the
three named records are members of one infinite theorem rather than
isolated coincidences.

## 2. Exact complementary-factor splitting

The multiplicity of \(s=i+j-1\) is \(s\) for \(1\leq s\leq N\) and
\(2N-s\) for \(N<s<2N\).  Pairing \(s\) with \(2N-s\) gives

```math
B_c(N)=(c+1)^N P_c(N),
```

where

```math
P_c(N)=\prod_{s=1}^{N-1}
\left(1+\frac{c(c+2)N^2}{s(2N-s)}\right)^s.
```

Indeed, the paired factor is exactly

```math
\frac{cN+s}{s}\frac{(c+2)N-s}{2N-s}
=1+\frac{c(c+2)N^2}{s(2N-s)}.
```

Replacing \(N\) by \(pN\), the factors with \(p\mid s\) reproduce
\(P_c(N)^p\) exactly.  The central factors also agree exactly.  Hence

```math
B_c(pN)=B_c(N)^pU_{p,c}(N),
```

with

```math
U_{p,c}(N)=
\prod_{\substack{1\leq s<pN\\p\nmid s}}
\left(1+\frac{c(c+2)p^2N^2}{s(2pN-s)}\right)^s.
```

It remains to bound this residual unit product.

## 3. The odd-prime interval lemma

### Lemma 1

Let \(p\) be odd, \(q=p^r\), and \(n,r\geq1\).  Then

```math
\sum_{\substack{nq<t<2nq\\p\nmid t}}\frac1t
\equiv0\pmod {p^{2r}}.
```

### Proof

The involution \(t\mapsto3nq-t\) preserves the interval and its units.  It
has no unit fixed point.  For a set \(J\) containing one member from each
pair,

```math
\sum_{\substack{nq<t<2nq\\p\nmid t}}\frac1t
=3nq\sum_{t\in J}\frac1{t(3nq-t)}.
```

Modulo \(q\), the last sum is minus one half of the reciprocal-square sum
over the full interval.  Each nonzero residue modulo \(q\) occurs \(n\)
times there, while inversion permutes the units.  Therefore it is enough to
use

```math
\sum_{\substack{1\leq u<q\\p\nmid u}}u^2
=\frac{q(p-1)(2p(q/p)^2-1)}6.
```

This has \(p\)-adic valuation \(r\) for \(p\geq5\), and \(r-1\) for
\(p=3\).  The prefactor \(3nq\) has valuation at least \(r\), with the
missing power restored exactly when \(p=3\).  The claimed \(2r\) follows.
\(\square\)

## 4. Odd primes

Put \(N=np^{r-1}\) and

```math
x_s=\frac{c(c+2)p^2N^2}{s(2pN-s)}.
```

For \(p\nmid s\), \(v_p(x_s)\geq2r\).  The linear term in
\(\log U_{p,c}(N)\) is

```math
c(c+2)p^2N^2
\sum_{\substack{1\leq s<pN\\p\nmid s}}\frac1{2pN-s}.
```

After writing \(q=p^r\), the denominators are precisely the units strictly
between \(nq\) and \(2nq\).  Lemma 1 gives another \(2r\) powers, so the
linear term is divisible by \(p^{4r}\).

Every logarithmic term of degree \(k\geq2\) has valuation at least

```math
2rk-v_p(k)\geq4r.
```

Thus \(U_{p,c}(N)\equiv1\pmod {p^{4r}}\) for every odd prime \(p\).

## 5. The binary prime

Write \(N=2^tm\), with \(m\) odd.  We use the elementary odd-block bound

```math
\sum_{a=0}^{2^t-1}\frac1{d2^{t+1}+2a+1}
\equiv0\pmod {2^{2t}}
```

for every integer \(d\).  It follows by pairing complementary odd residues;
inversion reduces the remaining factor to the sum of their squares.

The odd denominators \(4N-s\), for \(1\leq s<2N\), split into \(m\) such
blocks.  Consequently their reciprocal sum has valuation at least \(2t\).

If \(c\) is even, then \(v_2(c(c+2))\geq3\).  Each logarithmic variable in
\(U_{2,c}(N)\) has valuation at least \(2t+5\).  The linear term therefore
has valuation at least \(4t+5\), and every higher term has still larger
valuation.  Since \(t\geq r-1\), this already proves
\(U_{2,c}(N)\equiv1\pmod {2^{4r}}\).

Suppose instead that \(c\) is odd.  The same calculation without the three
bonus powers gives

```math
U_{2,c}(N)\equiv1\pmod {2^{4t+2}}.
```

Two powers remain, and they come from \(B_c(N)^2\).

### Lemma 2

If \(c\) is odd and \(N\geq1\), then \(B_c(N)\) is even.

### Proof

For odd \(N\), complementation is a fixed-point-free involution on plane
partitions in the box: a fixed point would have volume \(cN^3/2\), impossible
because \(cN^3\) is odd.

For every \(N\), Legendre's formula and the balanced hyperfactorial ratio
give

```math
v_2(B_c(2N))=2v_2(B_c(N)).
```

Indeed, applying
\(v_2(H(2M))=2v_2(H(M))+M(M-1)\) to the six hyperfactorials makes all
quadratic correction terms cancel.  Removing powers of two from \(N\)
therefore reduces to the odd case. \(\square\)

Finally,

```math
B_c(2N)-B_c(N)^2=B_c(N)^2\bigl(U_{2,c}(N)-1\bigr).
```

Lemma 2 supplies the two missing powers, giving valuation at least
\(4t+4\geq4r\).  This proves the theorem at \(p=2\).

## 6. Verification and source boundary

The exact checker verifies:

1. the A008793, A352656, and A352657 initial values;
2. the paired product and exact residual decomposition;
3. both reciprocal-sum lemmas;
4. binary evenness and the valuation-doubling identity; and
5. the full theorem for several values of \(c,p,n,r\).

Run:

```text
python verification/related/verify_symmetric_box_plane_partitions.py
```

MacMahon's product and both named conjectures are stated on the linked OEIS
pages.  This note supplies one elementary proof for the complete symmetric
family.  A targeted priority search is still required; no claim of
literature priority or peer review is made.
