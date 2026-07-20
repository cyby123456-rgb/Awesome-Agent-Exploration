# Contributing papers

Please submit additions through an issue or pull request. Every public entry
needs:

1. the exact paper title;
2. a primary source (normally an arXiv identifier);
3. a section and one relevance label: `Core`, `Adjacent`, or `Context`;
4. one sentence explaining its relationship to exploration in RL for LLMs.

Edit `data/papers.json`, then run:

```bash
python scripts/build_catalog.py
python scripts/validate_catalog.py
```

Do not edit either README directly: both are generated from the catalog.
Records lacking a verified primary source belong in `data/needs-verification.json`.
