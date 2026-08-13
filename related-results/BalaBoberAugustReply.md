# Draft reply to Peter Bala, copying Paul Hanna

**Subject:** Re: Follow-up on the Bala supercongruence collection

Dear Peter,

Thank you for sending the Bober list. I am copying Paul and Alexander so that
the same thread contains the statements and our present status.

We checked all 52 ordinary ratios A295431--A295482. For every one of them, the
full adjacent congruence

```math
A(np^r)\equiv A(np^{r-1})\pmod {p^{3r}}
```

for $p\ge5$ follows from Bober's integrality result and classical
Jacobsthal--Kazandzidis scaling. Thus the passage from Zudilin's $r=1$ result
to arbitrary $r$ does not require a separate argument for each of the 52
records.

We also checked the fractional-index suggestions. Their odd-prime congruence
part has a uniform treatment by rational gamma-ratio scaling, but integrality
is a genuinely separate question. We have now completed the first such case:

```math
A295456(n/2)=A364176(n).
```

Writing its value as $B(n)$, the even indices are the original integral Bober
ratio,

```math
B(2m)=A295456(m),
```

and the half-integer gamma identity gives

```math
B(2m+1)=2^{20m+10}
\frac{(15m+7)!(4m+2)!}
     {(5m+2)!(12m+6)!(2m+1)!}.
```

Legendre's formula reduces integrality of the remaining ratio to
nonnegativity of

```math
\left\lfloor\frac{15m+7}{d}\right\rfloor
+\left\lfloor\frac{4m+2}{d}\right\rfloor
-\left\lfloor\frac{5m+2}{d}\right\rfloor
-\left\lfloor\frac{12m+6}{d}\right\rfloor
-\left\lfloor\frac{2m+1}{d}\right\rfloor.
```

This expression is periodic in $m$ modulo $d$. Writing $5m+2=qd+s$ reduces
it to the five cases $q=0,1,2,3,4$; its value in every case is exactly $0$ or
$1$. This proves A364176 integral for every $n$. The rational gamma-ratio
scaling theorem then gives its full conjectured $p^{3r}$ tower for every
$p\ge5$.

The proof and the complete Bober packet are here:

- [A364176 affine-Landau proof](https://github.com/rbajaj5/a183068-supercongruence/blob/main/related-results/A364176AffineLandauTower.md)
- [Bober 52-record packet](https://github.com/rbajaj5/a183068-supercongruence/blob/main/related-results/BoberSporadicFactorialRatioPacket.md)

The exact checker performs 501,908 tests of the formulas, floor reduction,
Legendre valuations, and sample towers. We use those checks only to catch
transcription errors; the finite five-case calculation above is the proof.
We would particularly appreciate your assessment of the odd-index identity
and the affine floor lemma.

For completeness, here is the current status of the three groups you
identified in your July 31 message:

1. The A008793/A352656 superfactorial direction is now proved in the more
   general $N\times N\times cN$ symmetric-box family, including the binary
   case and the full modulus $p^{4r}$.
2. The enhanced linear combinations and products of Apéry numbers have been
   reduced exactly to three linear adjacent-defect congruences. Those three
   arithmetic statements remain open.
3. The paired congruences for A363984 and A376459--A376466 remain open; we
   have recorded their formulas but do not yet have a common proof.

Of the 15 fractional-index formulas currently visible in the Bober packet,
A364176 and A364183 are therefore closed completely. The rational $p$-adic
transfer is available for all 15, and the other 13 global integrality statements remain
the active queue. We have not made a literature-priority claim for the new
affine floor argument.

Best,

Ravi

cc: Paul Hanna; Alexander Burns
