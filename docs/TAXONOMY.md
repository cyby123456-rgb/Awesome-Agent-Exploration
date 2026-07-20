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
during generation and inference, without requiring an RL policy update as the
central contribution.

Typical work includes sampling and decoding, diverse generation, latent
steering, self-consistency, tree or graph reasoning, and test-time search.

**Why it is separate:** exploration can happen entirely inside model generation.
Putting all such work under RLVR would incorrectly imply that policy training is
required; putting it under agents would incorrectly imply an external
environment.

### 2. Exploration for RLVR

Exploration during reinforcement learning or reinforcement learning with
verifiable rewards, including entropy collapse, rollout diversity, intrinsic or
shaped rewards, policy-distribution control, gradient interventions, curriculum,
and capability expansion.

**Why it is separate:** here exploration affects the data distribution and the
policy update. This creates problems and interventions—such as on-policy
collapse, advantage shaping, or exploration-aware optimization—that are
different from inference-only sampling.

### 3. Agentic Exploration

Exploration by a language agent acting in an external or persistent environment,
such as the web, tools, GUIs, knowledge graphs, games, embodied worlds, or
multi-agent systems. The explored object is normally a sequence of states,
actions, observations, or tool calls.

**Why it is separate:** agentic exploration is governed by interaction,
partial observability, long horizons, memory, recovery, and environment
coverage—not only by diversity in generated text.

### 4. Understanding, Evaluation & Benchmarks

Empirical analysis, theory, surveys, metrics, and benchmarks whose main
contribution is to explain or measure exploration, diversity, training dynamics,
or capability boundaries rather than introduce an exploration method.

**Why it is separate:** explanatory and evaluative work is essential, but mixing
it into method sections makes it difficult to distinguish evidence about a
phenomenon from interventions intended to change that phenomenon.

### Primary-area decision rule

Use the paper's main contribution, not every context mentioned in the paper:

1. If the main exploration loop acts in an external environment, use
   `agentic-exploration`.
2. Otherwise, if exploration is changed through an RL/RLVR policy update, use
   `rlvr-exploration`.
3. Otherwise, if exploration happens during model generation, decoding, or
   test-time search, use `llm-exploration`.
4. If the main contribution measures, explains, benchmarks, or surveys rather
   than intervenes, use `understanding-evaluation`.

Tags preserve secondary aspects, so a paper does not need multiple primary
areas. When the boundary remains ambiguous, classify by the component evaluated
in the main experiments and state the choice in the curation rationale.

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
