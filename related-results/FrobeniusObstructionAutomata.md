# Frobenius obstruction automata for weighted-lift collisions

## Status

This note extracts the finite-state theorem suggested by the degree-four
through degree-seven Jacobian-counterexample calculations.

For every good prime and every fixed \(p\)-adic precision, the levels at
which the raw collision sequence satisfies an adjacent congruence form an
eventually periodic set. Equivalently, their unary encodings form a regular
language. The density therefore exists and is rational. At precision \(p\),
the eventual period has a sharper bound obtained by deleting the
coefficients of the curve \(L\)-polynomial that vanish modulo \(p\).

After the complete Frobenius packet is removed, no automaton is needed: the
corrected sequence has the universal exact valuation \(2r-2\).

This is a **structural follow-on**, not the solution of a named open
conjecture. The rational-zeta/linear-recurrence input is standard. The
application to the weighted-lift collision tower, the fixed-precision
obstruction language, and the explicit higher-precision examples below are
new to this repository. Literature priority remains provisional.

## 1. The collision packet

Let \(F_\rho\) be a normalized weighted-lift Keller map over a finite field
of odd characteristic \(p\). Assume that:

1. the tangent divided-difference curve \(\mathcal C\) is smooth of genus
   \(g\);
2. the infinity, diagonal, and bitangency schemes are finite and étale; and
3. all coefficients and boundary strata have good reduction at \(p\).

Write

\[
\tau_r=p^r+1-\#\mathcal C(\mathbf F_{p^r})
\tag{1}
\]

and

\[
c_r=-2+2I_r+2D_r+H_r.
\tag{2}
\]

The all-degree collision theorem gives

\[
\mathcal V_r
=(p^r-1)\left(p^{2r}+B_r\right),
\qquad
B_r=2\tau_r+c_r-\delta p^r,
\tag{3}
\]

where \(\delta\in\{0,1\}\) is the boundary indicator.

Let

\[
P_{\mathcal C,p}(T)
=1+a_1T+\cdots+a_{2g}T^{2g}
\tag{4}
\]

be the numerator of the local zeta function of \(\mathcal C\). If its
reciprocal roots are \(\alpha_1,\ldots,\alpha_{2g}\), then

\[
\tau_r=\sum_{j=1}^{2g}\alpha_j^r.
\tag{5}
\]

Consequently, for \(r>2g\),

\[
\tau_r+a_1\tau_{r-1}+\cdots+a_{2g}\tau_{r-2g}=0.
\tag{6}
\]

Every finite étale scheme is a finite Frobenius permutation set. Hence
\(c_r\) is periodic. Let \(L\) be any common multiple of the orbit lengths
of the three finite schemes.

## 2. Fixed-precision automata

For \(k\ge1\), define the successful-level set

\[
\mathcal A_{p,k}
=
\left\{
r\ge2:
p^k\mid \mathcal V_r-\mathcal V_{r-1}
\right\}.
\tag{7}
\]

### Theorem 1

For every fixed \(k\ge1\), the set \(\mathcal A_{p,k}\) is eventually
periodic. In particular:

1. its natural density exists and is rational;
2. the unary language
   \[
   \{\,1^r:r\in\mathcal A_{p,k}\,\}
   \tag{8}
   \]
   is regular; and
3. after a finite prefix, membership is decided by a deterministic state
   machine with at most
   \[
   Lp^{2gk}
   \tag{9}
   \]
   states.

### Proof

Reduce the recurrence (6) modulo \(p^k\). The state

\[
S_r=(\tau_{r-2g+1},\ldots,\tau_r)
\in(\mathbf Z/p^k\mathbf Z)^{2g}
\tag{10}
\]

has at most \(p^{2gk}\) possible values, and (6) determines \(S_{r+1}\)
from \(S_r\). Every orbit of a map on a finite set is eventually periodic.

The finite correction \(c_r\) is periodic with period dividing \(L\).
Therefore the combined state

\[
(S_r,r\bmod L)
\tag{11}
\]

is eventually periodic and has at most \(Lp^{2gk}\) values.

For \(r\ge k+1\), both \(p^r\) and \(p^{r-1}\) vanish modulo \(p^k\).
Equation (3) then gives

\[
\mathcal V_r-\mathcal V_{r-1}
\equiv B_{r-1}-B_r\pmod {p^k}.
\tag{12}
\]

The right side is a function of two consecutive combined states. Thus the
truth value of (7) is eventually periodic. An eventually periodic subset
of the nonnegative integers is recognized by a finite unary automaton, and
its density is the number of accepting positions in one eventual period
divided by the period. \(\square\)

The theorem is effective: the recurrence coefficients, the first
\(2g\) traces, and the finite Frobenius orbit degrees produce the automaton
without counting points over further extension fields.

## 3. A sharper theorem modulo \(p\)

Put

\[
m=\max\{j:1\le j\le2g,\ a_j\not\equiv0\pmod p\},
\tag{13}
\]

with \(m=0\) if every \(a_j\) vanishes modulo \(p\).

### Theorem 2

If \(m>0\), then the trace sequence modulo \(p\) is periodic from the state
ending at \(r=2g\), with period

\[
t\le p^m-1.
\tag{14}
\]

Consequently, the raw obstruction pattern modulo \(p\) has eventual period
dividing

\[
\operatorname{lcm}(t,L),
\tag{15}
\]

and therefore at most \(L(p^m-1)\). If \(m=0\), then
\(\tau_r\equiv0\pmod p\) for every \(r>2g\), so only the finite packet
remains.

### Proof

Modulo \(p\), equation (6) reduces to the order-\(m\) recurrence

\[
\tau_r\equiv
-a_1\tau_{r-1}-\cdots-a_m\tau_{r-m}\pmod p.
\tag{16}
\]

