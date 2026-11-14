# Migration and Propagation Method

**Standard:** AM-MODEL-REPOSITORY-STANDARD v1.0.0 · CR-AM-ORG-RES-000

## 1. Migration pipeline

```text
DISCOVER → ASSESS → MAP → STANDARDIZE → VALIDATE → REGISTER → RELEASE
```

1. **DISCOVER** — inventory every repository in the organization (the [portfolio conformance registry](../registry/conformance.yaml) is the living inventory).
2. **ASSESS** — classify each repository and assess its current structure against the standard. No repository is modified before its existing model semantics and dependencies have been assessed.
3. **MAP** — where established structure differs from the target, record an explicit structure mapping instead of renaming (repository-standard.md §3, rule R1).
4. **STANDARDIZE** — apply changes additively: `standard.yaml` declaration, version-coherence fixes, missing standard files, documentation, diagrams. Generated as repository-specific pull requests.
5. **VALIDATE** — CI validates each pull request (Level 1/2/3 plus the repository-standard conformance gate).
6. **REGISTER** — merged adoptions update the repository's declared standard version and the portfolio conformance registry.
7. **RELEASE** — each repository releases on its own independent lifecycle.

## 2. Non-negotiable invariants

- Preserve existing model definitions, identifiers, version history, provenance and lineage.
- Preserve valid scoring semantics and all canonical scale dependencies.
- Maintain compatibility with existing consumers and immutable registry references.
- Never restructure a repository merely because its directory structure differs; map instead.
- A repository is never declared conformant merely because its structure matches the template.

## 3. Standard-update cascade

When a new standard version is approved (ORG-RES series), the cascade follows the [governance standard](../specifications/governance-standard.md) §3: publish → identify affected repositories → prepare repository-specific changes → generate reviewable pull requests → validate → merge → record. Content propagation is always attributable; it is never a blanket automated rewrite.

## 4. What automation may and may not do

| Mechanism | Organization-wide | Notes |
|---|---|---|
| Repository template (`maturity-model-template`) | New repositories | Standard starting structure |
| Organization rulesets | Yes, subject to plan | Branch/tag policies |
| Reusable workflows | Yes | Consistent CI and validation (this repository + `assessment-ci`) |
| Repository inventory automation | Yes, via registry | Discovery and tracking |
| Standard repository files | Via PRs | README, declaration, documentation |
| Repository restructuring | Per-repository PRs | Directories, model files, examples |

## 5. Suggested pull-request template for adoption PRs

```text
Adopt AM-MODEL-REPOSITORY-STANDARD v1.0.0 (CR-AM-ORG-RES-000)

- [ ] Adds root standard.yaml declaration at conformance level <registered|structural|full>
- [ ] Cross-checks model.yaml ↔ VERSION ↔ README status line (no drift)
- [ ] Adds .github/workflows/repository-standard.yml (reusable conformance gate)
- [ ] No renames, no deletions, no model-semantics changes
- [ ] Portfolio conformance registry updated in Assessment-Models/maturity-model-standard
```
