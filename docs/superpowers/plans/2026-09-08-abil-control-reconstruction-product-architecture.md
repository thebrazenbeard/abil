# ABIL Control Reconstruction Product Architecture Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update ABIL's living product documentation so the repository clearly defines a coexistence-first, replacement-capable brownfield control-system reconstruction appliance while preserving the frozen 2026-09-06 F0/R1 evidence as historical provenance.

**Architecture:** The living docs will distinguish the long-term product from the current F0 learning substrate. ABIL will default to observing and working with surviving PLC logic, optionally use the PLC as a deterministic execution proxy, and replace ordinary PLC control logic with a separate ABIL deterministic control runtime only when necessary. Safety authority remains independently bounded.

**Tech Stack:** Markdown documentation; Git/GitHub; no production code change in this plan.

**Spec:** `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md`

## Global Constraints

- Preserve the exact historical meaning of the 2026-09-06 foundation/F0 design and its frozen R1 review; do not rewrite history.
- Default product strategy is **replacement-capable, coexistence-first**.
- Existing ordinary PLC logic is preferred as an execution partner when practical.
- Direct ABIL takeover of ordinary PLC control is a separately qualified capability promotion.
- Safety PLCs, safety relays, E-stops, guard circuits, hardwired interlocks, and other independent safety functions remain authoritative unless a separate explicitly engineered safety project changes that contract.
- The intelligence/commissioning plane must remain distinct from the deterministic control runtime.
- Read-only F0 remains a development/qualification stage, not the final product definition.
- No production code, machine connection, deployment, credential/provider mutation, or merge is part of this documentation update.

---

### Task 1: Reframe the README around the actual end product

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: successor product architecture spec.
- Produces: repository-level product summary used by all later documentation.

- [ ] **Step 1: Preserve Patrick's current recovery concept while editing it into durable product language**

Keep the core scenario intact: unsupported control/HMI system fails, ABIL appliance is inserted, discovers surviving network/I/O, supports guided manual commissioning, learns behavior and semantics, synthesizes replacement automation, and can become the permanent controller.

Replace the current unstructured concept paragraph with a concise staged workflow that explicitly distinguishes:

1. discovery/observation;
2. coexistence with surviving PLC logic;
3. PLC execution-proxy mode;
4. direct ABIL deterministic control takeover when needed.

- [ ] **Step 2: Correct the current product-definition sentence**

Replace the statement that ABIL is simply "intended to run alongside existing controls rather than replace them" with language equivalent to:

> ABIL should work with surviving controls by default, but it is ultimately capable of reconstructing and replacing ordinary brownfield control logic when the existing control system cannot remain viable.

- [ ] **Step 3: Expand the architectural stance from four responsibilities to the successor architecture**

Document these responsibilities explicitly:

- industrial discovery/adapters;
- machine-model learning and semantic grounding;
- operator commissioning/diagnostics;
- control-model synthesis and validation;
- deterministic control runtime;
- independent safety/action authority.

State that the learning/intelligence plane does not directly freestyle-control machine outputs.

- [ ] **Step 4: Replace the old development ladder with the successor ladder**

The README ladder should summarize:

`synthetic -> replay -> passive live discovery -> guided semantic commissioning -> bounded manual controls -> reconstructed machine model -> generated candidate control -> replay/simulation/shadow validation -> PLC proxy -> supervised cutover -> direct remote-I/O control when required -> permanent runtime`

- [ ] **Step 5: Update the document index**

Add:

- `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md` — successor product/control architecture.

Label the 2026-09-06 foundation design and F0 plan as the frozen/narrower first technical slice rather than the complete product end-state.

- [ ] **Step 6: Review README for contradictions**

Search for language that still implies ABIL can never replace controls or that bounded autonomy is the only terminal capability. Remove those contradictions while retaining the current no-production-code status.

- [ ] **Step 7: Commit**

```bash
git add README.md
git commit -m "docs: define ABIL as coexistence-first control reconstruction"
```

---

### Task 2: Expand the product thesis from analytics wedge to control-system reconstruction

**Files:**
- Modify: `docs/PRODUCT_THESIS.md`

**Interfaces:**
- Consumes: README framing and successor architecture spec.
- Produces: canonical living statement of customer problem, end product, commercial wedge, and replacement capability.

- [ ] **Step 1: Expand the problem statement**

