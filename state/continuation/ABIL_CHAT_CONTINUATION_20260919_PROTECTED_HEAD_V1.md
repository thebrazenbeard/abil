# ABIL Chat Continuation — 2026-09-19 Protected Head V1

Restore directive:

`ABIL::RESTORE::ABIL_CHAT_CONTINUATION_20260919_PROTECTED_HEAD_V1`

Predecessor continuation:
- repo: `thebrazenbeard/abil`
- branch: `state/abil-chat-continuation-20260919-hostile-review-batch-v1`
- file: `state/continuation/ABIL_CHAT_CONTINUATION_20260919_HOSTILE_REVIEW_BATCH_V1.md`
- commit: `616a4baa674c9565cb09c08023e46e3f42090ea6`
- blob: `8ae9879750713179c4d138c89efe2c45b49a6171`

Status:
- no merge/protected effect performed;
- PR #3 remains the written-design hard gate;
- Thirteen exact-head review is clean on PR #3 R6 but not all peer facets are complete;
- Thirteen returned blockers on PR #4, PR #21, and the transaction/evidence witness chain;
- all three blocker classes were repaired and fresh rereviews were routed;
- shared PR #25 ProtectedHeadWitness semantic primitive now carries non-forking predecessor-bound unique-advancement semantics;
- current limiting dependency is independent exact-head peer review/reconciliation.

## Governance

Patrick remains sole merge/protected-effect authority.

Do not merge/canonically promote, deploy, connect/write to machines, commission, mutate provider/credentials/rulesets/billing, create/advance real witnesses, provision roots, select/procure licensed products, create current-memory/R9B0 admission, or perform another protected effect without Patrick's exact authority.

Fresh exact-head review is mandatory after material head movement.

PR #3 hard gate:
if exact-head peer review + One reconciliation becomes clean, STOP before implementation planning and obtain Patrick's explicit final written-design acceptance.

## Current exact heads

Architecture base:
- PR #2: `712d5b30b45ba9299dcfce0599878cb81db70e8f`

Written/design:
- PR #3: `1da5bc57b0228178300f6ba966d97d1dce807dc1`
- PR #4: `e60bc866ad6893214c14b7dd25e312752dc4c791`
- PR #6: `b191822ecbc95ce120384acf1c17289b4b834033`

Transaction/evidence chain:
- PR #14: `e9fb2751e75379ae901de5dcf539cc64cc2f109d`
- PR #15: `c79a13b3d6995cfccfc2f6c80b89c7dca367e0a0`
- PR #17: `30cccddc0eb2ec476d97c3c6166cc71d2b31b7fb`
- PR #18: `0c7a764486e7bb758915e8bbe767fc5ea6f9416a`
- PR #20: `dfb66be6b39ee66a270f1f29fd25de24790affb1`

Trust/governance/time:
- PR #21: `abeaf69774eefe96701e7db73cd54e24dc5294b6`
- PR #22: `a6377627f73fed5a396ea9606e02b17dbdd92392`
- PR #23: `705e0a9c2aa0143091761a2eb875213e1c24832e`
- PR #24: `57039cecbc8aa8bbf41ae2bf56a037d50a03db5b`

Integration/shared primitive:
- PR #19: `ef017dba6d04da33275ead7d316d70782474a947`
- PR #25: `7e760c0f1bd4384a079948a20dba1cdef188f0dc`

All were OPEN / DRAFT / UNMERGED / MERGEABLE at the final exact-head sweep; PR #19 briefly reported false mergeability immediately after head movement, but exact compare showed ahead-only and subsequent readback was mergeable.

## PR #3 — R6 review status

Exact head:
`1da5bc57b0228178300f6ba966d97d1dce807dc1`

Thirteen exact-head disposition:
`NO DEFECT FOUND` on the prior evaluator-context/equivalence/currentness blockers.

Accepted points:
- changed consulted evaluator context => distinct experiment identity;
- equivalence is separate derived relation;
- no evaluator self-issued irrelevance;
- mechanical dependency/noninterference proof or deterministic paired replay;
- exact evaluator/configuration + claim-scope binding;
- fail-closed unknown dependency edges;
- integrity vs read authorization separation;
- coherent run-level context cut / deterministic multi-cut join.

Non-blocking Thirteen note:
eventual verifier-independence profile must define actual failure-domain independence where needed; a differently named process is not enough.

Other peer facets + One reconciliation remain pending.
Do NOT infer Patrick acceptance gate reached.

## PR #4 — definition-policy authority repair

Thirteen reviewed predecessor:
`1fd7767a6516dd9efab8eb6b74fdd8f97cf23407`

Disposition:
`CHANGES_REQUIRED`

Blockers:
- claim/dependency definition could itself be weakened without rooted definition authority;
- high-consequence upward restoration independence was only SHOULD-level.

