# Documentation Standard — Normative Specification

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)

## 1. Machine-readable authority

Documentation MUST be consistent with the authoritative machine-readable model definition (`model.yaml`, `maturity/`). Where a section can be generated from or validated against the model definition, it SHOULD be. Documentation drift is a conformance failure.

## 2. Required diagrams (`full` conformance)

| Id | Diagram | Purpose |
|---|---|---|
| DGM-01 | Model positioning | The model's location in the Assessment-Models ecosystem and relationship to downstream consumers |
| DGM-02 | Conceptual architecture | The major concepts and relationships constituting the model |
| DGM-03 | Assessment architecture | Relationship between dimensions, criteria, evidence, scores and maturity determination |
| DGM-04 | Maturity progression | The model's maturity levels and progression semantics |

## 3. Recommended diagrams

| Id | Diagram | Purpose |
|---|---|---|
| DGM-05 | Assessment lifecycle | Preparation → evaluation → evidence → scoring → determination → improvement |
| DGM-06 | Repository architecture | The repository's files, directories and their relationships |
| DGM-07 | Model lineage | Source frameworks, adaptations, dependencies and version history |

## 4. Visualization conventions

- Use Mermaid for diagrams maintainable as source; use SVG/PNG only where Mermaid is insufficient.
- Keep diagrams readable in GitHub-rendered Markdown.
- Use terminology consistent with the machine-readable model.
- Do not duplicate normative definitions in diagram labels.
- Include diagram purpose and explanatory text.
- Diagrams MUST be validated against actual model semantics.

## 5. Documentation set (`full` conformance)

`docs/` contains, at minimum: `overview.md`, `architecture.md`, `assessment-methodology.md`, `maturity-levels.md`, `dimensions.md`, `evidence-framework.md`, `provenance.md`, `governance.md`, `use-cases.md`, `diagrams/`. Each document must be consistent with the authoritative model definition and must not redefine canonical constructs owned by the metamodel.