Add failure modes where the machine remains mechanically useful but the control stack is unsupported, locked, damaged, obsolete, undocumented, or dependent on hardware/software that can no longer be serviced.

- [ ] **Step 2: Rewrite the product proposition**

The proposition must state both phases:

- ABIL first learns and reconstructs the surviving machine/control environment;
- ABIL can then either cooperate with surviving PLC logic or replace ordinary control behavior with its own validated deterministic runtime.

- [ ] **Step 3: Define the primary recovery/customer scenario**

Describe a manufacturer with valuable automated equipment whose HMI/supervisory PC or ordinary PLC control stack can no longer be supported. The commercial objective is to restore supportable machine operation without forcing wholesale mechanical/electrical replacement.

- [ ] **Step 4: Correct "What ABIL is not"**

Remove any blanket statement that ABIL is not a replacement PLC.

Replace it with narrower exclusions:

- not an automatic safety-system replacement;
- not an unrestricted learning policy directly driving outputs;
- not a promise to overwrite arbitrary vendor PLC projects;
- not a claim that network discovery alone reveals functional semantics.

- [ ] **Step 5: Preserve the early commercial wedge while distinguishing it from the end product**

State clearly:

> Read-only shadow mode is the first technical/commercial wedge because ABIL must first prove machine-specific learning. It is not the final product boundary.

- [ ] **Step 6: Add coexistence-first migration value**

Explain that surviving PLCs can remain useful as evidence sources, deterministic execution proxies, permanent execution targets, or replaceable legacy components.

- [ ] **Step 7: Add long-term success conditions**

Require evidence that ABIL can:

- reconstruct useful machine semantics with targeted rather than exhaustive labeling;
- generate an inspectable control model;
- validate generated automation;
- coexist with existing PLC logic where that is best;
- replace ordinary PLC behavior where necessary;
- remain supportable as a permanent system.

- [ ] **Step 8: Commit**

```bash
git add docs/PRODUCT_THESIS.md
git commit -m "docs: expand ABIL product thesis to control replacement"
```

---

### Task 3: Rebuild the architecture boundaries around coexistence, synthesis, and deterministic control

**Files:**
- Modify: `docs/ARCHITECTURE_BOUNDARIES.md`

**Interfaces:**
- Consumes: successor architecture spec.
- Produces: living system-boundary contract for future implementation and review.

- [ ] **Step 1: Replace the current four-box diagram**

Use a diagram equivalent to:

```text
Existing machine / surviving controls
        |
        v
Discovery + industrial adapters
        |
        v
Machine-model / intelligence plane
        |
        +----> Operator commissioning + diagnostics
        |
        +----> Control-model synthesis + validation
                         |
                         v
              Approved control artifact
                         |
                +--------+--------+
                |                 |
                v                 v
       Existing PLC proxy   ABIL deterministic
          / target           control runtime
                |                 |
                +--------+--------+
                         |
                         v
               Ordinary machine I/O

Independent safety systems remain authoritative across all modes.
```

- [ ] **Step 2: Expand industrial adapters into discovery plus protocol capabilities**

Distinguish:

- passive/read-only acquisition;
- topology/configuration discovery;
- commissioning/manual action capability;
- deterministic write/control capability.

State that qualification for one capability does not imply qualification for another.

- [ ] **Step 3: Add a first-class semantic-grounding/commissioning boundary**

Document the loop:

`observe -> propose candidate relationship -> constrained technician action -> measure consequences -> technician confirm/correct semantics -> retain provenance -> update machine model`.

- [ ] **Step 4: Split intelligence from deterministic execution**

State mechanically that:

- learner/LLM/ML components may propose or synthesize candidate control artifacts;
- only a validated promoted artifact enters the deterministic runtime;
- learning does not mutate production control logic continuously or implicitly.

- [ ] **Step 5: Define PLC coexistence roles**

Document the PLC as possible:

- evidence/configuration source;
- deterministic proxy;
- permanent execution target;
- replaceable controller.

Direct vendor-project rewriting is target-specific, not a universal ABIL mechanism.

- [ ] **Step 6: Add direct-control runtime requirements**

Require explicit treatment of:

- deterministic state/sequence execution;
- timers;
- ordinary permissives/interlocks;
- I/O scheduling/update semantics;
- watchdog/fail-closed behavior;
- protocol-specific runtime qualification;
- execution evidence and alarms.

