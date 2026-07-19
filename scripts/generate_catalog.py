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

AREA_DESCRIPTIONS = {
    "llm-exploration": (
        "Exploration during generation and inference: sampling, decoding, semantic "
        "diversity, latent steering, and test-time search without requiring RL training."
    ),
    "rlvr-exploration": (
        "Exploration during RL/RLVR post-training: entropy collapse, token and rollout "
        "diversity, intrinsic rewards, policy-distribution control, and capability expansion."
    ),
    "agentic-exploration": (
        "Exploration in interactive environments: web, tool, GUI, knowledge-graph and "
        "embodied search, long-horizon trajectories, memory, and self-play."
    ),
    "understanding-evaluation": (
        "Empirical, theoretical, survey, and benchmark work that measures exploration, "
        "diversity, training dynamics, or capability boundaries."
    ),
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
        "# Awesome Exploration",
        "",
        "> A curated reading list on exploration in language-model generation, RLVR, and agents.",
        "",
        "This list treats exploration as a **primary research variable**, not as a keyword. A paper must "
        "identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. "
        "Generic RL, agent, test-time-scaling, self-improvement, and diversity papers are excluded.",
        "",
        f"**Evidence snapshot:** {catalog['snapshot_date']} · "
        "[Taxonomy design](docs/TAXONOMY.md) · [Detailed metadata](README_DETAILED.md) · "
        "[2026 curation notes](docs/CURATION_2026.md) · "
        "[Contribution guide](CONTRIBUTING.md)",
        "",
        "## Taxonomy",
        "",
        "Each paper has exactly one primary area and may carry multiple orthogonal tags. "
        "See [Taxonomy design](docs/TAXONOMY.md) for the decision rules, meaning of each dimension, "
        "and the rationale for separating signals such as entropy from mechanisms such as temperature or noise.",
        "",
        "| Primary area | Definition |",
        "|---|---|",
        *[f"| **{AREA_LABELS[a]}** | {AREA_DESCRIPTIONS[a]} |" for a in AREA_LABELS],
        "",
        "The former Token / Sequence / Policy sections are now `level` tags. Entropy, temperature, and "
        "noise are grouped under distributional/stochastic exploration while remaining distinct tags.",
        "",
        "| Tag dimension | Values |",
        "|---|---|",
        *[f"| **{name}** | {values} |" for name, values in TAG_DIMENSIONS],
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

    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend(["", f"## {index}. {label}", "", AREA_DESCRIPTIONS[area], ""])
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        lines.extend(["| Date | Paper | Source | Tags |", "|---|---|---|---|"])
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
        lines.extend([f"## {index}. {label}", "", AREA_DESCRIPTIONS[area], ""])
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
