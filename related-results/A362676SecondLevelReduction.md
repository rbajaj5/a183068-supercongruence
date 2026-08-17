# The second-level cubic congruence for A362676

**Status:** complete proof of the full \(r=2\) layer; higher adjacent
levels remain open; priority provisional

Let

~~~math
F(N)=\sum_{k=0}^{N}4^{N-k}\binom Nk\binom{N-1}{k}\binom{2k}{k}.
~~~

The [one-step theorem](A362676OneStepCongruence.md) proves

~~~math
F(np)\equiv F(n)\pmod {p^3}
~~~

for every prime \(p\geq5\).  This note advances the next adjacent level.
It first proves that every term whose upper-level index is divisible by
\(p\) transfers with the full required precision \(p^6\).  A second
reciprocal-sum calculation then cancels the remaining unit indices in
two-digit superblocks.

## 1. Positive convolution

Put

~~~math
A_N(k)=\binom{N+k-1}{k}
       \binom{2(N-k)}{N-k}\binom{2k}{k}.
\tag{1}
~~~

The terminating hypergeometric transformation proved in the one-step note
gives

~~~math
F(N)=\sum_{k=0}^{N}A_N(k).
\tag{2}
~~~

## 2. Two Jacobsthal forms

For a prime \(p\geq5\), write

~~~math
Q_p(a,b)=\frac{\binom{pa}{pb}}{\binom ab}.
~~~

The refined Jacobsthal congruence gives

~~~math
v_p\!\left(Q_p(a,b)-1\right)
\geq 3+v_p\!\left(ab(a-b)\right).
\tag{3}
~~~

We also need the leading term only for central binomial coefficients.
There is a constant \(\kappa_p\in\mathbb Z/p\mathbb Z\), depending on
\(p\) but not on \(x\), such that

~~~math
Q_p(2x,x)\equiv1+\kappa_p p^3x^3\pmod {p^4}.
\tag{4}
~~~

For completeness, (4) follows directly from the unit product

~~~math
Q_p(2x,x)=
\prod_{\substack{1\leq j\leq px\\p\nmid j}}
\left(1+\frac{px}{j}\right).
~~~

To see the coefficient explicitly, put

~~~math
H_{p-1}^{(m)}=\sum_{b=1}^{p-1}b^{-m}
~~~

in \(\mathbb Z_p\), and split \(j=ap+b\), with \(0\leq a<x\) and
\(1\leq b<p\).  Wolstenholme's congruence and the finite-field power
sums give

~~~math
H_{p-1}^{(1)}\equiv0\pmod {p^2},\qquad
H_{p-1}^{(2)}\equiv0\pmod p,\qquad
H_{p-1}^{(3)}\equiv0\pmod p.
~~~

Pairing \(b\) with \(p-b\) also gives

~~~math
H_{p-1}^{(1)}
\equiv-\frac p2H_{p-1}^{(2)}\pmod {p^3}.
~~~

If

~~~math
S_m(x)=
\sum_{\substack{1\leq j\leq px\\p\nmid j}}j^{-m},
~~~

then expansion of \((ap+b)^{-m}\) gives

~~~math
\begin{aligned}
S_1(x)&\equiv
xH_{p-1}^{(1)}
-p\frac{x(x-1)}2H_{p-1}^{(2)}
\pmod {p^3},\\
S_2(x)&\equiv xH_{p-1}^{(2)}\pmod {p^2},\\
S_3(x)&\equiv0\pmod p.
\end{aligned}
~~~

Therefore

~~~math
\begin{aligned}
\log Q_p(2x,x)
&\equiv pxS_1(x)-\frac{p^2x^2}{2}S_2(x)
                 +\frac{p^3x^3}{3}S_3(x)\\
&\equiv
px^2H_{p-1}^{(1)}
-\frac{p^2}{2}(2x^3-x^2)H_{p-1}^{(2)}\\
&\equiv-p^2x^3H_{p-1}^{(2)}
\pmod {p^4}.
\end{aligned}
~~~

Thus (4) holds with
\(\kappa_p\equiv-H_{p-1}^{(2)}/p\pmod p\).  The logarithm has valuation
at least three, so exponentiating introduces no new term modulo \(p^4\).

