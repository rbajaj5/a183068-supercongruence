# The enhanced prime congruence for A212334

**Status:** complete elementary proof of the conjectured prime-level
`p^5` congruence for every prime `p>=5`; for `p>=7`, the remaining
higher-level claim is an exact consequence of the three unresolved Apéry
defect relations in the campaign ledger

The OEIS record [A212334](https://oeis.org/A212334) gives, for `N>=1`,

```math
a(N)=\sum_{k=0}^{N-1}
\binom Nk\binom{N-1}{k}\binom{N+k-1}{k}^{\!2}.
\tag{1}
```

It conjectures

```math
a(p)\equiv1\pmod {p^5}
\tag{2}
```

for every prime `p>=5`, and a stronger adjacent pure-prime tower at the
higher levels.  This note proves (2) and places the higher claim inside the
existing rank-three Apéry defect packet.

## 1. Prime-level theorem

### Theorem 1

For every prime `p>=5`,

```math
\boxed{a(p)\equiv1\pmod {p^5}.}
\tag{3}
```

#### Proof

The term `k=0` in (1) is `1`.  For `1<=k<p`, the elementary product
formulas for the three binomial factors give the exact identity

```math
\begin{aligned}
&\binom pk\binom{p-1}{k}\binom{p+k-1}{k}^{\!2}\\
&\qquad=-\frac{p^3}{k^3}
 \left(1-\frac pk\right)
 \prod_{j=1}^{k-1}\left(1-\frac{p^2}{j^2}\right)^2.
\end{aligned}
\tag{4}
```

All denominators are `p`-adic units.  Reducing (4) modulo `p^5` yields

```math
\binom pk\binom{p-1}{k}\binom{p+k-1}{k}^{\!2}
\equiv-\frac{p^3}{k^3}+\frac{p^4}{k^4}pmod {p^5}.
\tag{5}
```

If `p>=7`, then

```math
\sum_{k=1}^{p-1}\frac1{k^3}\equiv0\pmod {p^2},
\qquad
\sum_{k=1}^{p-1}\frac1{k^4}\equiv0\pmod p.
\tag{6}
```

For the second congruence, use the ordinary power sum in
`F_p^times`.  For the first, pair `k` with `p-k`:

```math
\frac1{k^3}+\frac1{(p-k)^3}
\equiv-\frac{3p}{k^4}\pmod {p^2},
```

and apply the second congruence to the half-system of representatives.
Summing (5) proves (3) for `p>=7`.

At the only excluded power-sum boundary, direct exact arithmetic gives

```math
a(5)-1=87500=28\cdot5^5.
\tag{7}
```

This completes every prime `p>=5`.  QED

## 2. The higher defect is already in the Apéry packet

Let `W=A005259` be the fourth-order Apéry sequence and, at adjacent
pure-prime levels `N=p^r`, `M=p^(r-1)`, write

```math
\gamma_r=W(N)-W(M),
\qquad
\delta_r=W(N-1)-W(M-1).
\tag{8}
```

The identity printed on A212334 is

```math
a(N)=\frac{W(N)+7W(N-1)}{12},
\tag{9}
```

so its adjacent defect is `(gamma_r+7 delta_r)/12`.  With the notation of
[the Apéry defect packet](AperyRankOneDefectPacket.md), one has the exact
linear identity

```math
\begin{aligned}
5(\gamma_r+7\delta_r)
={}&(5\gamma_r-14\alpha_r)
 +7(5\delta_r-2\beta_r)\\
&+14(\alpha_r+\beta_r).
\end{aligned}
\tag{10}
```

Consequently, for `p>=7`, the three relations `R_1`, `R_2`, and `R_3` in
that packet imply the full enhanced A212334 tower after division by the
units `5` and `12`.  Thus A212334 does not introduce a fourth defect
direction.

At `p=5`, identity (10) loses one power when divided by `5`.  The exact
higher-level A212334 congruence at that prime therefore remains a separate
boundary obligation; neither this note nor the three relations as presently
stated prove it.

## 3. Verification and source boundary

The exact checker
[`verify_a212334_enhanced_prime.py`](../verification/related/verify_a212334_enhanced_prime.py)

1. compares (1) with the initial OEIS values;
2. verifies the product identity (4) term by term;
3. checks the two harmonic congruences in (6);
4. verifies (3) through a broad finite prime range, including the exact
   `p=5` boundary; and
5. checks (9)--(10) and sampled higher defects exactly.

The finite checks are transcription control.  The proof of Theorem 1 is
the product calculation (4)--(7).  No literature-priority claim is made.
