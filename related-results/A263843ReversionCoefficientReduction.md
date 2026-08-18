# The complete A263843 reversion supercongruence family

**Status:** complete elementary proof candidate for every prime $p\geq3$;
exact checks pass; independent review pending.

**Source boundary:** [OEIS A263843](https://oeis.org/A263843) conjectures the
full family below for every prime $p\geq3$.  The note proves that family,
including the named sequence at the exceptional prime $3$.  The final ternary
step uses a cancellation between the quadratic and cubic exponential terms;
neither term has the required valuation separately.

## 1. Reversion and the proposed family

Let $Y(x)$ be the unique formal series with zero constant term satisfying

```math
Y=x\frac{(1+Y)^3}{1-Y},
\tag{1}
```

and set

```math
H(x)=\frac{Y(x)}x=1+4x+23x^2+\cdots.
\tag{2}
```

For a positive integer $c$, an integer $s$, and $N\geq1$, define

```math
B_{c,s}(N)=[x^{cN}]H(x)^{sN}.
\tag{3}
```

The OEIS page asks for

```math
B_{c,s}(np^r)\equiv B_{c,s}(np^{r-1})\pmod {p^{3r}}
\tag{4}
```

for every prime $p\geq3$.

## 2. Exact Lagrange reduction

Put

```math
\phi(t)=\frac{(1+t)^3}{1-t},
\qquad d=c+s.
\tag{5}
```

Equation (1) is $Y=x\phi(Y)$ and (2) is $H=\phi(Y)$.  If $s\ne0$ and
$d\ne0$, Lagrange--Bürmann inversion gives

```math
\begin{aligned}
B_{c,s}(N)
&=\frac1{cN}[t^{cN-1}]
\frac{d}{dt}\bigl(\phi(t)^{sN}\bigr)\phi(t)^{cN}\\
&=\frac{s}{c+s}[t^{cN}]\phi(t)^{(c+s)N}.
\end{aligned}
\tag{6}
```

Thus

```math
B_{c,s}(N)=\frac{s}{d}
[t^{cN}](1+t)^{3dN}(1-t)^{-dN}.
\tag{7}
```

This is exactly the repository's coefficient-framing family, with the
parameters $(\alpha,\beta;c)=(3d,-d;c)$.

There are two elementary singular cases.  If $s=0$, then (3) is zero.  If
$d=0$, direct use of the first line of (6) gives

```math
B_{c,-c}(N)=-1-3(-1)^{cN-1}.
\tag{8}
```

For odd $p$, the right side is unchanged under $N\mapsto pN$, so its tower
is an equality.

## 3. Denominator primes do not cause a loss

Formula (7) contains a factor $1/d$, so simply quoting the coefficient-
framing theorem would lose powers when $p\mid d$.  The proof itself supplies
exactly the missing compensation.

Let

```math
A_d(N)=[t^{cN}](1+t)^{3dN}(1-t)^{-dN}.
\tag{9}
```

For $N=np^r$, the reduced Frobenius logarithm in the framing proof is

```math
L_p(t)=d\bigl(3V_p(t)+U_p(t)\bigr),
\tag{10}
```

where $U_p,V_p$ are the reduced logarithms used in
[the coefficient-framing theorem](CoefficientFramingCubicTower.md).  Write
$e=v_p(d)$.  The linear exponential term still vanishes exactly.  For
$p\geq5$, the reciprocal-square Cartier estimate and integration by parts
give the quadratic term valuation

```math
3r+2e,
\tag{11}
```

while every term of degree $h\geq3$ has valuation at least

```math
hr-v_p(h!)+he\geq3r+e.
\tag{12}
```

Consequently,

```math
v_p\bigl(A_d(np^r)-A_d(np^{r-1})\bigr)
\geq3r+v_p(d).
\tag{13}
```

Multiplying by $s/d$ in (7) loses at most $v_p(d)$ and proves (4) for every
$p\geq5$, including primes dividing $c+s$.

## 4. Closing the exact ternary boundary

At $p=3$, the general reciprocal-square estimate is one power weaker.  The
same calculation gives the quadratic budget

```math
3r-1+2v_3(d)
\tag{14}
```

before division by $d$.  Therefore (4) is already proved whenever
$3\mid d=c+s$.  Together with (8), this includes $d=0$ as an exact equality.

It remains to suppose that $d$ is a $3$-adic unit.  The apparent loss in
(14) is real for the quadratic term, but its leading residue cancels with
the cubic term.  The next two lemmas make that cancellation explicit.

### 4.1 The normalized quadratic and cubic Cartier terms

Keep the notation of the coefficient-framing proof, put

```math
W=3V_3+U_3,
\qquad
G(x)=\frac{(1+x)^{3d}(1-x)^{-d}}{x^c},
\tag{15}
```

and let $C_3(\sum a_jx^j)=\sum a_{3j}x^j$.  Direct convolution gives a
series $K_d\in\mathbb Z_3[[x]]$ such that

```math
C_3(d^2W^2)=xK_d'(x),
\qquad
K_d(x)\equiv d^2\frac{x}{1-x}\pmod3.
\tag{16}
```

Indeed, if

```math
H_T=\sum_{\substack{1\le j<T\\3\nmid j}}\frac1j,
\qquad
H_T^\pm=\sum_{\substack{1\le j<T\\3\nmid j}}
\frac{(-1)^{j+1}}j,
```

then

```math
[x^T]W^2=
\frac2T\left((1+9(-1)^T)H_T
+3(1+(-1)^T)H_T^\pm\right).
\tag{17}
```

Here is the normalized residue calculation in detail.  Write
$m=3^eu$, $3\nmid u$, and put $P=3^{e+1}$.  On one complete reduced block
define

```math
S_1=\sum_{\substack{1\le v<P\\3\nmid v}}\frac1v,
\qquad
S_2=\sum_{\substack{1\le v<P\\3\nmid v}}\frac1{v^2}.
```

Pairing $v$ with $P-v$ and using inversion on the units modulo $P$ gives

```math
S_1\equiv P S_2\pmod {P^2},
\qquad
S_2\equiv-\frac P3\pmod P.
\tag{18}
```

For the second congruence, inversion permutes the reduced residues, so it
is enough to sum their squares; subtracting the multiples of $3$ from
$1^2+\cdots+(P-1)^2$ gives the displayed residue.  In the first congruence,
pairing first gives $S_1\equiv-(P/2)S_2$; this equals $PS_2$ modulo $P^2$
because $v_3(S_2)=e$.

Now split the range defining $H_{3m}$ into the $u$ translated blocks
$aP+v$.  The expansion

```math
\frac1{aP+v}\equiv\frac1v-\frac{aP}{v^2}\pmod {P^2}
```

and (18) give

```math
H_{3m}\equiv
uS_1-P\frac{u(u-1)}2S_2
\equiv-3m^2\pmod {P^2}.
\tag{19}
```

If $3m$ is even, then $u$ is even.  The same block expansion with
alternating signs has block multipliers
$\sum_{a=0}^{u-1}(-1)^a=0$ and
$\sum_{a=0}^{u-1}a(-1)^a=-u/2$.  The alternating inverse-square block is
divisible by $P$: pair (v) with (P-v), whose alternating signs are
opposite while their inverse squares agree modulo (P).  Therefore

```math
H_{3m}^{\pm}\equiv0\pmod {P^2}.
\tag{20}
```

Substituting (19)--(20) into (17), separately according as $3m$ is odd or
even, gives

```math
\frac1m[x^{3m}]W^2\in\mathbb Z_3,
\qquad
\frac1m[x^{3m}]W^2\equiv1\pmod3.
\tag{21}
```

This is precisely (16).  Notice that (21) retains the normalized residue
which the coarser bound $v_3(H_T)\geq2v_3(T)-1$ discards.

The cubic term is simpler.  In $\mathbb F_3[[x]]$,

```math
W\equiv U_3\equiv\frac{x}{(1-x)^2}.
```

The Frobenius identity $f(x)^3=f(x^3)$ therefore gives

```math
C_3(d^3W^3)\equiv d^3\frac{x}{(1-x)^2}\pmod3.
\tag{22}
```

### 4.2 The leading defect formula

Write $N=n3^r$, $M=N/3$, initially with $3\nmid n$.  The exact reduced-log
identity is

```math
A_d(N)-A_d(M)
=\operatorname{CT}G(x^3)^M\bigl(\exp(NdW)-1\bigr).
\tag{23}
```

The linear term has zero constant coefficient.  Every exponential term of
degree at least four is divisible by $3^{3r}$, since

```math
jr-v_3(j!)\geq3r\qquad(j\geq4).
```

For the quadratic term, apply (16) and integrate by parts.  For the cubic
term, apply (22).  After division by the common factor $3^{3r-1}$, their
sum is

```math
\begin{aligned}
&\frac{n^3}{2}\operatorname{CT}G(x)^M
\left(-K_d(x)\frac{xG'(x)}{G(x)}
+d^3\frac{x}{(1-x)^2}\right)\\
&\quad\equiv
\frac{n^3d^2(d+c)}2
\operatorname{CT}\frac{x}{1-x}G(x)^M
\pmod3,
\end{aligned}
\tag{24}
```

because

```math
\frac{xG'(x)}{G(x)}
\equiv d\frac{x}{1-x}-c\pmod3.
```

Thus the only possible missing residue is completely explicit.

### 4.3 A Frobenius-descent coefficient lemma

Set

```math
T_{d,c}(M)=
\operatorname{CT}\frac{x}{1-x}G(x)^M
=[x^{cM-1}]\frac{(1+x)^{3dM}(1-x)^{-dM}}{1-x}.
\tag{25}
```

If $3\mid c$ and $3\nmid d$, then

```math
T_{d,c}(M)\equiv0\pmod3
\qquad(M\geq1).
\tag{26}
```

To prove this, first suppose $3\nmid M$ and put $A=dM$.  Modulo $3$, the
series in (25) is

```math
g(x)=(1+x^3)^A(1-x)^{-A-1}.
```

It satisfies

```math
(n+1)[x^{n+1}]g=(n+A+1)[x^n]g.
```

At $n=cM-1\equiv-1\pmod3$, the left multiplier is zero and the right
multiplier is the unit $A$, proving (26).  If $3\mid M$, Frobenius gives

```math
T_{d,c}(M)\equiv T_{d,c}(M/3)\pmod3.
```

Repeated descent reaches the unit case.

### 4.4 Completion of the ternary proof

Recall that $s=d-c$ and $B_{c,s}(N)=(s/d)A_d(N)$.  If $3\mid s$, the
factor $s/d$ supplies the one power missing from (14).  If $3\nmid s$,
then $c\not\equiv d\pmod3$.  There are only two possibilities:

- $3\mid c$, in which case (26) kills (24); or
- $c\equiv-d\pmod3$, in which case the factor $d+c$ kills (24).

Hence (24) always vanishes after multiplication by $s/d$, and (4) holds
at $p=3$.  If the original $n$ is divisible by $3$, absorb its valuation
into the level; the resulting modulus is stronger than the required
$3^{3r}$.  This completes the proof for every prime $p\geq3$.

## 5. Verification

Run

```text
python verification/related/verify_a263843_reversion_reduction.py
```

The exact checker verifies the published named values, the Lagrange formula
and its two singular cases, integrality across positive and negative slopes,
the full $p\geq5$ tower including denominator primes, the normalized
quadratic and cubic Cartier residues, the Frobenius-descent lemma, the
leading-defect formula (24), and the now-proved full ternary parameter grid.
