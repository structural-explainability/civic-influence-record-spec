# Civic Influence Record Model

Status: Working Draft

This document defines the working record model for `civic-influence-record-spec`.

Civic Influence Record (CIR) is an Accountable Record domain profile for
source-backed civic influence structures.
It records people, organizations, roles, relationships, funding, lobbying,
affiliations, policy documents, entity resolutions, claims, interpretations,
provenance, and reports without asserting causation, endorsement, control,
ideological agreement, coordination, legitimacy, or wrongdoing by default.

## Model Purpose

The purpose of this record model is to make civic influence structures
inspectable without collapsing source-backed records into stronger
interpretive claims.

The model supports:

- stable identity-bearing records
- source-backed relationship records
- explicit entity resolution records
- source-filing provenance
- declared interpretive inference types
- derived reports that do not replace underlying records
- export bundles suitable for SE verification

The model does not define:

- causation
- endorsement
- control
- ideological agreement
- wrongdoing
- public influence scoring
- recommendation or decision logic
- source data hosting
- automatic entity truth

## Record Model Overview

Civic Influence Record uses the following primary record families:

- source records
- person records
- organization records
- role records
- affiliation records
- relationship records
- contribution records
- lobbying records
- policy document references
- entity resolution records
- claim records
- interpretation records
- provenance records
- review status records
- report records

Each record must have a stable identifier, a declared record type, and enough
source or provenance information to support inspection and verification.

## Common Record Fields

All civic influence records should use this common structure where applicable:

```json
{
  "id": "cir:record:example",
  "record_type": "example_record",
  "schema_version": "0.1.0",
  "created_at": "2026-05-16",
  "updated_at": "2026-05-16",
  "source_refs": [],
  "provenance_refs": [],
  "review_status": "draft",
  "notes": []
}
```

Common fields:

- `id`: stable record identifier
- `record_type`: declared record type
- `schema_version`: CIR record model version
- `created_at`: record creation date where available
- `updated_at`: last update date where available
- `source_refs`: source records or source spans supporting the record
- `provenance_refs`: provenance records describing derivation
- `review_status`: review status value
- `notes`: non-normative implementation notes

Common fields do not imply that all records have the same meaning.
The declared `record_type` controls the role of the record.

## Source Record

A source record identifies an external source, filing, document, database
entry, or public record used by the system.

```json
{
  "id": "source:fec:filing:example",
  "record_type": "source_record",
  "source_system": "FEC",
  "source_identifier": "example",
  "source_url": "https://example.invalid/source",
  "retrieved_at": "2026-05-16",
  "description": "Example source filing."
}
```

A source record:

- identifies source material
- remains distinct from interpretations of that source
- does not assert that source content is true, complete, current, or
  authoritative by default

## Person Record

A person record represents an individual person as an identity-bearing civic
influence entity.

```json
{
  "id": "person:example-person",
  "record_type": "person_record",
  "display_name": "Example Person",
  "source_refs": ["source:fec:filing:example"],
  "identity_basis": "source-backed-reference",
  "review_status": "draft"
}
```

A person record:

- conforms to `CIR.PERSON.RECORD`
- uses a stable identifier
- remains distinct from organization and role records
- does not assert ideological alignment, intent, coordination, or wrongdoing

## Organization Record

An organization record represents an organizational entity.

```json
{
  "id": "organization:example-org",
  "record_type": "organization_record",
  "display_name": "Example Organization",
  "organization_type": "nonprofit",
  "source_refs": ["source:propublica:990:example"],
  "identity_basis": "source-backed-reference",
  "review_status": "draft"
}
```

An organization record:

- conforms to `CIR.ORGANIZATION.RECORD`
- uses a stable identifier
- remains distinct from person and role records
- does not assert ideology, intent, control, or coordination as substrate facts

## Role Record

A role record represents a role held by a person within an organization or
other entity.

```json
{
  "id": "role:example-person:example-org:director",
  "record_type": "role_record",
  "person_ref": "person:example-person",
  "role_holding_entity_ref": "organization:example-org",
  "role_type": "director",
  "time_bounds": {
    "start": "2024-01-01",
    "end": null,
    "bound_status": "open-ended"
  },
  "source_refs": ["source:propublica:990:example"]
}
```

