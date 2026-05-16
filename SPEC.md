# Civic Influence Record Specification

Status: Working Draft Specification

This document defines the working requirements for Civic Influence Record (CIR)
systems.

CIR is a domain profile of Accountable Record (AR) for source-backed civic
influence structures. CIR records persons, organizations, roles, funding,
contributions, lobbying, affiliations, policy documents, relationships, entity
resolutions, source provenance, claims, and interpretations without asserting
causation, endorsement, control, ideological agreement, coordination,
legitimacy, or wrongdoing by default.

## How to Read This Spec

Keywords MUST, MUST NOT, SHOULD, and MAY are to be interpreted as described in
RFC 2119.

Identifiers are the sole normative reference for conformance.
Section ordering, formatting, and presentation are non-normative.

---

## CIR.AFFILIATION.RECORD

CIR MUST provide a structural form for affiliation records.

Affiliation records:

- MUST identify the affiliated entities
- MUST identify the affiliation type as a declared type
- MUST conform to CIR.RELATIONSHIP.RECORD
- MUST NOT imply endorsement
- MUST NOT imply ideological agreement
- MUST NOT imply coordination, control, or shared intent

An affiliation record represents a declared association. It does not convert
association into endorsement, ideological agreement, coordination, control, or
shared intent.

## CIR.CLAIM.RECORD

CIR MUST provide a structural form for claim records.

Claim records:

- MUST conform to AR.CLAIM.RECORD
- MUST reference the records the claim is about
- MUST identify the asserting actor
- MUST be distinguishable from relationship records
- MUST NOT assert causation, endorsement, control, or coordination unless those
  are declared claim types with explicit source support

A claim record represents an assertion about civic influence structures. It does
not become a source-backed relationship by default.

## CIR.COLLAPSE.PROHIBITED

CIR MUST prohibit category collapses that would turn source-backed civic records
into stronger claims without explicit declaration.

CIR MUST preserve these distinctions:

- association and endorsement
- employment and corporate action
- funding and authorship
- grant and control
- lobbying and policy outcome
- shared personnel and unified intent
- network proximity and causation
- entity resolution and ideological agreement
- relationship and inference
- source-backed record and interpretation
- source provenance and source truth
- source provenance and endorsement
- interpretation and source-backed relationship

A CIR system is non-conformant if it collapses any prohibited civic influence
category as a substrate fact.

## CIR.CONFORMANCE.AR.REQUIRED

Any system claiming conformance with CIR MUST also conform to the Accountable
Record specification.

CIR MUST NOT weaken, override, or reinterpret AR constraints.

## CIR.CONFORMANCE.SE.REQUIRED

Any system claiming conformance with CIR MUST also conform to Structural
Explainability.

CIR MUST NOT weaken, override, or reinterpret SE neutrality constraints.

## CIR.CONTRIBUTION.RECORD

CIR MUST provide a structural form for contribution records.

Contribution records:

- MUST identify contributor and recipient entities
- MUST identify amount and time where available
- MUST reference the source filing
- MUST be distinguishable from claim records and interpretation records
- MUST NOT imply influence, endorsement, control, authorship, coordination, or
  expected outcome

A contribution record records that a contribution was represented in a source.
It does not establish what the contribution caused or meant.

## CIR.DEFINITION.CORE

Civic Influence Record defines a domain profile of Accountable Record for
source-backed civic influence structures.

CIR specifies structural forms for:

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
- source provenance records
- time-bound references

CIR does not define causation, endorsement, control, ideological agreement,
coordination, wrongdoing, influence scoring, recommendation, decision logic, or
source data hosting.

## CIR.ENTITY_RESOLUTION.RECORD

CIR MUST provide a structural form for entity resolution records.

Entity resolution records:

- MUST identify the source-backed references being resolved
- MUST identify evidence supporting the resolution
- MUST identify the asserting actor
- MUST be distinguishable from source-backed references
- MUST NOT modify source-backed references
- MUST NOT imply ideological agreement, coordination, or shared intent
- MUST be revisable as new evidence becomes available

Entity resolution records make identity assertions inspectable. They do not
silently merge source records or establish automatic entity truth.

## CIR.INTERPRETATION.RECORD

CIR MAY provide a structural form for interpretation records that attach
interpretive content to civic influence records.

Interpretation records:

- MUST conform to AR.INTERPRETATION.RECORD
- MUST identify the interpretive inference type as a declared type
  (such as causal claim, endorsement claim, control claim, coordination claim,
  or ideological claim)
- MUST identify the records on which the interpretation depends
- MUST identify the asserting actor or framework
- MUST be distinguishable from relationship records and claim records
- MUST NOT modify source-backed records
- MUST NOT convert an interpretation into a source-backed relationship
- MUST NOT assert correctness, authority, legitimacy, obligation, or enforcement

An interpretation in the civic influence domain often takes the form of an
inference from source-backed relationships to causal, endorsement, control,
coordination, or ideological claims. The inference type MUST be declared so that
the inference and its grounding records remain separately inspectable.

This identifier is supported but not required. A civic influence record system
MAY satisfy AR.INTERPRETATION.RECORD without specializing it through
CIR.INTERPRETATION.RECORD.

Systems that record civic influence inferences SHOULD specialize through this
identifier to support inference-type-specific verification.

