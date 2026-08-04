#!/usr/bin/env python3
"""Generate the public Markdown views from the curated paper registry."""

from __future__ import annotations

import json
from collections import Counter
from html import escape
from pathlib import Path
from urllib.parse import quote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.json"
RESEARCH_MAP_PATH = ROOT / "assets" / "research-map.svg"

AREA_LABELS = {
    "llm-exploration": "Exploration for LLM Generation & Inference",
    "rlvr-policy-curriculum-exploration": "Exploration for RLVR, Policy & Curriculum",
    "agentic-exploration": "Agentic Exploration",
    "agentic-training-exploration": "Agentic Exploration for Training",
    "understanding-evaluation": "Understanding, Evaluation & Benchmarks",
}

AREA_ANCHORS = {
    "llm-exploration": "category-1",
    "rlvr-policy-curriculum-exploration": "category-2",
    "agentic-exploration": "category-3",
    "agentic-training-exploration": "category-4",
    "understanding-evaluation": "category-5",
}

AREA_SUMMARIES = {
    "llm-exploration": "Exploration during language-model generation and inference, without RL policy updates as the central contribution.",
    "rlvr-policy-curriculum-exploration": "Exploration in RLVR and policy learning, where curricula, rollouts, rewards, or updates change what the model discovers.",
    "agentic-exploration": "Exploration by language agents acting at inference time over states, tools, observations, and long-horizon trajectories.",
    "agentic-training-exploration": "Agent-environment exploration used to generate experience, construct training tasks, or improve an agent policy.",
    "understanding-evaluation": "Work that measures, explains, surveys, or benchmarks exploration rather than primarily introducing an intervention.",
}

RESEARCH_MAP_TRACKS = [
    {
        "area": "llm-exploration",
        "eyebrow": "01 / GENERATION",
        "title": ["Exploration for LLM Generation & Inference"],
        "keywords": "sampling  |  search  |  diversity",
        "color": "#6E8FB8",
    },
    {
        "area": "rlvr-policy-curriculum-exploration",
        "eyebrow": "02 / POLICY LEARNING",
        "title": ["Exploration for RLVR, Policy & Curriculum"],
        "keywords": "curriculum  |  reward  |  policy",
        "color": "#B07A68",
    },
    {
        "area": "agentic-exploration",
        "eyebrow": "03 / INTERACTION",
        "title": ["Agentic Exploration"],
        "keywords": "tools  |  planning  |  memory  |  worlds",
        "color": "#8B80B6",
    },
    {
        "area": "agentic-training-exploration",
        "eyebrow": "04 / AGENT LEARNING",
        "title": ["Agentic Exploration for Training"],
        "keywords": "experience  |  tasks  |  policy updates",
        "color": "#5F8F8B",
    },
    {
        "area": "understanding-evaluation",
        "eyebrow": "05 / EVIDENCE",
        "title": ["Understanding, Evaluation & Benchmarks"],
        "keywords": "theory  |  metrics  |  benchmarks",
        "color": "#B06D73",
    },
]

AREA_DESCRIPTIONS = {
    "llm-exploration": [
        "This category covers exploration that happens while a language model is generating or selecting candidate outputs, rather than through a reinforcement-learning update. Typical examples include sampling and decoding strategies, self-consistency, semantic-diversity methods, latent-state steering, and tree or graph search at inference time.",
        "The central question is how to search a model's existing generative distribution more broadly, safely, or efficiently. Papers belong here when the main contribution improves or analyzes candidate generation, reasoning-path search, or output diversity without making RL post-training the core mechanism.",
    ],
    "rlvr-policy-curriculum-exploration": [
        "This category covers exploration inside RLVR and policy-learning loops: constructing curricula, collecting rollouts, shaping rewards and advantages, and updating a language-model policy.",
        "The central question is how learning changes what the model can discover. Entropy control, capability expansion, replay, self-play, co-evolution, data selection, and task synthesis belong here when they improve a model policy without making external agent-environment interaction the defining loop.",
    ],
    "agentic-exploration": [
        "This category covers language agents that explore an external or persistent environment at inference or test time: webpages, tools, GUIs, knowledge graphs, games, embodied worlds, or multi-agent settings.",
        "The explored object is a trajectory of states, actions, observations, tool calls, and accumulated memory. Papers belong here when planning, recovery, information seeking, or environment coverage is the main contribution and no training update is central.",
    ],
    "agentic-training-exploration": [
        "This category covers agent-environment exploration whose purpose is to create training experience, synthesize interactive tasks, or update and improve an agent policy.",
        "It includes agentic RL, exploration-aware policy optimization, self-play training, autonomous experience collection, and environment generation. The defining feature is that external interaction supplies or structures the learning signal rather than serving only as test-time search.",
    ],
    "understanding-evaluation": [
        "This category collects empirical analyses, theoretical accounts, surveys, metrics, and benchmarks that help the field understand exploration. Rather than primarily proposing a new exploration intervention, these works measure diversity, characterize training dynamics, evaluate capability boundaries, or establish a shared vocabulary and test bed.",
        "They are essential for judging whether a method genuinely improves exploration instead of merely changing accuracy or sampling behavior. Keeping them separate makes the evidence about a phenomenon easy to distinguish from methods designed to change it.",
    ],
}

