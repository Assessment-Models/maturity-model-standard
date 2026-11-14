# CR-AM-ORG-RES-000

**Organization-Wide Maturity Model Repository Standardization, Architecture and Global Conformance**

| Attribute | Value |
|---|---|
| Status | Accepted (organization resolution) |
| Governing organization | Assessment-Models |
| Change type | Foundational / Ecosystem architecture / Repository standardization |
| Scope | All repositories in Assessment-Models (policy) · all maturity-model repositories (implementation) |
| Standard authority | `Assessment-Models/maturity-model-standard` |
| Template authority | `Assessment-Models/maturity-model-template` |
| Reference implementation | `maturity-model-autonomous-operations` |
| Dependencies | CR-AM-11, CR-AM-01, canonical assessment metamodel (`technehub-labs/dea-metamodel`) |
| Implementation strategy | Additive, non-destructive, progressively adoptable |
| Series | ORG-RES (organization resolution) — first entry |

## 0. Numbering reconciliation

This initiative was drafted under the working label *CR-AM-12*. The `CR-AM-12` slot in the `technehub-labs/dea-metamodel` change-request series is already occupied by an unrelated change ("Cardinal Root, Cross-Model Relations and the Dotted Line"). This initiative is therefore formalized as **CR-AM-ORG-RES-000**, the first entry of a new Assessment-Models organization-resolution series. Its substantive content supersedes nothing that already exists; it **ratifies and extends** the CR-AM-11 machinery (model.yaml §15 contract handshake, three-level CI, assessment-registry identity spine, GOVERNANCE.md taxonomy) and adds the repository-standard governance layer on top.

## 1. Executive summary

This resolution establishes a standardized repository architecture, documentation framework, governance model and technical conformance approach for all maturity models maintained by the Assessment-Models organization, and a centrally governed, automatically propagated repository standard rather than a one-time change to a single repository.

The change introduces:

1. A normative standard (`AM-MODEL-REPOSITORY-STANDARD`) owned by `maturity-model-standard`.
2. A reusable repository template (`maturity-model-template`).
3. A standardized repository declaration (`standard.yaml`) cross-referenced to the authoritative `model.yaml`.
4. Shared schemas and validators, including automated version-coherence checks (manifest ↔ VERSION ↔ README).
5. Reusable conformance workflows callable by every repository.
6. A portfolio-wide conformance registry with repository classification.
7. An additive, controlled migration programme for existing repositories.
8. Organization ruleset-backed policy enforcement, kept deliberately separate from content propagation.

The Autonomous Operations Maturity Model serves as the first complete reference implementation; `maturity-model-digital-transformation` is nominated as the second, materially different implementation (AC-28).

## 2. Problem statement

Existing maturity-model repositories differ in documentation, directory organization, model representation, assessment guidance and validation practice. Consequences: users cannot consistently navigate models; technical consumers must interpret repository-specific structures; documentation drifts from authoritative machine-readable definitions (observed concretely: the Autonomous Operations README declared 1.0.0 while model.yaml declared 1.0.1); and quality cannot be compared consistently across the portfolio.

A GitHub organization can enforce policy (rulesets, required checks) but cannot restructure individual repositories. Therefore the right solution is a **centrally governed, automatically propagated repository standard**: policy enforcement is central; content changes are always repository-specific, reviewable pull requests.

## 3. Objectives and non-objectives

**Objectives (O1–O10).** Common repository architecture; normative README/documentation specification; standardized identity/metadata/level/scoring representation; machine-readable authority; common diagram framework (DGM-01..07); reproducible examples; provenance/licensing; reusable CI and conformance automation; model enrichment framework; non-destructive migration.

**Non-objectives.** Redesigning the canonical metamodel; redefining the canonical maturity scale; forcing identical dimensions, scales or scoring algorithms on all models; centralizing assessment execution; merging independently governed repositories; transferring domain-model ownership to the template; mandating AI features. Canonical metamodel changes remain subject to their own CRs in `technehub-labs/dea-metamodel`.

**Critical principle:** standardize the architecture, not the model's intellectual content.

## 4. Architectural principles

