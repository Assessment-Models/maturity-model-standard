# Templates

The executable repository scaffold lives in **[Assessment-Models/maturity-model-template](https://github.com/Assessment-Models/maturity-model-template)**.

This `maturity-model-standard` repository is the *normative authority*; the template is an *implementation* of that authority. If they ever disagree, the specifications and schemas here win, and a template issue is filed.

Rules:

- New maturity-model repositories should be created from the template.
- Existing repositories adopt via migration PRs (see `migrations/`), never by overwriting from the template.
- The template's `standard.yaml` declares conformance level `registered` by default; adopting repositories raise the level deliberately as structure and validation are completed.
