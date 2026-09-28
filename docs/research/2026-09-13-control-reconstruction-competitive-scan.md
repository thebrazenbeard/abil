# Control-Reconstruction Competitive Scan

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / VERIFY BEFORE EXTERNAL CLAIMS**

Date: 2026-09-13

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Question

The current ABIL competitive note correctly says anomaly detection, edge analytics, brownfield connectivity, soft-PLC execution, and conventional controls migration are not moats.

This spike asks a narrower question:

> How close are current commercial and academic efforts to ABIL's stronger claim of machine-specific control reconstruction and validated replacement control?

This is not an exhaustive market study and does not establish freedom to operate, patentability, uniqueness, or customer demand.

## Finding

The competitive boundary has moved closer.

In 2026, it is no longer credible to treat **AI-generated PLC logic**, **AI explanation of legacy ladder/ST**, **legacy-program translation**, or **AI-assisted controls migration** as meaningful differentiation by themselves.

Commercial providers now explicitly market AI-assisted PLC generation and reverse engineering of legacy project files. Other migration products advertise structured cross-platform transformation of existing legacy PLC programs. Academic work is also targeting interpretable PLC-structure reconstruction and automated IEC 61131-3 logic generation.

The evidence reviewed here did **not** surface a clear commercial equivalent to ABIL's full proposed workflow:

> source-optional reconstruction from the behavior and surviving evidence of an unfamiliar physical installation, explicit uncertainty/unknown-state quarantine, targeted technician-guided interventions, evidence-backed machine/control model synthesis, coexistence-first execution, and a separately validated path to permanent replacement control.

That narrower claim is still plausible as differentiation, but it is a claim ABIL must prove rather than assume.

## Closer competitor classes

### 1. AI-assisted PLC engineering and legacy-code reverse engineering

Dorn Systems currently markets an AI-augmented controls-engineering workflow covering ladder/Structured Text generation, explanation of legacy routines, I/O-map generation, modernization, and migration across major PLC platforms. Its site explicitly describes ingesting legacy PLC-5 / SLC / Siemens project artifacts and producing human-readable narratives and modernized equivalents, with engineer review.

Competitive significance:

- `AI writes PLC code` is not ABIL differentiation.
- `AI explains old ladder` is not ABIL differentiation.
- `AI helps migrate a known legacy project to a new platform` is not ABIL differentiation.

The important distinction is evidence source. This class starts from an existing program/project or explicit engineering specification. ABIL's strongest thesis must survive cases where source is missing, stale, locked, incomplete, or behavior has diverged from documentation.

Sources:
- https://www.dornsystems.com/
- https://dornsystems.com/

### 2. Structured legacy-program transformation

Ri Tech currently markets an `IEC 61131 Crosswalk` approach for legacy PLC modernization, describing transformation of proven legacy control logic onto modern target platforms rather than a clean-sheet rewrite.

Competitive significance:

If an intact trustworthy legacy project exists, source-to-source or source-to-target migration may be cheaper, faster, and safer than behavioral reconstruction. ABIL should not force its novel reconstruction machinery into a problem that an existing-project transformer solves directly.

This strengthens the coexistence/evidence principle:

> Existing source code is high-value evidence when available, not an obstacle to the product story.

ABIL's stronger advantage must appear when source artifacts are incomplete/unavailable, when installed behavior differs materially from the project, or when the migration needs independent behavioral/coverage evidence rather than syntactic translation alone.

Source:
- https://ri-tech.app/solutions/legacy-plc-modernization

### 3. Academic PLC reconstruction

A 2025/2026 Journal of Intelligent Manufacturing article describes symbolic `White Box Networks` for recovering functional structure of PLC circuits, motivated by the interpretability/reliability limitations of black-box deep-learning approaches to PLC restoration.

Competitive significance:

Interpretable reconstruction is an active research area. ABIL should not frame symbolic/white-box control recovery as intrinsically novel.

The pressure this creates is useful: ABIL must show that its reconstruction system handles real deployment identity, incomplete observations, temporal behavior, recurring modes, provenance, technician interventions, unknown states, control coverage, restart/fault/recovery semantics, and migration authority—not merely recover logical blocks from a bounded dataset.

Source:
- https://link.springer.com/article/10.1007/s10845-025-02651-z

### 4. Automated IEC 61131-3 logic generation from engineering knowledge

A 2026 Journal of Systems and Software paper describes a domain-aware LLM/RAG workflow for automatic function-block PLC logic generation in maritime systems, using domain knowledge, I/O descriptions, graph-based context, and an IEC 61131-3 generator. The reported research focuses on structured logic generation from supplied engineering knowledge rather than autonomous reconstruction of an unknown installed machine.

Competitive significance:

ABIL cannot claim a moat merely because it can turn structured machine knowledge into syntactically valid control logic. The defensible value, if any, lies upstream in earning the machine model and downstream in validating/promoting it safely.

Source:
- https://www.sciencedirect.com/science/article/abs/pii/S0164121226002244

### 5. Prompt-to-ladder / PLC copilots

Current products and services advertise natural-language ladder generation, HMI generation, simulation, PLC-code explanation, and project-aware troubleshooting.

Competitive significance:

These tools lower the cost of conventional controls engineering. That is a competitive threat even when they do not reconstruct a machine themselves, because they reduce the labor baseline ABIL must beat.

ABIL's economic comparison must therefore be against **AI-augmented controls engineers**, not only traditional manual programming.

