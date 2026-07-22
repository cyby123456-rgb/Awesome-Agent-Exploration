# Taxonomy Design

This document explains how **Awesome Exploration** organizes papers, what each
classification dimension means, and why the taxonomy is structured this way.

## Design goal

The catalog is about exploration in language models, RLVR, and language agents.
It is not a general collection of reinforcement learning, search, diversity, or
agent papers. The taxonomy therefore has two jobs:

1. make the list easy to browse by a paper's main research context; and
2. preserve the different ways in which exploration can be observed or changed.

A single hierarchy cannot do both well. For example, `token`, `entropy`, and
`temperature` answer three different questions: **where** exploration appears,
**what quantity** represents it, and **how** a method controls it. Treating them
as sibling sections creates overlaps and duplicate entries.

The catalog instead uses:

- exactly **one primary area** for navigation; and
- multiple **orthogonal tags** for phase, level, signal, mechanism, problem, and
  setting.

`paper_type` is a separate metadata field describing the kind of research
contribution.

## Primary areas

Primary areas answer: **In which research context does this paper make its main
exploration contribution?** A paper appears in only one area, even when its
method or findings transfer to other areas.

### 1. LLM Generation & Inference Exploration

Exploration among candidate tokens, responses, reasoning paths, or latent states
during generation and inference, without an RL policy update as the central
contribution. This includes sampling, decoding, diverse generation, latent
steering, self-consistency, and test-time search.

### 2. Policy & RLVR Exploration

Exploration during RL or RLVR post-training, where the method changes rollout
collection, reward or advantage signals, the policy distribution, or the policy
update. Entropy collapse, low-probability tokens, reward shaping, and gradient
interventions belong here.

### 3. Data, Task & Curriculum Exploration

Exploration over what the model learns from: active data selection, synthetic
task generation, difficulty control, adaptive curricula, and
exploration-aware training-set construction. The primary exploration object is
the data or problem space rather than a single model trajectory.

### 4. Agentic & Environment Exploration

Exploration by a language agent acting in an external environment, such as the
web, tools, GUIs, games, or embodied worlds. The explored object is normally a
sequence of states, actions, observations, or tool calls.

### 5. Self-Improvement & Population Exploration

Exploration through repeated improve-and-evaluate loops or interaction among
multiple policies. This covers self-play, co-evolution, ensembles, multi-agent
collaboration, and systems that preserve diversity across iterations.

### 6. Memory & Knowledge Exploration

Exploration over retrieved documents, episodic traces, long-context memory,
knowledge graphs, or internal memory representations. The question is how a
system searches, selects, combines, writes, compresses, or updates memory to
extend its effective context and search space.

### 7. Understanding, Evaluation & Benchmarks

Empirical analysis, theory, surveys, metrics, and benchmarks whose main
contribution is to explain or measure exploration, diversity, training dynamics,
or capability boundaries rather than introduce an exploration method.

### Primary-area decision rule

Use the paper's main contribution, not every context mentioned in the paper:

1. If the main contribution measures, explains, benchmarks, or surveys rather
   than intervenes, use `understanding-evaluation`.
2. Otherwise, if population interaction or an iterative self-improvement loop
   is the main exploration unit, use `self-improvement-population-exploration`.
3. Otherwise, if searching or managing memory and knowledge is central, use
   `memory-knowledge-exploration`.
4. Otherwise, if selecting data, tasks, or curricula is central, use
   `data-task-curriculum-exploration`.
5. Otherwise, if the main exploration loop acts in an external environment, use
   `agentic-exploration`.
6. Otherwise, if exploration is changed through an RL/RLVR policy update, use
   `rlvr-exploration`.
7. Otherwise, use `llm-exploration` for generation, decoding, and test-time
   search.

Tags preserve secondary aspects, so a paper does not need multiple primary
areas. When the boundary remains ambiguous, classify by the component evaluated
in the main experiments and state the choice in the curation rationale.

## Subtopics

Every paper also has one subtopic within its primary area. Subtopics are a
navigation aid, not a replacement for the orthogonal tags below.

| Primary area | Subtopics |
|---|---|
| LLM Generation & Inference | Decoding & Sampling; Search & Deliberation; Representation & Latent Steering; Diversity & Coverage |
| Policy & RLVR | Entropy & Distribution Control; Credit Assignment & Optimization; Reward & Rollout Shaping; Capability Boundaries & Training Dynamics |
| Data, Task & Curriculum | Data Selection & Prompt Exploration; Task Synthesis & Curriculum; Agent Task & Environment Generation |
| Agentic & Environment | Web, Tools & GUI; Planning & Interactive Search; Embodied & Simulated Environments |
| Self-Improvement & Population | Self-Play & Co-Evolution; Multi-Agent & Ensemble Exploration; Iterative Self-Improvement |
| Memory & Knowledge | Replay & Trajectory Memory; Retrieval & Long-Context Memory; Knowledge-Graph Memory; Memory-Guided Planning |
| Understanding, Evaluation & Benchmarks | Surveys & Position Papers; Theory & Training Dynamics; Capability Boundaries; Benchmarks & Metrics |

## Tag dimensions

Each tag dimension answers a different question. Multiple values within a
dimension are allowed when they are materially part of the contribution.

