# Exact dyadic orientation lifts

## Status and source boundary

This note proves an elementary \(2\)-adic lemma that makes the lifting
phenomenon in Roe and Turturean's Remark C.7 completely explicit.

The source is David Roe and David Turturean,
[*A Presentation of the Absolute Galois Group of \(\mathbb Q_2\)*][RT],
especially Appendix C.5 and Remark C.7. Their paper supplies the motivating
orientation equation. The theorem below is a quantitative sharpening of that
remark, not a correction of their main classification theorem. No claim of
literature novelty is made here.

[RT]: https://roed314.github.io/gq2/paper.pdf

## The orientation equation

Let \(X\in\mathbb Z_2\) be the Hensel lift determined by

\[
X^3+2X^2+1=0,\qquad X\equiv5\pmod 8,
\]

and put

\[
\eta=-\frac13.
\]

Both \(X\) and \(\eta\) lie in \(1+4\mathbb Z_2\). At precision \(2^k\), the
orientation condition is

\[
X^e\equiv\eta\pmod {2^k}.
\]

### Theorem (exact orientation lift)

There is a unique \(\alpha\in\mathbb Z_2\) such that

\[
X^\alpha=\eta.
\]

For every \(k\ge3\),

\[
X^e\equiv\eta\pmod {2^k}
\quad\Longleftrightarrow\quad
e\equiv\alpha\pmod {2^{k-2}}.
\]

If \(e_k\) denotes the representative in
\(\{0,\ldots,2^{k-2}-1\}\), then

\[
e_{k+1}\in\{e_k,\ e_k+2^{k-2}\}.
\]

Thus each new level either preserves the current representative or appends
one new high binary digit. The modulus of the exponent class doubles at every
level.

Finally, \(\alpha\) is not an ordinary integer. Consequently the compatible
finite-level solutions do define a \(2\)-adic exponent, but they cannot all
come from one fixed finite exponent.

## Proof

The defining congruence gives

\[
v_2(X-1)=2,\qquad v_2(X+1)=1.
\]

For \(j\ge1\), the \(2\)-adic lifting-the-exponent formula therefore gives

\[
v_2\!\left(X^{2^j}-1\right)
=v_2(X-1)+v_2(X+1)+j-1
=j+2.
\]

The same conclusion at \(j=0\) is just \(v_2(X-1)=2\). Hence the order of
\(X\) modulo \(2^k\), inside \(1+4\mathbb Z/2^k\mathbb Z\), is exactly
\(2^{k-2}\). That group also has \(2^{k-2}\) elements, so \(X\) generates it.
There is therefore one and only one exponent class modulo \(2^{k-2}\)
mapping to \(\eta\).

Reduction from level \(k+1\) to level \(k\) makes these classes compatible.
Their inverse limit is a unique \(\alpha\in\mathbb Z_2\). The two lifts of a
class modulo \(2^{k-2}\) are exactly

\[
e_k\quad\text{and}\quad e_k+2^{k-2},
\]

which proves the binary lifting rule. The usual \(2\)-adic exponentiation on
\(1+4\mathbb Z_2\), or equivalently continuity of the finite-level
isomorphisms, gives \(X^\alpha=\eta\).

It remains to exclude \(\alpha\in\mathbb Z\). Let \(K=\mathbb Q(X)\). Since
\(X\) has minimal polynomial \(t^3+2t^2+1\),

\[
N_{K/\mathbb Q}(X)=-1.
\]

If \(X^n=-1/3\) for an integer \(n\), taking norms would give

\[
(-1)^n=N_{K/\mathbb Q}(-1/3)=-\frac1{27},
\]

which is impossible. Thus no fixed finite exponent solves every congruence.
\(\square\)

## What Remark C.7 does and does not show

The finite congruences are perfectly compatible and converge in the profinite
sense. The obstruction is not a failure of inverse-limit compactness.
Instead, the limiting \(2\)-adic exponent is outside the discrete set of
ordinary integer exponents.

Accordingly, the phrase that representatives “grow like” a power of \(2\)
should be read as growth of the available exponent modulus, not monotone
growth of the least nonnegative representative. A representative can remain
unchanged for several levels before acquiring another high binary digit.

This is a useful boundary example for lifting arguments: levelwise solvability
plus compatibility produces a profinite solution, but an additional
closedness or bounded-complexity argument is needed to recover a finite
discrete witness.

## Relation to the supercongruence program

This theorem does not imply a new congruence for A183068. Its relevance is
architectural: the same dyadic discipline appears when a congruence class
lifts through successively doubled moduli. Exact order, compatibility, and
the distinction between a profinite limit and a finite witness must be
checked separately.

The accompanying exact checker constructs the Hensel root and all exponent
classes through precision \(2^{32}\):

[`verify_gq2_orientation_lifts.py`](../verification/related/verify_gq2_orientation_lifts.py).