A role record:

- identifies the person, role-holding entity, and role type
- records time bounds where available
- does not imply endorsement, control, or shared intent beyond the declared role

## Affiliation Record

An affiliation record represents a declared association between persons and
organizations or between organizations.

```json
{
  "id": "affiliation:example-org:example-coalition",
  "record_type": "affiliation_record",
  "entity_refs": ["organization:example-org", "organization:example-coalition"],
  "affiliation_type": "member",
  "source_refs": ["source:public-document:example"]
}
```

An affiliation record:

- conforms to `CIR.AFFILIATION.RECORD`
- identifies affiliated entities
- does not imply endorsement, ideological agreement, coordination, control,
  or shared intent

## Relationship Record

A relationship record represents a source-backed association between civic
entities.

```json
{
  "id": "relationship:example-org:example-document",
  "record_type": "relationship_record",
  "subject_ref": "organization:example-org",
  "object_ref": "policy-document:example-document",
  "relationship_type": "listed_as_sponsor",
  "time_bounds": {
    "start": null,
    "end": null,
    "bound_status": "unknown"
  },
  "source_refs": ["source:public-document:example"]
}
```

A relationship record:

- identifies related entities
- declares relationship type
- references source backing
- remains distinct from inference, claim, and interpretation records
- does not imply causation, endorsement, control, ideological agreement,
  or coordination by default

## Contribution Record

A contribution record represents a funding flow from one entity to another as
recorded in a source filing.

```json
{
  "id": "contribution:example-contributor:example-recipient:001",
  "record_type": "contribution_record",
  "contributor_ref": "person:example-person",
  "recipient_ref": "organization:example-committee",
  "amount": "100.00",
  "currency": "USD",
  "recorded_date": "2025-10-01",
  "source_refs": ["source:fec:filing:example"]
}
```

A contribution record:

- records that a contribution was recorded in a source
- does not imply influence, endorsement, control, authorship,
  coordination, or expected outcome

## Lobbying Record

A lobbying record represents a filing or disclosure of lobbying activity.

```json
{
  "id": "lobbying:example-client:2025-q1",
  "record_type": "lobbying_record",
  "registrant_ref": "organization:example-registrant",
  "client_ref": "organization:example-client",
  "subject_matter": "example issue area",
  "time_bounds": {
    "start": "2025-01-01",
    "end": "2025-03-31",
    "bound_status": "closed"
  },
  "source_refs": ["source:lda:report:example"]
}
```

A lobbying record:

- records a source-backed lobbying disclosure
- does not imply policy outcome, success, or causal influence

## Policy Document Reference

A policy document reference identifies a policy document referenced in civic
influence records.

```json
{
  "id": "policy-document:example-document",
  "record_type": "policy_document_reference",
  "title": "Example Policy Document",
  "document_date": "2025-01-01",
  "source_refs": ["source:public-document:example"]
}
```

A policy document reference:

- identifies a document
- remains distinct from interpretations of that document
- is not modified to reflect interpretation

## Entity Resolution Record

