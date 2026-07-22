# Contributing to Awesome Exploration

Thank you for helping improve this reading list. The repository is intentionally
focused on **exploration in language-model generation, learning and
post-training, interactive agents, and evaluation**. It is a curated guide, not
a feed of every paper that mentions reinforcement learning, entropy, search,
diversity, or agents.

## Scope

A paper is in scope when exploration is part of its primary contribution or
analysis. At least one of the following should be true:

- It changes how an LLM policy explores during RL/RLVR or post-training.
- It changes how an LLM explores candidate generations or reasoning paths at
  inference time.
- It changes how a language agent explores states, actions, tools, or long-horizon
  trajectories in an external environment.
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

When a work is adjacent but does not satisfy the acceptance rule, keep it out of
the public catalog and, if worthwhile to revisit, add it to the candidate queue
with a clear review reason.

## Evidence and quality bar

Every proposed entry must include:

1. An exact-title primary source link, preferably arXiv, OpenReview, ACL
   Anthology, or the publisher page. Search-result and title-mismatched links are
   not accepted.
2. A one- or two-sentence curation rationale based on reading the abstract (and,
   for ambiguous cases, the method or experiments), not just the title.
3. One primary category and accurate multi-dimensional tags.
4. The official code link when one is available.
5. A change to the structured registry in `data/papers.json`. The Markdown views
   are generated and must not be edited directly.

Prefer one strong, well-supported entry over a large batch. Automated discovery
may create review candidates, but it must not write directly to the canonical
list without human review. Candidate records belong in
[`data/candidates.json`](data/candidates.json); see
[`docs/CANDIDATES.md`](docs/CANDIDATES.md) for the review workflow.

## Entry format

Each paper has exactly one `primary_area` and may use several orthogonal tag
dimensions. The required dimensions are `phase` and `level`; at least one
`signal` or `mechanism` tag is also required.

```json
{
  "id": "arxiv:2510.03222",
  "title": "Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward",
  "url": "https://arxiv.org/abs/2510.03222",
  "date": "2025-10-03",
  "primary_area": "rlvr-policy-curriculum-exploration",
  "subtopic": "entropy-distribution",
  "paper_type": "method",
  "phase": ["rl-training"],
  "level": ["token", "policy-distribution"],
  "signal": ["entropy/probability"],
  "mechanism": ["regularization"],
  "problem": ["entropy-collapse"],
  "setting": ["math"]
}
```

Every entry also needs one valid `subtopic` within its primary category. Valid
primary categories are `llm-exploration`,
`rlvr-policy-curriculum-exploration`, `agentic-exploration`,
`agentic-training-exploration`, and `understanding-evaluation`. Agentic papers
belong in `agentic-training-exploration` when external interaction generates
experience, tasks, or policy updates; inference- and test-time interaction stays
in `agentic-exploration`. Data, memory, population, and self-improvement remain
subtopics and tags. Classical non-LLM RL papers are not normal entries; the
maintainers keep a deliberately small appendix of foundational references.

See [`docs/TAXONOMY.md`](docs/TAXONOMY.md) for the primary-area decision rule,
the meaning of every tag dimension, and worked classification examples.

## Before opening a pull request

- Search the repository for both the exact title and the arXiv/DOI identifier.
- Verify that the link resolves to the same title and authors.
- Check that the primary category and all tag dimensions describe the paper's
  actual exploration contribution rather than incidental keywords.
- Run `python3 scripts/validate_catalog.py`.
- Run `python3 scripts/generate_catalog.py` and include the generated Markdown
  changes.
- Keep unrelated formatting changes out of a paper-addition pull request.

The catalog currently has historical quality debt. A contribution should reduce
that debt or, at minimum, avoid increasing it.
