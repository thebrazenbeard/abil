# Synthetic Reconstruction Benchmark Hostile Validation V1

Status: **NON-NORMATIVE RESEARCH HOSTILE-VALIDATION CONTRACT / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR MACHINE AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #5

Fixture:
- `ABIL_SYNTH_INDEX_PROCESS_CELL_V1`

Preregistration:
- `docs/research/2026-09-18-synthetic-reconstruction-preregistration-v1.md`

Evidence package:
- `docs/research/2026-09-18-synthetic-reconstruction-evidence-package-v1.md`

Baseline workflows:
- `docs/research/2026-09-18-synthetic-reconstruction-baseline-workflows-v1.md`

Architecture base examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

A benchmark can be internally consistent and still be easy to fool.

This document defines hostile validation obligations for the benchmark machinery and retained evidence **before** any benchmark implementation exists.

The target is not ABIL's reconstruction algorithm.

The target is the experiment system itself:
- evidence boundaries;
- participant/evaluator separation;
- technician accounting;
- subject identity;
- scoring joins;
- baseline parity;
- invalidation logic;
- claim-tier derivation.

A benchmark result that survives the participant but fails the experiment-integrity checks is not valid evidence.

## 1. Hostile-validation principle

The benchmark must fail closed when experiment integrity cannot be proven.

The evaluator should prefer:
- invalidating a comparison;
- downgrading a claim;
- preserving an unresolved ambiguity;

over silently repairing missing evidence from memory or narrative.

No hostile test may reveal its hidden truth to the participant during the scored run.

## 2. Validation surfaces

Hostile validation applies to at least:

1. experiment-subject identity;
2. participant-visible projection;
3. evaluator-only context;
4. technician interaction ledger;
5. observation corpus;
6. participant output retention;
7. behavior scoring joins;
8. seeded hostile-case register;
9. baseline symmetry;
10. resource accounting;
11. invalidation/exclusion handling;
12. claim-disposition derivation.

A package is not "valid" merely because required filenames exist.

## 3. Subject-identity attacks

### HV-01 — Missing fixture digest

Remove immutable fixture identity while retaining the fixture label.

Expected result:
`INVALID_EXPERIMENT_SUBJECT`

A human-recognizable fixture name is not enough.

### HV-02 — Same label, changed truth

Keep `ABIL_SYNTH_INDEX_PROCESS_CELL_V1` as the visible label but alter one truth parameter or holdout behavior.

Expected:
- experiment subject changes;
- prior run is not replay-equivalent.

### HV-03 — Scoring version drift

Change evaluator/scoring behavior without changing the bound scoring subject identity.

Expected:
`INVALID_EVALUATOR_DRIFT`

### HV-04 — Technician-budget drift

Increase allowed technician interactions while keeping the old experiment subject ID.

Expected:
subject mismatch / invalid comparison.

## 4. Participant/evaluator separation attacks

### HV-05 — Hidden truth in filename

Encode a withheld behavior, state name, timeout, or "stale/current" hint in a participant-visible filename.

Expected:
`INVALID_EVIDENCE_LEAK`

### HV-06 — Hidden truth in error text

Have an evaluator/tool error reveal a withheld transition or exact timing value.

Expected:
`INVALID_EVIDENCE_LEAK`

### HV-07 — Evaluator manifest omitted

Run scoring with evaluator-only control context but omit it from the evaluator-context manifest.

Expected:
`INVALID_EVALUATOR_DRIFT` or `EVALUATOR_CONTEXT_UNBOUND`.

### HV-08 — Evaluator context changed, output unchanged

Change evaluator-only state that is actually irrelevant to fixture selection/admissibility/scoring/claim ceiling.

Expected:
replay may remain comparable only if a retained irrelevance disposition proves non-effect.

### HV-09 — Evaluator context changed, semantics changed

Change evaluator-only state that changes scoring or admissibility while preserving old experiment identity.

Expected:
invalid experiment subject.

## 5. Technician-accounting attacks

### HV-10 — Uncharged semantic hint

Provide one semantic label outside the technician ledger.

Expected:
`INVALID_BUDGET_ASYMMETRY` or participant-contamination disposition.

### HV-11 — Free correction

Technician corrects a participant's wrong state/transition after output generation but before retained participant output is frozen.

Expected:
run invalid for direct comparison unless the pre-correction output is recovered and correction is charged/documented.

### HV-12 — Reused answer across arms

One arm asks a technician question; another arm receives the answer automatically without charging the answer as supplied evidence.

Expected:
cross-arm contamination / parity failure.

### HV-13 — Human cleanup hidden as tool output

Manual engineer fixes AI/ABIL output but resource accounting credits the result entirely to the automated workflow.

Expected:
resource/provenance failure.

## 6. Observation-corpus attacks

