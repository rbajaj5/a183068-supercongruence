# Gaussian power sums: one conjecture proved and two corrected

**Status:** complete draft proof and exact counterexamples; unchecked by
Fable and not peer reviewed.

## 1. Source and definition

For an odd prime $p$, define

$$
\mathcal G_n(p)=
\sum_{a=1}^{p-1}\sum_{b=1}^{p-1}(a+bi)^n\in\mathbb Z[i],
\qquad
v_p(x+yi)=\min\{v_p(x),v_p(y)\}.
\tag{1}
$$

Kalinin and Zottor's 2026 preprint formulates three conjectures about
these sums.  This note proves their Conjecture 3, gives a counterexample
to Conjecture 2, and records that Conjecture 1 is contradicted by the
exceptional blocks already printed in the source.

## 2. The small-prime conjecture

### Theorem 1

For every integer $n\geq1$,

$$
v_3(\mathcal G_n(3))=
\begin{cases}
0,&n\equiv0\pmod4,\\
1+v_3(n),&n\equiv1\pmod4,\\
2+v_3(n)+v_3(n-1),&n\equiv2\pmod4,\\
2+v_3(n)+v_3(n-1)+v_3(n-2),&n\equiv3\pmod4,
\end{cases}
\tag{2}
$$

and

$$
v_5(\mathcal G_n(5))=
\begin{cases}
0,&n\equiv0\pmod4,\\
1+v_5(n),&n\equiv1\pmod4,\\
2+v_5(n)+v_5(n-1),&n\equiv2\pmod4,\\
3+v_5(n)+v_5(n-1)+v_5(n-2),&n\equiv3\pmod4.
\end{cases}
\tag{3}
$$

Thus Conjecture 3 of the source is true.

## 3. Proof at $p=3$

Put $\alpha=1+i$.  Directly from the four points in the square
$\{1,2\}^2$,

$$
\frac{2^n\mathcal G_n(3)}{\alpha^n}
=2^n+4^n+(3+i)^n+(3-i)^n=:K_n.
\tag{4}
$$

Both $2$ and $\alpha$ are $3$-adic units, so

$$
v_3(\mathcal G_n(3))=v_3(K_n).
\tag{5}
$$

Expanding every term around a fourth root of unity gives

$$
K_n=
\sum_{k=0}^n
\binom nk3^k
\left((-1)^{n-k}+1+i^{\,n-k}+(-i)^{\,n-k}\right).
\tag{6}
$$

Write $r$ for the residue of $n$ modulo $4$.

- If $r=0$, the $k=0$ bracket is $4$, so $K_n$ is a
  $3$-adic unit.
- If $r=1$, the first nonzero bracket occurs at $k=1$, and its
  contribution is
  $$
  12n.
  \tag{7}
  $$
- If $r=2$, the $k=0$ bracket vanishes and the $k=2$
  contribution is
  $$
  36\binom n2=18n(n-1).
  \tag{8}
  $$
- If $r=3$, the $k=1$ bracket vanishes and the $k=3$
  contribution is
  $$
  108\binom n3=18n(n-1)(n-2).
  \tag{9}
  $$

Each later nonzero term has strictly larger $3$-adic valuation than
the displayed leading term.  Indeed, dividing a term with index $k$
by its leading term leaves an integer product times, respectively,

$$
\frac{3^{k-1}}{k!},\qquad
\frac{3^{k-2}}{k!},\qquad
\frac{3^{k-2}}{k!}.
\tag{10}
$$

The later nonzero indices actually begin at $k=5,6,7$, respectively.
Already on the weaker ranges $k\geq3,4,5$, Legendre's formula gives
valuation at least $1$ for the three quantities in (10).  Therefore
the leading term cannot be cancelled, and (7)--(9) give exactly (2).

## 4. Proof at $p=5$

Let

$$
D=\{a+bi:1\leq a,b\leq4\}.
$$

The affine quarter-turn

$$
T(z)=iz+5
\tag{11}
$$

permutes $D$: if $z=a+bi$, then

$$
T(z)=(5-b)+ai.
$$

Its fixed center is

$$
h=\frac{5}{1-i}=\frac{5(1+i)}2.
\tag{12}
$$

The set $D$ is the disjoint union of four $T$-orbits.  Choose one
representative $z_j$ from each orbit and put $w_j=z_j-h$.  Since

$$
T^t(z_j)=h+i^tw_j,
$$

the sum around one orbit is

$$
\begin{aligned}
\sum_{t=0}^3(h+i^tw_j)^n
&=
\sum_{k=0}^n\binom nk h^kw_j^{\,n-k}
\sum_{t=0}^3i^{t(n-k)}\\
&=
4\sum_{\substack{0\leq k\leq n\\k\equiv n\ (4)}}
\binom nk h^kw_j^{\,n-k}.
\end{aligned}
\tag{13}
$$

