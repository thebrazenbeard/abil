# Controller Compliance and Protocol-Conformance Addendum

Status: **NON-NORMATIVE RESEARCH / PRIVATE ABIL SOURCE / NOT LEGAL OR CERTIFICATION ADVICE / NO PRODUCT-SELECTION AUTHORITY**

Date: 2026-09-13

Parent research PR: Draft PR #4

Architecture base examined: `work/abil-control-reconstruction-architecture-20260908@712d5b30b45ba9299dcfce0599878cb81db70e8f`

## Purpose

The deterministic-runtime feasibility spike showed that ABIL can plausibly integrate commercial soft-PLC and protocol hardware rather than invent every controller/runtime/fieldbus layer itself.

This addendum asks why that matters beyond engineering effort:

> What controller-equipment, protocol-conformance, and functional-safety qualification surfaces appear relevant if ABIL eventually ships an industrial controller-class appliance, and which burdens can be reduced by integrating already-qualified components rather than owning every layer?

This is engineering research only. Exact market, jurisdiction, installation, NRTL/CE/UKCA, customer, machine-builder, and functional-safety obligations require qualified product-compliance/safety review for the actual product and deployment.

## Executive finding

`Industrial PC running control software` is not a shortcut around controller-product qualification.

If ABIL's primary product purpose becomes command/control of machines and industrial processes, current standards and protocol-organization requirements create several distinct evidence surfaces:

1. **controller functionality / EMC** — IEC 61131-2;
2. **electrical/control-equipment safety** — IEC 61010-2-201 together with IEC 61010-1, and corresponding national certification paths such as UL 61010-2-201 in the US;
3. **protocol licensing/conformance/interoperability** — technology-owner rules such as ODVA for EtherNet/IP/DeviceNet, PI for PROFINET, and ETG for EtherCAT device implementations;
4. **functional-safety engineering** — separate standards such as ISO 13849-1 when a control system actually performs safety functions.

These are not interchangeable. Passing protocol conformance does not qualify electrical safety; ordinary controller certification does not qualify a safety function; a certified industrial PC does not automatically qualify ABIL's whole assembled controller product or its machine application.

This strengthens the prior recommendation: **buy/integrate first, own selectively later**. Qualified commercial runtime/hardware can reduce the amount of low-differentiation implementation and conformance surface ABIL owns directly, but cannot erase ABIL's own system/product/deployment responsibilities.

## 1. IEC 61131-2 controller equipment requirements

The current published IEC 61131-2 edition is IEC 61131-2:2017, `Industrial-process measurement and control - Programmable controllers - Part 2: Equipment requirements and tests`.

IEC states that it specifies functional and electromagnetic-compatibility requirements and related verification tests for products whose primary purpose is industrial control, including PLC/PAC equipment and associated peripherals used to command/control machines, automated manufacturing, and industrial processes.

The 2017 edition explicitly moved safety requirements out of IEC 61131-2 and points to IEC 61010-2-201 instead.

Engineering consequence for ABIL:

- controller functionality/EMC is a separate qualification subject from the software's logical correctness;
- the exact appliance hardware, I/O interfaces, environmental ratings, EMC behavior, and controller function matter;
- adopting a pre-qualified industrial controller/soft-PLC platform can provide useful component evidence, but ABIL must not assume that component evidence automatically covers the final assembled system or target machine.

Source:
- https://webstore.iec.ch/en/publication/31007

## 2. IEC 61010-2-201 / UL controller-equipment safety

The current IEC edition is **IEC 61010-2-201:2024**, `Safety requirements for electrical equipment for measurement, control, and laboratory use - Part 2-201: Particular requirements for control equipment`.

IEC 61010-2-201:2024 supplements/modifies IEC 61010-1 for control equipment. The prior 2017 edition has been withdrawn and replaced by the 2024 edition.

The 2026 IECEE Test Report Form `61010-2-201E` explicitly applies to IEC 61010-2-201:2024, confirming the current testing subject.

UL's published controller transition material identifies UL 61010-1 + UL 61010-2-201 as the US safety-certification path for programmable controllers, replacing the former UL 508/UL 61131-2 PLC certification path for the affected category. UL also describes IEC/UL 61010-2-201 as covering programmable controllers and other industrial control equipment.

Engineering consequence for ABIL:

- a custom ABIL controller appliance is not merely a software packaging exercise;
- enclosure, power, isolation, terminals, temperatures, markings, and other control-equipment safety attributes can become product evidence/certification subjects;
- selecting an industrial PC/controller platform already designed/certified for industrial control can materially reduce hardware redesign risk, but exact system-level certification scope still requires qualified review.

Sources:
- https://webstore.iec.ch/en/publication/64909
- https://webstore.iec.ch/en/publication/113667
- https://www.ul.com/resources/industrial-control-equipment-transition-iec-standards
- https://www.ul.com/sites/g/files/qbfpbp251/files/2019-05/UL-61010-2-201-FAQs-revised-Dec-16th-2014.pdf

## 3. EtherNet/IP and DeviceNet — ODVA licensing and conformance

ODVA's current developer guidance says companies developing products using EtherNet/IP or other ODVA technologies must become licensed vendors under the ODVA Terms of Usage, obtain the applicable Vendor ID, and maintain the relevant specification subscription.

ODVA's current conformance-testing guidance states that each product incorporating an ODVA technology must be submitted for vendor-independent conformance testing, with successful testing resulting in an ODVA Declaration of Conformity.

The same ODVA infrastructure currently provides conformance-test suites for both EtherNet/IP and DeviceNet.

Engineering consequence for ABIL:

- writing or embedding an EtherNet/IP/DeviceNet product stack is not simply an open-protocol coding task;
- licensing, Vendor ID, specification access, conformance tooling, test-service planning, and product declarations belong in the product lifecycle from the beginning;
- using a commercial protocol card/runtime whose vendor owns the protocol implementation and conformance subject can be substantially simpler than making ABIL itself the protocol-device implementation, depending on the exact host/card integration and product representation;
- the boundary must be checked contractually and technically; a certified card does not magically certify arbitrary host behavior built on top of it.

Sources:
- https://www.odva.org/technology-standards/key-technologies/ethernet-ip/
- https://www.odva.org/technology-standards/conformance-testing/
- https://www.odva.org/subscriptions-services/test-services/
- https://www.odva.org/subscriptions-services/software/

## 4. PROFINET — PI certification

PROFIBUS & PROFINET International currently describes certification testing as mandatory for PROFINET products, and its `How to Get a Certificate for a PROFINET Node` guidance says the certifying test is an essential part of PI quality assurance. The current guidance also states certification is mandatory for implemented PROFINET-based PI profiles.

Engineering consequence for ABIL:

- if ABIL becomes the PROFINET controller/device implementation presented as a product, certification planning belongs in architecture/product planning rather than as an afterthought;
- a commercial runtime plus qualified communication hardware is therefore attractive for an early product path if it keeps ABIL above the protocol implementation/conformance layer;
- exact certification inheritance/composition must still be confirmed for the actual product topology and branding.

Sources:
- https://www.profibus.com/aboutus/institutions-support/test-labs
- https://www.profibus.com/download/how-to-get-a-certificate-for-a-profinet-device

## 5. EtherCAT — mandatory in-house conformance for device vendors, optional official certificate

The EtherCAT Technology Group distinguishes mandatory implementation conformance from optional official certification.

Current ETG guidance says:

- EtherCAT device manufacturers must use a valid EtherCAT Vendor ID;
- a valid subscription to the official Conformance Test Tool is mandatory for device vendors;
- device manufacturers must successfully apply the current CTT before market release;
- official testing at an EtherCAT Test Center is additionally required to obtain the formal EtherCAT Conformance Tested certificate/logo, but that official certificate is encouraged rather than universally mandatory.

ETG's current conformance-test records were updated in June 2026.

Engineering consequence for ABIL:

- `open EtherCAT master exists` does not mean commercial product conformance is free;
- the product role matters: MainDevice, SubDevice, configuration tooling, or OEM user can have different obligations;
- ABIL should decide whether it needs to own a protocol-device identity at all or can integrate a qualified component/runtime;
- protocol role, vendor identity, test-tool access, and interoperability testing belong in the execution-target qualification profile.

Sources:
- https://www.ethercat.org/en/conformance.html
- https://www.ethercat.org/en/ctt.htm
- https://www.ethercat.org/en/conformance_for_vendors.htm
- https://www.ethercat.org/en/technology.html
- https://www.ethercat.org/en/downloads/downloads_607A069210B14903BC77B711A53A7D9F.htm

