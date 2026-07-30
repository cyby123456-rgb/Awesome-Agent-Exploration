# Contributing to Awesome Exploration

Thank you for improving this curated map of exploration in large language
models and agents. The easiest contribution is one well-supported paper in a
focused pull request.

## Submit a paper in four steps

1. [Check scope and duplicates](#check) before editing.
2. [Add one record](#add) to `data/papers.json` with the template below.
3. [Generate and test](#test) the public files locally.
4. [Open a pull request](#pr) with the required evidence and classification.

> **Important:** Edit `data/papers.json`, not `README.md`,
> `README_DETAILED.md`, or `assets/research-map.svg`. Those public files are
> generated automatically from the registry.

<a id="check"></a>

## 1. Check scope and duplicates

Add a paper only when exploration is a primary method, analysis, or evaluation
contribution for an LLM or agent. Generic RL, search, diversity, test-time
scaling, or agent papers are out of scope when exploration is only a keyword.
Classical non-LLM RL belongs in the background appendix, not the main catalog.

Use an exact-title primary source URL: arXiv, OpenReview, ACL Anthology,
official proceedings, or a publisher DOI page. Confirm that the title and
authors match, then search for an existing entry:

```bash
rg -inF "Exact Paper Title" data/papers.json data/candidates.json
rg -in "2510\.03222|10\.1234/example-doi" data/papers.json data/candidates.json
```

If the work is already present, update its existing record instead of adding a
second arXiv, conference, or journal version. If scope or evidence is unclear,
add it to [`data/candidates.json`](data/candidates.json) or open an issue first.

<a id="add"></a>

## 2. Add a paper record

Fork the repository, clone your fork, and create a branch:

```bash
git clone https://github.com/<your-username>/Awesome-Exploration.git
cd Awesome-Exploration
git switch -c add-<short-paper-name>
```

Add one object to the top-level `papers` list in `data/papers.json`. Use double
quotes and commas between objects. Use `[]` for an optional tag dimension with
no applicable value.

```json
{
  "id": "arxiv:YYMM.NNNNN",
  "title": "Exact paper title",
  "url": "https://arxiv.org/abs/YYMM.NNNNN",
  "authors": ["First Author", "Second Author"],
  "date": "YYYY-MM-DD",
  "venue": "arXiv",
  "primary_area": "llm-exploration",
  "subtopic": "decoding-sampling",
  "paper_type": "method",
  "phase": ["inference"],
  "level": ["response/sequence"],
  "signal": [],
  "mechanism": ["sampling/decoding"],
  "problem": [],
  "setting": [],
  "rationale": "State where exploration happens and the paper's concrete exploration contribution."
}
```

### Fill the fields

| Field | What to provide |
|---|---|
| `id` | A unique stable ID: normally `arxiv:<number>`, `doi:<DOI>`, or `openreview:<forum-id>`. |
| `title`, `url`, `authors` | Exact metadata from the primary source. The URL must use HTTPS. |
| `date`, `venue` | Public date (`YYYY-MM-DD` preferred) and `arXiv` or a verified venue, such as `NeurIPS 2025`. |
| `published_venue` | Optional: verified formal venue when the canonical URL remains arXiv. |
| `primary_area`, `subtopic` | One category and one matching subtopic from [the category table](#choose-the-category-and-subtopic). |
| `paper_type` | `method`, `analysis`, `benchmark`, `survey`, or `position`. |
| `rationale` | One or two factual sentences explaining why exploration is central. |

`phase` and `level` are required. At least one of `signal` or `mechanism` must
be non-empty. `problem` and `setting` are optional. Copy exact tag values from
[Taxonomy Design](docs/TAXONOMY.md#tag-dimensions); do not invent synonyms.

For these tag fields, first answer the question in the middle column:

| Field | Ask yourself | Example |
|---|---|---|
| `phase` | **When** does exploration happen or change? | Inference: `inference`; RL update: `rl-training` |
| `level` | **What** is explored or diversified? | Token: `token`; reasoning path: `response/sequence` |
| `signal` | **What quantity** values or guides exploration? | Entropy: `entropy/probability`; novelty: `novelty/curiosity` |
| `mechanism` | **How** is exploration produced or controlled? | Sampling: `sampling/decoding`; tree search: `tree-search/branching` |
| `problem` | **Why** is exploration needed? | `entropy-collapse`, `sparse-reward`; otherwise `[]` |
| `setting` | **Where** is it evaluated? | `math`, `code`, `web`; otherwise `[]` |

Do not set `featured`, `featured_rank`, `notability`, `citation_*`,
`source_group`, or `discovery_category` unless a maintainer asks. Put an
official code URL in the PR description; the registry currently has no code URL
field.

### Choose the category and subtopic

Choose the paper's **main exploration loop**, not every setting it mentions.

| `primary_area` | Use when | Valid `subtopic` values |
|---|---|---|
| `llm-exploration` | Exploration happens in generation or inference without a central learning update. | `decoding-sampling`, `search-deliberation`, `representation-steering`, `diversity-coverage` |
| `rlvr-policy-curriculum-exploration` | Exploration changes an LLM policy, rollout, reward, data choice, or curriculum. | `entropy-distribution`, `credit-optimization`, `reward-rollout`, `replay-population`, `capability-dynamics`, `data-selection-prompting`, `task-synthesis-curriculum` |
| `agentic-exploration` | An agent explores an external environment at inference or test time. | `web-tools-gui`, `planning-interaction`, `embodied-environments`, `knowledge-memory` |
| `agentic-training-exploration` | External interaction creates experience, tasks, or updates an agent policy. | `web-tools-gui`, `planning-interaction`, `embodied-environments`, `knowledge-memory` |
| `understanding-evaluation` | The contribution measures, explains, surveys, or benchmarks exploration. | `surveys-position`, `theory-training-dynamics`, `capability-boundaries`, `benchmarks-metrics` |

Use `method` only for the first four intervention categories. `analysis`,
`benchmark`, `survey`, and `position` must use `understanding-evaluation`.
For boundary cases and all allowed tags, see [Taxonomy Design](docs/TAXONOMY.md).

<a id="test"></a>

## 3. Generate and test

Run these commands before committing:

```bash
python3 -m json.tool data/papers.json >/dev/null
python3 scripts/validate_catalog.py
python3 scripts/generate_catalog.py
python3 scripts/audit_catalog.py
git diff --check
```

The generator updates `README.md`, `README_DETAILED.md`, and
`assets/research-map.svg`. Include all generated changes in the same commit;
the CI rejects a PR when they are stale.

```bash
git add data/papers.json README.md README_DETAILED.md assets/research-map.svg
git commit -m "Add <short paper title>"
git push -u origin add-<short-paper-name>
```

<a id="pr"></a>

## 4. Open a pull request

On your fork, select **Compare & pull request**. Set the base repository to
`cyby123456-rgb/Awesome-Exploration` and the base branch to `main`.

GitHub opens the [PR template](.github/PULL_REQUEST_TEMPLATE.md) automatically.
For a paper addition, fill in:

- exact paper title and primary source URL;
- official code URL, if available;
- proposed `primary_area` and `subtopic` IDs;
- exploration signal and/or mechanism; and
- one or two sentences explaining direct relevance to LLM or agent exploration.

Keep the PR focused: one paper or a tightly related batch, no unrelated
formatting changes, and no hand-edited generated files. CI checks JSON syntax,
duplicate IDs/titles/URLs, taxonomy validity, and generated-file parity.

## Other contributions

Metadata fixes, broken links, taxonomy documentation, and tooling improvements
are welcome. Explain the problem and intended behavior in the PR, then run the
relevant checks. For a simple typo or broken link, a small focused PR is ideal.
