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
\(1\le r\le p-2\) be odd.  Then

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
nontrivial range, not merely at \(p=7\).

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
write it as \(t(p-1)\).  For \(1\le t\le r-1\), Lucas' theorem gives

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

and \(p-t>p-r-2\).  Hence every interior term in (10) vanishes modulo
\(p^2\).  Since \(i^q=1\), only the two endpoints remain:

```math
\mathcal G_q(p)
\equiv2(p-1)S_q
\equiv-2pB_q
\pmod {p^2}.
\tag{12}
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
\tag{13}
```

## 4. Assembly

From \(h^2=ip^2/2\), equations (7), (9), and (12) give

```math
\mathcal G_n(p)
\equiv
-\frac{i\,p^3}{2}n(n-1)B_q
\pmod {p^4}.
\tag{14}
```

Modulo \(p\),

```math
n(n-1)\equiv r(r+1).
```

Substitution of (13) into (14) proves (1).  Taking \(r=1\) gives

```math
\mathcal G_{p-1}(p)\equiv-i\,p^3B_{p-3}\pmod {p^4},
```

and proves the equivalent form (2).  Taking \(r=p-2\) proves (3).

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
- the universal counterexample (3)

for every inert prime through \(199\) by default, and through \(503\) with
`--extended`.

Run:

```text
python verification/related/verify_gaussian_angular_residue.py
python verification/related/verify_gaussian_angular_residue.py --extended
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
