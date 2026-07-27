# Gaussian base change for Jacobian collision supercongruences

## Status

This note combines the weighted-lift Jacobian collision program with the
split/inert arithmetic of Gaussian primes.

The organizing theorem is prime-ideal theoretic. If a good prime ideal
\(\mathfrak p\) has ramification index \(e\) and residue degree \(f\), then
the complete Frobenius-corrected collision tower has exact
\(\mathfrak p\)-adic adjacent valuation

\[
2ef(r-1).
\]

For a construction defined over \(\mathbf Z\), base change to the residue
field replaces rational Frobenius \(F\) by \(F^f\). Thus a split Gaussian
prime sees \(F\), while an inert Gaussian prime sees \(F^2\). In the
degree-four weighted lift, squaring Frobenius kills the entire quadratic
Artin obstruction. This gives an uncorrected adjacent supercongruence at
every good inert Gaussian prime.

This is a **structural follow-on**, not the solution of a named open
conjecture. Prime-ideal decomposition, Frobenius base change, and the
behavior of permutation cycles under powering are standard. Their
application to these collision towers and the explicit degree-four
split/inert law are new to this repository. Literature priority remains
provisional.

## 1. Prime-ideal form of the collision tower

Let \(K\) be a number field with ring of integers \(\mathcal O_K\), and let
\(\mathfrak p\) lie above the rational prime \(p\). Write

\[
(p)=\mathfrak p^e\mathfrak a,
\qquad
[\mathcal O_K/\mathfrak p:\mathbf F_p]=f,
\qquad
Q=N\mathfrak p=p^f.
\tag{1}
\]

Let a normalized weighted-lift Keller map have good reduction at
\(\mathfrak p\). Assume that its tangent divided-difference curve is smooth
of genus \(g\), and that its finite infinity, diagonal, and bitangency
schemes have good étale reduction.

Over \(\mathbf F_{Q^r}\), write

\[
\tau_{\mathfrak p,r}
=Q^r+1-\#\mathcal C(\mathbf F_{Q^r})
\tag{2}
\]

and

\[
B_{\mathfrak p,r}
=2\tau_{\mathfrak p,r}
+c_{\mathfrak p,r}
-\delta Q^r.
\tag{3}
\]

The all-degree collision theorem gives

\[
\mathcal V_{\mathfrak p,r}
=(Q^r-1)
\left(
Q^{2r}+B_{\mathfrak p,r}
\right).
\tag{4}
\]

Define the complete Tate correction

\[
\widehat{\mathcal V}_{\mathfrak p,r}
=
\mathcal V_{\mathfrak p,r}
-(Q^r-1)B_{\mathfrak p,r}.
\tag{5}
\]

## 2. The prime-ideal theorem

### Theorem 1

For every \(r\ge2\),

\[
\widehat{\mathcal V}_{\mathfrak p,r}
=Q^{3r}-Q^{2r}
\tag{6}
\]

and

\[
\boxed{
v_{\mathfrak p}\left(
\widehat{\mathcal V}_{\mathfrak p,r}
-\widehat{\mathcal V}_{\mathfrak p,r-1}
\right)
=2ef(r-1).}
\tag{7}
\]

For every fixed \(k\ge1\), the set of levels

\[
\left\{
r\ge2:
\mathfrak p^k\mid
\mathcal V_{\mathfrak p,r}
-\mathcal V_{\mathfrak p,r-1}
\right\}
\tag{8}
\]

is eventually periodic and has rational density.

### Proof

Equation (6) follows from (4) and (5). Its adjacent difference is

\[
Q^{2r-2}
\left(
Q^{r+2}-Q^2-Q^{r-1}+1
\right).
\tag{9}
\]

The second factor is congruent to \(1\) modulo \(\mathfrak p\), so it is a
\(\mathfrak p\)-adic unit. Since \(Q=p^f\) and
\(v_{\mathfrak p}(p)=e\),

\[
v_{\mathfrak p}(Q^{2r-2})
=(2r-2)ef,
\]

which proves (7).

The curve trace satisfies a recurrence of order \(2g\) over
\(\mathcal O_K\). Modulo \(\mathfrak p^k\), its state lies in a set of size
at most

