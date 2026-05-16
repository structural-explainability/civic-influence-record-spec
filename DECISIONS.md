# Decisions

This document records founding decisions.

## Decision 1: Define Civic Influence Record as an Accountable Record system

Decision: `civic-influence-record-spec` implements the Accountable Record contract
for source-backed civic influence structures.

Rationale: Civic influence data often spans public filings, nonprofit records,
campaign finance records, lobbying records, organization records, policy
documents, and public claims.
The system needs a durable record model that can represent those structures
without collapsing them into causation, endorsement, control,
ideological agreement, coordination, legitimacy, or wrongdoing.

Consequences:

- The repository depends on `accountable-record`.
- Civic Influence Record keeps domain vocabulary separate from SE substrate
  commitments.
- SE verification can check whether the exported records preserve required
  distinctions.

## Decision 2: Preserve source-backed records separately from interpretations

Decision: Source-backed records and interpretation records are separate record
types.

Rationale: A source may show that a filing, relationship, contribution,
lobbying disclosure, role, or affiliation exists.
It does not by itself prove causation, endorsement, control,
coordination, ideological agreement, or wrongdoing.

Consequences:

- Relationship records do not imply inference by default.
- Interpretation records must identify their interpretive inference type.
- Reports must not convert interpretations into source-backed facts.

## Decision 3: Treat entity resolution as an explicit, revisable record

Decision: Entity resolution is represented by explicit entity resolution
records, not by silent merging of source records.

Rationale: Civic influence data often contains the same person or organization
under different names, identifiers, spellings, or source systems.
Silent merge logic hides uncertainty and makes later contestation difficult.

Consequences:

- Source-backed entity references remain distinct.
- Entity resolution records identify evidence and asserting actor.
- Entity resolution does not imply ideological agreement, coordination, shared
  intent, or automatic entity truth.

## Decision 4: Keep civic influence records source-traceable

Decision: Records derived from source filings or public records should preserve
source references and provenance where available.

Rationale: Inspection, contestation, and audit depend on knowing which source
supports each record and how the record was derived.

Consequences:

- Source records remain distinct from derived records.
- Source provenance may be represented through `CIR.PROVENANCE.SOURCE`.
- Provenance does not certify correctness, completeness, authority, causation,
  endorsement, control, coordination, or enforcement.

## Decision 5: Keep the implementation verifiable

Decision: The record model and exports are designed for verification by
`se-verification-civic-influence-record-spec`.

Rationale: The purpose of the system is not only to store civic influence
records, but to make the record discipline externally checkable.

Consequences:

- Export bundles identify versions, record types, manifests, and references.
- Records use stable identifiers.
- Verification reports can trace failures to CIR, AR, and SE constraints.

## Decision 6: Do not replace source systems

Decision: Civic Influence Record does not replace FEC, LDA.gov, USAspending,
ProPublica Nonprofit Explorer, OpenCorporates, OpenSecrets, LittleSis, court
records, government records, or other source systems.

Rationale: The repository is an accountable record layer.
It references and derives from source systems;
it does not become the authoritative source system.

Consequences:

- Source records identify external systems and filings.
- Source content is not treated as true, complete, current, or authoritative by
  default.
- The project can remain lightweight and inspectable.

## Decision 7: Use working draft status

Decision: The initial version is a working draft specification.

Rationale: The contract and domain model will be stress-tested through
implementation and verification.

Consequences:

- Version `0.1.0` is appropriate for the initial release.
- Breaking changes may occur before a stable major release.
- Identifier changes should still be treated as serious and diff-visible.
