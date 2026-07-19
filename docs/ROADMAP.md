# Awesome Exploration: Repository Audit and Roadmap

> Evidence snapshot: 2026-07-19. Repository counts can be reproduced with
> `python3 scripts/audit_catalog.py`.

## Executive conclusion

The repository has a useful and defensible niche: **how LLMs explore during
reinforcement learning and post-training**. That is narrower than general RL,
RLHF, RLVR, or LLM reasoning lists and can become the project's main advantage.

The immediate bottleneck is not coverage. It is trust. Automated additions have
mixed directly relevant papers with broad keyword matches, duplicated entries,
incorrect paper links, and two Markdown views that no longer represent the same
catalog. The highest-return strategy is therefore:

1. Freeze direct-to-catalog automation.
2. Recover a human-reviewed core.
3. Separate machine-discovered candidates from accepted entries.
4. Generate every public view from one structured source of truth.

## Comparable repositories and standards

| Project | Evidence observed | Practice worth adopting | Caveat or lesson |
|---|---|---|---|
| [Official Awesome project](https://github.com/sindresorhus/awesome) | Manifesto, list requirements, and `awesome-lint` | Treat the list as curation rather than collection; require descriptions, a license file, contribution guidelines, and consistent formatting | The current catalog would not satisfy the quality and lint bar yet |
| [OpenDILab Awesome Exploration RL](https://github.com/opendilab/awesome-exploration-rl) | About 713 stars; taxonomy graphic; authors, keywords, and experiment environments; contribution guide and license | Visual taxonomy and structured per-paper metadata make a large list navigable | Its scope is all exploration RL, so this repository should stay differentiated around LLM post-training |
| [OpenDILab Awesome RLHF](https://github.com/opendilab/awesome-RLHF) | About 4.4k stars; papers plus codebases, datasets, blogs, and books; contribution guide and license | Add high-signal resource types beyond papers and expose a predictable entry schema | Breadth must remain curated or it becomes difficult to scan |
| [Awesome LLM Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) | About 3.6k stars; papers include authors, venue/year, and code | Lightweight bibliographic metadata is more useful than a decorative tag alone | Its broad reasoning scope leaves room for a deeper exploration-mechanism view here |
| [Awesome RL for LRMs](https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs) | About 2.5k stars; tied to a survey; includes a BibTeX database, figures, and a release | Connect the list to a stable taxonomy and machine-readable bibliography | Survey-driven organization needs a clear update policy after publication |
| [Awesome LLM-RLVR](https://github.com/smiles724/Awesome-LLM-RLVR) | Automated recent-paper section and update workflow | Automation is useful for discovery and freshness | Its auto-fetched section also shows unrelated results; candidates should not be treated as curated entries |

Primary standards consulted:

- [The Awesome manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md)
- [Requirements for an Awesome list](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md#requirements-for-your-awesome-list)
- [`awesome-lint`](https://github.com/sindresorhus/awesome-lint)

## Current-state evidence

The local audit reports:

- `README.md`: **817 entries**, **713 unique titles**, **54 duplicate-title
  groups**, **104 extra duplicate occurrences**, and **21 primary-identifier
  collisions**.
- `README_DETAILED.md`: **230 entries**, **225 unique titles**, **4
  duplicate-title groups**, and **15 primary-identifier collisions**.
- View drift: **511 titles only in the compact view** and **23 titles only in
  the detailed view**.
- A second catalog exists under `awesome-exploration/`, creating four competing
  README files and two title registries.

The quality problems are not merely cosmetic:

- Clearly unrelated works appear in the canonical list, including papers on an
  evaporating black hole, silicon photonic phase shifters, electric aircraft,
  quantum circuits, and clinical imaging.
- Some links resolve to a different publication than the displayed title. For
  example, the local entry for **Can GRPO Help LLMs Transcend Their Pretraining
  Origin?** points to a 2013 Joyce bibliography, while the paper is
  [arXiv:2510.15990](https://arxiv.org/abs/2510.15990). **JustRL** should resolve
  to [arXiv:2512.16649](https://arxiv.org/abs/2512.16649), and **DRA-GRPO** to
  [arXiv:2505.09655](https://arxiv.org/abs/2505.09655).
- `batch_fetch_links.py` contains a machine-specific Windows path and searches
  only the older quoted-title syntax. Its first-match behavior also lacks a
  strong exact-title verification gate, which can silently attach a valid but
  unrelated DOI.
- Nightly commits are not backed by a workflow or discovery configuration in
  this checkout, making the ingestion criteria hard to audit or reproduce.

## Recommended product position

The list should answer a researcher's concrete question:

> Where is exploration introduced, what signal controls it, at what granularity
> does it act, and how is its effect measured in LLM RL?

That framing suggests a two-axis taxonomy:

- **Intervention level:** token, response/trajectory, latent state, policy
  distribution, data/curriculum, multi-policy or population.
- **Exploration signal:** entropy/probability, uncertainty, novelty/curiosity,
  diversity, search/replay, perturbation/noise, intrinsic reward, external
  guidance.

Scenario (math, code, agent, creative generation) and evidence status (preprint,
peer reviewed, code available, independently reproduced) should be filters, not
the main taxonomy. This avoids placing the same paper in several top-level
sections.

## Prioritized roadmap

### P0 — Restore trust in the canonical list

1. Pause any job that commits search results directly into `README.md`.
2. Choose a last-known human-reviewed commit as the baseline and review later
   additions in batches. Preserve rejected candidates in an archive with a
   rejection reason rather than silently losing provenance.
3. Correct title-to-link mismatches using arXiv/OpenReview/publisher metadata,
   then deduplicate by normalized title and canonical arXiv/DOI identifier.
4. Select the root files as canonical and remove the nested catalog only after
   all unique reviewed entries have been migrated.
5. Add a real root `LICENSE` file matching the stated Creative Commons license.
   If official Awesome inclusion matters, its current guidance recommends CC0;
   otherwise the existing CC BY 4.0 choice is reasonable when attribution is
   desired.

Exit criteria: zero duplicate titles, zero identifier collisions, zero known
title/link mismatches, and no unreviewed automated entries in the accepted list.

### P1 — Establish one source of truth

Move accepted records into `data/papers.json` (or YAML) and generate the compact
README, detailed README, title index, and optional BibTeX from it. A record should
contain at least:

```json
{
  "id": "arxiv:2505.09655",
  "title": "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models",
  "date": "2025-05-14",
  "intervention_level": ["response", "policy"],
  "exploration_signal": ["semantic-diversity"],
  "scenarios": ["math", "rlvr"],
  "primary_url": "https://arxiv.org/abs/2505.09655",
  "code_url": "https://github.com/xiwenc1/DRA-GRPO",
  "status": "reviewed",
  "summary": "Reweights group rewards using semantic diversity to reduce redundant completions."
}
```

Maintain a separate `data/candidates.json` for automated discoveries. Promotion
from candidate to reviewed should require a pull request and the curation rubric
in `CONTRIBUTING.md`.

Exit criteria: public artifacts are reproducible from data; generated files are
never hand-edited; compact and detailed views have exact identifier parity.

### P2 — Improve researcher usability

- Put a concise taxonomy graphic and a "start here" set of surveys/foundational
  papers above the full catalog.
- Add a comparison matrix for representative mechanisms: intervention level,
  signal, training/inference phase, reward type, target metric, code, and main
  limitation.
- Split **Recently reviewed** from the stable core and publish a small changelog.
- Add codebases, benchmarks, datasets, and high-quality tutorials only when they
  directly serve exploration research.
- Provide BibTeX and a machine-readable export. Add a filterable static site only
  after the data model is stable; it should be generated from the same catalog.

Exit criteria: a new reader can find foundational work, compare mechanisms, and
export citations without scanning hundreds of undifferentiated bullets.

### P3 — Make maintenance sustainable

- Run local structural checks on every pull request, followed by network-based
  title metadata and link validation.
- Configure automated discovery to open an issue or pull request containing
  candidates, search rationale, and confidence; never push accepted content.
- Review on a weekly or biweekly cadence and publish a monthly curated release.
- Add GitHub topics such as `awesome`, `awesome-list`, `llm`, `reinforcement-learning`,
  `rlvr`, `exploration`, and `reasoning`.
- Track catalog health: reviewed additions, rejection reasons, stale/broken
  links, duplicate rate, metadata completeness, and median review age.

## Changes already introduced by this audit

- `CONTRIBUTING.md` defines the scope and acceptance rubric.
- `.github/PULL_REQUEST_TEMPLATE.md` collects evidence needed for review.
- `scripts/audit_catalog.py` makes duplication, identifier collision, view drift,
  and nested-copy debt reproducible.

The audit intentionally does not mass-delete historical entries. That cleanup
requires a human-reviewed baseline or explicit acceptance decisions, and should
be the first follow-up implementation project.
