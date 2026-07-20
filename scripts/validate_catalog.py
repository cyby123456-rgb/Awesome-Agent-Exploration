#!/usr/bin/env python3
"""Validate the canonical public paper catalog."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
ARXIV = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")


def normalise(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def main() -> int:
    papers = json.loads(DATA.read_text(encoding="utf-8"))["papers"]
    errors: list[str] = []
    title_counts = Counter(normalise(p["title"]) for p in papers)
    duplicates = [key for key, count in title_counts.items() if count > 1]
    if duplicates:
        errors.append(f"duplicate titles: {len(duplicates)}")
    missing_ids = [p["title"] for p in papers if not p.get("arxiv")]
    if missing_ids:
        errors.append(f"entries without a primary-source link: {', '.join(missing_ids)}")
    ids = [p["arxiv"] for p in papers if p.get("arxiv")]
    id_counts = Counter(ids)
    duplicate_ids = [key for key, count in id_counts.items() if count > 1]
    if duplicate_ids:
        errors.append(f"duplicate arXiv IDs: {', '.join(sorted(duplicate_ids))}")
    malformed = [key for key in ids if not ARXIV.fullmatch(key)]
    if malformed:
        errors.append(f"malformed arXiv IDs: {', '.join(sorted(malformed))}")
    invalid_scopes = [p["title"] for p in papers if p.get("scope") not in {"Core", "Adjacent", "Context"}]
    if invalid_scopes:
        errors.append(f"invalid scope labels: {', '.join(invalid_scopes)}")
    if errors:
        print("Catalog validation failed:", *errors, sep="\n- ", file=sys.stderr)
        return 1
    print(f"Catalog validation passed: {len(papers)} unique entries, {len(ids)} primary-source links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
