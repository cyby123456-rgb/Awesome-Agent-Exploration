#!/usr/bin/env python3
"""Compatibility audit: validate data and prove generated-view parity."""

from __future__ import annotations

from pathlib import Path
import json

import validate_catalog
from generate_catalog import (
    load_catalog,
    render_detailed,
    render_readme,
    render_research_map,
)


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data" / "candidates.json"
PAPERS = ROOT / "data" / "papers.json"
CANDIDATE_STATUSES = {"pending", "promoted", "rejected", "duplicate"}
SCHEMA_VERSION = 2


def validate_candidates() -> list[str]:
    """Keep unverified records separate and reviewable."""
    payload = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    catalog = json.loads(PAPERS.read_text(encoding="utf-8"))
    paper_ids = {paper["id"] for paper in catalog.get("papers", [])}
    errors: list[str] = []
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"candidate registry: schema_version must be {SCHEMA_VERSION}")
    if not isinstance(payload.get("candidates"), list):
        return [*errors, "candidate registry: candidates must be a list"]
    seen: set[str] = set()
    for index, candidate in enumerate(payload["candidates"]):
        label = candidate.get("title", f"candidate #{index}")
        for field in ("id", "status", "title", "reason"):
            if not candidate.get(field):
                errors.append(f"{label}: missing {field}")
        status = candidate.get("status")
        if status not in CANDIDATE_STATUSES:
            errors.append(f"{label}: invalid status {status!r}")
        resolved_to = candidate.get("resolved_to")
        if status == "pending":
            if not candidate.get("next_step"):
                errors.append(f"{label}: pending candidates need next_step")
        elif status == "promoted":
            if not resolved_to:
                errors.append(f"{label}: promoted candidates need resolved_to")
            elif resolved_to not in paper_ids:
                errors.append(f"{label}: promoted resolved_to is not a catalog paper ID")
            if not candidate.get("resolved_at"):
                errors.append(f"{label}: promoted candidates need resolved_at")
            if candidate.get("next_step"):
                errors.append(f"{label}: promoted candidates cannot retain next_step")
        elif status == "duplicate":
            if not candidate.get("duplicate_of"):
                errors.append(f"{label}: duplicate candidates need duplicate_of")
        elif status == "rejected":
            for field in ("decision_reason", "resolved_at"):
                if not candidate.get(field):
                    errors.append(f"{label}: rejected candidates need {field}")
        if status != "promoted" and resolved_to:
            errors.append(f"{label}: only promoted candidates may set resolved_to")
        if candidate.get("id") in seen:
            errors.append(f"duplicate candidate id: {candidate.get('id')}")
        seen.add(candidate.get("id"))
    return errors


def main() -> int:
    status = validate_catalog.main()
    if status:
        return status

    candidate_errors = validate_candidates()
    if candidate_errors:
        print("Candidate registry failures:")
        for error in candidate_errors:
            print(f"- {error}")
        return 1

    catalog = load_catalog()
    expected = {
        "README.md": render_readme(catalog),
        "README_DETAILED.md": render_detailed(catalog),
        "assets/research-map.svg": render_research_map(catalog),
    }
    drift = []
    for name, generated in expected.items():
        actual = (ROOT / name).read_text(encoding="utf-8")
        if actual != generated:
            drift.append(name)

    if drift:
        print("Generated view drift detected:", ", ".join(drift))
        print("Run: python3 scripts/generate_catalog.py")
        return 1

    print("Generated views match data/papers.json; candidate registry is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
