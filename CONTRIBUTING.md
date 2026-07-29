# Contributing to Awesome Exploration

Thank you for helping improve **Awesome Exploration**. This repository is a
curated research map, so every paper addition needs both correct bibliographic
information and a clear explanation of why exploration is central to the work.

> **Fast path:** check scope and duplicates, add one record to
> `data/papers.json`, regenerate the public views, run the checks, and open a
> focused pull request. Do not edit `README.md`, `README_DETAILED.md`, or the
> research-map SVG by hand.

## Quick contribution workflow

1. Read [What belongs in the catalog?](#what-belongs-in-the-catalog) and make
   sure exploration is a primary contribution, not just a keyword.
2. Search for the exact title and arXiv/DOI identifier to avoid duplicates.
3. Fork the repository, create a branch, and add the paper to
   `data/papers.json` using the template below.
4. Choose exactly one `primary_area` and one valid `subtopic`, then add only
   taxonomy values listed in this guide.
5. Run the generator and validation commands.
6. Commit the data change together with all generated files and open a pull
   request using the repository's [PR template](.github/PULL_REQUEST_TEMPLATE.md).

If you are unsure about scope or classification, open an issue before doing a
large batch. One carefully supported paper is easier to review than many
borderline entries.

## What belongs in the catalog?

A paper is in scope when exploration is part of its primary method, analysis,
or evaluation. At least one of the following should be true:

- It changes how an LLM policy explores during RL/RLVR or post-training.
- It changes how an LLM explores candidate generations, reasoning paths, or
  latent representations at inference time.
- It changes how a language agent explores states, actions, tools, or
  long-horizon trajectories in an external environment.
- It explicitly preserves or increases token-, response-, trajectory-, latent-,
  policy-, data-, or population-level diversity.
- It studies entropy collapse, exploration/exploitation, capability boundaries,
  or another exploration-specific training dynamic.
- It introduces an exploration-specific metric, benchmark, survey, or empirical
  analysis that materially informs the mechanisms above.

The following are normally out of scope:

- Generic LLM, agent, RL, reasoning, optimization, or test-time-scaling papers
  without a direct exploration contribution.
- Papers included only because a search query matched words such as *entropy*,
  *noise*, *search*, *diversity*, *policy*, or *exploration*.
- Non-LLM work using those terms in an unrelated scientific domain.
- Duplicate arXiv, conference, workshop, or journal versions of a work already
  represented by one canonical entry.
- Classical non-LLM RL papers. Maintainers keep only a small background appendix
  of foundational references.

Ambiguous or unverified papers belong in `data/candidates.json`, not in the
public catalog. See [Candidate registry](docs/CANDIDATES.md) for that review
workflow.

## Before editing

### 1. Verify the source

Use an exact-title primary source URL, preferably:

- `https://arxiv.org/abs/...`
- an official OpenReview forum page;
- ACL Anthology;
- an official conference proceedings page; or
- the publisher's DOI page.

The URL must use HTTPS and must resolve to the same title and authors. Do not
submit search-result pages, paper-list pages, title-mismatched links, or copied
PDF mirrors.

### 2. Check for duplicates

Search for both the exact title and the identifier:

```bash
rg -inF "Exact Paper Title" data/papers.json data/candidates.json
rg -in "2510\.03222|10\.1234/example-doi" data/papers.json data/candidates.json
```

Also check alternate punctuation, capitalization, and earlier arXiv titles. If
the work already exists, update that record rather than adding a second version.

## Add a paper record

Add one JSON object inside the top-level `papers` array in
`data/papers.json`. Preserve valid JSON: objects are separated by commas,
strings use double quotes, and list-valued fields use square brackets.

### Copyable template

Replace every placeholder before submitting. Empty optional tag dimensions
should be written as `[]`, not omitted.

```json
{
  "id": "arxiv:YYMM.NNNNN",
  "title": "Exact paper title",
  "url": "https://arxiv.org/abs/YYMM.NNNNN",
  "authors": [
    "First Author",
    "Second Author"
  ],
  "date": "YYYY-MM-DD",
  "venue": "arXiv",
  "primary_area": "choose-one-primary-area",
  "subtopic": "choose-one-valid-subtopic",
  "paper_type": "method",
  "phase": [
    "choose-at-least-one-phase"
  ],
  "level": [
    "choose-at-least-one-level"
  ],
  "signal": [],
  "mechanism": [
    "choose-a-signal-or-mechanism"
  ],
  "problem": [],
  "setting": [],
  "rationale": "In one or two factual sentences, state where exploration occurs and what signal or mechanism the paper contributes."
}
```

### Worked example

This example shows valid structure and taxonomy values. Do not copy it as a new
entry because the paper is already in the catalog.

```json
{
  "id": "arxiv:2510.15502",
  "title": "The Road Less Traveled: Enhancing Exploration in LLMs via Sequential Sampling",
  "url": "https://arxiv.org/abs/2510.15502",
  "authors": [
    "Shijia Kang",
    "Muhan Zhang"
  ],
  "date": "2025-10-17",
  "venue": "arXiv",
  "primary_area": "llm-exploration",
  "subtopic": "decoding-sampling",
  "paper_type": "method",
  "phase": [
    "inference"
  ],
  "level": [
    "response/sequence"
  ],
  "signal": [],
  "mechanism": [
    "sampling/decoding"
  ],
  "problem": [],
  "setting": [],
  "rationale": "Uses sequential sampling to explore alternative LLM generations at inference time, with candidate diversity controlled through the decoding process."
}
```

## Field-by-field reference

| Field | Required? | How to fill it |
|---|---|---|
| `id` | Yes | A stable unique identifier. Use `arxiv:<number>` for arXiv, `doi:<DOI>` for DOI-only records, or `openreview:<forum-id>` for OpenReview. Ask a maintainer before inventing another prefix. |
| `title` | Yes | Copy the exact title from the primary source. Preserve capitalization and punctuation; do not add Markdown or a star emoji. |
| `url` | Yes | Canonical HTTPS primary-source URL matching the exact paper. Prefer an arXiv abstract page or official proceedings/publisher page. |
| `authors` | Expected | Authors in the source's displayed order, as a JSON list of names. Do not shorten the list to `et al.`. |
| `date` | Yes | Earliest public paper date, preferably `YYYY-MM-DD`. The validator also accepts `YYYY-MM` and `YYYY`. |
| `venue` | Expected | Use `arXiv` for a preprint or the official venue and year, such as `NeurIPS 2025`. Do not guess acceptance status. |
| `published_venue` | Optional | Use when the canonical link remains arXiv but a formal version is verified, for example `ACL 2025 Main`. |
| `primary_area` | Yes | Exactly one category ID from the category table below. Classify the paper by its main exploration loop. |
| `subtopic` | Yes | Exactly one subtopic ID belonging to the selected `primary_area`. |
| `paper_type` | Yes | One of `method`, `analysis`, `benchmark`, `survey`, or `position`; see the rule below. |
| `phase` | Yes | One or more allowed phase values. Answers **when** exploration occurs or changes. |
| `level` | Yes | One or more allowed level values. Answers **what object** is explored or diversified. |
| `signal` | Conditional | Allowed values only. `signal` and `mechanism` cannot both be empty. Answers **what quantity** indicates or guides exploration. |
| `mechanism` | Conditional | Allowed values only. `signal` and `mechanism` cannot both be empty. Answers **how** exploration is produced or controlled. |
| `problem` | Optional | Zero or more allowed failure modes or trade-offs. Use `[]` when none applies. |
| `setting` | Optional | Zero or more allowed evaluation domains. Use `[]` when none applies. |
| `rationale` | Expected | One or two factual sentences based on the abstract and, if needed, method/experiments. State where exploration happens and what makes it central. |

Do not add `featured`, `featured_rank`, `notability`, `citation_count`,
`citation_source`, `citation_checked`, `source_group`, or `discovery_category`
unless a maintainer explicitly asks. These fields control curated selections,
stars, evidence snapshots, and import provenance. Put an official code URL in
the PR description; the current paper schema has no code-URL field.

## Choose the primary category and subtopic

Choose the category containing the paper's **main exploration loop**, not every
context mentioned in the introduction.

| `primary_area` | Use when | Valid `subtopic` values |
|---|---|---|
| `llm-exploration` | Generation, decoding, reasoning-path search, or latent steering at inference time without a learning update as the central contribution. | `decoding-sampling`, `search-deliberation`, `representation-steering`, `diversity-coverage` |
| `rlvr-policy-curriculum-exploration` | Exploration changes an LLM policy, rollout distribution, reward, data selection, or curriculum. | `entropy-distribution`, `credit-optimization`, `reward-rollout`, `replay-population`, `capability-dynamics`, `data-selection-prompting`, `task-synthesis-curriculum` |
| `agentic-exploration` | An agent explores an external or persistent environment at inference/test time without a training update as the central loop. | `web-tools-gui`, `planning-interaction`, `embodied-environments`, `knowledge-memory` |
| `agentic-training-exploration` | External interaction generates experience, tasks, or policy updates for agent training. | `web-tools-gui`, `planning-interaction`, `embodied-environments`, `knowledge-memory` |
| `understanding-evaluation` | The main contribution measures, explains, surveys, or benchmarks exploration rather than introducing an intervention. | `surveys-position`, `theory-training-dynamics`, `capability-boundaries`, `benchmarks-metrics` |

Use this decision order for ambiguous papers:

1. Measurement, explanation, benchmark, survey, or position paper only:
   `understanding-evaluation`.
2. External agent interaction supplies training experience, tasks, or updates:
   `agentic-training-exploration`.
3. External or persistent environment exploration occurs at inference/test time:
   `agentic-exploration`.
4. Exploration changes an LLM policy, RLVR rollout, dataset, or curriculum:
   `rlvr-policy-curriculum-exploration`.
5. Generation, decoding, latent steering, or test-time reasoning search:
   `llm-exploration`.

For fuller explanations and worked boundary cases, read
[Taxonomy Design](docs/TAXONOMY.md).

## Choose the paper type

| `paper_type` | Meaning | Category rule |
|---|---|---|
| `method` | Introduces an intervention that changes exploration. | Must use one of the four intervention categories, not `understanding-evaluation`. |
| `analysis` | Empirically or theoretically explains exploration behavior. | Must use `understanding-evaluation`. |
| `benchmark` | Introduces an exploration-focused benchmark or metric suite. | Must use `understanding-evaluation`. |
| `survey` | Synthesizes the exploration literature. | Must use `understanding-evaluation`. |
| `position` | Argues for a research framing or agenda. | Must use `understanding-evaluation`. |

## Allowed taxonomy values

Use the exact lowercase strings below. Do not create a new spelling, synonym,
or capitalization variant in a paper-addition PR.

| Dimension | Allowed values |
|---|---|
| `phase` | `data-generation`, `supervised-post-training`, `rl-training`, `inference`, `test-time-adaptation`, `continual/self-improvement` |
| `level` | `token`, `response/sequence`, `trajectory/action`, `latent/representation`, `policy-distribution`, `data/task`, `population/multi-policy` |
| `signal` | `entropy/probability`, `uncertainty/confidence`, `novelty/curiosity`, `semantic-diversity`, `coverage`, `information-gain`, `reward/advantage`, `disagreement` |
| `mechanism` | `sampling/decoding`, `temperature-control`, `noise/perturbation`, `regularization`, `gradient-reshaping`, `reward-shaping/intrinsic-reward`, `tree-search/branching`, `structured-search`, `backtracking/resampling`, `replay/memory`, `curriculum/task-generation`, `self-play/co-evolution`, `ensemble/population` |
| `problem` | `entropy-collapse`, `mode-collapse`, `sparse-reward`, `local-optimum`, `capability-boundary`, `long-horizon`, `exploration-exploitation`, `recovery/error-correction` |
| `setting` | `math`, `code`, `multimodal`, `creative/open-ended`, `web`, `tool-use`, `knowledge-graph`, `embodied`, `multi-agent` |

Include only values that materially describe the paper's exploration
contribution. The registry may preserve several applicable values, while the
generated README intentionally displays at most three representative badges.

## Create and test your branch

### 1. Fork and clone

Fork the repository on GitHub, then clone your fork and create a focused branch:

```bash
git clone https://github.com/<your-username>/Awesome-Exploration.git
cd Awesome-Exploration
git switch -c add-<short-paper-name>
```

### 2. Edit the registry

Edit `data/papers.json`. Do not manually edit generated files. Keep unrelated
formatting, reordering, or cleanup out of a paper-addition PR.

### 3. Run all checks

Python 3.11 is used in CI. The repository has no package-install step for the
catalog checks.

```bash
python3 -m json.tool data/papers.json >/dev/null
python3 scripts/validate_catalog.py
python3 scripts/generate_catalog.py
python3 scripts/audit_catalog.py
git diff --check
```

`generate_catalog.py` updates `README.md`, `README_DETAILED.md`, and
`assets/research-map.svg`. Include those generated changes in the same commit.
Do not hand-edit them after generation.

### 4. Review and commit

```bash
git status --short
git diff -- data/papers.json README.md README_DETAILED.md assets/research-map.svg
git add data/papers.json README.md README_DETAILED.md assets/research-map.svg
git commit -m "Add <short paper title>"
git push -u origin add-<short-paper-name>
```

## Open the pull request

Open your fork on GitHub and select **Compare & pull request**. Set the base
repository to `cyby123456-rgb/Awesome-Exploration` and the base branch to
`main`.

GitHub pre-populates the [PR template](.github/PULL_REQUEST_TEMPLATE.md) when
you open the pull request. Complete every relevant field:

- **Exact paper title:** must match `data/papers.json` and the primary source.
- **Primary source URL:** canonical arXiv, OpenReview, proceedings, or publisher
  URL.
- **Official code URL:** include it when available; do not put an unverified
  third-party implementation here.
- **Primary category and subtopic:** provide both registry IDs.
- **Exploration mechanism:** briefly name the signal and/or mechanism.
- **Why directly relevant:** explain the exploration contribution in one or two
  sentences rather than repeating the title.

A good PR is focused: one paper or one tightly related batch, one purpose, no
unrelated formatting changes, and no manual edits to generated views.

## What CI checks

Every pull request runs the catalog workflow. It verifies that:

- required fields are present and dates/URLs are well formed;
- IDs, normalized titles, and URLs are unique;
- the primary area, subtopic, paper type, and tags use allowed combinations;
- every paper has a `phase`, a `level`, and at least one `signal` or
  `mechanism`;
- the generated README files and research-map SVG match `data/papers.json`; and
- the public catalog and detailed catalog contain the same registry entries.

### Common CI failures

| Failure | How to fix it |
|---|---|
| JSON parse error | Check commas, double quotes, brackets, and braces. Run `python3 -m json.tool data/papers.json`. |
| Duplicate ID, title, or URL | Update the existing record or remove the duplicate entry. |
| Invalid subtopic | Choose a subtopic listed under the selected `primary_area`. |
| Invalid tag | Copy the exact value from [Allowed taxonomy values](#allowed-taxonomy-values). |
| `method` category error | Put methods in an intervention category; reserve `understanding-evaluation` for analysis, benchmark, survey, and position papers. |
| Missing signal/mechanism | Add at least one evidence-based `signal` or `mechanism` value. |
| Generated files differ | Run `python3 scripts/generate_catalog.py` and commit all generated changes. |
| Link/title concern in review | Replace the URL with an exact-title primary source and verify the author list. |

If local checks pass but CI fails, read the first failing step in the GitHub
Actions log and include the error in the PR discussion. Do not silence or bypass
the validator.

## Non-paper contributions

Fixes to metadata, taxonomy documentation, scripts, links, or repository design
are welcome. Explain the problem and intended behavior in the PR, run the
relevant checks, and keep generated-file changes tied to their source change.
For a simple typo or broken link, a small focused PR is best.

Thank you for helping keep the catalog accurate, navigable, and useful.
