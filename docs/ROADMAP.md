# Awesome Exploration: Curation Roadmap

> Current-state snapshot: 2026-08-03.

## Current position

Awesome Exploration is a curated map of exploration in language-model
generation, learning and post-training, interactive agents, and evaluation. It
is intentionally narrower than general RL, RLHF, reasoning, test-time-scaling,
or agent lists.

The repository now uses one structured source of truth:

- `data/papers.json` stores accepted records and multi-dimensional tags.
- `README.md` is the compact generated catalog.
- `README_DETAILED.md` is the generated metadata view.
- `scripts/validate_catalog.py` enforces schema, identity, tag, and official
  conference-link invariants.
- `scripts/generate_catalog.py` regenerates both public views.
- `scripts/check_links.py` performs an optional network link check.
- `.github/workflows/catalog.yml` checks validation and generated-file parity
  for pull requests and updates to `main`.

The earlier duplicate catalog, title caches, and first-match link-fetching
script have been removed. They remain available in Git history.

## Taxonomy

Each paper has exactly one primary category:

1. Exploration for LLM Generation & Inference
2. Exploration for RLVR, Policy & Curriculum
3. Agentic Exploration
4. Agentic Exploration for Training
5. Understanding, Evaluation & Benchmarks

Orthogonal tags describe phase, intervention level, exploration signal,
mechanism, target problem, and application setting. Data, memory, population,
and self-improvement remain subtopics or tags rather than primary categories.
Classical non-LLM RL is limited to a background appendix and is not counted in
catalog totals.

## Acceptance rule

A paper belongs only when exploration is a primary contribution or object of
analysis. It must identify where exploration occurs and supply a concrete signal
or mechanism. An occurrence of terms such as RL, agent, entropy, search,
sampling, diversity, or self-improvement is not sufficient.

Automated discovery may prepare candidates, but promotion to `data/papers.json`
requires exact-title source verification and human review.

## Done

1. Established a candidate registry with review states and promotion links.
2. Added CI for validation and generated-file parity.
3. Consolidated the catalog into structured source data and generated views.

## Next

1. Enrich records with code URLs and canonical publication identifiers.
2. Add link checking as a scheduled or manually triggered CI job.
3. Add a filterable static view once the JSON schema has remained stable.
4. Publish a small monthly changelog of reviewed additions and removals.

## Release checklist

```bash
python3 scripts/validate_catalog.py
python3 scripts/generate_catalog.py
python3 scripts/check_links.py
git diff --check
```

Generated Markdown should be committed together with every registry change.
