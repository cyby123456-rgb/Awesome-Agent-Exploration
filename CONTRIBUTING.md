# Contributing to Awesome Exploration

Thank you for helping improve this reading list. The repository is intentionally
focused on **exploration mechanisms in reinforcement learning and post-training
for large language models**. It is a curated guide, not a feed of every paper
that mentions reinforcement learning, entropy, search, diversity, or agents.

## Scope

A paper is in scope when exploration is part of its primary contribution or
analysis. At least one of the following should be true:

- It changes how an LLM policy explores during RL/RLVR or post-training.
- It explicitly preserves or increases token-, response-, trajectory-, latent-,
  or policy-level diversity.
- It studies entropy collapse, exploration/exploitation, or capability-boundary
  expansion in LLM training.
- It introduces an exploration-specific metric, benchmark, or empirical analysis
  that materially informs the mechanisms above.

The following are normally out of scope:

- Non-LLM work that merely uses words such as "entropy", "noise", "diffusion",
  "policy", or "exploration" in another scientific domain.
- Generic LLM, agent, RL, reasoning, optimization, or test-time-scaling papers
  without a direct exploration contribution.
- Papers included only because a search query or classifier matched a keyword.
- Duplicate versions of a work already represented by its canonical paper.

When a work is useful but adjacent rather than directly in scope, put it in
**Related Topics** and explain the relationship.

## Evidence and quality bar

Every proposed entry must include:

1. An exact-title primary source link, preferably arXiv, OpenReview, ACL
   Anthology, or the publisher page. Search-result and title-mismatched links are
   not accepted.
2. A one- or two-sentence curation rationale based on reading the abstract (and,
   for ambiguous cases, the method or experiments), not just the title.
3. The most specific existing section and an accurate mechanism tag.
4. The official code link when one is available.
5. Matching updates to `README.md` and `README_DETAILED.md` until those files are
   generated from a single catalog.

Prefer one strong, well-supported entry over a large batch. Automated discovery
may create review candidates, but it must not write directly to the canonical
list without human review.

## Entry format

Compact view:

```markdown
- **Paper Title** ![](https://img.shields.io/badge/exploration--path-brightgreen)
  [[arxiv YYMM](https://arxiv.org/abs/YYMM.NNNNN)]
  [[Code](https://github.com/owner/repository)]
```

Detailed view:

```markdown
- **Paper Title** ![](https://img.shields.io/badge/exploration--path-brightgreen)
  [[arxiv YYMM](https://arxiv.org/abs/YYMM.NNNNN)]
  [[Code](https://github.com/owner/repository)]
  - *What exploration mechanism is introduced or analyzed, and why it belongs in this section.*
```

## Before opening a pull request

- Search the repository for both the exact title and the arXiv/DOI identifier.
- Verify that the link resolves to the same title and authors.
- Check that the classification and badge agree.
- Run `python3 scripts/audit_catalog.py` and note whether your change introduces
  any additional duplicate or drift warnings.
- Keep unrelated formatting changes out of a paper-addition pull request.

The catalog currently has historical quality debt. A contribution should reduce
that debt or, at minimum, avoid increasing it.