Example sources:
- https://www.plcs.ai/blog/what-is-plc-ai
- https://ladderlogicai.com/pages/

### 6. Brownfield edge/AI layers

A large current market class adds a protocol-aware edge layer to surviving PLC/SCADA systems for analytics, anomaly detection, OEE, digital twins, or AI inference while intentionally preserving existing deterministic control.

Competitive significance:

This validates the practicality of the read-only/coexistence wedge but also makes it crowded. ABIL's shadow-mode product will not be differentiated merely because it connects to old equipment and learns from existing signals.

Examples reviewed:
- brownfield edge AI systems that poll mixed PLC fleets through EtherNet/IP/Modbus/OPC-style interfaces;
- brownfield modernization architectures that explicitly keep PLCs in control;
- data-layer modernization products that normalize mixed generations without controller replacement.

These are useful substitutes for customers who need visibility rather than control recovery.

Example sources:
- https://qscompute.com/blog/brownfield-ai-retrofit-legacy-factory-edge-2026
- https://www.dfos.ai/resources/blog/why-brownfield-factories-need-modern-operating-layer
- https://elpisitsolutions.com/solutions-brownfield-modernization

### 7. Conventional controls modernization remains the benchmark

Major automation vendors and controls integrators already migrate obsolete PLC/HMI/control systems using staged assessment, offline validation, commissioning, and rollback planning.

Competitive significance:

ABIL's end state is not unique because a skilled integrator can already replace unsupported controls. The product thesis only becomes stronger if ABIL reduces engineering archaeology and preserves/reuses machine-specific evidence more efficiently than that baseline.

Examples:
- https://process.honeywell.com/us/en/initiative/legacy-plc-migration
- https://www.mescada.com/plc-migration/
- https://axiotech.co.uk/services/controls-modernisation/

## Sharpened moat boundary

The fresh competitive evidence suggests ABIL should avoid broad claims such as:

- `AI for PLCs`;
- `AI-generated ladder logic`;
- `AI reverse engineers PLC code`;
- `AI modernizes legacy controls`;
- `edge AI for brownfield equipment`;
- `vendor-neutral PLC migration`;
- `soft PLC on an industrial PC`.

All of those now have obvious substitutes.

The stronger product hypothesis is instead:

> **Source-optional evidence-driven control reconstruction of the installed machine itself.**

That means ABIL must demonstrate a repeatable ability to combine whatever survives—traffic, configuration, source/project artifacts where available, topology, I/O behavior, timing, operator knowledge, guided interventions, and learned relationships—into an inspectable model with explicit provenance, uncertainty, unknown-state quarantine, and control coverage, then validate a supportable coexistence or replacement target.

The word **source-optional** matters. Source code should be used when trustworthy and available, but the product must not depend on it to create value in the failure cases it is meant to address.

## Competitive falsifiers ABIL should add to its evidence discipline

### Falsifier A — intact-source baseline

When a trustworthy legacy project exists, compare ABIL against a modern AI-assisted/source-transform migration workflow.

If ABIL adds no material value beyond source translation plus ordinary commissioning, do not claim reconstruction advantage for that class of job.

### Falsifier B — source-withheld reconstruction

For a machine whose control source is available to the evaluator, withhold the source from ABIL and require reconstruction from declared machine-visible evidence plus bounded technician interaction.

The evaluator can then compare recovered behavior/coverage against the hidden source and actual machine behavior without leaking the answer to the learner.

This is much closer to the intended product claim than generic anomaly metrics.

### Falsifier C — stale-source conflict

Provide a source/project artifact that disagrees with installed behavior because of later field modifications, replacement devices, operator workarounds, or incomplete backups.

ABIL should preserve the conflict and resolve claims through evidence/provenance rather than blindly privileging source or telemetry.

### Falsifier D — archaeology labor

Measure human engineering time required to reach a supportable reconstruction against:

1. conventional manual reverse engineering;
2. AI-augmented legacy-code analysis/migration;
3. ABIL with source available;
4. ABIL with source withheld or partial.

If ABIL does not reduce the relevant labor or improve evidence quality enough to justify its complexity, the product thesis narrows.

### Falsifier E — behavioral coverage beyond the happy path

Require startup, shutdown, manual mode, jam recovery, reset/restart, fault handling, intermittent conditions, and at least one rare/unobserved transition class.

A system that reconstructs only normal-cycle logic is not a replacement-control product.

## Strategic implication

The competitive threat is not that another company already appears to offer the whole ABIL thesis. The threat is that adjacent tools are rapidly making each **individual** part cheaper:

- code generation;
- legacy-code explanation;
- source migration;
- soft-PLC execution;
- protocol connectivity;
- brownfield analytics;
- digital-twin/simulation support.

Therefore ABIL's moat cannot be a shopping list of those parts.

It has to be the governed reconstruction loop and accumulated deployment capability: how evidence is acquired, attributed, tested, reconciled, converted into an inspectable control model, challenged for unknown states, and promoted into a supportable execution target with less engineering archaeology.

That is a stronger and more falsifiable thesis than `AI PLC replacement`.

## No architecture change required yet

The current PR #2 architecture already points in this direction: coexistence-first, source/provenance separation, guided commissioning, explicit unknowns, control coverage, validation, and multiple execution targets.

This scan therefore does not justify moving the current architecture review head. It does suggest that future field-validation design should explicitly include the intact-source, source-withheld, stale-source-conflict, and archaeology-labor baselines above.

Those are research-derived proposed falsifiers, not current canonical acceptance criteria until separately reviewed/adopted.
