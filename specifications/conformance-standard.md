# Conformance Standard — Normative Specification

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)

## 1. Conformance levels

Three adoption states exist. They are repository-standard adoption states, **not** maturity levels.

| Level | Meaning | Validated by |
|---|---|---|
| `registered` | Identified in the ecosystem registry; valid `standard.yaml` declaration; identity coherent (`standard.yaml` ↔ `model.yaml` ↔ `VERSION`) | Reusable conformance workflow (declaration checks) |
| `structural` | `registered` + required repository structure, metadata and README baseline present | Reusable conformance workflow (structure checks by declared level) |
| `full` | `structural` + complete README (22 sections), documentation set, required diagrams, mappings, documentation consistent with the model definition | Reusable conformance workflow + documentation review |

## 2. Classification precedes restructuring

Not every repository in Assessment-Models receives the maturity-model standard. Classification follows the taxonomy in [`.github/GOVERNANCE.md`](https://github.com/Assessment-Models/.github/blob/main/GOVERNANCE.md) and is recorded in the [portfolio conformance registry](../registry/conformance.yaml) **before** any migration:

| Classification | Treatment |
|---|---|
| Maturity model | Full maturity-model repository standard (this document) |
| Assessment model | Separate assessment-model standard (out of scope for standard v1.0.0) |
| Assessment tool | Tool/application architecture |
| Metamodel or contract | Semantic and schema governance (excluded) |
| Registry or catalogue | Registry and catalogue architecture (excluded) |
| Shared infrastructure | Reusable engineering standards (excluded) |
| Legacy (frozen/superseded) | Excluded — remains frozen per CR-AM-01 Release 1 D-1 |
| Organization governance | Excluded (`.github`, `assessment-ci`, `assessment-registry`, this repository, the template) |

## 3. Relation to the three-level CI model

The CR-AM-11 CI levels remain independently identifiable and unchanged:

| Level | Scope | Status under this standard |
|---|---|---|
| Level 1 — local model CI | Manifest, scale, examples, scoring math | Unchanged (each repository's `local-model-ci.yml`) |
| Level 2 — contract conformance CI | §15 handshake vs pinned `dea-metamodel` release | Unchanged (reusable from `assessment-ci`) |
| Level 3 — ecosystem CI | Registry integrity, cross-repository references | Unchanged (`assessment-ci` + `assessment-registry`) |
| **Repository-standard conformance** | Declaration, structure, version coherence, README baseline | **New, additive gate** — reusable from this repository |

## 4. Portfolio conformance registry

[`registry/conformance.yaml`](../registry/conformance.yaml) records, per repository: classification, declared standard version, conformance level, and notes. The registry is updated when a repository's adoption PR merges. Non-conformant repositories are identifiable and tracked there.

**Reconciliation:** `assessment-registry` remains the identity spine (id, release, contract handshake, immutable refs). The portfolio registry records standard adoption only. Consolidating these fields into the registration schema is a tracked reconciliation item; until then the two views are joined by repository identity.

## 5. Enforcement model

- **Policy enforcement (central):** required status checks and conformance-level tracking are centrally controlled. Organization rulesets MAY be applied to enforce branch/tag policies, subject to the organization's GitHub plan and the existing CR-AM-11 CI baseline policies.
- **Content propagation (attributable):** standard updates cascade through generated, repository-specific pull requests reviewed by each repository's maintainers. A reusable workflow cannot and MUST NOT automatically restructure repository files. See the [governance standard](governance-standard.md).

## 6. Drift detection

Version coherence (README ↔ `model.yaml` ↔ `VERSION` ↔ `standard.yaml`) is checked on every PR in repositories that wire the reusable workflow, and periodically at portfolio level. Documentation drift against the machine-readable model is checked wherever automated consistency checking is feasible.
