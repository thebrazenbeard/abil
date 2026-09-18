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
- the independently resolved current freshness profile expected for that target/deployment;
- the independently resolved canonicalization profile for digest-bound authority-state payloads;
- the independently resolved deployment authority-surface profile and required authority-surface set;
- the exact current authority-grant, safety-classification, commissioning-envelope, control-coverage, and active-artifact subjects referenced by the candidate.

## 2. Fail-closed validation requirements

A candidate is not `WRITE_ADMISSION_VALID` unless all required checks succeed.

At minimum reject:

- malformed or schema-invalid candidate;
- `status != AUTHORIZED`;
- `AUTHORIZED` record carrying contradictory revocation material;
- `expires_at` present and `expires_at <= issued_at`;
- `expires_at` present and evaluation time is at or after expiry;
- candidate `authority_epoch <= max_observed_authority_epoch`, where that maximum is recomputed from the verified canonical current/revoked/superseded epoch set;
- target mismatch between candidate and current-authority read;
- stale, partial, conflicting, self-attested, or otherwise untrusted current-authority read;
- freshness profile identity/digest mismatch, a carried deadline that does not equal the deadline independently derived from the bound freshness profile, or evaluation time at/after the derived deadline;
- canonicalization profile identity/digest mismatch;
- required authority-surface profile identity/digest mismatch;
- any deployment-required authority surface missing from the reconciled read set;
- any unexpected or duplicate surface identity that makes the reconciled set ambiguous;
- required/reconciled surface-set digest mismatch or mismatch between the declared reconciled set and the per-surface read identities;
- epoch-set digest mismatch, duplicate/conflicting epoch state, declared maximum mismatch, or current-epoch inconsistency with the materialized epoch set;
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

The validator must not accept a bare caller-supplied `current_epoch`, a self-declared `FRESH`/`COMPLETE` label, or a single-surface read as proof of the complete comparison state.

Its comparison state must be bound by `AUTHORITY_STATE_READ_RECEIPT_V1` or a mechanically equivalent receipt that records:

- target identity;
- qualified reader identity;
- reconciliation subject;
- aggregate read time;
- a non-null freshness deadline;
- independently resolved freshness-profile identity and digest;
- independently resolved canonicalization-profile identity and digest;
- completeness/conflict status;
- independently resolved deployment authority-surface-profile identity and digest;
- the canonical required authority-surface identities and canonical required-set digest;
- one bound read for every reconciled authority surface, including surface ID, observed subject, read time, freshness deadline, and authority-state digest;
- the canonical reconciled authority-surface identities and reconciled-set digest;
- current authority epoch;
- the materialized canonical current/revoked/superseded epoch set;
- a recomputable maximum observed authority epoch over that set;
- digest of the canonical epoch-set payload;
- immutable digest of the reconciled authority-state subject.

`freshness_status` and `completeness_status` are summary fields only. They are never accepted as proof by themselves.

### 3.1 Freshness computation

The validator must resolve the expected freshness profile independently of the receipt, verify the receipt's `freshness_profile_id` and `freshness_profile_digest` against that profile, and then evaluate time.

For a receipt to be usable, the validator must derive freshness from the independently resolved profile rather than trust a carried deadline:

1. for each required surface read, derive the permitted `fresh_until` from that surface's `read_at`, surface identity, target/deployment context, and the bound freshness profile;
2. require each carried per-surface `fresh_until` to equal the independently derived deadline;
3. derive the aggregate `fresh_until` as the earliest derived required-surface deadline;
4. require the carried aggregate `fresh_until` to equal that derived aggregate deadline;
5. require evaluation time to be strictly before the aggregate and every required-surface derived deadline;
6. require `freshness_status` to be `FRESH` and consistent with the computed result.

A label of `FRESH` with a missing, expired, non-derivable, profile-mismatched, or independently inconsistent deadline is rejection. A caller cannot extend authority freshness by choosing a later deadline than the bound profile yields.

### 3.2 Epoch computation

