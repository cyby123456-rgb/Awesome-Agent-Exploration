# Awesome Exploration

> A curated reading list on exploration in language-model generation, RLVR, and agents.

This list treats exploration as a **primary research variable**, not as a keyword. A paper must identify where exploration happens and introduce or analyze a concrete exploration signal or mechanism. Generic RL, agent, test-time-scaling, self-improvement, and diversity papers are excluded.

**Evidence snapshot:** 2026-07-19 · [Taxonomy design](docs/TAXONOMY.md) · [Detailed metadata](README_DETAILED.md) · [2026 curation notes](docs/CURATION_2026.md) · [Contribution guide](CONTRIBUTING.md)

## Taxonomy

Each paper has exactly one primary area and may carry multiple orthogonal tags. See [Taxonomy design](docs/TAXONOMY.md) for the decision rules, meaning of each dimension, and the rationale for separating signals such as entropy from mechanisms such as temperature or noise.

| Primary area | Definition |
|---|---|
| **LLM Generation & Inference Exploration** | Exploration during language-model generation and inference, without RL policy updates as the central contribution. |
| **Exploration for RLVR** | Exploration during RL/RLVR post-training, where exploration changes the rollout distribution or policy update. |
| **Agentic Exploration** | Exploration by language agents acting over states, tools, observations, and long-horizon trajectories. |
| **Understanding, Evaluation & Benchmarks** | Work that measures, explains, surveys, or benchmarks exploration rather than primarily introducing an intervention. |

The former Token / Sequence / Policy sections are now `level` tags. Entropy, temperature, and noise are grouped under distributional/stochastic exploration while remaining distinct tags.

| Tag dimension | Values |
|---|---|
| **Phase** | data generation; supervised post-training; RL training; inference; test-time adaptation; continual/self-improvement |
| **Level** | token; response/sequence; trajectory/action; latent/representation; policy distribution; data/task; population |
| **Signal** | entropy/probability; uncertainty/confidence; novelty/curiosity; semantic diversity; coverage; information gain; reward/advantage; disagreement |
| **Mechanism** | sampling/decoding; temperature control; noise/perturbation; regularization; gradient reshaping; intrinsic reward; structured/tree search; replay/memory; curriculum; self-play; ensemble/population |
| **Problem** | entropy or mode collapse; sparse reward; local optimum; capability boundary; long horizon; exploration/exploitation; recovery |
| **Setting** | math; code; multimodal; creative/open-ended; web; tool use; knowledge graph; embodied; multi-agent |

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

## 1. LLM Generation & Inference Exploration

This category covers exploration that happens while a language model is generating or selecting candidate outputs, rather than through a reinforcement-learning update. Typical examples include sampling and decoding strategies, self-consistency, semantic-diversity methods, latent-state steering, and tree or graph search at inference time.

The central question is how to search a model's existing generative distribution more broadly, safely, or efficiently. Papers belong here when the main contribution improves or analyzes candidate generation, reasoning-path search, or output diversity without making RL post-training the core mechanism.