Because \(a_m\ne0\), its companion transition is invertible on
\(\mathbf F_p^m\). The state ending at \(2g\) therefore lies on a cycle,
not on a proper tail. A nonzero cycle contains at most \(p^m-1\) nonzero
states; the zero state is fixed. Combining this trace cycle with the
period-\(L\) finite packet proves (15). \(\square\)

The order \(m\), rather than the geometric value \(2g\), is often small.
This is why a high-genus curve can still produce a short obstruction
automaton modulo its defining prime.

## 4. The universal corrected tower

Define

\[
\widehat{\mathcal V}_r
=\mathcal V_r-(p^r-1)B_r.
\tag{17}
\]

### Theorem 3

For every \(r\ge2\),

\[
\widehat{\mathcal V}_r=p^{3r}-p^{2r}
\tag{18}
\]

and

\[
\boxed{
v_p\left(
\widehat{\mathcal V}_r-\widehat{\mathcal V}_{r-1}
\right)=2r-2.}
\tag{19}
\]

### Proof

Equation (18) follows immediately from (3). Moreover,

\[
\widehat{\mathcal V}_r-\widehat{\mathcal V}_{r-1}
=p^{2r-2}
\left(
p^{r+2}-p^2-p^{r-1}+1
\right).
\tag{20}
\]

For \(r\ge2\), the factor in parentheses is congruent to \(1\) modulo
\(p\). This proves (19). \(\square\)

The raw and corrected statements have different meanings. The raw language
records the surviving curve and finite-orbit arithmetic. The corrected
tower removes exactly those packets and isolates the Tate contribution.

## 5. Two explicit automata

### Degree six at \(p=13\)

The genus-three example has

\[
P_{13}(T)=1+16T^2-26T^3+208T^4+2197T^6.
\tag{21}
\]

Modulo \(13\), this is \(1+3T^2\), so \(m=2\). The trace period is \(12\),
and the finite packet also has period \(12\). No adjacent pair of packet
values agrees. Therefore

\[
13\nmid\mathcal V_r-\mathcal V_{r-1}
\qquad(r\ge2).
\tag{22}
\]

At precisions \(13^k\), the trace-state periods observed directly from the
exact recurrence are

\[
12,\ 156,\ 2028,\ 26364
=12\cdot13^{k-1}
\qquad(1\le k\le4),
\tag{23}
\]

with state preperiods \(0,2,4,6\). Equation (22) already excludes every
higher raw divisibility condition.

### Degree seven at \(p=5\)

The genus-six example has

\[
\begin{aligned}
P_5(T)={}&1+2T^3+7T^4-16T^5-34T^6-80T^7\\
&+175T^8+250T^9+15625T^{12}.
\end{aligned}
\tag{24}
\]

Here \(m=6\). The trace period modulo \(5\) is \(39\), while the finite
packet modulo \(5\) has period \(4\). The raw automaton therefore has
period

\[
\operatorname{lcm}(39,4)=156.
\tag{25}
\]

It accepts \(28\) classes, giving density

\[
\frac{28}{156}=\frac7{39}.
\tag{26}
\]

The same recurrence gives the following higher-precision data.

| Precision | Trace-state preperiod | Trace period | Combined period | Accepting classes | Density |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(5\) | \(0\) | \(39\) | \(156\) | \(28\) | \(7/39\) |
| \(5^2\) | \(1\) | \(195\) | \(780\) | \(32\) | \(8/195\) |
| \(5^3\) | \(2\) | \(975\) | \(3900\) | \(40\) | \(2/195\) |
| \(5^4\) | \(3\) | \(4875\) | \(19500\) | \(55\) | \(11/3900\) |

These are exact recurrence computations, not point-count extrapolations.
They illustrate Theorem 1 at four successive \(5\)-adic resolutions.

## 6. Arithmetization and its limit

The automaton description gives a precise, modest form of arithmetized
syntax. At a fixed prime and precision, the question

\[
\text{“does level \(r\) satisfy the raw congruence?”}
\]

is encoded by membership of the unary word \(1^r\) in a regular language.
The automaton state is not metaphorical: it is the Frobenius-recurrence
state together with the finite-orbit phase.

This does **not** imply pseudorandomness, cryptographic hardness, or a
finite-state description uniform in the precision \(k\). The number of
available recurrence states grows with \(k\). What it supplies is an exact
decision procedure and a rational-density theorem at every fixed
resolution.

## 7. Verification

The checker
[`verify_frobenius_obstruction_automata.py`](../verification/related/verify_frobenius_obstruction_automata.py)
verifies:

1. Newton reconstruction and recurrence propagation for the genus-three
   and genus-six local \(L\)-polynomials;
2. the sharp modulo-\(p\) state orders \(m=2\) and \(m=6\);
3. trace periods and preperiods through \(13^4\) and \(5^4\);
4. the degree-six permanent obstruction;
5. all four degree-seven density rows; and
6. the universal corrected valuation at several primes and levels.

Run:

```text
python verification/related/verify_frobenius_obstruction_automata.py
```

## 8. References and priority boundary

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  for the weighted-lift construction.
- [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md),
  for the collision formula and zeta decomposition.
- [Degree-six genus-three packet](JacobianDegreeSixGenusThree.md) and
  [degree-seven genus-six packet](JacobianDegreeSevenGenusSix.md), for the
  explicit local data used above.

Rational local zeta functions yielding linear recurrences, and finite
recurrences modulo an integer yielding eventual periodicity, are standard
facts. A targeted search found no prior source applying them to classify
the successful levels of these weighted-lift collision congruences. This
is preliminary evidence only, not a novelty certificate.
