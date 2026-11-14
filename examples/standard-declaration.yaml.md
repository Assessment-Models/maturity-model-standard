# Standard declaration — annotated example

Every conformant repository places `standard.yaml` at its root. The declaration is a **cross-reference, not a second identity source**: `model.yaml` (CR-AM-11 §15 handshake) remains authoritative for identity; CI checks that the two agree.

```yaml
repository:
  type: maturity-model        # must equal model.yaml type; other classes must NOT adopt this standard
standard:
  id: AM-MODEL-REPOSITORY-STANDARD
  version: "1.0.0"            # published SemVer version of the standard being adopted
  conformance: structural     # registered | structural | full
model:
  id: autonomous-operations   # must equal model.yaml id
  name: Autonomous Operations Maturity Model
  version: "1.0.1"            # must equal model.yaml version AND the VERSION file
```

The declaration above is the reference implementation's actual state.

## Coherence rules (machine-checked)

1. `repository.type` = `model.yaml` type = `maturity-model`.
2. `model.id` = `model.yaml` id.
3. `model.version` = `model.yaml` version = `VERSION` file = version shown in the README `## Status` line.
4. `standard.id` = `AM-MODEL-REPOSITORY-STANDARD`.
5. `standard.version` is a published SemVer version of the standard (see the standard repository's `VERSION`).
6. `standard.conformance` ∈ {`registered`, `structural`, `full`}; higher levels require more structure (see the repository standard specification).

## Validation

Locally:

```bash
python validators/validate_standard_declaration.py --root .
```

In CI (from the repository):

```yaml
jobs:
  repository-standard:
    uses: Assessment-Models/maturity-model-standard/.github/workflows/repository-conformance.yml@main
```

The validator exits non-zero on any drift (for example, a README status line that lags the manifest, as happened with 1.0.0 vs 1.0.1 in the reference repository before adoption).
