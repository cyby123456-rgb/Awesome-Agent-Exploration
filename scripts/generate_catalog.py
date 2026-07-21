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
    "llm-exploration": "LLM Generation & Inference Exploration",
    "rlvr-exploration": "Policy & RLVR Exploration",
    "data-task-curriculum-exploration": "Data, Task & Curriculum Exploration",
    "agentic-exploration": "Agentic & Environment Exploration",
    "self-improvement-population-exploration": "Self-Improvement & Population Exploration",
    "memory-knowledge-exploration": "Memory & Knowledge Exploration",
    "understanding-evaluation": "Understanding, Evaluation & Benchmarks",
}

AREA_SUMMARIES = {
    "llm-exploration": "Exploration during language-model generation and inference, without RL policy updates as the central contribution.",
    "rlvr-exploration": "Exploration during RL/RLVR post-training, where exploration changes the rollout distribution or policy update.",
    "data-task-curriculum-exploration": "Exploration over data, tasks, difficulty, and curricula that determines what the model learns from next.",
    "agentic-exploration": "Exploration by language agents acting over states, tools, observations, and long-horizon trajectories.",
    "self-improvement-population-exploration": "Exploration through self-play, multiple policies, collaboration, and iterative self-improvement loops.",
    "memory-knowledge-exploration": "Exploration over retrieved, written, consolidated, or structured memories and knowledge sources.",
    "understanding-evaluation": "Work that measures, explains, surveys, or benchmarks exploration rather than primarily introducing an intervention.",
}

RESEARCH_MAP_TRACKS = [
    {
        "area": "llm-exploration",
        "eyebrow": "01 / GENERATION",
        "title": ["LLM Exploration"],
        "keywords": "sampling  |  search  |  diversity",
        "color": "#6E8FB8",
    },
    {
        "area": "rlvr-exploration",
        "eyebrow": "02 / POLICY LEARNING",
        "title": ["Policy & RLVR"],
        "keywords": "entropy  |  reward  |  optimization",
        "color": "#B07A68",
    },
    {
        "area": "data-task-curriculum-exploration",
        "eyebrow": "03 / LEARNING MATERIAL",
        "title": ["Data, Task & Curriculum"],
        "keywords": "selection  |  synthesis  |  difficulty",
        "color": "#5F8F8B",
    },
    {
        "area": "agentic-exploration",
        "eyebrow": "04 / INTERACTION",
        "title": ["Agentic & Environment"],
        "keywords": "tools  |  planning  |  embodied worlds",
        "color": "#8B80B6",
    },
    {
        "area": "self-improvement-population-exploration",
        "eyebrow": "05 / POPULATIONS",
        "title": ["Self-Improvement", "& Population"],
        "keywords": "self-play  |  ensembles  |  iteration",
        "color": "#A07593",
    },
    {
        "area": "memory-knowledge-exploration",
        "eyebrow": "06 / INFORMATION",
        "title": ["Memory & Knowledge"],
        "keywords": "retrieval  |  replay  |  knowledge graphs",
        "color": "#718B75",
    },
    {
        "area": "understanding-evaluation",
        "eyebrow": "07 / EVIDENCE",
        "title": ["Understanding", "& Evaluation"],
        "keywords": "theory  |  metrics  |  benchmarks",
        "color": "#B06D73",
    },
]

