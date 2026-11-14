# maturity-model-standard

Normative source of truth for the **maturity-model repository standard** across the [Assessment-Models](https://github.com/Assessment-Models) organization.

Established by [CR-AM-ORG-RES-000 — Organization-Wide Maturity Model Repository Standardization, Architecture and Global Conformance](change-requests/CR-AM-ORG-RES-000.md). Builds on [CR-AM-11 — Federated Assessment Model Ecosystem](https://github.com/technehub-labs/dea-metamodel/blob/main/change-requests/CR-AM-11.md), under the CR-AM-01 umbrella.

> **Naming note.** This initiative was drafted as an elevation of a repository-standardization proposal informally numbered "CR-AM-12". The `CR-AM-12` slot in the metamodel change-request series (`technehub-labs/dea-metamodel/change-requests/`) is occupied by the *Cardinal Root, Cross-Model Relations and the Dotted Line* CR. To avoid a numbering collision, the initiative is established here as **CR-AM-ORG-RES-000**, the first entry in the Assessment-Models organization-resolution series. See the [resolution](change-requests/CR-AM-ORG-RES-000.md) for the full reconciliation record.

## What this repository governs

The standard is organized in three governance layers:

| Layer | Scope | Governed here |
|---|---|---|
| **Organization** | Assessment-Models | The repository standard, schemas, reusable conformance workflow, conformance policy, portfolio conformance registry, repository template |
| **Repository** | Every `maturity-model-*` repository | Standardized structure, standard README, machine-readable model, documentation, examples, model-specific extensions |
| **Consumer** | Assessment implementations | Not governed here — consumers consume versioned model releases through the registry |

**The principle: standardize the repository architecture, never the model's intellectual content.** Each maturity model keeps its own dimensions, criteria, scales, scoring rules and evidence semantics, provided they are explicitly defined and conform to the applicable canonical contracts.

## Contents

| Path | Role |
|---|---|
| [`standard.yaml`](standard.yaml) | Normative identity and version of the standard (currently **1.0.1**) |
| [`specifications/`](specifications/) | Normative specifications: repository, README, metadata, documentation, conformance, governance |
| [`schemas/`](schemas/) | Machine-readable schemas (standard declaration) |
| [`validators/`](validators/) | Local validation utilities |
| [`.github/workflows/repository-conformance.yml`](.github/workflows/repository-conformance.yml) | **Reusable** `workflow_call` workflow every conformant repository can call |
| [`registry/conformance.yaml`](registry/conformance.yaml) | Portfolio conformance registry (classification + standard-version + conformance level) |
| [`templates/`](templates/) | Pointers to the scaffold (implemented in [`maturity-model-template`](https://github.com/Assessment-Models/maturity-model-template)) |
| [`migrations/`](migrations/) | Controlled propagation and migration method |
| [`examples/`](examples/) | Example declarations and artifacts |
| [`change-requests/`](change-requests/) | The organization resolutions that govern this standard |
| [`fixtures/`](fixtures/) | Positive and negative controls for the validator |

## Relationship to existing ecosystem machinery (reconciliation)

This standard **composes with** the machinery CR-AM-11 already delivered. It does not replace any of it:

| Existing capability (more mature than the plan) | Reconciliation |
|---|---|
| `model.yaml` contract handshake (CR-AM-11 §15/§22), validated by `assessment-ci` | **Remains the authoritative identity manifest.** The new `standard.yaml` declaration binds a repository to the repository standard and is cross-checked against `model.yaml`, `VERSION` and the README status line — it never restates contract handshakes |
| `assessment-registry` — registration records, immutable refs, manifest coherence | **Remains the identity spine.** The portfolio conformance registry records repository-standard adoption only; the intended long-term home for these fields is the registration schema (tracked as a reconciliation issue) |
| Three-level CI (local, contract, ecosystem) in `assessment-ci` + `assessment-registry` | **Unchanged.** Repository-standard conformance is an additional, additive gate delivered as a reusable workflow; Levels 1–3 remain independently identifiable |
| Repository taxonomy, naming and legacy classification in [`.github/GOVERNANCE.md`](https://github.com/Assessment-Models/.github/blob/main/GOVERNANCE.md) | **Extended, not replaced.** Classification (maturity-model vs assessment-model vs shared infrastructure vs legacy) is performed *before* any restructuring; legacy naming exceptions and frozen repositories are respected |
| Canonical metamodel and contracts in [`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) | **Remain the semantic authority.** This standard governs repository architecture, documentation and conformance only |

## How a repository adopts the standard

1. Add a root `standard.yaml` declaring the standard id, version and conformance level (see the [metadata standard](specifications/metadata-standard.md)).
2. Add the reusable conformance workflow call (see below).
3. Close structural gaps additively — no renames, no destructive rewrites, no content changes to model semantics.
4. The conformance level is recorded in the [portfolio conformance registry](registry/conformance.yaml).

Conformance levels:

| Level | Meaning |
|---|---|
| `registered` | Identified in the ecosystem registry, with a valid standard declaration and identity coherence |
| `structural` | Meets the repository structure, metadata, version-coherence and documentation-baseline requirements |
| `full` | Passes structural checks plus complete README, documentation and diagram requirements |

Where established repository structure legitimately differs from the target layout, the declaration records explicit **structure mappings** (added in v1.0.1): a role such as `model-definition` is satisfied by mapped paths instead of its default location — recorded, reviewed and integrity-checked, never a rename (rule R1). See [repository standard §6](specifications/repository-standard.md).

## Reusable conformance workflow

Any `maturity-model-*` repository can validate its declaration and structure by calling:

```yaml
jobs:
  repository-standard:
    uses: Assessment-Models/maturity-model-standard/.github/workflows/repository-conformance.yml@main
```

The workflow checks the declaration, cross-checks `standard.yaml` against `model.yaml`, `VERSION` and the README status line, and verifies structure by declared conformance level. It runs alongside the existing Level 1/2/3 CI — it does not replace any of them.

## Policy enforcement vs content propagation

Two different kinds of "global enforcement" are kept deliberately separate (see the [governance standard](specifications/governance-standard.md)):

- **Policy enforcement** — centrally controlled: required status checks, organization rulesets, conformance-level tracking.
- **Content propagation** — always reviewable and attributable: standard updates cascade through generated, repository-specific pull requests, never through automatic overwriting of repository content.

## Licence

MIT — see [LICENSE](LICENSE).
