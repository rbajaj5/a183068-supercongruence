# Catalan ballot-power supercongruence audit

## Status

This note records exact computations and a unified conjectural target. It is
not a proof.

For an odd integer \(m\ge 3\), put

\[
 B_m(n)=
 \frac{1}{\binom{2n-1}{n-1}}
 \sum_{k=0}^{n-1}
 \left(
   \binom{2n-1}{k}-\binom{2n-1}{k-1}
 \right)^m,
 \qquad n\ge1,
\]

where \(\binom{2n-1}{-1}=0\).  The three cases used here are existing
OEIS sequences:

- \(B_3=\) [A183069];
- \(B_5=\) [A361889];
- \(B_7=\) [A361892].

Each entry records the same named conjecture:

\[
 B_m(np^r)\equiv B_m(np^{r-1})\pmod {p^{3r}}
 \tag{1}
\]

for primes \(p\ge5\) and positive integers \(n,r\).

## Two older OEIS records reduce to the same target

Let

\[
S_m(j)=\sum_{k=0}^{\lfloor j/2\rfloor}
\left(\binom jk-\binom j{k-1}\right)^m.
\]

The live page [A003161] is \(S_3(j)\), while [A003162] is
\(S_3(j)/S_1(j)\). At an odd index \(j=2n-1\), the elementary ballot sum is

\[
S_1(2n-1)=\binom{2n-1}{n-1}.
\]

Consequently,

\[
\operatorname{A003162}(2n-1)=B_3(n),
\tag{4}
\]

and

\[
\operatorname{A003161}(2n-1)
=\binom{2n-1}{n-1}B_3(n).
\tag{5}
\]

The factor in (5) is

\[
\binom{2n-1}{n-1}=\frac12\binom{2n}{n}.
\]

For every prime \(p\ge5\), the classical binomial scaling congruence gives

\[
\binom{2np^r-1}{np^r-1}
\equiv
\binom{2np^{r-1}-1}{np^{r-1}-1}
\pmod {p^{3r}}.
\tag{6}
\]

Equations (4)--(6) show that the conjectures on A003161 and A003162 do not
introduce new arithmetic directions. The A003162 claim is literally the
\(m=3\) case (1), and the A003161 claim follows from that case by multiplying
by the integral factor in (6). Both records therefore reduce to the single
unresolved \(B_3\) tower already isolated here.

## Exact audit of the three named conjectures

The checker
[`verify_catalan_ballot_supercongruences.py`](../verification/related/verify_catalan_ballot_supercongruences.py)
uses Python integers only. It checks the division defining \(B_m(n)\) before
performing any congruence test.

It first checks (4)--(5) as exact integer identities for every
\(1\le n\le200\). It also tests the classical cubic adjacent scaling of the
central-binomial factor in (6) in the same 388 admissible
\((p,r,n)\)-cases used below. These checks make the reduction of A003161 and
A003162 independently executable rather than merely notational.

For each \(m\in\{3,5,7\}\), it tests (1) for

\[
 p\in\{5,7,11,13,17,19\},\qquad
 1\le r\le3,\qquad
 1\le n\le50,\qquad np^r\le1000.
\]

There are 388 admissible quadruples for each exponent \(m\), or 1,164
official-conjecture checks in total. All pass. The valuation \(3r\) is
attained, so the displayed exponent cannot be uniformly increased on this
range.

This is evidence for the three OEIS conjectures, not a proof of them.

## Small-prime refinement suggested by the data

The same computation supports the following refinement for all three
exponents:

\[
 v_3\!\left(B_m(n3^r)-B_m(n3^{r-1})\right)\ge 3r-1,
 \tag{2}
\]

and

\[
 v_2\!\left(B_m(n2^r)-B_m(n2^{r-1})\right)\ge
 \begin{cases}
 1,&r=1,\\
 3r-1,&r\ge2.
 \end{cases}
 \tag{3}
\]

The checker tests (2)--(3) for \(r\le4\), \(n\le50\), and \(np^r\le1000\).
There are 349 admissible cases for each \(m\), or 1,047 checks in total.
All pass, and equality occurs. Thus the proposed losses at \(2\) and \(3\)
are sharp in the tested range.

Neither (2) nor (3) appears on the three cited OEIS entries. Literature
priority has not been searched beyond those records.

## Unified target

The identical valuation profile for \(m=3,5,7\) suggests studying the
family rather than proving three isolated conjectures:

> **Ballot-power target.** Determine the odd exponents \(m\ge3\) for which
> \(B_m(n)\) is always integral and the adjacent-scale bounds
> (1)--(3) hold.

The integrality clause matters. Divisibility of odd power sums of Catalan
triangle entries is itself part of the surrounding literature, and finite
integer output is not a proof of general integrality.

This target is structurally separate from A183068. Exact checks of A183068
frequently attain its exponent \(2r\), so a blanket strengthening of that
sequence to \(3r\) is false.

## Reproduction

From the repository root, run

```text
python verification/related/verify_catalan_ballot_supercongruences.py
```

[A183069]: https://oeis.org/A183069
[A361889]: https://oeis.org/A361889
[A361892]: https://oeis.org/A361892
[A003161]: https://oeis.org/A003161
[A003162]: https://oeis.org/A003162
