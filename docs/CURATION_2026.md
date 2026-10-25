# 2026 Curation Notes

> Initial review snapshot: 2026-07-22. Current registry update: 2026-10-25.
> Focused literature search cutoff: 2026-10-23. Citation snapshot: 2026-07-23.

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

The current catalog contains 194 records labelled with a 2026 peer-reviewed
venue: 189 have an official venue URL recorded in `publication.official_url`,
and five legacy records retain a venue claim while an official URL is still
needed. The current distribution is:

| Venue | Venue records | Official URL evidence |
|---|---:|---:|
| ACL 2026 Main | 30 | 27 |
| ACL 2026 Findings | 38 | 35 |
| ICLR 2026 | 62 | 62 |
| ICML 2026 | 63 | 63 |
| ICRA 2026 | 1 | 1 |
| **Total** | **194** | **189** |

The distinction matters: the 182-paper cohort describes the reproducible
conference review performed in July; the 194-paper total describes all current
venue-labelled records and must not be read as 194 records with direct official
venue evidence.

## October 2026 additions

On 2026-10-16, a focused review added 20 previously absent papers from
ICML 2023, ICLR/ICML/NeurIPS 2024, ICLR/ICML/ICRA/NeurIPS 2025, and
ICLR/ICRA 2026, bringing the curated catalog from 262 to 282 papers.
The batch adds three model-space learning methods, two environment-space
inference methods, twelve environment-space learning methods, and three
exploration evaluation or analysis papers. Existing records, the ten quick-start
selections, and the citation snapshot are preserved.

Titles, authors, and venue records were checked against official conference
pages or proceedings, with exact-title checks against both the curated registry
and the candidate registry. All twenty additions have structured official venue
evidence and a verification date in `data/papers.json`. For the two ICRA papers,
IEEE-deposited Crossref metadata confirms the exact titles, authors, conference
years, and canonical IEEE Xplore URLs:

- [ExploRLLM (ICRA 2025)](https://doi.org/10.1109/ICRA55743.2025.11127622)
- [LLM-TALE (ICRA 2026)](https://doi.org/10.1109/ICRA57385.2026.11695912)

The updated snapshot date records this addition batch; earlier records retain
their original evidence-verification dates and have not been globally rechecked.

On 2026-10-25, a focused follow-up added 17 papers, promoted four existing
candidates, and retained AGEE as pending after its publisher full text returned
HTTP 403. The catalog now has 299 papers and 16 background references. It
includes both September–October work and older omissions; arXiv records retain
preprint status unless separate official venue evidence is recorded.

All 29 template rationales in the previous evaluation category were rewritten
against primary-source abstracts. Three intervention papers were moved to
model-space learning, and benchmark/metric and capability-boundary subtopics
were corrected. There are still 216 legacy template rationales in other
categories; their exact text is tracked rather than described as reverified.
See the [October review report](REVIEW_2026-10.md) for per-paper sources,
classification decisions, evidence limits, and the remaining review queue.

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
