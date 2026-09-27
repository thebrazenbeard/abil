# ABIL R2 Review Corrections R1

Classification: **IP_CONFIDENTIAL**

Status: **normative correction companion for Draft PR #3 review; implementation not authorized**

Date: 2026-09-08

## 1. Purpose and precedence

This document is a normative correction companion to:

`docs/superpowers/specs/2026-09-08-abil-r2-substrate-design.md`

It incorporates the converged exact-head review findings returned against PR #3 head `adb46c61e854d1a10527ea5840f4cf7b255d82c5` without rewriting the reviewed commit history.

For the current PR #3 source subject:

1. the primary R2 substrate design remains the base design;
2. this correction document is cumulative with it;
3. where the two conflict, this document controls;
4. the minimum `R2-SUBSTRATE-QUALIFIED` gate is the conjunction of the primary design's current acceptance set and every added obligation in this document;
5. `NOT_RUN`, unresolved, or unavailable evidence for a required obligation is not a pass.

Nothing here authorizes implementation, package scaffolding, live machine access, active industrial discovery, machine writes, commissioning, deterministic control, deployment, merge, repository visibility change, licensing change, or another protected effect.

## 2. Source-incarnation identity model

A stable learner stream handle is not sufficient proof that the physical or logical evidence source is still the same source.

R2 therefore distinguishes at least:

- `learner_stream_id` — opaque stable learner-visible stream namespace;
- `channel_id` — opaque channel identity scoped within the learner stream;
- `stream_incarnation_id` — opaque generation identifying one continuity-established incarnation of that stream;
- `EndpointObservation` — evaluator-side time-bound locator/address/slot/node/tag/assembly/register or other endpoint observation;
- `IdentityBinding` — evaluator/control-side record binding source-incarnation continuity to evidence and provenance.

`IdentityBinding` must expose an explicit continuity state equivalent to:

- `ESTABLISHED`;
- `UNRESOLVED`;
- `BROKEN_NEW_INCARNATION`.

The exact enum names may change during implementation planning, but the semantics may not collapse into a boolean or locator-equality test.

### 2.1 Continuity rules

R2 must enforce the following:

- same locator plus replacement source does **not** imply continuity;
- same independently established source at a changed locator may retain continuity only when evidence establishes that continuity;
- unresolved continuity blocks ordinary state attachment/ordinary restore, or starts a fresh incarnation under an explicit rule;
- unrelated topology changes do not automatically invalidate a source incarnation whose continuity remains established;
- material adapter/schema/feature-semantic changes require a new compatible profile or explicit migration rather than silent ordinary restore;
- evaluator/vendor/operator semantic-label-only changes do not force learner identity churn when learner-visible evidence semantics are unchanged;
- learner-visible opaque IDs must not encode rich plant provenance or become reversible aliases for it;
- replay must preserve intentional incarnation changes and their causal boundaries.

### 2.2 Identity binding and checkpoint compatibility

The evaluator-side outer checkpoint binding must include or content-address:

- the exact active stream-incarnation set;
- the relevant `IdentityBinding`/continuity-profile digest;
- continuity status at checkpoint time;
- source-scoped frontiers by incarnation;
- adapter/projection/schema/feature-assembly compatibility identity.

An old-incarnation checkpoint presented against a replacement source at a reused locator is incompatible ordinary state and must be rejected.

An explicit migration/transfer operation, if designed later, is mechanically distinct from ordinary restore and cannot be inferred merely because bytes decode successfully.

## 3. Incarnation transition is a causal barrier

Changing `stream_incarnation_id` is not only an identity bookkeeping event. It is an atomic causal boundary across all state derived from that stream.

The transition barrier applies to at least:

- accepted-event/frontier state;
- reorder buffers and watermarks;
- open windows;
- feature frames and last-known-value state;
- normalization/calibration state;
- rolling statistics;
- change/regime detector state;
- learner/model state where that state depends on the transitioned stream;
- pending checkpoint material;
- replay state.

Required behavior:

- one feature frame/window may not silently combine evidence from different incarnations;
- late events from the old incarnation remain old-incarnation evidence and cannot advance the new-incarnation frontier;
- open buffers/windows are deterministically closed, flushed, quarantined, or recomputed before new-incarnation learning proceeds;
- normalization/calibration/detector/model state resets or migrates only under an explicit compatible rule;
- a checkpoint created while identity is `UNRESOLVED` remains unresolved on resume and cannot silently attach to whichever source later wins resolution;
- replay reproduces the same barrier, quarantine, frontier, and state-transition behavior.

