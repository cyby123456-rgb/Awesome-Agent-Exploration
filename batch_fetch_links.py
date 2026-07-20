#!/usr/bin/env python3
"""Deprecated: edit data/papers.json, then run scripts/build_catalog.py.

Automatic title matching can silently attach the wrong paper to a catalog
entry. This repository intentionally requires a reviewed primary-source ID.
"""

from __future__ import annotations

import sys


if __name__ == "__main__":
    print(
        "This tool no longer modifies README files. Add a verified source to "
        "data/papers.json and run: python scripts/build_catalog.py",
        file=sys.stderr,
    )
    raise SystemExit(2)
