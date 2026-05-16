# Civic Influence Record Conformance Checklist

This document defines the criteria for determining whether an artifact conforms
to the Civic Influence Record specification.

Identifiers referenced in this document are the sole normative reference.
Section ordering, formatting, and presentation are non-normative.

An artifact may be a civic influence record system, export bundle, repository,
domain profile, or other deliverable claiming conformance.

## Conformance Overview

An artifact CONFORMS if and only if:

- all mandatory requirements are satisfied
- no prohibited assertions are present
- conformance with Accountable Record is preserved
- conformance with Structural Explainability is preserved
- civic influence records remain source-backed, inspectable, and contestable
- civic influence records do not assert causation, endorsement, control,
  ideological agreement, coordination, legitimacy, or wrongdoing by default

Failure of any single check constitutes non-conformance.

## CIR.AFFILIATION.RECORD

- [ ] Affiliation records identify the affiliated entities.
- [ ] Affiliation records identify the affiliation type as a declared type.
- [ ] Affiliation records conform to CIR.RELATIONSHIP.RECORD.
- [ ] Affiliation records do not imply endorsement.
- [ ] Affiliation records do not imply ideological agreement.
- [ ] Affiliation records do not imply coordination, control, or shared intent.
- Fail if: affiliation is treated as endorsement, ideological agreement,
  coordination, control, or shared intent.

## CIR.CLAIM.RECORD

- [ ] Claim records conform to AR.CLAIM.RECORD.
- [ ] Claim records reference the records the claim is about.
- [ ] Claim records identify the asserting actor.
- [ ] Claim records remain distinguishable from relationship records.
- [ ] Claim records do not assert causation, endorsement, control, or
  coordination unless those are declared claim types with explicit source support.
- Fail if: a claim is treated as a source-backed relationship or as
  undeclared causation, endorsement, control, or coordination.

## CIR.COLLAPSE.PROHIBITED

- [ ] Association remains distinct from endorsement.
- [ ] Employment remains distinct from corporate action.
- [ ] Funding remains distinct from authorship.
- [ ] Grants remain distinct from control.
- [ ] Lobbying remains distinct from policy outcome.
- [ ] Shared personnel remains distinct from unified intent.
- [ ] Network proximity remains distinct from causation.
- [ ] Entity resolution remains distinct from ideological agreement.
- [ ] Relationship remains distinct from inference.
- [ ] Source-backed record remains distinct from interpretation.
- [ ] Source provenance remains distinct from source truth.
- [ ] Source provenance remains distinct from endorsement.
- [ ] Interpretation remains distinct from source-backed relationship.
- Fail if: a civic influence record collapses any prohibited civic influence category.

## CIR.CONFORMANCE.AR.REQUIRED

- [ ] The artifact declares conformance with AR.
- [ ] The artifact preserves all AR constraints.
- [ ] The artifact does not weaken, override, or reinterpret AR.
- Fail if: CIR conformance is asserted while weakening, overriding, or reinterpreting AR.

## CIR.CONFORMANCE.SE.REQUIRED

- [ ] The artifact declares conformance with SE.
- [ ] The artifact preserves SE neutrality constraints.
- [ ] The artifact does not weaken, override, or reinterpret SE.
- Fail if: CIR conformance is asserted while weakening, overriding, or reinterpreting SE neutrality.

## CIR.CONTRIBUTION.RECORD

- [ ] Contribution records identify contributor and recipient entities.
- [ ] Contribution records identify amount and time where available.
- [ ] Contribution records reference the source filing.
- [ ] Contribution records remain distinguishable from claim records and interpretation records.
- [ ] Contribution records do not imply influence, endorsement, control, or expectation of outcome.
- Fail if: contribution is treated as influence, endorsement, control, or expected outcome.

## CIR.DEFINITION.CORE

- [ ] The artifact treats CIR as a domain profile of AR.
- [ ] The artifact limits CIR to source-backed civic influence records and prohibited collapses.
- [ ] The artifact does not define causation, endorsement, control, ideological agreement,
  wrongdoing, influence scoring, legal or ethical judgment, recommendation,
  decision logic, source data hosting, or automatic entity truth.
- Fail if: CIR is treated as a causation model, endorsement model, control model,
  scoring system, judgment system, recommendation engine, or source data host.

## CIR.ENTITY_RESOLUTION.RECORD

- [ ] Entity resolution records identify the source-backed references being resolved.
- [ ] Entity resolution records identify evidence supporting the resolution.
- [ ] Entity resolution records identify the asserting actor.
- [ ] Entity resolution records remain distinguishable from source-backed references.
- [ ] Entity resolution records do not modify source-backed references.
- [ ] Entity resolution records do not imply ideological agreement, coordination, or shared intent.
- [ ] Entity resolution records are revisable as new evidence becomes available.
- Fail if: entity resolution is treated as source-record merger, ideological agreement,
  coordination, shared intent, or automatic entity truth.

## CIR.INTERPRETATION.RECORD

- [ ] CIR interpretation records conform to AR.INTERPRETATION.RECORD when used.
- [ ] CIR interpretation records identify the interpretive inference type as a declared type.
- [ ] CIR interpretation records identify the records on which the interpretation depends.
- [ ] CIR interpretation records identify the asserting actor or framework.
- [ ] CIR interpretation records remain distinguishable from relationship records and claim records.
- [ ] CIR interpretation records do not modify source-backed records.
- [ ] CIR interpretation records do not convert an interpretation into a source-backed relationship.
- [ ] CIR interpretation records do not assert correctness, authority, legitimacy, obligation, or enforcement.
- Fail if: civic influence interpretation is treated as source-backed relationship,
  substrate fact, correctness, authority, legitimacy, obligation, or enforcement.

