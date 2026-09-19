# ABIL Chat Continuation — 2026-09-19 hostile-review batch V1

Restore directive:

`ABIL::RESTORE::ABIL_CHAT_CONTINUATION_20260919_HOSTILE_REVIEW_BATCH_V1`

Status:
- active ABIL written/research review gates repaired and rerouted;
- no merge/protected effect performed;
- exact-head peer rereviews pending on PR #3/#4/#21;
- broader Bus hostile-review queue substantially processed in this chat.

## Governance / boundaries

Patrick remains sole merge/protected-effect authority.

Do not merge/canonically promote, deploy, connect/write to machines, commission, mutate provider/credentials/rulesets/billing, install trust roots, select/procure licensed products, create current-memory/R9B0 admission, or perform another protected effect without Patrick's exact authority.

Fresh exact-head review is mandatory after material head movement.

PR #3 hard gate remains:
if exact-head written-design peer review + coordinator reconciliation becomes clean, STOP before implementation planning and obtain Patrick's explicit final written-design acceptance.

## Current ABIL exact heads

- PR #2 architecture: `712d5b30b45ba9299dcfce0599878cb81db70e8f`
- PR #3 R2 written design: `1da5bc57b0228178300f6ba966d97d1dce807dc1`
- PR #4 component/runtime evidence research: `1fd7767a6516dd9efab8eb6b74fdd8f97cf23407`
- PR #6 write-capability admission: `b191822ecbc95ce120384acf1c17289b4b834033`
- PR #7 deployment commissioning currentness: `a62ae16a0c1bc484ae6b45e4af853af64a2e6707`
- PR #8 support/recovery currentness: `7d11cea51bfff3f2bf32e98516479be4d742d172`
- PR #9 cross-axis state consistency: `90d40f4baca29629f8f17f956f20687fee674820`
- PR #21 trust-state currentness/antirollback: `2b4d5da33d9ce7dfe4d13c44a07bcd2f1c469120`

All above are OPEN / DRAFT / UNMERGED / MERGEABLE at this continuation save.

Architecture base remains:
`712d5b30b45ba9299dcfce0599878cb81db70e8f`.

## PR #3 — R6 hostile repair

Thirteen returned predecessor R5 exact head `c2e363d4c1b8c67e032c22d9cad6451342b04e7b` CHANGES_REQUIRED because:
- evaluator-context irrelevance could be self-asserted;
- protected evaluator evidence references lacked explicit authorization-scoped resolution;
- evaluator-only inputs lacked a coherent run-level temporal/context cut.

Repair published:
- exact head: `1da5bc57b0228178300f6ba966d97d1dce807dc1`
- file: `docs/superpowers/specs/2026-09-19-abil-r2-review-corrections-r6.md`
- blob: `1a239a95a78849f27cfd8b07ebeb345a065bfe78`
- PR comment: `5743270745`

R6 rules:
- changed consulted evaluator context always means distinct experiment identity;
- equivalence is a separate claim-scoped derived relation;
- evaluator cannot self-issue irrelevance;
- equivalence requires independently bound dependency/noninterference proof or deterministic paired replay;
- protected evaluator payload resolution is authorization-scoped;
- digest/URI possession is not read authority;
- learner-safe commitments are separate from authorized evaluator/verifier resolution;
- evaluation binds a coherent run-level context cut or deterministic multi-cut join;
- generation/lineage currentness cannot be defeated by wall-clock rollback.

R6 rereview routed to:
Three, Seven, Nine, Two, Six, One, Thirteen.

Bus message:
`messages/20260919-vera-abil-pr3-r6-rereview-request.md`
message commit:
`1f22e1c1c249f10fa2c97d59a8c76b6a7da3a8ef`
Vera HEAD update:
`f201b566fbaffcf6a1502b04a594d58b9d5531c5`

No exact-head peer return had landed at latest check.

## PR #4 — component evidence restoration/dependency closure repair

Thirteen returned predecessor exact head `cd4f811ec9318231a3864fcedf4cd67befab07a7` CHANGES_REQUIRED because:
- upward evidence restoration had no authority/provenance rule;
- derived claims could remain green by omitting a required dependency edge;
- declared envelopes could become self-authored scope expansion;
- temporal/currentness semantics were underspecified.

Repair published:
- exact head: `1fd7767a6516dd9efab8eb6b74fdd8f97cf23407`
- file: `docs/research/2026-09-19-component-evidence-restoration-authority-and-dependency-closure-v1.md`
- blob: `89ca467e26bd107310d32fde77b353dc4684a7d0`
- PR comment: `5743288327`

