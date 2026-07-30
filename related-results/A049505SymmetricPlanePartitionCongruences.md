# The three A049505 congruences

**Status:** complete elementary proof of all three displayed OEIS
congruences, through one stronger prime-power evaluation

## 1. Statement

The [OEIS A049505](https://oeis.org/A049505) sequence is

```math
a(N)=\prod_{1\le i\le j\le N}
\frac{N+i+j-1}{i+j-1}.
\tag{1}
```

It counts symmetric plane partitions in an $N$-cube.  The source page
conjectures, for odd primes $p$,

```math
a(p)\equiv 2^{(p+1)/2}\pmod {p^3},
\tag{2}
```

```math
a(p^2)\equiv
(-1)^{(p^2-1)/8}a(p)^{p^2-p+1}
\pmod {p^3},
\tag{3}
```

and, for every prime $p$,

```math
a(p^3)\equiv
a(p^2)^{(p^3-p^2+2)/2}
\pmod {p^3}.
\tag{4}
```

We prove all three from one formula.

## 2. Exact product pairing

For $1\le s\le 2N-1$, let $\lambda_N(s)$ be the number of pairs
$1\le i\le j\le N$ with $i+j-1=s$.  Direct counting gives

```math
\lambda_N(s)=\lceil s/2\rceil
\qquad(1\le s\le N),
\tag{5a}
```

and

```math
\lambda_N(s)=N-\lfloor s/2\rfloor
\qquad(N<s\le2N-1).
\tag{5b}
```

In particular,

```math
\lambda_N(2N-s)=\lambda_N(s)
\qquad(1\le s<N).
\tag{6}
```

Assume that $N$ is odd.  The central factor $s=N$ is $2$, with
multiplicity $(N+1)/2$.  Pairing $s$ with $2N-s$ elsewhere gives the exact
identity

```math
a(N)=
2^{(N+1)/2}
\prod_{s=1}^{N-1}
\left(
1+\frac{3N^2}{s(2N-s)}
\right)^{\lceil s/2\rceil}.
\tag{7}
```

Indeed,

```math
\frac{N+s}{s}\,
\frac{3N-s}{2N-s}
=
1+\frac{3N^2}{s(2N-s)}.
\tag{8}
```

This pairing is the whole proof mechanism.

## 3. The stronger master congruence

### Theorem 1

For every odd prime $p$ and every $r\ge1$,

```math
a(p^r)\equiv 2^{(p^r+1)/2}\pmod {p^3}.
\tag{9}
```

### Proof

Put $N=p^r$.  Since $s<N$,

```math
v_p(2N-s)=v_p(s).
\tag{10}
```

The correction in the $s$-th factor of (7) therefore has valuation

```math
v_p(3)+2r-2v_p(s).
\tag{11}
```

When $p=3$, this is always at least $3$, so (9) follows immediately.
Assume henceforth that $p\ge5$.

If $v_p(s)\le r-2$, (11) is at least $4$.  Modulo $p^3$, only

```math
s=p^{r-1}t,\qquad 1\le t\le p-1,
\tag{12}
```

can contribute.  For these terms,

```math
1+\frac{3N^2}{s(2N-s)}
=
1+\frac{3p^2}{t(2p-t)}.
\tag{13}
```

Cross-products of two corrections already vanish modulo $p^3$.  Thus it
is enough to calculate the exponent-weighted reciprocal-square sum modulo
$p$.

First suppose $r=1$.  We need

```math
\sum_{t=1}^{p-1}\frac{\lceil t/2\rceil}{t^2}\equiv0\pmod p.
\tag{14}
```

Write $h=(p-1)/2$.  Splitting into odd and even indices,

```math
\sum_{t=1}^{p-1}\frac{\lceil t/2\rceil}{t^2}
=
\sum_{j=1}^{h}
\left(
\frac{j}{(2j-1)^2}+\frac1{4j}
\right).
\tag{15}
```

Now

```math
\sum_{u=1}^{p-1}\frac1u\equiv0,
\qquad
\sum_{u=1}^{p-1}\frac1{u^2}\equiv0
\pmod p.
\tag{16}
```

Pairing $u$ with $p-u$ shows that the half-range square sum vanishes.
Consequently the odd square sum vanishes as well, while the odd harmonic
sum is minus one half of the half-range harmonic sum.  Expanding

```math
\frac{j}{(2j-1)^2}
=
\frac1{2(2j-1)}+\frac1{2(2j-1)^2}
\tag{17}
```

in (15), the harmonic terms cancel and the square terms vanish.  This
proves (14).

If $r\ge2$, then

```math
\left\lceil\frac{p^{r-1}t}{2}\right\rceil
\equiv0\pmod p
\qquad(t\text{ even}),
\tag{18a}
```

whereas

```math
\left\lceil\frac{p^{r-1}t}{2}\right\rceil
\equiv\frac12\pmod p
\qquad(t\text{ odd}).
\tag{18b}
```

The remaining sum is therefore one half of the odd reciprocal-square
sum, which vanishes by (16).  Equations (7), (13), and the two
cancellations prove (9). $\square$

## 4. The three source conjectures

Equation (2) is Theorem 1 with $r=1$.

For (3), put

```math
\varepsilon=(-1)^{(p^2-1)/8}
=\left(\frac2p\right).
\tag{19}
```

Theorem 1 reduces its right-hand side to a power of $2$.  The difference
between the two exponents is

```math
\frac{p+1}{2}(p^2-p+1)-\frac{p^2+1}{2}
=p^2\frac{p-1}{2}.
\tag{20}
```

Euler's criterion gives
$2^{(p-1)/2}\equiv\varepsilon\pmod p$.  If
$2^{(p-1)/2}=\varepsilon+pu$, raising to the $p^2$-th power gives

```math
\left(2^{(p-1)/2}\right)^{p^2}
\equiv\varepsilon\pmod {p^3}.
\tag{21}
```

The extra factor $\varepsilon$ in (3) cancels this sign.  Hence (3)
follows.

For (4), the exponent difference is

```math
\frac{p^2+1}{2}\frac{p^3-p^2+2}{2}
-\frac{p^3+1}{2}
=
p^2(p-1)\frac{p^2-1}{4}.
\tag{22}
```

The last factor is integral for odd $p$.  Fermat's theorem followed by
the same one-step lifting calculation shows that $2$ to the power in
(22) is $1$ modulo $p^3$.  This proves (4) for every odd prime.

At $p=2$, the sole remaining instance is a finite boundary:

```math
a(4)=2772,\qquad
a(8)=2740612658576,
\qquad
a(8)\equiv a(4)^3\equiv0\pmod8.
\tag{23}
```

Thus all three conjectures on the source page hold.

## 5. Verification and provenance

The exact checker:

1. reproduces the displayed initial sequence;
2. verifies the multiplicity and paired-product identities;
3. checks the half-range harmonic cancellations;
4. tests Theorem 1 through several prime-power levels; and
5. verifies all three source congruences, including the binary boundary.

Run:

```text
python verification/related/verify_a049505_symmetric_plane_partitions.py
```

The source of the three named conjectures is the live OEIS page.  This
note makes no literature-priority claim for the proof or its paired-product
form.