## 3. Complete scaled-index transfer

### Theorem 1

For every prime \(p\geq5\), every positive integer \(n\), and every
\(0\leq k\leq np\),

~~~math
\boxed{A_{np^2}(pk)\equiv A_{np}(k)\pmod {p^6}.}
\tag{5}
~~~

### Proof

Put \(M=np\).  The exact identities

~~~math
\binom{p(M+k)-1}{pk}
=\frac{M}{M+k}\binom{p(M+k)}{pk},
~~~

and

~~~math
\binom{M+k-1}{k}
=\frac{M}{M+k}\binom{M+k}{k}
~~~

show that the quotient of the two sides of (5) is

~~~math
\frac{A_{pM}(pk)}{A_M(k)}
=Q_p(M+k,k)\,
 Q_p(2(M-k),M-k)\,
 Q_p(2k,k).
\tag{6}
~~~

The degenerate factors with lower index zero or equal to the upper index
are interpreted as \(1\).

First suppose that \(p\mid k\).  Then \(p\) divides \(M+k\), \(k\), and
\(M\).  Formula (3) puts the first factor of (6) at \(1\) modulo \(p^6\).
It does the same for each nontrivial central factor, since both \(k\) and
\(M-k\) are divisible by \(p\).  Hence (6) is \(1\) modulo \(p^6\), and
(5) follows.

Now suppose that \(p\nmid k\).  Because \(p\mid M\), (3) gives

~~~math
Q_p(M+k,k)\equiv1\pmod {p^4}.
\tag{7}
~~~

Applying (4) to the two central factors gives

~~~math
\begin{aligned}
&Q_p(2(M-k),M-k)Q_p(2k,k)\\
&\qquad\equiv
1+\kappa_pp^3\bigl((M-k)^3+k^3\bigr)
\equiv1\pmod {p^4},
\end{aligned}
\tag{8}
~~~

because

~~~math
(M-k)^3+k^3=M(M^2-3Mk+3k^2).
~~~

Thus the quotient (6) is \(1\) modulo \(p^4\).  Two independent carries
supply the other two powers.  The lower base-\(p\) digit of \(M+k-1\) is
one less than that of \(k\), so

~~~math
p\mid\binom{M+k-1}{k}.
~~~

If \(k\equiv c\pmod p\), with \(1\leq c<p\), exactly one of \(c\) and
\(p-c\) exceeds \(p/2\).  Kummer's theorem therefore shows that exactly
one of

~~~math
\binom{2k}{k},\qquad
\binom{2(M-k)}{M-k}
~~~

has a units-digit carry.  Consequently \(p^2\mid A_M(k)\).  Multiplying
the \(p^4\) quotient error by \(A_M(k)\) proves (5). QED

## 4. Reduction to the unit shell

Split (2) at level \(np^2\) according to whether \(p\mid k\).  Theorem 1
gives

~~~math
\boxed{
F(np^2)-F(np)
\equiv
\sum_{\substack{0\leq k\leq np^2\\p\nmid k}}A_{np^2}(k)
\pmod {p^6}.}
\tag{9}
~~~

For \(0\leq a<n\), define the two-digit unit superblock

~~~math
U_a=
\sum_{\substack{ap^2<k<(a+1)p^2\\p\nmid k}}A_{np^2}(k).
\tag{10}
~~~

The full second-level conjecture is therefore reduced to the following
single local statement:

~~~math
U_a\equiv0\pmod {p^6}
\qquad(0\leq a<n).
\tag{11}
~~~

No divisible-index transfer remains to be proved.  We now prove (11).

## 5. One-digit blocks to precision \(p^6\)

Write \(M=np\).  For \(0\leq j<M\), set

~~~math
B_j=\sum_{b=1}^{p-1}A_{pM}(jp+b)
\tag{12}
~~~

and define

~~~math
\begin{aligned}
D_j^-&=M(M-j)\binom{M+j}{j}
\binom{2j}{j}\binom{2(M-j)}{M-j},\\
D_j^+&=M(j+1)\binom{M+j}{j}
\binom{2j+2}{j+1}
\binom{2(M-j-1)}{M-j-1}.
\end{aligned}
\tag{13}
~~~

