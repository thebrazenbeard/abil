# Component Conformance Evidence Boundary Research

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NOT LEGAL OR CERTIFICATION ADVICE / NO PRODUCT-SELECTION AUTHORITY**

Date: 2026-09-18

Parent research PR: Draft PR #4

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Research question

The existing runtime/protocol/compliance research supports using qualified commercial components where that reduces low-differentiation implementation and conformance burden.

The unresolved productization seam is not whether a component has a certificate, declaration, test report, or conformance result.

It is:

> What exact behavior and product boundary does that evidence cover after ABIL integrates the component into a controller appliance and machine application?

A component claim that is real but scoped incorrectly can be more dangerous than having no claim at all.

## Finding

ABIL should eventually treat third-party qualification evidence as a provenance-bearing subject with an explicit scope boundary, not as a boolean `certified=true`.

A useful evidence record must distinguish at least:

1. **direct component evidence** — what the vendor or test body actually qualified;
2. **composition-dependent evidence** — behavior that remains valid only if host, firmware, configuration, protocol role, and integration assumptions stay within the qualified envelope;
3. **ABIL-owned behavior** — logic, orchestration, adapters, timing behavior, authority handling, recovery, generated artifacts, or other behavior introduced by ABIL and therefore not inherited from the component evidence;
4. **machine-application evidence** — installation-specific commissioning, control semantics, machine safety, wiring, environmental conditions, and target validation that cannot be inferred from a component certificate.

## Proposed evidence tuple

A future product-qualification record for a third-party runtime, protocol card, stack, controller, or industrial computer should bind, where applicable:

- component manufacturer/vendor;
- exact product/model identity;
- hardware revision;
- firmware version;
- software/runtime/stack version;
- driver version;
- protocol technology and exact role;
- vendor/device/profile identifier where relevant;
- certificate/declaration/test-report identifier;
- issuing/test organization;
- referenced standard/specification/test-suite edition;
- test date and validity/expiry semantics where defined;
- exact qualified features/options/profiles;
- configuration assumptions;
- host OS/kernel/runtime assumptions;
- electrical/environmental assumptions;
- integration/topology assumptions;
- explicitly excluded features/modes;
- evidence source URL/document digest or immutable archive reference;
- licensing/usage prerequisites that materially affect the represented product role;
- whether the evidence is vendor self-declaration, independent conformance test, product-safety certification, interoperability test, or another evidence class.

The record should also bind the exact ABIL deployment subject that consumed the component evidence so later firmware/runtime/hardware changes cannot silently retain an obsolete qualification claim.

## Scope classes

Research shorthand for future design discussion:

### `DIRECT_COMPONENT_EVIDENCE`

The claim applies directly to the exact component/configuration tested or certified.

Examples:
- exact protocol-device conformance for the tested implementation/profile;
- exact industrial-PC safety/environmental certification for the listed product.

This does not automatically extend to ABIL's assembled controller product or machine application.

### `COMPOSITION_DEPENDENT_EVIDENCE`

The evidence remains useful only while integration assumptions are preserved.

Examples:
- protocol-card conformance that assumes a particular firmware and host API;
- runtime qualification tested on a declared OS family;
- driver timing behavior measured under a specified kernel/configuration.

A material integration change reopens the evidence subject.

### `ABIL_OWNED_EVIDENCE`

ABIL must qualify behavior it introduces or controls.

Examples:
- authority/admission logic;
- artifact activation and anti-rollback;
- deterministic scheduling configuration;
- protocol orchestration above a certified card;
- restart/recovery semantics;
- command idempotency/ambiguity handling;
- machine-model reconstruction and generated control behavior;
- cross-component failure handling.

Third-party evidence may reduce the tested surface but does not replace this evidence.

### `MACHINE_APPLICATION_EVIDENCE`

Per-installation evidence remains separate.

Examples:
- correct I/O mapping;
- machine-specific control semantics;
- commissioning envelope;
- safe-state/fallback policy;
- startup/restart behavior;
- installation-specific timing/resource limits;
- machine safety validation where separately applicable.

No component certificate should be represented as proving these facts.

## Anti-inheritance rules

The future product qualification process should reject at least these inference errors:

- a protocol certificate is treated as electrical/product-safety certification;
- an industrial-PC safety certificate is treated as proof of ABIL control correctness;
- a certified protocol card is treated as proof that arbitrary ABIL host behavior is protocol-conformant;
- a runtime's supported-OS statement is treated as deterministic timing qualification;
- a component's functional-safety capability is treated as authorization for ABIL to own a safety function;
- a certificate for one firmware/profile/role is carried across an unreviewed firmware/profile/role change;
- vendor evidence is carried across a product rebrand/integration topology whose certification terms do not actually cover that representation;
- component evidence is treated as machine-specific commissioning evidence.

## Change-control consequence

Qualification evidence must be invalidatable.

A future evidence graph should be able to answer:

- Which deployed ABIL subjects depend on this exact component evidence?
- What changed: hardware, firmware, driver, runtime, OS, configuration, protocol role, certificate/test-suite edition, or topology?
- Does the change stay within the declared evidence envelope?
- Which ABIL-owned qualification must be rerun even if third-party evidence remains valid?
- Which product or machine claims must be downgraded to `UNKNOWN` or `REQUALIFICATION_REQUIRED` until evidence is restored?

A version bump is not automatically material, but materiality must be established rather than assumed.

## Hostile research cases

Before a future product-qualification contract is considered credible, test it against cases such as:

1. certified protocol card, unqualified new firmware;
2. same card/firmware, different protocol role/profile;
3. vendor-certified runtime moved to an untested distro/kernel;
4. industrial PC certificate retained while ABIL adds external I/O/power hardware outside the certified assembly;
5. protocol conformance retained while ABIL changes host-side cyclic scheduling enough to violate timing/interoperability assumptions;
6. component safety capability present but ABIL has no authority or validation to implement a safety function;
7. certificate or test report valid, but the represented product branding/vendor-ID/licensing role is different;
8. machine application passes functionally while one component evidence subject is stale or unresolved.

The desired behavior is not always `reject product`; it is to prevent unsupported evidence inheritance and force the affected claim back to the correct qualification owner.

## Relationship to current architecture

The current PR #2 architecture already separates target qualification, deployment commissioning, authority, safety, and deterministic execution. This research does not require a current PR #2 head move.

If this seam is later promoted into normative design, it belongs in a dedicated execution-target/product-qualification evidence contract rather than being smuggled into the learner or reconstruction substrate.

## Research disposition

The practical rule is:

> Qualified third-party components can shrink ABIL's owned qualification surface, but every inherited claim must retain exact scope, provenance, assumptions, and invalidation rules.

That makes commercial runtime/protocol hardware more useful, not less: ABIL can deliberately buy down low-value conformance work without pretending the remaining system has been certified by association.

No certification claim, product selection, procurement, license acceptance, implementation planning, machine connection/write, commissioning, safety authority, deployment, merge/canonical promotion, publication/visibility change, credential/provider mutation, or other protected effect is authorized by this research.