An entity resolution record asserts that two or more source-backed entity
references refer to the same entity.

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
    "address match",
    "source identifier match"
  ],
  "asserting_actor": "curator:example",
  "review_status": "curated"
}
```

An entity resolution record:

- identifies source-backed references being resolved
- identifies evidence supporting the resolution
- identifies the asserting actor
- does not merge or modify source-backed records
- does not imply ideological agreement, coordination, shared intent,
  or automatic entity truth

## Claim Record

A claim record represents an assertion about civic influence structures.

```json
{
  "id": "claim:example-influence-claim",
  "record_type": "claim_record",
  "claim_type": "source-backed-association-claim",
  "claim_text": "Example Organization is listed as a sponsor of Example Document.",
  "about_record_refs": ["relationship:example-org:example-document"],
  "asserting_actor": "curator:example",
  "source_refs": ["source:public-document:example"]
}
```

A claim record:

- conforms to `AR.CLAIM.RECORD`
- references the records the claim is about
- identifies the asserting actor
- remains distinct from relationship and interpretation records

## Interpretation Record

An interpretation record attaches interpretive content to civic influence
records.

```json
{
  "id": "interpretation:example-control-claim",
  "record_type": "interpretation_record",
  "interpretive_inference_type": "control claim",
  "depends_on_record_refs": [
    "relationship:example-org:example-document",
    "contribution:example-contributor:example-recipient:001"
  ],
  "interpretation_text": "The referenced records may support a contestable control interpretation.",
  "asserting_actor": "analyst:example",
  "review_status": "draft"
}
```

An interpretation record:

- conforms to `AR.INTERPRETATION.RECORD`
- may specialize through `CIR.INTERPRETATION.RECORD`
- identifies the interpretive inference type
- identifies grounding records
- remains distinct from source-backed relationships and claims
- does not modify source-backed records
- does not assert correctness, authority, legitimacy, obligation, or enforcement

## Source Provenance Record

A source provenance record traces a source filing to one or more derived civic
influence records.

```json
{
  "id": "provenance:source-filing:example",
  "record_type": "source_provenance_record",
  "originating_source_ref": "source:fec:filing:example",
  "derived_record_refs": [
    "contribution:example-contributor:example-recipient:001"
  ],
  "derivation_method": "manual extraction",
  "asserting_actor": "curator:example",
  "review_status": "draft"
}
```

A source provenance record:

- conforms to `AR.PROVENANCE`
- may specialize through `CIR.PROVENANCE.SOURCE`
- identifies the originating source filing
- identifies derived records
- does not certify correctness, completeness, authority, causation,
  endorsement, control, coordination, or enforcement

## Review Status Record

A review status record identifies review state for a civic influence record.

```json
{
  "id": "review-status:relationship:example-org:example-document",
  "record_type": "review_status_record",
  "record_ref": "relationship:example-org:example-document",
  "status": "curated",
  "assigned_by": "curator:example",
  "assigned_at": "2026-05-16"
}
```

Review status values may include:

- `draft`
- `machine-suggested`
- `curated`
- `reviewed`
- `disputed`
- `deprecated`
- `superseded`

A review status record:

- does not assert truth, correctness, authority, legitimacy, obligation,
  causation, endorsement, control, or enforcement
- remains distinct from governance, interpretation, and provenance records

## Report Record

A report record represents a derived human-readable or machine-readable view.

```json
{
  "id": "report:example-civic-influence",
  "record_type": "report_record",
  "report_type": "civic-influence-summary",
  "derived_from_record_refs": [
    "organization:example-org",
    "relationship:example-org:example-document",
    "claim:example-influence-claim"
  ],
  "generated_at": "2026-05-16"
}
```

A report record:

- is a derived view
- does not replace the records it summarizes
- does not assert causation, endorsement, control, ideological agreement,
  coordination, legitimacy, wrongdoing, or proof

## Prohibited Collapses

The record model must preserve these distinctions:

- association is not endorsement
- employment is not corporate action
- funding is not authorship
- grant is not control
- lobbying is not policy outcome
- shared personnel is not unified intent
- network proximity is not causation
- entity resolution is not ideological agreement
- relationship is not inference
- source-backed record is not interpretation
- source provenance is not source truth
- source provenance is not endorsement
- interpretation is not source-backed relationship

## Verification Readiness

A civic influence record system should be able to export a bundle containing:

- manifest metadata
- record type counts
- source records
- identity-bearing records
- relationship records
- claim records
- interpretation records where used
- provenance records where used
- review status records where used
- version declarations for CIR and AR

The exported bundle should be suitable for checking by
`se-verification-civic-influence-record-spec`.

## Clarifying Statement

Civic Influence Record records source-backed civic structures, not civic
judgment.

It may show that a filing, relationship, role, contribution, lobbying record,
or entity resolution exists. It does not assert that the relationship caused
an outcome, proves control, establishes endorsement, demonstrates ideological
agreement, or resolves disagreement about influence.