### HV-14 — Trace omission without identity change

Remove one fault/recovery trace while retaining the old observation-corpus digest/subject.

Expected:
identity verification failure.

### HV-15 — Reordered events

Reorder timing-sensitive events while preserving row content.

Expected:
corpus digest/subject changes; timing-dependent comparison cannot inherit prior subject.

### HV-16 — Semantic enrichment during conversion

Convert opaque signals to a spreadsheet and silently add human-readable semantic names.

Expected:
evidence-advantage detection; direct comparison invalid unless all compared arms receive equivalent enrichment.

### HV-17 — Future/holdout leakage

Participant-visible corpus contains a trace from the clamped-part recovery holdout.

Expected:
`INVALID_EVIDENCE_LEAK`.

## 7. Participant-output attacks

### HV-18 — Evaluator-corrected output replaces original

Only the corrected reconstruction is retained.

Expected:
package not auditable; run invalid for behavior-precision comparison.

### HV-19 — Unsupported behavior with no provenance

Participant states withheld recovery as established but provides no valid supporting evidence.

Expected:
`INCORRECT_ESTABLISHED` or `PROVENANCE_MISATTRIBUTED`, with appropriate secondary defect.

### HV-20 — Unknown omitted from output schema

Participant cannot express "unknown" because the representation forces every transition into a binary known/false state.

Expected:
workflow limitation must be reported; absence of representable uncertainty cannot be scored as correct completeness.

## 8. Scoring-join attacks

### HV-21 — Aggregate-only score

Package reports one percentage but omits item-level `BehaviorScoreRecord` evidence.

Expected:
not independently auditable; claim tier not awardable.

### HV-22 — Truth proposition changed after participant output

Evaluator edits a truth proposition after seeing participant output without creating a new fixture/scoring subject.

Expected:
invalidated run.

### HV-23 — Multiple primary dispositions

One behavior receives two incompatible primary dispositions to improve aggregate reporting.

Expected:
scoring validation failure.

### HV-24 — Missing provenance misattribution

Behavior is correct only because technician supplied it, but evaluator scores it `CORRECT_ESTABLISHED` as autonomous inference.

Expected:
`PROVENANCE_MISATTRIBUTED`.

### HV-25 — Unsupported causal promotion ignored

Participant promotes `UPSTREAM_PHOTOEYE` from correlation to permissive truth; evaluator scores only prediction accuracy.

Expected:
scoring defect; hostile case must produce `UNSUPPORTED_CAUSAL_PROMOTION`.

## 9. Seeded-hostile-case attacks

### HV-26 — Hostile case absent from summary

Withheld clamped-part recovery fails, but the run summary reports only normal-cycle success.

Expected:
claim-disposition validation failure.

### HV-27 — Failed profile averaged away

E2 replacement-at-same-locator fails identity handling, but high scores on A1/B1 hide the failure in an aggregate.

Expected:
identity-robustness claim blocked.

### HV-28 — Stale-source conflict silently resolved

D1 conflict is absent from the conflict register because evaluator selected one truth source before scoring.

Expected:
benchmark integrity failure; stale-source resilience not awardable.

## 10. Baseline-parity attacks

### HV-29 — Baseline gets weaker evidence representation

ABIL receives timestamped event data; baseline receives screenshots without machine-readable timing despite equivalent representation being feasible.

Expected:
`INVALID_BUDGET_ASYMMETRY` or parity failure.

### HV-30 — ABIL gets project-aware search, AI baseline is denied it

If project-aware search/RAG is a normal capability of the selected AI baseline and the evidence profile permits it, prohibiting it creates a straw baseline.

Expected:
baseline invalid for direct competitive claim.

### HV-31 — Baseline operator incompetence

Baseline participant demonstrably fails the competence floor on the non-scored pilot.

Expected:
do not use that baseline run to support an ABIL advantage.

### HV-32 — Direct-source arm omitted from intact-source profile

A1 has trustworthy current source and realistic direct transformation is feasible, but direct-source comparison is omitted without reason.

Expected:
intact-source superiority claim incomplete.

## 11. Resource-accounting attacks

### HV-33 — Human time hidden

Post-run manual cleanup is not charged to participant engineering time.

Expected:
labor-comparison invalid.

### HV-34 — Technician time rounded away

Repeated short technician interactions are omitted because each is individually small.

Expected:
technician ledger/accounting failure.

### HV-35 — Compute/tool cost selectively omitted

One arm's material external/tool cost is omitted while another arm's cost is reported.

Expected:
resource comparison invalid until normalized.

## 12. Invalidation attacks

### HV-36 — Failure relabeled fixture defect

A participant fails E1 and the evaluator marks the run invalid solely because the outcome is poor.

Expected:
invalid invalidation; failed participant result must stand.

