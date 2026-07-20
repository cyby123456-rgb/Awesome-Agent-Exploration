#!/usr/bin/env python3
"""Build the public catalog from one canonical JSON source.

Run once with ``--bootstrap`` to migrate the legacy README, then use the
default command after editing ``data/papers.json``.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.json"
REVIEW_QUEUE = ROOT / "data" / "needs-verification.json"
README = ROOT / "README.md"
DETAILED = ROOT / "README_DETAILED.md"

ENTRY = re.compile(r"^- \*\*(.+?)\*\*(.*)$", re.MULTILINE)
ARXIV = re.compile(r"https://arxiv\.org/abs/([^\])\s]+)")
BADGE = re.compile(r"shields\.io/badge/([^)]*)")
HEADING = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)


def normalise(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def scope_for(badge_text: str) -> str:
    """Classify relevance conservatively; editorial review may override it."""
    if any(key in badge_text for key in ("random--exploration", "noisy--net", "feature--perturbation")):
        return "Context"
    if any(key in badge_text for key in ("related--topics", "semantic--diversity", "rl--limitations")):
        return "Adjacent"
    return "Core"


def bootstrap() -> None:
    legacy = README.read_text(encoding="utf-8")
    details = DETAILED.read_text(encoding="utf-8") if DETAILED.exists() else ""
    headings = [(m.start(), len(m.group(1)), m.group(2)) for m in HEADING.finditer(legacy)]

    def section_at(position: int) -> str:
        previous = "Unclassified"
        for start, level, heading in headings:
            if start >= position:
                break
            if level == 2:
                previous = heading
            elif level == 3:
                previous = f"{previous} / {heading}"
        return previous

    descriptions: dict[str, str] = {}
    for block in re.split(r"(?=^- \*\*)", details, flags=re.MULTILINE):
        match = ENTRY.match(block)
        if not match:
            continue
        summary = re.search(r"^  - \*(.+?)\*\s*$", block, re.MULTILINE)
        if summary and "..." not in summary.group(1):
            descriptions[normalise(match.group(1))] = summary.group(1)

    papers = []
    seen_titles: set[str] = set()
    for match in ENTRY.finditer(legacy):
        title, tail = match.groups()
        key = normalise(title)
        if key in seen_titles:
            continue
        seen_titles.add(key)
        block_end = legacy.find("\n- **", match.end())
        block = legacy[match.start() : block_end if block_end != -1 else len(legacy)]
        arxiv = ARXIV.search(block)
        badges = BADGE.findall(tail)
        papers.append(
            {
                "title": title,
                "section": section_at(match.start()),
                "scope": scope_for(" ".join(badges)),
                "arxiv": arxiv.group(1) if arxiv else None,
                "summary": descriptions.get(key),
            }
        )

    by_arxiv: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        if paper["arxiv"]:
            by_arxiv[paper["arxiv"]].append(paper)
    queue = []
    for arxiv, group in by_arxiv.items():
        names = {normalise(item["title"]) for item in group}
        if len(names) > 1:
            for item in group:
                queue.append({"title": item["title"], "legacy_arxiv": arxiv, "reason": "Conflicting legacy arXiv mapping"})
                item["arxiv"] = None

    public_papers = []
    for item in papers:
        if item["arxiv"]:
            public_papers.append(item)
        elif not any(entry["title"] == item["title"] for entry in queue):
            queue.append({"title": item["title"], "legacy_arxiv": None, "reason": "Missing primary-source link"})

    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps({"schema_version": 1, "papers": public_papers}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    REVIEW_QUEUE.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def link(paper: dict) -> str:
    if paper.get("arxiv"):
        return f"[arXiv:{paper['arxiv']}](https://arxiv.org/abs/{paper['arxiv']})"
    return "Source under verification"


def quarantine_missing() -> None:
    """One-time migration: remove source-less legacy records from public data."""
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    queue = json.loads(REVIEW_QUEUE.read_text(encoding="utf-8")) if REVIEW_QUEUE.exists() else []
    public = []
    queued_titles = {item["title"] for item in queue}
    for paper in payload["papers"]:
        if paper.get("arxiv"):
            public.append(paper)
        elif paper["title"] not in queued_titles:
            queue.append({"title": paper["title"], "legacy_arxiv": None, "reason": "Missing primary-source link"})
    DATA.write_text(json.dumps({"schema_version": 1, "papers": public}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    REVIEW_QUEUE.write_text(json.dumps(queue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_sections() -> None:
    """Repair section paths produced by the legacy heading migration."""
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    for paper in payload["papers"]:
        parts = [part.strip() for part in re.split(r" / (?=\d+(?:\.\d+)+\s)", paper["section"])]
        paper["section"] = parts[0] if len(parts) == 1 else f"{parts[0]} / {parts[-1]}"
        # Earlier migration runs used a plain string split, which damaged these
        # two headings because their human-readable names contain slashes.
        if paper["section"].startswith("5. Semantic-Ignorant Exploration (Entropy / "):
            suffix = paper["section"].split(" / ")[-1]
            paper["section"] = "5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise)"
            if suffix.startswith("5."):
                paper["section"] += f" / {suffix}"
        if paper["section"] == "6. Exploration in Specific Scenarios / Code)":
            paper["section"] = "6. Exploration in Specific Scenarios / 6.1 RLVR (Math / Code)"
    overrides = {
        "From Trial-and-Error to Improvement: A Systematic Analysis of LLM Exploration Mechanisms in RLVR": "Core",
        "Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining": "Context",
    }
    for paper in payload["papers"]:
        if paper["title"] in overrides:
            paper["scope"] = overrides[paper["title"]]
    DATA.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def render(detailed: bool) -> str:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    papers = payload["papers"]
    sections: dict[str, list[dict]] = defaultdict(list)
    for paper in papers:
        sections[paper["section"]].append(paper)

    title = "Detailed View" if detailed else "List View"
    switch = "[List View](README.md)" if detailed else "[Detailed View](README_DETAILED.md)"
    lines = [
        "# Awesome-Exploration",
        "",
        f"**{title}** · {switch}",
        "",
        "A curated, evidence-linked reading list on **exploration mechanisms in RL for LLMs**.",
        "",
        "> **Scope.** Core entries directly propose, measure, or analyze exploration in RL-for-LLM training or inference. "
        "Adjacent entries supply essential diversity, evaluation, or capability-boundary context. Context entries are useful precedents "
        "from broader RL or applications, not evidence for an RL4LLM claim.",
        "",
        "## How to use this catalog",
        "",
        "- **Core** — direct RL4LLM exploration work.",
        "- **Adjacent** — closely related evaluation, diversity, or capability-boundary work.",
        "- **Context** — transferable ideas from other RL settings; interpret separately.",
        "- Every public entry has one unique primary-source identifier. Ambiguous or source-less legacy records are held in `data/needs-verification.json` until verified.",
        "",
        "## Inclusion policy",
        "",
        "We include work with a primary-source link and a clear relationship to exploration: expanding the search space, controlling exploration/exploitation, measuring diversity or coverage, or testing whether exploration improves capability. Papers that merely use RL or LLMs without that connection belong in Context or are excluded.",
        "",
        "## Contributing",
        "",
        "Please open an issue or PR with the paper title, primary link, relevant section, scope label, and a one-sentence rationale. Edit `data/papers.json`; the two README files are generated.",
    ]
    for section, items in sections.items():
        lines.extend(["", f"## {section}", ""])
        for paper in items:
            lines.append(f"- **{paper['title']}** — `{paper['scope']}` · {link(paper)}")
            if detailed and paper.get("summary"):
                lines.append(f"  - {paper['summary']}")
    lines.extend(["", "## License", "", "This list is licensed under [CC BY 4.0](LICENSE.md).", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--quarantine-missing", action="store_true")
    parser.add_argument("--normalize-sections", action="store_true")
    args = parser.parse_args()
    if args.bootstrap:
        bootstrap()
    if args.quarantine_missing:
        quarantine_missing()
    if args.normalize_sections:
        normalize_sections()
    README.write_text(render(detailed=False), encoding="utf-8")
    DETAILED.write_text(render(detailed=True), encoding="utf-8")


if __name__ == "__main__":
    main()
