# Dixon--Legendre half-binomial towers

**Status:** complete elementary proof candidate; exact checks pass.
Independent review and literature-priority work remain.

This note proves together the full supercongruence conjectures recorded
on [OEIS A275652](https://oeis.org/A275652) and
[OEIS A275654](https://oeis.org/A275654).  The proof applies to every
member of the Dixon--Legendre family below.

## 1. The coefficient family

For integers $a\geq3$ and $N\geq0$, put $D_a(0)=1$ and, for $N\geq1$,

```math
D_a(N)
=
\sum_{k=0}^{N}
\binom{(a-1)N-k-1}{N-k}\binom{aN}{k}^{2}.
\tag{1}
```

Every summand is an integer.  Equivalently,

```math
D_a(N)
=
[x^N](1-x)^{2N}
P_{aN}\left(\frac{1+x}{1-x}\right),
\tag{2}
```

where $P_j$ is the Legendre polynomial of degree $j$.
Indeed, the standard identity

```math
(1-x)^m P_m\left(\frac{1+x}{1-x}\right)
=
\sum_{k=0}^{m}\binom{m}{k}^{2}x^k
```

followed by multiplication by $(1-x)^{-(a-2)N}$ gives (1) after
extracting the coefficient of $x^N$.

### Theorem 1 (Dixon--Legendre tower)

For every integer $a\geq3$, every prime $p\geq5$, and all positive
integers $n,r$,

```math
D_a(np^r)\equiv D_a(np^{r-1})\pmod {p^{3r}}.
\tag{3}
```

The cases $a=3$ and $a=5$ are A275652 and A275654.  Thus Theorem 1
proves both named adjacent-level conjectures.  The even cases $a=4$ and
$a=6$ recover the already-recorded companion congruences A275653 and
A275655, whose factorial products involve only integral arguments.  The
half-binomial lemma is what supplies the missing odd-parameter cases.

The exclusions at $2$ and $3$ are genuine for both named cases:

```math
\begin{array}{c|cc}
&v_2(D_a(2)-D_a(1))&v_3(D_a(3)-D_a(1))\\ \hline
a=3&1&2\\
a=5&1&2.
\end{array}
\tag{4}
```

## 2. Dixon evaluation

Reverse the summation in (1), writing $j=N-k$.  After taking out
$\binom{aN}{N}^2$, use

```math
\frac{\binom{aN}{N-j}}{\binom{aN}{N}}
=
\frac{(-1)^j(-N)_j}{((a-1)N+1)_j}.
```

The remaining sum is

```math
{}_3F_2\left[
\begin{matrix}
(a-2)N,-N,-N\\
(a-1)N+1,(a-1)N+1
\end{matrix};1
\right].
\tag{5}
```

This is Dixon's terminating evaluation

```math
{}_3F_2\left[
\begin{matrix}
A,B,C\\
1+A-B,1+A-C
\end{matrix};1
\right]
=
\frac{
\Gamma(1+A/2)
\Gamma(1+A-B)
\Gamma(1+A-C)
\Gamma(1+A/2-B-C)}
{\Gamma(1+A)
\Gamma(1+A/2-B)
\Gamma(1+A/2-C)
\Gamma(1+A-B-C)}
\tag{6}
```

with $A=(a-2)N$ and $B=C=-N$.  Simplification gives

```math
D_a(N)
=
\frac{
\Gamma(aN+1)
\Gamma((a+2)N/2+1)
\Gamma((a-2)N/2+1)}
{\Gamma((a-2)N+1)
\Gamma(aN/2+1)^2
\Gamma(N+1)^2}.
\tag{7}
```

In binomial notation this is the especially useful identity

```math
D_a(N)
=
\binom{aN}{2N}
\binom{(a+2)N/2}{N}
\binom{2N}{N}
\binom{aN/2}{N}^{-1}.
\tag{8}
```

Formula (1), rather than (8), supplies integrality.

## 3. Half-binomial scaling

For an integer $c\geq2$, define the $p$-integral rational number

```math
B_c(N)=\binom{cN/2}{N}.
\tag{9}
```

### Lemma 2 (half-binomial unit block)

Let $p\geq5$ be prime and let $N=pM$.  If $e=v_p(N)$, then

```math
\frac{B_c(N)}{B_c(M)}\equiv1\pmod {p^{3e}}.
\tag{10}
```

#### Proof

Use the product

```math
B_c(N)
=
\frac1{2^N N!}
\prod_{j=0}^{N-1}(cN-2j).
\tag{11}
```

Because $p$ is odd, the factors divisible by $p$ are exactly those with
$p\mid j$.  They reproduce the product for $B_c(M)$, while the divisible
factors of $N!$ reproduce $M!$.  The remaining powers of $2$ cancel
against the factors $-2j$.  Since $N-M$ is even, the signs cancel as
well.  Let $U$ be the set of integers $j$ with $1\leq j<N$ and
$p\nmid j$.  Hence the exact identity

```math
\frac{B_c(N)}{B_c(M)}
=
\prod_{j\in U}
\left(1-\frac{cN}{2j}\right).
\tag{12}
```

Put $P=p^e$ and write

```math
S_\nu
=
\sum_{j\in U}\frac1{j^\nu}.
```

Complete unit blocks modulo $P$ satisfy

```math
S_1\equiv0\pmod {P^2},
\qquad
S_2\equiv0\pmod P.
\tag{13}
```

For the second congruence, multiplication by a unit whose square is not
$1$ modulo $p$ permutes the units.  For the first, pair $u$ with $P-u$
and reduce the result to the inverse-square sum.  Translating a complete
block by a multiple of $P$ preserves both congruences to the displayed
precisions.

Expanding (12), the linear term is a multiple of $NS_1$, the quadratic
term is

```math
\left(\frac{cN}{2}\right)^2
\frac{S_1^2-S_2}{2},
\tag{14}
```

and every term of degree at least three contains $N^3$.  All nonconstant
terms are therefore divisible by $P^3=p^{3e}$.  This proves (10).
$\square$

## 4. Proof of Theorem 1

Set $N=np^r$ and $M=N/p$.  The two ordinary binomial factors in (8)
satisfy the classical Ljunggren--Jacobsthal--Kazandzidis scaling
congruence:

```math
\frac{\binom{aN}{2N}}{\binom{aM}{2M}}
\equiv1\pmod {p^{3r}},
\qquad
\frac{\binom{2N}{N}}{\binom{2M}{M}}
\equiv1\pmod {p^{3r}}.
\tag{15}
```

Lemma 2 gives the same congruence for the adjacent quotients of
$B_{a+2}$ and $B_a$.  Each quotient is a $p$-adic unit, so its inverse
has the same congruence.  Dividing (8) at level $N$ by (8) at level $M$
therefore gives

```math
\frac{D_a(N)}{D_a(M)}\equiv1\pmod {p^{3r}}.
\tag{16}
```

Finally, $D_a(M)$ is an integer by (1), so multiplication proves (3).
$\square$

## 5. What has and has not been proved

This note proves:

- the complete $p^{3r}$ conjecture on A275652;
- the complete $p^{3r}$ conjecture on A275654; and
- the same theorem for every integer parameter $a\geq3$ in (1).

It does not claim:

- an extension to $p=2$ or $p=3$;
- that arbitrary rational factorial ratios satisfy a cubic tower; or
- literature priority for the family theorem.

Targeted searches by the two OEIS identifiers and their exact factorial
formulas located the conjecture records but did not locate a full
adjacent-level proof.  That is routing evidence, not a priority
certificate.

## 6. References

- [OEIS A275652](https://oeis.org/A275652) and
  [OEIS A275654](https://oeis.org/A275654), including Bala's formulas
  and the stated adjacent-level conjectures.
- [OEIS A275653](https://oeis.org/A275653) and
  [OEIS A275655](https://oeis.org/A275655), the even-parameter
  companions recovered by the family theorem.
- [NIST DLMF index entry for Dixon's
  sum](https://dlmf.nist.gov/idx/D), for the classical
  ${}_3F_2(1)$ evaluation used in Section 2.
- [Meštrović, *Wolstenholme's theorem: Its Generalizations and
  Extensions in the last hundred and fifty years
  (1862--2012)*](https://arxiv.org/abs/1111.3057), for the classical
  binomial scaling congruence used in (15).

## 7. Verification

Run:

```text
python verification/related/verify_dixon_legendre_towers.py
```

The checker verifies the finite-sum, terminating-hypergeometric, and
binomial forms; the exact half-binomial factorization (12); the two
unit-block harmonic congruences; the family tower over a range of
$a,n,p,r$; the named initial values; and the sharp small-prime failures.