Key rules:
- immutable evidence facts + immutable claim/dependency definitions + recomputed claim-state receipts;
- upward restoration requires EvidenceRestorationReceipt;
- restoration is claim-owner/evidence-class constrained;
- ABIL cannot restore THIRD_PARTY_DIRECT by self-authored evidence;
- supportable derived claims bind a versioned RequiredDependencySpecification;
- DependencyClosureReceipt proves complete required-edge resolution;
- omitted/missing required edges cannot disappear and remain green;
- dependency-definition change invalidates prior derived support until re-derived;
- envelopes are provenance-bound;
- ABIL may conservatively narrow inherited third-party envelope, not broaden it without qualifying evidence;
- current and historical evaluation cuts are distinct;
- stale persisted support labels are non-authoritative.

Rereview routed to:
Thirteen, Seven, One.

Bus message:
`messages/20260919-vera-abil-pr4-restoration-rereview-request.md`
message commit:
`c763f58bc9ab20bc5a41018f87e10375c0f1ad09`
Vera HEAD update:
`0c316c0f727fd29eef8960b0b2706d0669a3a640`

No exact-head peer return had landed at latest check.

## PR #21 — protected trust-state head witness / transition authority repair

Thirteen returned predecessor exact head `1e2d16913bd9014a38306c0a2d53314ad98491e2` CHANGES_REQUIRED because monotonic generation was not itself an anti-rollback authority and the resolver could be circular after restore/failover.

Source-owner notes also identified:
- who/what is authorized to create T(n+1);
- time-source/currentness ambiguity.

Repair published:
- exact head: `2b4d5da33d9ce7dfe4d13c44a07bcd2f1c469120`
- file: `docs/research/2026-09-19-trust-state-protected-head-witness-and-transition-authority-v2.md`
- blob: `6a79a5bdd183cb31e1dc5a2ffa6204c16b388b9a`
- PR comment: `5743304622`

Key rules:
- immutable append-only trust-state nodes;
- separately protected TrustStateHeadWitness with rollback-domain separation sufficient to falsify restored-store rollback;
- local maximum generation never proves currentness;
- unavailable/unverifiable/non-unique witness fails protected current acceptance closed;
- sibling successors are `TRUST_STATE_CONFLICTING`, never winner-by-generation/time/permissiveness/local recency;
- currentness receipts bind witness evidence, scope, resolver identity/profile, lineage/fork/time result;
- higher generation is not automatically legitimate;
- each successor requires independently rooted TrustStateTransitionAuthorizationReceipt;
- successor state cannot self-bootstrap transition authority;
- transition authority is scope-bound and may require quorum/multi-role policy;
- node creation and witness advancement are distinct;
- multi-scope changes require atomic parent cut or explicit independent-cut semantics and combination receipts;
- lineage/protected witness order dominates wall-clock; qualified time may only narrow acceptance;
- restore/failover treats local bytes as candidate state until witness reconciliation.

Rereview routed to:
Thirteen, Six, One.

Bus message:
`messages/20260919-vera-abil-pr21-protected-witness-rereview-request.md`
message commit:
`9d11e7d7fbcd72a55ccfa40a472faaae3650ee33`
Vera HEAD update:
`a660822adf610f84e0539287080e9ff03ba880a4`

No exact-head peer return had landed at latest check.

## Other ABIL review state

PR #6 remains design/governance closed at exact head `b191822e...`; no rereview needed without head/new finding.

PR #7/#8/#9 remain frozen on exact heads above, awaiting routed independent review where applicable.

Do not create additional research PRs solely to manufacture activity. Current limiting dependency is independent exact-head review/reconciliation.

## Wider Bus hostile-review batch handled in this chat

The user requested all open hostile review requests on the Chat Bus be addressed. This chat performed supplemental exact-head reviews without impersonating separately named reviewer identities.

### Radar PR #117
Exact head:
`6932c278d95cd93910fe34daeb3789b41c3e485a`

Disposition:
RETURN / CHANGES_REQUIRED.

Blockers:
- privileged registration/reconciliation creation is self-asserted by payload rather than independently rooted transition/governance authority;
- routing metadata parser has no bounded header/body envelope and can derive routing keys from arbitrary Markdown body lines.

Native review:
`5256211611`

Bus return:
`messages/20260919-vera-to-radar-pr117-hostile-return.md`

Head remains unchanged at latest check, so RETURN is still current.

### Radar PR #118
Exact head:
`40673e16819aee4c6b40b23a7fdc64f215cec0f5`

Disposition:
ACCEPT at SOURCE / EXACT_DATA_PLANE_QUERY_ONLY.

Native review:
`5256222250`

Bus message:
`messages/20260919-vera-pr118-hostile-accept.md`

### Deep Memory repaired pair
Initial pair:
provider `8c58821d...`, consumer `2cf9af51...`

Initial Vera result:
RETURN due provider DM-V-001:
malformed/missing row-count evidence inside a present latest receipt could yield `ROW_COUNT_MISMATCH` while leaving `load_union().errors` empty, allowing query path to proceed.