AREA_BOTTLENECKS = {
    "llm-exploration": (
        "The central challenge is still the diversity-quality-efficiency trade-off: broader sampling and search can improve coverage while rapidly increasing inference cost or admitting low-quality paths. Results are also hard to compare because gains from exploration are often entangled with extra compute, verifier strength, and model scale, while semantic and latent diversity lack reliable task-independent measures."
    ),
    "rlvr-policy-curriculum-exploration": (
        "Training-time exploration remains vulnerable to entropy collapse, biased or sparse rewards, unstable credit assignment, and curricula that overfit to what a verifier can already recognize. A key open question is whether an intervention creates genuinely new capability or only redistributes probability mass over existing behavior; replay, self-play, and population methods add further stability, data-quality, and compute challenges."
    ),
    "agentic-exploration": (
        "Long horizons, partial observability, and compounding action errors make efficient coverage and reliable recovery difficult, especially when tools or environments change. Current benchmarks often simplify feedback and reset conditions, leaving unresolved questions around realistic exploration cost, safe interaction, memory quality, reproducibility, and whether improvements transfer beyond a narrow environment."
    ),
    "agentic-training-exploration": (
        "Agent-generated trajectories are expensive, correlated, and vulnerable to reward hacking or compounding environment errors, while successful experience is often too sparse to train on directly. Open problems include reliable credit across long interactions, balancing diverse experience with learnability, preventing self-training feedback loops, and transferring policies across tools and environments."
    ),
    "understanding-evaluation": (
        "The field lacks standardized measures that separate useful exploration from superficial diversity, additional sampling compute, or benchmark-specific variance. Static and contamination-prone benchmarks, limited cross-model replication, and weak causal links between token-level statistics, training dynamics, and downstream capability make it difficult to identify which interventions genuinely expand exploration."
    ),
}

SUBTOPIC_LABELS = {
    "llm-exploration": {
        "decoding-sampling": "Decoding & Sampling",
        "search-deliberation": "Search & Deliberation",
        "representation-steering": "Representation & Latent Steering",
        "diversity-coverage": "Diversity & Coverage",
    },
    "rlvr-policy-curriculum-exploration": {
        "entropy-distribution": "Entropy & Distribution Control",
        "credit-optimization": "Credit Assignment & Optimization",
        "reward-rollout": "Reward & Rollout Shaping",
        "replay-population": "Replay, Population & Self-Improvement",
        "capability-dynamics": "Capability Expansion & Training Interventions",
        "data-selection-prompting": "Data Selection & Prompt Exploration",
        "task-synthesis-curriculum": "Task Synthesis & Curriculum",
    },
    "agentic-exploration": {
        "web-tools-gui": "Web, Tools & GUI",
        "planning-interaction": "Planning & Interactive Search",
        "embodied-environments": "Embodied & Simulated Environments",
        "knowledge-memory": "Knowledge & Memory-Guided Exploration",
    },
    "agentic-training-exploration": {
        "web-tools-gui": "Web, Tools & GUI Training",
        "planning-interaction": "Agentic Policy Learning",
        "embodied-environments": "Embodied & Simulated Training",
        "knowledge-memory": "Memory-Augmented Agent Training",
    },
    "understanding-evaluation": {
        "surveys-position": "Surveys & Position Papers",
        "theory-training-dynamics": "Theory & Training Dynamics",
        "capability-boundaries": "Capability Boundaries",
        "benchmarks-metrics": "Benchmarks & Metrics",
    },
}

