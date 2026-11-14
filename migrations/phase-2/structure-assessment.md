# Phase 2 — Portfolio structure assessment

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0 · CR-AM-ORG-RES-000 §8 (Phase 2) · AC-19, AC-21
**Assessment date:** 2026-11-14 · **Scope:** all 7 `maturity-model` repositories · **Method:** direct inspection of `main` (root, `maturity/`, `.github/workflows/`, `examples/`, `scripts/`, `model.yaml`, `VERSION`, README status line)

This is the per-repository structure assessment feeding the [migration matrix](migration-matrix.yaml). No repository was modified during assessment. Machine-readable companion: [`migration-matrix.yaml`](migration-matrix.yaml).

## Summary

| Repository | model.yaml | VERSION | README Status | §15 handshake | maturity/ | CI workflows | standard.yaml |
|---|---|---|---|---|---|---|---|
| autonomous-operations | 1.0.1 | 1.0.1 | 1.0.1 ✅ | ✅ | scale + model/ | L1, L2, RS | ✅ (structural) |
| digital-transformation | 1.0.0 | **absent** | **absent** | ✅ | scale + evaluation + components/ | L1, L2 | ❌ |
| digital-transformation-operationalized | 1.0.1 | 1.0.1 | **1.0.0 (drift)** | ✅ | scale + model/ | L1, L2 | ❌ |
| technology | 1.0.0 | 1.0.0 | 1.0.0 ✅ | ✅ | scale + model/ | L1, L2 | ❌ |
| operations | 1.0.0 | 1.0.0 | 1.0.0 ✅ | ✅ | scale + model/ | L1, L2 | ❌ |
| modernization | 1.0.0 | 1.0.0 | 1.0.0 ✅ | ✅ | scale + model/ | L1, L2 | ❌ |
| services-delivery | 1.0.0 | 1.0.0 | 1.0.0 ✅ | ✅ | scale + model/ | L1, L2 | ❌ |

**Common structural gaps (all 6 not-yet-adopted repos):** root `standard.yaml` declaration + `.github/workflows/repository-standard.yml` (reusable conformance gate). Everything else required at `structural` level already exists in 5 of 6.

