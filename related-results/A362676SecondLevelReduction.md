# A second-level transfer and reduction for A362676

**Status:** complete proof of the scaled-index transfer modulo \(p^6\);
exact reduction of the \(r=2\) theorem to one unit-superblock lemma; that
last lemma is verified in the companion checker but is not claimed proved
here; priority provisional

Let

~~~math
F(N)=\sum_{k=0}^{N}4^{N-k}\binom Nk\binom{N-1}{k}\binom{2k}{k}.
~~~

The [one-step theorem](A362676OneStepCongruence.md) proves

~~~math
F(np)\equiv F(n)\pmod {p^3}
~~~

for every prime \(p\geq5\).  This note advances the next adjacent level.
It proves that every term whose upper-level index is divisible by \(p\)
already transfers with the full required precision \(p^6\).  Thus the only
remaining \(r=2\) obstruction is an explicitly displayed sum over unit
indices.

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

## 4. Exact reduction of the \(r=2\) theorem

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

No divisible-index transfer remains to be proved.

## 5. The observed two-stage cancellation

Write \(j=ap+c\), \(0\leq c<p\), and set

~~~math
B_j=\sum_{b=1}^{p-1}A_{np^2}(jp+b).
\tag{12}
~~~

Exact arithmetic shows first that every \(B_j\) is divisible by \(p^5\).
Set \(h=(p-1)/2\) and

~~~math
\begin{aligned}
C_a^-&=n(n-a)\binom{n+a}{a}
\binom{2a}{a}\binom{2(n-a)}{n-a},\\
C_a^+&=n(a+1)\binom{n+a}{a}
\binom{2a+2}{a+1}
\binom{2(n-a-1)}{n-a-1}.
\end{aligned}
~~~

The checker finds a constant \(\lambda_p\), independent of \(n,a,c\),
for which

~~~math
\frac{B_{ap+c}}{p^5}\equiv
\begin{cases}
\lambda_pC_a^-,
  &0\leq c<h,\\[2mm]
\dfrac{\lambda_p}{2}(C_a^--C_a^+),
  &c=h,\\[2mm]
-\lambda_pC_a^+,
  &h<c<p
\end{cases}
\pmod p.
\tag{13}
~~~

Summing (13) over \(c\) gives zero: there are \(h\) low blocks,
\(h\) high blocks, and \(h\equiv-1/2\pmod p\).  Hence (13), once derived
algebraically, proves (11).

Equation (13) is a sharply specified next lemma, not a theorem claimed by
this note.  Its role is to expose the last cancellation rather than hide it
inside a numerical statement.

## 6. Verification boundary

The companion checker
[verify_a362676_second_level.py](../verification/related/verify_a362676_second_level.py)
verifies:

- the scaled-index transfer (5);
- the exact reduction (9);
- divisibility of every one-digit block by \(p^5\);
- divisibility of every two-digit superblock by \(p^6\);
- the residue law (13); and
- the resulting \(r=2\) congruence
  \(F(np^2)\equiv F(np)\pmod {p^6}\)

over a finite grid in exact integer arithmetic.  These checks audit the
reduction and identify the missing lemma; they are not used as a proof of
(11).  The default grid contains 4,560 assertions: 1,110 scaled transfers,
150 central cubic-quotient expansions, 990 carry budgets, 1,080 one-digit
blocks, 90 superblocks, 1,080 piecewise residues, 30 exact reductions, and
30 direct second-level congruences.

## References

- Peter Bala, [OEIS A362676](https://oeis.org/A362676).
- Charles Helou and Guy Terjanian,
  [On Wolstenholme's theorem and its converse](https://doi.org/10.1016/j.jnt.2007.06.008),
  for refined Jacobsthal congruences.
- Robert Osburn and Brundaban Sahu,
  [A supercongruence for generalized Domb numbers](https://arxiv.org/abs/1201.6195),
  for the divisible/unit-index proof architecture.