## CIR.LOBBYING.RECORD

- [ ] Lobbying records reference the source filing.
- [ ] Lobbying records identify the lobbying entity and lobbied entity where declared.
- [ ] Lobbying records identify time period and subject matter where available.
- [ ] Lobbying records remain distinguishable from claim records and interpretation records.
- [ ] Lobbying records do not imply policy outcome, success, or causal influence.
- Fail if: lobbying is treated as policy success, outcome, causation, or influence proof.

## CIR.ORGANIZATION.RECORD

- [ ] Organization records use stable identifiers.
- [ ] Organization records conform to AR.IDENTITY.RECORD.
- [ ] Organization records identify organization type where declared.
- [ ] Organization records remain distinguishable from person records and role records.
- [ ] Organization records do not assert ideological alignment, intent, or
  coordination as substrate facts.
- Fail if: an organization record is treated as ideological alignment, intent,
  coordination, or undifferentiated person/role record.

## CIR.PERSON.RECORD

- [ ] Person records use stable identifiers.
- [ ] Person records conform to AR.IDENTITY.RECORD.
- [ ] Person records remain distinguishable from organization records and role records.
- [ ] Person records do not assert ideological alignment, intent, or
  coordination as substrate facts.
- [ ] Person records support privacy and identity disclosure constraints declared
  by the implementing system.
- Fail if: a person record is treated as ideological alignment, intent,
  coordination, organization record, role record, or privacy-insensitive disclosure by default.

## CIR.POLICY_DOCUMENT.REFERENCE

- [ ] Policy document references use stable identifiers.
- [ ] Policy document references are referenceable from claim, lobbying, and relationship records.
- [ ] Policy document references remain distinguishable from interpretations of the referenced document.
- [ ] Policy document references are not modified to reflect interpretation of the referenced document.
- Fail if: policy document references are treated as interpretations or modified by interpretation.

## CIR.PROVENANCE.SOURCE

- [ ] Source-filing provenance records conform to AR.PROVENANCE when used.
- [ ] Source-filing provenance records identify the originating source filing.
- [ ] Source-filing provenance records identify the records derived from the source filing.
- [ ] Source-filing provenance records identify derivation methods or processes where known.
- [ ] Source-filing provenance records remain distinguishable from the source filing and derived records.
- [ ] Source-filing provenance records do not modify the source filing or derived records.
- [ ] Source-filing provenance records do not assert correctness, completeness, authority,
  legitimacy, obligation, causation, endorsement, control, coordination, or enforcement.
- Fail if: source provenance is treated as source truth, endorsement, control, causation,
  correctness, completeness, authority, or mutation of source/derived records.

## CIR.RELATIONSHIP.RECORD

- [ ] Relationship records identify related entities.
- [ ] Relationship records identify relationship type as a declared type.
- [ ] Relationship records reference the source supporting the relationship.
- [ ] Relationship records identify time bounds where available.
- [ ] Relationship records remain distinguishable from inference records, claim records, and
  interpretation records.
- [ ] Relationship records do not imply causation, endorsement, control,
  ideological agreement, or coordination by default.
- Fail if: relationship is treated as inference, causation, endorsement, control,
  ideological agreement, or coordination by default.

## CIR.ROLE.RECORD

- [ ] Role records identify the person.
- [ ] Role records identify the role-holding entity.
- [ ] Role records identify the role type.
- [ ] Role records identify the time period where available.
- [ ] Role records reference the source supporting the role.
- [ ] Role records remain distinguishable from person records and organization records.
- [ ] Role records do not imply that the person endorses, controls, or shares intent
  with the role-holding entity beyond what the role itself declares.
- Fail if: role is treated as endorsement, control, shared intent, person identity, or
  organization identity.

## CIR.SCOPE.EXCLUSIONS

Verify that the artifact does not define:

- [ ] causation
- [ ] endorsement
- [ ] control
- [ ] ideological agreement
- [ ] wrongdoing
- [ ] public influence scoring
- [ ] legal or ethical judgment
- [ ] recommendation or decision logic
- [ ] source data hosting
- [ ] automatic entity truth
- [ ] source truth certification
- [ ] endorsement certification
- [ ] control certification
- [ ] replacements for source databases or public filing systems

Presence of any excluded concern as a CIR-defined construct constitutes non-conformance.

## CIR.TIME_BOUND.REFERENCE

- [ ] Time bound references identify start time where available.
- [ ] Time bound references identify end time where available.
- [ ] Time bound references distinguish unknown bounds from open-ended bounds.
- [ ] Time bound references do not assert that time bounds imply causation or coordination.
- Fail if: time bounds are treated as causation, coordination, or influence chains.

## CIR.VERSIONING

- [ ] CIR versioning conforms to AR.VERSIONING.
- [ ] CIR identifies the CIR version.
- [ ] CIR identifies the underlying AR version.
- [ ] CIR does not allow silent or implicit change.
- Fail if: CIR or AR versioning is missing, implicit, unstable, or silently changed.

## Final Determination

An artifact CONFORMS if:

- all checks above pass
- no prohibited assertions are present
- conformance with Accountable Record is preserved
- conformance with Structural Explainability is preserved
- civic influence records remain source-backed, inspectable, and contestable
- causation, endorsement, control, ideological agreement, coordination,
  legitimacy, wrongdoing, and judgment remain outside substrate records

Otherwise, the artifact is NON-CONFORMANT.

## Conformance Declaration

Artifacts claiming conformance SHOULD include a declaration of the form:

```text
Conforms to: CIR Specification vX.Y
Conforms to: AR Specification vX.Y
Conforms to: SE Specification vX.Y
```