Provider repaired successor:
`deepmemorystorage PR #1 @ 539b5988e0913130427da3d1098d84592d1122cf`

Consumer repaired repin:
`vera PR #59 @ 5157405295531437007050e2256fda9298c9e92f`

Current Vera disposition:
ACCEPT_SOURCE for exact repaired pair.

Provider native review:
`5256361565`

Consumer native review:
`5256362020`

Bus successor acceptance:
`messages/20260919-vera-deep-memory-successor-hostile-accept.md`
message commit:
`86f47411296fddc0ec52cd0ab7c95975e3fee508`
Vera HEAD update:
`2039c1e24ece179f4b220c004eb8e9889c0a7f61`

### Rezon Kernel
R19 exact head `c1804411...` was RETURNed for exception-atomicity/partial-commit failure.

R20 superseded R19:
- PR #33
- exact head `71ff317cb2e086088866c551854e8b9e3bca708b`

R20 adds rollback checkpoint of all five current mutable Episode containers under shared RLock and re-raises after restore.

Vera supplemental disposition:
ACCEPT at current in-memory Episode-transaction ceiling.

Native review:
`5256268253`

Bus:
`messages/20260919-vera-rezon-r20-hostile-accept.md`

Named Mune/Masa/One identity gates remain distinct.

### Writer-generation PR #87/#88
PR #87 exact head:
`df00b78fb23966cd6ca3118290b6c92e16d10371`

PR #88 exact head:
`18daf4bb01b361727b02d68e1550b669701295a0`

Vera supplemental source/inert-only ACCEPTs:
- PR #87 native review `5256244368`
- PR #88 native review `5256244831`

Bus:
`messages/20260919-vera-pr87-pr88-hostile-accept.md`

Brigit named gate remains distinct and had not moved at latest check.

### Radar stale merge-boundary successors PR #71/#80
Prior exact gates became stale after head movement.

PR #71 current:
`f23a86675d3ccd783e48fe08a80f8a2cea8cae66`
Delta from old accepted `7d2813dc...`:
one test file only; production source unchanged.

Vera supplemental disposition:
ACCEPT_SOURCE / TEST-HARNESS-SUCCESSOR.

Native review:
`5256352053`

PR #80 current:
`f77576a7e5c0a454271c0389496f8dbc28578b43`
Current exact #71 base:
`f23a86675d3ccd783e48fe08a80f8a2cea8cae66`

Branch-bound production source unchanged from old accepted #80; own successor change restores durable operator-contract phrase while retaining stronger exact-physical-ref requirement.

Vera supplemental disposition:
ACCEPT_SOURCE / BRANCH-PROVENANCE-PHASE-TAXONOMY.

Native review:
`5256352457`

Bus:
`messages/20260919-vera-pr71-pr80-successor-rereview.md`

Prior Radar/Brigit old-head gates remain stale unless exact-head rebound by those identities.

### Intranel PR #3
Current exact head:
`27c4676d79621de6d17dd14ed4064ea5e742c107`

One has already returned this head FAIL / CHANGES_REQUIRED because parser `_tuple_of_strings()` converts null governance-array items into empty strings while schema rejects null.

No repaired successor exists at latest check.

Do not duplicate hostile review until head moves.

### SelfImage FNG gate
FNG's coarse-fit hostile gate is not yet reviewable because the requested actual candidate/evidence package has not arrived. Later FNG messages reject the radial builder as diagnostic-only and require surface-aware global fit.

Do not manufacture a verdict on a nonexistent candidate.

### World Zero PR #2
Exact subject from the old review route is CLOSED / UNMERGED. Treat the request as non-live.

## Requester-lane freshness

At latest check:
- Radar branch advanced only with Deep Memory repair/successor messages after its continuation.
- Hephaestus branch had no movement from its prior observed head.
- Brigit branch had no movement from its prior observed head.

Therefore named Hephaestus/Brigit independent gates are still genuinely pending where required; Vera supplemental reviews must not impersonate them.

## Immediate next actions

1. Fresh-check PR #3/#4/#21 heads before using any review return.
2. Fresh-check Three/Seven/Nine/Two/Six/Thirteen/One Bus lanes for exact-head replies.
3. If PR #3 exact-head peer review + One reconciliation becomes clean, STOP and ask Patrick for explicit final written-design acceptance before any implementation planning.
4. For PR #4/#21, repair only material exact-head findings; any head move invalidates predecessor review.
5. Keep PR #6 frozen unless new finding/head movement.
6. Do not churn PR #7/#8/#9 without a material review result.
7. Radar PR #117 remains a live RETURN until successor head.
8. Deep Memory repaired pair is currently Vera source-review ACCEPT.
9. Intranel remains a current FAIL until successor.
10. No merge/protected effect.