\[
\left|\mathcal O_K/\mathfrak p^k\right|^{2g}
=Q^{2gk}.
\]

The finite schemes contribute periodic Frobenius-permutation counts.
Combining the recurrence state with the finite-orbit phase gives a finite
deterministic state machine. The argument of the fixed-precision Frobenius
automaton theorem then proves eventual periodicity and rational density in
(8). \(\square\)

The factor \(ef\) has two different sources: \(f\) changes the size of the
residue field, while \(e\) changes the normalization of the prime-ideal
valuation.

## 3. Frobenius powering under base change

Suppose now that the map and all collision data are defined over
\(\mathbf Z\), and that \(p\) is a rational prime of good reduction. Let
\(F_p\) denote geometric Frobenius over \(\mathbf F_p\).

### Theorem 2

After base change to the residue field
\(\mathcal O_K/\mathfrak p=\mathbf F_{p^f}\), every Frobenius packet is
obtained by replacing

\[
F_p\longmapsto F_p^f.
\tag{10}
\]

In particular:

1. the curve trace at level \(r\) is the rational-prime trace at level
   \(fr\);
2. a finite Frobenius orbit of length \(d\) splits into
   \(\gcd(d,f)\) orbits of length
   \[
   \frac d{\gcd(d,f)};
   \tag{11}
   \]
3. an automaton cycle of length \(t\) becomes a cycle whose length divides
   \[
   \frac t{\gcd(t,f)}.
   \tag{12}
   \]

If the displayed cycle is the actual orbit of the initial state, equality
holds in (12).

### Proof

The arithmetic Frobenius of \(\mathbf F_{p^f}\) acts as the \(f\)-th power
of the arithmetic Frobenius of \(\mathbf F_p\); the same statement holds
with geometric Frobenius after inversion. This proves the trace statement.

On a cycle of length \(d\), the permutation \(F_p^f\) advances by \(f\)
places. It therefore has \(\gcd(d,f)\) cycles, each of length (11). The same
cyclic-group calculation gives (12). \(\square\)

Thus splitting behavior acts directly on the obstruction automaton. It is
not an analogy between pictures of primes and collision graphs.

## 4. Specialization to Gaussian primes

Take \(K=\mathbf Q(i)\). For an odd rational prime:

\[
\begin{array}{c|c|c|c}
p\bmod4&\text{behavior in }\mathbf Z[i]&e&f\\ \hline
1&\text{split }(p)=\pi\overline\pi&1&1\\
3&\text{inert }(p)\text{ prime}&1&2.
\end{array}
\tag{13}
\]

The ramified prime \(2=-i(1+i)^2\) has \((e,f)=(2,1)\), but the
weighted-lift collision theorem used here assumes odd residue
characteristic. The dyadic case therefore requires a separate geometric
analysis and is not claimed in this note.

For every good odd Gaussian prime, Theorem 1 gives

\[
v_\pi\left(
\widehat{\mathcal V}_{\pi,r}
-\widehat{\mathcal V}_{\pi,r-1}
\right)
=
\begin{cases}
2r-2,&p\equiv1\pmod4,\\
4r-4,&p\equiv3\pmod4.
\end{cases}
\tag{14}
\]

At a split prime the two conjugate reductions agree for a map defined over
\(\mathbf Z\). At an inert prime the residue field is
\(\mathbf F_{p^2}\), so the collision tower samples only the even rational
extension levels.

## 5. Degree four: inert primes remove the Artin obstruction

For Gallagher's degree-four weighted lift,

\[
\mathcal V_4(q)
=(q-1)\left(q^2+\kappa(q)\right),
\tag{15}
\]

where

\[
\kappa(q)
=3+\chi_q(2)+2\chi_q(-2)+2\chi_q(6).
\tag{16}
\]

Every nonzero element of \(\mathbf F_p\) is a square in
\(\mathbf F_{p^{2r}}\). Hence

\[
\kappa(p^{2r})=8
\qquad(r\ge1).
\tag{17}
\]

### Theorem 3

Let \(p\ge7\) be an inert Gaussian prime, so \(p\equiv3\pmod4\). Put

\[
W_r=\mathcal V_4(p^{2r}).
\tag{18}
\]

Then