**Defects found (version-coherence, the exact class the standard's validator targets):**

1. `maturity-model-digital-transformation-operationalized`: README Status declares `1.0.0` while `model.yaml` and `VERSION` declare `1.0.1` — same defect the reference implementation had before adoption. Fix in its adoption PR.
2. `maturity-model-digital-transformation`: no `VERSION` file and no README `## Status` section — no version anchor besides the manifest.

## Per-repository detail

### 1. maturity-model-autonomous-operations — reference implementation (done)
Adopted at `structural` via PR #1 (merged 2026-11-14): declaration, drift fix (1.0.0→1.0.1), reusable conformance gate. Identity fully coherent. **Full-level gaps (optional, backlog):** `docs/`, `docs/diagrams/`, `mappings/`, `docs/provenance.md`, `docs/assessment-methodology.md`.

### 2. maturity-model-digital-transformation — composite model, second implementation candidate (AC-28)
- Most mature CI pedigree in the portfolio: Level 1 (schema, vocabulary, reference integrity, version consistency, examples), Level 2 (reusable `assessment-ci`), Level 3 (registry resolution + `scripts/check_immutable_refs.py` immutable-reference guard).
- §15 handshake complete; four CR-AM-10 component imports from `maturity-components` with explicit kinds (import/extend/override); scoring anchored on the OpenDEA EA evaluation instance (`dea-evaluation-opendea-enterprise-architecture-v1` v1.0.0).
- **Structure differs from the template target (mapping decision M2, R1 — map, never rename):** the model definition lives in `maturity/evaluation.yaml` + `maturity/components/` (4 files), not `maturity/model/`.
- **Gaps vs structural:** `VERSION` file, README `## Status` section, `CONTRIBUTING.md`, `standard.yaml`, `repository-standard.yml`. The `maturity/model` path check cannot be satisfied without restructuring, so DT adopts at `registered` first; raising to `structural` requires the recorded-structure-mappings amendment (standard v1.0.1 proposal, filed as an issue).
- **Risk notes:** composite semantics and component kinds must be preserved verbatim; consumers may depend on current layout; Level 1 validator behaviour differs from the template's (established, more mature — preserve).

### 3. maturity-model-digital-transformation-operationalized
- Structure matches the target shape exactly (`maturity/scale.yaml` + `maturity/model/…yaml`, examples, scripts/local_validate.py, CONTRIBUTING, both CI workflows).
- **Defect:** README Status `1.0.0` vs manifest/VERSION `1.0.1` (drift fix required in adoption PR).
- **Legacy artifact (mapping decision M4):** a self-named root directory `maturity-model-digital-transformation-operationalized/` **duplicates the entire repository** (own `model.yaml`, `VERSION`, `maturity/`, workflows). Retained untouched per R1; flagged as a duplication risk (two copies of the manifest can diverge). Deduplication is a repository-owner decision, explicitly out of scope for the adoption PR.
- **Gaps vs structural:** `standard.yaml`, `repository-standard.yml`, drift fix. Can adopt directly at `structural`.

### 4–7. technology, operations, modernization, services-delivery (v2-beta ports)
Four sibling repositories with an identical, near-conformant shape: coherent 1.0.0 identity across manifest/VERSION/README, `maturity/scale.yaml` + `maturity/model/{domain}.yaml`, worked example, `scripts/local_validate.py`, both CI workflows, provenance and CI-levels sections in README.
- operations additionally imports the `operations-modernization` component (kind: import) from `maturity-components`.
- **Gaps vs structural:** `standard.yaml` + `repository-standard.yml` (all four); `CONTRIBUTING.md` (modernization, services-delivery only).
- All four can adopt directly at `structural`; `modernization` and `services-delivery` PRs add `CONTRIBUTING.md` additively (org-wide pointer, same as siblings).
- **Mapping decision M1:** these repos carry model-owned scales (L0..L4, canonical v2 bands dependency `dea-maturity-bands-v2` v1.0.0) — established CR-AM-11 v2-beta port work. The structural requirement is satisfied by `maturity/scale.yaml` existing; the template's canonical-scale-binding pattern applies to new repositories only. Model-owned scales are preserved verbatim (invariant).
- **Mapping decision M5 (full level):** README `Provenance`, `Scoring scheme` and `CI levels` sections already carry content the documentation standard expects under `docs/`. When pursuing `full`, add `docs/` files that link to these sections rather than duplicating them (prevents a second drift surface).

## Nominated Phase 3 order

| # | Repository | PR content | Target level |
|---|---|---|---|
| 1 | digital-transformation | `VERSION` + README Status (1.0.0 anchor), `CONTRIBUTING.md`, `standard.yaml` (registered), `repository-standard.yml` | registered |
| 2 | digital-transformation-operationalized | drift fix (Status → 1.0.1), `standard.yaml` (structural), `repository-standard.yml` | structural |
| 3 | technology | `standard.yaml` (structural), `repository-standard.yml` | structural |
| 4 | operations | `standard.yaml` (structural), `repository-standard.yml` | structural |
| 5 | modernization | + `CONTRIBUTING.md` | structural |
| 6 | services-delivery | + `CONTRIBUTING.md` | structural |

Rationale: digital-transformation first because AC-28 requires a second, materially different implementation and it exercises the standard's hardest case (composite model, mapped structure); operationalized second because its drift fix mirrors the reference implementation's defect class; the four siblings follow in low-risk, near-identical PRs.

## Constraints honoured

- No repository modified during discovery.
- Frozen/legacy repositories and assessment models remain excluded (registry classifications unchanged).
- Existing model semantics, component imports, scoring anchors and provenance preserved verbatim in every nominated PR.