### 3.1 Delayed discovery of a transition

If source replacement/remap is discovered after evidence has already been processed:

- when the exact causal boundary can be established, affected derived state is deterministically recomputed or invalidated from a valid cut where practical;
- when the boundary cannot be established exactly, affected state is marked contaminated/claim-limited and is not silently retained as clean learner history;
- contaminated state cannot earn a qualification claim that assumes clean continuity.

## 4. Mechanical no-hindsight / prequential falsifiers

The existing prequential rule is strengthened from an ordering convention into a hostile-test requirement.

For a prequential profile, once a historical prediction/evidence frontier has been committed, later evidence must not rewrite the feature frame or prediction as though that evidence had been available earlier.

The substrate must mechanically test and reject or claim-limit at least:

- future-event insertion into an earlier feature frame;
- backward fill from a later observation;
- centered windows that use future samples;
- interpolation whose right-hand anchor occurs after the prediction frontier;
- later evaluator labels/status/causal interpretation leaking into an earlier learner frame;
- late/out-of-order evidence silently rewriting an already-scored historical prediction;
- future-dependent normalization or feature construction presented as online/prequential evidence.

If an experiment intentionally uses acausal/offline transforms, it must use an explicitly distinct profile and cannot inherit the claim language of the prequential/online profile.

A committed historical prediction record is append-only evidence. Corrections create successor evaluation records; they do not mutate history in place.

## 5. Identity-memorization controls

Opaque identifiers can still become fixture answer keys if they remain stable across training and evaluation.

For any claim where source identity itself is **not** intended to carry predictive information, qualification must include at least one of:

- a deterministic consistent opaque-ID remapping run that preserves event/value/order structure while changing learner-visible IDs; or
- held-out source/incarnation identities not observed during the relevant training/adaptation period.

Where stable source identity is intentionally supplied predictive evidence, the run manifest and claim ceiling must state that explicitly.

A learner that succeeds only by memorizing fixture/stream/incarnation IDs does not earn a claim of identity-independent machine-structure learning.

## 6. Qualification evidence package

`QualificationReceipt` is an index/attestation of a qualification run, not a substitute for the evidence required to recompute it.

Every run that claims `INDEPENDENTLY_RECOMPUTABLE` must produce a content-addressed `QualificationEvidencePackage` or equivalent that contains or references, with stable digests, enough retained material to independently recompute the declared result.

At minimum it binds or content-addresses:

- exact learner-visible event stream/canonical sequence used for the run;
- projection/timing/feature-assembly profiles and versions;
- target definition and prediction frontiers;
- every scored learner output required to recompute reported metrics;
- evaluator scoring joins/targets and scoring-profile identity;
- paired baseline outputs and their exact configurations;
- negative-control outputs;
- per-test PASS/FAIL/NOT_RUN detail rather than only aggregate gate status;
- checkpoint/cut-point artifacts where restart equivalence is claimed;
- raw resource measurements used for reported resource metrics;
- run/software/build/dependency/schema/corpus identities;
- evidence-package manifest and content digests.

Aggregate metrics alone do not establish independent recomputability.

A receipt whose referenced evidence package is missing, digest-mismatched, incomplete, or non-reconstructable cannot earn `INDEPENDENTLY_RECOMPUTABLE`.

## 7. Deliberately broken harness/comparator oracle

The qualification harness itself is not trusted merely because it reports PASS.

The minimum substrate gate must include a deterministic negative-control case in which a deliberately broken comparator, scoring path, hidden-truth boundary, fixture, or equivalent known-invalid condition is expected to fail.

Required disposition:

- expected failure observed => negative control works for that declared defect class;
- broken case unexpectedly passes => qualification harness is untrusted and the affected gate/run is invalid;
- broken case not run => gate remains incomplete.

This oracle is separate from learner performance and must not be optimized away as an artificial test.

## 8. Resource-accounting attribution

Resource evidence must distinguish at least three scopes:

