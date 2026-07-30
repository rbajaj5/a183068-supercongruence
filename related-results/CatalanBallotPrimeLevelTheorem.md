# A cubic prime-level theorem for every odd Catalan-ballot power

**Status:** complete elementary proof candidate; independent review and
literature-priority review pending

## 1. The theorem

Let

$$
d_{p,k}
=
\binom{2p-1}{k}-\binom{2p-1}{k-1},
\qquad 0\le k\le p-1,
$$

where \(\binom{2p-1}{-1}=0\).

**Theorem.** If \(p\ge5\) is prime and \(m\ge1\) is odd, then

$$
\boxed{
\sum_{k=0}^{p-1}d_{p,k}^{\,m}
\equiv
\binom{2p-1}{p-1}
\pmod {p^3}.
}
\tag{1}
$$

Equivalently, in the localization \(\mathbb Z_{(p)}\),

$$
\boxed{
\frac{1}{\binom{2p-1}{p-1}}
\sum_{k=0}^{p-1}d_{p,k}^{\,m}
\equiv1\pmod {p^3}.
}
\tag{2}
$$

The localized formulation does not assume that the quotient is an integer
for every odd \(m\). For \(m=3,5,7\), the quotients are the named OEIS
sequences [A183069], [A361889], and [A361892].

Thus (2) proves the \(n=r=1\) case of all three recorded
supercongruence conjectures at once, and proves the same prime-level
statement for every odd exponent. It also proves the prime-level
conjectures recorded for the odd bisections of [A003161] and [A003162].
The full adjacent-scale claim for arbitrary \(n,r\) remains open.

## 2. Expansion of one ballot entry

Work in \(\mathbb Z_{(p)}\). For \(1\le k\le p-1\), put

$$
H_j=\sum_{a=1}^{j}\frac1a,
\qquad
H_j^{(2)}=\sum_{a=1}^{j}\frac1{a^2}.
$$

Pascal's identity gives the exact factorization

$$
\begin{aligned}
d_{p,k}
&=
(-1)^k
\prod_{a=1}^{k-1}\left(1-\frac{2p}{a}\right)
\left(2-\frac{2p}{k}\right)\\
&=
2(-1)^k
\prod_{a=1}^{k-1}\left(1-\frac{2p}{a}\right)
\left(1-\frac pk\right).
\end{aligned}
\tag{3}
$$

Define

$$
\alpha_k=-\left(2H_{k-1}+\frac1k\right)
$$

and

$$
\beta_k=
2H_{k-1}^2-2H_{k-1}^{(2)}
+\frac{2H_{k-1}}k.
$$

Expanding the product in (3) through degree two gives

$$
d_{p,k}
\equiv
2(-1)^k
\left(1+p\alpha_k+p^2\beta_k\right)
\pmod {p^3}.
\tag{4}
$$

Since \(m\) is odd,

$$
\frac{d_{p,k}^{\,m}}{2^m}
\equiv
(-1)^k
\left(
1+mp\alpha_k
+p^2\left(m\beta_k+\binom m2\alpha_k^2\right)
\right)
\pmod {p^3}.
\tag{5}
$$

## 3. Linear cancellation

Because \(p-1\) is even,

$$
\sum_{k=1}^{p-1}(-1)^k=0.
$$

The coefficient of \(p\) in the sum of (5) telescopes:

$$
\begin{aligned}
\sum_{k=1}^{p-1}(-1)^k\alpha_k
&=
-\sum_{k=1}^{p-1}(-1)^k
\left(H_{k-1}+H_k\right)\\
&=-H_{p-1}.
\end{aligned}
\tag{6}
$$

Wolstenholme's congruence gives

$$
H_{p-1}\equiv0\pmod {p^2}
$$

for \(p\ge5\). Hence the full linear contribution in (5) vanishes
modulo \(p^3\).

## 4. Quadratic cancellation

Set

