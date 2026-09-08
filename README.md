# ABIL

**Adaptive Brownfield Intelligence Layer**

ABIL is a proposed adaptive reconstruction and control platform for existing industrial equipment and other brownfield physical systems.

The product principle is simple:

> Do not replace a functioning machine just because its software, documentation, vendor support, or tribal knowledge is obsolete. Learn the machine that actually exists.

ABIL should work with surviving controls by default, but it is ultimately intended to reconstruct and replace ordinary brownfield control logic when the existing control system cannot remain viable.

## Product concept

A representative recovery case looks like this:

1. A machine remains mechanically useful, but its HMI/control PC, PLC project, supervisory software, or vendor support becomes unavailable or impractical to recover.
2. An ABIL appliance is connected to the surviving control network and appropriate industrial interfaces.
3. ABIL first determines where ordinary control authority actually lives: supervisory HMI, soft PLC/control PC, PLC/PAC logic, motion/drive control, safety control, mixed, or unknown.
4. ABIL observes and inventories reachable controllers, remote I/O, drives, sensors, valve manifolds, fieldbus nodes, and communication relationships without treating connectivity, names, or metadata as proven functional meaning.
5. If the existing PLC logic still works, ABIL uses it as evidence and, where useful, as the deterministic execution target rather than immediately replacing it.
6. During guided commissioning, a technician manually exercises known machine functions through a separately constrained action path and identifies or confirms the purpose of devices, signals, solenoids, sensors, and sequences.
7. ABIL records operator-supplied semantics separately from relationships learned from timing, state changes, and repeated machine behavior.
8. ABIL builds and revises a machine-specific behavioral/control model with explicit unknowns and a control-coverage ledger.
9. ABIL synthesizes a candidate automation model and validates it through replay, simulation, shadow comparison, held-out/negative transition tests, and technician review before it gains authority.
10. When practical, the existing PLC may remain as a deterministic execution proxy or permanent execution target.
11. When the ordinary PLC/control logic is unsupported, locked, unreliable, failed, uneconomic to preserve, or otherwise unsuitable, ABIL may replace its function with a separately qualified deterministic control runtime that talks directly to remote I/O and field devices.
12. Cutover transfers each physical output/control namespace to exactly one authoritative writer with mechanically enforced fencing; ABIL must not create split-brain control authority.
13. The ABIL appliance can then become the permanent supported ordinary-control computer for that installation.

The default strategy is therefore **replacement-capable, coexistence-first**.

## Current status

**Foundation / research / architecture. No production control code exists yet.**

The repository contains the product thesis, architecture boundaries, validation strategy, competitive reality check, the frozen first F0 learning-substrate design, and a proposed successor control-reconstruction architecture under review. Claims remain hypotheses until demonstrated empirically.

The successor architecture is reviewer-ready but not yet promoted as canonical living architecture. The immediate R2 work remains bounded to a corrected early learning/telemetry substrate; it is not authorization to build write-capable commissioning or production control.

## Product direction

The initial commercial target is brownfield industrial equipment with some combination of:

- legacy or unsupported HMI/SCADA/control software;
- unavailable, locked, stale, or undocumented PLC projects;
- PLC/PAC/remote-I/O/drive/sensor networks;
- accumulated machine-specific quirks and modifications;
- operational knowledge concentrated in a small number of experienced people;
- obsolete controller or fieldbus hardware that is difficult to support;
- equipment that is too valuable, specialized, or mechanically healthy to replace simply for controls modernization.

ABIL should still begin technically in **read-only shadow mode**. The first proof is that it can learn useful machine-specific structure without exhaustive semantic hand-mapping. That is a qualification stage and commercial wedge, not the final product boundary.

Substrate qualification and learner efficacy are separate. A correct substrate must be able to report that a simple baseline wins; the first learner does not have to prove product differentiation in order for the experimental substrate itself to be valid.

## Architectural stance

ABIL is not Noema and is not required to satisfy Noema's research-purity constraints. It may use whichever combination of system identification, time-series learning, causal inference, rules, databases, language models, vision models, and Noema-derived mechanisms best serves the industrial problem.

The product keeps these responsibilities distinct:

1. **Industrial discovery and adapters** — passive observation, bounded reads, active discovery, commissioning, and deterministic control are separate capability levels; `read-only` is not automatically `non-disruptive`.
2. **Machine-model learning and semantic grounding** — learn dynamics, delays, regimes, relationships, uncertainty, and change while keeping human-supplied semantics distinct from learned structure.
3. **Operator commissioning and diagnostics** — support guided manual commissioning, technician confirmations/corrections, evidence inspection, predictions, diagnostics, and proposed tests.
4. **Control-model synthesis and validation** — produce inspectable candidate states, transitions, commands, permissives, timing expectations, alarms, recovery paths, and independently classified ordinary interlocks, with explicit evidence coverage and unknown-state quarantine.
5. **Deterministic control runtime** — execute only an approved promoted control artifact with explicit I/O scheduling, timers, watchdogs, ordinary permissives/interlocks, alarms, and protocol-specific runtime behavior.
6. **Independent safety/action authority** — preserve independent safety systems. Unknown protective/interlock semantics are treated as safety-relevant until independently classified.
7. **Control ownership/fencing** — exactly one authoritative ordinary-control writer per physical output/control namespace during proxy operation, cutover, rollback, and restart.

