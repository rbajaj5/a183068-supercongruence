# Precision lifting and a \(p\)-adic valuation expansion

## Status

This note proves an all-precision period law for the degree-seven Frobenius
trace at \(p=5\), extends the exact valuation partition polynomial from
precision \(5^4\) to \(5^6\), and places the resulting obstruction language
on one profinite clock.

The proof uses a Hensel unit-root factor and one finite matrix certificate
modulo \(125\). The period-lifting lemma is elementary. The unit-root
application and the explicit high-precision distributions are structural
follow-ons in this repository; literature priority remains preliminary.

## 1. Valuation as nested residue-class indicators

Put \(v_p(0)=+\infty\). For \(x\in\mathbf Z_p\) and \(k\geq1\), define

\[
d_k(x)=\min\{k,v_p(x)\}.
\tag{1}
\]

Then

\[
\boxed{
d_k(x)
=
\sum_{h=1}^{k}\mathbf 1_{p^h\mathbf Z_p}(x).
}
\tag{2}
\]

Indeed, both sides count the integers \(h\) with \(1\leq h\leq k\) and
\(p^h\mid x\).

Every set \(p^h\mathbf Z_p\) is the inverse image of \(0\) under reduction
modulo \(p^h\), hence is both open and closed. Thus (2) is an exact expansion
of the truncated valuation into nested residue-class indicators. No
separation theorem or product-compactness theorem is needed for this fact.
The formula is closer to a van der Put or \(p\)-adic wavelet expansion than
to a classical Taylor series.

There is also a Mahler expansion. If
\(f_h(x)=\mathbf 1_{p^h\mathbf Z_p}(x)\), then

\[
f_h(x)=\sum_{n\geq0}a_{h,n}\binom{x}{n},
\qquad
a_{h,n}
=
\sum_{\substack{0\leq j\leq n\\p^h\mid j}}
(-1)^{n-j}\binom nj.
\tag{3}
\]

Formula (3) is simply the Newton forward-difference formula
\(a_{h,n}=\Delta^nf_h(0)\). Equation (2), rather than (3), is the useful
form for congruence strata.

### Berkovich boundary and possible extension

