# Adjacent-binomial supercongruences for the meander rows

**Status:** complete elementary proof candidate for the three conjectures on
[A198060](https://oeis.org/A198060), after correcting the evident exponent
typo in its third conjecture; in particular it proves the named towers on
[A198256](https://oeis.org/A198256) and
[A198258](https://oeis.org/A198258)

This note proves one theorem for every row of the meander array.  It also
explains a prime-range feature which otherwise looks accidental: the quartic
row starts at `p = 5`, whereas the sextic row includes `p = 3`, because the
unit-shell residue contains the factor `d/4`, where `d` is the binomial
degree.

The third conjecture on A198060 currently prints `n*p*(r-1)-1` on its
right-hand side.  At `r = 1` that gives the index `-1`, so the statement is
not literally well formed.  Throughout this note we use the only adjacent
level interpretation compatible with the other two records:

```math
np^r-1\longmapsto np^{r-1}-1.
```

## 1. One sequence for every row

For an integer `d >= 1`, put

```math
M_d(N)=
\sum_{k=0}^{N-1}\sum_{j=0}^{d-1}
 \binom{N-1}{k}^{d-j}\binom{N-1}{k+1}^{j}
\qquad(N\geq1).
\tag{1}
```

The entry `T(m,N-1)` of A198060 is `M_{m+1}(N)`.  Indeed, if
`x=(N)/(k+1)`, then the two inner sums in the OEIS definition reduce to

```math
\sum_{i=0}^{m}(-1)^i(1-x)^i
=\sum_{i=0}^{m}(x-1)^i,
```

and `x-1=(N-1-k)/(k+1)`.  Multiplication by
`binom(N-1,k)^(m+1)` gives (1).

The theorem is as follows.

### Theorem 1 (meander-row towers)

Let `d,N,r` be positive integers and let `p` be an odd prime.

1. Every row has the Gauss tower

   ```math
   M_d(np^r)\equiv M_d(np^{r-1})\pmod {p^r}.
   \tag{2}
   ```

2. If `d` is odd, then

   ```math
   M_d(p^r)\equiv 2^{p^r-1}\pmod {p^2}.
   \tag{3}
   ```

3. If `d` is even and `p >= 5`, then

   ```math
   M_d(np^r)\equiv M_d(np^{r-1})\pmod {p^{3r}}.
   \tag{4}
   ```

4. Congruence (4) also holds at `p = 3` whenever `3 | d`.

Parts 1--3 are exactly the three intended conjectures on A198060 after
putting `d=m+1`.  Part 4 proves the extra ternary claim on A198258.  The
prime restriction is real: for `d=4`,

```math
M_4(3)-M_4(1)=46-1=45,
\qquad v_3(45)=2<3.
\tag{5}
```

## 2. Symmetric adjacent-binomial form

For `0 <= t <= N`, set

```math
L_N(t)=\binom{N-1}{t-1},\qquad
R_N(t)=\binom{N-1}{t},\qquad
D_N(t)=L_N(t)+R_N(t)=\binom Nt.
\tag{6}
```

We use the convention that a binomial outside its ordinary range is zero.
Define the homogeneous polynomial

```math
H_d(X,Y)=\frac{X^d+Y^d}{2}
          +\sum_{j=1}^{d-1}X^{d-j}Y^j.
\tag{7}
```

Reflection `t -> N-t` interchanges `L_N(t)` and `R_N(t)`.  Symmetrizing
(1), including its zero endpoint, therefore gives the exact identity

```math
M_d(N)=\sum_{t=0}^{N}H_d(L_N(t),R_N(t)).
\tag{8}
```

Two elementary polynomial facts drive all three congruences:

```math
\begin{array}{ll}
d\text{ even}:&H_d(X,Y)=(X+Y)^2J_d(X,Y),\quad
J_d(X,-X)=\dfrac d4X^{d-2},\\[6pt]
d\text{ odd}:&H_d(X,Y)=(X+Y)K_d(X,Y),\quad
K_d(X,-X)=\dfrac12X^{d-1}.
\end{array}
\tag{9}
```

They follow by putting `Y=tX` in (7): at `t=-1` the resulting polynomial
has a double zero for even `d` and a simple zero for odd `d`; its first two
derivatives give the displayed values.  The coefficients lie in
`Z[1/2]`, which is harmless at every odd prime.

For `p` not dividing `t`, (6) and (9) immediately give

```math
\begin{array}{ll}
d\text{ even}:&p^{2r}\mid H_d(L_{np^r}(t),R_{np^r}(t)),\\
d\text{ odd}:&p^r\mid H_d(L_{np^r}(t),R_{np^r}(t)).
\end{array}
\tag{10}
```

This already disposes of the unit indices for the Gauss congruence (2).

## 3. The divisible indices

We may assume `p` does not divide `n`: otherwise absorb `v_p(n)` into the
level, obtaining a stronger modulus.  Put `N=np^r`, `t=p^s u`, with
`p` not dividing `u` and `s>=1`, and define

```math
c=\frac{\binom Nt}{\binom{N/p}{t/p}}.
```

The elementary identities

```math
L_N(t)=\frac tN\binom Nt,
\qquad
R_N(t)=\frac{N-t}{N}\binom Nt
\tag{11}
```

show exactly, not just congruentially, that

```math
(L_N(t),R_N(t))
=c\,(L_{N/p}(t/p),R_{N/p}(t/p)).
\tag{12}
```

Jacobsthal's binomial congruence gives

```math
v_p(c-1)\ge
\begin{cases}
r+2s,&s\le r,\ p\ge5,\\
3r,&s\ge r,\ p\ge5,
\end{cases}
\tag{13}
```

and the same bounds with the right side lowered by one when `p=3`.
When `d` is even, (9) and (11) give

```math
v_p\bigl(H_d(L_{N/p}(t/p),R_{N/p}(t/p))\bigr)
\ge2(r-s)
\tag{14}
```

for `s<=r`.  Homogeneity, (12), (13), and (14) now show term by term that

```math
H_d(L_N(t),R_N(t))
\equiv H_d(L_{N/p}(t/p),R_{N/p}(t/p))
\pmod {p^{3r}}
\tag{15}
```

for `p>=5`.  At `p=3`, the lost power is restored when `3|d`, since
`v_3(c^d-1)>=v_3(c-1)+v_3(d)`.  The weaker modulus `p^r` follows for
every `d` and every odd `p`.  Thus only the unit indices remain for the
cubic statement.

## 4. The unit shell and the factor `d/4`

We use the signed shifted-binomial descent

```math
(-1)^t\binom{np^r-1}{t}
\equiv
(-1)^{\lfloor t/p\rfloor}
\binom{np^{r-1}-1}{\lfloor t/p\rfloor}
\pmod {p^r}.
\tag{16}
```

This is the product-splitting lemma used by Beukers and recorded as
Lemma 5.4 in Straub's multivariate Apéry paper.  If `p` does not divide
`t`, the two floors of `t/p` and `(t-1)/p` agree, while the signs differ.
Consequently

```math
L_N(t)\equiv-R_N(t)\pmod {p^r}.
\tag{17}
```

For even `d`, equations (9), (11), and (17) give

```math
H_d(L_N(t),R_N(t))
\equiv
\frac{N^2}{t^2}\frac d4 R_N(t)^d
\pmod {p^{3r}}.
\tag{18}
```

Because `d` is even, `R_N(t)^d` itself has the unsigned Cartier descent
modulo `p^r` obtained from (16).  The standard reciprocal-square block
sum is

```math
\sum_{\substack{1\le u<p^s\\p\nmid u}}u^{-2}
\equiv0\pmod {p^s}\qquad(p\ge5).
\tag{19}
```

The usual block-induction lemma therefore makes the sum on the right of
(18), after removing `N^2`, divisible by `p^r`.  This proves (4).

At `p=3`, the corresponding sum is divisible by `3^{s-1}`.  One quick
induction groups the units modulo `3^s` by their residue modulo
`3^{s-1}`; each residue has three lifts.  If `3|d`, the factor `d` in
(18) supplies the missing power at every block level.  This proves the
ternary extension.

## 5. The odd-degree quadratic residue

Let `d` be odd.  The divisible-index comparison (15), now needed only
modulo `p^2`, shows for `r>=2` that

```math
M_d(p^r)\equiv M_d(p^{r-1})\pmod {p^2}.
\tag{20}
```

It remains to calculate `M_d(p)`.  The two endpoints in (8) contribute
one.  For `1<=t<p`, (9), (11), and (16) give

```math
H_d(L_p(t),R_p(t))
\equiv\frac p{2t}(-1)^{t-1}\pmod {p^2}.
\tag{21}
```

Finally,

```math
\sum_{t=1}^{p-1}\frac{(-1)^{t-1}}t
\equiv2\frac{2^{p-1}-1}{p}\pmod p.
\tag{22}
```

Indeed, reduce
`binom(p,t) = (p/t) binom(p-1,t-1)` modulo `p^2` and sum over `t`.
Equations (21)--(22) yield

```math
M_d(p)\equiv1+p\frac{2^{p-1}-1}{p}=2^{p-1}\pmod {p^2}.
```

Since `p^r-1` and `p-1` are congruent modulo `p(p-1)`, Euler's theorem
also gives `2^(p^r-1) == 2^(p-1) (mod p^2)`.  This completes (3).

## 6. The two named rows

For `d=4`, (9) specializes to

```math
H_4(X,Y)=\frac12(X+Y)^2(X^2+Y^2).
```

Reflection in (8) therefore proves the formerly conjectural identity

```math
M_4(n+1)=\sum_{k=0}^{n}
\binom{n+1}{k}^2\binom nk^2.
\tag{23}
```

This is A198256 Conjecture 1, while Theorem 1(3) proves its complete
`p^(3r)` tower for `p>=5`.

For `d=6`,

```math
H_6(X,Y)=\frac12(X+Y)^2(X^4+X^2Y^2+Y^4).
```

Theorem 1(3)--(4) proves the A198258 tower for every prime `p>=3`.

## 7. Verification and source boundary

The exact checker
[`verify_meander_adjacent_binomial_towers.py`](../verification/related/verify_meander_adjacent_binomial_towers.py)
verifies:

- the original OEIS formula, the adjacent-binomial form, and the symmetric
  form against each other;
- the displayed initial terms of A198256 and A198258;
- all three A198060 congruence families over finite parameter boxes;
- the extra ternary family and the sharp quartic failure (5);
- the polynomial factorizations and the reciprocal-block valuations used
  in the proof.

The proof uses only Pascal's identity, Jacobsthal scaling, the shifted
binomial descent, and finite reciprocal sums.  The shifted descent and the
block-induction organization are stated in:

- A. Straub, [*Multivariate Apéry numbers and supercongruences of rational
  functions*](https://arxiv.org/abs/1401.0854), Lemmas 5.4 and 5.6.

No claim of literature priority is made.  The exact matching of this
meander family to the theorem above is the repository's contribution and
still needs independent review.
