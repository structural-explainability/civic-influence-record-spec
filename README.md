# civic-influence-record (CIR)

[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/civic-influence-record)
[![Tooling](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/civic-influence-record/actions/workflows/ci-python.yml/badge.svg?branch=main)](https://github.com/structural-explainability/civic-influence-record/actions/workflows/ci-python.yml)
[![Links](https://github.com/structural-explainability/civic-influence-record/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/civic-influence-record/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/structural-explainability/civic-influence-record/security)

> Civic influence accountable record system for source-backed relationships, organizations,
> people, funding, lobbying, roles, affiliations, documents, and claims.

## Overview

Civic Influence Record defines a domain record system for representing
source-backed civic influence structures as durable, inspectable records.

Civic Influence Record records:

- people, organizations, and roles
- funding, contribution, and lobbying records
- affiliations and policy documents
- source records and relationship records
- entity resolution records
- claims, interpretations, and reports

Civic Influence Record does not assert causation, endorsement, control,
ideological agreement, coordination, legitimacy, or wrongdoing by default.

## Purpose

The purpose of Civic Influence Record is to provide a durable record structure
for inspecting influence-relevant relationships without collapsing them into
stronger claims.

Civic Influence Record defines constraints on:

- organization records
- person records
- source records
- relationship records
- entity resolution records
- funding and contribution records
- lobbying and public filing references
- policy document records
- claim and interpretation records
- rendered influence reports

Civic Influence Record helps protect civic information systems
from specific failure modes:

- treating association as endorsement
- treating employment as corporate action
- treating funding as authorship
- treating grants as control
- treating lobbying as policy success
- treating shared personnel as unified intent
- treating network proximity as causation
- treating entity resolution as ideological agreement

## Versioning and Stability

Current versions are pre-v1.
The contract is being co-developed with its
implementations and verifiers;
dependencies track main during this phase.
Versioned releases will follow once the contract stabilizes.

v1 will commit to:

- the civic influence record model shape
- entity resolution evidence requirements
- relationship typing requirements
- time-bound recording conventions

v1 does not claim closure over influence, causation, ideology,
coordination, endorsement, or control.

## Extension Policy

Extension policy applies once v1 stabilizes.
Until then, the contract is in active development
and changes occur on main.
Extension is permitted under a new version of the record model
or through declared profile extensions.

Any extension MUST:

- preserve conformance with the Accountable Record contract
- preserve source traceability
- preserve the distinction between relationship and inference
- preserve the distinction between entity resolution and substantive agreement
- preserve the distinction between funding, influence, authorship, and control
- declare prohibited inferences for new record types or fields
- be explicit, traceable, and verifiable

## Scope

This system defines:

- civic influence accountable records
- person and organization records
- source-backed relationship records
- entity resolution records
- funding, contribution, lobbying, and public filing references
- policy document and claim records
- interpretation records
- human-readable civic influence reports
- export bundles for verification

This system does NOT define:

- causation
- endorsement
- control
- ideological agreement
- wrongdoing
- public influence scoring
- legal or ethical judgment
- recommendation or decision logic
- source data hosting
- automatic entity truth
- replacements for source databases or public filing systems

## Relationship to Other Work

- Civic Influence Record implements the Accountable Record contract for
  civic influence materials.
- Other implementations could organize civic influence records differently
  while still satisfying the contract.
- Civic Influence Record may consume data from sources such as FEC,
  LDA.gov, USAspending, ProPublica Nonprofit Explorer, OpenCorporates,
  OpenSecrets, and LittleSis, and from public campaign finance, lobbying,
  nonprofit, corporate, government spending, and public filing records.
- Civic Influence Record does not replace those sources.
- Civic Influence Record produces export bundles that may be checked by
  `se-verification-civic-influence-record`.
- SE verification checks whether Civic Influence Record preserves SE-relevant
  distinctions without determining causation, endorsement, control, or judgment.

## Clarifying Statement

Civic Influence Record records source-backed civic relationships,
not causation or judgment.

A civic influence record may show that a person, organization, filing,
funding record, lobbying report, policy document, or relationship
was recorded from a source.
It does not assert that the relationship caused an outcome, demonstrated
control, established endorsement, or resolved disagreement about influence.

Civic Influence Record exists so that civic influence structures can remain
inspectable across disagreement, reinterpretation, and time.

## Repository Contents

- [README.md](./README.md) - Project overview
- [DECISIONS.md](./DECISIONS.md) - Founding design decisions
- [RECORD_MODEL.md](./RECORD_MODEL.md) - Civic influence record model
- [EXPORTS.md](./EXPORTS.md) - Export bundle description
- [ANNOTATIONS.md](./ANNOTATIONS.md) - Annotation standards
- [LICENSE](./LICENSE) - Licensing terms
- [CITATION.cff](./CITATION.cff) - Citation metadata
- [CHANGELOG.md](./CHANGELOG.md) - Version history
- [data/examples](./data/examples) - Example civic influence records
- [data/records](./data/records) - Record fixtures
- [data/exports](./data/exports) - Verification-ready exports

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/structural-explainability/civic-influence-record

cd civic-influence-record
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

# install git hooks once per clone
uvx pre-commit install

# autofix and manual fix issues
git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# generate/check registry artifacts
uv run se-validate
uv run se-ref-export
uv run se-ref-export --check
uv run se-ref-validate
uv run se-validate --strict

# do chores
uv run python -m pyright
uv run python -m pytest

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
