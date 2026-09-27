# ABIL R2 Review Corrections R3 — Source Composition and Precedence

Status: **IP_CONFIDENTIAL / proposed review correction; implementation not authorized**

Date: 2026-09-09

This document is cumulative with the R2 design and the R1/R2 correction companions. It exists to remove an integration ambiguity in the primary design header, which predates the second correction companion and therefore describes an incomplete source composition.

## Exact normative composition

For the current R2 design subject, reviewers and future implementers must read the exact PR head as the cumulative composition of:

1. `docs/superpowers/specs/2026-09-08-abil-r2-substrate-design.md`
2. `docs/superpowers/specs/2026-09-08-abil-r2-review-corrections-r1.md`
3. `docs/superpowers/specs/2026-09-08-abil-r2-review-corrections-r2.md`
4. this R3 correction.

The primary design's earlier singular wording about one correction companion and "both documents" is superseded by this composition statement.

## Precedence

The documents are cumulative. Where two statements genuinely conflict, the later correction controls only the conflicting point; unchanged requirements from the primary design and earlier corrections remain in force.

No requirement may be dropped merely because it appears in a correction companion rather than the primary design.

## Scope

This correction changes source-composition/precedence clarity only. It does not alter the approved package-first direction, add executable code, authorize implementation planning or Hephaestus handoff, authorize machine access or actuation, or grant merge/deployment authority.