### HV-37 — One-arm fixture defect exclusion

A real fixture defect affects all arms, but only ABIL's run is rerun.

Expected:
comparison invalid until affected arms are handled consistently.

### HV-38 — Corrected fixture pooled with old runs

Fixture truth is corrected, but new runs are pooled with historical runs under the same subject.

Expected:
subject-separation failure.

## 13. Claim-tier attacks

### HV-39 — Source-optional claim from intact-source only

Only A1 succeeds, but `SOURCE_OPTIONAL_RECONSTRUCTION_SUPPORTED` is awarded.

Expected:
claim validation failure.

### HV-40 — Archaeology reduction without baselines

ABIL runs alone; `ARCHAEOLOGY_REDUCTION_SUPPORTED` is awarded.

Expected:
claim validation failure.

### HV-41 — Stale-source resilience despite D1 overtrust

D1 silently trusts stale source for one seeded conflict.

Expected:
`STALE_SOURCE_RESILIENCE_SUPPORTED` blocked until preregistered criteria are met.

### HV-42 — Replacement-control promotion

Benchmark success is used to award or imply `REPLACEMENT_CONTROL_READY`.

Expected:
hard validation failure. This tier is non-awardable by the benchmark.

## 14. Cross-run contamination attacks

### HV-43 — Participant memory across arms

Same operator runs one arm after reading another arm's reconstruction and no contamination control is recorded.

Expected:
direct comparison invalid or downgraded to exploratory.

### HV-44 — Persistent AI context leakage

AI baseline or ABIL candidate retains hidden context from an earlier fixture run.

Expected:
participant subject changes; run invalid unless persistence is explicitly part of the experiment.

### HV-45 — Shared technician learns answers

Technician changes later responses because earlier arms exposed participant hypotheses or evaluator feedback.

Expected:
interaction oracle/technician-subject drift must be recorded; direct parity claim may be invalid.

## 15. Ambiguous-action integrity attacks

### HV-46 — Missing acknowledgement treated as no execution

The simulated `REQUEST_SYNTHETIC_INDEX_PULSE` loses acknowledgement and evaluator/participant records `NOT_EXECUTED` without independent evidence.

Expected:
`AMBIGUOUS_ACTION_COLLAPSED`.

### HV-47 — Automatic retry erases ambiguity

A workflow retries the simulated action and later success is used to infer the first dispatch did not execute.

Expected:
first outcome remains `UNKNOWN/AMBIGUOUS_EXECUTION_OUTCOME`; blind retry is not credited.

## 16. Required hostile-validation report

A future benchmark implementation should produce one validation report containing at least:

- benchmark implementation subject;
- evidence-package schema/contract identity;
- hostile case ID;
- mutation/injection applied;
- expected disposition;
- observed disposition;
- PASS/FAIL;
- supporting artifact references;
- whether failure invalidates:
  - one run;
  - one arm;
  - one run family;
  - one claim tier;
  - the benchmark implementation itself.

A single overall PASS without per-case evidence is insufficient.

## 17. Minimum qualification rule

Before confirmatory benchmark results are treated as evidence, the experiment system should demonstrate that it can detect at least one hostile mutation in every validation surface:

- identity;
- leakage;
- technician accounting;
- corpus integrity;
- participant-output retention;
- scoring joins;
- hostile-case reporting;
- baseline parity;
- resource accounting;
- invalidation;
- claim derivation.

Passing only happy-path package validation is insufficient.

## 18. No self-validating evaluator

The component that generates a participant result should not be the only component deciding whether the evidence package proves that result.

At minimum, the retained package must permit independent recomputation or hostile review of:
- subject identities;
- behavior dispositions;
- aggregate metrics;
- claim-tier prerequisites.

This does not require a specific implementation architecture at the research stage.

## 19. Failure handling

If hostile validation finds an experiment-system defect:

1. preserve the failing exact subject;
2. identify affected historical runs;
3. invalidate/downgrade only what evidence supports;
4. repair under a new exact benchmark implementation subject;
5. rerun the relevant hostile case;
6. rerun confirmatory participant runs when the defect could have changed their evidence or scoring.

Do not silently patch old evidence into compliance.

## 20. Research disposition

This hostile-validation contract makes the benchmark itself a falsifiable object.

It should be possible for:
- ABIL to produce a good reconstruction;
- the evaluator to score it plausibly;
- and the overall benchmark result still to be rejected because experiment integrity failed.

That is intentional.

A benchmark designed only to detect participant mistakes is too weak to support claims about a system whose proposed advantage depends heavily on provenance, uncertainty, identity, and evidence discipline.

No hostile-test implementation, benchmark runner, scoring engine, package scaffolding, account/tool connection, paid service use, machine connection/write, commissioning, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research contract.