\[
W_r=(p^{2r}-1)(p^{4r}+8)
\tag{19}
\]

and, for every \(r\ge2\),

\[
\boxed{
v_p(W_r-W_{r-1})=2r-2.}
\tag{20}
\]

After the complete Tate correction

\[
\widehat W_r=W_r-8(p^{2r}-1),
\tag{21}
\]

one has

\[
\boxed{
v_p(\widehat W_r-\widehat W_{r-1})=4r-4.}
\tag{22}
\]

### Proof

Equations (19) and (21) follow from (15) and (17). In the raw difference,
the lowest-order term is

\[
8p^{2r-2}(p^2-1),
\]

which has exact valuation \(2r-2\). The remaining terms have valuation at
least \(4r-4\). This proves (20).

The corrected sequence is

\[
\widehat W_r=p^{6r}-p^{4r},
\]

so (22) is the inert case of (14). \(\square\)

The result can be compared with the split tower over \(\mathbf F_{p^r}\).
For split primes \(p\equiv1\pmod4\), the existing degree-four theorem gives

\[
v_p\left(
\mathcal V_4(p^r)-\mathcal V_4(p^{r-1})
\right)
=
\begin{cases}
r-1,&p\equiv1\pmod {24},\\
0,&p\equiv5,13,17\pmod {24}.
\end{cases}
\tag{23}
\]

The complete correction has valuation \(2r-2\). Thus:

| Gaussian behavior | Raw degree-four tower | Complete correction |
| --- | --- | --- |
| split, \(p\equiv1\pmod {24}\) | \(r-1\) | \(2r-2\) |
| split, \(p\equiv5,13,17\pmod {24}\) | \(0\) | \(2r-2\) |
| inert, \(p\equiv3\pmod4\) | \(2r-2\) | \(4r-4\) |

The inert base field does two things simultaneously: it freezes the
quadratic Artin packet and doubles the Tate scale.

## 6. The common abstract-algebra mechanism

The Gaussian Lucas results and the Jacobian collision results do not yet
follow from one identical theorem. Their local objects differ:

- Gaussian Lucas uses normalized products in a local ring and estimates
  logarithmic moments;
- Jacobian collisions use point-count zeta functions and Frobenius traces.

They nevertheless share a precise prime-ideal architecture:

1. choose a prime ideal and its residue degree;
2. split the quantity into a stable leading contribution and a local
   obstruction packet;
3. let Frobenius or scaling act on the obstruction;
4. remove or control that packet; and
5. read the valuation from the surviving leading term.

Theorem 1 is the collision-side version of this architecture. It explains
why abstract algebra helps both programs without pretending that their
hard local lemmas are interchangeable.

## 7. Verification

The checker
[`verify_gaussian_base_change_collisions.py`](../verification/related/verify_gaussian_base_change_collisions.py)
verifies:

1. the general \(2ef(r-1)\) prime-ideal valuation law on a grid of
   \((e,f,p,r)\);
2. the orbit-powering formula (11);
3. every split/inert degree-four valuation in (20)--(23) for all odd primes
   below \(200\);
4. direct quadratic-extension collision checks already supplied by the
   degree-four checker; and
5. the complete correction at both split and inert primes.

Run:

```text
python verification/related/verify_gaussian_base_change_collisions.py
```

## 8. References and priority boundary

- A. Gallagher,
  [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained),
  for the weighted-lift construction.
- [All-degree weighted-lift collision theorem](WeightedLiftCollisionSynthesis.md).
- [Frobenius obstruction automata](FrobeniusObstructionAutomata.md).
- J. S. Milne,
  [Values of zeta functions of varieties over finite fields](https://www.jmilne.org/math/articles/1986a.pdf),
  for the standard finite-field Frobenius and zeta-function setting.

The phrase
[“Gaussian Moments Conjecture”](https://arxiv.org/abs/1506.05192)
also occurs in work on the Jacobian Conjecture, but there “Gaussian” refers
to Gaussian integration, not to the arithmetic of \(\mathbf Z[i]\). It is
not a source for the split/inert theorem above.

A targeted search found no earlier statement of the degree-four inert
collision law (20) or of the prime-ideal valuation formula in this
weighted-lift setting. This is preliminary evidence only, not a priority
certificate.
