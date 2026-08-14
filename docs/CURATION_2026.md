# 2026 Curation Notes

> Initial review snapshot: 2026-07-22. Current registry snapshot: 2026-08-06.

## Sources

The 2026 review started from the complete accepted-paper pages for:

- [ACL 2026 Main](https://aclanthology.org/volumes/2026.acl-long/)
- [ACL 2026 Findings](https://aclanthology.org/volumes/2026.findings-acl/)
- [ICLR 2026](https://iclr.cc/virtual/2026/papers.html)
- [ICML 2026](https://icml.cc/virtual/2026/papers.html)

The initial review cohort used official accepted-paper pages. Later additions and
legacy records retain their own provenance in `data/papers.json` under the
structured `publication` object.

## Selection result

The high-recall discovery pass produced 413 candidates. Manual scope review
retained the following 182-paper conference-review cohort:

| Venue | Retained |
|---|---:|
| ACL 2026 Main | 26 |
| ACL 2026 Findings | 35 |
| ICLR 2026 | 58 |
| ICML 2026 | 63 |

Of these, 55 were exact-title matches to the former repository and four were
fuzzy matches. The remaining 123 are newly added conference papers.

The 231 rejected candidates were primarily generic policy-optimization or
efficiency papers, generic self-improvement/self-play work, generic agent or
test-time-scaling papers, and papers where “exploration” described an application
rather than a model mechanism.

## Current registry view

The current catalog contains 188 records labelled with a 2026 peer-reviewed
venue: 183 have an official venue URL recorded in `publication.official_url`,
and five legacy records retain a venue claim while an official URL is still
needed. The current distribution is:

| Venue | Venue records | Official URL evidence |
|---|---:|---:|
| ACL 2026 Main | 29 | 26 |
| ACL 2026 Findings | 38 | 35 |
| ICLR 2026 | 58 | 58 |
| ICML 2026 | 63 | 63 |
| **Total** | **188** | **183** |

The distinction matters: the 182-paper cohort describes the reproducible
conference review performed in July; the 188-paper total describes all current
venue-labelled records and must not be read as 188 records with direct official
venue evidence.

## Legacy migration

The former detailed catalog contained 193 entries with arXiv links. Exact arXiv
metadata checks found 158 credible title matches and at least 32 clear link-title
mismatches. After scope review and deduplication against the official 2026
records, 58 additional verified legacy papers were retained.

The catalog also adds pre-2025 LLM/agent foundations and keeps classical
non-LLM RL references in a background-only appendix.

The catalog's seven mixed-axis sections were subsequently consolidated into
five primary research categories: LLM generation and inference; RLVR, policy,
and curriculum; agentic inference; agentic exploration for training; and
understanding and evaluation. Separating agentic inference from agentic
training distinguishes test-time environment search from interaction that
generates experience or updates a policy. Data, memory, population, and
self-improvement remain orthogonal subtopics and tags.

## Invariants

- A paper appears once and has one primary area.
- Multi-dimensional tags describe phase, level, signal, mechanism, problem, and
  setting.
- Official venue evidence is stored separately from venue claims. A record is
  counted as directly verified only when `publication.official_url` passes the
  venue-specific HTTPS host and path validation rule.
- Classical RL papers do not count toward catalog totals.
- Automated discovery cannot write directly to the accepted registry.