SUBTOPIC_SUMMARIES = {
    "llm-exploration": {
        "decoding-sampling": "Methods that broaden candidate generation at inference time, with probability shaping, temperature, and sampling strategy as the key levers for balancing diversity, quality, and cost.",
        "search-deliberation": "Methods that explore multi-step reasoning paths through branching, resampling, planning, or verification, with search-budget allocation and path quality as the central concerns.",
        "representation-steering": "Methods that diversify generation by steering activations, embeddings, or latent states, focusing on controllable variation beyond output-level sampling.",
        "diversity-coverage": "Methods that counter mode collapse and expand semantic coverage, emphasizing how novelty and breadth can improve without sacrificing correctness or coherence.",
    },
    "rlvr-policy-curriculum-exploration": {
        "entropy-distribution": "Work that analyzes or controls policy entropy and token probabilities during RL, aiming to preserve useful distributional support while preventing premature collapse.",
        "credit-optimization": "Methods that reshape rewards, advantages, or gradients so exploratory behavior receives an informative learning signal, with stable and precise credit assignment as the key challenge.",
        "reward-rollout": "Methods that alter rollout collection, reward shaping, intrinsic bonuses, or resampling to elicit more varied and informative training trajectories.",
        "replay-population": "Learning systems that use replay, self-play, co-evolution, ensembles, or policy populations to retain useful experience and expand behavioral coverage across updates.",
        "capability-dynamics": "Training interventions designed to expand or stabilize model capabilities, focusing on generalization boundaries and genuine capability growth rather than evidence-only analysis.",
        "data-selection-prompting": "Methods that select, prioritize, or prompt training examples, using informativeness, uncertainty, and coverage to decide which data is most valuable next.",
        "task-synthesis-curriculum": "Methods that generate and sequence tasks across difficulty levels, with adaptive progression, task diversity, and learnability as the main curriculum concerns.",
    },
    "agentic-exploration": {
        "web-tools-gui": "Agents that explore websites, tools, and graphical interfaces, where action grounding, partial observability, tool choice, and recovery from failed interactions are central.",
        "planning-interaction": "Agents that search over multi-step action plans while interacting with an environment, focusing on long-horizon feedback, replanning, and efficient state-space coverage.",
        "embodied-environments": "Agents that explore physical or simulated worlds, with spatial reasoning, world-model learning, action consequences, and sample-efficient coverage as key issues.",
        "knowledge-memory": "Agents that traverse knowledge graphs or use accumulated memory to guide future actions, emphasizing relation-aware search, timely recall, and experience-grounded planning.",
    },
    "agentic-training-exploration": {
        "web-tools-gui": "Training methods that collect or synthesize experience in websites, tools, and graphical interfaces, with task diversity, feedback quality, and transfer as the central concerns.",
        "planning-interaction": "Methods that train agent policies from exploratory multi-step trajectories, focusing on long-horizon credit, stable optimization, and useful behavioral diversity.",
        "embodied-environments": "Training methods that explore physical or simulated worlds, where noisy observations, sparse rewards, environment coverage, and sample efficiency shape the learning problem.",
        "knowledge-memory": "Methods that combine exploratory experience with replay or memory during agent training, emphasizing which trajectories to retain, retrieve, and learn from.",
    },
    "understanding-evaluation": {
        "theory-training-dynamics": "Theoretical and empirical work that explains why exploration changes during training, isolating causal mechanisms behind entropy, diversity, optimization, and policy dynamics.",
        "benchmarks-metrics": "Benchmarks and metrics that quantify exploration quality, emphasizing valid measures of diversity, coverage, efficiency, reproducibility, and downstream utility.",
        "surveys-position": "Surveys and position papers that organize the field's definitions, evidence, trade-offs, and open problems into a coherent research agenda.",
        "capability-boundaries": "Work that tests whether exploration reaches beyond a model's existing competence, distinguishing genuine capability expansion from redistribution, memorization, or extra sampling.",
    },
}

TAG_DIMENSIONS = [
    ("Phase", "data generation; supervised post-training; RL training; inference; test-time adaptation; continual/self-improvement"),
    ("Level", "token; response/sequence; trajectory/action; latent/representation; policy distribution; data/task; population"),
    ("Signal", "entropy/probability; uncertainty/confidence; novelty/curiosity; semantic diversity; coverage; information gain; reward/advantage; disagreement"),
    ("Mechanism", "sampling/decoding; temperature control; noise/perturbation; regularization; gradient reshaping; intrinsic reward; structured/tree search; replay/memory; curriculum; self-play; ensemble/population"),
    ("Problem", "entropy or mode collapse; sparse reward; local optimum; capability boundary; long horizon; exploration/exploitation; recovery"),
    ("Setting", "math; code; multimodal; creative/open-ended; web; tool use; knowledge graph; embodied; multi-agent"),
]

