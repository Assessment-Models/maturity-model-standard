#!/usr/bin/env python3
"""Portfolio conformance and adoption-projection report (CR-AR-07).

assessment-registry is authoritative for registered maturity-model adoption
snapshots. This report verifies that the standard repository's portfolio view
matches those snapshots, then checks each current source repository declaration
and its structural conformance. The standard repository remains normative for
the standard itself and retains classification and Phase 2 assessment data.
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
VALIDATOR = os.path.join(ROOT, "validators", "validate_standard_declaration.py")
ORG = "Assessment-Models"
ASSET_REGISTRY_URL = "https://github.com/Assessment-Models/assessment-registry.git"
STANDARD_ID = "AM-MODEL-REPOSITORY-STANDARD"


def read_published_standard_version():
    with open(os.path.join(ROOT, "VERSION"), encoding="utf-8") as handle:
        return handle.read().strip()


def run_validator(clone_dir):
    proc = subprocess.run(
        [sys.executable, VALIDATOR, "--root", clone_dir],
        capture_output=True, text=True,
    )
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()


def read_adoption_snapshots(registry_clone):
    records = {}
    base = os.path.join(registry_clone, "registry", "maturity-models")
    for filename in sorted(os.listdir(base)):
        if not filename.endswith(".yaml"):
            continue
        path = os.path.join(base, filename)
        with open(path, encoding="utf-8") as handle:
            record = yaml.safe_load(handle) or {}
        if record.get("type") != "maturity-model" or record.get("status") == "legacy":
            continue
        snapshot = record.get("repository_standard")
        if not isinstance(snapshot, dict):
            raise ValueError("%s: missing repository_standard adoption snapshot" % record.get("id", filename))
        repository = (record.get("source") or {}).get("repository")
        if not repository:
            raise ValueError("%s: missing source.repository" % record.get("id", filename))
        if repository in records:
            raise ValueError("duplicate adoption snapshot for repository %s" % repository)
        records[repository] = {
            "asset_id": record.get("id"),
            "release_version": str((record.get("release") or {}).get("version") or ""),
            "id": snapshot.get("id"),
            "version": str(snapshot.get("version") or ""),
            "conformance": snapshot.get("conformance"),
        }
    return records


def check_projection(entry, snapshot):
    errors = []
    if entry.get("standard_version") != snapshot["version"]:
        errors.append("portfolio standard_version=%r != assessment-registry=%r" %
                      (entry.get("standard_version"), snapshot["version"]))
    if entry.get("conformance") != snapshot["conformance"]:
        errors.append("portfolio conformance=%r != assessment-registry=%r" %
                      (entry.get("conformance"), snapshot["conformance"]))
    if snapshot["id"] != STANDARD_ID:
        errors.append("assessment-registry standard id=%r != %r" % (snapshot["id"], STANDARD_ID))
    return errors


def check_current_declaration(clone_dir, repository, snapshot):
    path = os.path.join(clone_dir, "standard.yaml")
    if not os.path.isfile(path):
        return ["%s: standard.yaml is missing" % repository], None
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    repo_type = (data.get("repository") or {}).get("type")
    standard = data.get("standard") or {}
    model = data.get("model") or {}
    declared = str(standard.get("version") or "")
    checks = [
        ("repository.type", repo_type, "maturity-model"),
        ("standard.id", standard.get("id"), snapshot["id"]),
        ("standard.version", declared, snapshot["version"]),
        ("standard.conformance", standard.get("conformance"), snapshot["conformance"]),
        ("model.id", model.get("id"), snapshot["asset_id"]),
        ("model.version", str(model.get("version") or ""), snapshot["release_version"]),
    ]
    errors = []
    for field, actual, expected in checks:
        if actual != expected:
            errors.append("%s: current standard.yaml %s=%r != registry snapshot %r" %
                          (repository, field, actual, expected))
    return errors, declared


def version_lag(declared, published):
    if not declared:
        return "missing"
    if declared == published:
        return "ok"

    def major_minor(value):
        parts = str(value).split(".")
        return tuple(parts[:2]) if len(parts) >= 2 else None

    return "behind-patch" if major_minor(declared) == major_minor(published) else "stale"


def main():
    published = read_published_standard_version()
    with open(REGISTRY_PATH, encoding="utf-8") as handle:
        portfolio = yaml.safe_load(handle) or {}

    targets = [
        entry for entry in portfolio.get("repositories", [])
        if entry.get("classification") == "maturity-model"
        and entry.get("standard_version")
    ]

    rows = []
    failures = []
    workdir = tempfile.mkdtemp(prefix="portfolio-")
    try:
        registry_clone = os.path.join(workdir, "assessment-registry")
        clone = subprocess.run(
            ["git", "clone", "--depth", "1", ASSET_REGISTRY_URL, registry_clone],
            capture_output=True, text=True,
        )
        if clone.returncode != 0:
            print("FAIL — could not clone authoritative assessment-registry: " + clone.stderr.strip())
            return 1
        snapshots = read_adoption_snapshots(registry_clone)

        target_names = {entry["repository"] for entry in targets}
        missing = sorted(target_names - set(snapshots))
        unprojected = sorted(set(snapshots) - target_names)
        if missing:
            failures.append("portfolio maturity-model entries missing adoption snapshots: " + ", ".join(missing))
        if unprojected:
            failures.append("registered adoption snapshots lack maturity-model portfolio classification: " + ", ".join(unprojected))

        for entry in targets:
            repo = entry["repository"]
            snapshot = snapshots.get(repo)
            if snapshot is None:
                rows.append((repo, entry.get("conformance"), "?", "FAIL — no registry snapshot"))
                continue

            projection_errors = check_projection(entry, snapshot)
            if projection_errors:
                failures.extend(projection_errors)

            clone_dir = os.path.join(workdir, repo)
            result = subprocess.run(
                ["git", "clone", "--depth", "1",
                 "https://github.com/%s/%s.git" % (ORG, repo), clone_dir],
                capture_output=True, text=True,
            )
            if result.returncode != 0:
                failures.append("%s: clone failed: %s" % (repo, result.stderr.strip()))
                rows.append((repo, snapshot["conformance"], snapshot["version"], "clone-failed"))
                continue

            declaration_errors, declared = check_current_declaration(clone_dir, repo, snapshot)
            failures.extend(declaration_errors)
            ok, detail = run_validator(clone_dir)
            if not ok:
                failures.append("%s: %s" % (repo, detail))

            lag = version_lag(snapshot["version"], published)
            status = "ok" if ok and not declaration_errors and not projection_errors else "FAIL"
            if lag == "stale":
                status = "FAIL"
                failures.append(
                    "%s: adoption snapshot v%s but published standard is v%s "
                    "(major/minor lag; compatible upgrade required)" %
                    (repo, snapshot["version"], published))
            elif lag == "behind-patch" and status == "ok":
                status = "ok (patch behind)"
            rows.append((repo, snapshot["conformance"], snapshot["version"], status))

    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    lines = [
        "# Portfolio conformance report",
        "",
        "Standard: %s v%s · %d maturity-model repositories" %
        (STANDARD_ID, published, len(rows)),
        "",
        "Adoption snapshots: assessment-registry (authoritative); this registry's "
        "adoption fields are a checked projection.",
        "",
        "| Repository | Conformance | Adoption version | Status |",
        "|---|---|---|---|",
    ]
    for repo, level, version, status in rows:
        lines.append("| %s | `%s` | %s | %s |" % (repo, level, version, status))
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
