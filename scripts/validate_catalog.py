#!/usr/bin/env python3
"""Validate the curated Awesome Exploration paper registry."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"

AREAS = {
    "llm-exploration",
    "rlvr-exploration",
    "agentic-exploration",
    "understanding-evaluation",
}
PAPER_TYPES = {"method", "analysis", "benchmark", "survey", "position"}
OFFICIAL_2026_HOSTS = {"aclanthology.org", "iclr.cc", "icml.cc"}
TAG_VALUES = {
    "phase": {"data-generation", "supervised-post-training", "rl-training", "inference", "test-time-adaptation", "continual/self-improvement"},
    "level": {"token", "response/sequence", "trajectory/action", "latent/representation", "policy-distribution", "data/task", "population/multi-policy"},
    "signal": {"entropy/probability", "uncertainty/confidence", "novelty/curiosity", "semantic-diversity", "coverage", "information-gain", "reward/advantage", "disagreement"},
    "mechanism": {"sampling/decoding", "temperature-control", "noise/perturbation", "regularization", "gradient-reshaping", "reward-shaping/intrinsic-reward", "tree-search/branching", "structured-search", "backtracking/resampling", "replay/memory", "curriculum/task-generation", "self-play/co-evolution", "ensemble/population"},
    "problem": {"entropy-collapse", "mode-collapse", "sparse-reward", "local-optimum", "capability-boundary", "long-horizon", "exploration-exploitation", "recovery/error-correction"},
    "setting": {"math", "code", "multimodal", "creative/open-ended", "web", "tool-use", "knowledge-graph", "embodied", "multi-agent"},
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def main() -> int:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    papers = catalog.get("papers", [])
    errors: list[str] = []
    seen_ids: dict[str, str] = {}
    seen_titles: dict[str, str] = {}
    seen_urls: dict[str, str] = {}

    for index, paper in enumerate(papers):
        label = paper.get("title", f"record #{index}")
        required = ("id", "title", "url", "date", "primary_area", "paper_type", "phase", "level")
        for field in required:
            if not paper.get(field):
                errors.append(f"{label}: missing {field}")
        if paper.get("primary_area") not in AREAS:
            errors.append(f"{label}: invalid primary_area {paper.get('primary_area')!r}")
        if paper.get("paper_type") not in PAPER_TYPES:
            errors.append(f"{label}: invalid paper_type {paper.get('paper_type')!r}")
        if not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", paper.get("date", "")):
            errors.append(f"{label}: date must be YYYY, YYYY-MM, or YYYY-MM-DD")
        if not paper.get("signal") and not paper.get("mechanism"):
            errors.append(f"{label}: needs at least one signal or mechanism tag")
        for dimension, allowed in TAG_VALUES.items():
            invalid = sorted(set(paper.get(dimension, [])) - allowed)
            if invalid:
                errors.append(f"{label}: invalid {dimension} tags {invalid}")

        paper_id = paper.get("id", "")
        if paper_id in seen_ids:
            errors.append(f"duplicate id: {paper_id} used by {label} and {seen_ids[paper_id]}")
        seen_ids[paper_id] = label

        title_key = normalize(paper.get("title", ""))
        if title_key in seen_titles:
            errors.append(f"duplicate title: {label} / {seen_titles[title_key]}")
        seen_titles[title_key] = label

        url = paper.get("url", "")
        url_key = url.rstrip("/").casefold()
        if url_key in seen_urls:
            errors.append(f"duplicate URL: {url} used by {label} and {seen_urls[url_key]}")
        seen_urls[url_key] = label
        if url and urlparse(url).scheme != "https":
            errors.append(f"{label}: URL must use HTTPS")

        if paper.get("source_group") == "conference-2026":
            host = urlparse(url).netloc.casefold()
            if host not in OFFICIAL_2026_HOSTS:
                errors.append(f"{label}: 2026 acceptance must use an official venue URL, got {host}")

    classic_titles = [normalize(p["title"]) for p in catalog.get("classics", [])]
    if len(classic_titles) != len(set(classic_titles)):
        errors.append("duplicate title in classical RL appendix")
    if len(classic_titles) > 8:
        errors.append("classical RL appendix must contain at most 8 papers")

    print(f"Validated {len(papers)} curated papers and {len(classic_titles)} classical references")
    print("Primary areas:", dict(sorted(Counter(p["primary_area"] for p in papers).items())))
    print(
        "2026 venues:",
        dict(
            sorted(
                Counter(
                    p.get("venue", "")
                    for p in papers
                    if p.get("source_group") == "conference-2026"
                ).items()
            )
        ),
    )
    if errors:
        print("\nValidation failures:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Catalog validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
