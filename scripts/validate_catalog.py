#!/usr/bin/env python3
"""Validate the curated Awesome Exploration paper registry."""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
SCHEMA_VERSION = 2

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
SOURCE_GROUPS = {"conference-2026", "foundational-llm", "legacy-curated", "recent-curated", "verified-legacy"}
PUBLICATION_EVIDENCE = {"official", "venue-claim"}
OFFICIAL_HOSTS_BY_VENUE = {
    "ACL": {"aclanthology.org"},
    "ICLR": {"iclr.cc"},
    "ICML": {"icml.cc"},
}
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
    return re.sub(r"[^\w]+", " ", value).strip()


def valid_date(value: str) -> bool:
    """Accept catalog date formats while rejecting impossible calendar values."""
    if re.fullmatch(r"\d{4}", value):
        return True
    if re.fullmatch(r"\d{4}-\d{2}", value):
        return 1 <= int(value[-2:]) <= 12
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            date.fromisoformat(value)
        except ValueError:
            return False
        return True
    return False


def main() -> int:
    catalog = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    papers = catalog.get("papers", [])
    errors: list[str] = []
    if catalog.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"catalog: schema_version must be {SCHEMA_VERSION}")
    if not isinstance(papers, list):
        errors.append("catalog: papers must be a list")
        papers = []
    for field in ("snapshot_date", "citation_snapshot"):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", catalog.get(field, "")):
            errors.append(f"catalog: {field} must be in YYYY-MM-DD format")
    seen_ids: dict[str, str] = {}
    seen_titles: dict[str, str] = {}
    seen_urls: dict[str, str] = {}

    for index, paper in enumerate(papers):
        label = paper.get("title", f"record #{index}")
        required = ("id", "title", "url", "authors", "date", "venue", "rationale", "source_group", "primary_area", "subtopic", "paper_type", "phase", "level")
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
        if not valid_date(paper.get("date", "")):
            errors.append(f"{label}: date must be a valid YYYY, YYYY-MM, or YYYY-MM-DD value")
        if not isinstance(paper.get("authors"), list) or not paper.get("authors") or not all(
            isinstance(author, str) and author for author in paper.get("authors", [])
        ):
            errors.append(f"{label}: authors must be a non-empty list of names")
        if paper.get("source_group") not in SOURCE_GROUPS:
            errors.append(f"{label}: invalid source_group {paper.get('source_group')!r}")
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
        if "published_venue" in paper:
            errors.append(f"{label}: use publication metadata instead of published_venue")
        publication = paper.get("publication")
        if publication is not None:
            if not isinstance(publication, dict):
                errors.append(f"{label}: publication must be an object")
            else:
                for field in ("venue", "year", "track", "evidence"):
                    if not publication.get(field):
                        errors.append(f"{label}: publication missing {field}")
                if not isinstance(publication.get("year"), int):
                    errors.append(f"{label}: publication year must be an integer")
                if publication.get("evidence") not in PUBLICATION_EVIDENCE:
                    errors.append(f"{label}: invalid publication evidence {publication.get('evidence')!r}")
                official_url = publication.get("official_url")
                if publication.get("evidence") == "official":
                    if not official_url or urlparse(official_url).scheme != "https":
                        errors.append(f"{label}: official publication evidence needs an HTTPS official_url")
                    elif publication.get("venue") in OFFICIAL_HOSTS_BY_VENUE and urlparse(official_url).netloc.casefold() not in OFFICIAL_HOSTS_BY_VENUE[publication["venue"]]:
                        errors.append(f"{label}: official_url host does not match publication venue")
                    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", publication.get("verified_at", "")):
                        errors.append(f"{label}: official publication evidence needs verified_at")
                elif official_url or publication.get("verified_at"):
                    errors.append(f"{label}: venue-claim evidence cannot set official_url or verified_at")
        elif paper.get("source_group") == "conference-2026":
            errors.append(f"{label}: conference-2026 records require publication metadata")

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

        if "rationale_tags" not in paper:
            errors.append(f"{label}: missing rationale_tags")
        rationale_tags = paper.get("rationale_tags", [])
        if not isinstance(rationale_tags, list) or not all(
            isinstance(tag, str) for tag in rationale_tags
        ):
            errors.append(f"{label}: rationale_tags must be a list of tag IDs")
            rationale_tags = []
        recorded_tags = set().union(*(set(paper.get(dimension, [])) for dimension in TAG_VALUES))
        unrecorded_tags = sorted(set(rationale_tags) - recorded_tags)
        if unrecorded_tags:
            errors.append(f"{label}: rationale_tags must be recorded taxonomy tags {unrecorded_tags}")

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
                    f"{p['publication']['venue']} {p['publication']['year']}"
                    + (f" {p['publication']['track']}" if p["publication"]["track"] != "Conference" else "")
                    for p in papers
                    if p.get("publication", {}).get("year") == 2026
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