- **AP-01 Common structure, independent semantics** — standard structure; each model keeps its own dimensions, criteria, levels and scoring.
- **AP-02 Machine-readable authority** — `model.yaml` and `maturity/` definitions are authoritative; documentation is validated against them.
- **AP-03 Explicit model boundaries** — MaturityModel, AssessmentModel, AssessmentDimension, AssessmentCriterion, EvidenceRequirement, AssessmentExecution, AssessmentResult, MaturityLevel remain distinguishable.
- **AP-04 Explicit provenance** — origin, source material, adaptations, licensing.
- **AP-05 Reproducibility** — an independent consumer can reproduce the scoring calculations.
- **AP-06 Extensibility** — model-specific constructs without cross-repository churn.
- **AP-07 Independent governance** — every model stays independently versioned in its own repository.
- **AP-08 Progressive conformance** — incremental adoption with explicit conformance status (`registered` → `structural` → `full`).

## 5. Architectural decisions

| ID | Decision |
|---|---|
| ADR-AM-12-01 | Establish one standard maturity-model repository architecture. |
| ADR-AM-12-02 | Introduce a reusable repository template and documentation specification. |
| ADR-AM-12-03 | Preserve model-specific semantics, dimensions, scales and scoring rules. |
| ADR-AM-12-04 | Make machine-readable model definitions authoritative over explanatory documentation. |
| ADR-AM-12-05 | Establish common evidence, assessment-methodology and provenance conventions. |
| ADR-AM-12-06 | Implement reusable validation and conformance automation. |
| ADR-AM-12-07 | Use Autonomous Operations as the first complete reference implementation. |
| ADR-AM-12-08 | Establish progressive migration of existing repositories. |
| ADR-AM-12-09 | Separate maturity-model definition from assessment execution and result management. |
| ADR-AM-12-10 | Establish optional model enrichment without turning model repositories into assessment applications. |
| ADR-ORG-RES-000-01 | Establish `maturity-model-standard` as the normative standard authority, separate from the template repository. |
| ADR-ORG-RES-000-02 | Declare adoption via a root `standard.yaml` cross-referenced to `model.yaml` (a new file, so the CR-AM-11 §15 handshake schema is not churned). |
| ADR-ORG-RES-000-03 | Classify every repository before restructuring; only `maturity-model` repositories adopt this standard. |

## 6. Repository standard and template

The standard repository (`maturity-model-standard`) owns: specifications, schemas, validators, reusable workflows, the portfolio conformance registry, and migration method. The template repository (`maturity-model-template`) owns the executable scaffold for new repositories. The template is an *implementation* of the standard, never its authority.

### 6.1 Declaration (standard.yaml)

Every conformant repository declares at its root:

```yaml
repository:
  type: maturity-model
standard:
  id: AM-MODEL-REPOSITORY-STANDARD
  version: "1.0.0"
  conformance: structural
model:
  id: autonomous-operations
  name: Autonomous Operations Maturity Model
  version: "1.0.1"
```

Identity fields must equal `model.yaml` (authoritative manifest) and the `VERSION` file; CI checks coherence, including the README status line (AP-02).

### 6.2 Conformance levels

| Level | Meaning |
|---|---|
| `registered` | Identified in the registry; declaration present; identity coherent. |
| `structural` | Repository structure, metadata and documentation requirements met; conformance workflow wired. |
| `full` | Passes structural checks plus docs/diagrams/mappings and semantic validation (Level 2/3 green). |

### 6.3 Portfolio registry

`registry/conformance.yaml` records classification and adoption for every repository in the organization. The `assessment-registry` registration records remain the identity spine; reconciliation of the two registries is tracked in `assessment-registry#16`.

## 7. What cascades globally through GitHub

| Mechanism | Organization-wide | Purpose |
|---|---|---|
| Repository template | New repositories | Standard starting structure |
| Organization rulesets | Yes (plan-dependent) | Branch protection and contribution controls |
| Reusable GitHub Actions | Yes | Consistent CI and validation |
| Repository inventory automation | Yes, via registry | Discover and track repositories |
| Standard repository files | Via PRs | Declarations, README, documentation |
| Repository restructuring | Per-repository PRs only | Directories, model files, examples |

Policy enforcement (central) and content propagation (per-repo reviewable PRs) are kept separate by design.

## 8. Implementation phases

- **Phase 1 — Organization foundation (done):** publish `maturity-model-standard`, `maturity-model-template`, governance update in `.github`, reference adoption in `maturity-model-autonomous-operations`.
- **Phase 2 — Portfolio-wide discovery (next):** inventory and classify all repositories, produce the migration matrix (AC-19, AC-21). Classification already ratified in the registry; the phase deepens it with per-repo structure assessment.
- **Phase 3 — Global adoption:** controlled, repository-specific pull requests across applicable repositories (adoption issues filed).
- **Phase 4 — Continuous enforcement:** required conformance checks, standard-version tracking, drift detection, periodic portfolio reporting (AC-29).

