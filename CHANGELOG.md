# Changelog — maturity-model-standard

Normative source for AM-MODEL-REPOSITORY-STANDARD. Versions follow the standard's own versioning policy (specifications/governance-standard.md §4).

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