Let $r\in\{0,1,2,3\}$ satisfy $n\equiv r\pmod4$.  Summing (13)
over the four orbits, the first possible term is

$$
4\binom nrh^r U_{n-r},
\qquad
U_q=\sum_{j=1}^4w_j^q.
\tag{14}
$$

The factor $U_q$ is always a $5$-adic unit when $q\geq0$ is
divisible by $4$.  For $q=0$, this is $U_0=4$.  For $q>0$,
take the representatives

$$
z_1=4+4i,\quad z_2=2+4i,\quad
z_3=2+i,\quad z_4=2+3i.
$$

Modulo $5$, $w_j\equiv z_j$, and

$$
z_1^4=z_4^4=1,\qquad
z_2^4=3+i,\qquad z_3^4=3-i.
\tag{15}
$$

The last two elements are idempotent modulo $5$.  Hence for every
positive multiple $q$ of $4$,

$$
U_q\equiv1+(3+i)+(3-i)+1\equiv3\pmod5.
\tag{16}
$$

Since $v_5(h)=1$, the valuation of (14) is

$$
r+v_5\left(\binom nr\right)
=r+\sum_{j=0}^{r-1}v_5(n-j),
\tag{17}
$$

because $r!$ is a $5$-adic unit.

It remains only to exclude cancellation by later terms.  Such a term
has $k=r+4s$ with $s\geq1$.  Relative to the scale of (14), its
additional valuation is at least

$$
(k-r)-v_5(k!/r!)\geq1.
\tag{18}
$$

The last inequality follows at once from Legendre's formula; here
$0\leq r\leq3$ and $k\geq r+4$.  Thus all later terms have strictly
larger valuation, (14) cannot be cancelled, and (3) follows.

## 5. The inert-prime conjecture is false

Conjecture 2 of the source asserts that, for $p\geq7$ with
$p\equiv3\pmod4$,

$$
v_p\left(\mathcal G_{r(p-1)}(p)\right)
=
\begin{cases}
0,&r\ \text{even},\\
3,&r\ \text{odd}.
\end{cases}
\tag{19}
$$

The first failure occurs already at

$$
p=7,\qquad r=5,\qquad n=30.
$$

Exact integer summation gives

$$
\mathcal G_{30}(7)
=-6264101156848215194673755568\,i,
\tag{20}
$$

and

$$
v_7\left(\mathcal G_{30}(7)\right)=5,
\tag{21}
$$

not $3$.  The quotient by $7^5$ is

$$
-372707869152627785724624\equiv2\pmod7,
$$

so the valuation in (21) is exact.

Further small failures include

$$
v_7(\mathcal G_{42}(7))=4,\qquad
v_{11}(\mathcal G_{90}(11))=4.
\tag{22}
$$

The normalized residue

$$
\frac{\mathcal G_{r(p-1)}(p)}{p^3}\pmod p
$$

vanishes systematically at $r\equiv0,-1,-2\pmod p$ in the tested
inert primes.  This explains why a constant valuation $3$ cannot be
correct, but the roots at $-1$ and $-2$ do not lift as the literal
integer factors $r+1$ and $r+2$.  A corrected all-$r$ valuation
formula remains open.

## 6. Conjecture 1 is inconsistent as printed

Conjecture 1 predicts, for $4\leq n\leq p-2$, the valuation cycle

$$
1,2,3,4
\tag{23}
$$

according to $n\bmod4$.  The same source later lists exceptional
blocks with cycle $2,3,4,5$, beginning with $(p,t)=(37,8)$.

The contradiction is independently visible at

$$
p=37,\qquad n=32:
\qquad
v_{37}(\mathcal G_{32}(37))=2,
\tag{24}
$$

where (23) predicts $1$.  The source relates these exceptional blocks
to irregular pairs

$$
p\mid\operatorname{num}(B_{4t}).
$$

Consequently, the mathematically meaningful replacement is to classify
the excess valuation in terms of Bernoulli divisibility, not to prove
Conjecture 1 verbatim.

## 7. Verification

The companion script performs:

1. recurrence-based exact modular checks of (2)--(3) through
   $n=100000$ by default, or $n=1000000$ with `--extended`;
2. exact-integer verification of (20)--(22);
3. a direct modular check of (24); and
4. verification of the four affine orbits and the unit calculation
   (15)--(16).

Run:

```text
python verification/related/verify_gaussian_power_sums.py
python verification/related/verify_gaussian_power_sums.py --extended
```

## 8. Provenance

The source is:

- N. Kalinin and F. S. Zottor, *A $p$-adic
  ($p\equiv3\pmod4$) depth-5 supercongruence for Gaussian $p$-th
  power sums over a square*, arXiv:2602.00206v2, 2026.

A targeted search on the exact conjecture titles and formulas found no
later proof or counterexample.  Because the preprint is recent and the
search is not exhaustive, priority should be checked again before
circulation.
