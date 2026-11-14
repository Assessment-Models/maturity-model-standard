# Changelog — maturity-model-standard

Normative source for AM-MODEL-REPOSITORY-STANDARD. Versions follow the standard's own versioning policy (specifications/governance-standard.md §4).

## 1.0.1 — 2026-11-14

Patch release (additive, backward-compatible). Established by amendment [issue #3](https://github.com/Assessment-Models/maturity-model-standard/issues/3), from the Phase 2 discovery finding M2: `maturity-model-digital-transformation` — the AC-28 second implementation — keeps its composite model definition in `maturity/evaluation.yaml` + `maturity/components/`, which v1.0.0's structural path check could only satisfy by restructuring (forbidden by rule R1).

### Added

- Optional `structure.mappings` block in the `standard.yaml` declaration: a role with established alternative paths (v1 role: `model-definition`) satisfies the structural path check when the mapping is recorded, with the mapping integrity-checked (mapped paths must exist) and logged.
- Schema support: `structure` in [`schemas/standard-declaration.schema.json`](schemas/standard-declaration.schema.json).
- Validator support (v1.0.1) in `validators/validate_standard_declaration.py` and the inline copy in the reusable workflow `.github/workflows/repository-conformance.yml` (kept in sync).
- Specification sections: repository standard §6 (structure mappings), metadata standard rule M8.
- Fixtures: `fixtures/mapped-structure` (positive control — structural via recorded mapping) and `fixtures/negative-bad-mapping` (negative control — mapping to a missing path must fail); self-test extended.

### Changed

- Portfolio drift report (`scripts/portfolio_conformance_report.py`): declaring a published **patch** version older than the current standard is informational ("behind", compatible-patch adoption policy), not a failure; a major/minor lag remains a failure.

### Notes

- This release is the first standard-update cascade, exercising AC-24 end-to-end: publish → identify affected repositories (`maturity-model-digital-transformation`) → repository-specific elevation pull request → validate → record.

## 1.0.0 — 2026-11-14

Initial publication under **CR-AM-ORG-RES-000** (Assessment-Models organization resolution; drafted under the working label CR-AM-12 and re-numbered because the CR-AM-12 slot is occupied in `technehub-labs/dea-metamodel`).

### Added

- Normative specifications: repository standard, README standard, documentation standard, metadata standard, governance standard, conformance standard.
- `standard.yaml` declaration format + `schemas/standard-declaration.schema.json`.
- `validators/validate_standard_declaration.py` (declaration, identity coherence: standard.yaml ↔ model.yaml ↔ VERSION ↔ README status, structure by conformance level).
- Reusable workflow `.github/workflows/repository-conformance.yml` for all conformant repositories.
- Self-test workflow with positive and negative fixtures (`fixtures/positive`, `fixtures/negative-version-drift`).
- Portfolio conformance registry `registry/conformance.yaml` covering all 19 organization repositories with classifications.
- Migration and propagation method (`migrations/`).
- Formalized resolution `change-requests/CR-AM-ORG-RES-000.md`.

### Ratified (pre-existing, more mature work extended rather than replaced)

- CR-AM-11 three-level CI, model.yaml §15 contract handshake, assessment-registry identity spine, GOVERNANCE.md taxonomy and legacy classification.
- Reference implementation adoption: `maturity-model-autonomous-operations` PR #1 (structural level; 1.0.0→1.0.1 README drift fixed).
