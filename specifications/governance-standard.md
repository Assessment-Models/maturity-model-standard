# Governance Standard — Normative Specification

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)

## 1. Ownership

- **Assessment-Models** owns the repository standard, the template, the portfolio conformance registry and the conformance policy.
- **`technehub-labs/dea-metamodel`** remains the canonical engineering authority for the metamodel, contracts, scales and scoring semantics. This standard references those contracts; it never redefines them.
- **Each maturity-model repository** retains independent ownership of its domain model definition, versioning, releases and evolution.
- **Downstream assessment consumers** consume published model releases through the registry, never repository structure.

## 2. Standard lifecycle

- The standard is SemVer-versioned (`standard.yaml`); each version is recorded in `CHANGELOG.md`.
- Changes to normative requirements MUST go through an organization resolution (ORG-RES series) in this repository's `change-requests/`.
- Documentation corrections that do not alter normative semantics MAY follow the standard contribution process.

## 3. How changes cascade (controlled propagation)

```text
1. A new standard version is approved (organization resolution).
2. This repository publishes updated specifications, schemas, templates and workflows.
3. The conformance process identifies affected repositories via the portfolio registry.
4. Automated migration tooling (migrations/) prepares repository-specific changes.
5. Pull requests are generated for maintainers to review.
6. CI validates the changes (Level 1/2/3 + repository-standard conformance).
7. Merged changes update each repository's declared standard version.
8. The portfolio conformance registry records the new conformance state.
```

Global consistency without uncontrolled overwriting of repository-specific content.

## 4. Policy enforcement vs content propagation

- **Policy enforcement** — required status checks, conformance tracking, organization rulesets (branch/tag policies) — is centrally controlled.
- **Content propagation** — directories, READMEs, model files, examples — always lands as reviewable, attributable, repository-specific pull requests. No blanket automated rewrites.

## 5. Migration invariants

Migration MUST: preserve existing model definitions, identifiers, version history, provenance and lineage; preserve valid scoring semantics; introduce explicit mappings where structures change; avoid unnecessary model redesign; maintain compatibility with existing consumers; record migration status and remaining gaps. Repositories are never declared conformant merely because their directory structure matches the template.

## 6. Migration pipeline

```text
DISCOVER → ASSESS → MAP → STANDARDIZE → VALIDATE → REGISTER → RELEASE
```

Classification precedes restructuring; the reference implementation precedes portfolio-wide migration; nothing is destructively rewritten as a first step.