The intelligence/commissioning plane may keep learning. It must not continuously or implicitly rewrite the running deterministic controller.

## Existing PLC strategy

ABIL should treat an existing PLC as potentially useful as an evidence/configuration source, deterministic execution proxy, permanent execution target, or replaceable legacy controller.

ABIL should not assume it can or should overwrite arbitrary Allen-Bradley, Siemens, Mitsubishi, Omron, Beckhoff, or other vendor projects. Vendor-project rewriting is a target-specific migration path. The universal goal is to reconstruct and support the machine's ordinary control function, not depend on modifying proprietary internals.

## Commercial differentiation target

ABIL should not become another generic anomaly detector, historian dashboard, AI manual explainer, or conventional one-off control migration.

The differentiating target is:

> **Learn how this particular machine works, ground enough of that understanding through targeted technician interaction to reconstruct its control behavior, validate the reconstruction, and preserve or replace the surviving control stack with the least disruptive supportable path.**

A successful ABIL system should eventually answer questions such as:

- What devices and signals are actually present?
- Which relationships are learned from behavior and which were supplied by a human or vendor project?
- Where does ordinary control authority currently live?
- What changed relative to the machine's own history?
- What operating regimes and sequence relationships has the system learned?
- What evidence would distinguish competing explanations?
- What bounded observation or commissioning action would reduce uncertainty?
- Which states/transitions remain unobserved or insufficiently covered for automation?
- Can the existing PLC remain the best execution target?
- If not, can the reconstructed control model be promoted into a deterministic ABIL runtime without bypassing safety or creating competing writers?

## Development and capability ladder

1. Synthetic/headless substrate qualification.
2. Learner-efficacy evaluation on the qualified substrate.
3. Recorded-telemetry replay.
4. Live passive discovery/read-only shadow mode.
5. Operator-facing diagnostics and evidence review.
6. Guided semantic commissioning.
7. Bounded manual controls through an independently constrained action path.
8. Reconstructed machine/control model with control-coverage ledger.
9. Generated candidate control artifact.
10. Replay, simulation, shadow, held-out, and negative-transition validation.
11. Existing-PLC execution-proxy mode where useful.
12. Supervised cutover with explicit single-writer authority transfer.
13. Direct remote-I/O control when replacement is required and separately qualified.
14. Permanent ABIL runtime with ongoing diagnostics and learning outside deterministic execution authority.

Passing one stage does not imply authority for the next.

## Safety boundary

Ordinary control reconstruction does not automatically include safety-system reconstruction.

Existing safety PLCs, safety relays, E-stops, guard circuits, hardwired protective interlocks, drive safety functions, and other independent safety systems remain authoritative unless a separate explicitly engineered safety project changes that contract.

Unknown protective/interlock semantics are safety-relevant and out of autonomous reconstruction until independently classified by qualified engineering evidence. Observed successful operation is not sufficient evidence to recreate or downgrade a protective function.

## Likely product form

The long-term physical product is likely an industrial edge appliance rather than an APK or ordinary desktop application: a rugged/fanless mini-PC, appropriate industrial Ethernet/fieldbus interfaces, bootable install/recovery media, a small Linux-based appliance OS, persistent machine/deployment state, commissioning tools, and a deterministic control runtime.

The exact Linux distribution, real-time strategy, first fieldbus, HMI framework, and controller runtime remain open engineering decisions.

## Documents

- `docs/PRODUCT_THESIS.md` — living problem, customer, value proposition, migration strategy, and end-product thesis.
- `docs/ARCHITECTURE_BOUNDARIES.md` — living system boundaries, coexistence roles, control synthesis, deterministic runtime, ownership/fencing, and safety limits.
- `docs/FIELD_VALIDATION_ROADMAP.md` — staged route from substrate qualification through permanent control replacement.
- `docs/COMPETITIVE_REALITY_CHECK.md` — what is already commoditized and what the stronger reconstruction thesis must prove.
- `docs/superpowers/specs/2026-09-08-abil-control-reconstruction-product-architecture.md` — proposed successor product/control architecture under review.
- `docs/superpowers/plans/2026-09-08-abil-control-reconstruction-product-architecture.md` — documentation implementation/review plan for the successor architecture.
- `docs/superpowers/specs/2026-09-06-abil-foundation-design.md` — frozen narrower first technical slice retained as historical provenance.
- `docs/superpowers/plans/2026-09-06-abil-f0-shadow-pilot.md` — frozen first F0 implementation plan retained as historical provenance.

## Naming

**ABIL = Adaptive Brownfield Intelligence Layer.**

Working phrase: **Make old systems able.**
