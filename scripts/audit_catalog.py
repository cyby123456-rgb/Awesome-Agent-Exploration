#!/usr/bin/env python3
"""Compatibility audit: validate data and prove generated-view parity."""

from __future__ import annotations

from pathlib import Path

import validate_catalog
from generate_catalog import load_catalog, render_detailed, render_readme


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    status = validate_catalog.main()
    if status:
        return status

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

    print("Generated views match data/papers.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
