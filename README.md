<div align="center">

# Awesome Exploration

**A curated research map of exploration in language models, RLVR, and agents.**

[![Curated catalog](https://img.shields.io/badge/catalog-curated-3B82F6?style=flat-square)](docs/CURATION_2026.md) [![254 papers](https://img.shields.io/badge/papers-254-8B5CF6?style=flat-square)](#catalog) [![Four research tracks](https://img.shields.io/badge/tracks-4-10B981?style=flat-square)](#research-map) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-F59E0B?style=flat-square)](CONTRIBUTING.md)

[Guide](#guide) · [Research map](#research-map) · [Start here](#start-here) · [Catalog](#catalog) · [Detailed metadata](README_DETAILED.md) · [Contribute](CONTRIBUTING.md)

</div>

## Guide

| Start here | What you will find |
|---|---|
| **[What counts as exploration](#what-counts-as-exploration)** | Our scope: exploration must be a concrete research variable, not only a keyword. |
| **[Research map](#research-map)** | The four places exploration occurs: generation, RLVR, agents, and evaluation. |
| **[Taxonomy lens](#taxonomy-lens)** | How phase, level, signal, mechanism, problem, and setting describe each paper. |
| **[Start here](#start-here)** | A cross-section of recommended papers for first-time readers. |
| **[Full catalog](#catalog)** | All curated papers, grouped by their primary research context. |

## What counts as exploration?

> This repository treats exploration as a **primary research variable**: a paper must identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. Generic RL, agents, test-time scaling, self-improvement, and diversity work are excluded when exploration is merely incidental.

> Evidence snapshot: **2026-07-19** · [Taxonomy design](docs/TAXONOMY.md) · [2026 curation notes](docs/CURATION_2026.md)

## Research map

Every paper has one home in the map; its tags then describe the research lens. Start with the track that matches your question, then use the tags to compare mechanisms across tracks.

| Track | Best for |
|---|---|
| **[LLM Generation & Inference](#1-llm-generation--inference-exploration)** | Sampling, decoding, reasoning-path search, and output diversity without an RL update. |
| **[Exploration for RLVR](#2-exploration-for-rlvr)** | Entropy collapse, rollout diversity, reward shaping, and policy-distribution control during training. |
| **[Agentic Exploration](#3-agentic-exploration)** | Web, tool, GUI, knowledge-graph, embodied, or multi-agent trajectories. |
| **[Understanding & Evaluation](#4-understanding-evaluation--benchmarks)** | Surveys, theory, metrics, benchmarks, and evidence about exploration. |

<a id="taxonomy-lens"></a>

<details>
<summary><strong>How to read the tags</strong></summary>

The former Token / Sequence / Policy sections are now `level` tags. Entropy, temperature, and noise belong to a broad distributional-and-stochastic family, but remain separate tags because they play different causal roles.

| Tag dimension | Values |
|---|---|
| **Phase** | data generation; supervised post-training; RL training; inference; test-time adaptation; continual/self-improvement |
| **Level** | token; response/sequence; trajectory/action; latent/representation; policy distribution; data/task; population |
| **Signal** | entropy/probability; uncertainty/confidence; novelty/curiosity; semantic diversity; coverage; information gain; reward/advantage; disagreement |
| **Mechanism** | sampling/decoding; temperature control; noise/perturbation; regularization; gradient reshaping; intrinsic reward; structured/tree search; replay/memory; curriculum; self-play; ensemble/population |
| **Problem** | entropy or mode collapse; sparse reward; local optimum; capability boundary; long horizon; exploration/exploitation; recovery |
| **Setting** | math; code; multimodal; creative/open-ended; web; tool use; knowledge graph; embodied; multi-agent |

</details>

## Catalog at a glance

| Collection | Papers |
|---|---:|
| LLM Generation & Inference Exploration | 60 |
| Exploration for RLVR | 119 |
| Agentic Exploration | 45 |
| Understanding, Evaluation & Benchmarks | 30 |
| **Curated total** | **254** |

2026 peer-reviewed acceptances in the catalog:

| Venue | Papers |
|---|---:|
| ACL 2026 Findings | 35 |
| ACL 2026 Main | 26 |
| ICLR 2026 | 58 |
| ICML 2026 | 63 |
| **Accepted total** | **182** |

## Start here

- **[Representation-Based Exploration for Language Models: From Test-Time to Post-Training](https://iclr.cc/virtual/2026/poster/10009438)** — **ICLR 2026** · LLM Generation & Inference Exploration · `inference` `latent/representation` `response/sequence` `semantic-diversity` `novelty/curiosity` `reward-shaping/intrinsic-reward`
- **[Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://iclr.cc/virtual/2026/poster/10009093)** — **ICLR 2026** · LLM Generation & Inference Exploration · `inference` `response/sequence` `entropy/probability` `semantic-diversity` `sampling/decoding`
- **[Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward](https://aclanthology.org/2026.findings-acl.1209/)** — **ACL 2026 Findings** · Exploration for RLVR · `rl-training` `token` `policy-distribution` `entropy/probability` `regularization`
- **[Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://icml.cc/virtual/2026/poster/63287)** — **ICML 2026** · Agentic Exploration · `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping`
- **[Go-Browse: Training Web Agents with Structured Exploration](https://iclr.cc/virtual/2026/poster/10010264)** — **ICLR 2026** · Agentic Exploration · `inference` `trajectory/action` `structured-search`
- **[CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](https://iclr.cc/virtual/2026/poster/10011417)** — **ICLR 2026** · Exploration for RLVR · `rl-training` `policy-distribution` `novelty/curiosity` `uncertainty/confidence` `reward-shaping/intrinsic-reward`
- **[Outcome-based Exploration for LLM Reasoning](https://arxiv.org/abs/2509.06941)** — arXiv · Exploration for RLVR · `rl-training` `response/sequence` `policy-distribution` `reward/advantage` `semantic-diversity` `reward-shaping/intrinsic-reward`
- **[From Trial-and-Error to Improvement: A Systematic Analysis of LLM Exploration Mechanisms in RLVR](https://arxiv.org/abs/2508.07534)** — arXiv · Understanding, Evaluation & Benchmarks · `rl-training` `policy-distribution` `structured-search`
- **[Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2506.01939)** — arXiv · Exploration for RLVR · `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping`
- **[ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://arxiv.org/abs/2505.24864)** — arXiv · Exploration for RLVR · `rl-training` `policy-distribution` `coverage` `regularization`
- **[The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](https://arxiv.org/abs/2505.22617)** — arXiv · Exploration for RLVR · `rl-training` `policy-distribution` `entropy/probability` `regularization` `gradient-reshaping`
- **[DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)** — arXiv · Exploration for RLVR · `rl-training` `policy-distribution` `entropy/probability` `sampling/decoding` `gradient-reshaping`
- **[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291)** — TMLR 2024 · Agentic Exploration · `continual/self-improvement` `trajectory/action` `data/task` `novelty/curiosity` `coverage` `curriculum/task-generation`
- **[Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://proceedings.mlr.press/v235/zhou24r.html)** — ICML 2024 · Agentic Exploration · `inference` `trajectory/action` `reward/advantage` `tree-search/branching` `replay/memory`
- **[Reasoning with Language Model is Planning with World Model](https://aclanthology.org/2023.emnlp-main.507/)** — EMNLP 2023 · LLM Generation & Inference Exploration · `inference` `response/sequence` `trajectory/action` `reward/advantage` `tree-search/branching`
- **[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html)** — NeurIPS 2023 · LLM Generation & Inference Exploration · `inference` `response/sequence` `reward/advantage` `coverage` `tree-search/branching` `backtracking/resampling`
- **[Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://iclr.cc/virtual/2023/poster/11718)** — ICLR 2023 · LLM Generation & Inference Exploration · `inference` `response/sequence` `semantic-diversity` `sampling/decoding` `ensemble/population`
- **[Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html)** — NeurIPS 2023 · Agentic Exploration · `test-time-adaptation` `trajectory/action` `reward/advantage` `replay/memory`
- **[ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X)** — ICLR 2023 · Agentic Exploration · `inference` `trajectory/action` `information-gain` `structured-search`

<a id="catalog"></a>

## Catalog

## 1. LLM Generation & Inference Exploration

> **Research focus.** This category covers exploration that happens while a language model is generating or selecting candidate outputs, rather than through a reinforcement-learning update. Typical examples include sampling and decoding strategies, self-consistency, semantic-diversity methods, latent-state steering, and tree or graph search at inference time.

The central question is how to search a model's existing generative distribution more broadly, safely, or efficiently. Papers belong here when the main contribution improves or analyzes candidate generation, reasoning-path search, or output diversity without making RL post-training the core mechanism.

| Evidence | Paper | Research lens |
|---|---|---|
| arXiv | [From Noise to Diversity: Random Embedding Injection in LLM Reasoning](https://arxiv.org/abs/2605.11936) | `inference` `latent/representation` `semantic-diversity` `noise/perturbation` |
| **ICLR 2026** | [e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs](https://iclr.cc/virtual/2026/poster/10008718) | `inference` `response/sequence` `structured-search` |
| **ICML 2026** | [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://icml.cc/virtual/2026/poster/60489) | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` |
| **ACL 2026 Main** | [Uncertainty-Aware Test-Time Search for Optimization Problem Solving](https://aclanthology.org/2026.acl-long.1975/) | `inference` `response/sequence` `uncertainty/confidence` `structured-search` |
| **ICML 2026** | [Towards Diverse Scientific Hypothesis Search with Large Language Models](https://icml.cc/virtual/2026/poster/66259) | `inference` `response/sequence` `semantic-diversity` `structured-search` |
| **ICLR 2026** | [Thought Branches: Interpreting LLM Reasoning Requires Resampling](https://iclr.cc/virtual/2026/poster/10008605) | `inference` `response/sequence` `sampling/decoding` `tree-search/branching` |
| **ACL 2026 Findings** | [Think Earlier, Not Longer: Prompt Optimization via Reducing Unhealthy Exploration](https://aclanthology.org/2026.findings-acl.817/) | `inference` `data/task` `structured-search` |
| **ACL 2026 Main** | [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](https://aclanthology.org/2026.acl-long.200/) | `inference` `response/sequence` `entropy/probability` `temperature-control` |
| **ICML 2026** | [The Geometric Reasoner: Manifold-Informed Latent Foresight Search for Long-Context Reasoning](https://icml.cc/virtual/2026/poster/61787) | `inference` `latent/representation` `structured-search` |
| **ICLR 2026** | [TS$^2$: Training with Sparsemax+, Testing with Softmax for Accurate and Diverse LLM Fine-Tuning](https://iclr.cc/virtual/2026/poster/10010811) | `inference` `response/sequence` `semantic-diversity` |
| **ACL 2026 Main** | [Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration](https://aclanthology.org/2026.acl-long.761/) | `inference` `response/sequence` `structured-search` |
| **ICLR 2026** | [String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation](https://iclr.cc/virtual/2026/poster/10007633) | `inference` `response/sequence` `data/task` `entropy/probability` `semantic-diversity` |
| **ACL 2026 Main** | [SeDev: Structured Semantic Exploration for LLM-Driven Code Generation](https://aclanthology.org/2026.acl-long.1641/) | `inference` `response/sequence` `structured-search` |
| **ICML 2026** | [Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening](https://icml.cc/virtual/2026/poster/63925) | `inference` `response/sequence` `entropy/probability` `sampling/decoding` |
| **ICLR 2026** | [Sample Smart, Not Hard: Correctness-First Decoding for Better Reasoning in LLMs](https://iclr.cc/virtual/2026/poster/10007335) | `inference` `response/sequence` `sampling/decoding` |
| **ACL 2026 Main** | [SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning](https://aclanthology.org/2026.acl-short.54/) | `supervised-post-training` `response/sequence` `semantic-diversity` |
| **ICLR 2026** | [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](https://iclr.cc/virtual/2026/poster/10009438) | `inference` `latent/representation` `response/sequence` `semantic-diversity` `novelty/curiosity` `reward-shaping/intrinsic-reward` |
| **ACL 2026 Findings** | [Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning](https://aclanthology.org/2026.findings-acl.1085/) | `inference` `response/sequence` `sampling/decoding` |
| **ICLR 2026** | [Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://iclr.cc/virtual/2026/poster/10009093) | `inference` `response/sequence` `entropy/probability` `semantic-diversity` `sampling/decoding` |
| **ICLR 2026** | [Post-training Large Language Models for Diverse High-Quality Responses](https://iclr.cc/virtual/2026/poster/10010944) | `supervised-post-training` `response/sequence` `semantic-diversity` |
| **ICML 2026** | [One-shot Entropy Minimization for Language Model Reasoning](https://icml.cc/virtual/2026/poster/66725) | `inference` `response/sequence` `entropy/probability` |
| **ACL 2026 Findings** | [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](https://aclanthology.org/2026.findings-acl.1149/) | `inference` `response/sequence` `structured-search` |
| **ACL 2026 Findings** | [Multi-LLM Collaborative Search for Complex Problem Solving](https://aclanthology.org/2026.findings-acl.2115/) | `inference` `population/multi-policy` `ensemble/population` |
| **ACL 2026 Main** | [ModeX: Evaluator-Free Best-of-N Selection for Open-Ended Generation](https://aclanthology.org/2026.acl-long.655/) | `inference` `response/sequence` `sampling/decoding` |
| **ACL 2026 Main** | [Learning Diverse Responses with Prefix-Conditioned Supervised Fine-Tuning](https://aclanthology.org/2026.acl-long.9/) | `supervised-post-training` `response/sequence` `semantic-diversity` |
| **ICML 2026** | [Large Language Models Explore by Latent Distilling](https://icml.cc/virtual/2026/poster/63542) | `inference` `latent/representation` `structured-search` |
| **ACL 2026 Main** | [Language of Thought Shapes Output Diversity in Large Language Models](https://aclanthology.org/2026.acl-long.628/) | `inference` `response/sequence` `semantic-diversity` |
| **ICML 2026** | [HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction](https://icml.cc/virtual/2026/poster/65181) | `inference` `response/sequence` `tree-search/branching` |
| **ICLR 2026** | [GuidedSampling: Steering LLMs Towards Diverse Candidate Solutions at Inference-Time](https://iclr.cc/virtual/2026/poster/10009336) | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` `noise/perturbation` |
| **ICML 2026** | [From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models](https://icml.cc/virtual/2026/poster/65555) | `inference` `response/sequence` `sampling/decoding` |
| **ICLR 2026** | [Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering](https://iclr.cc/virtual/2026/poster/10006851) | `inference` `response/sequence` `latent/representation` `semantic-diversity` `noise/perturbation` |
| **ICML 2026** | [Escaping Mode Collapse in LLM Generation](https://icml.cc/virtual/2026/poster/65524) | `inference` `response/sequence` `structured-search` |
| **ICML 2026** | [Entropy-informed Decoding: Adaptive Information-Driven Branching](https://icml.cc/virtual/2026/poster/61896) | `inference` `response/sequence` `entropy/probability` `sampling/decoding` `tree-search/branching` |
| **ICML 2026** | [Entropy-Aware On-Policy Distillation of Language Models](https://icml.cc/virtual/2026/poster/64855) | `supervised-post-training` `policy-distribution` `entropy/probability` |
| **ICML 2026** | [Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models](https://icml.cc/virtual/2026/poster/64102) | `inference` `response/sequence` `structured-search` |
| **ICML 2026** | [EAGer: Entropy-Aware GEneRation for Adaptive Inference-Time Scaling](https://icml.cc/virtual/2026/poster/65185) | `inference` `response/sequence` `entropy/probability` |
| **ICML 2026** | [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](https://icml.cc/virtual/2026/poster/63569) | `inference` `response/sequence` `semantic-diversity` |
| **ICLR 2026** | [Diverse Text Decoding via Iterative Reweighting](https://iclr.cc/virtual/2026/poster/10011729) | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` |
| **ACL 2026 Main** | [Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning](https://aclanthology.org/2026.acl-long.1231/) | `inference` `response/sequence` `structured-search` |
| **ICLR 2026** | [Differential Fine-Tuning Large Language Models Towards Better Diverse Reasoning Abilities](https://iclr.cc/virtual/2026/poster/10008716) | `inference` `response/sequence` `semantic-diversity` |
| **ICML 2026** | [D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning](https://icml.cc/virtual/2026/poster/63783) | `inference` `response/sequence` `entropy/probability` `semantic-diversity` |
| **ICLR 2026** | [Continuous Chain of Thought Enables Parallel Exploration and Reasoning](https://iclr.cc/virtual/2026/poster/10007055) | `inference` `response/sequence` `structured-search` |
| **ACL 2026 Findings** | [ConMA : Confidence-Guided Kernel Sampling with Multi-Stage Aggregation for LLM Reasoning](https://aclanthology.org/2026.findings-acl.1475/) | `inference` `response/sequence` `uncertainty/confidence` `sampling/decoding` |
| **ACL 2026 Findings** | [Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search](https://aclanthology.org/2026.findings-acl.214/) | `inference` `response/sequence` `tree-search/branching` |
| **ICML 2026** | [Cache Coherent Resampling for Efficient Test Time Scaling in LLM Reasoning via Adaptive Sequential Monte Carlo](https://icml.cc/virtual/2026/poster/64829) | `inference` `response/sequence` `sampling/decoding` `backtracking/resampling` |
| **ACL 2026 Findings** | [Beyond Templates: Dynamic Adaptation of Reasoning Demonstrations via Feasibility-Aware Exploration](https://aclanthology.org/2026.findings-acl.327/) | `inference` `data/task` `structured-search` |
| **ACL 2026 Findings** | [Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.390/) | `inference` `trajectory/action` `sampling/decoding` |
| **ICML 2026** | [Beyond Logits: Metastable Latent Dynamics for Sample-Efficient Best-of-N Selection in LLMs](https://icml.cc/virtual/2026/poster/66569) | `inference` `token` `latent/representation` `sampling/decoding` |
| **ICML 2026** | [Annotations Mitigate Post-Training Mode Collapse](https://icml.cc/virtual/2026/poster/63468) | `supervised-post-training` `response/sequence` `structured-search` |
| **ICML 2026** | [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](https://icml.cc/virtual/2026/poster/63795) | `inference` `token` `structured-search` |
| arXiv | [Think Before You Retrieve: Learning Test-Time Adaptive Search with Small Language Models](https://arxiv.org/abs/2511.07581) | `inference` `response/sequence` `structured-search` |
| arXiv | [SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search](https://arxiv.org/abs/2510.16916) | `inference` `response/sequence` `structured-search` |
| arXiv | [The Road Less Traveled: Enhancing Exploration in LLMs via Sequential Sampling](https://arxiv.org/abs/2510.15502) | `inference` `response/sequence` `sampling/decoding` |
| arXiv | [Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation](https://arxiv.org/abs/2509.15194) | `inference` `response/sequence` `novelty/curiosity` |
| arXiv | [Learning from Diverse Reasoning Paths with Routing and Collaboration](https://arxiv.org/abs/2508.16861) | `inference` `response/sequence` `semantic-diversity` |
| arXiv | [COS(M+O)S: Curiosity and RL-Enhanced MCTS for Exploring Story Space via Language Models](https://arxiv.org/abs/2501.17104) | `inference` `response/sequence` `novelty/curiosity` `tree-search/branching` |
| EMNLP 2023 | [Reasoning with Language Model is Planning with World Model](https://aclanthology.org/2023.emnlp-main.507/) | `inference` `response/sequence` `trajectory/action` `reward/advantage` `tree-search/branching` |
| arXiv | [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687) | `inference` `response/sequence` `semantic-diversity` `tree-search/branching` `structured-search` |
| NeurIPS 2023 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html) | `inference` `response/sequence` `reward/advantage` `coverage` `tree-search/branching` `backtracking/resampling` |
| ICLR 2023 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://iclr.cc/virtual/2023/poster/11718) | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` `ensemble/population` |

## 2. Exploration for RLVR

> **Research focus.** This category concerns exploration during reinforcement learning or RL with verifiable rewards (RLVR). Here, exploration changes which rollouts are collected, how reward or advantage signals are assigned, or how the policy distribution is updated during training.

It includes work on entropy or mode collapse, low-probability tokens, rollout diversity, intrinsic or shaped rewards, gradient and regularization interventions, curriculum design, and attempts to push beyond a base model's capability boundary. The defining feature is that exploration is part of the learning loop, not only an inference-time search choice.

| Evidence | Paper | Research lens |
|---|---|---|
| arXiv | [Entropy Polarity in Reinforcement Fine-Tuning: Direction, Asymmetry, and Control](https://arxiv.org/abs/2605.11775) | `rl-training` `policy-distribution` `entropy/probability` |
| arXiv | [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](https://arxiv.org/abs/2605.11461) | `rl-training` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| arXiv | [Exploration-Driven Optimization for Test-Time Large Language Model Reasoning](https://arxiv.org/abs/2605.09853) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control](https://arxiv.org/abs/2604.26326) | `rl-training` `policy-distribution` `entropy/probability` |
| arXiv | [DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off](https://arxiv.org/abs/2604.13902) | `rl-training` `policy-distribution` `gradient-reshaping` |
| arXiv | [Policy Split: Incentivizing Dual-Mode Exploration in LLM Reinforcement with Dual-Mode Entropy Regularization](https://arxiv.org/abs/2604.11510) | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| arXiv | [Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems](https://arxiv.org/abs/2604.04767) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [Bootstrapping Exploration with Group-Level Natural Language Feedback in Reinforcement Learning](https://arxiv.org/abs/2603.04597) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning](https://arxiv.org/abs/2602.22642) | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| arXiv | [UpSkill: Mutual Information Skill Learning for Structured Response Diversity in LLMs](https://arxiv.org/abs/2602.22296) | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` `information-gain` |
| arXiv | [DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning](https://arxiv.org/abs/2602.19895) | `rl-training` `policy-distribution` `semantic-diversity` `regularization` |
| arXiv | [MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2602.17550) | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| arXiv | [Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/abs/2602.13035) | `rl-training` `policy-distribution` `entropy/probability` `temperature-control` |
| arXiv | [Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities](https://arxiv.org/abs/2602.05281) | `rl-training` `token` `policy-distribution` `entropy/probability` `structured-search` |
| arXiv | [Entropy-Gated Selective Policy Optimization:Token-Level Gradient Allocation for Hybrid Training of Large Language Models](https://arxiv.org/abs/2602.03309) | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| arXiv | [Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models](https://arxiv.org/abs/2601.22478) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning](https://icml.cc/virtual/2026/poster/66494) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [XRPO: Pushing the Limits of GRPO with Targeted Exploration and Exploitation](https://icml.cc/virtual/2026/poster/65777) | `rl-training` `policy-distribution` `structured-search` |
| **ACL 2026 Findings** | [VANE: Guiding High-Value Exploration in RLVR via Outcome-Process Novelty Shaping](https://aclanthology.org/2026.findings-acl.1434/) | `rl-training` `policy-distribution` `novelty/curiosity` `reward/advantage` `reward-shaping/intrinsic-reward` |
| **ACL 2026 Findings** | [Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning](https://aclanthology.org/2026.findings-acl.951/) | `rl-training` `policy-distribution` `uncertainty/confidence` `reward/advantage` `gradient-reshaping` |
| **ICLR 2026** | [Token Hidden Reward: Steering Exploration-Exploitation in Group Relative Deep Reinforcement Learning](https://iclr.cc/virtual/2026/poster/10008016) | `rl-training` `token` `policy-distribution` `reward/advantage` `noise/perturbation` |
| **ACL 2026 Main** | [Temporal Sampling for Forgotten Reasoning in LLMs](https://aclanthology.org/2026.acl-long.1305/) | `rl-training` `policy-distribution` `sampling/decoding` |
| **ACL 2026 Findings** | [Targeted Exploration via Unified Entropy Control for Reinforcement Learning](https://aclanthology.org/2026.findings-acl.828/) | `rl-training` `policy-distribution` `entropy/probability` `structured-search` |
| **ICML 2026** | [Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO](https://icml.cc/virtual/2026/poster/64272) | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| **ACL 2026 Findings** | [Semantic-Space Exploration and Exploitation in RLVR for LLM Reasoning](https://aclanthology.org/2026.findings-acl.1915/) | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| **ICLR 2026** | [Selective Expert Guidance for Effective and Diverse Exploration in Reinforcement Learning of LLMs](https://iclr.cc/virtual/2026/poster/10008654) | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| **ICML 2026** | [SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning](https://icml.cc/virtual/2026/poster/60895) | `rl-training` `policy-distribution` `reward/advantage` `reward-shaping/intrinsic-reward` |
| **ACL 2026 Findings** | [SPS: Steering Probability Squeezing for Better Exploration in Reinforcement Learning for Large Language Models](https://aclanthology.org/2026.findings-acl.865/) | `rl-training` `token` `policy-distribution` `entropy/probability` `noise/perturbation` `gradient-reshaping` |
| **ICML 2026** | [SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs](https://icml.cc/virtual/2026/poster/63563) | `rl-training` `policy-distribution` `regularization` |
| **ICLR 2026** | [Risk-Sensitive Reinforcement Learning for Alleviating Exploration Dilemmas in Large Language Models](https://iclr.cc/virtual/2026/poster/10011269) | `rl-training` `policy-distribution` `structured-search` |
| **ACL 2026 Findings** | [Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://aclanthology.org/2026.findings-acl.1982/) | `rl-training` `policy-distribution` `novelty/curiosity` `reward/advantage` `reward-shaping/intrinsic-reward` |
| **ICML 2026** | [Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](https://icml.cc/virtual/2026/poster/65737) | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| **ICML 2026** | [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](https://icml.cc/virtual/2026/poster/66546) | `supervised-post-training` `latent/representation` `policy-distribution` `sampling/decoding` |
| **ICML 2026** | [ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning](https://icml.cc/virtual/2026/poster/62006) | `rl-training` `policy-distribution` `structured-search` |
| **ACL 2026 Main** | [Reinforced Efficient Reasoning via Semantically Diverse Exploration](https://aclanthology.org/2026.acl-long.2216/) | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| **ACL 2026 Findings** | [Reasoning-Guided Exploration for Online DPO](https://aclanthology.org/2026.findings-acl.1370/) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [On Entropy Control in LLM-RL Algorithms](https://iclr.cc/virtual/2026/poster/10010002) | `rl-training` `policy-distribution` `entropy/probability` |
| **ICLR 2026** | [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://iclr.cc/virtual/2026/poster/10007755) | `rl-training` `policy-distribution` `data/task` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| **ACL 2026 Findings** | [Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward](https://aclanthology.org/2026.findings-acl.1209/) | `rl-training` `token` `policy-distribution` `entropy/probability` `regularization` |
| **ICLR 2026** | [Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards](https://iclr.cc/virtual/2026/poster/10011530) | `rl-training` `response/sequence` `trajectory/action` `reward/advantage` `tree-search/branching` |
| **ICML 2026** | [Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization](https://icml.cc/virtual/2026/poster/62699) | `rl-training` `policy-distribution` `information-gain` `gradient-reshaping` `tree-search/branching` |
| **ACL 2026 Main** | [Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models](https://aclanthology.org/2026.acl-long.617/) | `supervised-post-training` `policy-distribution` `entropy/probability` |
| **ICML 2026** | [Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation](https://icml.cc/virtual/2026/poster/60948) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [Incentivizing LLM Reasoning via Reinforcement Learning with Functional Monte Carlo Tree Search](https://iclr.cc/virtual/2026/poster/10007699) | `rl-training` `policy-distribution` `tree-search/branching` |
| **ACL 2026 Findings** | [How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization](https://aclanthology.org/2026.findings-acl.724/) | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| **ACL 2026 Main** | [HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment](https://aclanthology.org/2026.acl-long.1418/) | `rl-training` `policy-distribution` `entropy/probability` `semantic-diversity` `reward-shaping/intrinsic-reward` |
| **ACL 2026 Main** | [Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence](https://aclanthology.org/2026.acl-long.739/) | `rl-training` `policy-distribution` `uncertainty/confidence` |
| **ICML 2026** | [GeoAlign: Geometric Rollout Curation for Robust LLM Reinforcement Learning](https://icml.cc/virtual/2026/poster/60634) | `rl-training` `response/sequence` `policy-distribution` `structured-search` |
| **ICML 2026** | [GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy](https://icml.cc/virtual/2026/poster/65174) | `rl-training` `token` `response/sequence` `entropy/probability` `reward/advantage` `reward-shaping/intrinsic-reward` |
| **ACL 2026 Main** | [Free Energy-Driven Reinforcement Learning with Adaptive Advantage Shaping for Unsupervised Reasoning in LLMs](https://aclanthology.org/2026.acl-long.797/) | `rl-training` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| **ACL 2026 Findings** | [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](https://aclanthology.org/2026.findings-acl.1520/) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs](https://icml.cc/virtual/2026/poster/65561) | `rl-training` `policy-distribution` `replay/memory` |
| **ICLR 2026** | [Expanding Reasoning Potential in Foundation Model by Learning Diverse Chains of Thought Patterns](https://iclr.cc/virtual/2026/poster/10011658) | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` |
| **ACL 2026 Findings** | [EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning for LLMs](https://aclanthology.org/2026.findings-acl.1031/) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [Escaping Policy Contraction: Contraction-Aware PPO (CaPPO) for Stable Language Model Fine-Tuning](https://iclr.cc/virtual/2026/poster/10006831) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [Entropy-preserving reinforcement learning](https://iclr.cc/virtual/2026/poster/10010707) | `rl-training` `policy-distribution` `entropy/probability` |
| **ACL 2026 Findings** | [Entropy-Aware Reshaping of Reinforcement Signals for Multi-Answer Reasoning](https://aclanthology.org/2026.findings-acl.2001/) | `rl-training` `policy-distribution` `entropy/probability` |
| **ACL 2026 Findings** | [Entropy Scheduling in Reinforcement Learning for Large Language Models](https://aclanthology.org/2026.findings-acl.206/) | `rl-training` `policy-distribution` `entropy/probability` |
| **ICLR 2026** | [Empowering Small VLMs to Think with Dynamic Memorization and Exploration](https://iclr.cc/virtual/2026/poster/10007260) | `rl-training` `policy-distribution` `structured-search` |
| **ACL 2026 Main** | [ETR: Entropy Trend Reward for Efficient Chain-of-Thought Reasoning](https://aclanthology.org/2026.acl-long.799/) | `rl-training` `response/sequence` `policy-distribution` `entropy/probability` `reward/advantage` |
| **ICLR 2026** | [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://iclr.cc/virtual/2026/poster/10009769) | `rl-training` `policy-distribution` `gradient-reshaping` |
| **ICML 2026** | [ECHO: Entropy-Confidence Hybrid Optimization for Test-Time Reinforcement Learning](https://icml.cc/virtual/2026/poster/63137) | `rl-training` `policy-distribution` `entropy/probability` `uncertainty/confidence` |
| **ICLR 2026** | [Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](https://iclr.cc/virtual/2026/poster/10006780) | `rl-training` `policy-distribution` `sampling/decoding` |
| **ACL 2026 Findings** | [Dynamic Sampling that Adapts: Self-Aware Iterative Data Persistent Optimization for Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.1412/) | `rl-training` `policy-distribution` `data/task` `sampling/decoding` |
| **ICLR 2026** | [Do Not Let Low-Probability Tokens Over-Dominate in RL for LLMs](https://iclr.cc/virtual/2026/poster/10010601) | `rl-training` `token` `policy-distribution` `entropy/probability` |
| **ICLR 2026** | [Diversity-Incentivized Exploration for Versatile Reasoning](https://iclr.cc/virtual/2026/poster/10011130) | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| **ICLR 2026** | [Diversity-Enhanced Reasoning for Subjective Questions](https://iclr.cc/virtual/2026/poster/10011855) | `rl-training` `policy-distribution` `semantic-diversity` |
| **ICML 2026** | [Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration](https://icml.cc/virtual/2026/poster/60955) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Tree-based Search](https://iclr.cc/virtual/2026/poster/10010078) | `rl-training` `policy-distribution` `coverage` `reward/advantage` `tree-search/branching` `replay/memory` |
| **ACL 2026 Findings** | [DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.685/) | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` |
| **ACL 2026 Main** | [DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing](https://aclanthology.org/2026.acl-long.647/) | `rl-training` `policy-distribution` `semantic-diversity` `tree-search/branching` |
| **ICML 2026** | [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](https://icml.cc/virtual/2026/poster/61634) | `rl-training` `response/sequence` `trajectory/action` `entropy/probability` |
| **ACL 2026 Findings** | [DARL: Encouraging Diverse Answers for General Reasoning without Verifiers](https://aclanthology.org/2026.findings-acl.1530/) | `rl-training` `policy-distribution` `semantic-diversity` |
| **ICLR 2026** | [Count Counts: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards](https://iclr.cc/virtual/2026/poster/10011073) | `rl-training` `policy-distribution` `reward/advantage` `reward-shaping/intrinsic-reward` |
| **ICLR 2026** | [Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning](https://iclr.cc/virtual/2026/poster/10011411) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [Contextual Rollout Bandits for Reinforcement Learning with Verifiable Rewards](https://icml.cc/virtual/2026/poster/60796) | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` |
| **ACL 2026 Main** | [CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://aclanthology.org/2026.acl-long.1376/) | `rl-training` `policy-distribution` `disagreement` `self-play/co-evolution` |
| **ICLR 2026** | [CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](https://iclr.cc/virtual/2026/poster/10011417) | `rl-training` `policy-distribution` `novelty/curiosity` `uncertainty/confidence` `reward-shaping/intrinsic-reward` |
| **ICML 2026** | [BroRL: Scaling Reinforcement Learning via Broadened Exploration](https://icml.cc/virtual/2026/poster/64690) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning](https://icml.cc/virtual/2026/poster/64959) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [Beyond Mode Collapse: Distribution Matching for Diverse Reasoning](https://icml.cc/virtual/2026/poster/65266) | `rl-training` `policy-distribution` `entropy/probability` `semantic-diversity` |
| **ICLR 2026** | [Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning](https://iclr.cc/virtual/2026/poster/10006770) | `rl-training` `policy-distribution` `structured-search` |
| **ACL 2026 Findings** | [Beyond High-Entropy Exploration: Correctness-Aware Low-Entropy Segment-Based Advantage Shaping for Reasoning LLMs](https://aclanthology.org/2026.findings-acl.1650/) | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| **ICML 2026** | [Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization](https://icml.cc/virtual/2026/poster/61727) | `rl-training` `policy-distribution` `gradient-reshaping` |
| **ICLR 2026** | [Attention as a Compass: Efficient Exploration for Process-Supervised RL in Reasoning Models](https://iclr.cc/virtual/2026/poster/10009884) | `rl-training` `policy-distribution` `structured-search` |
| **ICML 2026** | [Anchored Policy Optimization: Mitigating Exploration Collapse via Support-Constrained Rectification](https://icml.cc/virtual/2026/poster/65360) | `rl-training` `policy-distribution` `regularization` `gradient-reshaping` |
| **ICLR 2026** | [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](https://iclr.cc/virtual/2026/poster/10011711) | `rl-training` `token` `policy-distribution` `entropy/probability` |
| **ACL 2026 Findings** | [A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning](https://aclanthology.org/2026.findings-acl.641/) | `rl-training` `token` `policy-distribution` `entropy/probability` |
| arXiv | [Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2512.15687) | `rl-training` `policy-distribution` `gradient-reshaping` |
| arXiv | [Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning](https://arxiv.org/abs/2512.04359) | `rl-training` `token` `policy-distribution` `entropy/probability` |
| arXiv | [From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training](https://arxiv.org/abs/2511.07738) | `rl-training` `policy-distribution` `entropy/probability` `noise/perturbation` |
| arXiv | [Explore Data Left Behind in Reinforcement Learning for Reasoning Language Models](https://arxiv.org/abs/2511.04800) | `rl-training` `policy-distribution` `data/task` `structured-search` |
| arXiv | [Scheduling Your LLM Reinforcement Learning with Reasoning Trees](https://arxiv.org/abs/2510.24832) | `rl-training` `policy-distribution` `tree-search/branching` |
| arXiv | [Revisiting Entropy Regularization: Adaptive Coefficient Unlocks Its Potential for LLM Reinforcement Learning](https://arxiv.org/abs/2510.10959) | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| arXiv | [Let it Calm: Exploratory Annealed Decoding for Verifiable Reinforcement Learning](https://arxiv.org/abs/2510.05251) | `rl-training` `policy-distribution` `sampling/decoding` |
| arXiv | [More Than One Teacher: Adaptive Multi-Guidance Policy Optimization for Diverse Exploration](https://arxiv.org/abs/2510.02227) | `rl-training` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| arXiv | [Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models](https://arxiv.org/abs/2509.26114) | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| arXiv | [CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning](https://arxiv.org/abs/2509.20712) | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| arXiv | [Outcome-based Exploration for LLM Reasoning](https://arxiv.org/abs/2509.06941) | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` `semantic-diversity` `reward-shaping/intrinsic-reward` |
| arXiv | [Know When to Explore: Difficulty-Aware Certainty as a Guide for LLM Reinforcement Learning](https://arxiv.org/abs/2509.00125) | `rl-training` `policy-distribution` `uncertainty/confidence` `structured-search` |
| arXiv | [ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism](https://arxiv.org/abs/2508.11356) | `rl-training` `policy-distribution` `entropy/probability` `structured-search` |
| arXiv | [CURE: Critical-Token-Guided Re-Concatenation for Entropy-Collapse Prevention](https://arxiv.org/abs/2508.11016) | `rl-training` `token` `policy-distribution` `entropy/probability` |
| arXiv | [AMFT: Aligning LLM Reasoners by Meta-Learning the Optimal Imitation-Exploration Balance](https://arxiv.org/abs/2508.06944) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [Decomposing the Entropy-Performance Exchange: The Missing Keys to Unlocking Effective Reinforcement Learning](https://arxiv.org/abs/2508.02260) | `rl-training` `policy-distribution` `entropy/probability` |
| arXiv | [RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization](https://arxiv.org/abs/2508.00222) | `rl-training` `policy-distribution` `gradient-reshaping` |
| arXiv | [RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning](https://arxiv.org/abs/2507.07451) | `rl-training` `policy-distribution` `replay/memory` |
| arXiv | [EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework](https://arxiv.org/abs/2506.22200) | `rl-training` `policy-distribution` `replay/memory` |
| arXiv | [TreeRL: LLM Reinforcement Learning with On-Policy Tree Search](https://arxiv.org/abs/2506.11902) | `rl-training` `policy-distribution` `tree-search/branching` |
| arXiv | [R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2506.04185) | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| arXiv | [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2506.01939) | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| arXiv | [ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://arxiv.org/abs/2505.24864) | `rl-training` `policy-distribution` `coverage` `regularization` |
| arXiv | [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](https://arxiv.org/abs/2505.22617) | `rl-training` `policy-distribution` `entropy/probability` `regularization` `gradient-reshaping` |
| arXiv | [PPO-BR: Dual-Signal Entropy-Reward Adaptation for Trust Region Policy Optimization](https://arxiv.org/abs/2505.17714) | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| arXiv | [DGRO: Enhancing LLM Reasoning via Exploration-Exploitation Control and Reward Variance Management](https://arxiv.org/abs/2505.12951) | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| arXiv | [SEED-GRPO: Semantic Entropy Enhanced GRPO for Uncertainty-Aware Policy Optimization](https://arxiv.org/abs/2505.12346) | `rl-training` `policy-distribution` `entropy/probability` `uncertainty/confidence` `gradient-reshaping` |
| arXiv | [Improving RL Exploration for LLM Reasoning through Retrospective Replay](https://arxiv.org/abs/2504.14363) | `rl-training` `policy-distribution` `backtracking/resampling` `replay/memory` |
| arXiv | [Entropy-guided sequence weighting for efficient exploration in RL-based LLM fine-tuning](https://arxiv.org/abs/2503.22456) | `rl-training` `response/sequence` `policy-distribution` `entropy/probability` `structured-search` |
| arXiv | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) | `rl-training` `policy-distribution` `entropy/probability` `sampling/decoding` `gradient-reshaping` |
| arXiv | [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://arxiv.org/abs/2502.02508) | `rl-training` `response/sequence` `policy-distribution` `structured-search` |

## 3. Agentic Exploration

> **Research focus.** This category covers language agents that explore an external or persistent environment: webpages, tools, GUIs, knowledge graphs, games, embodied worlds, or multi-agent settings. The object of exploration is usually a trajectory of states, actions, observations, and tool calls rather than a single textual response.

These papers focus on challenges such as partial observability, long horizons, recovery from failed actions, memory, environment coverage, and interactive search. A paper belongs here when external interaction is central to the exploration problem and evaluation.

| Evidence | Paper | Research lens |
|---|---|---|
| arXiv | [RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization](https://arxiv.org/abs/2603.03078) | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` |
| arXiv | [AT$^2$PO: Agentic Turn-based Policy Optimization via Tree Search](https://arxiv.org/abs/2601.04767) | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` `tree-search/branching` |
| **ICML 2026** | [What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity](https://icml.cc/virtual/2026/poster/60509) | `inference` `trajectory/action` `novelty/curiosity` `structured-search` |
| **ACL 2026 Main** | [WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement](https://aclanthology.org/2026.acl-long.1456/) | `inference` `trajectory/action` `population/multi-policy` `self-play/co-evolution` |
| **ICLR 2026** | [Unlocking Long-Horizon Agentic Search with Large-Scale End-to-End RL](https://iclr.cc/virtual/2026/poster/10009929) | `inference` `trajectory/action` `structured-search` |
| **ICLR 2026** | [Towards Self-Evolving Agent Benchmarks : Validatable Agent Trajectory via Test-Time Exploration](https://iclr.cc/virtual/2026/poster/10011762) | `inference` `trajectory/action` `self-play/co-evolution` |
| **ICLR 2026** | [Toward Efficient Exploration by Large Language Model Agents](https://iclr.cc/virtual/2026/poster/10009979) | `inference` `trajectory/action` `structured-search` |
| **ICML 2026** | [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://icml.cc/virtual/2026/poster/63090) | `rl-training` `trajectory/action` `uncertainty/confidence` `structured-search` |
| **ICLR 2026** | [Search Self-Play: Pushing the Frontier of Agent Capability without Supervision](https://iclr.cc/virtual/2026/poster/10008777) | `inference` `trajectory/action` `population/multi-policy` `self-play/co-evolution` |
| **ICLR 2026** | [Scaling Synthetic Task Generation for Agents via Exploration](https://iclr.cc/virtual/2026/poster/10007463) | `data-generation` `response/sequence` `trajectory/action` `curriculum/task-generation` |
| **ACL 2026 Findings** | [SQLAgent: Learning to Explore Before Generating as a Data Engineer](https://aclanthology.org/2026.findings-acl.1959/) | `inference` `trajectory/action` `data/task` `structured-search` |
| **ICML 2026** | [SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience](https://icml.cc/virtual/2026/poster/65711) | `continual/self-improvement` `trajectory/action` `replay/memory` `self-play/co-evolution` |
| **ACL 2026 Main** | [Reinforcement Learning for Self-Improving Agent with Skill Library](https://aclanthology.org/2026.acl-long.69/) | `rl-training` `trajectory/action` `structured-search` |
| **ICML 2026** | [RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents](https://icml.cc/virtual/2026/poster/60790) | `inference` `trajectory/action` `structured-search` |
| **ICML 2026** | [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://icml.cc/virtual/2026/poster/65447) | `inference` `trajectory/action` `population/multi-policy` `semantic-diversity` `self-play/co-evolution` |
| **ACL 2026 Main** | [PExA: Parallel Exploration Agent for Complex Text-to-SQL](https://aclanthology.org/2026.acl-short.48/) | `inference` `trajectory/action` `structured-search` |
| **ICLR 2026** | [Meta-RL Induces Exploration in Language Agents](https://iclr.cc/virtual/2026/poster/10011567) | `inference` `trajectory/action` `structured-search` |
| **ACL 2026 Findings** | [MAXS: Meta-Adaptive Exploration with LLM Agents](https://aclanthology.org/2026.findings-acl.670/) | `inference` `trajectory/action` `structured-search` |
| **ICML 2026** | [Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://icml.cc/virtual/2026/poster/63287) | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` |
| **ICLR 2026** | [Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning](https://iclr.cc/virtual/2026/poster/10010088) | `rl-training` `trajectory/action` `structured-search` |
| **ACL 2026 Findings** | [LLM Inductive Reasoning Through Multi-Agent Enhanced Monte Carlo Tree Search](https://aclanthology.org/2026.findings-acl.1178/) | `inference` `trajectory/action` `population/multi-policy` `tree-search/branching` `ensemble/population` |
| **ICML 2026** | [Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents](https://icml.cc/virtual/2026/poster/63273) | `rl-training` `trajectory/action` `policy-distribution` `entropy/probability` `uncertainty/confidence` `gradient-reshaping` |
| **ICLR 2026** | [Go-Browse: Training Web Agents with Structured Exploration](https://iclr.cc/virtual/2026/poster/10010264) | `inference` `trajectory/action` `structured-search` |
| **ACL 2026 Main** | [FusionFlow: Enabling Deep Structural Exploration for Automated Agentic Workflow Generation](https://aclanthology.org/2026.acl-long.1278/) | `inference` `response/sequence` `trajectory/action` `structured-search` |
| **ICLR 2026** | [Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling](https://iclr.cc/virtual/2026/poster/10009840) | `inference` `trajectory/action` `reward/advantage` `structured-search` |
| **ICLR 2026** | [Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization](https://iclr.cc/virtual/2026/poster/10009229) | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` `replay/memory` |
| **ACL 2026 Main** | [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://aclanthology.org/2026.acl-long.1670/) | `inference` `trajectory/action` `data/task` `replay/memory` |
| **ICLR 2026** | [Dyna-Mind: Learning to Simulate from Experience for Better AI Agents](https://iclr.cc/virtual/2026/poster/10010625) | `inference` `trajectory/action` `replay/memory` |
| **ICLR 2026** | [Dual-Scale World Memory for LLM Agents towards Hard-Exploration Problems](https://iclr.cc/virtual/2026/poster/10008626) | `inference` `trajectory/action` `replay/memory` |
| **ICLR 2026** | [DreamPhase: Offline Imagination and Uncertainty-Guided Planning for Large-Language-Model Agents](https://iclr.cc/virtual/2026/poster/10011238) | `inference` `trajectory/action` `uncertainty/confidence` |
| **ACL 2026 Main** | [DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents](https://aclanthology.org/2026.acl-long.2151/) | `rl-training` `trajectory/action` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| **ICML 2026** | [DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use](https://icml.cc/virtual/2026/poster/66305) | `data-generation` `trajectory/action` `data/task` `semantic-diversity` |
| **ACL 2026 Findings** | [Chain-of-Relations: Faithful and Efficient LLM Reasoning over Knowledge Graphs via Relation-Centric Exploration](https://aclanthology.org/2026.findings-acl.2138/) | `inference` `trajectory/action` `structured-search` |
| **ACL 2026 Main** | [Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory](https://aclanthology.org/2026.acl-long.838/) | `inference` `trajectory/action` `tree-search/branching` `replay/memory` |
| **ACL 2026 Findings** | [Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search](https://aclanthology.org/2026.findings-acl.160/) | `inference` `trajectory/action` `data/task` `structured-search` |
| **ACL 2026 Findings** | [Beneficial Reasoning Behaviors in Agentic Search and Effective Training Methods to Obtain Them](https://aclanthology.org/2026.findings-acl.1400/) | `inference` `trajectory/action` `structured-search` |
| **ICML 2026** | [Backjump-on-Graph: Empowering LLMs with Reinforced Retrospective Exploration for Agentic KG Reasoning](https://icml.cc/virtual/2026/poster/61995) | `inference` `trajectory/action` `backtracking/resampling` |
| **ACL 2026 Main** | [Autonomous Knowledge Graph Exploration with Adaptive Breadth-Depth Retrieval](https://aclanthology.org/2026.acl-long.714/) | `inference` `trajectory/action` `tree-search/branching` |
| **ICML 2026** | [Active Exploring like a Pigeon: Reinforcing Spatial Reasoning via Agentic Vision-Language Models](https://icml.cc/virtual/2026/poster/61450) | `inference` `trajectory/action` `structured-search` |
| arXiv | [EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning](https://arxiv.org/abs/2509.22576) | `rl-training` `trajectory/action` `policy-distribution` `entropy/probability` `regularization` `gradient-reshaping` |
| arXiv | [Enhancing Diversity in Parallel Agents: A Maximum State Entropy Exploration Story](https://arxiv.org/abs/2505.01336) | `inference` `trajectory/action` `entropy/probability` `semantic-diversity` `structured-search` |
| TMLR 2024 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | `continual/self-improvement` `trajectory/action` `data/task` `novelty/curiosity` `coverage` `curriculum/task-generation` |
| ICML 2024 | [Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://proceedings.mlr.press/v235/zhou24r.html) | `inference` `trajectory/action` `reward/advantage` `tree-search/branching` `replay/memory` |
| NeurIPS 2023 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | `test-time-adaptation` `trajectory/action` `reward/advantage` `replay/memory` |
| ICLR 2023 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X) | `inference` `trajectory/action` `information-gain` `structured-search` |

## 4. Understanding, Evaluation & Benchmarks

> **Research focus.** This category collects empirical analyses, theoretical accounts, surveys, metrics, and benchmarks that help the field understand exploration. Rather than primarily proposing a new exploration intervention, these works measure diversity, characterize training dynamics, evaluate capability boundaries, or establish a shared vocabulary and test bed.

They are essential for judging whether a method genuinely improves exploration instead of merely changing accuracy or sampling behavior. Keeping them separate makes the evidence about a phenomenon easy to distinguish from methods designed to change it.

| Evidence | Paper | Research lens |
|---|---|---|
| arXiv | [Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning](https://arxiv.org/abs/2605.09292) | `inference` `response/sequence` `semantic-diversity` |
| **ACL 2026 Findings** | [Why Did Apple Fall: Evaluating Curiosity in Large Language Models](https://aclanthology.org/2026.findings-acl.1954/) | `inference` `response/sequence` `novelty/curiosity` |
| **ICLR 2026** | [When Greedy Wins: Emergent Exploitation Bias in Meta-Bandit LLM Training](https://iclr.cc/virtual/2026/poster/10008807) | `inference` `response/sequence` `structured-search` |
| **ICLR 2026** | [Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity](https://iclr.cc/virtual/2026/poster/10007331) | `inference` `response/sequence` `semantic-diversity` |
| **ICML 2026** | [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](https://icml.cc/virtual/2026/poster/62606) | `inference` `response/sequence` `entropy/probability` |
| **ACL 2026 Findings** | [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](https://aclanthology.org/2026.findings-acl.879/) | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| **ICML 2026** | [Understanding Reasoning Collapse in LLM Agent Reinforcement Learning](https://icml.cc/virtual/2026/poster/66821) | `rl-training` `response/sequence` `structured-search` |
| **ICML 2026** | [The Unlearnability Phenomenon in RLVR for Language Models](https://icml.cc/virtual/2026/poster/64909) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward](https://iclr.cc/virtual/2026/poster/10006646) | `rl-training` `response/sequence` `semantic-diversity` `reward/advantage` |
| **ACL 2026 Findings** | [Single-Agent Generation Surpasses Multi-Agent Systems in Semantic Diversity](https://aclanthology.org/2026.findings-acl.1894/) | `inference` `response/sequence` `population/multi-policy` `semantic-diversity` `ensemble/population` |
| **ICLR 2026** | [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://iclr.cc/virtual/2026/poster/10007896) | `rl-training` `response/sequence` `reward/advantage` |
| **ICML 2026** | [Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems](https://icml.cc/virtual/2026/poster/63622) | `inference` `population/multi-policy` `entropy/probability` `ensemble/population` |
| **ICLR 2026** | [RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs](https://iclr.cc/virtual/2026/poster/10009898) | `supervised-post-training` `response/sequence` `structured-search` |
| **ICML 2026** | [Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently](https://icml.cc/virtual/2026/poster/64293) | `rl-training` `policy-distribution` `backtracking/resampling` |
| **ICML 2026** | [Post-Training with Policy Gradients: Optimality and the Base Model Barrier](https://icml.cc/virtual/2026/poster/61683) | `rl-training` `policy-distribution` `gradient-reshaping` |
| **ICML 2026** | [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](https://icml.cc/virtual/2026/poster/63897) | `rl-training` `response/sequence` `entropy/probability` |
| **ICML 2026** | [Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models](https://icml.cc/virtual/2026/poster/64671) | `inference` `response/sequence` `semantic-diversity` |
| **ICLR 2026** | [KL-Regularized Reinforcement Learning for Generative Modelling is Designed to Mode Collapse](https://iclr.cc/virtual/2026/poster/10008208) | `rl-training` `response/sequence` `regularization` |
| **ICLR 2026** | [Generalization of RLVR Using Causal Reasoning as a Testbed](https://iclr.cc/virtual/2026/poster/10010768) | `rl-training` `policy-distribution` `structured-search` |
| **ICLR 2026** | [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://iclr.cc/virtual/2026/poster/10007078) | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| **ICML 2026** | [Exploration Hacking: LLMs Can Learn to Resist RL Training](https://icml.cc/virtual/2026/poster/64674) | `inference` `response/sequence` `structured-search` |
| **ICML 2026** | [Does Reinforcement Fine-Tuning Improve Generalization of LLM Agents? An Empirical Study](https://icml.cc/virtual/2026/poster/65794) | `rl-training` `response/sequence` `structured-search` |
| **ICML 2026** | [Demystifying Entropy Control in LLM RL Training: Theoretical Analysis and Dynamic Scheduling](https://icml.cc/virtual/2026/poster/62302) | `inference` `response/sequence` `entropy/probability` |
| **ICLR 2026** | [Breaking Barriers: Do Reinforcement Post Training Gains Transfer To Unseen Domains?](https://iclr.cc/virtual/2026/poster/10007526) | `rl-training` `response/sequence` `structured-search` |
| **ICML 2026** | [Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation](https://icml.cc/virtual/2026/poster/64547) | `rl-training` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| arXiv | [Diversity or Precision? A Deep Dive into Next Token Prediction](https://arxiv.org/abs/2512.22955) | `inference` `token` `semantic-diversity` |
| arXiv | [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2511.05993) | `rl-training` `response/sequence` `entropy/probability` |
| arXiv | [The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View](https://arxiv.org/abs/2510.04028) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [From Trial-and-Error to Improvement: A Systematic Analysis of LLM Exploration Mechanisms in RLVR](https://arxiv.org/abs/2508.07534) | `rl-training` `policy-distribution` `structured-search` |
| arXiv | [An Empirical Study on Reinforcement Learning for Reasoning-Search Interleaved LLM Agents](https://arxiv.org/abs/2505.15117) | `rl-training` `response/sequence` `structured-search` |

## Classical RL exploration — background only

A deliberately small appendix of foundational non-LLM work. These papers are not counted in the curated LLM catalog.

- **[Unifying Count-Based Exploration and Intrinsic Motivation](https://proceedings.neurips.cc/paper_files/paper/2016/hash/afda332245e2af431fb7b672a68b659d-Abstract.html)** (2016) — Pseudo-counts for high-dimensional exploration.
- **[Curiosity-driven Exploration by Self-supervised Prediction](https://proceedings.mlr.press/v70/pathak17a.html)** (2017) — The influential intrinsic-curiosity-module formulation.
- **[Parameter Space Noise for Exploration](https://arxiv.org/abs/1706.01905)** (2017) — Consistent behavioral exploration through parameter perturbations.
- **[Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295)** (2018) — Learned parameter noise for deep RL exploration.
- **[Exploration by Random Network Distillation](https://openreview.net/forum?id=H1lJJnR5Ym)** (2019) — Prediction-error novelty through a fixed random target network.
- **[Diversity is All You Need: Learning Skills without a Reward Function](https://openreview.net/forum?id=SJx63jRqFm)** (2019) — Unsupervised skill discovery through discriminable state visitation.
- **[First Return, Then Explore](https://www.nature.com/articles/s41586-020-03157-9)** (2021) — Go-Explore separates returning to promising states from exploration.

## Curation policy

- One primary area per paper; multiple tags are encouraged.
- Conference status is shown only when backed by an official venue page.
- Automated discovery produces candidates, never accepted catalog entries.
- Classical RL is limited to the short appendix above.
- The public Markdown files are generated from [`data/papers.json`](data/papers.json).

Run `python3 scripts/validate_catalog.py` and `python3 scripts/generate_catalog.py` after changing the registry.

## License

[CC BY 4.0](LICENSE)