Current successor:
`e60bc866ad6893214c14b7dd25e312752dc4c791`

New artifact:
`docs/research/2026-09-19-component-evidence-definition-authority-and-restoration-independence-v2.md`

Blob:
`8c40ddbfe2730c7f775e1039557415c672a9a0c8`

Repair:
- EvidenceClaimPolicySubject unifies claim definition, RequiredDependencySpecification, envelope semantics, restoration matrix, evidence/currentness/independence policy;
- ClaimDefinitionAuthorityReceipt binds predecessor/delta/authority/scope/approvals;
- unauthorized changes => `DEFINITION_AUTHORITY_UNRESOLVED`;
- THIRD_PARTY_* owner predicates cannot be silently removed/redefined;
- dependency removal is high-risk semantic change;
- HIGH_CONSEQUENCE restoration requires explicit authority-approved RestorationIndependencePolicy;
- missing/unknown/stale independence policy fails closed;
- independence is failure-domain/profile-specific, not a second process name.

Fresh peer rereview pending.

## PR #21 — exact witness equality / commit authority repair

Thirteen reviewed predecessor:
`2b4d5da33d9ce7dfe4d13c44a07bcd2f1c469120`

Disposition:
`CHANGES_REQUIRED`

Blockers:
- generic admissible descendant/equivalent could bypass exact protected-head witness;
- witness advancement lacked distinct commit authority.

Current successor:
`abeaf69774eefe96701e7db73cd54e24dc5294b6`

New V3 artifact:
`docs/research/2026-09-19-trust-state-exact-witness-equality-and-commit-authority-v3.md`

Blob:
`a4cfbc5d5ee23ee17691ba2792619c2d4dcfd3fb`

Repair:
- protected currentness requires exact candidate-node digest equality to uniquely resolved TrustStateHeadWitness;
- generic descendant/equivalent shortcut removed;
- authorized descendant not witnessed => `TRUST_STATE_PENDING_NOT_CURRENT` / authorized-not-committed;
- equivalence/alias only when itself protected-committed;
- transition authority and witness-commit authority are distinct;
- TrustStateWitnessCommitAuthorizationReceipt binds predecessor witness, successor node, scope, commit authority/quorum/profile, conflict check, resulting witness.

PR #22 was rebound to this exact PR #21 head:
- current PR #22 head `a6377627f73fed5a396ea9606e02b17dbdd92392`
- companion blob `71df0e06e8a8fd06a242c860ec1ecdb6a8c09867`

Fresh peer rereview pending.

## Transaction/evidence hostile review — Thirteen

Thirteen reviewed:
- PR #14 `ec6dc0c1...`
- PR #15 `78b62ccb...`
- PR #17 `30cccddc...`
- PR #18 `13d0a5c6...`
- PR #20 `dfb66be6...`
- PR #19 `107e426e...`

Bus return:
`messages/20260919T1242-thirteen-to-vera-abil-transaction-evidence-v2-hostile-review.md`
blob `11b7d7cbdc84ed52914e26567229c0b59c8e2161`

Disposition:
`CHANGES_REQUIRED`

Blocking finding:
protected replay/evidence witnesses were independent from judged stores but lacked a required unique/serialized predecessor-bound advancement property. Two incompatible successors could both appear committed before a later fork was discovered, while PR #15 already relied on witness advancement as a dispatch safety barrier.

Material finding:
replay/evidence coherent operation-cut binding was advisory where required axes need an exact aggregate/ordered revalidation rule.

Question:
witness authority/root currentness needed explicit non-circular currentness.

## PR #25 — shared ProtectedHeadWitness primitive

New draft PR #25:
`Research protected-head witness semantic primitive`

Exact head:
`7e760c0f1bd4384a079948a20dba1cdef188f0dc`

Artifact:
`docs/research/2026-09-19-protected-head-witness-semantic-primitive-v1.md`

Blob:
`fa5a883551d92fd35b73f0ad6bd5456caf81ffd0`

Core semantics:
- one reusable `ProtectedHeadWitness`;
- `CURRENT(scope) := candidate == unique_current_witness(scope).successor`;
- predecessor-bound atomic/linearizable/consensus-equivalent unique advancement;
- two incompatible successors from one predecessor cannot both receive `CURRENT_COMMITTED`;
- ProtectedHeadCommitReceipt;
- WitnessAuthorityReadReceipt;
- no circular witness authority;
- split-brain currentness fails closed;
- readback is part of commit evidence;
- authorized candidate vs uniquely current head separation;
- multi-head operations use aggregate ProtectedOperationCutCommit OR explicit independent-head ordering/revalidation;
- MultiHeadOperationCutReceipt.

