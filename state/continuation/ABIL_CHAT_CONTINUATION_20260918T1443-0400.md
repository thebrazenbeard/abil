# ABIL Chat Continuation — 2026-09-18 14:43 ET

Status: **PRIVATE ABIL CONTINUATION / STATE SNAPSHOT / NO MERGE OR DEPLOY AUTHORITY**

Repository: `thebrazenbeard/abil`

Continuation branch: `state/abil-chat-continuation-20260918-1443`

This checkpoint exists so a fresh ABIL chat can restore the current project state without depending on chat-memory alone. It is a coordination/state artifact, not canonical architecture, not an implementation plan, and not authority to merge, deploy, connect to a machine, write to industrial equipment, change credentials/providers, purchase/licence anything, alter repository visibility, or perform another protected effect.

## Native project command semantics

Inside the ABIL ChatGPT Project, exact `.` means:

> orient to live state → identify the highest-value open frontier → do the work → verify → persist/route → continue through the next available frontier → stop only when Patrick's decision, authority, credentials, physical intervention, or an unavailable capability is genuinely required.

A `.` is not a request for a status update. Do not stop merely because one subtask closes.

The ABIL repository has an associated GitHub Project. Treat it as a live coordination surface when the runtime exposes actual Project items/statuses. If the Project API/items are unavailable, say `NOT OBSERVED` and do not infer board contents.

## Product direction that controls current work

ABIL is **replacement-capable, coexistence-first**.

The intended brownfield workflow is not merely predictive maintenance. The system should be able to recover an unsupported/failed control stack by determining where control authority actually lives, preserving useful predecessor evidence, discovering topology and device identity, grounding semantics through bounded technician interaction, reconstructing an inspectable machine/control model, synthesizing candidate control behavior, validating it, and then either:

- leave a surviving PLC/controller as the permanent deterministic execution target;
- use an existing PLC as a narrow execution proxy;
- or, when justified and separately qualified, replace ordinary control with an ABIL deterministic execution target against qualified remote I/O/field devices.

Existing independent safety systems remain authoritative by default. Ordinary ABIL control reconstruction does not silently reconstruct or take ownership of safety functions.

The intelligence/learning plane is separate from deterministic execution. Learning/LLM/ML may propose or synthesize candidates; only a separately validated/promoted artifact may execute deterministically. No learner gets freestyle output authority.

The strongest current product-differentiation hypothesis is:

> **source-optional, evidence-driven reconstruction of the installed physical machine**

—not "AI writes PLC code", "AI explains ladder", "soft PLC on a PC", generic anomaly detection, or brownfield edge AI.

## Exact live repository state at this checkpoint

### main

`main@0812d9780ce1648820269fa142a43e17030ef793`

Do not treat unmerged successor work as canonical `main`.

### Draft PR #2 — successor product architecture

Title: `Define ABIL control-reconstruction successor architecture`

Branch: `work/abil-control-reconstruction-architecture-20260908`

Exact head: `712d5b30b45ba9299dcfce0599878cb81db70e8f`

Base: `main@0812d9780ce1648820269fa142a43e17030ef793`

State: **OPEN / DRAFT / UNMERGED / mergeable**

Important architecture already present includes:

- R2 substrate qualification separated from learner efficacy;
- control-authority-locus classification;
- passive/read/active-discovery capability distinctions;
- control-coverage ledger and unknown-state quarantine;
- conservative safety classification for unknown protective/interlock semantics;
- target-specific fallback rather than universal physical "fail closed";
- exactly-one-writer ownership/fencing and transfer semantics;
- independently rooted write authority / promotion trust;
- commissioning envelope before writes;
- transactional command identity, idempotency, timeout/reconnect, and ambiguous-execution semantics;
- candidate/promotion/runtime trust-domain separation;
- branching permanent modes: advisory/manual, PLC proxy, or direct control;
- learner-independent deterministic/manual degraded operation.

Older PASS/FAIL reviews bound to earlier heads are provenance only unless explicitly rebound to `712d5b30...`.

