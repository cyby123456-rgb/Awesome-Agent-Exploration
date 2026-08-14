# Taxonomy Design

This document explains how **Awesome Exploration** organizes papers, what each
classification dimension means, and why the taxonomy is structured this way.

## Design goal

The catalog is about exploration in language models, post-training, and
language agents. It is not a general collection of reinforcement learning,
search, diversity, self-improvement, or memory papers. The taxonomy has two
jobs:

1. make the list easy to browse by the research category containing the main
   exploration loop; and
2. preserve the different ways exploration can be observed or changed.

A single hierarchy cannot do both well. For example, `token`, `entropy`, and
`temperature` answer three different questions: **what object** is explored,
**what quantity** represents it, and **how** a method controls it. Treating them
as sibling sections creates overlaps and duplicate entries.

The catalog therefore uses:

- exactly **one primary category** for navigation; and
- multiple **orthogonal tags** for phase, level, signal, mechanism, problem, and
  setting.

`paper_type` separately describes the kind of research contribution. Data,
memory, population, and self-improvement are not primary categories because each can
support several different exploration loops; they remain visible through
subtopics and tags.

## Primary categories

Primary categories form a 2 x 2 map. They answer both **what space is being
explored** (a model's internal capability space or an external environment) and
**what the exploration is for** (solving the current task at inference or
generating experience for learning). A paper appears in one category even when
its method or findings transfer elsewhere.

### 1. Model-Space Exploration at Inference

Exploration among candidate tokens, responses, reasoning paths, or latent states
during generation and inference, without a parameter update as the central
contribution. Key concerns are decoding and sampling, self-consistency,
reasoning-path search, tree or graph search, representation or latent
exploration, semantic diversity, and coverage.

**Core question:** How can an LLM explore alternative generations or reasoning
paths without updating its parameters?

### 2. Model-Space Exploration for Learning

Exploration inside the language-model learning loop, including entropy and
policy support, rollout exploration, advantage and credit assignment, intrinsic
reward, replay, self-play, data exploration, task synthesis, curriculum
learning, and post-training updates. The explored object is a model output,
reasoning rollout, data distribution, or task distribution rather than an
external environment interaction.

**Core question:** How can exploration generate informative experience and
expand what the model can learn?

### 3. Environment-Space Exploration at Inference

Exploration by a language agent acting at inference or test time in an external
or persistent environment, including the web, tools, GUIs, knowledge graphs,
games, and embodied worlds. Key concerns are long-horizon planning, partial
observability, action grounding, recovery, environment coverage, and
memory-guided interaction.

The explored object is environment state, action, or information, rather than
only a token or reasoning trajectory.

### 4. Environment-Space Exploration for Learning

Agent-environment exploration used to create experience, synthesize interactive
tasks, or improve an agent policy. Key concerns are agentic RL, long-horizon
credit assignment, autonomous experience collection, self-play training,
environment generation, and transferring learned policies across tools and
environments.

**Core distinction:** The environment is not merely searched to finish the
current task; interaction becomes training experience.

### 5. Understanding, Evaluation & Benchmarks

Empirical analysis, theory, surveys, metrics, and benchmarks whose main
contribution is evidence about exploration rather than an intervention. Key
concerns are explaining training dynamics, measuring diversity and coverage,
testing capability boundaries, and establishing reproducible evaluation.

### Primary-category decision rule

Use the paper's main contribution, not every context it mentions:

1. If the main contribution only measures, explains, benchmarks, or surveys,
   use `understanding-evaluation`.
2. Otherwise, if external agent interaction becomes experience, tasks, or a
   policy update, use `agentic-training-exploration` (environment space for
   learning).
3. Otherwise, if the main exploration loop acts in an external or persistent
   environment at inference or test time, use `agentic-exploration`
   (environment space at inference).
4. Otherwise, if exploration changes an LLM policy, rollout distribution, data
   selection, or curriculum, use `rlvr-policy-curriculum-exploration` (model
   space for learning).
5. Otherwise, use `llm-exploration` for generation, decoding, representation
   steering, and test-time search (model space at inference).

This order resolves common ambiguities. Memory-guided web navigation is
environment-space inference; web trajectories collected to update an agent are
environment-space learning; entropy control without external interaction is
model-space learning; self-consistency at inference is model-space inference;
and a paper that only analyzes entropy collapse is understanding and evaluation.
When the boundary remains ambiguous, classify by the component evaluated in the
main experiments and state the choice in the curation rationale.

## Subtopics

Every paper has one subtopic within its primary category. Each subtopic states both
the category and its central concern; it is a navigation aid rather than a
replacement for the orthogonal tags below.

| Primary category | Subtopics and key points |
|---|---|
| Model-Space Exploration at Inference | **Decoding & Sampling:** broadens candidate generation through probability shaping and sampling; **Search & Deliberation:** explores multi-step reasoning paths through branching, verification, or resampling; **Representation & Latent Steering:** diversifies behavior by intervening in internal representations; **Diversity & Coverage:** expands semantic breadth while preserving quality. |
| Model-Space Exploration for Learning | **Entropy & Distribution Control:** preserves useful policy support; **Credit Assignment & Optimization:** makes exploratory behavior learnable; **Reward & Rollout Shaping:** elicits informative trajectories; **Replay, Population & Self-Improvement:** reuses experience or interacting policies across updates; **Capability Expansion & Training Interventions:** changes or stabilizes what training can learn; **Data Selection & Prompt Exploration:** chooses informative training examples; **Task Synthesis & Curriculum:** generates and sequences learnable tasks. |
| Environment-Space Exploration at Inference | **Web, Tools & GUI:** explores interactive digital interfaces; **Planning & Interactive Search:** searches long-horizon action plans under feedback; **Embodied & Simulated Environments:** explores spatial or simulated worlds; **Knowledge & Memory-Guided Exploration:** uses structured knowledge or accumulated experience to choose future actions. |
| Environment-Space Exploration for Learning | **Web, Tools & GUI Training:** learns from interactive digital experience; **Agentic Policy Learning:** updates policies from exploratory trajectories; **Embodied & Simulated Training:** learns under noisy observations and sparse rewards; **Memory-Augmented Agent Training:** selects and reuses experience during learning. |
| Understanding, Evaluation & Benchmarks | **Surveys & Position Papers:** organizes definitions and open problems; **Theory & Training Dynamics:** explains why exploration changes; **Capability Boundaries:** tests whether exploration reaches beyond existing competence; **Benchmarks & Metrics:** measures diversity, coverage, efficiency, and utility. |

## Tag dimensions

Each tag dimension answers a different question. Multiple values within a
dimension are allowed when they materially describe the contribution.

| Dimension | Question answered | Meaning and examples | Why it matters |
|---|---|---|---|
| `phase` | **When** does exploration occur or change? | `data-generation`, `supervised-post-training`, `rl-training`, `inference`, `test-time-adaptation`, `continual/self-improvement` | Separates training-time distribution change from inference-time search and sampling. |
| `level` | **What object** is explored or diversified? | `token`, `response/sequence`, `trajectory/action`, `latent/representation`, `policy-distribution`, `data/task`, `population/multi-policy` | Makes the exploration granularity explicit. |
| `signal` | **What quantity** indicates exploration or guides a decision? | `entropy/probability`, `uncertainty/confidence`, `novelty/curiosity`, `semantic-diversity`, `coverage`, `information-gain`, `reward/advantage`, `disagreement` | Separates the evidence used to value exploration from the operation applied to the model. |
| `mechanism` | **How** is exploration produced or controlled? | `sampling/decoding`, `temperature-control`, `noise/perturbation`, `regularization`, `gradient-reshaping`, `reward-shaping/intrinsic-reward`, `tree-search/branching`, `structured-search`, `backtracking/resampling`, `replay/memory`, `curriculum/task-generation`, `self-play/co-evolution`, `ensemble/population` | Supports comparisons across contexts without duplicating papers. |
| `problem` | **Why** is exploration needed? | `entropy-collapse`, `mode-collapse`, `sparse-reward`, `local-optimum`, `capability-boundary`, `long-horizon`, `exploration-exploitation`, `recovery/error-correction` | Records the failure mode or trade-off a method addresses. |
| `setting` | **Where** is the method demonstrated? | `math`, `code`, `multimodal`, `creative/open-ended`, `web`, `tool-use`, `knowledge-graph`, `embodied`, `multi-agent` | Enables application-oriented browsing without turning domains into primary areas. |
| `paper_type` | **What kind of contribution** is it? | `method`, `analysis`, `benchmark`, `survey`, `position` | Distinguishes interventions from evidence-only work. |

`phase` and `level` are required. Every catalog entry also needs at least one
`signal` or `mechanism`, ensuring that exploration is concrete rather than an
incidental keyword. `problem` and `setting` are optional.

The registry preserves all applicable metadata, but generated public views show
at most three representative tags per paper. They prefer one `phase`, one
`signal`, and one `mechanism`; when one is absent, `level`, `problem`, or
`setting` supplies the missing context. Value-specific muted colors make tags
distinguishable without overwhelming the catalog.

## Entropy, temperature, and noise

These concepts are related but should not be one tag:

- **Entropy / probability** is a `signal`: it measures or describes a
  distribution and may serve as a diagnostic, target, or control input.
- **Temperature control** is a `mechanism`: it changes the shape of a sampling
  distribution.
- **Noise / perturbation** is a `mechanism`: it injects stochastic variation
  into logits, parameters, latent states, inputs, rewards, or trajectories.

Keeping them distinct preserves causal meaning. A temperature method may be
entropy-aware; a noise method may not use entropy; and an entropy analysis may
introduce no intervention.

## Worked examples

| Paper pattern | Primary area | Representative tags | Reasoning |
|---|---|---|---|
| An RLVR method preserves low-probability tokens with a regularizer | `rlvr-policy-curriculum-exploration` | phase: `rl-training`; signal: `entropy/probability`; mechanism: `regularization` | The learning update is central; entropy is the signal and regularization is the intervention. |
| A decoder branches over candidate reasoning paths at inference time | `llm-exploration` | phase: `inference`; level: `response/sequence`; mechanism: `tree-search/branching` | It explores generations without making training the contribution. |
| A web agent uses past trajectories to decide which tool to call next | `agentic-exploration` | phase: `inference`; level: `trajectory/action`; mechanism: `replay/memory` | Memory supports an external interaction loop, so it is an agentic lens rather than a primary category. |
| A web agent explores pages to collect trajectories for a policy update | `agentic-training-exploration` | phase: `rl-training`; level: `trajectory/action`; mechanism: `structured-search` | External interaction generates the learning experience, so agent training is the primary category. |
| A self-play system generates non-agent reasoning tasks and updates an LLM policy | `rlvr-policy-curriculum-exploration` | phase: `continual/self-improvement`; level: `population/multi-policy`; mechanism: `self-play/co-evolution` | Population and self-improvement describe how the policy-learning loop expands experience. |
| A benchmark measures strategy diversity in mathematical reasoning | `understanding-evaluation` | type: `benchmark`; phase: `inference`; signal: `semantic-diversity` | Measurement, rather than a new exploration intervention, is the contribution. |

## Scope boundaries

Traditional non-LLM reinforcement-learning exploration is not part of the main
catalog. A small background appendix keeps only a handful of foundational ideas
that provide vocabulary or mechanisms still used in LLM exploration. These
references are intentionally not counted in catalog totals.

The following are also excluded unless exploration is a primary contribution:

- generic RL or policy-optimization papers;
- generic test-time scaling or search papers concerned only with efficiency or
  accuracy;
- generic agent frameworks, self-improvement, memory, or self-play systems;
- diversity papers where diversity is merely a dataset or evaluation property;
- papers matched only by words such as *entropy*, *noise*, *policy*, or
  *exploration* in an unrelated sense.

This boundary keeps the list useful as a map of **LLM exploration research**, not
as a broad bibliography of adjacent machine-learning topics.