No concrete CAS/consensus/quorum/provider implementation is selected.

## PR #14 — replay binding to PR #25

Current head:
`e9fb2751e75379ae901de5dcf539cc64cc2f109d`

New V3:
`docs/research/2026-09-19-replay-ledger-protected-head-primitive-binding-v3.md`

Blob:
`95081ef0418e871853e25220065d13cd38f8e219`

ReplayLedgerHeadWitness specializes PR #25.
Concurrent incompatible replay successors cannot both become CURRENT_COMMITTED.
Replay witness authority currentness is explicit/non-circular.

## PR #18 — evidence binding to PR #25

Current head:
`0c7a764486e7bb758915e8bbe767fc5ea6f9416a`

New V3:
`docs/research/2026-09-19-evidence-ledger-protected-head-primitive-binding-v3.md`

Blob:
`eed2febf81fb11ccf956435d7d22d2819ccecf77`

EvidenceLedgerHeadWitness specializes PR #25.
Required partition closure is inside the exact committed successor cut.
Concurrent incompatible complete evidence cuts cannot both be CURRENT_COMMITTED.

## PR #15 — dispatch multi-head operation cut

Current head:
`c79a13b3d6995cfccfc2f6c80b89c7dca367e0a0`

New V3:
`docs/research/2026-09-19-dispatch-multi-head-operation-cut-binding-v3.md`

Blob:
`ac70aec499b87fb46ae440ad5aa30c49178b3283`

Repair:
- dispatch may rely on a protected witness only if PR #25 uniqueness semantics hold;
- every multi-head protected operation profile MUST select:
  A. aggregate ProtectedOperationCutCommit; or
  B. explicit independent-head ordering/invalidation/revalidation;
- replay/evidence coherent binding is mandatory when both are required;
- final dispatch fence validates the exact multi-head cut before effect-possible boundary.

## PR #17 / PR #20 supporting hardening

PR #17 current:
`30cccddc0eb2ec476d97c3c6166cc71d2b31b7fb`

V2 blob:
`70e36a80d1eb2846f2c481f3f83e4aea8bde9353`

Current reconciliation derives from current EvidenceLedgerHeadWitness cut + immutable resolution lineage + producer/reviewer provenance.

PR #20 current:
`dfb66be6b39ee66a270f1f29fd25de24790affb1`

V2 blob:
`3dab8fce11adf1c8f8414150b76ebaaf232b046f`

Authenticated transport/intermediary/checkpoint != authenticated evidence origin.
Producer chain/transformation provenance + current trust/root/time cuts are explicit.

## PR #19 current integration subject

Current head:
`ef017dba6d04da33275ead7d316d70782474a947`

V4 rebind:
`docs/research/2026-09-19-research-integration-claim-lattice-v4-rebind.md`

Blob:
`fd6415925da83077c27106b20e4b60052ffa7a90`

V4 adds PR #25 and binds the current PR #14/#15/#18 successors.

## Current Bus review request

Latest Vera review request:
`messages/20260919-vera-abil-protected-head-rereview-v1.md`

Message commit:
`31223ddc2ae0a9fecd03bda59c46178cde687860`

Vera HEAD update:
`91548e9f495e51b220729d15182d6bd66014d216`

Round:
`ABIL-PROTECTED-HEAD-REREVIEW-V1-20260919`

Recipients:
Thirteen, Six, Nine, Four, One.

Requested review focus:
- exact uniqueness/serialization closure;
- witness authority non-circularity;
- split-brain/partition behavior;
- replay/evidence coherent multi-head cut;
- primitive minimality;
- exact-head reconciliation.

No new peer return had landed after this request at final lane check.

## Immediate next actions

1. Fresh-check PR #3/#4/#14/#15/#18/#19/#21/#22/#25 heads before using any review status.
2. Fresh-check Bus lanes for:
   - Thirteen response to protected-head rereview;
   - Six failover/crash review;
   - Nine dependency/currentness review;
   - Four minimality review;
   - One reconciliation.
3. PR #3:
   - preserve exact head;
   - Thirteen facet is clean;
   - do not ask Patrick for acceptance until all required peer facets + One reconciliation are clean.
4. PR #4:
   - inspect fresh review against `e60bc866...`;
   - repair only material exact-head findings.
5. PR #21/#22:
   - inspect fresh review against `abeaf697...` + `a6377627...`;
   - no descendant shortcut or witness-commit authority regression.
6. PR #14/#15/#18/#25:
   - inspect exact-head hostile review against shared uniqueness primitive;
   - if PR #25 head moves, all dependent review credit becomes stale.
7. PR #19:
   - V4 is the current integration rebind;
   - old V2/V3 head bindings remain provenance only.
8. Keep all reviewed heads frozen pending peer feedback.
9. No merge/protected effect.