Kummer's theorem shows that both \(D_j^-\) and \(D_j^+\) are divisible
by \(p^2\).  Put \(h=(p-1)/2\) and, in \(\mathbb Z_p\), define

~~~math
\alpha_p\equiv
\frac1p\sum_{b=1}^{h}\frac1{b^2}\pmod p,\qquad
\beta_p\equiv\sum_{b=1}^{h}\frac1{b^3}\pmod p,
\qquad
\mu_p=-\alpha_p-\beta_p.
\tag{14}
~~~

The first quotient is defined because
\(\sum_{b=1}^{p-1}b^{-2}=0\) in \(\mathbb F_p\), while pairing \(b\)
with \(p-b\) makes the full sum twice the displayed half-sum.

### Lemma 2

For \(0\leq j<M\),

~~~math
\boxed{
B_j\equiv
\mu_pp^3(D_j^--D_j^+)\pmod {p^6}.}
\tag{15}
~~~

### Proof

Split the block into its lower and upper halves.  For \(1\leq b\leq h\),
separate the factors divisible by \(p\) in the three binomial coefficients
of \(A_{pM}(pj+b)\).  The three scaled binomial quotients can be replaced
by \(1\) modulo \(p^3\) by (3).  Since \(p^2\mid D_j^-\), their discarded
contribution is zero modulo \(p^6\).

In the remaining unit products put \(x=pj\).  Because \(pM\equiv0\pmod
{p^2}\), direct cancellation gives

~~~math
\begin{aligned}
&\frac1{2(x+b)}
\frac{\prod_{t=1}^{2b}(2x+t)}
     {\prod_{t=1}^{b}(x+t)^2}
\left(
-\frac{\prod_{t=1}^{b-1}(x+t)^2}
       {\prod_{t=1}^{2b-1}(2x+t)}
\right)\\
&\hspace{35mm}=-\frac1{(x+b)^2}.
\end{aligned}
~~~

This is exactly the normalized product left after removing the factor
\(p^2D_j^-\).  Hence

~~~math
A_{pM}(pj+b)
\equiv-\frac{p^2D_j^-}{(b+pj)^2}\pmod {p^6}.
\tag{16}
~~~

For the upper half write the index as \(p(j+1)-b\).  The same falling-
factorial calculation, now with \(x=p(j+1)\), gives

~~~math
A_{pM}(p(j+1)-b)
\equiv\frac{p^2D_j^+}{(b-p(j+1))^2}\pmod {p^6}.
\tag{17}
~~~

The two shifted reciprocal sums are

~~~math
\begin{aligned}
\sum_{b=1}^{h}\frac1{(b+pj)^2}
&\equiv p\alpha_p-2pj\beta_p\pmod {p^2},\\
\sum_{b=1}^{h}\frac1{(b-p(j+1))^2}
&\equiv p\alpha_p+2p(j+1)\beta_p\pmod {p^2}.
\end{aligned}
\tag{18}
~~~

Substitution into (16)--(17) yields

~~~math
\frac{B_j}{p^3}\equiv
D_j^-(-\alpha_p+2j\beta_p)
+D_j^+(\alpha_p+2(j+1)\beta_p)
\pmod {p^3}.
\tag{19}
~~~

The next lemma shows that the right side is
\(\mu_p(D_j^--D_j^+)\) modulo \(p^3\). QED

## 6. The second digit

For \(0\leq a<n\), define

~~~math
\begin{aligned}
C_a^-&=n(n-a)\binom{n+a}{a}
\binom{2a}{a}\binom{2(n-a)}{n-a},\\
C_a^+&=n(a+1)\binom{n+a}{a}
\binom{2a+2}{a+1}
\binom{2(n-a-1)}{n-a-1}.
\end{aligned}
\tag{20}
~~~

### Lemma 3

If \(j=ap+c\), \(0\leq c<p\), then

~~~math
\begin{array}{c|cc}
 &D_j^-/p^2&D_j^+/p^2\\ \hline
0\leq c<h&C_a^-&-C_a^-\\
c=h&C_a^-&C_a^+\\
h<c<p&-C_a^+&C_a^+
\end{array}
\pmod p.
\tag{21}
~~~

### Proof

Apply Lucas' theorem to the uncarried central binomial coefficient and
the carried formula