| Date | Paper | Source | Tags |
|---|---|---|---|
| 2026-05 | [From Noise to Diversity: Random Embedding Injection in LLM Reasoning](https://arxiv.org/abs/2605.11936) | arXiv | `inference` `latent/representation` `semantic-diversity` `noise/perturbation` |
| 2026 | [e3: Learning to Explore Enables Extrapolation of Test-Time Compute for LLMs](https://iclr.cc/virtual/2026/poster/10008718) | **ICLR 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://icml.cc/virtual/2026/poster/60489) | **ICML 2026** | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` |
| 2026 | [Uncertainty-Aware Test-Time Search for Optimization Problem Solving](https://aclanthology.org/2026.acl-long.1975/) | **ACL 2026 Main** | `inference` `response/sequence` `uncertainty/confidence` `structured-search` |
| 2026 | [Towards Diverse Scientific Hypothesis Search with Large Language Models](https://icml.cc/virtual/2026/poster/66259) | **ICML 2026** | `inference` `response/sequence` `semantic-diversity` `structured-search` |
| 2026 | [Thought Branches: Interpreting LLM Reasoning Requires Resampling](https://iclr.cc/virtual/2026/poster/10008605) | **ICLR 2026** | `inference` `response/sequence` `sampling/decoding` `tree-search/branching` |
| 2026 | [Think Earlier, Not Longer: Prompt Optimization via Reducing Unhealthy Exploration](https://aclanthology.org/2026.findings-acl.817/) | **ACL 2026 Findings** | `inference` `data/task` `structured-search` |
| 2026 | [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](https://aclanthology.org/2026.acl-long.200/) | **ACL 2026 Main** | `inference` `response/sequence` `entropy/probability` `temperature-control` |
| 2026 | [The Geometric Reasoner: Manifold-Informed Latent Foresight Search for Long-Context Reasoning](https://icml.cc/virtual/2026/poster/61787) | **ICML 2026** | `inference` `latent/representation` `structured-search` |
| 2026 | [TS$^2$: Training with Sparsemax+, Testing with Softmax for Accurate and Diverse LLM Fine-Tuning](https://iclr.cc/virtual/2026/poster/10010811) | **ICLR 2026** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [Student Guides Teacher: Weak-to-Strong Inference via Spectral Orthogonal Exploration](https://aclanthology.org/2026.acl-long.761/) | **ACL 2026 Main** | `inference` `response/sequence` `structured-search` |
| 2026 | [String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation](https://iclr.cc/virtual/2026/poster/10007633) | **ICLR 2026** | `inference` `response/sequence` `data/task` `entropy/probability` `semantic-diversity` |
| 2026 | [SeDev: Structured Semantic Exploration for LLM-Driven Code Generation](https://aclanthology.org/2026.acl-long.1641/) | **ACL 2026 Main** | `inference` `response/sequence` `structured-search` |
| 2026 | [Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening](https://icml.cc/virtual/2026/poster/63925) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` `sampling/decoding` |
| 2026 | [Sample Smart, Not Hard: Correctness-First Decoding for Better Reasoning in LLMs](https://iclr.cc/virtual/2026/poster/10007335) | **ICLR 2026** | `inference` `response/sequence` `sampling/decoding` |
| 2026 | [SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning](https://aclanthology.org/2026.acl-short.54/) | **ACL 2026 Main** | `supervised-post-training` `response/sequence` `semantic-diversity` |
| 2026 | [Representation-Based Exploration for Language Models: From Test-Time to Post-Training](https://iclr.cc/virtual/2026/poster/10009438) | **ICLR 2026** | `inference` `latent/representation` `response/sequence` `semantic-diversity` `novelty/curiosity` `reward-shaping/intrinsic-reward` |
| 2026 | [Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning](https://aclanthology.org/2026.findings-acl.1085/) | **ACL 2026 Findings** | `inference` `response/sequence` `sampling/decoding` |
| 2026 | [Reasoning with Sampling: Your Base Model is Smarter Than You Think](https://iclr.cc/virtual/2026/poster/10009093) | **ICLR 2026** | `inference` `response/sequence` `entropy/probability` `semantic-diversity` `sampling/decoding` |
| 2026 | [Post-training Large Language Models for Diverse High-Quality Responses](https://iclr.cc/virtual/2026/poster/10010944) | **ICLR 2026** | `supervised-post-training` `response/sequence` `semantic-diversity` |
| 2026 | [One-shot Entropy Minimization for Language Model Reasoning](https://icml.cc/virtual/2026/poster/66725) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` |
| 2026 | [Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models](https://aclanthology.org/2026.findings-acl.1149/) | **ACL 2026 Findings** | `inference` `response/sequence` `structured-search` |
| 2026 | [Multi-LLM Collaborative Search for Complex Problem Solving](https://aclanthology.org/2026.findings-acl.2115/) | **ACL 2026 Findings** | `inference` `population/multi-policy` `ensemble/population` |
| 2026 | [ModeX: Evaluator-Free Best-of-N Selection for Open-Ended Generation](https://aclanthology.org/2026.acl-long.655/) | **ACL 2026 Main** | `inference` `response/sequence` `sampling/decoding` |
| 2026 | [Learning Diverse Responses with Prefix-Conditioned Supervised Fine-Tuning](https://aclanthology.org/2026.acl-long.9/) | **ACL 2026 Main** | `supervised-post-training` `response/sequence` `semantic-diversity` |
| 2026 | [Large Language Models Explore by Latent Distilling](https://icml.cc/virtual/2026/poster/63542) | **ICML 2026** | `inference` `latent/representation` `structured-search` |
| 2026 | [Language of Thought Shapes Output Diversity in Large Language Models](https://aclanthology.org/2026.acl-long.628/) | **ACL 2026 Main** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [HyPER: Bridging Exploration and Exploitation for Scalable LLM Reasoning with Hypothesis Path Expansion and Reduction](https://icml.cc/virtual/2026/poster/65181) | **ICML 2026** | `inference` `response/sequence` `tree-search/branching` |
| 2026 | [GuidedSampling: Steering LLMs Towards Diverse Candidate Solutions at Inference-Time](https://iclr.cc/virtual/2026/poster/10009336) | **ICLR 2026** | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` `noise/perturbation` |
| 2026 | [From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models](https://icml.cc/virtual/2026/poster/65555) | **ICML 2026** | `inference` `response/sequence` `sampling/decoding` |
| 2026 | [Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering](https://iclr.cc/virtual/2026/poster/10006851) | **ICLR 2026** | `inference` `response/sequence` `latent/representation` `semantic-diversity` `noise/perturbation` |
| 2026 | [Escaping Mode Collapse in LLM Generation](https://icml.cc/virtual/2026/poster/65524) | **ICML 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [Entropy-informed Decoding: Adaptive Information-Driven Branching](https://icml.cc/virtual/2026/poster/61896) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` `sampling/decoding` `tree-search/branching` |
| 2026 | [Entropy-Aware On-Policy Distillation of Language Models](https://icml.cc/virtual/2026/poster/64855) | **ICML 2026** | `supervised-post-training` `policy-distribution` `entropy/probability` |
| 2026 | [Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models](https://icml.cc/virtual/2026/poster/64102) | **ICML 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [EAGer: Entropy-Aware GEneRation for Adaptive Inference-Time Scaling](https://icml.cc/virtual/2026/poster/65185) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` |
| 2026 | [Diversity Matters: Revisiting Test-Time Compute in Vision-Language Models](https://icml.cc/virtual/2026/poster/63569) | **ICML 2026** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [Diverse Text Decoding via Iterative Reweighting](https://iclr.cc/virtual/2026/poster/10011729) | **ICLR 2026** | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` |
| 2026 | [Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning](https://aclanthology.org/2026.acl-long.1231/) | **ACL 2026 Main** | `inference` `response/sequence` `structured-search` |
| 2026 | [Differential Fine-Tuning Large Language Models Towards Better Diverse Reasoning Abilities](https://iclr.cc/virtual/2026/poster/10008716) | **ICLR 2026** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [D-FUSEr: Diverse Failure, Unified Success via Error-Distribution Shaping in LLM Reasoning](https://icml.cc/virtual/2026/poster/63783) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` `semantic-diversity` |
| 2026 | [Continuous Chain of Thought Enables Parallel Exploration and Reasoning](https://iclr.cc/virtual/2026/poster/10007055) | **ICLR 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [ConMA : Confidence-Guided Kernel Sampling with Multi-Stage Aggregation for LLM Reasoning](https://aclanthology.org/2026.findings-acl.1475/) | **ACL 2026 Findings** | `inference` `response/sequence` `uncertainty/confidence` `sampling/decoding` |
| 2026 | [Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search](https://aclanthology.org/2026.findings-acl.214/) | **ACL 2026 Findings** | `inference` `response/sequence` `tree-search/branching` |
| 2026 | [Cache Coherent Resampling for Efficient Test Time Scaling in LLM Reasoning via Adaptive Sequential Monte Carlo](https://icml.cc/virtual/2026/poster/64829) | **ICML 2026** | `inference` `response/sequence` `sampling/decoding` `backtracking/resampling` |
| 2026 | [Beyond Templates: Dynamic Adaptation of Reasoning Demonstrations via Feasibility-Aware Exploration](https://aclanthology.org/2026.findings-acl.327/) | **ACL 2026 Findings** | `inference` `data/task` `structured-search` |
| 2026 | [Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.390/) | **ACL 2026 Findings** | `inference` `trajectory/action` `sampling/decoding` |
| 2026 | [Beyond Logits: Metastable Latent Dynamics for Sample-Efficient Best-of-N Selection in LLMs](https://icml.cc/virtual/2026/poster/66569) | **ICML 2026** | `inference` `token` `latent/representation` `sampling/decoding` |
| 2026 | [Annotations Mitigate Post-Training Mode Collapse](https://icml.cc/virtual/2026/poster/63468) | **ICML 2026** | `supervised-post-training` `response/sequence` `structured-search` |
| 2026 | [Aligning Tree-Search Policies with Fixed Token Budgets in Test-Time Scaling of LLMs](https://icml.cc/virtual/2026/poster/63795) | **ICML 2026** | `inference` `token` `structured-search` |
| 2025-11 | [Think Before You Retrieve: Learning Test-Time Adaptive Search with Small Language Models](https://arxiv.org/abs/2511.07581) | arXiv | `inference` `response/sequence` `structured-search` |
| 2025-10 | [SolverLLM: Leveraging Test-Time Scaling for Optimization Problem via LLM-Guided Search](https://arxiv.org/abs/2510.16916) | arXiv | `inference` `response/sequence` `structured-search` |
| 2025-10 | [The Road Less Traveled: Enhancing Exploration in LLMs via Sequential Sampling](https://arxiv.org/abs/2510.15502) | arXiv | `inference` `response/sequence` `sampling/decoding` |
| 2025-09 | [Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation](https://arxiv.org/abs/2509.15194) | arXiv | `inference` `response/sequence` `novelty/curiosity` |
| 2025-08 | [Learning from Diverse Reasoning Paths with Routing and Collaboration](https://arxiv.org/abs/2508.16861) | arXiv | `inference` `response/sequence` `semantic-diversity` |
| 2025-01 | [COS(M+O)S: Curiosity and RL-Enhanced MCTS for Exploring Story Space via Language Models](https://arxiv.org/abs/2501.17104) | arXiv | `inference` `response/sequence` `novelty/curiosity` `tree-search/branching` |
| 2023-12 | [Reasoning with Language Model is Planning with World Model](https://aclanthology.org/2023.emnlp-main.507/) | EMNLP 2023 | `inference` `response/sequence` `trajectory/action` `reward/advantage` `tree-search/branching` |
| 2023-08 | [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://arxiv.org/abs/2308.09687) | arXiv | `inference` `response/sequence` `semantic-diversity` `tree-search/branching` `structured-search` |
| 2023 | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract.html) | NeurIPS 2023 | `inference` `response/sequence` `reward/advantage` `coverage` `tree-search/branching` `backtracking/resampling` |
| 2023 | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://iclr.cc/virtual/2023/poster/11718) | ICLR 2023 | `inference` `response/sequence` `semantic-diversity` `sampling/decoding` `ensemble/population` |

## 2. Exploration for RLVR

This category concerns exploration during reinforcement learning or RL with verifiable rewards (RLVR). Here, exploration changes which rollouts are collected, how reward or advantage signals are assigned, or how the policy distribution is updated during training.

It includes work on entropy or mode collapse, low-probability tokens, rollout diversity, intrinsic or shaped rewards, gradient and regularization interventions, curriculum design, and attempts to push beyond a base model's capability boundary. The defining feature is that exploration is part of the learning loop, not only an inference-time search choice.

| Date | Paper | Source | Tags |
|---|---|---|---|
| 2026-05 | [Entropy Polarity in Reinforcement Fine-Tuning: Direction, Asymmetry, and Control](https://arxiv.org/abs/2605.11775) | arXiv | `rl-training` `policy-distribution` `entropy/probability` |
| 2026-05 | [Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning](https://arxiv.org/abs/2605.11461) | arXiv | `rl-training` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| 2026-05 | [Exploration-Driven Optimization for Test-Time Large Language Model Reasoning](https://arxiv.org/abs/2605.09853) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2026-04 | [Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control](https://arxiv.org/abs/2604.26326) | arXiv | `rl-training` `policy-distribution` `entropy/probability` |
| 2026-04 | [DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off](https://arxiv.org/abs/2604.13902) | arXiv | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2026-04 | [Policy Split: Incentivizing Dual-Mode Exploration in LLM Reinforcement with Dual-Mode Entropy Regularization](https://arxiv.org/abs/2604.11510) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| 2026-04 | [Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems](https://arxiv.org/abs/2604.04767) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2026-03 | [Bootstrapping Exploration with Group-Level Natural Language Feedback in Reinforcement Learning](https://arxiv.org/abs/2603.04597) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2026-02 | [Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning](https://arxiv.org/abs/2602.22642) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| 2026-02 | [UpSkill: Mutual Information Skill Learning for Structured Response Diversity in LLMs](https://arxiv.org/abs/2602.22296) | arXiv | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` `information-gain` |
| 2026-02 | [DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning](https://arxiv.org/abs/2602.19895) | arXiv | `rl-training` `policy-distribution` `semantic-diversity` `regularization` |
| 2026-02 | [MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2602.17550) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2026-02 | [Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL](https://arxiv.org/abs/2602.13035) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `temperature-control` |
| 2026-02 | [Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities](https://arxiv.org/abs/2602.05281) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` `structured-search` |
| 2026-02 | [Entropy-Gated Selective Policy Optimization:Token-Level Gradient Allocation for Hybrid Training of Large Language Models](https://arxiv.org/abs/2602.03309) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2026-01 | [Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models](https://arxiv.org/abs/2601.22478) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [h1: Bootstrapping LLMs to Reason over Longer Horizons via Reinforcement Learning](https://icml.cc/virtual/2026/poster/66494) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [XRPO: Pushing the Limits of GRPO with Targeted Exploration and Exploitation](https://icml.cc/virtual/2026/poster/65777) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [VANE: Guiding High-Value Exploration in RLVR via Outcome-Process Novelty Shaping](https://aclanthology.org/2026.findings-acl.1434/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `novelty/curiosity` `reward/advantage` `reward-shaping/intrinsic-reward` |
| 2026 | [Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning](https://aclanthology.org/2026.findings-acl.951/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `uncertainty/confidence` `reward/advantage` `gradient-reshaping` |
| 2026 | [Token Hidden Reward: Steering Exploration-Exploitation in Group Relative Deep Reinforcement Learning](https://iclr.cc/virtual/2026/poster/10008016) | **ICLR 2026** | `rl-training` `token` `policy-distribution` `reward/advantage` `noise/perturbation` |
| 2026 | [Temporal Sampling for Forgotten Reasoning in LLMs](https://aclanthology.org/2026.acl-long.1305/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `sampling/decoding` |
| 2026 | [Targeted Exploration via Unified Entropy Control for Reinforcement Learning](https://aclanthology.org/2026.findings-acl.828/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `entropy/probability` `structured-search` |
| 2026 | [Smaller Models are Natural Explorers for Policy-Level Diversity in GRPO](https://icml.cc/virtual/2026/poster/64272) | **ICML 2026** | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| 2026 | [Semantic-Space Exploration and Exploitation in RLVR for LLM Reasoning](https://aclanthology.org/2026.findings-acl.1915/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| 2026 | [Selective Expert Guidance for Effective and Diverse Exploration in Reinforcement Learning of LLMs](https://iclr.cc/virtual/2026/poster/10008654) | **ICLR 2026** | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| 2026 | [SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning](https://icml.cc/virtual/2026/poster/60895) | **ICML 2026** | `rl-training` `policy-distribution` `reward/advantage` `reward-shaping/intrinsic-reward` |
| 2026 | [SPS: Steering Probability Squeezing for Better Exploration in Reinforcement Learning for Large Language Models](https://aclanthology.org/2026.findings-acl.865/) | **ACL 2026 Findings** | `rl-training` `token` `policy-distribution` `entropy/probability` `noise/perturbation` `gradient-reshaping` |
| 2026 | [SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs](https://icml.cc/virtual/2026/poster/63563) | **ICML 2026** | `rl-training` `policy-distribution` `regularization` |
| 2026 | [Risk-Sensitive Reinforcement Learning for Alleviating Exploration Dilemmas in Large Language Models](https://iclr.cc/virtual/2026/poster/10011269) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://aclanthology.org/2026.findings-acl.1982/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `novelty/curiosity` `reward/advantage` `reward-shaping/intrinsic-reward` |
| 2026 | [Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](https://icml.cc/virtual/2026/poster/65737) | **ICML 2026** | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| 2026 | [Restoring Exploration after Post-Training: Latent Exploration Decoding for Large Reasoning Models](https://icml.cc/virtual/2026/poster/66546) | **ICML 2026** | `supervised-post-training` `latent/representation` `policy-distribution` `sampling/decoding` |
| 2026 | [ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning](https://icml.cc/virtual/2026/poster/62006) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Reinforced Efficient Reasoning via Semantically Diverse Exploration](https://aclanthology.org/2026.acl-long.2216/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| 2026 | [Reasoning-Guided Exploration for Online DPO](https://aclanthology.org/2026.findings-acl.1370/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [On Entropy Control in LLM-RL Algorithms](https://iclr.cc/virtual/2026/poster/10010002) | **ICLR 2026** | `rl-training` `policy-distribution` `entropy/probability` |
| 2026 | [No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping](https://iclr.cc/virtual/2026/poster/10007755) | **ICLR 2026** | `rl-training` `policy-distribution` `data/task` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| 2026 | [Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward](https://aclanthology.org/2026.findings-acl.1209/) | **ACL 2026 Findings** | `rl-training` `token` `policy-distribution` `entropy/probability` `regularization` |
| 2026 | [Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards](https://iclr.cc/virtual/2026/poster/10011530) | **ICLR 2026** | `rl-training` `response/sequence` `trajectory/action` `reward/advantage` `tree-search/branching` |
| 2026 | [Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization](https://icml.cc/virtual/2026/poster/62699) | **ICML 2026** | `rl-training` `policy-distribution` `information-gain` `gradient-reshaping` `tree-search/branching` |
| 2026 | [Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models](https://aclanthology.org/2026.acl-long.617/) | **ACL 2026 Main** | `supervised-post-training` `policy-distribution` `entropy/probability` |
| 2026 | [Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation](https://icml.cc/virtual/2026/poster/60948) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Incentivizing LLM Reasoning via Reinforcement Learning with Functional Monte Carlo Tree Search](https://iclr.cc/virtual/2026/poster/10007699) | **ICLR 2026** | `rl-training` `policy-distribution` `tree-search/branching` |
| 2026 | [How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization](https://aclanthology.org/2026.findings-acl.724/) | **ACL 2026 Findings** | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| 2026 | [HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment](https://aclanthology.org/2026.acl-long.1418/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `entropy/probability` `semantic-diversity` `reward-shaping/intrinsic-reward` |
| 2026 | [Guided by Gut: Efficient Test-Time Scaling with Reinforced Intrinsic Confidence](https://aclanthology.org/2026.acl-long.739/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `uncertainty/confidence` |
| 2026 | [GeoAlign: Geometric Rollout Curation for Robust LLM Reinforcement Learning](https://icml.cc/virtual/2026/poster/60634) | **ICML 2026** | `rl-training` `response/sequence` `policy-distribution` `structured-search` |
| 2026 | [GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy](https://icml.cc/virtual/2026/poster/65174) | **ICML 2026** | `rl-training` `token` `response/sequence` `entropy/probability` `reward/advantage` `reward-shaping/intrinsic-reward` |
| 2026 | [Free Energy-Driven Reinforcement Learning with Adaptive Advantage Shaping for Unsupervised Reasoning in LLMs](https://aclanthology.org/2026.acl-long.797/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| 2026 | [Exploration-Exploitation Reshaping towards Efficient Reasoning for Large Language Models](https://aclanthology.org/2026.findings-acl.1520/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs](https://icml.cc/virtual/2026/poster/65561) | **ICML 2026** | `rl-training` `policy-distribution` `replay/memory` |
| 2026 | [Expanding Reasoning Potential in Foundation Model by Learning Diverse Chains of Thought Patterns](https://iclr.cc/virtual/2026/poster/10011658) | **ICLR 2026** | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` |
| 2026 | [EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning for LLMs](https://aclanthology.org/2026.findings-acl.1031/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Escaping Policy Contraction: Contraction-Aware PPO (CaPPO) for Stable Language Model Fine-Tuning](https://iclr.cc/virtual/2026/poster/10006831) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Entropy-preserving reinforcement learning](https://iclr.cc/virtual/2026/poster/10010707) | **ICLR 2026** | `rl-training` `policy-distribution` `entropy/probability` |
| 2026 | [Entropy-Aware Reshaping of Reinforcement Signals for Multi-Answer Reasoning](https://aclanthology.org/2026.findings-acl.2001/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `entropy/probability` |
| 2026 | [Entropy Scheduling in Reinforcement Learning for Large Language Models](https://aclanthology.org/2026.findings-acl.206/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `entropy/probability` |
| 2026 | [Empowering Small VLMs to Think with Dynamic Memorization and Exploration](https://iclr.cc/virtual/2026/poster/10007260) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [ETR: Entropy Trend Reward for Efficient Chain-of-Thought Reasoning](https://aclanthology.org/2026.acl-long.799/) | **ACL 2026 Main** | `rl-training` `response/sequence` `policy-distribution` `entropy/probability` `reward/advantage` |
| 2026 | [EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget](https://iclr.cc/virtual/2026/poster/10009769) | **ICLR 2026** | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2026 | [ECHO: Entropy-Confidence Hybrid Optimization for Test-Time Reinforcement Learning](https://icml.cc/virtual/2026/poster/63137) | **ICML 2026** | `rl-training` `policy-distribution` `entropy/probability` `uncertainty/confidence` |
| 2026 | [Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](https://iclr.cc/virtual/2026/poster/10006780) | **ICLR 2026** | `rl-training` `policy-distribution` `sampling/decoding` |
| 2026 | [Dynamic Sampling that Adapts: Self-Aware Iterative Data Persistent Optimization for Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.1412/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `data/task` `sampling/decoding` |
| 2026 | [Do Not Let Low-Probability Tokens Over-Dominate in RL for LLMs](https://iclr.cc/virtual/2026/poster/10010601) | **ICLR 2026** | `rl-training` `token` `policy-distribution` `entropy/probability` |
| 2026 | [Diversity-Incentivized Exploration for Versatile Reasoning](https://iclr.cc/virtual/2026/poster/10011130) | **ICLR 2026** | `rl-training` `policy-distribution` `semantic-diversity` `structured-search` |
| 2026 | [Diversity-Enhanced Reasoning for Subjective Questions](https://iclr.cc/virtual/2026/poster/10011855) | **ICLR 2026** | `rl-training` `policy-distribution` `semantic-diversity` |
| 2026 | [Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration](https://icml.cc/virtual/2026/poster/60955) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Tree-based Search](https://iclr.cc/virtual/2026/poster/10010078) | **ICLR 2026** | `rl-training` `policy-distribution` `coverage` `reward/advantage` `tree-search/branching` `replay/memory` |
| 2026 | [DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning](https://aclanthology.org/2026.findings-acl.685/) | **ACL 2026 Findings** | `rl-training` `response/sequence` `policy-distribution` `semantic-diversity` |
| 2026 | [DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing](https://aclanthology.org/2026.acl-long.647/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `semantic-diversity` `tree-search/branching` |
| 2026 | [DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning](https://icml.cc/virtual/2026/poster/61634) | **ICML 2026** | `rl-training` `response/sequence` `trajectory/action` `entropy/probability` |
| 2026 | [DARL: Encouraging Diverse Answers for General Reasoning without Verifiers](https://aclanthology.org/2026.findings-acl.1530/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `semantic-diversity` |
| 2026 | [Count Counts: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards](https://iclr.cc/virtual/2026/poster/10011073) | **ICLR 2026** | `rl-training` `policy-distribution` `reward/advantage` `reward-shaping/intrinsic-reward` |
| 2026 | [Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning](https://iclr.cc/virtual/2026/poster/10011411) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Contextual Rollout Bandits for Reinforcement Learning with Verifiable Rewards](https://icml.cc/virtual/2026/poster/60796) | **ICML 2026** | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` |
| 2026 | [CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution](https://aclanthology.org/2026.acl-long.1376/) | **ACL 2026 Main** | `rl-training` `policy-distribution` `disagreement` `self-play/co-evolution` |
| 2026 | [CDE: Curiosity-Driven Exploration for Efficient Reinforcement Learning in Large Language Models](https://iclr.cc/virtual/2026/poster/10011417) | **ICLR 2026** | `rl-training` `policy-distribution` `novelty/curiosity` `uncertainty/confidence` `reward-shaping/intrinsic-reward` |
| 2026 | [BroRL: Scaling Reinforcement Learning via Broadened Exploration](https://icml.cc/virtual/2026/poster/64690) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning](https://icml.cc/virtual/2026/poster/64959) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Beyond Mode Collapse: Distribution Matching for Diverse Reasoning](https://icml.cc/virtual/2026/poster/65266) | **ICML 2026** | `rl-training` `policy-distribution` `entropy/probability` `semantic-diversity` |
| 2026 | [Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning](https://iclr.cc/virtual/2026/poster/10006770) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Beyond High-Entropy Exploration: Correctness-Aware Low-Entropy Segment-Based Advantage Shaping for Reasoning LLMs](https://aclanthology.org/2026.findings-acl.1650/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| 2026 | [Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization](https://icml.cc/virtual/2026/poster/61727) | **ICML 2026** | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2026 | [Attention as a Compass: Efficient Exploration for Process-Supervised RL in Reasoning Models](https://iclr.cc/virtual/2026/poster/10009884) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Anchored Policy Optimization: Mitigating Exploration Collapse via Support-Constrained Rectification](https://icml.cc/virtual/2026/poster/65360) | **ICML 2026** | `rl-training` `policy-distribution` `regularization` `gradient-reshaping` |
| 2026 | [ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping](https://iclr.cc/virtual/2026/poster/10011711) | **ICLR 2026** | `rl-training` `token` `policy-distribution` `entropy/probability` |
| 2026 | [A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning](https://aclanthology.org/2026.findings-acl.641/) | **ACL 2026 Findings** | `rl-training` `token` `policy-distribution` `entropy/probability` |
| 2025-12 | [Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2512.15687) | arXiv | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2025-12 | [Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning](https://arxiv.org/abs/2512.04359) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` |
| 2025-11 | [From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training](https://arxiv.org/abs/2511.07738) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `noise/perturbation` |
| 2025-11 | [Explore Data Left Behind in Reinforcement Learning for Reasoning Language Models](https://arxiv.org/abs/2511.04800) | arXiv | `rl-training` `policy-distribution` `data/task` `structured-search` |
| 2025-10 | [Scheduling Your LLM Reinforcement Learning with Reasoning Trees](https://arxiv.org/abs/2510.24832) | arXiv | `rl-training` `policy-distribution` `tree-search/branching` |
| 2025-10 | [Revisiting Entropy Regularization: Adaptive Coefficient Unlocks Its Potential for LLM Reinforcement Learning](https://arxiv.org/abs/2510.10959) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `regularization` |
| 2025-10 | [Let it Calm: Exploratory Annealed Decoding for Verifiable Reinforcement Learning](https://arxiv.org/abs/2510.05251) | arXiv | `rl-training` `policy-distribution` `sampling/decoding` |
| 2025-10 | [More Than One Teacher: Adaptive Multi-Guidance Policy Optimization for Diverse Exploration](https://arxiv.org/abs/2510.02227) | arXiv | `rl-training` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| 2025-09 | [Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models](https://arxiv.org/abs/2509.26114) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2025-09 | [CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning](https://arxiv.org/abs/2509.20712) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2025-09 | [Outcome-based Exploration for LLM Reasoning](https://arxiv.org/abs/2509.06941) | arXiv | `rl-training` `response/sequence` `policy-distribution` `reward/advantage` `semantic-diversity` `reward-shaping/intrinsic-reward` |
| 2025-08 | [Know When to Explore: Difficulty-Aware Certainty as a Guide for LLM Reinforcement Learning](https://arxiv.org/abs/2509.00125) | arXiv | `rl-training` `policy-distribution` `uncertainty/confidence` `structured-search` |
| 2025-08 | [ETTRL: Balancing Exploration and Exploitation in LLM Test-Time Reinforcement Learning Via Entropy Mechanism](https://arxiv.org/abs/2508.11356) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `structured-search` |
| 2025-08 | [CURE: Critical-Token-Guided Re-Concatenation for Entropy-Collapse Prevention](https://arxiv.org/abs/2508.11016) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` |
| 2025-08 | [AMFT: Aligning LLM Reasoners by Meta-Learning the Optimal Imitation-Exploration Balance](https://arxiv.org/abs/2508.06944) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2025-08 | [Decomposing the Entropy-Performance Exchange: The Missing Keys to Unlocking Effective Reinforcement Learning](https://arxiv.org/abs/2508.02260) | arXiv | `rl-training` `policy-distribution` `entropy/probability` |
| 2025-07 | [RL-PLUS: Countering Capability Boundary Collapse of LLMs in Reinforcement Learning with Hybrid-policy Optimization](https://arxiv.org/abs/2508.00222) | arXiv | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2025-07 | [RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning](https://arxiv.org/abs/2507.07451) | arXiv | `rl-training` `policy-distribution` `replay/memory` |
| 2025-06 | [EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework](https://arxiv.org/abs/2506.22200) | arXiv | `rl-training` `policy-distribution` `replay/memory` |
| 2025-06 | [TreeRL: LLM Reinforcement Learning with On-Policy Tree Search](https://arxiv.org/abs/2506.11902) | arXiv | `rl-training` `policy-distribution` `tree-search/branching` |
| 2025-06 | [R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2506.04185) | arXiv | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| 2025-06 | [Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning](https://arxiv.org/abs/2506.01939) | arXiv | `rl-training` `token` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2025-05 | [ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models](https://arxiv.org/abs/2505.24864) | arXiv | `rl-training` `policy-distribution` `coverage` `regularization` |
| 2025-05 | [The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models](https://arxiv.org/abs/2505.22617) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `regularization` `gradient-reshaping` |
| 2025-05 | [PPO-BR: Dual-Signal Entropy-Reward Adaptation for Trust Region Policy Optimization](https://arxiv.org/abs/2505.17714) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| 2025-05 | [DGRO: Enhancing LLM Reasoning via Exploration-Exploitation Control and Reward Variance Management](https://arxiv.org/abs/2505.12951) | arXiv | `rl-training` `policy-distribution` `reward/advantage` `structured-search` |
| 2025-05 | [SEED-GRPO: Semantic Entropy Enhanced GRPO for Uncertainty-Aware Policy Optimization](https://arxiv.org/abs/2505.12346) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `uncertainty/confidence` `gradient-reshaping` |
| 2025-04 | [Improving RL Exploration for LLM Reasoning through Retrospective Replay](https://arxiv.org/abs/2504.14363) | arXiv | `rl-training` `policy-distribution` `backtracking/resampling` `replay/memory` |
| 2025-03 | [Entropy-guided sequence weighting for efficient exploration in RL-based LLM fine-tuning](https://arxiv.org/abs/2503.22456) | arXiv | `rl-training` `response/sequence` `policy-distribution` `entropy/probability` `structured-search` |
| 2025-03 | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476) | arXiv | `rl-training` `policy-distribution` `entropy/probability` `sampling/decoding` `gradient-reshaping` |
| 2025-02 | [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://arxiv.org/abs/2502.02508) | arXiv | `rl-training` `response/sequence` `policy-distribution` `structured-search` |

## 3. Agentic Exploration

This category covers language agents that explore an external or persistent environment: webpages, tools, GUIs, knowledge graphs, games, embodied worlds, or multi-agent settings. The object of exploration is usually a trajectory of states, actions, observations, and tool calls rather than a single textual response.

These papers focus on challenges such as partial observability, long horizons, recovery from failed actions, memory, environment coverage, and interactive search. A paper belongs here when external interaction is central to the exploration problem and evaluation.

| Date | Paper | Source | Tags |
|---|---|---|---|
| 2026-03 | [RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization](https://arxiv.org/abs/2603.03078) | arXiv | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` |
| 2026-01 | [AT$^2$PO: Agentic Turn-based Policy Optimization via Tree Search](https://arxiv.org/abs/2601.04767) | arXiv | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` `tree-search/branching` |
| 2026 | [What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity](https://icml.cc/virtual/2026/poster/60509) | **ICML 2026** | `inference` `trajectory/action` `novelty/curiosity` `structured-search` |
| 2026 | [WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement](https://aclanthology.org/2026.acl-long.1456/) | **ACL 2026 Main** | `inference` `trajectory/action` `population/multi-policy` `self-play/co-evolution` |
| 2026 | [Unlocking Long-Horizon Agentic Search with Large-Scale End-to-End RL](https://iclr.cc/virtual/2026/poster/10009929) | **ICLR 2026** | `inference` `trajectory/action` `structured-search` |
| 2026 | [Towards Self-Evolving Agent Benchmarks : Validatable Agent Trajectory via Test-Time Exploration](https://iclr.cc/virtual/2026/poster/10011762) | **ICLR 2026** | `inference` `trajectory/action` `self-play/co-evolution` |
| 2026 | [Toward Efficient Exploration by Large Language Model Agents](https://iclr.cc/virtual/2026/poster/10009979) | **ICLR 2026** | `inference` `trajectory/action` `structured-search` |
| 2026 | [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://icml.cc/virtual/2026/poster/63090) | **ICML 2026** | `rl-training` `trajectory/action` `uncertainty/confidence` `structured-search` |
| 2026 | [Search Self-Play: Pushing the Frontier of Agent Capability without Supervision](https://iclr.cc/virtual/2026/poster/10008777) | **ICLR 2026** | `inference` `trajectory/action` `population/multi-policy` `self-play/co-evolution` |
| 2026 | [Scaling Synthetic Task Generation for Agents via Exploration](https://iclr.cc/virtual/2026/poster/10007463) | **ICLR 2026** | `data-generation` `response/sequence` `trajectory/action` `curriculum/task-generation` |
| 2026 | [SQLAgent: Learning to Explore Before Generating as a Data Engineer](https://aclanthology.org/2026.findings-acl.1959/) | **ACL 2026 Findings** | `inference` `trajectory/action` `data/task` `structured-search` |
| 2026 | [SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience](https://icml.cc/virtual/2026/poster/65711) | **ICML 2026** | `continual/self-improvement` `trajectory/action` `replay/memory` `self-play/co-evolution` |
| 2026 | [Reinforcement Learning for Self-Improving Agent with Skill Library](https://aclanthology.org/2026.acl-long.69/) | **ACL 2026 Main** | `rl-training` `trajectory/action` `structured-search` |
| 2026 | [RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents](https://icml.cc/virtual/2026/poster/60790) | **ICML 2026** | `inference` `trajectory/action` `structured-search` |
| 2026 | [R-Diverse: Mitigating Diversity Illusion in Self-Play LLM Training](https://icml.cc/virtual/2026/poster/65447) | **ICML 2026** | `inference` `trajectory/action` `population/multi-policy` `semantic-diversity` `self-play/co-evolution` |
| 2026 | [PExA: Parallel Exploration Agent for Complex Text-to-SQL](https://aclanthology.org/2026.acl-short.48/) | **ACL 2026 Main** | `inference` `trajectory/action` `structured-search` |
| 2026 | [Meta-RL Induces Exploration in Language Agents](https://iclr.cc/virtual/2026/poster/10011567) | **ICLR 2026** | `inference` `trajectory/action` `structured-search` |
| 2026 | [MAXS: Meta-Adaptive Exploration with LLM Agents](https://aclanthology.org/2026.findings-acl.670/) | **ACL 2026 Findings** | `inference` `trajectory/action` `structured-search` |
| 2026 | [Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization](https://icml.cc/virtual/2026/poster/63287) | **ICML 2026** | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` |
| 2026 | [Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning](https://iclr.cc/virtual/2026/poster/10010088) | **ICLR 2026** | `rl-training` `trajectory/action` `structured-search` |
| 2026 | [LLM Inductive Reasoning Through Multi-Agent Enhanced Monte Carlo Tree Search](https://aclanthology.org/2026.findings-acl.1178/) | **ACL 2026 Findings** | `inference` `trajectory/action` `population/multi-policy` `tree-search/branching` `ensemble/population` |
| 2026 | [Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents](https://icml.cc/virtual/2026/poster/63273) | **ICML 2026** | `rl-training` `trajectory/action` `policy-distribution` `entropy/probability` `uncertainty/confidence` `gradient-reshaping` |
| 2026 | [Go-Browse: Training Web Agents with Structured Exploration](https://iclr.cc/virtual/2026/poster/10010264) | **ICLR 2026** | `inference` `trajectory/action` `structured-search` |
| 2026 | [FusionFlow: Enabling Deep Structural Exploration for Automated Agentic Workflow Generation](https://aclanthology.org/2026.acl-long.1278/) | **ACL 2026 Main** | `inference` `response/sequence` `trajectory/action` `structured-search` |
| 2026 | [Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling](https://iclr.cc/virtual/2026/poster/10009840) | **ICLR 2026** | `inference` `trajectory/action` `reward/advantage` `structured-search` |
| 2026 | [Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization](https://iclr.cc/virtual/2026/poster/10009229) | **ICLR 2026** | `rl-training` `trajectory/action` `policy-distribution` `gradient-reshaping` `replay/memory` |
| 2026 | [Empowering GUI Agents via Autonomous Experience Exploration and Hindsight Experience Utilization for Task Planning](https://aclanthology.org/2026.acl-long.1670/) | **ACL 2026 Main** | `inference` `trajectory/action` `data/task` `replay/memory` |
| 2026 | [Dyna-Mind: Learning to Simulate from Experience for Better AI Agents](https://iclr.cc/virtual/2026/poster/10010625) | **ICLR 2026** | `inference` `trajectory/action` `replay/memory` |
| 2026 | [Dual-Scale World Memory for LLM Agents towards Hard-Exploration Problems](https://iclr.cc/virtual/2026/poster/10008626) | **ICLR 2026** | `inference` `trajectory/action` `replay/memory` |
| 2026 | [DreamPhase: Offline Imagination and Uncertainty-Guided Planning for Large-Language-Model Agents](https://iclr.cc/virtual/2026/poster/10011238) | **ICLR 2026** | `inference` `trajectory/action` `uncertainty/confidence` |
| 2026 | [DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents](https://aclanthology.org/2026.acl-long.2151/) | **ACL 2026 Main** | `rl-training` `trajectory/action` `policy-distribution` `semantic-diversity` `gradient-reshaping` |
| 2026 | [DIVE: Scaling Diversity in Agentic Task Synthesis for Generalizable Tool Use](https://icml.cc/virtual/2026/poster/66305) | **ICML 2026** | `data-generation` `trajectory/action` `data/task` `semantic-diversity` |
| 2026 | [Chain-of-Relations: Faithful and Efficient LLM Reasoning over Knowledge Graphs via Relation-Centric Exploration](https://aclanthology.org/2026.findings-acl.2138/) | **ACL 2026 Findings** | `inference` `trajectory/action` `structured-search` |
| 2026 | [Branch-and-Browse: Efficient and Controllable Web Exploration with Tree-Structured Reasoning and Action Memory](https://aclanthology.org/2026.acl-long.838/) | **ACL 2026 Main** | `inference` `trajectory/action` `tree-search/branching` `replay/memory` |
| 2026 | [Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search](https://aclanthology.org/2026.findings-acl.160/) | **ACL 2026 Findings** | `inference` `trajectory/action` `data/task` `structured-search` |
| 2026 | [Beneficial Reasoning Behaviors in Agentic Search and Effective Training Methods to Obtain Them](https://aclanthology.org/2026.findings-acl.1400/) | **ACL 2026 Findings** | `inference` `trajectory/action` `structured-search` |
| 2026 | [Backjump-on-Graph: Empowering LLMs with Reinforced Retrospective Exploration for Agentic KG Reasoning](https://icml.cc/virtual/2026/poster/61995) | **ICML 2026** | `inference` `trajectory/action` `backtracking/resampling` |
| 2026 | [Autonomous Knowledge Graph Exploration with Adaptive Breadth-Depth Retrieval](https://aclanthology.org/2026.acl-long.714/) | **ACL 2026 Main** | `inference` `trajectory/action` `tree-search/branching` |
| 2026 | [Active Exploring like a Pigeon: Reinforcing Spatial Reasoning via Agentic Vision-Language Models](https://icml.cc/virtual/2026/poster/61450) | **ICML 2026** | `inference` `trajectory/action` `structured-search` |
| 2025-09 | [EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning](https://arxiv.org/abs/2509.22576) | arXiv | `rl-training` `trajectory/action` `policy-distribution` `entropy/probability` `regularization` `gradient-reshaping` |
| 2025-05 | [Enhancing Diversity in Parallel Agents: A Maximum State Entropy Exploration Story](https://arxiv.org/abs/2505.01336) | arXiv | `inference` `trajectory/action` `entropy/probability` `semantic-diversity` `structured-search` |
| 2024 | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | TMLR 2024 | `continual/self-improvement` `trajectory/action` `data/task` `novelty/curiosity` `coverage` `curriculum/task-generation` |
| 2024 | [Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models](https://proceedings.mlr.press/v235/zhou24r.html) | ICML 2024 | `inference` `trajectory/action` `reward/advantage` `tree-search/branching` `replay/memory` |
| 2023 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | NeurIPS 2023 | `test-time-adaptation` `trajectory/action` `reward/advantage` `replay/memory` |
| 2023 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://openreview.net/forum?id=WE_vluYUL-X) | ICLR 2023 | `inference` `trajectory/action` `information-gain` `structured-search` |

## 4. Understanding, Evaluation & Benchmarks

This category collects empirical analyses, theoretical accounts, surveys, metrics, and benchmarks that help the field understand exploration. Rather than primarily proposing a new exploration intervention, these works measure diversity, characterize training dynamics, evaluate capability boundaries, or establish a shared vocabulary and test bed.

They are essential for judging whether a method genuinely improves exploration instead of merely changing accuracy or sampling behavior. Keeping them separate makes the evidence about a phenomenon easy to distinguish from methods designed to change it.

| Date | Paper | Source | Tags |
|---|---|---|---|
| 2026-05 | [Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning](https://arxiv.org/abs/2605.09292) | arXiv | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [Why Did Apple Fall: Evaluating Curiosity in Large Language Models](https://aclanthology.org/2026.findings-acl.1954/) | **ACL 2026 Findings** | `inference` `response/sequence` `novelty/curiosity` |
| 2026 | [When Greedy Wins: Emergent Exploitation Bias in Meta-Bandit LLM Training](https://iclr.cc/virtual/2026/poster/10008807) | **ICLR 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity](https://iclr.cc/virtual/2026/poster/10007331) | **ICLR 2026** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](https://icml.cc/virtual/2026/poster/62606) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` |
| 2026 | [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](https://aclanthology.org/2026.findings-acl.879/) | **ACL 2026 Findings** | `rl-training` `policy-distribution` `entropy/probability` `gradient-reshaping` |
| 2026 | [Understanding Reasoning Collapse in LLM Agent Reinforcement Learning](https://icml.cc/virtual/2026/poster/66821) | **ICML 2026** | `rl-training` `response/sequence` `structured-search` |
| 2026 | [The Unlearnability Phenomenon in RLVR for Language Models](https://icml.cc/virtual/2026/poster/64909) | **ICML 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward](https://iclr.cc/virtual/2026/poster/10006646) | **ICLR 2026** | `rl-training` `response/sequence` `semantic-diversity` `reward/advantage` |
| 2026 | [Single-Agent Generation Surpasses Multi-Agent Systems in Semantic Diversity](https://aclanthology.org/2026.findings-acl.1894/) | **ACL 2026 Findings** | `inference` `response/sequence` `population/multi-policy` `semantic-diversity` `ensemble/population` |
| 2026 | [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://iclr.cc/virtual/2026/poster/10007896) | **ICLR 2026** | `rl-training` `response/sequence` `reward/advantage` |
| 2026 | [Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems](https://icml.cc/virtual/2026/poster/63622) | **ICML 2026** | `inference` `population/multi-policy` `entropy/probability` `ensemble/population` |
| 2026 | [RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs](https://iclr.cc/virtual/2026/poster/10009898) | **ICLR 2026** | `supervised-post-training` `response/sequence` `structured-search` |
| 2026 | [Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently](https://icml.cc/virtual/2026/poster/64293) | **ICML 2026** | `rl-training` `policy-distribution` `backtracking/resampling` |
| 2026 | [Post-Training with Policy Gradients: Optimality and the Base Model Barrier](https://icml.cc/virtual/2026/poster/61683) | **ICML 2026** | `rl-training` `policy-distribution` `gradient-reshaping` |
| 2026 | [On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models](https://icml.cc/virtual/2026/poster/63897) | **ICML 2026** | `rl-training` `response/sequence` `entropy/probability` |
| 2026 | [Less Diverse, Less Safe: The Indirect But Pervasive Risk of Test-Time Scaling in Large Language Models](https://icml.cc/virtual/2026/poster/64671) | **ICML 2026** | `inference` `response/sequence` `semantic-diversity` |
| 2026 | [KL-Regularized Reinforcement Learning for Generative Modelling is Designed to Mode Collapse](https://iclr.cc/virtual/2026/poster/10008208) | **ICLR 2026** | `rl-training` `response/sequence` `regularization` |
| 2026 | [Generalization of RLVR Using Causal Reasoning as a Testbed](https://iclr.cc/virtual/2026/poster/10010768) | **ICLR 2026** | `rl-training` `policy-distribution` `structured-search` |
| 2026 | [Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward](https://iclr.cc/virtual/2026/poster/10007078) | **ICLR 2026** | `rl-training` `policy-distribution` `entropy/probability` `reward/advantage` `gradient-reshaping` |
| 2026 | [Exploration Hacking: LLMs Can Learn to Resist RL Training](https://icml.cc/virtual/2026/poster/64674) | **ICML 2026** | `inference` `response/sequence` `structured-search` |
| 2026 | [Does Reinforcement Fine-Tuning Improve Generalization of LLM Agents? An Empirical Study](https://icml.cc/virtual/2026/poster/65794) | **ICML 2026** | `rl-training` `response/sequence` `structured-search` |
| 2026 | [Demystifying Entropy Control in LLM RL Training: Theoretical Analysis and Dynamic Scheduling](https://icml.cc/virtual/2026/poster/62302) | **ICML 2026** | `inference` `response/sequence` `entropy/probability` |
| 2026 | [Breaking Barriers: Do Reinforcement Post Training Gains Transfer To Unseen Domains?](https://iclr.cc/virtual/2026/poster/10007526) | **ICLR 2026** | `rl-training` `response/sequence` `structured-search` |
| 2026 | [Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation](https://icml.cc/virtual/2026/poster/64547) | **ICML 2026** | `rl-training` `policy-distribution` `reward/advantage` `gradient-reshaping` |
| 2025-12 | [Diversity or Precision? A Deep Dive into Next Token Prediction](https://arxiv.org/abs/2512.22955) | arXiv | `inference` `token` `semantic-diversity` |
| 2025-11 | [Revisiting Entropy in Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2511.05993) | arXiv | `rl-training` `response/sequence` `entropy/probability` |
| 2025-10 | [The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View](https://arxiv.org/abs/2510.04028) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2025-08 | [From Trial-and-Error to Improvement: A Systematic Analysis of LLM Exploration Mechanisms in RLVR](https://arxiv.org/abs/2508.07534) | arXiv | `rl-training` `policy-distribution` `structured-search` |
| 2025-05 | [An Empirical Study on Reinforcement Learning for Reasoning-Search Interleaved LLM Agents](https://arxiv.org/abs/2505.15117) | arXiv | `rl-training` `response/sequence` `structured-search` |

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
