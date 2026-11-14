# README Standard — Normative Specification

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0
**Authority:** [CR-AM-ORG-RES-000](../change-requests/CR-AM-ORG-RES-000.md)

## 1. Required information architecture

A fully conformant README contains these sections, in order. Sections requiring extensive explanation MAY link into `docs/`.

1. Model identity and introduction
2. Executive overview
3. Problem statement and rationale
4. Model purpose and objectives
5. Scope and applicability
6. Conceptual architecture
7. Assessment dimensions
8. Assessment criteria and structure
9. Maturity scale and level definitions
10. Assessment methodology
11. Evidence requirements
12. Scoring and interpretation
13. Practical usage guidance
14. Worked assessment example
15. Model architecture and data representation
16. Repository structure
17. Ecosystem positioning and dependencies
18. Provenance and references
19. Governance and versioning
20. Validation and conformance
21. Roadmap
22. Contribution guidance

## 2. Progressive conformance

The 22-section architecture is the `full` target. To protect repositories with strong existing but more compact READMEs, conformance is progressive:

| Conformance level | README requirement |
|---|---|
| `registered` | Identity, one-paragraph description, and a Status line whose version matches `model.yaml` and `VERSION` |
| `structural` | Status, placement (taxonomy + ecosystem), scoring scheme summary, layout, CI levels, provenance, licence, repository-standard declaration note — the existing federated README pattern ratifies this level |
| `full` | All 22 sections with the content requirements below |

## 3. Content requirements (`full`)

### 3.1 Executive overview
The README MUST explain: what the model is; what it assesss; why it exists; who should use it; what outcomes it supports; how it differs from related models.

### 3.2 Scope
The model MUST explicitly describe: what is included; what is excluded; the intended assessment subject; applicable organizational/operational contexts; relevant assumptions and limitations.

### 3.3 Assessment dimensions
Each dimension MUST document: identifier, name, definition, assessment intent, constituent criteria/capabilities, expected evidence, and relationships to other dimensions where applicable. The model MUST NOT assume dimensions are equally weighted or independent.

### 3.4 Maturity progression
Each maturity level MUST be explained with consistent aspects: identifier, name, definition, characteristics, observable behaviours, expected capabilities, evidence expectations, entry/exit conditions where applicable. The standard does not prescribe the number of levels or their names.

### 3.5 Assessment methodology
The model MUST explain: preparation, scope selection, criteria evaluation, evidence collection, scoring methodology, aggregation rules, maturity determination, confidence/completeness considerations where supported, interpretation, improvement planning. **The distinction between a numerical score and a maturity-level determination MUST be explicit.**

### 3.6 Worked examples
At least one valid example demonstrating how the model is interpreted and applied, consistent with the authoritative model definition and scoring rules.

## 4. Version coherence (all levels)

The README status line version MUST equal `model.yaml` `version` and the `VERSION` file. This cross-check is enforced by the reusable conformance workflow; drift is a conformance failure.