The distinction is visible in
[Murayama's notes on Berkovich spaces](https://www.math.purdue.edu/~murayama/Berkovich.pdf).
The ordinary non-Archimedean field is totally disconnected and its balls are
open and closed. The Berkovich closed disc adds multiplicative-seminorm
points and becomes a path-connected tree.

The clock used below remains the elementary profinite space
\(\mathbf Z/156\mathbf Z\times\mathbf Z_5\). No affinoid algebra \(A\) and
no identification with a Berkovich spectrum \(\mathcal M(A)\) are
constructed here. Consequently, the residue-cylinder expansion is not being
presented as Berkovich analytic geometry.

A genuine Berkovich extension would first require an analytic family whose
values at classical points recover the Frobenius defect. One could then ask
whether the negative logarithm of its seminorm organizes valuation thresholds
along a skeleton by a piecewise-affine slope law. Constructing that family
and proving such a law are open targets, not consequences of the finite
period calculation.

## 2. A vector period-lifting lemma

For a vector over \(\mathbf Z_p\), let \(v_p(x)\) denote the minimum
valuation of its coordinates.

### Lemma 1

Let \(p\) be an odd prime, let \(A\in M_d(\mathbf Z_p)\), and let
\(x\in\mathbf Z_p^d\). Suppose that for some \(t\geq1\):

1. \(t\) is the exact period of \(x\) under \(A\) modulo \(p^2\);
2. \(C=A^t\) satisfies \(C=I+pD\) with \(D\in M_d(\mathbf Z_p)\); and
3. \(v_p(Dx)=1\).

Then, for every integer \(m\geq1\),

\[
v_p(C^mx-x)=v_p(m)+2.
\tag{4}
\]

Consequently, the exact period of \(x\) under \(A\) modulo \(p^k\) is

\[
t\,p^{k-2}
\qquad(k\geq2).
\tag{5}
\]

### Proof

Expand

\[
C^mx-x
=
mpDx+
\sum_{q=2}^{m}\binom mq p^qD^qx.
\tag{6}
\]

The first term has valuation \(v_p(m)+2\). Since \(v_p(Dx)=1\), every
\(D^qx\) with \(q\geq1\) has valuation at least \(1\). Moreover,

\[
v_p\!\binom mq\geq v_p(m)-v_p(q),
\tag{7}
\]

because

\[
\binom mq=\frac mq\binom{m-1}{q-1}.
\]

For \(p\) odd and \(q\geq2\), one has \(q-v_p(q)\geq2\). Hence every term
of the sum in (6) has valuation at least

\[
v_p(m)-v_p(q)+q+1
\geq v_p(m)+3.
\tag{8}
\]

The first term therefore cannot cancel, proving (4).

Every period modulo \(p^k\) is a multiple of the exact period \(t\) modulo
\(p^2\). By (4), \(C^m x\equiv x\pmod {p^k}\) holds exactly when
\(v_p(m)\geq k-2\). The smallest such \(m\) is \(p^{k-2}\), proving (5).
\(\square\)

This lemma is the arithmetic analogue of resolving a grid at one additional
\(p\)-adic digit: after the first nonzero tangent is certified, each new
precision multiplies the period by \(p\).

## 3. The degree-seven unit-root certificate

The degree-seven collision example at \(p=5\) has local numerator

\[
\begin{aligned}
P_5(T)={}&1+2T^3+7T^4-16T^5-34T^6-80T^7\\
&+175T^8+250T^9+15625T^{12}.
\end{aligned}
\tag{9}
\]

Its reciprocal Frobenius polynomial is

\[
\begin{aligned}
\chi(X)={}&X^{12}+2X^9+7X^8-16X^7-34X^6\\
&-80X^5+175X^4+250X^3+15625.
\end{aligned}
\tag{10}
\]

Modulo \(5\),

\[
\chi(X)
\equiv
X^6\left(
X^6+2X^3+2X^2+4X+1
\right).
\tag{11}
\]

The two factors in (11) are coprime, so Hensel factorization gives a unique
degree-six unit-root factor \(W(X)\in\mathbf Z_5[X]\). Modulo \(125\),

\[
\boxed{
W(X)
\equiv
X^6+105X^5+100X^4+2X^3+92X^2+44X+111.
}
\tag{12}
\]

The complementary factor is

\[
N(X)\equiv X^6+20X^5+50X^4\pmod {125},
\tag{13}
\]

and direct multiplication gives

\[
W(X)N(X)\equiv\chi(X)\pmod {125}.
\tag{14}
\]

Let \(A\) be the recurrence companion matrix of \(W\), acting on six
consecutive unit-root power sums. Newton's identities give the state

\[
x=(20,75,119,97,80,91)\pmod {125}.
\tag{15}
\]

The finite certificate is:

\[
\begin{array}{ll}
\text{period of \(x\) modulo \(5\)}&=39,\\
\text{period of \(x\) modulo \(25\)}&=195,\\
A^{195}&\equiv I\pmod5,\\
(A^{195}-I)x
&\equiv25(4,1,4,3,0,1)\pmod {125}.
\end{array}
\tag{16}
\]

The last vector is nonzero modulo \(5\). Thus Lemma 1 applies with
\(p=5\) and \(t=195\).

For completeness, exactness of the two starting periods is certified by

\[
\begin{array}{c|ccc}
n&3&13&39\\ \hline
A^nx\bmod5
&(2,0,1,3,0,1)&(1,4,0,3,0,3)&(0,0,4,2,0,1),
\end{array}
\tag{17}
\]

where \(x\bmod5=(0,0,4,2,0,1)\), and

\[
\begin{array}{c|cccc}
n&15&39&65&195\\ \hline
A^nx\bmod25
&(5,23,10,3,22,5)&(5,20,4,2,20,11)&
(0,2,7,1,21,22)&(20,0,19,22,5,16).
\end{array}
\tag{18}
\]

Every proper divisor of \(39\) divides \(3\) or \(13\), and every proper
divisor of \(195\) divides \(15\), \(39\), or \(65\). The tables therefore
prove the asserted exact periods without an exhaustive orbit listing.

### Theorem 2 (all-precision trace period)

Let \(u_r\) be the power sum of the six unit roots of \(\chi\). Its exact
period modulo \(5^k\) is

\[
\boxed{
\operatorname{per}_{5^k}(u)
=
39\cdot5^{k-1}
}
\qquad(k\geq1).
\tag{19}
\]

The full Frobenius trace \(\tau_r\) has the same eventual period modulo
\(5^k\).

### Proof

The case \(k=1\) and the exact period \(195\) modulo \(25\) are certified in
(16). For \(k\geq2\), Lemma 1 gives

\[
195\cdot5^{k-2}=39\cdot5^{k-1}.
\]

The factorization (11) is ordinary: six Frobenius roots are units, and the
functional equation pairs each unit root \(\alpha\) with \(5/\alpha\).
Hence

\[
\tau_r=u_r+5^r w_r
\tag{20}
\]

for a \(5\)-adically integral sequence \(w_r\). For \(r\geq k\), the second
term vanishes modulo \(5^k\). Therefore the eventual full trace has exactly
the unit-root period (19). \(\square\)

For the finite correction in the collision packet, the period is \(4\)
modulo \(5\) and divides \(20\) at every higher precision. It follows that

\[
L_k=156\cdot5^{k-1}
\tag{21}
\]

is an eventual period of the complete raw obstruction packet modulo
\(5^k\).

## 4. Two new exact partition polynomials

Let

\[
d_{k,r}
=
\min\!\left\{
k,\,
v_5(\mathcal V_r-\mathcal V_{r-1})
\right\}.
\tag{22}
\]

Over one period \(L_5=97500\), the exact histogram is

\[
(N_0,N_1,N_2,N_3,N_4,N_5)
=
(80000,13500,3000,725,195,80).
\tag{23}
\]

Thus

\[
\boxed{
Z_5(u)
=
80000+13500u+3000u^2+725u^3+195u^4+80u^5.
}
\tag{24}
\]

Over one period \(L_6=487500\),

\[
(N_0,N_1,N_2,N_3,N_4,N_5,N_6)
=
(400000,67500,15000,3625,975,320,80),
\tag{25}
\]

so

\[
\boxed{
\begin{aligned}
Z_6(u)={}&400000+67500u+15000u^2+3625u^3\\
&+975u^4+320u^5+80u^6.
\end{aligned}
}
\tag{26}
\]

The two new threshold densities are

\[
\delta_5=\frac4{4875},
\qquad
\delta_6=\frac4{24375}.
\tag{27}
\]

At precision \(5^6\), the mean and variance of the truncated valuation are

\[
\frac{22871}{97500},
\qquad
\frac{3115714859}{9506250000}.
\tag{28}
\]

These are exact recurrence computations over the complete periods, not
sampling estimates.

## 5. One profinite valuation grid

The periods (21) form a divisibility tower:

\[
L_k\mid L_{k+1}.
\tag{29}
\]

Its inverse-limit clock is

\[
\mathcal X
=
\varprojlim_k\mathbf Z/L_k\mathbf Z
\cong
\mathbf Z/156\mathbf Z\times\mathbf Z_5.
\tag{30}
\]

For \(h\geq1\), let \(\mathcal A_h\subset\mathcal X\) be the eventual set
of clock states on which the raw adjacent defect is divisible by \(5^h\).
It is the inverse image of a subset of the finite quotient
\(\mathbf Z/L_h\mathbf Z\), hence a clopen cylinder, and

\[
\mathcal A_{h+1}\subseteq\mathcal A_h.
\tag{31}
\]

Define

\[
D_k(x)=\sum_{h=1}^{k}\mathbf1_{\mathcal A_h}(x).
\tag{32}
\]

### Corollary 3

The function \(D_k\) is the unique continuous extension to \(\mathcal X\)
of the eventual truncated raw-defect valuation at precision \(5^k\).
Pointwise,

\[
D(x)=\sum_{h\geq1}\mathbf1_{\mathcal A_h}(x)
\tag{33}
\]

is the corresponding extended valuation, possibly \(+\infty\) on
\(\bigcap_h\mathcal A_h\).

The continuity assertion is for each finite truncation \(D_k\). The
extended-valued limit \(D\) is not being asserted to be a continuous
real-valued function at points where it is infinite.

### Proof

Modulo \(5^h\), eventual acceptance depends only on the clock class modulo
\(L_h\), by (21). Thus \(\mathcal A_h\) is a cylinder in the inverse limit.
The divisibility implication \(5^{h+1}\mid y\Rightarrow5^h\mid y\) proves
(31). Formula (32) is exactly the valuation identity (2), applied to the
raw defect. A finite sum of clopen indicators is continuous. \(\square\)

This is the rigorous form of the grid picture: every additional row records
one more \(5\)-adic digit of divisibility, and the complete valuation is the
sum of the nested binary layers.

## 6. Relation to Collatz and Størmer

The same local building blocks occur in other problems, but the global
theorems are different.

- In the accelerated Collatz map, \(v_2(3n+1)\) determines how many binary
  digits are removed at one step. The level sets are clopen subsets of the
  odd \(2\)-adics. This gives a useful symbolic dynamics, but it does not
  supply the global orbit control required by the Collatz conjecture.
- In Størmer's theorem, the allowed valuations are exponent coordinates of
  \(S\)-units, and consecutive smooth numbers solve an \(S\)-unit equation.
  The finiteness theorem comes from global Diophantine structure, classically
  Pell equations, rather than from the valuation expansion alone.

Thus (2) is reusable syntax. A problem is solved only when its transition or
Diophantine constraints can also be controlled.

## 7. Verification and literature boundary

The checker
[`verify_padic_valuation_expansion.py`](../verification/related/verify_padic_valuation_expansion.py)
verifies:

1. the Hensel factorization (12)--(14);
2. every matrix certificate in (16)--(18);
3. the observed full trace-state periods through \(5^6\);
4. all \(97500\) precision-\(5^5\) clock classes;
5. all \(487500\) precision-\(5^6\) clock classes; and
6. the valuation expansion (2) on an independent integer range.

Run:

```text
python verification/related/verify_padic_valuation_expansion.py
```

Related literature:

- V. Anashin,
  [Automata finiteness criterion in terms of van der Put series of automata
  functions](https://arxiv.org/abs/1112.5089),
  identifies finite \(p\)-letter transducers with \(1\)-Lipschitz
  \(p\)-adic maps and relates their states to van der Put coefficients. The
  clock (30) has an additional prime-to-\(5\) phase, but the clopen-layer
  mechanism is the same.
- F. Beukers,
  [\(p\)-linear schemes for sequences modulo \(p^r\)](https://arxiv.org/abs/2211.15240),
  develops finite \(p\)-automata for Lucas-type combinatorial sequences.
  The present clock is instead generated by a Frobenius linear recurrence.
- L. Mérai and I. E. Shparlinski,
  [Distribution of recursive matrix pseudorandom number generators modulo
  prime powers](https://arxiv.org/abs/2302.03964),
  study distribution for invertible integral matrix recurrences. The full
  Frobenius companion here is not invertible modulo \(5\); the Hensel
  unit-root factor isolates the invertible part.
- R. Costa, P. Dynes, and C. Petsche,
  [A \(p\)-adic Perron--Frobenius theorem](https://arxiv.org/abs/1509.01702),
  provide a distinct dominant-eigenvalue convergence theorem. It is not used
  in the finite period-lifting proof above.
- [Finite-state thermodynamics of Frobenius obstruction
  towers](FrobeniusTransferThermodynamics.md), for the partition-polynomial
  formalism and the precision-\(5^4\) calculation.