Implementation sequence: `DEFINE → STANDARDIZE → TEMPLATE → VALIDATE → REFERENCE → ENRICH → INVENTORY → MIGRATE → REGISTER → GOVERN`.

## 9. Reconciliation with existing, more mature work

| Existing work | Status | Disposition |
|---|---|---|
| CR-AM-11 three-level CI (`assessment-ci`), §15 manifest handshake, assessment-registry identity spine | More mature than the plan's validation design | **Ratified and extended, not replaced.** The repository-standard conformance gate is an additive 4th CI level; existing workflows retained. |
| AO repository foundation (`model.yaml`, `VERSION`, `maturity/`, `examples/`, `scripts/`) | Already near-standard | Evolved via AO PR #1, not replaced. |
| `maturity-model-digital-transformation` full Level 1/2/3 CI pedigree | Exceeds the plan's minimums | Flagged as the second implementation candidate (AC-28); its validation approach is a reference, not overwritten. |
| GOVERNANCE.md legacy classification (CR-AM-01 D-1 frozen repos; legacy-named active assessment models) | Predates this CR | **Ratified** into the registry classifications; `dea-*` assessment models and frozen catalogs excluded from maturity-model standard treatment. |
| CR-AM-12 slot occupied in `technehub-labs/dea-metamodel` | Confirmed | Re-numbered to CR-AM-ORG-RES-000 (this document). |

## 10. Acceptance criteria

AC-01..AC-17 as defined in the CR body (normative standard published; template exists; README/docs specs published; manifest/schema conventions defined; Level 1/2 validation reusable; Level 3 operational; AO reference implementation complete; diagrams present; reproducible example; docs consistent with authoritative definition; provenance documented; repositories inventoried; per-repo migration plans; second repository adopts; semantics/lineage preserved; registry/release references resolve; docs validated against machine-readable model).

Organization-level additions:

| ID | Criterion | Status |
|---|---|---|
| AC-18 | Central normative standard repository exists | **Done** — `maturity-model-standard` |
| AC-19 | All applicable repositories discoverable through an organization-wide inventory | Registry v1 done; Phase 2 deepens per-repo assessment |
| AC-20 | Every applicable repository declares a standard version | In progress (AO done; issues filed) |
| AC-21 | Repository classifications established before migration | **Done** — `registry/conformance.yaml` |
| AC-22 | Portfolio-wide conformance registry operational | **Done** |
| AC-23 | Reusable workflows validate all applicable repositories | **Done** — reusable conformance workflow published |
| AC-24 | Standard updates generate repository-specific migration PRs | Method defined (`migrations/`); automation to be exercised at first standard update |
| AC-25 | Organization-wide conformance policies established | Governance updated in `.github` (PR #4); ruleset activation tracked under Phase 4 |
| AC-26 | Non-conformant repositories identifiable and tracked | **Done** — registry fields |
| AC-27 | Existing model semantics, history and downstream dependencies preserved | Enforced as migration invariant |
| AC-28 | Adoption demonstrated across two materially different models | AO (done, structural) + `maturity-model-digital-transformation` (nominated, issue #3) |
| AC-29 | Standard-version upgrades and documentation drift monitored continuously | Phase 4 issue to be filed |

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Over-standardization of domain models | Standardize architecture, not semantics (AP-01) |
| Documentation drift | Automated coherence checks (validator + workflow) |
| Breaking existing consumers | Additive migration, explicit mappings, immutable references preserved |
| Duplicate canonical constructs | Reuse versioned `dea-metamodel` contracts |
| Excessive complexity | Mandatory/recommended/optional classification |
| Registry duplication | Single identity spine; reconciliation issue `assessment-registry#16` |
| CI duplication | Reuse `assessment-ci` and standard's reusable workflows |

## 12. Decision

Adopted as an organization resolution of Assessment-Models. `AM-MODEL-REPOSITORY-STANDARD` v1.0.0 is published; the Autonomous Operations repository is the reference implementation; the next step is Phase 2 portfolio discovery, followed by controlled adoption PRs across the maturity-model portfolio, with `maturity-model-digital-transformation` as the second implementation proving reusability (AC-28).
