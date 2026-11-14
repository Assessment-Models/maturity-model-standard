# Repository Standard — Normative Specification

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)
**Applies to:** every repository classified `maturity-model` under the Assessment-Models taxonomy

## 1. Architectural principle

**Common structure, independent semantics.**

Every maturity-model repository MUST follow the standard repository architecture. Each model MUST retain its own domain-specific semantics: dimensions, criteria, maturity levels, scoring rules, evidence requirements and progression semantics. The standard never prescribes the number of maturity levels, their names, dimension sets, or scoring algorithms.

## 2. Required repository structure (target)

```text
maturity-model-<domain>/
├── README.md                     # standard README (see readme-standard.md)
├── standard.yaml                 # repository-standard declaration (see metadata-standard.md)
├── model.yaml                    # CR-AM-11 §15 contract handshake — AUTHORITATIVE manifest
├── VERSION                       # authoritative repository release version
├── CHANGELOG.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md                   # recommended
│
├── maturity/
│   ├── scale.yaml                # model-owned scale bound to the canonical instance (never minted)
│   └── model/<domain>.yaml       # authoritative domain model definition
│
├── docs/                         # detailed documentation (see documentation-standard.md)
│   ├── overview.md
│   ├── architecture.md
│   ├── assessment-methodology.md
│   ├── maturity-levels.md
│   ├── dimensions.md
│   ├── evidence-framework.md
│   ├── provenance.md
│   ├── governance.md
│   ├── use-cases.md
│   └── diagrams/
│
├── schemas/                      # by reference to this standard and assessment-ci; do not fork schemas
├── examples/                     # at least one valid, reproducible worked example
├── mappings/                     # explicit mappings to source/legacy/external frameworks
├── scripts/
│   └── local_validate.py         # Level 1 validator
└── .github/
    ├── workflows/
    │   ├── local-model-ci.yml            # Level 1
    │   ├── contract-conformance.yml       # Level 2 (reusable from assessment-ci)
    │   └── repository-standard.yml        # repository-standard conformance (reusable from here)
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

## 3. Mapping to the existing CR-AM-11 structure (reconciliation)

The existing federated repository layout is **more mature than this specification is allowed to break**. The standard therefore ratifies the existing conventions and layers additively:

| Artifact | Existing convention (CR-AM-11) | Standard treatment |
|---|---|---|
| `model.yaml` | §15 contract handshake, schema-validated by `assessment-ci` | **Retained verbatim. Authoritative identity manifest.** The `standard.yaml` declaration cross-references it; it never duplicates the handshake |
| `VERSION` | Authoritative release version | Retained; cross-checked against `model.yaml`, `standard.yaml` and the README status line |
| `maturity/scale.yaml`, `maturity/model/` | Model-owned scale and definition | Retained; `full` conformance additionally documents levels/dimensions in `docs/` |
| `examples/`, `scripts/local_validate.py` | Worked example + Level 1 validator | Retained; extended, not replaced |
| `.github/workflows/local-model-ci.yml`, `contract-conformance.yml` | Level 1/2 CI | Retained; a third workflow (`repository-standard.yml`) calls the reusable conformance workflow defined in this repository |
| Registration record in `assessment-registry` | Identity spine, immutable refs | Retained; the portfolio conformance registry records standard adoption only |
| `docs/`, `mappings/`, `schemas/`, `CONTRIBUTING.md`, `SECURITY.md`, templates | Absent in most repos | **Additive**; introduced per the migration method, never by destructive rewrite |

**Rules:**

- R1. No existing file or directory is renamed, moved or deleted to achieve conformance. Where an established naming convention differs, an explicit structure mapping is recorded instead.
- R2. Changes are additive and non-destructive; existing model semantics, identifiers, history, provenance and downstream dependencies are preserved.
- R3. New repositories created after this standard MUST be created from [`maturity-model-template`](https://github.com/Assessment-Models/maturity-model-template).
- R4. Repositories of other taxonomy classes (`assessment-model-*`, shared infrastructure, legacy catalogs, org-governed) MUST NOT adopt the maturity-model standard; see [conformance-standard.md](conformance-standard.md) §Classification.

## 4. File responsibilities

| File | Responsibility |
|---|---|
| `README.md` | Primary human-facing entry point; MUST satisfy the [README standard](readme-standard.md) at the declared conformance level |
| `standard.yaml` | Repository-standard declaration only (see the [metadata standard](metadata-standard.md)) |
| `model.yaml` | Model manifest and contract handshake: identity, type, version, conformance source, dependencies, compatibility (CR-AM-11 §15/§22) |
| `VERSION` | Authoritative repository release version (SemVer) |
| `CHANGELOG.md` | History of model changes and their compatibility implications |
| `maturity/scale.yaml` | Model's maturity scale, bound to (never duplicating) the canonical shared scale via a versioned dependency |
| `maturity/model/<domain>.yaml` | Authoritative domain model: dimensions, criteria, level characteristics, assessment semantics |
| `docs/` | Explanatory and operational documentation consistent with the authoritative model definition |
| `examples/` | Valid, reproducible model and assessment examples consistent with the model and scoring rules |
| `mappings/` | Explicit mappings to source frameworks, legacy versions, external references |
| `scripts/` | Local validation and maintenance utilities |
| `.github/workflows/` | Level 1/2 CI plus the repository-standard conformance call |

## 5. Machine-readable authority

Machine-readable model definitions (`model.yaml`, `maturity/`) are authoritative over explanatory documentation. Documentation MUST be consistent with those definitions; where automated consistency checking is feasible, CI MUST perform it. Documentation drift is a conformance failure, not a cosmetic issue.