$$
\begin{aligned}
A&=\sum_{k=1}^{p-1}(-1)^kH_{k-1}^2,\\
B&=\sum_{k=1}^{p-1}(-1)^k\frac{H_{k-1}}k,\\
C&=\sum_{k=1}^{p-1}\frac{(-1)^k}{k^2},\\
D&=\sum_{k=1}^{p-1}(-1)^kH_{k-1}^{(2)}.
\end{aligned}
$$

Applying the same alternating telescoping to \(H_k^2\) gives the exact
identity

$$
2(A+B)+C=H_{p-1}^2.
\tag{7}
$$

Reversing the order of summation in \(D\) gives

$$
D=\sum_{\substack{1\le j\le p-2\\j\ {\rm odd}}}\frac1{j^2}.
\tag{8}
$$

Also,

$$
\sum_{j=1}^{p-1}\frac1{j^2}\equiv0\pmod p.
\tag{9}
$$

If the even and odd parts of (9) are denoted by \(E\) and \(O\), then
\(C=E-O\), \(D=O\), and therefore

$$
D\equiv-\frac C2\pmod p.
\tag{10}
$$

Finally, pairing \(k\) with \(p-k\) shows directly that

$$
C\equiv0\pmod p,
\tag{11}
$$

because the two signs are opposite and the inverse squares agree.

The quadratic coefficient in the sum of (5) is

$$
\begin{aligned}
Q
&=
\sum_{k=1}^{p-1}(-1)^k
\left(m\beta_k+\binom m2\alpha_k^2\right)\\
&=
2m^2(A+B)-2mD+\binom m2 C.
\end{aligned}
\tag{12}
$$

Equations (7), (10), and (11) give

$$
Q\equiv-\frac{m(m-1)}2C\equiv0\pmod p.
\tag{13}
$$

Thus the quadratic term in (5) also vanishes modulo \(p^3\). We have proved

$$
\sum_{k=1}^{p-1}d_{p,k}^{\,m}\equiv0\pmod {p^3}.
\tag{14}
$$

Since \(d_{p,0}=1\), the left side of (1) is \(1\) modulo \(p^3\).
The classical product expansion

$$
\binom{2p-1}{p-1}
=
\prod_{j=1}^{p-1}\left(1+\frac pj\right)
\equiv1\pmod {p^3}
\tag{15}
$$

follows from Wolstenholme's congruence and (9). This proves (1) and (2).
\(\square\)

## 5. Named consequences and boundary

The OEIS pages state the following \(p^{3r}\) towers for \(p\ge5\):

- [A183069], the cubic quotient;
- [A361889], the fifth-power quotient;
- [A361892], the seventh-power quotient; and
- the equivalent odd-bisection formulations on [A003161] and [A003162].

The theorem proves their common first point

$$
B_m(p)\equiv B_m(1)=1\pmod {p^3}.
$$

It does not prove \(B_m(np^r)\equiv B_m(np^{r-1})\) for general \(n,r\).
Unlike A183068, individual terms with \(p\nmid k\) do not vanish to the
target precision. The proof above instead uses cancellation across the
entire first residue block. A higher-level proof must lift that block
cancellation through every \(p\)-adic digit.

The existing computational audit tests the full named towers and records
sharp experimental losses at \(p=2,3\). Those exceptional-prime patterns
are not consequences of this theorem.

## 6. Verification and literature boundary

Run

```text
python verification/related/verify_catalan_ballot_prime_level.py
```

The exact checker verifies the local expansion, the harmonic identities,
the all-odd-exponent prime theorem through \(p=47\), and all five named
consequences.

The source pages link Miana, Ohtsuka, and Romero's
[*Sums of powers of Catalan triangle numbers*](https://arxiv.org/abs/1602.04347),
which studies the relevant power identities and integrality questions.
Targeted searches by A-number, exact formula, and congruence shape did not
locate the prime-level all-odd-exponent theorem above. That search is not a
priority certificate; the argument uses classical harmonic congruences, so
independent literature review remains necessary.

[A003161]: https://oeis.org/A003161
[A003162]: https://oeis.org/A003162
[A183069]: https://oeis.org/A183069
[A361889]: https://oeis.org/A361889
[A361892]: https://oeis.org/A361892
