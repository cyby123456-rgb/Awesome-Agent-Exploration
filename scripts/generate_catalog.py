#!/usr/bin/env python3
"""Generate the public Markdown views from the curated paper registry."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"

AREA_LABELS = {
    "llm-exploration": "LLM Generation & Inference Exploration",
    "rlvr-exploration": "Exploration for RLVR",
    "agentic-exploration": "Agentic Exploration",
    "understanding-evaluation": "Understanding, Evaluation & Benchmarks",
}

AREA_SUMMARIES = {
    "llm-exploration": "Exploration during language-model generation and inference, without RL policy updates as the central contribution.",
    "rlvr-exploration": "Exploration during RL/RLVR post-training, where exploration changes the rollout distribution or policy update.",
    "agentic-exploration": "Exploration by language agents acting over states, tools, observations, and long-horizon trajectories.",
    "understanding-evaluation": "Work that measures, explains, surveys, or benchmarks exploration rather than primarily introducing an intervention.",
}

AREA_DESCRIPTIONS = {
    "llm-exploration": [
        "This category covers exploration that happens while a language model is generating or selecting candidate outputs, rather than through a reinforcement-learning update. Typical examples include sampling and decoding strategies, self-consistency, semantic-diversity methods, latent-state steering, and tree or graph search at inference time.",
        "The central question is how to search a model's existing generative distribution more broadly, safely, or efficiently. Papers belong here when the main contribution improves or analyzes candidate generation, reasoning-path search, or output diversity without making RL post-training the core mechanism.",
    ],
    "rlvr-exploration": [
        "This category concerns exploration during reinforcement learning or RL with verifiable rewards (RLVR). Here, exploration changes which rollouts are collected, how reward or advantage signals are assigned, or how the policy distribution is updated during training.",
        "It includes work on entropy or mode collapse, low-probability tokens, rollout diversity, intrinsic or shaped rewards, gradient and regularization interventions, curriculum design, and attempts to push beyond a base model's capability boundary. The defining feature is that exploration is part of the learning loop, not only an inference-time search choice.",
    ],
    "agentic-exploration": [
        "This category covers language agents that explore an external or persistent environment: webpages, tools, GUIs, knowledge graphs, games, embodied worlds, or multi-agent settings. The object of exploration is usually a trajectory of states, actions, observations, and tool calls rather than a single textual response.",
        "These papers focus on challenges such as partial observability, long horizons, recovery from failed actions, memory, environment coverage, and interactive search. A paper belongs here when external interaction is central to the exploration problem and evaluation.",
    ],
    "understanding-evaluation": [
        "This category collects empirical analyses, theoretical accounts, surveys, metrics, and benchmarks that help the field understand exploration. Rather than primarily proposing a new exploration intervention, these works measure diversity, characterize training dynamics, evaluate capability boundaries, or establish a shared vocabulary and test bed.",
        "They are essential for judging whether a method genuinely improves exploration instead of merely changing accuracy or sampling behavior. Keeping them separate makes the evidence about a phenomenon easy to distinguish from methods designed to change it.",
    ],
}

TAG_DIMENSIONS = [
    ("Phase", "data generation; supervised post-training; RL training; inference; test-time adaptation; continual/self-improvement"),
    ("Level", "token; response/sequence; trajectory/action; latent/representation; policy distribution; data/task; population"),
    ("Signal", "entropy/probability; uncertainty/confidence; novelty/curiosity; semantic diversity; coverage; information gain; reward/advantage; disagreement"),
    ("Mechanism", "sampling/decoding; temperature control; noise/perturbation; regularization; gradient reshaping; intrinsic reward; structured/tree search; replay/memory; curriculum; self-play; ensemble/population"),
    ("Problem", "entropy or mode collapse; sparse reward; local optimum; capability boundary; long horizon; exploration/exploitation; recovery"),
    ("Setting", "math; code; multimodal; creative/open-ended; web; tool use; knowledge graph; embodied; multi-agent"),
]


def load_catalog() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def area_description_lines(area: str) -> list[str]:
    """Render each explanatory paragraph as a distinct Markdown paragraph."""
    lines: list[str] = []
    for paragraph in AREA_DESCRIPTIONS[area]:
        lines.extend([paragraph, ""])
    return lines


def compact_tags(paper: dict) -> str:
    values: list[str] = []
    # Keep the compact view informative: show the main phase, at most two
    # intervention levels, then prioritize exploration signals and operators.
    values.extend(paper.get("phase", [])[:1])
    values.extend(paper.get("level", [])[:2])
    values.extend(paper.get("signal", [])[:2])
    values.extend(paper.get("mechanism", [])[:2])
    unique = list(dict.fromkeys(values))
    return " ".join(f"`{value}`" for value in unique[:6])


def source_label(paper: dict) -> str:
    venue = paper.get("venue") or "Preprint"
    if paper.get("source_group") == "conference-2026":
        return f"**{venue}**"
    return venue


def statistics_table(papers: list[dict]) -> list[str]:
    area_counts = Counter(p["primary_area"] for p in papers)
    accepted = Counter(
        p["venue"] for p in papers if p.get("source_group") == "conference-2026"
    )
    lines = [
        "| Collection | Papers |",
        "|---|---:|",
        *[f"| {AREA_LABELS[area]} | {area_counts[area]} |" for area in AREA_LABELS],
        f"| **Curated total** | **{len(papers)}** |",
        "",
        "2026 peer-reviewed acceptances in the catalog:",
        "",
        "| Venue | Papers |",
        "|---|---:|",
        *[f"| {venue} | {count} |" for venue, count in sorted(accepted.items())],
        f"| **Accepted total** | **{sum(accepted.values())}** |",
    ]
    return lines


def render_readme(catalog: dict) -> str:
    papers = catalog["papers"]
    lines = [
        "<div align=\"center\">",
        "",
        "# Awesome Exploration",
        "",
        "**A curated research map of exploration in language models, RLVR, and agents.**",
        "",
        "[![Curated catalog](https://img.shields.io/badge/catalog-curated-3B82F6?style=flat-square)](docs/CURATION_2026.md) "
        f"[![{len(papers)} papers](https://img.shields.io/badge/papers-{len(papers)}-8B5CF6?style=flat-square)](#catalog) "
        "[![Four research tracks](https://img.shields.io/badge/tracks-4-10B981?style=flat-square)](#research-map) "
        "[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-F59E0B?style=flat-square)](CONTRIBUTING.md)",
        "",
        "[Research map](#research-map) · [Start here](#start-here) · [Catalog](#catalog) · [Detailed metadata](README_DETAILED.md) · [Contribute](CONTRIBUTING.md)",
        "",
        "</div>",
        "",
        "> **What this list is for:** finding work that treats exploration as a first-class research variable—where it occurs, what signal identifies it, and which mechanism changes it.",
        "",
        "This list treats exploration as a **primary research variable**, not as a keyword. A paper must "
        "identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. "
        "Generic RL, agent, test-time-scaling, self-improvement, and diversity papers are excluded.",
        "",
        f"> Evidence snapshot: **{catalog['snapshot_date']}** · [Taxonomy design](docs/TAXONOMY.md) · [2026 curation notes](docs/CURATION_2026.md)",
        "",
        "## Research map",
        "",
        "Every paper has one home in the map; its tags then describe the research lens. Start with the track that matches your question, then use the tags to compare mechanisms across tracks.",
        "",
        "| Track | Best for |",
        "|---|---|",
        "| **[LLM Generation & Inference](#1-llm-generation--inference-exploration)** | Sampling, decoding, reasoning-path search, and output diversity without an RL update. |",
        "| **[Exploration for RLVR](#2-exploration-for-rlvr)** | Entropy collapse, rollout diversity, reward shaping, and policy-distribution control during training. |",
        "| **[Agentic Exploration](#3-agentic-exploration)** | Web, tool, GUI, knowledge-graph, embodied, or multi-agent trajectories. |",
        "| **[Understanding & Evaluation](#4-understanding-evaluation--benchmarks)** | Surveys, theory, metrics, benchmarks, and evidence about exploration. |",
        "",
        "<details>",
        "<summary><strong>How to read the tags</strong></summary>",
        "",
        "The former Token / Sequence / Policy sections are now `level` tags. Entropy, temperature, and noise belong to a broad distributional-and-stochastic family, but remain separate tags because they play different causal roles.",
        "",
        "| Tag dimension | Values |",
        "|---|---|",
        *[f"| **{name}** | {values} |" for name, values in TAG_DIMENSIONS],
        "",
        "</details>",
        "",
        "## Catalog at a glance",
        "",
        *statistics_table(papers),
        "",
        "## Start here",
        "",
    ]

    featured = sorted(
        (p for p in papers if p.get("featured")),
        key=lambda p: (p.get("date", ""), p["title"]),
        reverse=True,
    )
    for paper in featured:
        lines.append(
            f"- **[{paper['title']}]({paper['url']})** — {source_label(paper)} · "
            f"{AREA_LABELS[paper['primary_area']]} · {compact_tags(paper)}"
        )

    lines.extend(["", "<a id=\"catalog\"></a>", "", "## Catalog"])
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend(["", f"## {index}. {label}", "", f"> **Research focus.** {AREA_DESCRIPTIONS[area][0]}", "", AREA_DESCRIPTIONS[area][1], ""])
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        lines.extend(["| Published | Paper | Evidence | Research lens |", "|---|---|---|---|"])
        for paper in selected:
            date = paper.get("date", "")[:7] or str(paper.get("year", ""))
            lines.append(
                f"| {date} | [{paper['title']}]({paper['url']}) | "
                f"{source_label(paper)} | {compact_tags(paper)} |"
            )

    lines.extend(
        [
            "",
            "## Classical RL exploration — background only",
            "",
            "A deliberately small appendix of foundational non-LLM work. These papers are not counted in the curated LLM catalog.",
            "",
        ]
    )
    for paper in catalog["classics"]:
        lines.append(
            f"- **[{paper['title']}]({paper['url']})** ({paper['year']}) — {paper['note']}"
        )

    lines.extend(
        [
            "",
            "## Curation policy",
            "",
            "- One primary area per paper; multiple tags are encouraged.",
            "- Conference status is shown only when backed by an official venue page.",
            "- Automated discovery produces candidates, never accepted catalog entries.",
            "- Classical RL is limited to the short appendix above.",
            "- The public Markdown files are generated from [`data/papers.json`](data/papers.json).",
            "",
            "Run `python3 scripts/validate_catalog.py` and `python3 scripts/generate_catalog.py` after changing the registry.",
            "",
            "## License",
            "",
            "[CC BY 4.0](LICENSE)",
            "",
        ]
    )
    return "\n".join(lines)


def render_detailed(catalog: dict) -> str:
    papers = catalog["papers"]
    lines = [
        "# Awesome Exploration — Detailed Catalog",
        "",
        "> Generated from [`data/papers.json`](data/papers.json). Do not edit this file directly.",
        "",
        f"Evidence snapshot: **{catalog['snapshot_date']}** · {len(papers)} curated papers.",
        "",
    ]
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend([f"## {index}. {label}", "", *area_description_lines(area)])
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        for paper in selected:
            lines.append(
                f"- **[{paper['title']}]({paper['url']})** — {source_label(paper)}"
            )
            if paper.get("authors"):
                authors = paper["authors"]
                shown = ", ".join(authors[:8]) + (" et al." if len(authors) > 8 else "")
                lines.append(f"  - Authors: {shown}")
            lines.append(f"  - Type: `{paper['paper_type']}` · Date: `{paper.get('date', '')}`")
            for key, label_name in (
                ("phase", "Phase"),
                ("level", "Level"),
                ("signal", "Signal"),
                ("mechanism", "Mechanism"),
                ("problem", "Problem"),
                ("setting", "Setting"),
            ):
                values = paper.get(key, [])
                if values:
                    lines.append(f"  - {label_name}: " + " ".join(f"`{v}`" for v in values))
            if paper.get("rationale"):
                lines.append(f"  - {paper['rationale']}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    catalog = load_catalog()
    (ROOT / "README.md").write_text(render_readme(catalog), encoding="utf-8")
    (ROOT / "README_DETAILED.md").write_text(render_detailed(catalog), encoding="utf-8")
    print(f"Generated README.md and README_DETAILED.md from {len(catalog['papers'])} papers")


if __name__ == "__main__":
    main()