BADGE_COLORS = {
    "phase": "6E8FB8",
    "level": "8B80B6",
    "signal": "5F8F8B",
    "mechanism": "8C8960",
    "problem": "B06D73",
    "setting": "718B75",
}

TOP_TIER_VENUE_PREFIXES = (
    "AAAI",
    "ACL",
    "ASE",
    "EMNLP",
    "ICLR",
    "ICML",
    "ICRA",
    "ICSE",
    "IJCAI",
    "NEURIPS",
    "TMLR",
    "ARTIFICIAL INTELLIGENCE",
    "IEEE TRANSACTIONS ON CYBERNETICS",
)
PEER_REVIEWED_2026_VENUE_PREFIXES = ("ACL 2026", "ICLR 2026", "ICML 2026")

# Muted, value-specific colors keep neighboring papers distinguishable without
# turning the catalog into a wall of high-saturation badges.
TAG_VALUE_COLORS = {
    ("phase", "data-generation"): "5F8F8B",
    ("phase", "supervised-post-training"): "6E8FB8",
    ("phase", "rl-training"): "7284C7",
    ("phase", "inference"): "5B9AB5",
    ("phase", "test-time-adaptation"): "7E8DBD",
    ("phase", "continual/self-improvement"): "789B8A",
    ("level", "token"): "8B80B6",
    ("level", "response/sequence"): "8278A9",
    ("level", "trajectory/action"): "8F7DAF",
    ("level", "latent/representation"): "777FA8",
    ("level", "policy-distribution"): "8C719E",
    ("level", "data/task"): "9A7F9C",
    ("level", "population/multi-policy"): "A07593",
    ("signal", "entropy/probability"): "4F8D88",
    ("signal", "uncertainty/confidence"): "5B8E9E",
    ("signal", "novelty/curiosity"): "6B9275",
    ("signal", "semantic-diversity"): "538F7D",
    ("signal", "coverage"): "78935F",
    ("signal", "information-gain"): "5E8C97",
    ("signal", "reward/advantage"): "8C8960",
    ("signal", "disagreement"): "8B7A9C",
    ("mechanism", "sampling/decoding"): "5D8CA8",
    ("mechanism", "temperature-control"): "6B84AD",
    ("mechanism", "noise/perturbation"): "8176A8",
    ("mechanism", "regularization"): "737FB0",
    ("mechanism", "gradient-reshaping"): "B07A68",
    ("mechanism", "reward-shaping/intrinsic-reward"): "6E946B",
    ("mechanism", "tree-search/branching"): "A56F7A",
    ("mechanism", "structured-search"): "568D83",
    ("mechanism", "backtracking/resampling"): "8E759D",
    ("mechanism", "replay/memory"): "6F8093",
    ("mechanism", "curriculum/task-generation"): "A08B5F",
    ("mechanism", "self-play/co-evolution"): "A36F8A",
    ("mechanism", "ensemble/population"): "8774A5",
    ("problem", "entropy-collapse"): "B06D73",
    ("problem", "mode-collapse"): "B57676",
    ("problem", "sparse-reward"): "B1846A",
    ("problem", "local-optimum"): "A77878",
    ("problem", "capability-boundary"): "9A738A",
    ("problem", "long-horizon"): "8E7D6D",
    ("problem", "exploration-exploitation"): "A27C63",
    ("problem", "recovery/error-correction"): "9B6F75",
    ("setting", "math"): "6D8CAB",
    ("setting", "code"): "697F9D",
    ("setting", "multimodal"): "8176A5",
    ("setting", "creative/open-ended"): "A2778D",
    ("setting", "web"): "5B8B86",
    ("setting", "tool-use"): "718B75",
    ("setting", "knowledge-graph"): "7B8466",
    ("setting", "embodied"): "9A7D68",
    ("setting", "multi-agent"): "8D7595",
}

REPRESENTATIVE_TAG_LIMIT = 3


def load_catalog() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def area_description_lines(area: str) -> list[str]:
    """Render a compact, consistent overview for each research category."""
    return [
        "| Research lens | Summary |",
        "|---|---|",
        f"| **🧭 Scope** | {AREA_DESCRIPTIONS[area][0]} |",
        f"| **🎯 Core question** | {AREA_DESCRIPTIONS[area][1]} |",
        f"| **🚧 Open challenges** | {AREA_BOTTLENECKS[area]} |",
        "",
    ]