~~~math
\frac1p\binom{2(up-b)}{up-b}
\equiv-\frac{u\binom{2u}{u}}
 {b\binom{2b}{b}}\pmod p
\tag{22}
~~~

to the carried one.  For \(c<h\), the carry occurs in the
\(M-j\) central coefficient; for \(c>h\), it occurs in the \(j\)
central coefficient.  At \(c=h\), the first occurs in \(D_j^-\) and the
second occurs after the shift in \(D_j^+\).  For example, when
\(1\leq c\leq h\), Lucas and (22) give

~~~math
\begin{aligned}
\frac{D_j^-}{p^2}
&\equiv n(-c)\binom{n+a}{a}
\binom{2a}{a}\binom{2c}{c}
\left(
-\frac{(n-a)\binom{2(n-a)}{n-a}}
       {c\binom{2c}{c}}
\right)\\
&=C_a^-\pmod p.
\end{aligned}
~~~

The corresponding \(D_j^+\) calculation uses \(c+1\): it is
\(-C_a^-\) below the midpoint and \(C_a^+\) at the midpoint.  Above the
midpoint the carried and uncarried central coefficients exchange roles,
giving \(-C_a^+\) and \(C_a^+\).  At \(c=0\) and \(c=p-1\), the same rows
follow directly from the ordinary scaled binomial congruence.  This proves
(21). QED

By (21), the right side of (19), divided by \(p^2\), has three forms.
If \(c<h\), it equals

~~~math
C_a^-\bigl(-2\alpha_p-2\beta_p\bigr)
=2\mu_pC_a^-.
~~~

At \(c=h\), use \(h\equiv-1/2\pmod p\) to obtain

~~~math
\mu_p(C_a^--C_a^+).
~~~

If \(c>h\), the result is

~~~math
-2\mu_pC_a^+.
~~~

In every case this equals
\(\mu_p(D_j^--D_j^+)/p^2\), which completes the proof of Lemma 2.

Now sum (15) over \(j=ap+c\), \(0\leq c<p\).  Lemma 3 gives

~~~math
\begin{aligned}
\frac1{p^2}\sum_{c=0}^{p-1}
\bigl(D_{ap+c}^--D_{ap+c}^+\bigr)
&\equiv
2hC_a^-+(C_a^--C_a^+)-2hC_a^+\\
&=p(C_a^--C_a^+)\equiv0\pmod p.
\end{aligned}
~~~

Equation (15) therefore proves \(U_a\equiv0\pmod {p^6}\), which is (11).

## 7. Second-level theorem

### Theorem 2

For every prime \(p\geq5\) and every positive integer \(n\),

~~~math
\boxed{F(np^2)\equiv F(np)\pmod {p^6}.}
\tag{23}
~~~

### Proof

The scaled-index terms vanish by Theorem 1.  The unit-index terms are the
sum of the superblocks \(U_a\), each of which vanishes by Lemmas 2--3.
Apply (9). QED

## 8. Verification

The companion checker
[verify_a362676_second_level.py](../verification/related/verify_a362676_second_level.py)
verifies:

- the scaled-index transfer (5);
- the exact reduction (9);
- the explicit block expansion (15);
- the three-row scaling law (21);
- divisibility of every one-digit block by \(p^5\);
- divisibility of every two-digit superblock by \(p^6\); and
- the resulting \(r=2\) congruence
  \(F(np^2)\equiv F(np)\pmod {p^6}\)

over a finite grid in exact integer arithmetic.  These checks audit the
proof but are not inputs to it.  The default grid contains 20,850 cases,
including 14,130 local unit-term expansions and 1,080 checks each of the
explicit block expansion, the second-digit scaling table, and the
resulting piecewise block residue.

## References

- Peter Bala, [OEIS A362676](https://oeis.org/A362676).
- Charles Helou and Guy Terjanian,
  [On Wolstenholme's theorem and its converse](https://doi.org/10.1016/j.jnt.2007.06.008),
  for refined Jacobsthal congruences.
- Robert Osburn and Brundaban Sahu,
  [A supercongruence for generalized Domb numbers](https://arxiv.org/abs/1201.6195),
  for the divisible/unit-index proof architecture.
