# ABIL Write Capability Admission V1

This is a machine-facing promotion boundary for any future ABIL implementation capable of causing physical control effects.

No implementation may energize or command a real target merely because its source, learner, evaluator, deterministic runtime, or artifact has passed review. A current admission record conforming to `WRITE_CAPABILITY_ADMISSION_V1.schema.json` must exist for the exact implementation subject and target before write capability is considered admissible.

The admission record is deny-by-default and must bind: the exact implementation commit, target identity, monotonic authority epoch, independent authority-grant digest, current safety-classification digest, commissioning-envelope digest, control-coverage digest, active-artifact digest, exactly-one-writer fence identity, explicitly authorized effects, authorizer identities, and issuance time.

`status = REVOKED` is never write authority. Expired, malformed, stale-subject, target-mismatched, epoch-regressed, artifact-mismatched, fence-mismatched, or incomplete records are not write authority. Missing admission is not write authority.

This contract does not itself grant machine connection, commissioning, deployment, or write authority. It defines evidence a future write-capable implementation must require before a protected effect can be admitted.
