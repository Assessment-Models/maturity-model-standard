#!/usr/bin/env python3
"""Portfolio conformance report — CR-AM-ORG-RES-000 Phase 4 (AC-26, AC-29).

Continuous drift detection for the Assessment-Models maturity-model portfolio:

1. Reads the portfolio conformance registry (registry/conformance.yaml).
2. For every repository classified `maturity-model` with a declared adoption
   (standard_version not null), shallow-clones its default branch.
3. Runs the standard's declaration validator against the clone
   (identity coherence: standard.yaml / model.yaml / VERSION / README).
4. Compares each repository's declared standard version against this
   repository's published VERSION (staleness tracking, AC-29).
5. Writes a Markdown portfolio report (stdout and $GITHUB_STEP_SUMMARY) and
   exits non-zero on any drift or stale declaration.

Policy enforcement stays central (this scheduled check); content propagation
stays per-repository (reviewable PRs). This script never modifies repositories.
"""
import os
import shutil
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REGISTRY_PATH = os.path.join(ROOT, "registry", "conformance.yaml")
VALIDATOR = os.path.join(HERE, "validate_standard_declaration.py")
ORG = "Assessment-Models"


def read_published_standard_version():
    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as handle:
        return handle.read().strip()


def run_validator(clone_dir):
    proc = subprocess.run(
        [sys.executable, VALIDATOR, "--root", clone_dir],
        capture_output=True, text=True,
    )
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()


def declared_standard_version(clone_dir):
    path = os.path.join(clone_dir, "standard.yaml")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return str(((data.get("standard") or {}).get("version")) or "")


def main():
    published = read_published_standard_version()
    with open(REGISTRY_PATH, encoding="utf-8") as handle:
        registry = yaml.safe_load(handle) or {}

    targets = [
        entry for entry in registry.get("repositories", [])
        if entry.get("classification") == "maturity-model"
        and entry.get("standard_version")
    ]

    rows = []
    failures = []
    workdir = tempfile.mkdtemp(prefix="portfolio-")
    try:
        for entry in targets:
            repo = entry["repository"]
            clone_dir = os.path.join(workdir, repo)
            clone = subprocess.run(
                ["git", "clone", "--depth", "1",
                 "https://github.com/%s/%s.git" % (ORG, repo), clone_dir],
                capture_output=True, text=True,
            )
            if clone.returncode != 0:
                failures.append("%s: clone failed: %s" % (repo, clone.stderr.strip()))
                rows.append((repo, entry.get("conformance"), "?", "clone-failed"))
                continue
            ok, detail = run_validator(clone_dir)
            declared = declared_standard_version(clone_dir)
            stale = bool(declared) and declared != published
            status = "ok" if (ok and not stale) else "FAIL"
            if not ok:
                failures.append("%s: %s" % (repo, detail))
            if stale:
                failures.append(
                    "%s: declares standard v%s but the published standard is v%s"
                    % (repo, declared, published))
            rows.append((repo, entry.get("conformance"), declared or "?", status))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    lines = [
        "# Portfolio conformance report",
        "",
        "Standard: AM-MODEL-REPOSITORY-STANDARD v%s · %d conformant repositories" % (published, len(rows)),
        "",
        "| Repository | Declared level | Standard version | Status |",
        "|---|---|---|---|",
    ]
    for repo, level, declared, status in rows:
        lines.append("| %s | `%s` | %s | %s |" % (repo, level, declared, status))
    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    if failures:
        print("\n## Failures")
        for item in failures:
            print("- " + item)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