def tag_badge(dimension: str, value: str) -> str:
    """Render taxonomy metadata as a compact, color-coded Shields badge."""
    label = quote(dimension, safe="")
    # Shields' legacy badge route uses hyphens as field separators. Escape a
    # hyphen inside the message by doubling it; otherwise values such as
    # ``capability-boundary`` render a red "404 / badge not found" SVG.
    message = quote(value, safe="").replace("-", "--")
    color = TAG_VALUE_COLORS.get((dimension, value), BADGE_COLORS[dimension])
    return (
        f"![{dimension}: {value}]"
        f"(https://img.shields.io/badge/{label}-{message}-{color}?style=flat-square)"
    )


def representative_tags(paper: dict) -> str:
    """Render at most three tags that best distinguish a paper in the catalog."""
    values: list[tuple[str, str]] = []

    # Phase, signal, and mechanism answer when, what guides, and how. Prefer
    # one of each so repeated values in one dimension do not crowd the view.
    for dimension in ("phase", "signal", "mechanism"):
        if paper.get(dimension):
            values.append((dimension, paper[dimension][0]))

    # Some papers do not declare all three preferred dimensions. Fill the
    # remaining slots with the most useful available context.
    for dimension in ("level", "problem", "setting", "phase", "signal", "mechanism"):
        for value in paper.get(dimension, []):
            candidate = (dimension, value)
            if candidate not in values:
                values.append(candidate)
            if len(values) == REPRESENTATIVE_TAG_LIMIT:
                break
        if len(values) == REPRESENTATIVE_TAG_LIMIT:
            break

    return " ".join(
        tag_badge(dimension, value)
        for dimension, value in values[:REPRESENTATIVE_TAG_LIMIT]
    )


def papers_by_subtopic(papers: list[dict], area: str) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {key: [] for key in SUBTOPIC_LABELS[area]}
    for paper in papers:
        groups[paper["subtopic"]].append(paper)
    return {key: values for key, values in groups.items() if values}


def paper_count_label(count: int) -> str:
    """Format catalog section counts with correct singular and plural nouns."""
    return f"{count} {'paper' if count == 1 else 'papers'}"


def subtopic_anchor(area: str, subtopic: str) -> str:
    """Build stable anchors that do not depend on generated paper counts."""
    return f"{AREA_ANCHORS[area]}-{subtopic}"


def catalog_table_of_contents(papers: list[dict]) -> list[str]:
    lines = []
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.append(f"{index}. [{label}](#{AREA_ANCHORS[area]})")
        area_papers = [paper for paper in papers if paper["primary_area"] == area]
        for subtopic, grouped in papers_by_subtopic(area_papers, area).items():
            lines.append(
                f"   - [{SUBTOPIC_LABELS[area][subtopic]}]"
                f"(#{subtopic_anchor(area, subtopic)}) · {paper_count_label(len(grouped))}"
            )
    return lines


def has_top_tier_venue(paper: dict) -> bool:
    """Identify papers with a recognized top-tier publication venue."""
    venue = (paper.get("published_venue") or paper.get("venue") or "").upper()
    return venue.startswith(TOP_TIER_VENUE_PREFIXES)


def has_high_citation(paper: dict) -> bool:
    """Identify papers with a recorded high-citation assessment."""
    return "high-citation" in paper.get("notability", [])


def notability_marker(paper: dict) -> str:
    markers = []
    if has_top_tier_venue(paper):
        markers.append("🏆")
    if has_high_citation(paper):
        markers.append("⭐")
    return f"{' '.join(markers)} " if markers else ""


def source_label(paper: dict) -> str:
    parsed_url = urlparse(paper["url"])
    if parsed_url.netloc.lower() in {"arxiv.org", "www.arxiv.org"}:
        arxiv_id = parsed_url.path.removeprefix("/abs/").strip("/")
        if arxiv_id:
            if paper.get("published_venue"):
                return f"{paper['published_venue']} · arXiv `{arxiv_id}`"
            return f"arXiv `{arxiv_id}`"
    venue = paper.get("venue") or "Preprint"
    if paper.get("source_group") == "conference-2026":
        return f"**{venue}**"
    return venue


