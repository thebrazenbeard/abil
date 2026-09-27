# ABIL R2 Review Corrections R2

Classification: **IP_CONFIDENTIAL**

Status: **normative narrow successor correction for Draft PR #3; implementation not authorized**

Date: 2026-09-08

## 1. Purpose and precedence

This document closes the remaining exact-head review residual identified against PR #3 head `761bf03710e30a61f4949ad5005d87aafa3981fa` concerning evaluator-side reconstruction of learner-visible opaque identity across process restart.

For the current PR #3 design composition:

1. `2026-09-08-abil-r2-substrate-design.md` remains the primary design;
2. `2026-09-08-abil-r2-review-corrections-r1.md` remains cumulative and normative;
3. this R2 correction is cumulative with both and controls where its narrower identity-restart requirements are more specific;
4. the minimum substrate gate is the conjunction of the primary design, R1 correction obligations, and the obligations below;
5. this file creates no implementation, machine-connection, actuation, merge, deployment, publication, licensing, or other protected authority.

## 2. Opaque identity registry is evaluator/control state

A checkpoint that preserves learner state under opaque `learner_stream_id`, `stream_incarnation_id`, and `channel_id` subjects is not restart-safe unless the evaluator can reproduce the exact same learner-visible identity namespace for continuity-established sources after evaluator process loss.

R2 therefore requires an evaluator/control-side **Opaque Identity Registry** or mechanically equivalent deterministic reconstruction subject.

The implementation name may differ, but the semantics may not be omitted.

The registry/reconstruction subject must preserve enough evaluator-only state to reproduce the exact learner-visible identities required by active or restorable learner state while keeping rich plant/source provenance unavailable to the learner.

Its durable identity must include or content-address at least:

- registry/reconstruction schema and version;
- opaque namespace/root identity;
- active/restorable stream-incarnation/channel mapping state or the deterministic material required to reconstruct that state exactly;
- linkage to continuity-established evaluator-side `IdentityBinding` subjects;
- registry/reconstruction content digest and version/frontier;
- compatibility identity for the projection rules that consume the registry.

A projection-profile digest alone does not satisfy this obligation unless that exact profile plus persisted evaluator-only material deterministically reconstructs the same prior opaque IDs.

## 3. Two acceptable implementation families

R2 permits either of these approaches or a mechanically equivalent design.

### 3.1 Persisted registry

Persist a bounded evaluator/control-side registry containing the mapping needed for active and restorable streams/incarnations/channels.

The registry:

- is not learner input;
- may reference rich evaluator-side continuity subjects;
- must have deterministic bounded serialization;
- must be integrity/digest checked before use for ordinary restore;
- must not silently regenerate a new mapping when the prior mapping is required by checkpointed learner state.

### 3.2 Deterministic reconstruction

Instead of persisting every mapping entry, persist evaluator-only namespace/root material plus the exact deterministic reconstruction contract needed to reproduce the prior opaque IDs.

Reconstruction must:

- produce byte-identical opaque learner identities for the same continuity-established subject;
- remain bound to the exact compatible projection/identity profile;
- not derive learner-visible IDs from reversible/readable plant locators;
- never expose root/derivation material to the learner process;
- fail closed when required reconstruction material is unavailable, corrupt, or incompatible.

## 4. Outer checkpoint and replay binding

The evaluator-side outer checkpoint compatibility subject must include or content-address the exact opaque-identity registry/reconstruction digest needed to resume the checkpointed learner state.

Ordinary restore order is normative:

1. establish evaluator-side source/continuity identity independently;
2. load or deterministically reconstruct the prior opaque identity registry/namespace;
3. verify its schema/version/profile/content digest and compatibility;
4. resolve the continuity-established source to the exact expected learner stream/incarnation/channel identities;
5. verify checkpoint stream/incarnation/frontier compatibility;
6. only then attach and decode learner state.

Missing, corrupt, incompatible, or unreconstructable identity-registry state blocks ordinary learner-state attachment.

Starting a fresh run or fresh incarnation is an explicit new-state path. It is not ordinary restore, and old learner state may not be attached merely because the physical locator looks familiar.

Replay/corpus restart must reproduce the same opaque namespace/mapping behavior so restart equivalence is independent of evaluator process lifetime.

## 5. Positive-continuity and false-discontinuity requirement

Fail-closed mismatch rules protect against attaching old state to the wrong source, but that is only half of continuity correctness.

R2 must also prove that a source whose continuity is independently established can resume under the exact prior opaque learner identity after evaluator restart.

Qualification therefore distinguishes:

- **false positive continuity** — wrong/new source inherits prior learner identity/state;
- **false discontinuity** — same continuity-established source is unnecessarily assigned a new opaque identity because registry/reconstruction state was lost or changed.

Both are qualification failures for ordinary restore.

## 6. Learner-visible incarnation claim ceiling retained

`stream_incarnation_id` remains supplied identity/continuity evidence when the boundary is established by evaluator-side evidence.

A learner may use that supplied evidence only under the declared evidence profile. Any efficacy benefit attributable to supplied incarnation/identity transition information must be reported and claim-limited accordingly.

Identity-remap and held-out-identity controls remain required for claims that exclude stable identity/incarnation as predictive evidence. No result may be credited as autonomous machine-state discovery merely because evaluator-established continuity or replacement classification changed a learner-visible opaque identity.

## 7. Added hostile acceptance obligations

The cumulative R2 substrate gate adds these exact cases:

1. evaluator process restart with a continuity-established source reproduces the exact prior opaque learner stream/incarnation/channel identities before learner state attaches;
2. persisted-registry mode rejects ordinary restore when the required registry is missing, corrupt, digest-mismatched, wrong-version, or incompatible;
3. deterministic-reconstruction mode reproduces byte-identical opaque identities from the exact persisted evaluator-only reconstruction subject and fails closed when required root/profile material is unavailable or incompatible;
4. same continuity-established source does not suffer false discontinuity solely because the evaluator process restarted;
5. replacement source at a reused locator still cannot inherit the prior opaque identity/state merely because the registry contains a historical locator association;
6. replay interrupted across evaluator restart produces the same learner-visible identity namespace, feature sequence, subsequent predictions, learner-state digest, and evaluation result as uninterrupted replay for deterministic profiles;
7. fresh-run/fresh-incarnation creation is mechanically distinct from ordinary restore and cannot silently attach prior learner state;
8. learner-visible identity bytes remain unchanged when only evaluator-side semantic labels/provenance change and continuity plus the declared learner-visible evidence profile remain unchanged.

`NOT_RUN`, unavailable evidence, or an aggregate assertion without the required retained evidence does not satisfy these obligations.

## 8. Review disposition requested

Successor exact-head review should be delta-only for this narrow residual plus regression against previously passing seams.

The source owner should not reopen already-closed facets absent new evidence.

Hephaestus and implementation planning remain held until the exact corrected design composition is accepted under the current review gate and Patrick authorizes the next planning step.