Do not select the runtime language or RTOS in this documentation pass.

- [ ] **Step 7: Strengthen the safety boundary**

Retain existing safety PLC/relay/hardwired authority and explicitly say that ordinary control reconstruction does not authorize inferred reconstruction of certified safety logic.

- [ ] **Step 8: Reframe persistence**

Persistent state should now distinguish:

- discovered topology;
- signal/device identities;
- operator semantics with provenance;
- learned machine model;
- evidence/history;
- candidate control models;
- promoted control artifact/version;
- runtime configuration;
- deployment identity.

Do not imply all of this exists before ABIL first commissions a machine.

- [ ] **Step 9: Commit**

```bash
git add docs/ARCHITECTURE_BOUNDARIES.md
git commit -m "docs: define coexistence and deterministic control boundaries"
```

---

### Task 4: Extend the field-validation roadmap through permanent control replacement

**Files:**
- Modify: `docs/FIELD_VALIDATION_ROADMAP.md`

**Interfaces:**
- Consumes: product thesis and architecture boundaries.
- Produces: staged capability/evidence ladder from F0 research to permanent controller.

- [ ] **Step 1: Preserve Stages 0-3 as early evidence stages**

Do not weaken synthetic, replay, passive shadow, or operator-facing evidence requirements.

- [ ] **Step 2: Replace the current late-stage ladder with explicit reconstruction stages**

Use stages equivalent to:

- Stage 4 — guided semantic commissioning;
- Stage 5 — constrained manual-control gateway;
- Stage 6 — machine-model reconstruction;
- Stage 7 — candidate control synthesis;
- Stage 8 — replay/simulation/shadow validation;
- Stage 9 — existing-PLC execution proxy;
- Stage 10 — supervised cutover;
- Stage 11 — direct remote-I/O control where needed;
- Stage 12 — permanent ABIL control runtime and support lifecycle.

- [ ] **Step 3: Add promotion evidence per stage**

For each write-capable or replacement stage require explicit evidence for:

- exact hardware/protocol/deployment identity;
- capability boundary;
- operator authorization;
- deterministic behavior/timing;
- rollback/recovery;
- comparison against expected machine behavior;
- alarm/fault handling;
- independent safety authority.

- [ ] **Step 4: Add coexistence-versus-replacement decision evidence**

Record why a target installation remains in PLC-proxy mode or advances to direct ABIL control. Valid reasons may include supportability, locked/inaccessible project state, failed controller, hardware obsolescence, protocol availability, deterministic performance, maintainability, and rollback risk.

- [ ] **Step 5: Expand core evaluation metrics**

Add:

- semantic-grounding efficiency;
- topology/device discovery coverage;
- reconstructed control-model fidelity;
- generated-control validation pass/fail evidence;
- deterministic cycle/jitter/resource metrics where direct control is tested;
- recovery/rollback time;
- commissioning labor;
- permanent supportability.

- [ ] **Step 6: Expand kill conditions**

Add kill/revision conditions if:

- reconstruction requires essentially full manual re-engineering;
- generated control cannot be made inspectable/testable;
- direct control cannot meet target timing/reliability;
- protocol/vendor diversity makes every deployment a bespoke rewrite;
- coexistence with surviving PLCs consistently outperforms direct takeover at lower risk/cost, forcing product emphasis to shift.

- [ ] **Step 7: Commit**

```bash
git add docs/FIELD_VALIDATION_ROADMAP.md
git commit -m "docs: extend ABIL validation through control takeover"
```

---

### Task 5: Update the competitive framing for the stronger product thesis

**Files:**
- Modify: `docs/COMPETITIVE_REALITY_CHECK.md`

**Interfaces:**
- Consumes: revised product thesis.
- Produces: competitive boundary that distinguishes ABIL from analytics-only tools and from conventional one-off controls integration.

- [ ] **Step 1: Preserve existing analytics commoditization findings**

Keep the warning that anomaly detection, tag monitoring, forecasting, and predictive maintenance are not sufficient differentiation.

- [ ] **Step 2: Add the new competitive category boundary**

Explicitly distinguish ABIL's stronger target from:

- predictive-maintenance analytics;
- historian dashboards;
- AI copilots that explain manuals/alarms;
- PC-based PLC runtimes that still require conventional engineering/programming;
- one-off control-system integrator migrations.