AREA_DESCRIPTIONS = {
    "llm-exploration": [
        "This category covers exploration that happens while a language model is generating or selecting candidate outputs, rather than through a reinforcement-learning update. Typical examples include sampling and decoding strategies, self-consistency, semantic-diversity methods, latent-state steering, and tree or graph search at inference time.",
        "The central question is how to search a model's existing generative distribution more broadly, safely, or efficiently. Papers belong here when the main contribution improves or analyzes candidate generation, reasoning-path search, or output diversity without making RL post-training the core mechanism.",
    ],
    "rlvr-exploration": [
        "This category concerns exploration during reinforcement learning or RL with verifiable rewards (RLVR). Here, exploration changes which rollouts are collected, how reward or advantage signals are assigned, or how the policy distribution is updated during training.",
        "It includes work on entropy or mode collapse, low-probability tokens, rollout diversity, intrinsic or shaped rewards, gradient and regularization interventions, curriculum design, and attempts to push beyond a base model's capability boundary. The defining feature is that exploration is part of the learning loop, not only an inference-time search choice.",
    ],
    "data-task-curriculum-exploration": [
        "This category covers exploration over the learning material itself: which data to generate or select, which tasks to attempt, how to vary difficulty, and how to construct a curriculum. Rather than changing only a model's next-token or policy distribution, these methods expand or prioritize the problem space from which learning signals are drawn.",
        "It includes active data selection, synthetic task generation, adaptive curricula, and exploration-aware training-set construction. A paper belongs here when deciding what to learn from is its central exploration mechanism.",
    ],
    "agentic-exploration": [
        "This category covers language agents that explore an external or persistent environment: webpages, tools, GUIs, knowledge graphs, games, embodied worlds, or multi-agent settings. The object of exploration is usually a trajectory of states, actions, observations, and tool calls rather than a single textual response.",
        "These papers focus on challenges such as partial observability, long horizons, recovery from failed actions, memory, environment coverage, and interactive search. A paper belongs here when external interaction is central to the exploration problem and evaluation.",
    ],
    "self-improvement-population-exploration": [
        "This category covers exploration that emerges from repeated improvement loops or from interaction among multiple policies. Examples include self-play, co-evolution, ensembles, multi-agent collaboration, and generate–evaluate–train cycles that deliberately preserve diverse attempts.",
        "The key question is how a system can discover capabilities beyond a single fixed policy by using its own history, peer policies, or iterative feedback. Papers belong here when the population or self-improvement loop—not merely one rollout—is the main exploration unit.",
    ],
    "memory-knowledge-exploration": [
        "This category covers exploration over information stored beyond the immediate prompt: retrieved documents, episodic traces, long-context memories, knowledge graphs, or internal memory representations. The focus is not simply whether a model has memory, but how it searches, selects, combines, writes, compresses, or updates memory to expand its effective search space.",
        "It includes memory-retrieval policies, memory writing and consolidation, forgetting, structured knowledge navigation, and memory-guided planning. A paper belongs here when actively exploring or managing knowledge is central to the method or evaluation.",
    ],
    "understanding-evaluation": [
        "This category collects empirical analyses, theoretical accounts, surveys, metrics, and benchmarks that help the field understand exploration. Rather than primarily proposing a new exploration intervention, these works measure diversity, characterize training dynamics, evaluate capability boundaries, or establish a shared vocabulary and test bed.",
        "They are essential for judging whether a method genuinely improves exploration instead of merely changing accuracy or sampling behavior. Keeping them separate makes the evidence about a phenomenon easy to distinguish from methods designed to change it.",
    ],
}

SUBTOPIC_LABELS = {
    "llm-exploration": {
        "decoding-sampling": "Decoding & Sampling",
        "search-deliberation": "Search & Deliberation",
        "representation-steering": "Representation & Latent Steering",
        "diversity-coverage": "Diversity & Coverage",
    },
    "rlvr-exploration": {
        "entropy-distribution": "Entropy & Distribution Control",
        "credit-optimization": "Credit Assignment & Optimization",
        "reward-rollout": "Reward & Rollout Shaping",
        "capability-dynamics": "Capability Boundaries & Training Dynamics",
    },
    "data-task-curriculum-exploration": {
        "data-selection-prompting": "Data Selection & Prompt Exploration",
        "task-synthesis-curriculum": "Task Synthesis & Curriculum",
        "agent-task-environments": "Agent Task & Environment Generation",
    },
    "agentic-exploration": {
        "web-tools-gui": "Web, Tools & GUI",
        "planning-interaction": "Planning & Interactive Search",
        "embodied-environments": "Embodied & Simulated Environments",
    },
    "self-improvement-population-exploration": {
        "self-play-coevolution": "Self-Play & Co-Evolution",
        "multi-agent-ensembles": "Multi-Agent & Ensemble Exploration",
        "iterative-self-improvement": "Iterative Self-Improvement",
    },
    "memory-knowledge-exploration": {
        "replay-trajectory-memory": "Replay & Trajectory Memory",
        "retrieval-long-context": "Retrieval & Long-Context Memory",
        "knowledge-graph-memory": "Knowledge-Graph Memory",
        "memory-guided-planning": "Memory-Guided Planning",
    },
    "understanding-evaluation": {
        "theory-training-dynamics": "Theory & Training Dynamics",
        "capability-boundaries": "Capability Boundaries",
        "benchmarks-metrics": "Benchmarks & Metrics",
        "surveys-position": "Surveys & Position Papers",
    },
}

