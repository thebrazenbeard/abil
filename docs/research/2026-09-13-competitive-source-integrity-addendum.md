# Competitive Scan Source-Integrity Addendum

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / CURRENTNESS-BOUND TO 2026-09-13**

Date: 2026-09-13

Parent research PR: Draft PR #5

## Purpose

This addendum rechecks the strongest current-market / academic claims in the control-reconstruction competitive scan against direct or primary sources and records one additional adjacent competitor class surfaced during verification.

It does not change the ABIL architecture or create implementation/product authority.

## Verified current examples

### Dorn Systems

Current Dorn Systems material explicitly markets an AI-augmented controls workflow including:

- Ladder Logic and Structured Text generation;
- explanation and reverse engineering of legacy routines;
- ingestion of legacy PLC-5 / SLC / Siemens project artifacts;
- human-readable routine/rung narratives and I/O maps;
- modernization / translation to newer control platforms;
- human engineer review and field commissioning.

Research consequence: `AI writes PLC code`, `AI explains legacy ladder`, and `AI helps translate a known old PLC project` are plainly occupied claims, not ABIL differentiation.

Source:
- https://dornsystems.com/

### Ri Tech

Current Ri Tech material describes its shipping IEC 61131 Crosswalk as a structured, reviewable source-to-target migration engine rather than a clean-sheet rewrite. Its current site lists legacy Allen-Bradley, Schneider, Siemens, GE/Emerson, Mitsubishi, and Omron families and states that vendor-specific behaviors are flagged for engineering review rather than silently guessed.

Ri Tech also currently ships an IEC 61131 -> IEC 61499 transpilation path and publicly positions `transform what exists` as the first stage of its modernization ecosystem.

Research consequence: when an intact trustworthy source project exists, structured transformation is a serious baseline ABIL must beat or complement. ABIL should treat usable source as evidence, not force behavioral reconstruction into every migration.

Sources:
- https://ri-tech.app/solutions/legacy-plc-modernization
- https://ri-tech.app/solutions/iec-61131-to-iec-61499
- https://ri-tech.app/roadmap

### White Box Networks PLC reverse engineering

The Journal of Intelligent Manufacturing article `Reverse engineering for programmable logic controller structure estimation via white box networks` was published online in 2025 and appears in the 2026 volume. The paper explicitly frames PLC restoration as reverse engineering of internal functional structure and evaluates reconstruction of ladder-logic functional blocks from PLC input/output signals.

Research consequence: interpretable/symbolic PLC-structure reconstruction from behavior is an active research area. ABIL cannot claim novelty merely for recovering interpretable logical structure from I/O traces.

Source:
- https://link.springer.com/article/10.1007/s10845-025-02651-z

### Domain-aware LLM PLC generation

The Journal of Systems and Software article `Integrating domain knowledge and large language models for automatic generation of function block-based PLC logic in maritime systems` describes an LLM/RAG pipeline that combines function-block manuals, normalized I/O descriptions, graph relationships, structured planning, and a rule-based IEC 61131-3 Structured Text generator.

Research consequence: turning structured engineering knowledge into structurally valid PLC logic is not a sufficient moat. ABIL's hard problem is earning/reconciling the machine model and validating its supportable operating envelope.

Source:
- https://www.sciencedirect.com/science/article/abs/pii/S0164121226002244

## Additional adjacent competitor: PLC Copilot

Current PLC Copilot material explicitly markets legacy PLC explanation/reverse-engineering workflows across Ladder Logic, Function Block Diagram, and Structured Text, including vendor-agnostic analysis of old programs and project-aware explanation.

A current PLCs.ai article also makes a useful competitive point: adding more PLC context to a general LLM does not itself solve context curation, conflict resolution, currentness, or error handling.

Research consequence:

- project/code understanding is increasingly commoditized;
- merely noticing that sources can conflict is also not unique;
- ABIL must demonstrate **mechanical evidence arbitration** across source/project artifacts, installed behavior, topology/currentness, technician evidence, and explicit unknowns rather than only describe that conflict as a concern.

Sources:
- https://plccopilot.com/
- https://plccopilot.com/blogs/how-to-reverse-engineer-undocumented-plc-programs
- https://www.plcs.ai/blog/give-an-llm-more-plc-context

## Claim correction / precision

The parent scan's strongest differentiating statement should continue to be treated as a **hypothesis**, not a market-fact claim:

> source-optional, evidence-driven reconstruction of the installed physical machine itself.

The current evidence reviewed here did not surface a clearly equivalent end-to-end commercial product that combines all of ABIL's proposed evidence arbitration, targeted technician grounding, unknown-state quarantine, coverage accounting, coexistence-first migration, and separately validated replacement-control path.

That is not proof none exists. It only supports continuing to test the narrower hypothesis.

## Competitive pressure added to the benchmark

The source-optional benchmark should therefore include at least one project/code-aware AI baseline, not only a generic LLM or traditional engineer. The baseline should be allowed to ingest whatever source/project evidence the profile permits and to explain/translate that program using contemporary controls-specific AI tooling.

ABIL earns reconstruction credit only for value beyond that source-aware baseline, such as:

- discovering installed behavior that conflicts with the project;
- preserving currentness/provenance instead of silently choosing one source;
- reducing technician archaeology under partial/absent source;
- correctly quarantining behavior not established by any evidence path;
- proposing discriminating evidence when source and installed behavior disagree.

This makes the benchmark harder and more realistic.

## Disposition

The verification strengthens rather than overturns the parent research conclusion: adjacent tools are rapidly commoditizing PLC code generation, explanation, migration, and structure recovery. ABIL's defensible value, if it exists, must be demonstrated in the governed reconstruction loop and evidence discipline around the actual installed machine.

No architecture-head movement, implementation planning, machine access, commissioning, procurement, merge, deployment, publication, licensing, or other protected effect follows from this addendum.