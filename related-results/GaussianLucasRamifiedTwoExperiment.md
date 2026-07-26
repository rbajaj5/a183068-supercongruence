# The ramified prime in the Gaussian Lucas problem

## Status

**Exact computational discovery, now accompanied by a complete proof
candidate; no priority claim.**

The symbolic argument is in
[the ramified-prime theorem note](GaussianLucasRamifiedTwoTheorem.md).

The inert-prime proof does not apply at $p=2$, because

```math
2=-i(1+i)^2
```

in $\mathbb Z[i]$.

## Normalization

For $a\ge c\ge1$ and $b\ge d\ge1$, the rectangular Gaussian binomial used
here is

```math
Q(a,b;c,d)
=
\prod_{x=0}^{c-1}\prod_{y=0}^{d-1}
\frac{(a-x)+i(b-y)}{(x+1)+i(y+1)}.
\qquad\text{(0)}
```

Put $\varpi=1+i$ and

```math
R_{2,r}=
\frac{Q(2^rA,2^rB;2^rC,2^rD)}
{Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D)}.
```

## Ratio congruence

The companion proof candidate establishes, for every admissible rectangle and
every $r\ge2$,

```math
v_\varpi(R_{2,r}-1)\ge6r-3.
\qquad\text{(1)}
```

It now proves the exact refinement. Put

```math
g=A-C+i(B-D).
```

If $g\ne0$, then

```math
v_\varpi(R_{2,r}-1)
=
6r-3+v_\varpi(CDg).
\qquad\text{(1a)}
```

If $g=0$, then $R_{2,r}=1$.

The normalized leading residue is

```math
\frac{R_{2,r}-1}{\varpi^{6r-3}}
\equiv
CD(A+B-C-D)
\pmod\varpi.
\qquad\text{(2)}
```

Here $\mathbb Z[i]/(\varpi)=\mathbb F_2$, so the right side is an ordinary
parity condition. Equality in (1) occurs exactly when $C,D$ are odd and
$A+B-C-D$ is odd.

The level $r=1$ is a genuine boundary: its minimum ratio valuation on the
tested grids is $1$, rather than $3$.

## Difference rather than ratio

Let

```math
\Delta_{2,r}
=
Q(2^rA,2^rB;2^rC,2^rD)
-
Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D).
```

The companion parity induction proves

```math
v_\varpi(Q(A,B;C,D))\ge-1
```

and proves that the valuation is unchanged by simultaneous scaling of all
four parameters by a power of $2$. Consequently, for $r\ge2$,

```math
v_\varpi(\Delta_{2,r})\ge6r-4.
\qquad\text{(3)}
```

Because $\varpi^2$ is associated to $2$, (3) is the same as divisibility by
$2^{3r-2}$. Equality in (3) requires both equality in (1) and
$v_\varpi(Q(2^{r-1}A,2^{r-1}B;2^{r-1}C,2^{r-1}D))=-1$.

## Concrete examples at $r=2$

The rectangle $(A,B;C,D)=(1,2;1,1)$ is sharp. Direct evaluation of (0)
gives

```math
Q(2,4;2,2)=\frac{1+21i}{2},
\qquad
Q(4,8;4,4)=\frac{2642393+1166061i}{50},
```

and hence

```math
R_{2,2}-1
=
\frac{1043024-2089392i}{425}.
```

After removing the predicted power,

```math
\frac{R_{2,2}-1}{(1+i)^9}
=
\frac{-32699-97888i}{425},
```

which is a unit at $1+i$. Thus
$v_{1+i}(R_{2,2}-1)=9=6\mathbin{\cdot}2-3$. The corresponding difference
also attains its bound:

```math
\frac{\Delta_{2,2}}{(1+i)^8}
=
\frac{82574+36423i}{25},
\qquad
v_{1+i}(\Delta_{2,2})=8.
```

Strictly higher valuation is common. For $(A,B;C,D)=(2,2;1,1)$,

```math
Q(4,4;2,2)=30,
\qquad
Q(8,8;4,4)=\frac{317781086}{65},
```

and

```math
v_{1+i}(R_{2,2}-1)=10>9.
```

Here

```math
v_{1+i}\!\left(CD(A-C+i(B-D))\right)=1,
```

so the exact formula (1a) gives $9+1=10$.

## Exact data

On the 27-rectangle grid with parameters at most $3$, the difference
valuation distributions were:

| Scale | Distribution of $v_\varpi(\Delta_{2,r})$ |
| --- | --- |
| $r=1$ | minimum $0$ |
| $r=2$ | minimum $8=6r-4$ |
| $r=3$ | minimum $14=6r-4$ |
| $r=4$ | minimum $20=6r-4$ |
| $r=5$ | minimum $26=6r-4$ |

The full distribution shifts upward by exactly $6$ at each step from
$r=2$ onward.

The leading criterion (2) was also checked for every rectangle with
$A,B\le6$ at $r=2$ and $r=3$: 810 exact checks, with no mismatch. Of these,
72 of 405 ratio cases at each scale attained $6r-3$ (about $17.8\%$), and
36 of 405 difference cases at each scale attained $6r-4$ (about $8.9\%$).
Thus the lower bound is demonstrably sharp, but a randomly chosen small
rectangle more often has strictly higher valuation.

The exact refinement (1a) received a separate stress test:

- $5{,}940$ rectangles at $r=2$, with $A,B\le12$;
- $2{,}925$ rectangles at $r=3$, with $A,B\le10$;
- $1{,}232$ rectangles at $r=4$, with $A,B\le8$;
- $564$ targeted high-valuation cases through $r=5$; and
- $1{,}100$ additional deterministic random cases with $A,B\le100$.

There were no mismatches. A targeted rectangle

```math
(A,B;C,D)=(16777218,16777218;2,2)
```

has

```math
v_{1+i}\!\left(CD(A-C+i(B-D))\right)=53
```

and attains the predicted excess at every tested scale.

The standard command below reproduces the 810-rectangle grid and the four
high-valuation scales. The larger stress campaign above was a separate exact
run; its harness has not yet been added to the standard command.

## Reproduction and review

Run:

```text
python verification/related/experiment_gaussian_lucas_scaling.py
```

The computation uses literal Gaussian-integer products and repeated exact
division by $1+i$.

The proof uses a mixed-block reciprocal-sum lift rather than multiplying the
rectangle by $1+i$. Its principal review targets are the explicit $r=2$
base calculation, the uniform logarithmic tail, and the parity induction for
the denominator bound.
