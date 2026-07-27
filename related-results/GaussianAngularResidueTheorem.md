# A cubic angular residue for Gaussian square power sums

**Status:** complete proof candidate with exact checks; conventional review
and a literature-priority search are pending.

## 1. Result

For an odd prime \(p\), put

```math
\mathcal G_n(p)=
\sum_{a=1}^{p-1}\sum_{b=1}^{p-1}(a+bi)^n\in\mathbb Z[i].
```

Kalinin and Zottor conjectured that, when \(p\ge7\) is inert in
\(\mathbb Z[i]\), every odd multiple of \(p-1\) has \(p\)-adic valuation
exactly \(3\).  The numerical counterexample \(p=7,r=5\) was recorded in
[the first power-sum note](GaussianPowerSumConjectures.md).  The following
formula identifies the entire first angular residue and turns that example
into a counterexample family.

### Theorem 1 (cubic angular residue)

Let \(p\ge7\) be prime with \(p\equiv3\pmod4\), and let
\(1\le r\le 2p-1\) be odd.  Then

```math
\mathcal G_{r(p-1)}(p)
\equiv
-i\,p^3\binom{r+2}{3}B_{p-3}
\pmod {p^4}.
\tag{1}
```

Equivalently,

```math
\mathcal G_{r(p-1)}(p)
\equiv
\binom{r+2}{3}\mathcal G_{p-1}(p)
\pmod {p^4}.
\tag{2}
```

In particular,

```math
\mathcal G_{(p-2)(p-1)}(p)\equiv0\pmod {p^4}
\tag{3}
```

for every prime \(p\ge7\) with \(p\equiv3\pmod4\).  Thus the printed
constant-valuation conjecture fails for every inert prime in its first
nontrivial range, not merely at \(p=7\).  The same vanishing also occurs
at \(r=p\) and \(r=2p-1\).

When \(p\nmid\operatorname{num}(B_{p-3})\), equation (1) also gives the exact
criterion

```math
v_p\!\left(\mathcal G_{r(p-1)}(p)\right)=3
\quad\Longleftrightarrow\quad
p\nmid r(r+1)(r+2)
\tag{4}
```

within the stated range.  Without the Bernoulli nonvanishing hypothesis,
(1) remains valid but does not determine the exact valuation.

The cubic factor in (1) is an angular packet: quarter-turn symmetry removes
every Taylor mode below order two, and Kummer congruence reduces the surviving
radial power sum to \(B_{p-3}\).

## 2. Quarter-turn filtering

Let

```math
D=\{a+bi:1\le a,b\le p-1\}
```

and consider the affine quarter-turn

```math
T(z)=iz+p.
\tag{5}
```

It permutes \(D\), has center

```math
h=\frac{p}{1-i}=\frac{p(1+i)}2,
\tag{6}
```

and every orbit has four elements.  Write \(z=h+w\).  Since
\(T^t(z)=h+i^tw\), summing a power around an orbit kills every term except
those whose exponent of \(w\) is divisible by \(4\).

Put

```math
n=r(p-1),\qquad q=n-2.
```

Because \(p\equiv3\pmod4\) and \(r\) is odd, one has
\(n\equiv2\pmod4\) and \(q\equiv0\pmod4\).  The first surviving Taylor
term is therefore the term containing \(h^2\).  All later terms contain
at least \(h^6\) and hence at least \(p^6\).  Consequently,

```math
\mathcal G_n(p)
\equiv
\binom n2h^2
\sum_{z\in D}(z-h)^q
\pmod {p^4}.
\tag{7}
```

The shift can be removed modulo \(p^2\).  Indeed,

```math
\sum_{z\in D}(z-h)^q
\equiv
\mathcal G_q(p)-qh\,\mathcal G_{q-1}(p)
\pmod {p^2}.
\tag{8}
```

Neither \(q-1\) nor \(q\) is divisible by \(p-1\).  The standard power-sum
filter gives \(\mathcal G_{q-1}(p)\equiv0\pmod p\), so the second term in
(8) vanishes modulo \(p^2\).  Thus

```math
\sum_{z\in D}(z-h)^q\equiv\mathcal G_q(p)\pmod {p^2}.
\tag{9}
```

## 3. The radial residue

Write

```math
S_m=\sum_{a=1}^{p-1}a^m.
```

The binomial decomposition is

```math
\mathcal G_q(p)=
\sum_{j=0}^q
\binom qj i^jS_jS_{q-j}.
\tag{10}
```

If neither \(j\) nor \(q-j\) is divisible by \(p-1\), both power sums in
(10) are divisible by \(p\).  If exactly one is divisible by \(p-1\),
write it as \(t(p-1)\).

Suppose first that \(1\le r\le p-2\).  For \(1\le t\le r-1\), Lucas'
theorem gives

```math
\binom{r(p-1)-2}{t(p-1)}\equiv0\pmod p
\tag{11}
```

because, in base \(p\),

```math
r(p-1)-2=(r-1)p+(p-r-2),
\qquad
t(p-1)=(t-1)p+(p-t),
```

and \(p-t>p-r-2\).

There is a second Lucas range.  Write \(r=p+s\), where \(s\) is even and
\(2\le s\le p-3\).  Now

