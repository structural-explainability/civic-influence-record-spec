# Civic Influence Record Identifiers (CIR)

This document defines the stable requirement identifiers used by the
Civic Influence Record (CIR) specification.

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

## Overview

Defines domain profile identifiers for civic influence accountable record
systems.

CIR represents source-backed civic influence structures including persons,
organizations, roles, funding, contributions, lobbying, affiliations, policy
documents, relationships, entity resolutions, source provenance, and
interpretations.

CIR does not assert causation, endorsement, control, ideological agreement,
coordination, legitimacy, or wrongdoing by default.

## Identifier Semantics and Ordering

Identifiers are the sole normative reference mechanism.
Section ordering, formatting, and presentation are non-normative.

Identifiers are listed in strict alphabetical order to remove editorial
discretion and ensure deterministic placement.

## Identifier Naming Rules

All identifiers follow this pattern:

All identifiers begin with `CIR.` and use uppercase dot-separated semantic terms.

Identifiers are:

- semantic, not positional
- stable across versions
- reusable across prose, code, reports, and verification traces
- language-agnostic
- suitable for direct mapping to verification rule names

Identifiers MUST NOT be renamed or repurposed.
New identifiers MAY be added only in a new major version of this document.

## Identifier Notes

Each identifier MUST be followed by exactly one note.

- The note MUST be expressed as a single bullet.
- The bullet text MAY wrap across lines.
- No additional bullets, sublists, or structural markers are permitted.
- Notes are explanatory only and do not introduce additional requirements.

## Canonical Identifier List (Alphabetical, with Notes)

CIR.AFFILIATION.RECORD

- Defines affiliation records for declared associations among persons and
  organizations.

CIR.CLAIM.RECORD

- Defines claim records for assertions about civic influence structures.

CIR.COLLAPSE.PROHIBITED

- Prohibits civic influence category collapses such as association-to-endorsement
  or funding-to-control.

CIR.CONFORMANCE.AR.REQUIRED

- Requires conformance with Accountable Record.

CIR.CONFORMANCE.SE.REQUIRED

- Requires conformance with Structural Explainability.

CIR.CONTRIBUTION.RECORD

- Defines contribution records for source-backed funding flows.

CIR.DEFINITION.CORE

- Defines CIR as the civic influence domain profile of AR.

CIR.ENTITY_RESOLUTION.RECORD

- Defines entity resolution records for source-backed identity assertions across
  records.

CIR.INTERPRETATION.RECORD

- Supports civic influence interpretation records for declared interpretive
  inference types.

CIR.LOBBYING.RECORD

- Defines lobbying records for source-backed lobbying filings or disclosures.

CIR.ORGANIZATION.RECORD

- Defines organization records for organizational entities.

CIR.PERSON.RECORD

- Defines person records for individual persons.

CIR.POLICY_DOCUMENT.REFERENCE

- Defines policy document references used in civic influence records.

CIR.PROVENANCE.SOURCE

- Supports source-filing provenance records tracing source filings to derived
  civic influence records.

CIR.RELATIONSHIP.RECORD

- Defines source-backed relationship records among civic entities.

CIR.ROLE.RECORD

- Defines role records for roles held by persons within organizations or other
  entities.

CIR.SCOPE.EXCLUSIONS

- Defines what CIR explicitly does not specify.

CIR.TIME_BOUND.REFERENCE

- Defines time-bound references for relationship, role, contribution, and
  lobbying records.

CIR.VERSIONING

- Defines CIR versioning requirements.

## Cross-Artifact Consistency Rule

Each identifier in this list MUST appear:

- exactly once in SPEC.md
- exactly once in CONFORMANCE.md
- exactly once in generated requirements artifacts
- exactly once in generated conformance-check artifacts where applicable

Alphabetical order SHOULD be preserved across all artifacts.
