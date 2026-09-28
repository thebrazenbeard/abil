# Non-Authority Currentness Proof V1

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NO IMPLEMENTATION OR DEPLOYMENT AUTHORITY**

Date: 2026-09-18

Architecture subject examined:
- `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

Related subjects:
- Draft PR #6 — write-capability admission design
- Draft PR #7 — deployment commissioning currentness
- Draft PR #8 — support/recovery currentness
- Draft PR #9 — cross-axis consistency
- Draft PR #10 — dependency-cycle resolution

## Purpose

PR #6 already requires a future write-admission validator to reject stale or missing currentness evidence and independently verifies authority currentness with a dedicated read-receipt/freshness mechanism.

The remaining research question is:

> How should future write admission verify the currentness of non-authority evidence such as deployment commissioning, control coverage, recovery readiness, safety classification, and cross-axis currentness without trusting caller-supplied labels or digest equality alone?

A digest proves identity of bytes.

It does not prove those bytes are still current for the machine, deployment, operation, or evidence cut.

## 1. Non-authority currentness classes

Potential currentness subjects include:

- deployment commissioning;
- semantic mappings;
- commissioning envelope;
- control coverage;
- active artifact deployment binding;
- support/recovery readiness;
- fallback/safe-state evidence;
- component/product qualification;
- safety classification;
- ownership/fencing readback where not already handled by authority surfaces;
- cross-axis dependency/currentness cut.

These remain distinct subjects.

## 2. Currentness proof must be evidence-backed

A future validator should not accept:

- `CURRENT=true`;
- `status=FRESH`;
- matching digest alone;
- matching human-readable version;
- unchanged filename/path;
- unchanged endpoint address;
- unchanged deployment name;
- an admission issuer's assertion without supporting evidence.

Currentness must be derived from bound evidence and explicit invalidation rules.

## 3. Currentness receipt concept

A generic non-authority currentness receipt could bind:

- receipt schema/version;
- currentness subject type;
- exact subject identity/digest;
- deployment identity;
- operation/capability scope;
- subject generation/version;
- observed/read evidence;
- evidence sources;
- required dependency identities;
- dependency generations;
- freshness/as-of boundary;
- invalidation profile identity/digest;
- evaluation profile identity/digest;
- evaluator/reader identity;
- result:
  - `CURRENT`
  - `CURRENT_WITHIN_ENVELOPE`
  - `STALE`
  - `UNKNOWN`
  - `CONFLICTING`
  - `PROHIBITED_CARRYOVER`;
- resulting operating/evidence envelope;
- immutable receipt digest.

This is a research shape, not a mandated schema.

## 4. Independent profile resolution

PR #6 already requires independent profile resolution for authority freshness.

A similar principle should apply to non-authority currentness:

The caller must not choose:
- which dependencies matter;
- which invalidation rules apply;
- how long evidence remains fresh;
- which changed fields are irrelevant.

A future validator should independently resolve the expected currentness/invalidation profile for the subject and requested operation.

## 5. Digest equality is necessary, not sufficient

Examples:

### Commissioning envelope

Digest still matches, but:
- machine tooling changed;
- precondition semantics changed;
- stop path changed.

The object is unchanged; its deployment validity is not.

### Control coverage

Digest still matches, but:
- a sensor was replaced;
- timing range changed;
- recovery branch changed.

The ledger bytes remain intact but no longer prove current coverage.

### Recovery evidence

Receipt still matches, but:
- runtime/driver changed;
- backup tool disappeared;
- fallback policy changed.

Recovery evidence may be stale despite exact digest equality.

## 6. Evidence source provenance

Every currentness decision should retain how currentness was established.

Potential source classes:

- direct device identity/readback;
- configuration/firmware digest;
- topology snapshot;
- behavior/timing comparison;
- technician maintenance record;
- controlled commissioning/replay;
- recovery exercise;
- independent safety-project record;
- product/component qualification evidence;
- current artifact/promotion record;
- ownership/fencing readback.

A source class does not automatically prove every predicate.

## 7. Self-attestation boundary

A currentness subject must not be considered independently proven solely because the same plane that benefits from currentness produced the receipt.

Examples:

- learner declares its semantic map current;
- candidate generator declares control coverage current;
- recovery tooling declares itself qualified because restore completed;
- admission caller labels deployment current;
- runtime marks ownership valid without external fencing evidence.

Where currentness gates write authority, proof should come from either:

- mechanically verifiable evidence independent of the claimant;
- an independently authorized qualified reviewer/process;
- a directly qualified joint evidence procedure.

## 8. Operation-specific currentness

Currentness is not always global.

A deployment may be:

- current for read-only telemetry;
- current for one manual recovery action;
- stale for direct control of another output group.

A receipt should bind the operation/capability scope it supports.

No broad `DEPLOYMENT_CURRENT` label should silently authorize every stronger operation.

## 9. Dependency graph integration

PR #10 proposes exact currentness dependency graphs.

A non-authority currentness receipt should bind:

- exact dependency graph or graph digest;
- exact required subject generations;
- SCC disposition where relevant;
- leaf-evidence references;
- joint-qualification bundle references where relevant.

A receipt that omits a required dependency cannot prove currentness.

## 10. Currentness cut integration

PR #9 proposes a coherent currentness cut.

A future write-admission validation should bind the exact currentness receipts used for:

- product capability;
- deployment commissioning;
- artifact/current deployment binding;
- recovery/fallback dependency where required;
- safety classification where applicable;
- ownership/fencing;
- any other required axis.

It should reject incompatible historical cuts.

## 11. Safety classification special case

Safety classification is non-authority evidence but should not be treated as ordinary mutable application metadata.

A future currentness proof should bind:

- exact safety classification subject;
- independent safety-project/source identity;
- as-of/currentness;
- invalidation dependencies;
- whether preserved safety interfaces changed;
- exact operation scope.

Ordinary learner/candidate/runtime planes cannot self-issue safety currentness.

## 12. Control coverage special case

Control coverage is especially vulnerable to stale-but-identical bytes.

A future proof should verify that required coverage dependencies remain current:

- source/device identity;
- semantic mapping;
- timing envelope;
- operating regime;
- fault/recovery evidence;
- commissioning constraints;
- topology/ownership context.

If any required dependency is stale/unknown, the affected coverage downgrades.

## 13. Recovery readiness special case

Recovery readiness may age without explicit machine change.

A currentness proof may therefore need:

- last exercise time;
- exercise profile;
- backup readability;
- required tools/dependencies;
- target hardware/runtime compatibility;
- deployment identity;
- current fallback policy;
- ambiguity-journal preservation evidence.

A label `KNOWN_GOOD` is insufficient.

## 14. Currentness proof versus authority proof

Currentness proof does not grant authority.

Even perfect proof that:
- deployment is current;
- coverage is current;
- recovery is current;

does not establish:

- authority grant;
- authority epoch;
- output ownership;
- promotion authority.

Authority remains separately rooted.

## 15. Validation-time recomputation

Where practical, future admission should recompute or revalidate critical currentness predicates at evaluation/dispatch time.

A cached receipt may be acceptable only within its bound freshness/currentness profile and only if no invalidating generation changed.

Currentness proof cannot be indefinitely reusable.

## 16. Hostile research cases

A future currentness-proof mechanism should reject at least:

1. matching commissioning-envelope digest after machine tooling changed;
2. matching control-coverage digest after sensor replacement;
3. matching recovery receipt after driver/runtime change;
4. caller-supplied `CURRENT` with no evidence;
5. currentness receipt generated solely by learner/candidate plane;
6. old receipt reused after dependency generation changed;
7. currentness receipt omits one required dependency;
8. receipt uses caller-selected invalidation profile;
9. receipt extends freshness beyond independently resolved profile;
10. deployment current for read-only is reused for production write;
11. control coverage remains globally green after one dependency becomes unknown;
12. recovery currentness used as authority;
13. safety currentness self-issued by ordinary ABIL plane;
14. two individually valid receipts belong to incompatible historical cuts;
15. SCC/currentness cycle is accepted without leaf or joint grounding;
16. digest match is accepted when subject identity matches but deployment identity differs.

## 17. Write-admission integration boundary

A future successor to PR #6 may eventually require exact currentness receipts for every non-authority dependency relevant to the requested effect.

That does **not** imply PR #6's current design PASS is invalid.

PR #6 already states stale/missing currentness evidence is rejection.

This research supplies one possible future way to make that requirement machine-checkable.

## 18. Research disposition

The practical rule is:

> For non-authority evidence, exact identity answers "what object is this?" Currentness proof answers "may this exact object still be relied upon for this exact operation now?"

Future write admission should require both where the dependency matters.

No currentness-proof implementation, write-admission implementation, machine access/write, commissioning, recovery/restore action, product selection, procurement/license acceptance, deployment, promotion, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
