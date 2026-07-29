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
    "rlvr-policy-curriculum-exploration",
    "agentic-exploration",
    "agentic-training-exploration",
    "understanding-evaluation",
}
PAPER_TYPES = {"method", "analysis", "benchmark", "survey", "position"}
SUBTOPICS = {
    "llm-exploration": {"decoding-sampling", "search-deliberation", "representation-steering", "diversity-coverage"},
    "rlvr-policy-curriculum-exploration": {
        "data-selection-prompting",
        "task-synthesis-curriculum",
        "entropy-distribution",
        "credit-optimization",
        "reward-rollout",
        "replay-population",
        "capability-dynamics",
    },
    "agentic-exploration": {
        "web-tools-gui",
        "planning-interaction",
        "embodied-environments",
        "knowledge-memory",
    },
    "agentic-training-exploration": {
        "web-tools-gui",
        "planning-interaction",
        "embodied-environments",
        "knowledge-memory",
    },
    "understanding-evaluation": {"theory-training-dynamics", "benchmarks-metrics", "surveys-position", "capability-boundaries"},
}
OFFICIAL_2026_HOSTS = {"aclanthology.org", "iclr.cc", "icml.cc"}
TAG_VALUES = {
    "phase": {"data-generation", "supervised-post-training", "rl-training", "inference", "test-time-adaptation", "continual/self-improvement"},
    "level": {"token", "response/sequence", "trajectory/action", "latent/representation", "policy-distribution", "data/task", "population/multi-policy"},
    "signal": {"entropy/probability", "uncertainty/confidence", "novelty/curiosity", "semantic-diversity", "coverage", "information-gain", "reward/advantage", "disagreement"},
    "mechanism": {"sampling/decoding", "temperature-control", "noise/perturbation", "regularization", "gradient-reshaping", "reward-shaping/intrinsic-reward", "tree-search/branching", "structured-search", "backtracking/resampling", "replay/memory", "curriculum/task-generation", "self-play/co-evolution", "ensemble/population"},
    "problem": {"entropy-collapse", "mode-collapse", "sparse-reward", "local-optimum", "capability-boundary", "long-horizon", "exploration-exploitation", "recovery/error-correction"},
    "setting": {"math", "code", "multimodal", "creative/open-ended", "web", "tool-use", "knowledge-graph", "embodied", "multi-agent"},
}
NOTABILITY_VALUES = {"high-citation"}


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
        required = ("id", "title", "url", "date", "primary_area", "subtopic", "paper_type", "phase", "level")
        for field in required:
            if not paper.get(field):
                errors.append(f"{label}: missing {field}")
        if paper.get("primary_area") not in AREAS:
            errors.append(f"{label}: invalid primary_area {paper.get('primary_area')!r}")
        elif paper.get("subtopic") not in SUBTOPICS[paper["primary_area"]]:
            errors.append(f"{label}: invalid subtopic {paper.get('subtopic')!r} for {paper['primary_area']}")
        if paper.get("paper_type") not in PAPER_TYPES:
            errors.append(f"{label}: invalid paper_type {paper.get('paper_type')!r}")
        elif paper["paper_type"] == "method" and paper.get("primary_area") == "understanding-evaluation":
            errors.append(f"{label}: method papers must use an intervention context, not understanding-evaluation")
        elif paper["paper_type"] != "method" and paper.get("primary_area") != "understanding-evaluation":
            errors.append(f"{label}: evidence-only papers must use understanding-evaluation")
        if not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", paper.get("date", "")):
            errors.append(f"{label}: date must be YYYY, YYYY-MM, or YYYY-MM-DD")
        if not paper.get("signal") and not paper.get("mechanism"):
            errors.append(f"{label}: needs at least one signal or mechanism tag")
        for dimension, allowed in TAG_VALUES.items():
            invalid = sorted(set(paper.get(dimension, [])) - allowed)
            if invalid:
                errors.append(f"{label}: invalid {dimension} tags {invalid}")

        notability = paper.get("notability", [])
        if not isinstance(notability, list):
            errors.append(f"{label}: notability must be a list")
            notability = []
        invalid_notability = sorted(set(notability) - NOTABILITY_VALUES)
        if invalid_notability:
            errors.append(f"{label}: invalid notability values {invalid_notability}")
        citation_count = paper.get("citation_count")
        if citation_count is not None and (not isinstance(citation_count, int) or citation_count < 0):
            errors.append(f"{label}: citation_count must be a nonnegative integer")
        if "high-citation" in notability:
            if not isinstance(citation_count, int) or citation_count < 100:
                errors.append(f"{label}: high-citation requires citation_count >= 100")
            if not paper.get("citation_source"):
                errors.append(f"{label}: high-citation requires citation_source")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", paper.get("citation_checked", "")):
                errors.append(f"{label}: high-citation requires citation_checked in YYYY-MM-DD format")
        if paper.get("published_venue") is not None and not isinstance(paper["published_venue"], str):
            errors.append(f"{label}: published_venue must be a string")

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

    featured = [paper for paper in papers if paper.get("featured")]
    featured_ranks = [paper.get("featured_rank") for paper in featured]
    if len(featured) != 10:
        errors.append(f"Start Here must contain exactly 10 featured papers, got {len(featured)}")
    if sorted(featured_ranks, key=lambda rank: rank if isinstance(rank, int) else 10_000) != list(range(1, 11)):
        errors.append("featured papers must have unique featured_rank values from 1 through 10")
    for paper in papers:
        if paper.get("featured_rank") is not None and not paper.get("featured"):
            errors.append(f"{paper['title']}: featured_rank requires featured=true")

    print(f"Validated {len(papers)} curated papers and {len(classic_titles)} classical references")
    print("Primary categories:", dict(sorted(Counter(p["primary_area"] for p in papers).items())))
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
