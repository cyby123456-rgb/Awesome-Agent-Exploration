# 2026 Curation Notes

> Review snapshot: 2026-07-22.

## Sources

The 2026 review started from the complete accepted-paper pages for:

- [ACL 2026 Main](https://aclanthology.org/volumes/2026.acl-long/)
- [ACL 2026 Findings](https://aclanthology.org/volumes/2026.findings-acl/)
- [ICLR 2026](https://iclr.cc/virtual/2026/papers.html)
- [ICML 2026](https://icml.cc/virtual/2026/papers.html)
- [Tianjin University Deep Reinforcement Learning Lab publications](http://rl.beiyang.ren/)

Every accepted entry in `data/papers.json` links to its official venue page.

The Tianjin University lab review checked all 329 records exposed by its
publication registry. A high-recall title pass retained 45 candidates covering
exploration, curiosity, uncertainty, diversity, population methods, and search;
abstract and source review then retained 14 papers where exploration is a
primary variable or a concrete mechanism. Generic optimization search,
application-level coverage, preference diversity, and uncertainty-only work
were excluded.

## Selection result

The high-recall discovery pass produced 413 candidates. Manual scope review
retained 182 papers:

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

## Legacy migration

The former detailed catalog contained 193 entries with arXiv links. Exact arXiv
metadata checks found 158 credible title matches and at least 32 clear link-title
mismatches. After scope review and deduplication against the official 2026
records, 58 additional verified legacy papers were retained.

The catalog also adds eight pre-2025 LLM/agent foundations and keeps seven
classical non-LLM RL references in a background-only appendix.

The catalog's seven mixed-axis sections were subsequently consolidated into
four primary research contexts: generation and inference; training, policy, and
curriculum; agentic interaction; and understanding and evaluation. Data,
memory, population, and self-improvement remain available as orthogonal
subtopics and tags, avoiding duplicate or ambiguous primary homes.

## Invariants

- A paper appears once and has one primary area.
- Multi-dimensional tags describe phase, level, signal, mechanism, problem, and
  setting.
- An official venue page, not a search result, supports every 2026 acceptance.
- Classical RL papers do not count toward catalog totals.
- Automated discovery cannot write directly to the accepted registry.