| Dimension | Question answered | Meaning and examples | Why it matters |
|---|---|---|---|
| `phase` | **When** does exploration occur or get changed? | `data-generation`, `supervised-post-training`, `rl-training`, `inference`, `test-time-adaptation`, `continual/self-improvement` | Separates training-time distribution change from inference-time search and sampling. |
| `level` | **What object** is being explored or diversified? | `token`, `response/sequence`, `trajectory/action`, `latent/representation`, `policy-distribution`, `data/task`, `population/multi-policy` | Replaces overlapping Token / Sequence / Policy sections and makes granularity explicit. |
| `signal` | **What quantity** indicates exploration or guides a decision? | `entropy/probability`, `uncertainty/confidence`, `novelty/curiosity`, `semantic-diversity`, `coverage`, `information-gain`, `reward/advantage`, `disagreement` | Distinguishes the evidence used to detect or value exploration from the operation applied to the model. |
| `mechanism` | **How** is exploration produced or controlled? | `sampling/decoding`, `temperature-control`, `noise/perturbation`, `regularization`, `gradient-reshaping`, `reward-shaping/intrinsic-reward`, `tree-search/branching`, `structured-search`, `backtracking/resampling`, `replay/memory`, `curriculum/task-generation`, `self-play/co-evolution`, `ensemble/population` | Lets readers compare interventions that use different signals but the same operator, or the same signal with different operators. |
| `problem` | **Why** is exploration needed? | `entropy-collapse`, `mode-collapse`, `sparse-reward`, `local-optimum`, `capability-boundary`, `long-horizon`, `exploration-exploitation`, `recovery/error-correction` | Records the failure mode or trade-off a method is designed to address. |
| `setting` | **Where** is the method demonstrated? | `math`, `code`, `multimodal`, `creative/open-ended`, `web`, `tool-use`, `knowledge-graph`, `embodied`, `multi-agent` | Supports application-oriented browsing without making domains the conceptual taxonomy. |
| `paper_type` | **What kind of contribution** is it? | `method`, `analysis`, `benchmark`, `survey`, `position` | Prevents a benchmark or analysis from being mistaken for an intervention method. |

`phase` and `level` are required. Every normal catalog entry must also have at
least one `signal` or `mechanism`, which enforces that exploration is a concrete
part of the paper rather than an incidental keyword. `problem` and `setting` are
optional because many papers are domain-general or do not target a named failure
mode.

The registry preserves all applicable metadata, but the generated public views
show at most three representative tags per paper. They prefer one `phase`, one
`signal`, and one `mechanism`; when one of those dimensions is absent, `level`,
`problem`, or `setting` supplies the missing context. Mechanism badges use
distinct colors so different interventions remain easy to scan.

## Entropy, temperature, and noise

These concepts are related but should not be one tag:

- **Entropy / probability** is a `signal`: it describes or measures a
  distribution and can serve as a target, diagnostic, or control input.
- **Temperature control** is a `mechanism`: it changes the shape of a sampling
  distribution.
- **Noise / perturbation** is a `mechanism`: it injects stochastic variation into
  logits, parameters, latent states, inputs, rewards, or trajectories.

They belong to the same broad family of **distributional and stochastic
exploration**, which is useful as a conceptual grouping, but keeping the tags
distinct preserves causal meaning. A temperature method may be entropy-aware; a
noise method may not use entropy at all; and an entropy analysis may introduce
no intervention.

## Worked examples

| Paper pattern | Primary area | Representative tags | Reasoning |
|---|---|---|---|
| An RLVR method preserves low-probability tokens with a regularizer | `rlvr-exploration` | phase: `rl-training`; level: `token`, `policy-distribution`; signal: `entropy/probability`; mechanism: `regularization`; problem: `entropy-collapse` | The policy update is central; entropy is the signal and regularization is the intervention. |
| A decoder branches over candidate reasoning paths at inference time | `llm-exploration` | phase: `inference`; level: `response/sequence`; mechanism: `tree-search/branching` | It explores generations without making RL training the contribution. |
| A web agent learns which pages or tools to visit over a long trajectory | `agentic-exploration` | phase: `rl-training` or `inference`; level: `trajectory/action`; mechanism: `replay/memory` or `structured-search`; setting: `web`, `tool-use` | External interaction and trajectory coverage define the exploration problem. |
| A benchmark measures strategy diversity in mathematical reasoning | `understanding-evaluation` | type: `benchmark`; phase: `inference`; level: `response/sequence`; signal: `semantic-diversity`; setting: `math` | Measurement, rather than a new exploration intervention, is the main contribution. |

## Scope boundaries

Traditional non-LLM reinforcement-learning exploration is not part of the main
catalog. A small background appendix keeps only a handful of foundational ideas
that provide vocabulary or mechanisms still used in LLM exploration, such as
optimism, count-based exploration, curiosity, and intrinsic motivation. These
references are intentionally not counted in catalog totals.

The following are also excluded unless exploration is a primary contribution:

- generic RL or policy-optimization papers;
- generic test-time scaling or search papers whose contribution is only
  efficiency or accuracy;
- generic agent frameworks, self-improvement, or self-play systems;
- diversity papers where diversity is merely a dataset or evaluation property;
- papers matched only by words such as *entropy*, *noise*, *policy*, or
  *exploration* in an unrelated sense.

This boundary keeps the list useful as a map of **LLM exploration research**, not
as a broad bibliography of adjacent machine-learning topics.
