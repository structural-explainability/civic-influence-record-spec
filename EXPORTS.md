# Civic Influence Record Exports

Status: Working Draft

This document describes the export structure produced by `civic-influence-record`
for validation, inspection, and SE verification.

Civic Influence Record exports are designed to make civic influence records
portable, inspectable, and verifiable without requiring downstream systems to
reuse the internal implementation.

## Export Purpose

Exports provide machine-readable evidence of the record system's structure.

They support:

- record inspection
- source traceability
- provenance inspection
- conformance checking
- SE verification
- derived reporting
- cross-system review

Exports do not determine:

- causation
- endorsement
- control
- ideological agreement
- coordination
- wrongdoing
- legitimacy
- public influence score
- recommendation or decision outcome

## Export Directory

Generated and curated exports should live under:

```text
data/exports/
```

Specification-level generated artifacts live under:

```text
data/spec/
```

Example structure:

```text
data/
  spec/
    requirements.json
    conformance-checks.json
    scope-exclusions.json
  examples/
    example-civic-influence-records.json
  records/
    example-records.json
  exports/
    civic-influence-record-bundle.json
```

## Export Bundle

The primary export artifact is a civic influence record bundle.

Suggested filename:

```text
data/exports/civic-influence-record-bundle.json
```

Suggested top-level shape:

```json
{
  "schema": "civic-influence-record-bundle-1",
  "bundle_id": "cir-bundle:example",
  "generated_at": "2026-05-16",
  "versions": {
    "civic_influence_record": "0.1.0",
    "accountable_record": "0.1.0"
  },
  "conformance": {
    "cir": true,
    "ar": true,
    "se": true
  },
  "manifest": {
    "record_count": 0,
    "record_type_counts": {}
  },
  "records": []
}
```

## Required Bundle Fields

A civic influence record bundle must identify:

- bundle schema
- bundle identifier
- generation time where available
- CIR version
- AR version
- conformance declarations
- record manifest
- included records

## Manifest

The manifest summarizes the bundle contents.

Example:

```json
{
  "record_count": 5,
  "record_type_counts": {
    "source_record": 1,
    "organization_record": 1,
    "relationship_record": 1,
    "claim_record": 1,
    "source_provenance_record": 1
  }
}
```

The manifest is used for integrity checks. It does not define the meaning of
the records.

## Records Array

The `records` array contains the exported civic influence records.

Example:

```json
{
  "records": [
    {
      "id": "source:fec:filing:example",
      "record_type": "source_record",
      "source_system": "FEC",
      "source_identifier": "example"
    },
    {
      "id": "organization:example-org",
      "record_type": "organization_record",
      "display_name": "Example Organization",
      "source_refs": ["source:fec:filing:example"]
    }
  ]
}
```

Each record must declare its record type.

## Source References

Records that depend on source material should include stable source references.

Example:

```json
{
  "source_refs": [
    "source:fec:filing:example"
  ]
}
```

Source references identify source material. They do not assert that source
content is true, complete, current, or authoritative by default.

## Provenance References

Derived records should include provenance references where provenance is
available or required.

Example:

```json
{
  "provenance_refs": [
    "provenance:source-filing:example"
  ]
}
```

Provenance describes how a record was produced. It does not certify
correctness, completeness, authority, causation, endorsement, control,
coordination, or enforcement.

## Review Status

Records may include review status directly or through review status records.

Inline example:

```json
{
  "id": "relationship:example",
  "record_type": "relationship_record",
  "review_status": "curated"
}
```

Separate record example:

```json
{
  "id": "review-status:relationship:example",
  "record_type": "review_status_record",
  "record_ref": "relationship:example",
  "status": "curated"
}
```

Review status does not assert truth, correctness, authority, legitimacy,
causation, endorsement, control, or enforcement.

## Entity Resolution Exports

Entity resolution records must remain explicit.

Example:

```json
{
  "id": "entity-resolution:example-org:001",
  "record_type": "entity_resolution_record",
  "resolved_entity_ref": "organization:example-org",
  "source_entity_refs": [
    "source-entity:fec:example-org",
    "source-entity:propublica:example-org"
  ],
  "resolution_basis": [
    "name match",
    "address match"
  ],
  "asserting_actor": "curator:example"
}
```

Entity resolution does not merge source records. It records a revisable,
evidence-backed assertion that source-backed references refer to the same
entity.

## Interpretation Exports

Systems that record civic influence inferences should export interpretation
records separately from source-backed relationships.

Example:

```json
{
  "id": "interpretation:example-control-claim",
  "record_type": "interpretation_record",
  "interpretive_inference_type": "control claim",
  "depends_on_record_refs": [
    "relationship:example-org:example-document"
  ],
  "asserting_actor": "analyst:example"
}
```

An interpretation record does not become a source-backed relationship.

## Export Validation

An export is valid when:

- required bundle fields are present
- record identifiers are stable and unique
- record types are declared
- referenced records resolve within the bundle or to declared external sources
- manifest counts match included records
- CIR and AR versions are declared
- interpretation records do not mutate source-backed records
- provenance records do not certify source truth
- relationship records do not imply prohibited inferences

## Verification Handoff

The export bundle is the handoff artifact for:

```text
se-verification-civic-influence-record
```

The verifier checks whether the exported bundle preserves the distinctions
required by CIR, AR, and SE.

Verification may check:

- source traceability
- record type declarations
- relationship/inference separation
- entity resolution evidence
- contribution/control separation
- lobbying/outcome separation
- role/endorsement separation
- network proximity/causation separation
- source provenance chain discipline
- interpretation non-mutation
- export bundle integrity

## Generated Specification Artifacts

The repository also exports generated specification artifacts under:

```text
data/spec/
```

Expected artifacts:

```text
data/spec/requirements.json
data/spec/conformance-checks.json
data/spec/scope-exclusions.json
```

These artifacts are generated from:

```text
SPEC.md
IDENTIFIERS.md
CONFORMANCE.md
```

They support consistency checks and machine-readable inspection of the
specification itself.

## Clarifying Statement

A civic influence export makes records inspectable.

It does not certify the truth of source materials, prove influence, establish
endorsement, identify wrongdoing, or determine legitimacy. Those questions may
be represented as explicit claims or interpretations, but they remain separate
from source-backed records.
