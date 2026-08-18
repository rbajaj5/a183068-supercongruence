# A uniform half-index theorem for Bober factorial ratios

**Status:** complete elementary proof candidate; exact checks pass;
independent review and literature priority remain open

Let

```math
F(n)=\frac{\prod_i(u_i n)!}{\prod_j(v_j n)!}
\tag{1}
```

be an integral balanced factorial ratio, and write its Landau function as

```math
\Delta(x)=\sum_i\lfloor u_i x\rfloor-
\sum_j\lfloor v_jx\rfloor.
\tag{2}
```

Assume that the numbers of odd entries among the $u_i$ and $v_j$ are equal.

## Theorem

At every odd prime, the gamma-interpolated half-index value

```math
F(N/2)=
\frac{\prod_i\Gamma(u_iN/2+1)}
     {\prod_j\Gamma(v_jN/2+1)}
\tag{3}
```

p-integral. It is an integer whenever the binary digit-sum valuation in
(8) below is nonnegative.

For every prime $p\ge5$ and positive integers $n,r$,

```math
F(np^r/2)\equiv F(np^{r-1}/2)\pmod {p^{3r}}.
\tag{4}
```

## Proof

For even $N$, (3) is an ordinary value of the integral sequence. Suppose
$N$ is odd. The half-integer gamma identity gives

```math
\Gamma(k+3/2)=\frac{(2k+2)!}{4^{k+1}(k+1)!}\sqrt\pi.
\tag{5}
```

The square-root factors cancel because the two sides of (1) contain equally
many odd slopes. After removing the explicit integral power of two, the
remaining rational factorial ratio has, at an odd prime $\ell$, valuation

```math
\sum_{a\ge1}
\left(
\Delta\!\left(\frac{N}{2\ell^a}+\frac12\right)
-\Delta\!\left(\frac12\right)
\right).
\tag{6}
```

Indeed, an even slope $c$ contributes
$\lfloor cN/(2\ell^a)\rfloor$, while an odd slope $c$ contributes

```math
\left\lfloor\frac{cN+1}{\ell^a}\right\rfloor
-\left\lfloor\frac{cN+1}{2\ell^a}\right\rfloor.
```

For odd $\ell$, these are exactly the contributions of
$\lfloor c(N/(2\ell^a)+1/2)\rfloor-\lfloor c/2\rfloor$; pairing numerator
and denominator slopes yields (6).

The integrality of (1) is equivalent to $\Delta(x)\ge0$ for all real $x$.
The parity hypothesis gives

```math
\Delta(1/2)=0,
\tag{7}
```

because balance fixes the even contribution and the two sides contain the
same number of odd slopes. Hence every summand in (6) is nonnegative.

For the prime two, put

```math
K=\sum_{j:\ v_j\text{ odd}}v_j
-\sum_{i:\ u_i\text{ odd}}u_i.
```

Writing $s_2(m)$ for the number of ones in the binary expansion of $m$,
the half-gamma formula and $v_2(m!)=m-s_2(m)$ give the exact identity

```math
v_2(F(N/2))
=KN
-\sum_{i:\ u_i\text{ even}}s_2(u_iN/2)
+\sum_{j:\ v_j\text{ even}}s_2(v_jN/2).
\tag{8}
```

Thus a nonnegative right side completes global integrality. This condition
is not automatic from odd-prime Landau positivity and must be checked.

Finally, equality of the odd-slope counts is precisely residue balance
for denominator two, the hypothesis of the rational
gamma-ratio cubic-transfer theorem. It supplies the adjacent quotient
congruence modulo $p^{3r}$; multiplying by the integral lower-level value
proves (4). QED

## Bober packet corollary

All eleven Bober records in Peter Bala's packet having an $N/2$ variant pass
the parity-residue test:

```text
A295456, A295458, A295460, A295465, A295468, A295470,
A295471, A295475, A295477, A295479, A295481.
```

Bober's classification supplies their ordinary integrality and hence the
odd-prime part. For these eleven records, $K\ge2$, there are at most four
positive even slopes, and every positive even slope has the form $2c$ with
$c\le15$. For $N\ge8$,

```math
s_2(cN)\le \lfloor\log_2(15N)\rfloor+1\le N
\qquad(1\le c\le15).
```

In each row, the number of positive even slopes is at most $K$. Dropping
the favorable denominator digit sums in (8) therefore leaves
$v_2(F(N/2))\ge0$. The even base indices are ordinary integral values;
direct evaluation at $N=1,3,5,7$ finishes the finite base.

For auditability, the row data $(K,e,c_{\max};v_2(N=1,3,5,7))$, where $e$
is the number of positive even slopes and $c_{\max}$ is their largest
half-slope, are

```text
A295456  (10,2,15; 10,32,53,72)   A295458  (10,2,15; 10,32,53,72)
A295460  (12,2,15; 12,38,63,86)   A295465  ( 8,1,15;  8,26,43,58)
A295468  ( 8,2,15;  8,26,43,58)   A295470  ( 2,2,10;  3, 8,12,17)
A295471  ( 2,1,10;  3, 8,12,17)   A295475  ( 6,1,10;  7,20,32,45)
A295477  ( 4,1,12;  5,14,22,31)   A295479  ( 6,2,12;  7,20,32,45)
A295481  ( 6,2,12;  7,20,32,45)
```

The theorem consequently proves every one of the eleven half-index
integrality conjectures and its complete adjacent cubic tower for $p\ge5$.

The four still-visible fractional variants have denominators three or four:
A295456 and A295458 at $N/3$, and A295460 and A295477 at $N/4$. They require
a denominator-$q$ analogue of the midpoint argument and are not claimed here.

## Verification and source boundary

Run

```text
python verification/related/verify_bober_half_index_integrality.py
```

The checker verifies the eleven parity tests, the odd-prime translated
Landau identity, the binary digit-sum identity and bound, exact half-index
values, integrality, and adjacent towers. Finite checks are regression
evidence; the proof above is the general argument.

Bober's classification is the integrality input for the ordinary ratios.
The fractional-index conjectures are sourced to the approved OEIS comments
listed in the Bober packet. No assertion of literature priority is made.