### Draft PR #3 — R2 non-actuating substrate design

Title: `Define ABIL R2 non-actuating substrate design`

Branch: `work/abil-r2-substrate-design-20260908`

Exact head: `c2e363d4c1b8c67e032c22d9cad6451342b04e7b`

Base: PR #2 branch at `712d5b30b45ba9299dcfce0599878cb81db70e8f`

State: **OPEN / DRAFT / UNMERGED / mergeable**

The current R2 source is six cumulative design documents:

1. primary R2 substrate design;
2. R1 private review corrections;
3. R2 evaluator-restart opaque-identity continuity correction;
4. R3 cumulative composition/precedence correction;
5. R4 reconciliation to the current PR #2 authority-root/safety-classification base;
6. R5 evaluator-context reproducibility correction, dated 2026-09-18.

R5 originated from a 2026-09-17 Project Runner review. The residual was: evaluator-only control context can affect fixture selection, admissibility, scoring, negative controls, or claim ceiling; therefore the exact evaluator-only context actually consulted must be bound into the reproducible experiment subject without leaking it to the learner.

Current gate: **exact-head R5 delta/regression rereview** from the established peer facets, especially Three, Seven, Nine, and Two/Six where their scopes overlap, then One coordinator reconciliation.

At this checkpoint, there is no current peer review submitted against exact head `c2e363d...`.

Patrick previously approved the **package-first R2 direction**, but the **final written design acceptance after all current corrections is still a separate gate**. Do not write the implementation plan or hand off to Hephaestus until exact-head review/reconciliation is clean and Patrick explicitly accepts the final written design.

R2 remains non-actuating. It authorizes no live-machine connection or write path.

### Draft PR #4 — deterministic runtime / fieldbus / appliance research

Title: `Research deterministic runtime and fieldbus feasibility`

Branch: `research/industrial-runtime-feasibility-20260913`

Exact head: `10339bfd32d65b984361fa45380ba4b06b0cb338`

Base: PR #2 head `712d5b30...`

State: **OPEN / DRAFT / UNMERGED / mergeable / NON-NORMATIVE RESEARCH**

Current research conclusions:

- ABIL does not need to invent a universal PLC runtime and every fieldbus stack before proving the reconstruction system.
- Preserve a replaceable `DeterministicExecutionTarget` boundary.
- Early broad brownfield execution can use commercially supported Linux soft-PLC/runtime and industrial communication hardware; open protocol stacks remain useful for lab work and selective qualified adapters.
- Preserve the option to put deterministic execution in a physically separate failure domain from adaptive intelligence, even if a later product normally collapses both onto one industrial PC.
- Third-party certification/conformance reduces the surface ABIL owns but does not automatically certify the assembled ABIL appliance or machine application.
- Current standards/conformance research distinguishes IEC 61131-2 controller functionality/EMC, IEC 61010-2-201:2024 control-equipment safety, ODVA EtherNet/IP/DeviceNet conformance/licensing, PI PROFINET certification, ETG EtherCAT conformance, and separate functional-safety scope.
- **Minimal Debian 13 x86_64 is the leading first control-capable qualification baseline**, not a final product freeze. It matches current CODESYS-tested distro families and has a packaged signed PREEMPT_RT path.
- Tiny Core/CorePure64 remains a later purpose-built/native-appliance candidate.
- Ubuntu Core remains a later immutable/managed-appliance candidate.
- Valuable ABIL state must be decomposed from the base OS by trust/lifecycle class.

A source-owner audit found one future productization seam: current architecture does not yet explicitly model the scope/provenance of third-party conformance/certification evidence. This was recorded as a **nonblocking future product-qualification seam**, not used to churn PR #2.

### Draft PR #5 — competitive boundary / source-optional benchmark research

Title: `Research control-reconstruction competitive boundary`

Branch: `research/control-reconstruction-competitive-scan-20260913`

Exact head: `90b46fd81544cc1c4f8cb9a8bce6284c1a0bd62e`