SUBTOPIC_SUMMARIES = {
    "llm-exploration": {
        "decoding-sampling": "Methods that broaden candidate generation at inference time, with probability shaping, temperature, and sampling strategy as the key levers for balancing diversity, quality, and cost.",
        "search-deliberation": "Methods that explore multi-step reasoning paths through branching, resampling, planning, or verification, with search-budget allocation and path quality as the central concerns.",
        "representation-steering": "Methods that diversify generation by steering activations, embeddings, or latent states, focusing on controllable variation beyond output-level sampling.",
        "diversity-coverage": "Methods that counter mode collapse and expand semantic coverage, emphasizing how novelty and breadth can improve without sacrificing correctness or coherence.",
    },
    "rlvr-exploration": {
        "entropy-distribution": "Work that analyzes or controls policy entropy and token probabilities during RL, aiming to preserve useful distributional support while preventing premature collapse.",
        "credit-optimization": "Methods that reshape rewards, advantages, or gradients so exploratory behavior receives an informative learning signal, with stable and precise credit assignment as the key challenge.",
        "reward-rollout": "Methods that alter rollout collection, reward shaping, intrinsic bonuses, or resampling to elicit more varied and informative training trajectories.",
        "capability-dynamics": "Work that studies how RL training expands, redistributes, or erodes model capabilities, focusing on generalization boundaries, stability, and genuine capability growth.",
    },
    "data-task-curriculum-exploration": {
        "data-selection-prompting": "Methods that select, prioritize, or prompt candidate training examples, using informativeness, uncertainty, and coverage to decide which data is most valuable next.",
        "task-synthesis-curriculum": "Methods that generate and sequence tasks across difficulty levels, with adaptive progression, task diversity, and learnability as the main curriculum concerns.",
        "agent-task-environments": "Methods that create interactive tasks or environments for agents, emphasizing realism, behavioral coverage, controllable difficulty, and useful feedback.",
    },
    "agentic-exploration": {
        "web-tools-gui": "Agents that explore websites, tools, and graphical interfaces, where action grounding, partial observability, tool choice, and recovery from failed interactions are central.",
        "planning-interaction": "Agents that search over multi-step action plans while interacting with an environment, focusing on long-horizon feedback, replanning, and efficient state-space coverage.",
        "embodied-environments": "Agents that explore physical or simulated worlds, with spatial reasoning, world-model learning, action consequences, and sample-efficient coverage as key issues.",
    },
    "self-improvement-population-exploration": {
        "self-play-coevolution": "Systems in which policies or agents generate challenges for one another, using competitive or cooperative pressure to build an adaptive curriculum while maintaining diversity and stability.",
        "multi-agent-ensembles": "Systems that combine multiple agents or policies to expand behavioral coverage, with disagreement, specialization, coordination, and aggregation as the main design axes.",
        "iterative-self-improvement": "Systems that repeatedly generate, evaluate, and learn from their own outputs, focusing on retaining novelty and avoiding self-reinforcing errors or collapse across iterations.",
    },
    "memory-knowledge-exploration": {
        "replay-trajectory-memory": "Methods that store and revisit prior trajectories or experiences, emphasizing which memories to retain, replay, and credit for better long-horizon exploration.",
        "retrieval-long-context": "Methods that explore documents or long contexts through retrieval and selection, with query quality, evidence coverage, and context-budget efficiency as key concerns.",
        "knowledge-graph-memory": "Methods that traverse or update structured knowledge and memory graphs, focusing on relation-aware search, multi-hop coverage, and reliable knowledge integration.",
        "memory-guided-planning": "Methods that use retrieved or accumulated memory to choose reasoning and action paths, emphasizing timely recall, memory updates, and decision relevance.",
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
    """Render each explanatory paragraph as a distinct Markdown paragraph."""
    lines: list[str] = []
    for paragraph in AREA_DESCRIPTIONS[area]:
        lines.extend([paragraph, ""])
    return lines


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


def source_label(paper: dict) -> str:
    parsed_url = urlparse(paper["url"])
    if parsed_url.netloc.lower() in {"arxiv.org", "www.arxiv.org"}:
        arxiv_id = parsed_url.path.removeprefix("/abs/").strip("/")
        if arxiv_id:
            return f"arXiv `{arxiv_id}`"
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


def render_research_map(catalog: dict) -> str:
    """Render a compact, data-driven overview of the seven research tracks."""
    papers = catalog["papers"]
    area_counts = Counter(paper["primary_area"] for paper in papers)
    maximum = max(area_counts.values())
    rows = []

    for index, track in enumerate(RESEARCH_MAP_TRACKS, start=1):
        count = area_counts[track["area"]]
        percentage = count / len(papers) * 100
        y = 142 + (index - 1) * 57
        bar_width = max(12, round(600 * count / maximum, 1))
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
            f'<rect x="430" y="{y - 14}" width="600" height="14" rx="7" '
            f'class="bar-track" />'
            f'<rect x="430" y="{y - 14}" width="{bar_width:g}" height="14" rx="7" '
            f'fill="{color}" />'
            f'<text x="1055" y="{y - 1}" class="track-count" text-anchor="end">'
            f'{count}</text>'
            f'<text x="1138" y="{y - 1}" class="track-share" text-anchor="end">'
            f'{percentage:.1f}%</text>'
            f'<line x1="30" y1="{y + 31}" x2="1170" y2="{y + 31}" class="row-line" />'
            f'</g>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="570" viewBox="0 0 1200 570" role="img" aria-labelledby="map-title map-description">
  <title id="map-title">Awesome Exploration research map</title>
  <desc id="map-description">{len(papers)} curated papers organized into seven research tracks, with current paper counts and key topics for each track.</desc>
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
      .track-count {{ fill: #344054; font-size: 18px; font-weight: 500; }}
      .track-share {{ fill: #7A8495; font-size: 12px; font-weight: 400; }}
      .bar-track {{ fill: #E5E9EF; }}
      .row-line {{ stroke: #E3E7EC; stroke-width: 1; }}
      .footer {{ fill: #8993A4; font-size: 10px; font-weight: 500; letter-spacing: 1.2px; }}
    </style>
  </defs>
  <rect x="5" y="5" width="1190" height="560" rx="24" fill="url(#map-background)" />
  <text x="36" y="48" class="map-heading">Exploration research landscape</text>
  <text x="36" y="73" class="map-subtitle">Where exploration happens across language models, RLVR, agents, data, memory, and evaluation</text>
  <text x="1138" y="48" class="map-total" text-anchor="end">{len(papers)}</text>
  <text x="1138" y="70" class="map-total-label" text-anchor="end">CURATED PAPERS</text>
  <line x1="30" y1="95" x2="1170" y2="95" class="row-line" />
  {''.join(rows)}
  <text x="600" y="550" class="footer" text-anchor="middle">SEVEN COMPLEMENTARY RESEARCH TRACKS  /  COUNTS GENERATED FROM THE CURATED REGISTRY</text>
</svg>
'''


def render_readme(catalog: dict) -> str:
    papers = catalog["papers"]
    lines = [
        "<div align=\"center\">",
        "",
        "# Awesome Exploration",
        "",
        "**A curated research map of exploration in language models, RLVR, and agents.**",
        "",
        f'<img src="assets/research-map.svg" alt="Research map of {len(papers)} papers across seven exploration categories" width="100%">',
        "",
        "[![Curated catalog](https://img.shields.io/badge/catalog-curated-3B82F6?style=flat-square)](docs/CURATION_2026.md) "
        f"[![{len(papers)} papers](https://img.shields.io/badge/papers-{len(papers)}-8B5CF6?style=flat-square)](#catalog) "
        "[![Seven research tracks](https://img.shields.io/badge/tracks-7-10B981?style=flat-square)](#research-map) "
        "[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-F59E0B?style=flat-square)](CONTRIBUTING.md)",
        "",
        "[Guide](#guide) · [Research map](#research-map) · [Start here](#start-here) · [Catalog](#catalog) · [Detailed metadata](README_DETAILED.md) · [Contribute](CONTRIBUTING.md)",
        "",
        "</div>",
        "",
        "## Guide",
        "",
        "| Start here | What you will find |",
        "|---|---|",
        "| **[What counts as exploration](#what-counts-as-exploration)** | Our scope: exploration must be a concrete research variable, not only a keyword. |",
        "| **[Research map](#research-map)** | The seven places exploration occurs: generation, RLVR, data, agents, self-improvement, memory, and evaluation. |",
        "| **[Taxonomy lens](#taxonomy-lens)** | How phase, level, signal, mechanism, problem, and setting describe each paper. |",
        "| **[Start here](#start-here)** | A cross-section of recommended papers for first-time readers. |",
        "| **[Full catalog](#catalog)** | All curated papers, grouped by their primary research context. |",
        "",
        "## What counts as exploration?",
        "",
        "> This repository treats exploration as a **primary research variable**: a paper must identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. Generic RL, agents, test-time scaling, self-improvement, and diversity work are excluded when exploration is merely incidental.",
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
        "| **[Policy & RLVR](#2-policy--rlvr-exploration)** | Entropy collapse, rollout diversity, reward shaping, and policy-distribution control during training. |",
        "| **[Data, Task & Curriculum](#3-data-task--curriculum-exploration)** | Active data selection, task generation, and adaptive difficulty or curriculum design. |",
        "| **[Agentic & Environment](#4-agentic--environment-exploration)** | Web, tool, GUI, knowledge-graph, embodied, or multi-agent trajectories. |",
        "| **[Self-Improvement & Population](#5-self-improvement--population-exploration)** | Self-play, ensembles, collaboration, and iterative improve-and-evaluate loops. |",
        "| **[Memory & Knowledge](#6-memory--knowledge-exploration)** | Retrieval, memory writing, consolidation, knowledge graphs, and long-context search. |",
        "| **[Understanding & Evaluation](#7-understanding-evaluation--benchmarks)** | Surveys, theory, metrics, benchmarks, and evidence about exploration. |",
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
        "## Start here",
        "",
        "> These are signposts into the full catalog. Every highlighted paper—including all conference papers—also appears once in its corresponding category and subcategory below.",
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
            f"{AREA_LABELS[paper['primary_area']]} · {representative_tags(paper)}"
        )

    lines.extend(["", "<a id=\"catalog\"></a>", "", "## Catalog"])
    for index, (area, label) in enumerate(AREA_LABELS.items(), start=1):
        lines.extend(["", f"## {index}. {label}", "", f"> **Research focus.** {AREA_DESCRIPTIONS[area][0]}", "", AREA_DESCRIPTIONS[area][1], ""])
        selected = sorted(
            (p for p in papers if p["primary_area"] == area),
            key=lambda p: (p.get("date", ""), p["title"]),
            reverse=True,
        )
        for subtopic, grouped in papers_by_subtopic(selected, area).items():
            lines.extend(
                [
                    f"### {SUBTOPIC_LABELS[area][subtopic]} · {len(grouped)} papers",
                    "",
                    SUBTOPIC_SUMMARIES[area][subtopic],
                    "",
                    "| Evidence | Paper | Research lens |",
                    "|---|---|---|",
                ]
            )
            for paper in grouped:
                lines.append(
                    f"| {source_label(paper)} | [{paper['title']}]({paper['url']}) | "
                    f"{representative_tags(paper)} |"
                )
            lines.append("")

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
                    f"### {SUBTOPIC_LABELS[area][subtopic]} · {len(grouped)} papers",
                    "",
                    SUBTOPIC_SUMMARIES[area][subtopic],
                    "",
                ]
            )
            for paper in grouped:
                lines.append(
                    f"- **[{paper['title']}]({paper['url']})** — {source_label(paper)}"
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