- [ ] **Step 3: State the new moat hypothesis cautiously**

The possible differentiated capability is not "AI controls machines." It is:

> machine-specific reconstruction that combines topology discovery, targeted semantic grounding, learned behavioral structure, inspectable control synthesis, coexistence-first migration, and a validated path to permanent replacement control.

Mark this as unvalidated until demonstrated.

- [ ] **Step 4: Add new commercial risks**

Include:

- fieldbus/protocol breadth;
- deterministic-runtime engineering;
- vendor-project access/compatibility;
- commissioning labor;
- liability/safety boundary management;
- support lifecycle of a permanent controller.

- [ ] **Step 5: Commit**

```bash
git add docs/COMPETITIVE_REALITY_CHECK.md
git commit -m "docs: update ABIL competitive thesis for control reconstruction"
```

---

### Task 6: Reconcile successor docs against frozen R1 provenance

**Files:**
- Modify: `README.md`
- Modify: `docs/PRODUCT_THESIS.md`
- Modify: `docs/ARCHITECTURE_BOUNDARIES.md`
- Modify: `docs/FIELD_VALIDATION_ROADMAP.md`
- Modify: `docs/COMPETITIVE_REALITY_CHECK.md`
- Read-only verify: `docs/superpowers/specs/2026-09-06-abil-foundation-design.md`
- Read-only verify: `docs/superpowers/plans/2026-09-06-abil-f0-shadow-pilot.md`
- Read-only verify: `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md`

**Interfaces:**
- Consumes: all preceding documentation tasks.
- Produces: coherent living product documentation with historical boundaries intact.

- [ ] **Step 1: Verify no old historical source was rewritten**

Confirm the 2026-09-06 foundation design and F0 plan retain their original reviewed meaning.

- [ ] **Step 2: Search living docs for stale terminal-product language**

Search for phrases equivalent to:

- "rather than replace";
- "not a replacement PLC";
- "bounded autonomy" as the final product stage;
- any statement that read-only shadow mode is the final product.

Correct stale living-doc statements while leaving historical docs unchanged.

- [ ] **Step 3: Search living docs for unsafe overreach**

Verify there is no claim that ABIL:

- automatically replaces safety logic;
- can infer safety requirements from observed behavior;
- can safely overwrite arbitrary vendor PLCs;
- can treat discovery metadata as proven functional semantics;
- can let the learning plane directly self-modify the running deterministic controller.

- [ ] **Step 4: Verify the coexistence-first rule is consistent everywhere**

Every living document should support the same default:

> Work with surviving PLC logic when practical; replace ordinary PLC control only when coexistence is impossible, undesirable, unsupported, or uneconomic.

- [ ] **Step 5: Verify the product packaging claim remains a direction, not a frozen implementation choice**

The docs may describe an industrial mini-PC/appliance and bootable installer/recovery image, but must not yet bind the product to Tiny Core, Debian, a specific RT kernel, or a specific runtime language.

- [ ] **Step 6: Commit any reconciliation-only fixes**

```bash
git add README.md docs/PRODUCT_THESIS.md docs/ARCHITECTURE_BOUNDARIES.md docs/FIELD_VALIDATION_ROADMAP.md docs/COMPETITIVE_REALITY_CHECK.md
git commit -m "docs: reconcile ABIL successor architecture"
```

---

### Task 7: Review and hand off the successor documentation PR

**Files:**
- Review all changed documentation files.

**Interfaces:**
- Consumes: completed documentation updates.
- Produces: reviewable successor source; no merge.

- [ ] **Step 1: Compare the branch against the current base**

Expected changed files should be limited to the successor spec, this implementation plan, and the living documentation files explicitly named above.

- [ ] **Step 2: Verify the PR summary states the provenance boundary**

The PR body must say:

- current 2026-09-06 F0/R1 failure remains frozen evidence;
- this PR defines successor product architecture;
- no production control code or machine authority is introduced;
- implementation/qualification of the successor architecture remains future work.

- [ ] **Step 3: Mirror the external ABIL PR to the Chat Communication Bus**

Use the current Bus protocol and Vera writer lane. The mirror must identify the ABIL PR number/head and state that it is unmerged successor documentation only.

- [ ] **Step 4: Do not merge**

Leave the PR draft/open for review. Merge remains a protected effect.
