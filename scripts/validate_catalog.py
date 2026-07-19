#!/usr/bin/env python3
"""Fail when the public paper catalog contains duplicate titles or arXiv IDs."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
TITLE = re.compile(r"^- \*\*(.+?)\*\*", re.MULTILINE)
ARXIV = re.compile(r"arxiv\.org/abs/([^\])\s]+)")


def duplicates(values: list[str]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for value in values:
        counts[value] += 1
    return {value: count for value, count in counts.items() if count > 1}


def main() -> int:
    text = README.read_text(encoding="utf-8")
    title_dupes = duplicates(TITLE.findall(text))

    arxiv_to_titles: dict[str, set[str]] = defaultdict(set)
    for block in re.split(r"(?=^- \*\*)", text, flags=re.MULTILINE):
        match = TITLE.match(block)
        if match:
            for arxiv_id in ARXIV.findall(block):
                arxiv_to_titles[arxiv_id].add(match.group(1))
    id_conflicts = {key: value for key, value in arxiv_to_titles.items() if len(value) > 1}

    if title_dupes or id_conflicts:
        if title_dupes:
            print("Duplicate titles:", file=sys.stderr)
            for title, count in sorted(title_dupes.items()):
                print(f"  {count}x {title}", file=sys.stderr)
        if id_conflicts:
            print("arXiv IDs assigned to multiple titles:", file=sys.stderr)
            for arxiv_id, titles in sorted(id_conflicts.items()):
                print(f"  {arxiv_id}: {', '.join(sorted(titles))}", file=sys.stderr)
        return 1

    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
