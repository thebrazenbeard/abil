# ABIL Write Capability Admission Validation V1

Status: **DESIGN / GOVERNANCE CONTRACT / NO MACHINE-WRITE AUTHORITY**

This companion closes the distinction between structural record validity and actual write-admission validity.

## 1. Two separate predicates

`SCHEMA_VALID` means only that an admission record conforms structurally to `WRITE_CAPABILITY_ADMISSION_V1.schema.json`.

`WRITE_ADMISSION_VALID` is a separate stateful predicate. No future writer may treat `SCHEMA_VALID` as sufficient write authority.

The stateful validator consumes:

- the candidate `ABIL_WRITE_CAPABILITY_ADMISSION_V1` record;
- the exact implementation/artifact/fence subjects being activated;
- evaluation time;
- a current `AuthorityStateReadReceipt` or mechanically equivalent independently rooted current-authority read;
- the exact current authority-grant, safety-classification, commissioning-envelope, control-coverage, and active-artifact subjects referenced by the candidate.

## 2. Fail-closed validation requirements

A candidate is not `WRITE_ADMISSION_VALID` unless all required checks succeed.

At minimum reject:

- malformed or schema-invalid candidate;
- `status != AUTHORIZED`;
- `AUTHORIZED` record carrying contradictory revocation material;
- `expires_at` present and `expires_at <= issued_at`;
- `expires_at` present and evaluation time is at or after expiry;
- candidate `authority_epoch <=` the current or any superseding/revoked target authority epoch;
- target mismatch between candidate and current-authority read;
- stale, partial, conflicting, self-attested, or otherwise untrusted current-authority read;
- implementation-subject mismatch;
- authority-grant digest mismatch or non-current grant;
- safety-classification digest mismatch or non-current classification;
- commissioning-envelope digest mismatch or non-current envelope;
- control-coverage digest mismatch;
- active-artifact digest mismatch;
- writer-fence mismatch or unresolved/split ownership;
- requested effect outside `authorized_effects`;
- missing or unverified authorizer evidence.

Absence, ambiguity, stale evidence, or failed currentness proof is rejection, not provisional authority.

## 3. Authority-state read receipt

The validator must not accept a bare caller-supplied `current_epoch` or equivalent scalar.

Its comparison state must be bound by `AUTHORITY_STATE_READ_RECEIPT_V1` or a mechanically equivalent receipt that records:

- target identity;
- authority surface queried;
- qualified reader identity;
- observed generation/head/currentness subject;
- read time and freshness deadline/profile;
- completeness/conflict status;
- current authority epoch;
- digest of the relevant current/revoked/superseded epoch set;
- immutable digest of the returned authority-state subject.

If the deployment requires reconciliation across more than one authoritative surface, the receipt must represent that required set and fail closed when any required surface is missing, partial, divergent, stale, or conflicting.

## 4. Time semantics

Time-based validation is an execution-time check, not a JSON-Schema claim.

If `expires_at` is null/absent, the admission does not become timeless authority. It remains bounded by the currentness and validity of every referenced authority subject and by any independent authority-grant validity rules.

Implementations must use one declared evaluation clock/profile and record the evaluation timestamp in the validation receipt.

## 5. Validation receipt

Every stateful validation attempt should emit a machine-readable receipt containing at least:

- candidate admission digest;
- authority-state-read receipt digest;
- evaluation time/profile;
- exact implementation/artifact/fence subjects checked;
- per-check PASS/FAIL/NOT_RUN disposition;
- final `WRITE_ADMISSION_VALID` boolean;
- validator implementation/version identity.

A validation receipt is evidence, not an authority grant. The validator cannot self-issue or widen authority.

## 6. Hostile vectors

`WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.hostile-vectors.json` defines minimum negative cases for the future deterministic validator.

The vectors are acceptance obligations, not evidence that an implementation already exists or passes.

## 7. Authority ceiling

This companion does not create a machine client, writer, credential, deployment path, commissioning authority, safety authority, implementation approval, merge authority, or protected effect.

A future executable validator is a separate implementation subject and must be reviewed/tested on its own exact head before it can participate in any write-capability admission path.