```math
q=p^2+(s-2)p+(p-s-2)
\tag{12}
```

in base \(p\).  An interior multiple of \(p-1\) has one of two forms.
For \(1\le t\le p-1\),

```math
t(p-1)=(t-1)p+(p-t).
```

Lucas nonvanishing would require both \(t\le s-1\) and \(t\ge s+2\).
For \(t=p+u\), where \(0\le u\le s-1\), the case \(u=0\) has middle
digit \(p-1>s-2\); when \(u\ge1\),

```math
t(p-1)=p^2+(u-2)p+(p-u),
```

and Lucas nonvanishing would require \(u\ge s+2\).  Hence every interior
term with \(j\equiv0\pmod {p-1}\) again vanishes modulo \(p^2\); the
terms with \(q-j\equiv0\pmod {p-1}\) follow by the symmetry
\(\binom qj=\binom q{q-j}\).

For every nonboundary \(r\) covered above, \(i^q=1\) and only the two
endpoints remain:

```math
\mathcal G_q(p)
\equiv2(p-1)S_q
\equiv-2pB_q
\pmod {p^2}.
\tag{13}
```

The second congruence is the first term of Faulhaber's formula.  Kummer's
congruence applies because

```math
q=r(p-1)-2\equiv p-3\pmod {p-1},
```

and gives

```math
B_q
\equiv
\frac{q}{p-3}B_{p-3}
\equiv
\frac{r+2}{3}B_{p-3}
\pmod p.
\tag{14}
```

The two omitted boundary values are \(r=p\) and \(r=2p-1\).  The
power-sum filter and (9) give
\(\sum_{z\in D}(z-h)^q\equiv0\pmod p\).  In the first case \(p\mid n\),
and in the second \(p\mid n-1\), so \(\binom n2\) is also divisible by
\(p\).  Equation (7) is therefore zero modulo \(p^4\).  This agrees with
(1), since
\(\binom{r+2}{3}\) is divisible by \(p\) at both boundary values.

## 4. Assembly

Away from the two boundary values, \(h^2=ip^2/2\) and equations (7),
(9), and (13) give

```math
\mathcal G_n(p)
\equiv
-\frac{i\,p^3}{2}n(n-1)B_q
\pmod {p^4}.
\tag{15}
```

Modulo \(p\),

```math
n(n-1)\equiv r(r+1).
```

Substitution of (14) into (15) proves (1).  Taking \(r=1\) gives

```math
\mathcal G_{p-1}(p)\equiv-i\,p^3B_{p-3}\pmod {p^4},
```

and proves the equivalent form (2).  Taking \(r=p-2\) proves (3).

The upper limit \(2p-1\) is a real boundary for this formula, not merely
the limit of the proof.  At the next odd multiplier \(r=2p+1\), interior
Lucas terms can survive.  For example, at \(p=7,r=15\),

```math
\mathcal G_{90}(7)\equiv2058i\pmod {7^4},
\qquad
-i\,7^3\binom{17}{3}B_4\equiv1372i\pmod {7^4}.
\tag{16}
```

Thus (1) cannot be extended unchanged to all odd \(r\).

## 5. Fourier interpretation

The map \(T\) generates the cyclic group \(C_4\).  Orbit summation is the
projection onto the trivial Fourier character of \(C_4\).  Since
\(n\equiv2\pmod4\), translating to the fixed center moves that projection
to the second Taylor coefficient.  The factor
\(\binom{r+2}{3}\) is therefore not an accidental interpolation: it is the
product of

1. the second angular mode, contributing \(r(r+1)\); and
2. the radial Kummer shift, contributing \(r+2\).

This is a precise radial/angular decomposition in the Gaussian plane.

## 6. Exact checks

The companion script checks:

- equation (1);
- the equivalent rank-one law (2);
- the base Bernoulli residue; and
- the three universal zeros \(r=p-2,p,2p-1\).

for every inert prime through \(199\) by default, and through \(251\) with
`--extended`.  It tests every odd \(1\le r\le2p-1\), as well as the
first-outside-range failure \((p,r)=(7,15)\).  The default run comprises
2,197 residue checks and 69 universal zeros; the extended run comprises
3,348 residues and 84 zeros.  An arbitrary prime bound can be requested
with `--limit`; the direct exhaustive checker has cubic-time growth in that
bound.

Run:

```text
python verification/related/verify_gaussian_angular_residue.py
python verification/related/verify_gaussian_angular_residue.py --extended
python verification/related/verify_gaussian_angular_residue.py --limit 503
```

The computations are regression evidence, not a substitute for specialist
review.

## 7. Source and priority

The conjecture being corrected is Conjecture 2 of:

- N. Kalinin and F. S. Zottor,
  *A \(p\)-adic (\(p\equiv3\pmod4\)) depth-\(5\) supercongruence for
  Gaussian \(p\)-th power sums over a square*,
  [arXiv:2602.00206](https://arxiv.org/abs/2602.00206), 2026.

The source already uses Bernoulli power-sum expansions for a different
special exponent.  The cubic residue formula (1), its quarter-turn proof,
and the universal counterexample family (3) were not located in the source.
A broader literature-priority search remains necessary before claiming
novelty.