## CIR.LOBBYING.RECORD

CIR MUST provide a structural form for lobbying records.

Lobbying records:

- MUST reference the source filing
- MUST identify the lobbying entity and lobbied entity where declared
- MUST identify time period and subject matter where available
- MUST be distinguishable from claim records and interpretation records
- MUST NOT imply policy outcome, success, or causal influence

A lobbying record represents a source-backed lobbying disclosure. It does not
establish whether the lobbying caused, influenced, or produced an outcome.

## CIR.ORGANIZATION.RECORD

CIR MUST provide a structural form for organization records.

Organization records:

- MUST use stable identifiers
- MUST conform to AR.IDENTITY.RECORD
- MUST identify organization type where declared
- MUST be distinguishable from person records and role records
- MUST NOT assert ideological alignment, intent, or coordination as substrate
  facts

An organization record identifies an organization for civic influence records.
It does not assert the organization’s intent, ideology, coordination, control,
or wrongdoing.

## CIR.PERSON.RECORD

CIR MUST provide a structural form for person records.

Person records:

- MUST use stable identifiers
- MUST conform to AR.IDENTITY.RECORD
- MUST be distinguishable from organization records and role records
- MUST NOT assert ideological alignment, intent, or coordination as substrate
  facts
- MUST support privacy and identity disclosure constraints declared by the
  implementing system

A person record identifies an individual as a civic influence referent. It does
not assert intent, ideology, coordination, endorsement, or wrongdoing.

## CIR.POLICY_DOCUMENT.REFERENCE

CIR MUST provide a structural form for policy document references.

Policy document references:

- MUST use stable identifiers
- MUST be referenceable from claim, lobbying, and relationship records
- MUST be distinguishable from interpretations of the referenced document
- MUST NOT be modified to reflect interpretation of the referenced document

A policy document reference identifies a document. It does not assert the
meaning, validity, purpose, influence, or effect of the document.

## CIR.PROVENANCE.SOURCE

CIR MAY provide a structural form for source-filing provenance that represents
the chain from a source filing to one or more derived civic influence records.

Source-filing provenance records:

- MUST conform to AR.PROVENANCE
- MUST identify the originating source filing
- MUST identify the records derived from the source filing
- MUST identify methods or processes used in derivation where known
- MUST be distinguishable from the source filing and from the derived records
- MUST NOT modify the source filing or the derived records
- MUST NOT assert correctness, completeness, authority, legitimacy, obligation,
  causation, endorsement, control, coordination, or enforcement

Source filings in the civic influence domain are typically external public
filings, including campaign finance, lobbying, nonprofit, corporate, and
government spending records. The chain from filing to derived record is
load-bearing for inspection, contestation, and audit. Source-filing provenance
SHOULD be traceable from each derived record back to the originating filing.

This identifier is supported but not required. A civic influence record system
MAY satisfy AR.PROVENANCE without specializing it through CIR.PROVENANCE.SOURCE.

Systems that derive records from external public filings SHOULD specialize
through this identifier to support filing-chain-specific verification.

## CIR.RELATIONSHIP.RECORD

CIR MUST provide a structural form for relationship records.

Relationship records:

- MUST identify related entities
- MUST identify relationship type as a declared type
- MUST reference the source supporting the relationship
- MUST identify time bounds where available
- MUST be distinguishable from inference records, claim records, and
  interpretation records
- MUST NOT imply causation, endorsement, control, ideological agreement, or
  coordination by default

A relationship record is source-backed. It records a relationship represented in
a source; it does not convert that relationship into an inference by default.

## CIR.ROLE.RECORD

CIR MUST provide a structural form for role records.

Role records:

- MUST identify the person
- MUST identify the role-holding entity
- MUST identify the role type
- MUST identify the time period where available
- MUST reference the source supporting the role
- MUST be distinguishable from person records and organization records
- MUST NOT imply that the person endorses, controls, or shares intent with the
  role-holding entity beyond what the role itself declares

A role record records a declared role. It does not establish endorsement,
control, shared intent, or corporate action.

## CIR.SCOPE.EXCLUSIONS

This specification does not define:

- domain vocabularies beyond the CIR record profile
- causation
- endorsement
- control
- ideological agreement
- coordination
- wrongdoing
- public influence scoring
- legal or ethical judgment
- recommendation or decision logic
- source data hosting
- automatic entity truth
- source truth certification
- endorsement certification
- control certification
- replacements for source databases or public filing systems

These concerns are explicitly out of scope.

## CIR.TIME_BOUND.REFERENCE

CIR MUST provide a structural form for time-bound references.

Time-bound references:

- MUST identify start time where available
- MUST identify end time where available
- MUST distinguish unknown bounds from open-ended bounds
- MUST NOT assert that time bounds imply causation or coordination

Time bounds describe temporal scope. They do not establish influence,
coordination, causation, or relationship significance by default.

## CIR.VERSIONING

CIR MUST define explicit versioning rules.

Versioning:

- MUST conform to AR.VERSIONING
- MUST identify the CIR version
- MUST identify the underlying AR version
- MUST NOT allow silent or implicit change

CIR versions identify the record profile and conformance target. They do not
assert stability of source systems, public filings, or civic interpretations.