def statistics_table(papers: list[dict]) -> list[str]:
    area_counts = Counter(p["primary_area"] for p in papers)
    accepted = Counter(
        p.get("published_venue") or p["venue"]
        for p in papers
        if (p.get("published_venue") or p.get("venue") or "").startswith(
            PEER_REVIEWED_2026_VENUE_PREFIXES
        )
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


def render_research_map(catalog: dict) -> str:
    """Render a compact, data-driven overview of the five research categories."""
    papers = catalog["papers"]
    area_counts = Counter(paper["primary_area"] for paper in papers)
    maximum = max(area_counts.values())
    rows = []

    for index, track in enumerate(RESEARCH_MAP_TRACKS, start=1):
        count = area_counts[track["area"]]
        percentage = count / len(papers) * 100
        y = 142 + (index - 1) * 57
        bar_width = max(12, round(540 * count / maximum, 1))
        title = " ".join(track["title"])
        color = track["color"]
        rows.append(
            f'<g aria-label="{escape(AREA_LABELS[track["area"]])}: {count} papers, '
            f'{percentage:.1f} percent of the catalog">'
            f'<circle cx="45" cy="{y - 4}" r="16" fill="{color}" />'
            f'<text x="45" y="{y + 1}" class="track-index" text-anchor="middle">'
            f'{index:02d}</text>'
            f'<text x="76" y="{y - 4}" class="track-title">{escape(title)}</text>'
            f'<text x="76" y="{y + 17}" class="track-keywords">'
            f'{escape(track["keywords"])}</text>'
            f'<rect x="490" y="{y - 14}" width="540" height="14" rx="7" '
            f'class="bar-track" />'
            f'<rect x="490" y="{y - 14}" width="{bar_width:g}" height="14" rx="7" '
            f'fill="{color}" />'
            f'<rect x="1038" y="{y - 21}" width="80" height="30" rx="15" '
            f'class="count-chip" />'
            f'<text x="1078" y="{y - 1}" class="track-count" text-anchor="middle">'
            f'{count}</text>'
            f'<text x="1168" y="{y - 1}" class="track-share" text-anchor="end">'
            f'{percentage:.1f}%</text>'
            f'<line x1="30" y1="{y + 31}" x2="1170" y2="{y + 31}" class="row-line" />'
            f'</g>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="470" viewBox="0 0 1200 470" role="img" aria-labelledby="map-title map-description">
  <title id="map-title">Awesome Exploration research map</title>
  <desc id="map-description">{len(papers)} curated papers organized into five research categories, with current paper counts and key topics for each category.</desc>
  <defs>
    <linearGradient id="map-background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FAFBFC" />
      <stop offset="1" stop-color="#F4F7F8" />
    </linearGradient>
    <style>
      text {{ font-family: "Avenir Next", "Trebuchet MS", sans-serif; }}
      .map-heading {{ fill: #172033; font-size: 23px; font-weight: 500; letter-spacing: 0.7px; }}
      .map-subtitle {{ fill: #667085; font-size: 13px; font-weight: 400; }}
      .map-total {{ fill: #172033; font-size: 34px; font-weight: 500; }}
      .map-total-label {{ fill: #667085; font-size: 11px; font-weight: 500; letter-spacing: 1.3px; }}
      .track-index {{ fill: #FFFFFF; font-size: 10px; font-weight: 500; letter-spacing: 0.6px; }}
      .track-title {{ fill: #172033; font-size: 17px; font-weight: 500; }}
      .track-keywords {{ fill: #7A8495; font-size: 11px; font-weight: 400; }}
      .count-chip {{ fill: #172033; }}
      .track-count {{ fill: #FFFFFF; font-size: 15px; font-weight: 700; }}
      .track-share {{ fill: #475467; font-size: 12px; font-weight: 600; }}
      .bar-track {{ fill: #E5E9EF; }}
      .row-line {{ stroke: #E3E7EC; stroke-width: 1; }}
      .footer {{ fill: #8993A4; font-size: 10px; font-weight: 500; letter-spacing: 1.2px; }}
    </style>
  </defs>
  <rect x="5" y="5" width="1190" height="460" rx="24" fill="url(#map-background)" />
  <text x="36" y="48" class="map-heading">Exploration research landscape</text>
  <text x="36" y="73" class="map-subtitle">Five research categories across large language models, agents, training, and evaluation</text>
  <text x="1138" y="48" class="map-total" text-anchor="end">{len(papers)}</text>
  <text x="1138" y="70" class="map-total-label" text-anchor="end">CURATED PAPERS</text>
  <line x1="30" y1="95" x2="1170" y2="95" class="row-line" />
  {''.join(rows)}
  <text x="600" y="450" class="footer" text-anchor="middle">FIVE RESEARCH CATEGORIES  /  COUNTS GENERATED FROM THE CURATED REGISTRY</text>
</svg>
'''


def render_readme(catalog: dict) -> str:
    papers = catalog["papers"]
    lines = [
        "<div align=\"center\">",
        "",
        "# Awesome Exploration",
        "",
        "**A curated research map of exploration in large language models and agents.**",
        "",
        "[![Curated catalog](https://img.shields.io/badge/catalog-curated-3B82F6?style=flat-square)](docs/CURATION_2026.md) "
        f"[![{len(papers)} papers](https://img.shields.io/badge/papers-{len(papers)}-8B5CF6?style=flat-square)](#catalog) "
        "[![Five research categories](https://img.shields.io/badge/categories-5-10B981?style=flat-square)](#research-map) "
        "[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-F59E0B?style=flat-square)](CONTRIBUTING.md)",
        "",
        "[Guide](#guide) · [Research map](#research-map) · [10-paper introduction](#start-here) · [Catalog](#catalog) · [Detailed metadata](README_DETAILED.md) · [Contribute](CONTRIBUTING.md)",
        "",
        f'<img src="assets/research-map.svg" alt="Research map of {len(papers)} papers across five exploration categories" width="100%">',
        "",
        "</div>",
        "",
        "## Guide",
        "",
        "| Start here | What you will find |",
        "|---|---|",
        "| **[What counts as exploration](#what-counts-as-exploration)** | Sutton & Barto frame exploration as trying alternatives to improve future action selection, while exploitation uses current knowledge to obtain reward. |",
        "| **[Research map](#research-map)** | Five categories spanning LLM generation, RLVR and policy learning, agentic inference, agentic training, and evidence. |",
        "| **[Taxonomy lens](#taxonomy-lens)** | How phase, level, signal, mechanism, problem, and setting describe each paper. |",
        "| **[Memory × Exploration](#memory-exploration)** | How agents retain, retrieve, and reuse experience to explore more effectively. |",
        "| **[10 papers to get started](#start-here)** | A manually selected introduction to LLM exploration; automatic ranking is intentionally avoided. |",
        "| **[Full catalog](#catalog)** | All curated papers, grouped by their primary research category. |",
        "",
        "## What counts as exploration?",
        "",
        "> This repository treats exploration as a **primary research variable**: a paper must identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. Generic RL, agents, test-time scaling, self-improvement, and diversity work are excluded when exploration is merely incidental.",
        "",
        f"> Evidence snapshot: **{catalog['snapshot_date']}** · [Taxonomy design](docs/TAXONOMY.md) · [2026 curation notes](docs/CURATION_2026.md)",
        "",
        "## Research map",
        "",
        "Every paper has one home in the map; its tags then describe the research lens. Start with the category that matches your question, then use the tags to compare mechanisms across categories.",
        "",
        "| Category | Best for |",
        "|---|---|",
        "| **[Exploration for LLM Generation & Inference](#category-1)** | Sampling, decoding, reasoning-path search, and output diversity without a learning update. |",
        "| **[Exploration for RLVR, Policy & Curriculum](#category-2)** | Curricula, RL/RLVR updates, replay, rewards, and language-model policy-distribution control. |",
        "| **[Agentic Exploration](#category-3)** | Test-time exploration across the web, tools, GUIs, knowledge graphs, and embodied environments. |",
        "| **[Agentic Exploration for Training](#category-4)** | Agent experience collection, interactive task synthesis, self-play training, and agent policy optimization. |",
        "| **[Understanding, Evaluation & Benchmarks](#category-5)** | Surveys, theory, metrics, benchmarks, and evidence about exploration. |",
        "",
        "<a id=\"taxonomy-lens\"></a>",
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
        '<a id="start-here"></a>',
        "",
        "## 10 Papers to Get Started with LLM Exploration",
        "",
    ]

    featured = sorted(
        (p for p in papers if p.get("featured")),
        key=lambda p: p.get("featured_rank", 10_000),
    )
    if len(featured) != 10:
        lines.extend(
            [
                f"### Candidate Pool · {paper_count_label(len(featured))}",
                "",
            ]
        )

    for paper in featured:
        lines.append(
            f"- **[{paper['title']}]({paper['url']})** — {source_label(paper)} · "
            f"{AREA_LABELS[paper['primary_area']]} · {representative_tags(paper)}"
        )

    lines.extend(
        [
            "",
            "<a id=\"catalog\"></a>",
            "",
            "## Catalog",
            "",
            f"> 🏆 Published at a recognized top-tier venue. ⭐ Cited at least 100 times. Citation snapshot: **{catalog['citation_snapshot']}**; counts and sources are recorded in the paper registry.",
            "",
            "### Categories",
            "",
            *catalog_table_of_contents(papers),
        ]
    )
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend(
            [
                "",
                f'<a id="{AREA_ANCHORS[area]}"></a>',
                "",
                f"## {index}. {label}",
                "",
                *area_description_lines(area),
            ]
        )
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        for subtopic, grouped in papers_by_subtopic(selected, area).items():
            lines.extend(
                [
                    f'<a id="{subtopic_anchor(area, subtopic)}"></a>',
                    "",
                    f"### {SUBTOPIC_LABELS[area][subtopic]} · {paper_count_label(len(grouped))}",
                    "",
                    SUBTOPIC_SUMMARIES[area][subtopic],
                    "",
                    "| Evidence | Paper | Research lens |",
                    "|---|---|---|",
                ]
            )
            for paper in grouped:
                lines.append(
                    f"| {source_label(paper)} | {notability_marker(paper)}[{paper['title']}]({paper['url']}) | "
                    f"{representative_tags(paper)} |"
                )
            lines.append("")

    lines.extend(
        [
            "",
            "## Classical RL exploration — background only",
            "",
            "A curated appendix of classical RL exploration references. These papers are not counted in the curated LLM and agent catalog.",
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
            '<a id="memory-exploration"></a>',
            "",
            "## Memory × Exploration",
            "",
            "Memory is an exploration policy over past experience: it changes what an agent already knows, what it should revisit, and which unknown states are worth pursuing next. This cross-cutting lens links the catalog's agentic and policy-learning categories without creating a sixth primary area.",
            "",
            "| Research question | Read in the catalog |",
            "|---|---|",
            "| **Memory-guided exploration** — How can recalled trajectories, world models, and knowledge guide the next action? | [Knowledge & Memory-Guided Exploration](#category-3-knowledge-memory) |",
            "| **Exploration-driven memory** — Which successes, failures, and uncertainties should be written, refined, or forgotten? | [Knowledge & Memory-Guided Exploration](#category-3-knowledge-memory) · [Replay, Population & Self-Improvement](#category-2-replay-population) |",
            "| **Failure memory and recovery** — How can an agent avoid repeating failed paths and recover from dead ends? | [Planning & Interactive Search](#category-3-planning-interaction) · [Knowledge & Memory-Guided Exploration](#category-3-knowledge-memory) |",
            "| **Memory-augmented training** — How can retained experience improve later policy updates or task generation? | [Memory-Augmented Agent Training](#category-4-knowledge-memory) · [Replay, Population & Self-Improvement](#category-2-replay-population) |",
        ]
    )

    lines.extend(
        [
            "",
            "## License",
            "",
            "[CC BY 4.0](LICENSE)",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_detailed(catalog: dict) -> str:
    papers = catalog["papers"]
    lines = [
        "# Awesome Exploration — Detailed Catalog",
        "",
        "> Generated from [`data/papers.json`](data/papers.json). Do not edit this file directly.",
        "",
        f"Evidence snapshot: **{catalog['snapshot_date']}** · {len(papers)} curated papers.",
        "",
        f"> 🏆 Published at a recognized top-tier venue. ⭐ Cited at least 100 times. Citation snapshot: **{catalog['citation_snapshot']}**; counts and sources are recorded in the paper registry.",
        "",
    ]
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend([f"## {index}. {label}", "", *area_description_lines(area)])
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        for subtopic, grouped in papers_by_subtopic(selected, area).items():
            lines.extend(
                [
                    f"### {SUBTOPIC_LABELS[area][subtopic]} · {paper_count_label(len(grouped))}",
                    "",
                    SUBTOPIC_SUMMARIES[area][subtopic],
                    "",
                ]
            )
            for paper in grouped:
                lines.append(
                    f"- {notability_marker(paper)}**[{paper['title']}]({paper['url']})** — {source_label(paper)}"
                )
                if paper.get("authors"):
                    authors = paper["authors"]
                    shown = ", ".join(authors[:8]) + (" et al." if len(authors) > 8 else "")
                    lines.append(f"  - Authors: {shown}")
                lines.append(
                    f"  - Type: `{paper['paper_type']}` · Date: `{paper.get('date', '')}`"
                )
                if tags := representative_tags(paper):
                    lines.append(f"  - {tags}")
                if paper.get("rationale"):
                    lines.append(f"  - {paper['rationale']}")
            lines.append("")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    catalog = load_catalog()
    RESEARCH_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESEARCH_MAP_PATH.write_text(render_research_map(catalog), encoding="utf-8")
    (ROOT / "README.md").write_text(render_readme(catalog), encoding="utf-8")
    (ROOT / "README_DETAILED.md").write_text(render_detailed(catalog), encoding="utf-8")
    print(
        f"Generated research map, README.md, and README_DETAILED.md "
        f"from {len(catalog['papers'])} papers"
    )


if __name__ == "__main__":
    main()