1. **learner child/process-tree cost**;
2. **evaluator/orchestrator cost**;
3. **end-to-end substrate cost**.

Reported CPU, peak memory, disk, throughput, queue pressure, checkpoint time, restore time, and startup cost must identify which scope they measure.

Evaluator overhead may not be silently charged to the learner, and learner cost may not disappear inside an undifferentiated end-to-end aggregate.

Where a platform cannot perfectly attribute a metric, the limitation must be recorded rather than represented as exact attribution.

## 9. Process-boundary hostile checks retained for implementation qualification

The design-level evaluator/learner separation remains accepted, but implementation qualification must prove the declared boundary rather than infer it from package names.

The exact implementation subject must test at least:

- learner child environment contains only the intended learner distribution/dependencies for the declared profile;
- evaluator/repository working directory and evaluator truth paths are not inherited into the learner task environment;
- environment-variable allowlisting is exact;
- unintended inherited file/IPC handles/descriptors are closed or unavailable;
- child-to-parent protocol accepts only bounded typed prediction/evidence messages and rejects unexpected message/control shapes;
- reviewed learner code receives no evaluator/world object through the declared runtime path;
- pacing-independent profiles remain invariant under hostile wall-clock pauses/jitter that do not change declared learner-visible evidence.

These are implementation qualification obligations. They do not convert R2 into a hostile arbitrary-code sandbox; that threat model remains separately deferred.

## 10. Cumulative added acceptance obligations

The following obligations are added to, and do not replace, the primary R2 minimum acceptance set:

1. reused locator with replacement source does not inherit learner state;
2. same source moving locator retains state only with independent continuity evidence;
3. unresolved identity after topology change fails closed for ordinary state attachment/restore;
4. unrelated topology change does not force spurious source-incarnation reset when continuity remains established;
5. material adapter/schema/feature-semantics change blocks ordinary restore unless an explicit compatible migration exists;
6. evaluator/vendor/operator semantic-label-only mutation leaves learner identity/bytes unchanged when learner-visible evidence semantics are unchanged;
7. old-incarnation checkpoint against replacement source at reused locator is rejected;
8. explicit migration/transfer is mechanically distinct from ordinary restore;
9. replacement during an open rolling/reorder window cannot yield a mixed-incarnation feature frame;
10. late old-incarnation events cannot advance new-incarnation frontier/state;
11. checkpoint during unresolved continuity cannot later resume as an ordinary clean checkpoint;
12. old normalization/calibration/change-detector/rolling state cannot silently carry into a new incarnation;
13. exact retroactive boundary discovery deterministically recomputes or invalidates affected state from a valid cut where practical;
14. ambiguous retroactive boundary produces explicit contaminated/claim-limited state;
15. replay reproduces identical incarnation barrier/buffer/frontier/state behavior;
16. future-event insertion cannot alter a committed prequential prediction/frame;
17. backward fill, centered windows, future-anchored interpolation, or future-dependent normalization is rejected for a prequential profile or moves the run to an explicitly acausal profile;
18. later evaluator labels/status/causal interpretations cannot change already-committed learner-side historical evidence;
19. a qualification receipt claiming independent recomputability resolves to a complete digest-valid evidence package from which reported metrics can be recomputed;
20. opaque-ID remapping and/or held-out-identity control detects identity memorization for claims that exclude identity as predictive evidence;
21. a deliberately broken harness/comparator/fixture negative control fails as expected, and an unexpected pass invalidates trust in the affected harness/gate;
22. resource receipts separately attribute learner child/process-tree, evaluator/orchestrator, and end-to-end substrate cost;
23. pacing-independent output/state is invariant under undeclared wall-clock pause/jitter perturbation;
24. the implemented child process boundary mechanically proves no unintended evaluator truth path, inherited descriptor, rich environment, or untyped IPC channel reaches reviewed learner code.

The primary minimum acceptance set plus these 24 obligations is the current cumulative substrate gate for PR #3 source review. A future reviewer may reorganize the numbering, but no obligation may disappear merely because the document structure changes.

## 11. Review disposition requested

The next exact PR #3 head should be reviewed for:

- closure of the correction set above;
- regression against the seams already accepted at `adb46c61...`;
- no accidental expansion into implementation or actuation authority.

Hephaestus remains held until a later exact source subject is approved for implementation planning/handoff.
