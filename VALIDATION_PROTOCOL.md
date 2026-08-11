# Validation, retirement, and priority protocol

**Effective date:** 2026-08-02.

This protocol turns model review and exact computation into measured evidence
rather than a collection of endorsements. It governs admission to the root
result index and rankings. It does not decide mathematical truth by vote.

## 1. Three-way validator calibration

A review verdict has three admissible values:

1. **supported** -- the supplied material is sufficient and the claim checks;
2. **refuted** -- a stated step, boundary, or conclusion fails; and
3. **insufficient information** -- the material does not support either of
   the first two verdicts.

A validator that never returns the third answer is not calibrated for this
repository. Agreement among models is not independent evidence when their
training data, prompts, or proof templates overlap.

Calibration is recorded by capability, not as one global score:

- proof-step verification;
- exact-computation verification;
- source and citation verification; and
- literature-priority assessment.

The suite must contain supported, refuted, and undecidable-from-the-packet
items. Recent or private held-out items are preferred to famous published
examples, which can measure recall rather than checking. Public seed examples
may be documented, but their answer keys are not blind tests. Rates are
reported with integer counts and uncertainty intervals; small samples are used
directionally, not as weights to three decimal places.

Known repository incidents provide public, non-blind seed material, including
the finite-range failures in the Kalinin packets and earlier source misses on
[OEIS A133907](https://oeis.org/A133907) and
[OEIS A079044](https://oeis.org/A079044). They do not replace a held-out
suite.

## 2. Two independent status axes

Every primary-ledger claim records two axes.

### Author-completeness axis

- **open gap** -- the author knows that a proof obligation remains;
- **apparently gapless candidate** -- the author believes every proof step is
  present; and
- **externally closed** -- a conventional specialist or publication has
  accepted the argument as complete.

### Audit axis

- **unaudited**;
- **machine-assisted exact-text audit**;
- **specialist reviewed**; or
- **published**.

The legacy phrase **complete unchecked draft** maps to **apparently gapless
candidate / unaudited**. It must not be read as external certification.
Source status and literature priority remain separate axes.

Every new entry also records an immutable **entry date**. The first commit
containing the claim controls; cosmetic edits do not reset the clock.

## 3. Retirement rule

An unaudited claim remains in the active primary review queue for 30 calendar
days from its entry date. At expiry it is moved to an archived or unindexed
area unless it has acquired an independent audit. The proof note and Git
history are preserved: retirement changes prominence, not provenance.

Legacy entries must acquire entry dates or be marked legacy by 2026-08-16.
New generated material that has not passed admission goes to
[`intake/`](intake/README.md), not `RESULT_INDEX.md` or `RANKINGS.md`.

## 4. Checker mutation evidence

A checker counts as evidence only after stating what nearby false claim it
rejects. Mutation classes should include, where applicable:

- changing the exponent or modulus by exactly one power;
- adding or deleting one exceptional prime;
- perturbing one coefficient or the final verified index;
- removing one integrality or nonvanishing hypothesis; and
- changing the tested domain.

Only near-miss mutants are informative. Each checker reports a kill count
`killed / attempted`, together with any surviving mutants. Range mutation is
mandatory: a prefix and an extended range are run separately. A conclusion
that changes when the range is extended is a boundary observation, not a
theorem certificate.

Mutation testing remains finite evidence. It does not prove the theorem whose
transcription it tests.

## 5. Named literature corpus

Every priority audit starts with a named corpus rather than an unstructured
search log:

1. the OEIS record, history, comments, formulas, programs, links, and
   cross-references for every sequence touched;
2. the originating paper and every cited source attached to the conjecture;
3. the relevant lists of Van Hamme and Z.-W. Sun;
4. the Wolstenholme--Ljunggren--Jacobsthal--Kazandzidis line and the
   Osburn--Sahu--Straub, Osburn--Zudilin, and Straub literature;
5. forward citations of the anchor sources in zbMATH, MathSciNet, Crossref, or
   another named citation index; and
6. theorem-fingerprint searches using the summand, modulus, exceptional
   primes, and recurrence rather than only the OEIS identifier.

Confirmation from an originating author is strong priority evidence but is
not a gate. Silence, unavailability, and a negative search are not novelty
certificates.

## 6. Active gate

The current active audit is
[`GWL-TWO`](related-results/GWLTwoAuditPacket.md). Its checkpoint is
**2026-08-16**. Until it closes, fails, or is demoted, no newly generated
family enters the primary ledger or rankings. Generation may continue only
in the unindexed intake area.
