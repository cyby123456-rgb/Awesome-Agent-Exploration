#!/usr/bin/env python3
"""Compatibility audit: validate data and prove generated-view parity."""

from __future__ import annotations

from pathlib import Path
import json

import validate_catalog
from generate_catalog import load_catalog, render_detailed, render_readme


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data" / "candidates.json"


def validate_candidates() -> list[str]:
    """Keep unverified records separate and reviewable."""
    payload = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    errors: list[str] = []
    seen: set[str] = set()
    for index, candidate in enumerate(payload.get("candidates", [])):
        label = candidate.get("title", f"candidate #{index}")
        for field in ("id", "status", "title", "reason", "next_step"):
            if not candidate.get(field):
                errors.append(f"{label}: missing {field}")
        if candidate.get("status") != "pending":
            errors.append(f"{label}: unexpected status {candidate.get('status')!r}")
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
