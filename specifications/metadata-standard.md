# Metadata Standard — The `standard.yaml` Declaration

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)
**Schema:** [`schemas/standard-declaration.schema.json`](../schemas/standard-declaration.schema.json)

## 1. Purpose

Every applicable repository declares its adoption of the repository standard in a root `standard.yaml`. The declaration makes standard adoption **machine-readable, cross-checkable and trackable** across the portfolio.

## 2. Declaration format

```yaml
repository:
  type: maturity-model
standard:
  id: AM-MODEL-REPOSITORY-STANDARD
  version: "1.0.0"
  conformance: structural
model:
  id: maturity-model-<domain>
  name: <Human-readable model name>
  version: "<must equal model.yaml version and VERSION>"
```

## 3. Normative rules

- **M1.** `repository.type` MUST equal the `type` declared in `model.yaml` and MUST be `maturity-model` for this standard. Repositories of other classes MUST NOT declare maturity-model conformance.
- **M2.** `standard.id` MUST be `AM-MODEL-REPOSITORY-STANDARD`. `standard.version` MUST be a published SemVer version of the standard.
- **M3.** `standard.conformance` MUST be one of `registered`, `structural`, `full` (see the [conformance standard](conformance-standard.md)).
- **M4.** `model.id`, `model.name` and `model.version` MUST agree with the authoritative `model.yaml` manifest. The declaration restates identity **for cross-checking only**; `model.yaml` remains the authoritative source and the declaration is never edited independently of it.
- **M5.** The declaration MUST NOT restate the contract handshake, dependencies, compatibility or any other manifest content. It binds the repository to the repository standard, nothing else.
- **M6.** Version coherence is CI-enforced: `standard.yaml` model version, `model.yaml` version, `VERSION` file and the README status line MUST all agree.
- **M7.** A repository whose `standard.yaml` is missing is treated as not-declared; it is tracked as `registered` in the portfolio conformance registry and listed for adoption.

## 4. Why a separate file, not manifest fields

Extending `model.yaml` with standard fields would churn the CR-AM-11 §15 handshake schema (and its validators) for every adoption step. A separate declaration keeps the contract surface stable, lets adoption be incremental, and makes the declaration itself independently validatable. The intended long-term consolidation — adding repository-standard fields to the registration records in `assessment-registry` — is tracked as a reconciliation issue; until it lands, the [portfolio conformance registry](../registry/conformance.yaml) is the source of truth for standard adoption.