## 6. Functional safety remains a separate project

ISO 13849-1:2023 specifies methodology and requirements for design/integration of safety-related parts of control systems that perform safety functions, including software.

That reinforces the existing ABIL architecture boundary:

- ordinary control replacement is not automatic safety-function replacement;
- an ABIL controller can preserve and interact with independent safety systems without claiming to implement their safety function;
- if a future ABIL product intentionally performs a safety function, that is a new safety-engineering/certification scope and cannot be inferred from ordinary controller qualification, protocol conformance, or successful machine operation.

Source:
- https://www.iso.org/standard/73481.html

This addendum does not attempt to map the full functional-safety standards tree (for example IEC 61508/IEC 62061, drive safety, robot standards, or application-specific machinery standards). That mapping should occur only when an exact future safety scope exists.

## 7. Architectural implication: preserve certification boundaries

The deterministic-execution abstraction should expose not only runtime behavior but **qualification provenance**.

A future `DeterministicExecutionTarget` or deployment binding should be able to record at least:

- execution-runtime/product identity and version;
- controller-equipment hardware identity;
- protocol role (e.g. EtherNet/IP scanner/adapter, PROFINET controller/device, EtherCAT MainDevice/SubDevice);
- protocol stack/card/runtime vendor;
- relevant Vendor ID / licensed-technology identity where applicable;
- component conformance/certification identity and scope;
- controller-equipment certification/test evidence and scope where applicable;
- host OS/kernel/runtime configuration;
- driver/firmware identity;
- exact boundary between vendor-qualified component behavior and ABIL-owned behavior;
- integration assumptions that would invalidate inherited component evidence;
- target machine/deployment qualification evidence separately from component certification.

That lets ABIL use qualified components without falsely claiming their certificates apply to behavior outside the tested scope.

## 8. Hardware-form-factor consequence

This research adds a constraint to eventual appliance selection:

> Do not optimize the first ABIL appliance purely for minimum size/cost if doing so removes supported industrial expansion, certified power/environment options, or access to qualified protocol hardware.

An industrial PC with PCIe/M.2/mini-PCIe or another supported industrial communications path may cost more than a tiny fanless consumer mini-PC but reduce protocol/conformance and field-support risk dramatically.

This is not yet a purchasing decision. It is a reason to keep the hardware interface envelope open until the first target protocol/machine is chosen.

## 9. Buy/integrate-first does not mean certification-by-association

The strongest caution from this research is the opposite of `buy a certified box and we're done`.

Integration can reduce the amount of technology ABIL must design and independently qualify, but the final responsibility boundary depends on:

- whether ABIL is sold as software, appliance, controller, system, or component;
- which entity is the protocol vendor/manufacturer of record;
- whether host behavior changes the certified protocol implementation;
- power/enclosure/I/O/EMC integration;
- exact machine application and installation;
- branding/private labeling/OEM arrangements;
- jurisdiction/customer requirements;
- whether ABIL performs ordinary control or a safety function.

The product architecture should therefore optimize for **clean evidence boundaries**, not imagined certificate inheritance.

## 10. Recommended future qualification strategy

When implementation/product authority eventually exists:

1. keep non-actuating R2 independent of controller/product certification work;
2. choose one first industrial execution target whose hardware/runtime/protocol qualification boundary is commercially supportable;
3. obtain the exact vendor licensing/certification/OEM terms before product coupling;
4. qualify ABIL-owned behavior above that target: artifact verification, authority/fencing, deterministic task behavior, restart/resync, command ambiguity, diagnostics, and degraded operation;
5. preserve exact component qualification identities in deployment evidence;
6. only internalize a protocol/runtime layer when the product value justifies assuming its conformance, lifecycle, and support burden;
7. treat any future safety-function implementation as a separate engineering program.

## Research disposition

The compliance/conformance evidence strengthens the previous PR #4 conclusion.

A broad commercial runtime/protocol-hardware path is not merely a shortcut for coding. It can also preserve valuable third-party conformance and industrial-product evidence boundaries while ABIL concentrates engineering effort on reconstruction, authority, coverage, validation, and support lifecycle.

The qualification burden is reduced, not erased.

No architecture change to PR #2 or R2 change to PR #3 is required by this research. No procurement, license acceptance, certification claim, implementation, machine access/write, commissioning, deployment, merge, or canonical promotion is authorized.