The receipt must carry the materialized canonical epoch set used for comparison, with each entry typed `CURRENT`, `REVOKED`, or `SUPERSEDED`.

The validator must:

1. resolve the expected canonicalization profile independently of the receipt and verify the receipt's profile identity/digest;
2. canonicalize the epoch-set payload under that verified profile;
3. verify its digest against `epoch_set_digest`;
4. reject duplicate epoch numbers with conflicting state and reject more than one `CURRENT` epoch;
5. recompute `max_observed_authority_epoch` from all entries, including revoked and superseded entries;
6. verify the declared maximum equals the recomputed maximum;
7. verify `current_authority_epoch` equals the single `CURRENT` epoch and reject missing/ambiguous current state;
8. require the candidate `authority_epoch` to be strictly greater than the recomputed maximum.

An opaque digest without the materialized set is insufficient input for this predicate.

### 3.3 Multi-surface completeness

The validator must resolve the expected deployment authority-surface profile independently of the receipt and verify the receipt's profile identity/digest against it.

It must then:

1. resolve and verify the canonicalization profile independently of the receipt;
2. canonicalize and verify `required_authority_surface_ids` against `required_surface_set_digest`;
3. verify the required set exactly matches the independently resolved deployment profile;
4. derive the observed surface IDs from `authority_surface_reads` and reject duplicate surface IDs;
5. verify those IDs exactly match `reconciled_authority_surface_ids`;
6. canonicalize and verify the reconciled set against `reconciled_surface_set_digest`;
7. require the reconciled set to equal the required set exactly;
8. require each required surface read to be individually fresh and internally bound.

A `COMPLETE` label from one surface or from an incomplete reconciled set is rejection.

## 4. Time semantics

Time-based validation is an execution-time check, not a JSON-Schema claim.

If `expires_at` is null/absent, the admission does not become timeless authority. It remains bounded by the currentness and validity of every referenced authority subject and by any independent authority-grant validity rules.

Implementations must use one declared evaluation clock/profile and record the evaluation timestamp in the validation receipt.

## 5. Canonicalization requirement

Canonicalization is itself independently bound current input, not an implementation-local convention.

The future executable validator must resolve the expected canonicalization profile independently of the receipt, verify `canonicalization_profile_id` and `canonicalization_profile_digest`, and apply that exact profile to:

- the epoch-set payload;
- required authority-surface IDs;
- reconciled authority-surface IDs.

The profile must deterministically specify ordering, field encoding, string/number representation, and digest input bytes needed to make those hashes reproducible. A digest computed under an unbound, mismatched, or unknown canonicalization profile is rejection.

Until that profile and its resolver are implemented and qualified, these fields remain design-contract requirements rather than executable proof.

## 6. Validation receipt

Every stateful validation attempt should emit a machine-readable receipt containing at least:

- candidate admission digest;
- authority-state-read receipt digest;
- evaluation time/profile;
- exact freshness-profile identity/digest checked and independently derived per-surface/aggregate deadlines;
- exact canonicalization-profile identity/digest checked;
- exact deployment authority-surface-profile identity/digest checked;
- recomputed epoch-set digest and maximum;
- required/reconciled surface-set digests;
- exact implementation/artifact/fence subjects checked;
- per-check PASS/FAIL/NOT_RUN disposition;
- final `WRITE_ADMISSION_VALID` boolean;
- validator implementation/version identity.

A validation receipt is evidence, not an authority grant. The validator cannot self-issue or widen authority.

## 7. Hostile vectors

`WRITE_CAPABILITY_ADMISSION_VALIDATION_V1.hostile-vectors.json` defines minimum negative cases for the future deterministic validator.

The vectors are acceptance obligations, not evidence that an implementation already exists or passes.

## 8. Authority ceiling

This companion does not create a machine client, writer, credential, deployment path, commissioning authority, safety authority, implementation approval, merge authority, or protected effect.

A future executable validator is a separate implementation subject and must be reviewed/tested on its own exact head before it can participate in any write-capability admission path.