Base: PR #2 head `712d5b30...`

State: **OPEN / DRAFT / UNMERGED / mergeable / NON-NORMATIVE RESEARCH**

Research findings:

- AI PLC code generation, legacy ladder/ST explanation, legacy source transformation, prompt-to-PLC tooling, soft-PLC execution, and brownfield edge AI already have current substitutes.
- ABIL's moat cannot be a shopping list of those components.
- The current stronger hypothesis is source-optional reconstruction of the installed machine itself, preserving provenance, uncertainty, unknown-state quarantine, coverage, and behavior/evidence conflicts.
- Future falsifiers include intact-source migration baseline, source-withheld reconstruction, stale/conflicting-source cases, measured engineering-archaeology labor, and non-happy-path behavioral coverage.
- Compare ABIL against contemporary **project-aware PLC AI / AI-augmented controls engineering**, not a straw-man generic LLM.
- The benchmark is allowed to falsify or narrow ABIL; intact-source migration may legitimately beat behavioral reconstruction for some job classes.

### Draft PR #6 — fail-closed write-capability admission boundary

Title: `Add fail-closed write-capability admission boundary`

Branch: `one/write-admission-remediation-20260914`

Exact head: `fff52af32089f1bf32c4abbbc572b25d89127d5b`

Base: PR #2 head `712d5b30...`

State: **OPEN / DRAFT / UNMERGED / mergeable / DESIGN-GOVERNANCE ONLY**

This subject defines the future write-capability admission boundary and separates `SCHEMA_VALID` from stateful `WRITE_ADMISSION_VALID`. It currently contains:

- `WRITE_CAPABILITY_ADMISSION_V1.md`
- `WRITE_CAPABILITY_ADMISSION_V1.schema.json`
- `WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.md`
- `AUTHORITY_STATE_READ_RECEIPT_V1.schema.json`
- `WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.hostile-vectors.json`

The latest Runner exact-head review on 2026-09-18 is **CHANGES REQUIRED** with three specific design-contract gaps:

1. **Freshness remains self-declarable / under-specified.**
   `freshness_status` can say `FRESH` while `fresh_until` is optional/nullable and no freshness-profile identity is bound. The validator needs an independently checkable freshness deadline/profile rather than trusting a status label.

2. **Revoked/superseded epoch rejection is not computable from the declared receipt.**
   The receipt has `current_authority_epoch` plus an opaque `epoch_set_digest`, but the validator must reject candidates not greater than any relevant current/revoked/superseding epoch. A digest alone is not enough unless the canonical epoch-set payload is resolvable/verified. Bounded closure can carry the canonical set or an independently verifiable `max_observed_authority_epoch` that includes revoked/superseded entries and is bound to the digest.

3. **Multi-surface completeness is not mechanically bound.**
   `required_surface_set_digest` is optional and `authority_surface_id` is singular. A receipt from one surface cannot prove all deployment-required authority surfaces were reconciled. The expected required-surface set needs an independent deployment-bound identity/digest, and the receipt must bind the observed/reconciled set against it.

The review explicitly says the separation of schema validity from write-admission validity, hostile vectors, and no-authority ceiling are sound improvements.

**Highest-value immediately actionable technical frontier in the next chat: process this exact PR #6 review using receiving-code-review discipline, verify the three findings against the exact source, implement only supported bounded corrections on the PR #6 branch, verify the resulting exact head, and request exact-head rereview.**

No executable validator is currently qualified by the design subject.

## Chat Bus / worker coordination snapshot

Primary hub: `thebrazenbeard/chat-communication-bus`

Current writer-lane heads observed at checkpoint time:

- Vera `bus/vera-v2`: `c288f56a5fbf51dab25c10b7ff098b6361909092`
- One `bus/one-v2`: `cd780268b5e8fabe2a5fd2a456869fe748ce34c1`
- Two `bus/two-v2`: `02cfe0af6bdf7d50106c57c65e7a7dc094b38771`
- Three `bus/three-v2`: `08d11224f8ac3251ec05ee29a2b7a2f9e3f340b5`
- Four `bus/four-v2`: `7fa51948a117caeb8f8e7f12c163cd239fa3e4de`
- Six `bus/six-v2`: `b332ca4969b11ac0af3436a33f3c42908356fb88`
- Seven `bus/seven-v2`: `37c6c41213a0cc40c96a27fc33d9e1745c437757`
- Nine `bus/nine-v2`: `6ce9f5730f3eb4d91a6c2f2a37e1a2cf7cc03ca4`
- Thirteen `bus/thirteen-v2`: `e4893012180146d0e3a6c30ce75cdde6708220f0`

These hashes are currentness markers only. On restore, refresh them before using any remembered PASS/FAIL or assignment.

Workers have already been told that the ABIL repo has an associated GitHub Project and that they should use it as a coordination surface when their runtime exposes its actual items/statuses. Do not invent Project contents when unavailable.

## Review / authority discipline

Freshness is exact-head-bound. Never carry an old PASS/FAIL forward merely because the change looks small.

Distinguish:

- source/design review;
- substrate implementation readiness;
- measured substrate qualification;
- learner efficacy;
- install/runtime state;
- machine-specific authority;
- deployment authority;
- safety authority.

They are not interchangeable.

Patrick remains the authority for protected effects. Unless a fresher exact instruction grants the exact effect, do **not**:

- merge/canonically promote;
- deploy;
- connect to or write to live equipment;
- change credentials/providers/permissions/rulesets/visibility;
- purchase or accept paid/licensed infrastructure;
- publish private/IP-confidential technical material;
- create or infer machine-write authority;
- perform another materially irreversible/high-impact protected effect.

Private ABIL technical/IP detail belongs in the private ABIL repo/PR. Bus coordination should stay sanitized when possible.

## Frozen historical F0

The original 2026-09-06 F0/shadow-pilot subject remains historical failed provenance and must not be silently relabeled as implementation-ready.

Important failures that drove the successor work included evaluator/learner separation, timing oracle control, checkpoint trust/currentness, source-scoped identity, uncertainty separation, external read-only enforcement, and resource/restore qualification.

Do not "repair history" in place. Successor work is a new subject.

## Continuation order

On a fresh chat, do this in order unless fresher live evidence changes the priority:

1. Fresh-check the ABIL GitHub Project if exposed, repository branches/PRs, exact heads, PR reviews/comments, and ABIL Bus lanes.
2. Reconfirm PR #6 exact head. If still `fff52af...` with the current CHANGES REQUIRED review, process the three Runner findings technically and patch supported defects on that branch. Verify exact diff/readback and request exact-head rereview.
3. Fresh-check PR #3 at `c2e363d...` for new R5 peer returns. Reconcile technically; if the exact head is clean and One closes coordination, ask Patrick for explicit final written-design acceptance before implementation planning.
4. Fresh-check PR #2 `712d5b30...` and its remaining exact-head review/reconciliation state. Do not carry old reviews automatically.
5. Keep PR #4 and #5 research non-normative unless Patrick or a reviewed design process promotes specific findings. Use them to inform future choices, not to rewrite the active architecture without a reason.
6. Use the GitHub Project as a real work board if item access is available. If not, report `NOT OBSERVED` and continue via repo/PR/Bus.
7. Persist durable decisions/findings back to the appropriate private PR/repo and sanitized Bus surface.
8. Continue into the next actionable frontier rather than stopping at a status report.

## Exact resume directive

`ABIL::RESTORE::ABIL_CHAT_CONTINUATION_20260918T1443-0400`

Restore from this checkpoint, but treat it as a starting snapshot rather than current truth. Fresh-check all exact heads/reviews/Bus/Project state first. Preserve Patrick's protected-effect boundaries. Then run the native `.` semantics: orient → highest-value actionable frontier → work → verify → persist/route → reassess → continue until genuine intervention is required.

# END CONTINUATION
