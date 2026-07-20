# Awesome-Exploration

**Detailed View** · [List View](README.md)

A curated, evidence-linked reading list on **exploration mechanisms in RL for LLMs**.

> **Scope.** Core entries directly propose, measure, or analyze exploration in RL-for-LLM training or inference. Adjacent entries supply essential diversity, evaluation, or capability-boundary context. Context entries are useful precedents from broader RL or applications, not evidence for an RL4LLM claim.

## How to use this catalog

- **Core** — direct RL4LLM exploration work.
- **Adjacent** — closely related evaluation, diversity, or capability-boundary work.
- **Context** — transferable ideas from other RL settings; interpret separately.
- Every public entry has one unique primary-source identifier. Ambiguous or source-less legacy records are held in `data/needs-verification.json` until verified.

## Inclusion policy

We include work with a primary-source link and a clear relationship to exploration: expanding the search space, controlling exploration/exploitation, measuring diversity or coverage, or testing whether exploration improves capability. Papers that merely use RL or LLMs without that connection belong in Context or are excluded.

## Contributing

Please open an issue or PR with the paper title, primary link, relevant section, scope label, and a one-sentence rationale. Edit `data/papers.json`; the two README files are generated.

## 1. Survey & Frameworks

- **Switch-Reasoner: Learn When to Think in Multitask Mixtures via Reinforcement Learning** — `Core` · [arXiv:2607.08572](https://arxiv.org/abs/2607.08572)
- **TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models** — `Core` · [arXiv:2604.26553](https://arxiv.org/abs/2604.26553)
- **In-Token Rationality Optimization: Towards Accurate and Concise LLM Reasoning via Self-Feedback** — `Core` · [arXiv:2511.09865](https://arxiv.org/abs/2511.09865)
- **LLM-Based Scientific Equation Discovery via Physics-Informed Token-Regularized Policy Optimization** — `Core` · [arXiv:2602.10576](https://arxiv.org/abs/2602.10576)
- **Joint Selection for Large-Scale Pre-Training Data via Policy Gradient-based Mask Learning** — `Core` · [arXiv:2512.24265](https://arxiv.org/abs/2512.24265)
- **OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning** — `Core` · [arXiv:2605.21851](https://arxiv.org/abs/2605.21851)
- **C2GSPG: Confidence-calibrated Group Sequence Policy Gradient towards Self-aware Reasoning** — `Core` · [arXiv:2509.23129](https://arxiv.org/abs/2509.23129)
- **Contextually Entangled Gradient Mapping for Optimized LLM Comprehension** — `Core` · [arXiv:2502.00048](https://arxiv.org/abs/2502.00048)
- **GRADE: Replacing Policy Gradients with Backpropagation for LLM Alignment** — `Core` · [arXiv:2601.11574](https://arxiv.org/abs/2601.11574)
- **GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy** — `Core` · [arXiv:2508.04349](https://arxiv.org/abs/2508.04349)
- **OpenSIR: Open-Ended Self-Improving Reasoner** — `Core` · [arXiv:2511.00602](https://arxiv.org/abs/2511.00602)
- **Don't Let Gains FADE: Breaking Down Policy Gradient Weights in RL** — `Core` · [arXiv:2607.01490](https://arxiv.org/abs/2607.01490)
- **Modularized Reinforcement Learning on LLMs: From MDP Creation to Exploration and Learning** — `Core` · [arXiv:2606.21943](https://arxiv.org/abs/2606.21943)
- **Heuresis: Search Strategies for Autonomous AI Research Agents Across Quality, Diversity and Novelty** — `Core` · [arXiv:2606.25198](https://arxiv.org/abs/2606.25198)
- **Meta-Thinking in LLMs via Multi-Agent Reinforcement Learning: A Survey** — `Core` · [arXiv:2504.14520](https://arxiv.org/abs/2504.14520)
- **Inverse Reinforcement Learning Meets Large Language Model Post-Training: Basics, Advances, and Opportunities** — `Core` · [arXiv:2507.13158](https://arxiv.org/abs/2507.13158)
- **Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards** — `Context` · [arXiv:2605.14117](https://arxiv.org/abs/2605.14117)
- **RLFactory: A Plug-and-Play Reinforcement Learning Post-Training Framework for LLM Multi-Turn Tool-Use** — `Core` · [arXiv:2509.06980](https://arxiv.org/abs/2509.06980)
  - large language models excel at basic reasoning but struggle with tasks that require interaction with external tools.
- **The Landscape of Agentic Reinforcement Learning for LLMs: A Survey** — `Core` · [arXiv:2509.02547](https://arxiv.org/abs/2509.02547)
- **From Trial-and-Error to Improvement: A Systematic Analysis of LLM Exploration Mechanisms in RLVR** — `Core` · [arXiv:2508.07534](https://arxiv.org/abs/2508.07534)
  - Systematic study of exploration capabilities in LLM RLVR training. Organizes the field around three dimensions: constructing exploration space, entropy-performance interaction, and performance improvement.
- **Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining** — `Context` · [arXiv:2505.11122](https://arxiv.org/abs/2505.11122)
  - alpha factor mining is pivotal in quantitative investment for identifying predictive signals from complex financial data.
- **COS(M+O)S: Curiosity and RL-Enhanced MCTS for Exploring Story Space via Language Models** — `Context` · [arXiv:2501.17104](https://arxiv.org/abs/2501.17104)
- **LLM Post-Training: A Deep Dive into Reasoning Large Language Models** — `Core` · [arXiv:2502.21321](https://arxiv.org/abs/2502.21321)
- **Discovery and Reinforcement of Tool-Integrated Reasoning Chains via Rollout Trees** — `Context` · [arXiv:2601.08274](https://arxiv.org/abs/2601.08274)
- **GFlowPO: Generative Flow Network as a Language Model Prompt Optimizer** — `Core` · [arXiv:2602.03358](https://arxiv.org/abs/2602.03358)
- **Towards a Unified View of Large Language Model Post-Training** — `Core` · [arXiv:2509.04419](https://arxiv.org/abs/2509.04419)
- **Reinforced MLLM: A Survey on RL-Based Reasoning in Multimodal Large Language Models** — `Core` · [arXiv:2504.21277](https://arxiv.org/abs/2504.21277)
- **Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models** — `Core` · [arXiv:2503.16419](https://arxiv.org/abs/2503.16419)
- **A Comparative Theoretical Analysis of Entropy Control Methods in Reinforcement Learning** — `Core` · [arXiv:2604.09676](https://arxiv.org/abs/2604.09676)
- **On the Entropy Dynamics in Reinforcement Fine-Tuning of Large Language Models** — `Core` · [arXiv:2602.03392](https://arxiv.org/abs/2602.03392)
- **A Formula-Driven Survey and Research Agenda for On-Policy Distillation** — `Core` · [arXiv:2606.22793](https://arxiv.org/abs/2606.22793)
- **A Survey on LLM Test-Time Compute via Search: Tasks, LLM Profiling, Search Algorithms, and Relevant Frameworks** — `Core` · [arXiv:2501.10069](https://arxiv.org/abs/2501.10069)
- **Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs** — `Core` · [arXiv:2507.02076](https://arxiv.org/abs/2507.02076)
- **GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning** — `Core` · [arXiv:2506.16141](https://arxiv.org/abs/2506.16141)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** — `Core` · [arXiv:2602.05548](https://arxiv.org/abs/2602.05548)

## 2. Token-Level Exploration

- **Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood** — `Core` · [arXiv:2604.12736v1](https://arxiv.org/abs/2604.12736v1)
- **Where Hindsight Credit Can Reside: A Signed-Capacity View of Token Updates in RLVR** — `Core` · [arXiv:2604.11056v2](https://arxiv.org/abs/2604.11056v2)
- **ARCA: Adapter-Residual Credit Assignment When Token Signals Degenerate** — `Core` · [arXiv:2606.00257v1](https://arxiv.org/abs/2606.00257v1)
- **Heterogeneous Adaptive Policy Optimization: Tailoring Optimization to Every Token's Nature** — `Core` · [arXiv:2509.16591v2](https://arxiv.org/abs/2509.16591v2)
- **Beyond Penalizing Mistakes: Stabilizing Efficiency Training in Large Reasoning Models via Adaptive Correct-Only Rewards** — `Core` · [arXiv:2606.22716](https://arxiv.org/abs/2606.22716)
- **STORM: Stepwise Token Optimization with Reward-Guided Beam Search** — `Core` · [arXiv:2606.10621](https://arxiv.org/abs/2606.10621)
- **Not All Tokens Learn Alike: Attention Entropy Reveals Heterogeneous Signals in RL Reasoning** — `Core` · [arXiv:2605.07660](https://arxiv.org/abs/2605.07660)
- **Dynamic Rollout Editing for Reducing Overthinking in RL-Trained Reasoning Models** — `Core` · [arXiv:2606.17890](https://arxiv.org/abs/2606.17890)
- **CARE: Competence-Aware Reward Shaping for Adaptive Reasoning Length in Video-MLLMs** — `Core` · [arXiv:2606.19927](https://arxiv.org/abs/2606.19927)
- **3SPO: State-Score-Supervised Policy Optimization for LLM Agents** — `Core` · [arXiv:2606.09961](https://arxiv.org/abs/2606.09961)
- **VeriGate: Verifier-Gated Step-Level Supervision for GRPO** — `Core` · [arXiv:2605.30451](https://arxiv.org/abs/2605.30451)
- **VIMPO: Value-Implicit Policy Optimization for LLMs** — `Core` · [arXiv:2606.20008](https://arxiv.org/abs/2606.20008)
- **EchoRL: Reinforcement Learning via Rollout Echoing** — `Core` · [arXiv:2605.31228](https://arxiv.org/abs/2605.31228)
- **ERPO: Token-Level Entropy-Regulated Policy Optimization for Large Reasoning Models** — `Core` · [arXiv:2603.28204](https://arxiv.org/abs/2603.28204)
- **Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL** — `Core` · [arXiv:2602.13035](https://arxiv.org/abs/2602.13035)
- **MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning** — `Core` · [arXiv:2602.17550](https://arxiv.org/abs/2602.17550)
- **Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning** — `Core` · [arXiv:2512.04359](https://arxiv.org/abs/2512.04359)
- **From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training** — `Core` · [arXiv:2511.07738](https://arxiv.org/abs/2511.07738)
- **Semantic-Space Exploration and Exploitation in RLVR for LLM Reasoning** — `Core` · [arXiv:2509.23808](https://arxiv.org/abs/2509.23808)
- **On Entropy Control in LLM-RL Algorithms** — `Core` · [arXiv:2509.03493](https://arxiv.org/abs/2509.03493)
  - for rl algorithms, appropriate entropy control is crucial to their effectiveness.
- **Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration** — `Core` · [arXiv:2508.13755](https://arxiv.org/abs/2508.13755)

## 2. Token-Level Exploration / 2.1 Entropy-Aware Mechanisms

- **Asymmetric On-Policy Distillation: Bridging Exploitation and Imitation at the Token Level** — `Core` · [arXiv:2605.06387](https://arxiv.org/abs/2605.06387)
- **Rethinking Token-Level Credit Assignment in RLVR: A Polarity-Entropy Analysis** — `Core` · [arXiv:2604.11056](https://arxiv.org/abs/2604.11056)
- **EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Reward** — `Core` · [arXiv:2605.04960](https://arxiv.org/abs/2605.04960)
- **Targeted Exploration via Unified Entropy Control for Reinforcement Learning** — `Core` · [arXiv:2604.14646](https://arxiv.org/abs/2604.14646)
  - Unified entropy control framework for targeted exploration in LLM RL training.
- **Addressing Performance Saturation for LLM RL via Precise Entropy Curve Control** — `Core` · [arXiv:2604.26326](https://arxiv.org/abs/2604.26326)
  - Analyzes entropy curves during RL training and proposes precise control to combat performance saturation.
- **Token Hidden Reward: Steering Exploration-Exploitation in Group Relative Deep Reinforcement Learning** — `Core` · [arXiv:2510.03669](https://arxiv.org/abs/2510.03669)
  - Introduces token-level hidden rewards to guide exploration-exploitation in GRPO-based training.
- **CURE: Critical-Token-Guided Re-Concatenation for Entropy-Collapse Prevention** — `Core` · [arXiv:2508.11016](https://arxiv.org/abs/2508.11016)
  - Reviews how critical tokens affect entropy collapse; proposes token re-concatenation strategy to maintain exploration.
- **Stabilizing Knowledge, Promoting Reasoning: Dual-Token Constraints for RLVR** — `Core` · [arXiv:2507.15778](https://arxiv.org/abs/2507.15778)
- **Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities** — `Core` · [arXiv:2602.05281](https://arxiv.org/abs/2602.05281)
- **Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs** — `Core` · [arXiv:2603.22446](https://arxiv.org/abs/2603.22446)
- **Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective** — `Core` · [arXiv:2510.10150](https://arxiv.org/abs/2510.10150)

## 2. Token-Level Exploration / 2.2 High-Entropy Token Targeting

- **Entropy-KL Divergence-based Token Masking: A Novel Approach for Selective Fine-tuning of Large Language Models** — `Core` · [arXiv:2605.29303](https://arxiv.org/abs/2605.29303)
- **Where Rollouts Begin: Low-Load, High-Leverage First-Token Diversification for RLVR** — `Core` · [arXiv:2605.28295](https://arxiv.org/abs/2605.28295)
- **Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning** — `Core` · [arXiv:2506.01939](https://arxiv.org/abs/2506.01939)

## 2. Token-Level Exploration / 2.3 Low-Probability Token Regularization

- **Rethinking Importance Sampling in LLM Policy Optimization: A Cumulative Token Perspective** — `Core` · [arXiv:2605.07331](https://arxiv.org/abs/2605.07331)
- **Compress the Easy, Explore the Hard: Difficulty-Aware Entropy Regularization for Efficient LLM Reasoning** — `Core` · [arXiv:2602.22642](https://arxiv.org/abs/2602.22642)
  - Difficulty-aware entropy regularization that compresses easy tokens while encouraging exploration on hard ones.

## 2. Token-Level Exploration / 2.4 Policy Gradient Reshaping

- **Token-Efficient RL for LLM Reasoning** — `Core` · [arXiv:2504.20834](https://arxiv.org/abs/2504.20834)
- **Discriminative Policy Optimization for Token-Level Reward Models** — `Core` · [arXiv:2505.23363](https://arxiv.org/abs/2505.23363)
- **Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning** — `Core` · [arXiv:2607.07508](https://arxiv.org/abs/2607.07508)
- **Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space** — `Core` · [arXiv:2505.13308](https://arxiv.org/abs/2505.13308)
- **ResT: Reshaping Token-Level Policy Gradients for Tool-Use Large Language Models** — `Core` · [arXiv:2509.21826](https://arxiv.org/abs/2509.21826)
- **Beyond Token-Level Policy Gradients for Complex Reasoning with Large Language Models** — `Core` · [arXiv:2602.14386](https://arxiv.org/abs/2602.14386)
- **Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization** — `Core` · [arXiv:2511.20718](https://arxiv.org/abs/2511.20718)
- **KL-Regularised Q-Learning: A Token-level Action-Value perspective on Online RLHF** — `Core` · [arXiv:2508.17000](https://arxiv.org/abs/2508.17000)
- **Text-to-SPARQL Generation with Reinforcement Learning: A GRPO-based Approach on DBLP** — `Core` · [arXiv:2605.20066](https://arxiv.org/abs/2605.20066)
- **DiPO: Disentangled Perplexity Policy Optimization for Fine-grained Exploration-Exploitation Trade-Off** — `Core` · [arXiv:2604.13902](https://arxiv.org/abs/2604.13902)
  - Disentangles perplexity from policy optimization, enabling fine-grained control over exploration-exploitation balance.
- **Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models** — `Core` · [arXiv:2601.22478](https://arxiv.org/abs/2601.22478)
  - Augments GRPO with transformation operations to diversify reasoning paths and enhance exploration.
- **Whatever Remains Must Be True: Filtering Drives Reasoning in LLMs, Shaping Diversity** — `Core` · [arXiv:2512.05962](https://arxiv.org/abs/2512.05962)
- **Think Before You Retrieve: Learning Test-Time Adaptive Search with Small Language Models** — `Core` · [arXiv:2511.07581](https://arxiv.org/abs/2511.07581)
- **SIMKO: SIMPLE PASS@K POLICY OPTIMIZATION** — `Core` · [arXiv:2510.03222](https://arxiv.org/abs/2510.03222)
- **No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping** — `Core` · [arXiv:2509.21880](https://arxiv.org/abs/2509.21880)
- **$λ$-GRPO: Unifying the GRPO Frameworks with Learnable Token Preferences** — `Core` · [arXiv:2510.06870](https://arxiv.org/abs/2510.06870)
- **TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization** — `Core` · [arXiv:2606.05859](https://arxiv.org/abs/2606.05859)
- **Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought** — `Core` · [arXiv:2603.22847](https://arxiv.org/abs/2603.22847)
- **Selective-Advantage Entropy-Adaptive Horizon GRPO: Asymmetric Token-Level Discounting for Efficient Reinforcement Learning of Language Models** — `Core` · [arXiv:2606.05434](https://arxiv.org/abs/2606.05434)
- **Asymmetric Advantage Modulation Calibrates Entropy Dynamics in RLVR** — `Core` · [arXiv:2604.04894](https://arxiv.org/abs/2604.04894)
- **APPO: Agentic Procedural Policy Optimization** — `Core` · [arXiv:2606.12384](https://arxiv.org/abs/2606.12384)
- **PAEC: Position-Aware Entropy Calibration for LLM Reasoning in RLVR** — `Core` · [arXiv:2606.08543](https://arxiv.org/abs/2606.08543)
- **Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning** — `Core` · [arXiv:2606.19771](https://arxiv.org/abs/2606.19771)
- **STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Stability** — `Core` · [arXiv:2606.19236](https://arxiv.org/abs/2606.19236)
- **LLMs for Game Theory: Entropy-Guided In-Context Learning and Adaptive CoT Reasoning** — `Core` · [arXiv:2601.10775](https://arxiv.org/abs/2601.10775)
- **Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning** — `Core` · [arXiv:2606.10968](https://arxiv.org/abs/2606.10968)
- **When Implausible Tokens Get Reinforced: Tail-Aware Credit Calibration for LLM Reinforcement Learning** — `Core` · [arXiv:2607.07976](https://arxiv.org/abs/2607.07976)
- **On Advantage Estimates for Max@K Policy Gradients** — `Core` · [arXiv:2606.06080](https://arxiv.org/abs/2606.06080)
- **Dropout-GRPO: Variational Stochasticity for Continuous Latent Reasoning** — `Core` · [arXiv:2606.10184](https://arxiv.org/abs/2606.10184)
- **DemoPSD: Disagreement-Modulated Policy Self-Distillation** — `Core` · [arXiv:2607.02502](https://arxiv.org/abs/2607.02502)
- **Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning** — `Core` · [arXiv:2605.22263](https://arxiv.org/abs/2605.22263)
- **Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment** — `Core` · [arXiv:2607.04728](https://arxiv.org/abs/2607.04728)
- **ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy** — `Core` · [arXiv:2607.03126](https://arxiv.org/abs/2607.03126)
- **Trajectory-Refined Distillation** — `Core` · [arXiv:2606.08432](https://arxiv.org/abs/2606.08432)
- **Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes** — `Core` · [arXiv:2603.25562](https://arxiv.org/abs/2603.25562)
- **STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens** — `Core` · [arXiv:2602.15620](https://arxiv.org/abs/2602.15620)

## 3. Sequence / Response-Level Exploration

- **Exploiting Verification-Generation Gap: Test-Time Reinforcement Learning with Confidence-Conditioned Verification** — `Core` · [arXiv:2606.03608v1](https://arxiv.org/abs/2606.03608v1)
- **Single-Rollout Hidden-State Dynamics for Training-Free RLVR Data Selection** — `Core` · [arXiv:2605.28631v1](https://arxiv.org/abs/2605.28631v1)
- **Learning with a Single Rollout via Monte Carlo Pass@k Critic** — `Core` · [arXiv:2606.25451v1](https://arxiv.org/abs/2606.25451v1)
- **Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards** — `Core` · [arXiv:2606.18810v1](https://arxiv.org/abs/2606.18810v1)
- **GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcement Learning** — `Core` · [arXiv:2606.26917](https://arxiv.org/abs/2606.26917)
- **DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models** — `Core` · [arXiv:2606.23181](https://arxiv.org/abs/2606.23181)
- **TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning** — `Core` · [arXiv:2606.11119](https://arxiv.org/abs/2606.11119)
- **Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework** — `Core` · [arXiv:2605.22620](https://arxiv.org/abs/2605.22620)
- **Self-Distilled RLVR** — `Core` · [arXiv:2604.03128](https://arxiv.org/abs/2604.03128)
- **HISR: Hindsight Information Modulated Segmental Process Rewards For Multi-turn Agentic Reinforcement Learning** — `Core` · [arXiv:2603.18683](https://arxiv.org/abs/2603.18683)
- **ExTra: Exploratory Trajectory Optimization for Language Model Reinforcement Learning** — `Core` · [arXiv:2606.24994](https://arxiv.org/abs/2606.24994)
- **GraphPO: Graph-based Policy Optimization for Reasoning Models** — `Core` · [arXiv:2606.18954](https://arxiv.org/abs/2606.18954)
- **StarOR: Synergizing Tree Search and Test-Time Reinforcement Learning for Optimization Modeling** — `Core` · [arXiv:2606.15197](https://arxiv.org/abs/2606.15197)
- **ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL** — `Core` · [arXiv:2606.01619](https://arxiv.org/abs/2606.01619)
- **PACR: Progressively Ascending Confidence Reward for LLM Reasoning** — `Core` · [arXiv:2510.22255](https://arxiv.org/abs/2510.22255)
- **From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning** — `Core` · [arXiv:2605.22074](https://arxiv.org/abs/2605.22074)
- **Reward Hacking Mitigation using Verifiable Composite Rewards** — `Core` · [arXiv:2509.15557](https://arxiv.org/abs/2509.15557)
- **EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning** — `Core` · [arXiv:2508.07809](https://arxiv.org/abs/2508.07809)
- **Rewarding Graph Reasoning Process makes LLMs more Generalized Reasoners** — `Core` · [arXiv:2503.00845](https://arxiv.org/abs/2503.00845)
- **Graph-O1 : Monte Carlo Tree Search with Reinforcement Learning for Text-Attributed Graph Reasoning** — `Core` · [arXiv:2512.17912](https://arxiv.org/abs/2512.17912)
- **Hint-Guided Diversified Policy Optimization for LLM Reasoning** — `Core` · [arXiv:2606.03021](https://arxiv.org/abs/2606.03021)
- **PrAg-PO: Prompt Augmented Policy Optimization for Robust and Diverse Mathematical Reasoning** — `Core` · [arXiv:2602.03190](https://arxiv.org/abs/2602.03190)
- **SetPO: Set-Level Policy Optimization for Diversity-Preserving LLM Reasoning** — `Core` · [arXiv:2602.01062](https://arxiv.org/abs/2602.01062)
- **Quality-constrained Entropy Maximization Policy Optimization for LLM Diversity** — `Core` · [arXiv:2602.15894](https://arxiv.org/abs/2602.15894)
- **When RL Suppresses Its Own Vocabulary: Recovering Reasoning Diversity in Puzzle-to-Math Transfer** — `Core` · [arXiv:2605.29190](https://arxiv.org/abs/2605.29190)
- **Recovering Diversity Without Losing Alignment: A DPO Recipe for Post-Trained LLMs** — `Adjacent` · [arXiv:2605.30021](https://arxiv.org/abs/2605.30021)
- **Vector Policy Optimization: Training for Diversity Improves Test-Time Search** — `Core` · [arXiv:2605.22817](https://arxiv.org/abs/2605.22817)
- **Beyond Mode Collapse: Distribution Matching for Diverse Reasoning** — `Core` · [arXiv:2605.19461](https://arxiv.org/abs/2605.19461)
- **How You Begin is How You Reason: Driving Exploration in RLVR via Prefix-Tuned Priors** — `Core` · [arXiv:2605.08817](https://arxiv.org/abs/2605.08817)
- **Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR** — `Core` · [arXiv:2605.15726](https://arxiv.org/abs/2605.15726)
- **EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization** — `Core` · [arXiv:2605.14249](https://arxiv.org/abs/2605.14249)
- **""Like Taking the Path of Least Resistance": Exploring the Impact of LLM Interaction on the Creative Process of Programming"** — `Core` · [arXiv:2605.13776](https://arxiv.org/abs/2605.13776)
- **CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR** — `Adjacent` · [arXiv:2603.10101](https://arxiv.org/abs/2603.10101)
  - reinforcement learning with verifiable rewards (rlvr) has significantly advanced the reasoning capacity of large language models (llms).
- **Outcome-based Exploration for LLM Reasoning** — `Core` · [arXiv:2602.03635](https://arxiv.org/abs/2602.03635)
  - Explores outcome-level mechanisms for promoting exploration in LLM reasoning tasks.
- **Beyond Mode Elicitation: Diversity-Preserving Reinforcement Learning via Latent Diffusion Reasoner** — `Core` · [arXiv:2602.01705](https://arxiv.org/abs/2602.01705)
  - Uses latent diffusion to preserve reasoning diversity during RL training, preventing mode collapse.
- **DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning** — `Core` · [arXiv:2602.19895](https://arxiv.org/abs/2602.19895)
  - Dual-scale diversity regularization operating at both token and response levels.
- **UpSkill: Mutual Information Skill Learning for Structured Response Diversity in LLMs** — `Adjacent` · [arXiv:2602.22296](https://arxiv.org/abs/2602.22296)
- **Reinforced Efficient Reasoning via Semantically Diverse Exploration** — `Adjacent` · [arXiv:2601.05053](https://arxiv.org/abs/2601.05053)
  - Combines semantic diversity rewards with RL to encourage exploration across reasoning paths.
- **Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs** — `Context` · [arXiv:2601.08763](https://arxiv.org/abs/2601.08763)
  - Rewards unique/uncommon solutions to encourage creative exploration beyond standard reasoning paths.
- **Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning** — `Adjacent` · [arXiv:2512.15687](https://arxiv.org/abs/2512.15687)
- **Diversity or Precision? A Deep Dive into Next Token Prediction** — `Adjacent` · [arXiv:2512.22955](https://arxiv.org/abs/2512.22955)
  - Analyzes the tension between diversity and precision in next-token prediction during RL training.
- **Count Counts: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards** — `Adjacent` · [arXiv:2510.16614](https://arxiv.org/abs/2510.16614)
  - reinforcement learning (rl) has become a compelling way to strengthen the multi step reasoning ability of large language models (llms).
- **The Road Less Traveled: Enhancing Exploration in LLMs via Sequential Sampling** — `Core` · [arXiv:2510.15502](https://arxiv.org/abs/2510.15502)
  - Sequential sampling strategy that prioritizes less-explored reasoning paths during LLM training.
- **More Than One Teacher: Adaptive Multi-Guidance Policy Optimization for Diverse Exploration** — `Core` · [arXiv:2510.02227](https://arxiv.org/abs/2510.02227)
  - Uses multiple guidance signals to promote diverse exploration across different reasoning strategies.
- **Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning** — `Core` · [arXiv:2510.10649](https://arxiv.org/abs/2510.10649)
  - Shapes advantage estimates based on prediction uncertainty to encourage deeper exploration in RLVR.
- **Selective Expert Guidance for Effective and Diverse Exploration in Reinforcement Learning of LLMs** — `Core` · [arXiv:2510.04140](https://arxiv.org/abs/2510.04140)
  - Uses expert guidance to selectively steer exploration toward promising but under-explored regions.
- **Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents** — `Adjacent` · [arXiv:2509.09265](https://arxiv.org/abs/2509.09265)
- **Enhancing Diversity in Large Language Models via Determinantal Point Processes** — `Adjacent` · [arXiv:2509.06941](https://arxiv.org/abs/2509.06941)
- **Learning from Diverse Reasoning Paths with Routing and Collaboration** — `Adjacent` · [arXiv:2508.16861](https://arxiv.org/abs/2508.16861)
  - advances in large language models (llms) significantly enhance reasoning capabilities but their deployment is restricted in resource-constrained scenarios.
- **TreeRL: LLM Reinforcement Learning with On-Policy Tree Search** — `Adjacent` · [arXiv:2506.11902](https://arxiv.org/abs/2506.11902)
  - reinforcement learning (rl) with tree search has demonstrated superior performance in traditional reasoning tasks.
- **EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework** — `Core` · [arXiv:2506.22200](https://arxiv.org/abs/2506.22200)
  - Exploration-Filter-Replay framework that systematically discovers and reuses diverse reasoning strategies.
- **DeepTheorem: Advancing LLM Reasoning for Theorem Proving Through Natural Language and Reinforcement Learning** — `Adjacent` · [arXiv:2505.23754](https://arxiv.org/abs/2505.23754)
  - theorem proving serves as a major testbed for evaluating complex reasoning abilities in large language models (llms).
- **Enhancing Diversity in Parallel Agents: A Maximum State Entropy Exploration Story** — `Adjacent` · [arXiv:2505.01336](https://arxiv.org/abs/2505.01336)
- **DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning** — `Adjacent` · [arXiv:2505.09655](https://arxiv.org/abs/2505.09655)
- **Improving RL Exploration for LLM Reasoning through Retrospective Replay** — `Core` · [arXiv:2504.14363](https://arxiv.org/abs/2504.14363)
  - Introduces retrospective replay to revisit and learn from past exploration trajectories in LLM RL, improving sample efficiency and discovery of novel reasoning paths.
- **Entropy-guided sequence weighting for efficient exploration in RL-based LLM fine-tuning** — `Adjacent` · [arXiv:2503.22456](https://arxiv.org/abs/2503.22456)
- **LaTER: Efficient Test-Time Reasoning via Latent Exploration and Explicit Verification** — `Core` · [arXiv:2605.07315](https://arxiv.org/abs/2605.07315)
- **Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration** — `Core` · [arXiv:2605.10195](https://arxiv.org/abs/2605.10195)
- **TMAS: Scaling Test-Time Compute via Multi-Agent Synergy** — `Core` · [arXiv:2605.10344](https://arxiv.org/abs/2605.10344)
- **Long Live The Balance: Information Bottleneck Driven Tree-based Policy Optimization** — `Core` · [arXiv:2605.28109](https://arxiv.org/abs/2605.28109)
- **Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis** — `Core` · [arXiv:2604.24198](https://arxiv.org/abs/2604.24198)
- **Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes** — `Core` · [arXiv:2604.18381](https://arxiv.org/abs/2604.18381)
- **Reasoning through Exploration: A Reinforcement Learning Framework for Robust Function Calling** — `Core` · [arXiv:2508.05118](https://arxiv.org/abs/2508.05118)
- **Learning from Self-Debate: Preparing Reasoning Models for Multi-Agent Debate** — `Core` · [arXiv:2601.22297](https://arxiv.org/abs/2601.22297)
- **The Markovian Thinker: Architecture-Agnostic Linear Scaling of Reasoning** — `Adjacent` · [arXiv:2510.06557](https://arxiv.org/abs/2510.06557)
- **Not All Rollouts are Useful: Down-Sampling Rollouts in LLM Reinforcement Learning** — `Core` · [arXiv:2504.13818](https://arxiv.org/abs/2504.13818)
- **Unrewarded Exploration in Large Language Models Reveals Latent Learning from Psychology** — `Core` · [arXiv:2601.22474](https://arxiv.org/abs/2601.22474)
- **Multi-Path Collaborative Reasoning via Reinforcement Learning** — `Core` · [arXiv:2512.01485](https://arxiv.org/abs/2512.01485)
- **ETR: Entropy Trend Reward for Efficient Chain-of-Thought Reasoning** — `Core` · [arXiv:2604.05355](https://arxiv.org/abs/2604.05355)
- **DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents** — `Core` · [arXiv:2604.24320](https://arxiv.org/abs/2604.24320)
- **DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning** — `Core` · [arXiv:2605.30859](https://arxiv.org/abs/2605.30859)
- **Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization** — `Core` · [arXiv:2602.10048](https://arxiv.org/abs/2602.10048)
- **Information Gain-based Rollout Policy Optimization: An Adaptive Tree-Structured Rollout Approach for Multi-Turn LLM Agents** — `Core` · [arXiv:2607.06223](https://arxiv.org/abs/2607.06223)
- **STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training** — `Core` · [arXiv:2607.04963](https://arxiv.org/abs/2607.04963)
- **Process Advantage Signal Shaping: A Paradigm-Agnostic Middleware for Process-Supervised RL in LLM Reasoners** — `Core` · [arXiv:2606.29296](https://arxiv.org/abs/2606.29296)
- **Where to Spend Rollouts: Hit-Utility Optimal Rollout Allocation for Group-Based RLVR** — `Core` · [arXiv:2605.07114](https://arxiv.org/abs/2605.07114)
- **RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents** — `Core` · [arXiv:2607.04713](https://arxiv.org/abs/2607.04713)
- **PAINT: Partial-Solution Adaptive Interpolated Training for Self-Distilled Reasoners** — `Core` · [arXiv:2604.26573](https://arxiv.org/abs/2604.26573)
- **Rollout-Level Advantage-Prioritized Experience Replay for GRPO** — `Core` · [arXiv:2606.04560](https://arxiv.org/abs/2606.04560)
- **How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization** — `Core` · [arXiv:2602.19208](https://arxiv.org/abs/2602.19208)

## 4. Policy Distribution-Level Exploration

- **A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization** — `Core` · [arXiv:2606.16154v1](https://arxiv.org/abs/2606.16154v1)
- **Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization** — `Core` · [arXiv:2605.11491v1](https://arxiv.org/abs/2605.11491v1)
- **Sparsity Curse: Understanding RLVR Model Parameter Space from Model Merging** — `Core` · [arXiv:2606.18521v1](https://arxiv.org/abs/2606.18521v1)
- **EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance** — `Core` · [arXiv:2605.04960v1](https://arxiv.org/abs/2605.04960v1)
- **SCOPE-RL: Stable and Quantitative Control of Policy Entropy in RL Post-Training** — `Core` · [arXiv:2510.08141v7](https://arxiv.org/abs/2510.08141v7)
- **Exploring Multi-Temperature Strategies for Token- and Rollout-Level Control in RLVR** — `Core` · [arXiv:2510.08892v1](https://arxiv.org/abs/2510.08892v1)
- **Soft Adaptive Policy Optimization** — `Core` · [arXiv:2511.20347v2](https://arxiv.org/abs/2511.20347v2)
- **XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation** — `Core` · [arXiv:2510.06672](https://arxiv.org/abs/2510.06672)
- **GHPO: Adaptive Guidance for Stable and Efficient LLM Reinforcement Learning** — `Core` · [arXiv:2507.10628](https://arxiv.org/abs/2507.10628)
- **Pinpointing crucial steps: Attribution-based Credit Assignment for Verifiable Reinforcement Learning** — `Core` · [arXiv:2510.08899](https://arxiv.org/abs/2510.08899)
- **Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning** — `Core` · [arXiv:2509.03646](https://arxiv.org/abs/2509.03646)
- **Agentic Policy Optimization via Instruction-Policy Co-Evolution** — `Core` · [arXiv:2512.01945](https://arxiv.org/abs/2512.01945)
- **Bottom-up Policy Optimization: Your Language Model Policy Secretly Contains Internal Policies** — `Core` · [arXiv:2512.19673](https://arxiv.org/abs/2512.19673)
- **DISA: Offline Importance Sampling for Distribution-Matching LLM-RL** — `Core` · [arXiv:2605.17295](https://arxiv.org/abs/2605.17295)
- **EEPO: Exploration-Enhanced Policy Optimization via Sample-Then-Forget** — `Core` · [arXiv:2510.05837](https://arxiv.org/abs/2510.05837)
- **COPO: Consistency-Aware Policy Optimization** — `Core` · [arXiv:2508.04138](https://arxiv.org/abs/2508.04138)
- **Policy of Thoughts: Scaling LLM Reasoning via Test-time Policy Evolution** — `Core` · [arXiv:2601.20379](https://arxiv.org/abs/2601.20379)
- **Random Policy Valuation is Enough for LLM Reasoning with Verifiable Rewards** — `Core` · [arXiv:2509.24981](https://arxiv.org/abs/2509.24981)
- **Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences for LLM Reasoning** — `Core` · [arXiv:2602.04380](https://arxiv.org/abs/2602.04380)
- **Cast a Wider Net: Coordinated Pass@K Policy Optimization for Code Reasoning** — `Core` · [arXiv:2605.27000](https://arxiv.org/abs/2605.27000)
- **Agent Explorative Policy Optimization for Multimodal Agentic Reasoning** — `Core` · [arXiv:2605.28774](https://arxiv.org/abs/2605.28774)
- **EAPO: Entropy-Driven Adaptive Positive-Negative Sample Weighting for Policy Optimization in Open-Ended QA** — `Core` · [arXiv:2605.27846](https://arxiv.org/abs/2605.27846)
- **expo: Exploration-prioritized policy optimization via adaptive KL regulation and Gaussian noise injection** — `Core` · [arXiv:2605.09923](https://arxiv.org/abs/2605.09923)
- **fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive KL and gradient regulation** — `Core` · [arXiv:2605.11403](https://arxiv.org/abs/2605.11403)
- **Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning** — `Core` · [arXiv:2602.20197](https://arxiv.org/abs/2602.20197)
  - Proposes controllable exploration mechanisms in hybrid-policy RLVR to systematically adjust exploration intensity during multi-modal reasoning training.
- **Temperature as a Meta-Policy: Adaptive Temperature in LLM Reinforcement Learning** — `Core` · [arXiv:2602.11779](https://arxiv.org/abs/2602.11779)
  - Models temperature as a learnable meta-policy to dynamically balance exploration-exploitation during LLM RL training.
- **IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck** — `Core` · [arXiv:2601.05870](https://arxiv.org/abs/2601.05870)
  - Information bottleneck approach to control exploration-exploitation trade-off in latent policy space.
- **Explore Data Left Behind in Reinforcement Learning for Reasoning Language Models** — `Core` · [arXiv:2511.04800](https://arxiv.org/abs/2511.04800)
  - Analyzes data distribution skew in RL training and proposes methods to explore underutilized data regions.
- **RiskPO: Risk-based Policy Optimization via Verifiable Reward for LLM Post-Training** — `Core` · [arXiv:2510.00911](https://arxiv.org/abs/2510.00911)
  - Risk-sensitive policy optimization that balances exploration of high-risk-high-reward strategies.
- **Risk-Sensitive RL for Alleviating Exploration Dilemmas in Large Language Models** — `Core` · [arXiv:2509.24261](https://arxiv.org/abs/2509.24261)
  - Addresses bimodal distribution problems by shifting from sub-optimal peaks to optimal peaks. A risk-sensitive parameter controls the model's tendency to prioritize hard problems.
- **FlowRL: Matching Reward Distributions for LLM Reasoning** — `Core` · [arXiv:2509.15207](https://arxiv.org/abs/2509.15207)
- **Spectral Bellman Method: Unifying Representation and Exploration in RL** — `Core` · [arXiv:2507.13181](https://arxiv.org/abs/2507.13181)
- **Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning** — `Context` · [arXiv:2505.20561](https://arxiv.org/abs/2505.20561)
  - Extends beyond the Markovian assumption by incorporating reflective exploration through a Bayes-adaptive framework, enabling the model to learn from past exploration attempts.
- **BAPO: Stabilizing Off-Policy Reinforcement Learning for LLMs via Balanced Policy Optimization with Adaptive Clipping** — `Core` · [arXiv:2510.18927](https://arxiv.org/abs/2510.18927)
- **KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning** — `Core` · [arXiv:2506.02208](https://arxiv.org/abs/2506.02208)
- **RLVR without Ineffective Samples: Group Prioritized Off-Policy Optimization for LLM Reasoning** — `Core` · [arXiv:2606.01281](https://arxiv.org/abs/2606.01281)
- **Adaptive Negative Reinforcement for LLM Reasoning: Dynamically Balancing Correction and Diversity in RLVR** — `Core` · [arXiv:2605.07137](https://arxiv.org/abs/2605.07137)
- **Listwise Policy Optimization: Group-based RLVR as Target-Projection on the LLM Response Simplex** — `Core` · [arXiv:2605.06139](https://arxiv.org/abs/2605.06139)
- **Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs** — `Core` · [arXiv:2505.18573](https://arxiv.org/abs/2505.18573)
- **Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning** — `Core` · [arXiv:2606.10346](https://arxiv.org/abs/2606.10346)
- **BandPO: Bridging Trust Regions and Ratio Clipping via Probability-Aware Bounds for LLM Reinforcement Learning** — `Core` · [arXiv:2603.04918](https://arxiv.org/abs/2603.04918)
- **Rebellious Student: Reversing Teacher Signals for Reasoning Exploration with Self-Distilled RLVR** — `Core` · [arXiv:2605.10781](https://arxiv.org/abs/2605.10781)
- **Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation** — `Core` · [arXiv:2605.16826](https://arxiv.org/abs/2605.16826)
- **ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection** — `Core` · [arXiv:2602.21887](https://arxiv.org/abs/2602.21887)
- **Group-Aware Reinforcement Learning for Output Diversity in Large Language Models** — `Core` · [arXiv:2511.12596](https://arxiv.org/abs/2511.12596)
- **Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning** — `Core` · [arXiv:2606.06673](https://arxiv.org/abs/2606.06673)
- **Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning** — `Core` · [arXiv:2607.07178](https://arxiv.org/abs/2607.07178)
- **UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma** — `Core` · [arXiv:2607.06987](https://arxiv.org/abs/2607.06987)
- **DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training** — `Core` · [arXiv:2606.30345](https://arxiv.org/abs/2606.30345)
- **Beyond Trajectory Imitation: Strategy-Guided Policy Optimization for LLM Reasoning** — `Core` · [arXiv:2606.24064](https://arxiv.org/abs/2606.24064)
- **Learning to Explore: Scaling Agentic Reasoning via Exploration-Aware Policy Optimization** — `Core` · [arXiv:2605.08978](https://arxiv.org/abs/2605.08978)
- **Bridging SFT and RL: Dynamic Policy Optimization for Robust Reasoning** — `Core` · [arXiv:2604.08926](https://arxiv.org/abs/2604.08926)
- **Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning** — `Core` · [arXiv:2602.21420](https://arxiv.org/abs/2602.21420)
- **Beyond Stochastic Exploration: What Makes Training Data Valuable for Agentic Search** — `Core` · [arXiv:2604.08124](https://arxiv.org/abs/2604.08124)
- **Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning** — `Core` · [arXiv:2605.27765](https://arxiv.org/abs/2605.27765)

## 5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise)

- **On the Role of Temperature Sampling in Test-Time Scaling** — `Core` · [arXiv:2510.02611v1](https://arxiv.org/abs/2510.02611v1)
- **Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening** — `Core` · [arXiv:2601.21590v1](https://arxiv.org/abs/2601.21590v1)
- **Thoughts-as-Planning: Latent World Models for Chain-of-Thoughts Optimization via Reinforcement Planning** — `Context` · [arXiv:2605.28842](https://arxiv.org/abs/2605.28842)
- **Novelty-based Tree-of-Thought Search for LLM Reasoning and Planning** — `Context` · [arXiv:2605.06040](https://arxiv.org/abs/2605.06040)
- **LLM-Driven Intrinsic Motivation for Sparse Reward Reinforcement Learning** — `Core` · [arXiv:2508.18420](https://arxiv.org/abs/2508.18420)
- **From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism** — `Core` · [arXiv:2604.04648](https://arxiv.org/abs/2604.04648)
- **Global Convergence of Policy Gradient for Entropy Regularized Linear-Quadratic Control with multiplicative noise** — `Context` · [arXiv:2510.02896](https://arxiv.org/abs/2510.02896)
- **Arbitrary Entropy Policy Optimization Breaks The Exploration Bottleneck of Reinforcement Learning** — `Context` · [arXiv:2510.08141](https://arxiv.org/abs/2510.08141)
- **Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning** — `Context` · [arXiv:2510.04072](https://arxiv.org/abs/2510.04072)
  - reinforcement learning (rl) has become central to enhancing reasoning in large language models (llms).

## 5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise) / 5.1 Entropy-Based Methods

- **Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning** — `Core` · [arXiv:2605.27954](https://arxiv.org/abs/2605.27954)
- **Taming the Thinker: Conditional Entropy Shaping for Adaptive LLM Reasoning** — `Core` · [arXiv:2605.19358](https://arxiv.org/abs/2605.19358)
- **OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning** — `Core` · [arXiv:2604.18530](https://arxiv.org/abs/2604.18530)
- **Embarrassingly Simple Self-Distillation Improves Code Generation** — `Core` · [arXiv:2604.01193](https://arxiv.org/abs/2604.01193)
  - Fine-grained temperature tuning to balance exploration and exploitation.
- **SED-SFT: Selectively Encouraging Diversity in Supervised Fine-Tuning** — `Core` · [arXiv:2602.07464](https://arxiv.org/abs/2602.07464)
- **The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning** — `Core` · [arXiv:2505.15134](https://arxiv.org/abs/2505.15134)
- **Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models** — `Core` · [arXiv:2512.15347](https://arxiv.org/abs/2512.15347)

## 5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise) / 5.2 Entropy- & Probability-Based Methods

- **Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization** — `Core` · [arXiv:2605.21801](https://arxiv.org/abs/2605.21801)
- **Entropy Polarity in Reinforcement Fine-Tuning: Direction, Asymmetry, and Control** — `Core` · [arXiv:2605.11775](https://arxiv.org/abs/2605.11775)
  - Analyzes entropy polarity dynamics during RL fine-tuning and proposes directional entropy control.
- **Prototype Entropy Alignment: Reinforcing Structured Uncertainty in LLM Reasoning** — `Core` · [arXiv:2601.17275](https://arxiv.org/abs/2601.17275)
  - Aligns prototype entropy to maintain structured uncertainty during RL reasoning training.
- **Revisiting Entropy in Reinforcement Learning for Large Reasoning Models** — `Core` · [arXiv:2511.05993](https://arxiv.org/abs/2511.05993)
- **Decomposing the Entropy-Performance Exchange: The Missing Keys to Unlocking Effective Reinforcement Learning** — `Core` · [arXiv:2508.02260](https://arxiv.org/abs/2508.02260)
- **Entropy Is Not Enough: Unlocking Effective Reinforcement Learning for Visual Reasoning via Vision-Anchored Token Selection** — `Core` · [arXiv:2606.03937](https://arxiv.org/abs/2606.03937)
- **Calibrating LLMs with Semantic-level Reward** — `Core` · [arXiv:2605.15588](https://arxiv.org/abs/2605.15588)

## 5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise) / 5.3 Curiosity & Intrinsic Motivation

- **Planning to Explore: Curiosity-Driven Planning for LLM Test Generation** — `Context` · [arXiv:2604.05159](https://arxiv.org/abs/2604.05159)
- **In-Context Curiosity: Distilling Exploration for Decision-Pretrained Transformers on Bandit Tasks** — `Context` · [arXiv:2510.00347](https://arxiv.org/abs/2510.00347)
- **Curiosity-Driven Reinforcement Learning from Human Feedback** — `Context` · [arXiv:2501.11463](https://arxiv.org/abs/2501.11463)
- **HAMMER: Hamiltonian Curiosity Augmented Large Language Model Reinforcement** — `Context` · [arXiv:2509.25240](https://arxiv.org/abs/2509.25240)
- **WorldLLM: Improving LLMs' world modeling using curiosity-driven theory-making** — `Context` · [arXiv:2506.06725](https://arxiv.org/abs/2506.06725)
- **Large Language Models Explore by Latent Distilling** — `Core` · [arXiv:2604.24927](https://arxiv.org/abs/2604.24927)
- **Verifier-Free RL for LLMs via Intrinsic Gradient-Norm Reward** — `Context` · [arXiv:2605.09920](https://arxiv.org/abs/2605.09920)

## 5. Semantic-Ignorant Exploration (Entropy / Temperature / Noise) / 5.4 Noise-Based Perturbation

- **From Noise to Diversity: Random Embedding Injection in LLM Reasoning** — `Context` · [arXiv:2605.11936](https://arxiv.org/abs/2605.11936)
- **Why Did Apple Fall: Evaluating Curiosity in Large Language Models** — `Context` · [arXiv:2510.20635](https://arxiv.org/abs/2510.20635)
- **Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration** — `Context` · [arXiv:2605.05566](https://arxiv.org/abs/2605.05566)
- **CuES: A Curiosity-driven and Environment-grounded Synthesis Framework for Agentic RL** — `Context` · [arXiv:2512.01311](https://arxiv.org/abs/2512.01311)
- **HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment** — `Core` · [arXiv:2604.17928](https://arxiv.org/abs/2604.17928)
- **Flexible Entropy Control in RLVR with a Gradient-Preserving Perspective** — `Core` · [arXiv:2602.09782](https://arxiv.org/abs/2602.09782)
- **Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages** — `Core` · [arXiv:2603.12554](https://arxiv.org/abs/2603.12554)
- **From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty** — `Core` · [arXiv:2603.06317](https://arxiv.org/abs/2603.06317)

## 6. Exploration in Specific Scenarios

- **Expanding LLM Agent Boundaries with Strategy-Guided Exploration** — `Core` · [arXiv:2603.02045v1](https://arxiv.org/abs/2603.02045v1)
- **CALM: Curiosity-Driven Auditing for Large Language Models** — `Core` · [arXiv:2501.02997v1](https://arxiv.org/abs/2501.02997v1)
- **"I've Seen How This Goes": Characterizing Diversity via Progressive Conditional Surprise** — `Core` · [arXiv:2606.01811v1](https://arxiv.org/abs/2606.01811v1)
- **LLM-ACES: Closed-Loop Discovery of Dynamical Systems with LLM-Guided Adaptive Search** — `Core` · [arXiv:2606.25039](https://arxiv.org/abs/2606.25039)
- **OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models** — `Core` · [arXiv:2606.16774](https://arxiv.org/abs/2606.16774)
- **MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation** — `Core` · [arXiv:2603.03680](https://arxiv.org/abs/2603.03680)
- **Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling** — `Core` · [arXiv:2606.07040](https://arxiv.org/abs/2606.07040)
- **Plan-MCTS: Plan Exploration for Action Exploitation in Web Navigation** — `Context` · [arXiv:2602.14083](https://arxiv.org/abs/2602.14083)
- **RTLSeek: Boosting the LLM-Based RTL Generation with Multi-Stage Diversity-Oriented Reinforcement Learning** — `Core` · [arXiv:2603.27630](https://arxiv.org/abs/2603.27630)
- **SPADER: Step-wise Peer Advantage with Diversity-Aware Exploration Rewards for Multi-Answer Question Answering** — `Core` · [arXiv:2606.00593](https://arxiv.org/abs/2606.00593)
- **Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning** — `Core` · [arXiv:2601.09667](https://arxiv.org/abs/2601.09667)
- **From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation** — `Core` · [arXiv:2601.18533](https://arxiv.org/abs/2601.18533)
- **Flow-of-Options: Diversified and Improved LLM Reasoning by Thinking Through Options** — `Core` · [arXiv:2502.12929](https://arxiv.org/abs/2502.12929)

## 6. Exploration in Specific Scenarios / 6.1 RLVR (Math / Code)

- **T²PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning** — `Core` · [arXiv:2605.02178](https://arxiv.org/abs/2605.02178)
- **SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs** — `Core` · [arXiv:2605.18864](https://arxiv.org/abs/2605.18864)
- **Look Before You Leap: Autonomous Exploration for LLM Agents** — `Core` · [arXiv:2605.16143](https://arxiv.org/abs/2605.16143)
- **Exploration-Driven Optimization for Test-Time Large Language Model Reasoning** — `Core` · [arXiv:2605.09853](https://arxiv.org/abs/2605.09853)
  - Bridges test-time exploration with training-time RL to improve LLM reasoning.
- **Too Correct to Learn: Reinforcement Learning on Saturated Reasoning Data** — `Adjacent` · [arXiv:2604.18493](https://arxiv.org/abs/2604.18493)
  - Identifies the 'too correct' problem in RL training data — when data is already high-quality, there's little room for exploration to discover new strategies.
- **Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems** — `Core` · [arXiv:2604.04767](https://arxiv.org/abs/2604.04767)
  - Reformulates hard problems adaptively to create stepping stones for exploration during RL training.
- **Bootstrapping Exploration with Group-Level Natural Language Feedback in Reinforcement Learning** — `Core` · [arXiv:2603.04597](https://arxiv.org/abs/2603.04597)
  - Uses natural language feedback to bootstrap exploration in sparse-reward RLVR scenarios.
- **Asymmetric Proximal Policy Optimization: mini-critics boost LLM reasoning** — `Core` · [arXiv:2510.01656](https://arxiv.org/abs/2510.01656)
  - most recent rl for llms (rl4llm) methods avoid explicit critics, replacing them with average advantage baselines.
- **Revisiting Entropy Regularization: Adaptive Coefficient Unlocks Its Potential for LLM Reinforcement Learning** — `Core` · [arXiv:2510.10959](https://arxiv.org/abs/2510.10959)
- **Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning** — `Core` · [arXiv:2510.23038](https://arxiv.org/abs/2510.23038)
  - large language models (llms) are widely used as judges to evaluate response quality, providing a scalable alternative to human evaluation.
- **Do Not Step Into the Same River Twice: Learning to Reason from Trial and Error** — `Core` · [arXiv:2510.26109](https://arxiv.org/abs/2510.26109)
- **SCHEDULING YOUR LLM REINFORCEMENT LEARNING WITH REASONING TREES** — `Core` · [arXiv:2510.24832](https://arxiv.org/abs/2510.24832)
- **CLPO: Curriculum Learning meets Policy Optimization for LLM Reasoning** — `Core` · [arXiv:2509.25004](https://arxiv.org/abs/2509.25004)
- **EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning** — `Core` · [arXiv:2509.22576](https://arxiv.org/abs/2509.22576)
- **Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning** — `Core` · [arXiv:2509.25300](https://arxiv.org/abs/2509.25300)
- **Know When to Explore: Difficulty-Aware Certainty as a Guide for LLM Reinforcement Learning** — `Core` · [arXiv:2509.00125](https://arxiv.org/abs/2509.00125)
  - Uses model certainty to dynamically adjust exploration intensity based on problem difficulty.
- **RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning** — `Core` · [arXiv:2507.07451](https://arxiv.org/abs/2507.07451)
- **Consistent Paths Lead to Truth: Self-Rewarding Reinforcement Learning for LLM Reasoning** — `Core` · [arXiv:2506.08745](https://arxiv.org/abs/2506.08745)
- **The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning** — `Core` · [arXiv:2506.01347](https://arxiv.org/abs/2506.01347)
- **Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts** — `Core` · [arXiv:2506.02177](https://arxiv.org/abs/2506.02177)
  - reinforcement learning, such as ppo and grpo, has powered recent breakthroughs in llm reasoning.
- **Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective** — `Core` · [arXiv:2506.14965](https://arxiv.org/abs/2506.14965)
- **Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning** — `Core` · [arXiv:2506.06632](https://arxiv.org/abs/2506.06632)
  - we aim to improve the reasoning capabilities of language models via reinforcement learning (rl).
- **R-Search: Empowering LLM Reasoning with Search via Multi-Reward Reinforcement Learning** — `Core` · [arXiv:2506.04185](https://arxiv.org/abs/2506.04185)
  - large language models (llms) have notably progressed in multi-step and long-chain reasoning.
- **SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning** — `Core` · [arXiv:2506.01713](https://arxiv.org/abs/2506.01713)
- **Not All Thoughts are Generated Equal: Efficient LLM Reasoning via Multi-Turn Reinforcement Learning** — `Core` · [arXiv:2505.11827](https://arxiv.org/abs/2505.11827)
  - compressing long chain-of-thought (cot) from large language models (llms) is an emerging strategy to improve the reasoning efficiency of llms.
- **Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning** — `Core` · [arXiv:2505.14216](https://arxiv.org/abs/2505.14216)
- **DGRO: Enhancing LLM Reasoning via Exploration-Exploitation Control and Reward Variance Management** — `Core` · [arXiv:2505.12951](https://arxiv.org/abs/2505.12951)
- **Beyond Correctness: Confidence-Aware Reward Modeling for Enhancing Large Language Model Reasoning** — `Core` · [arXiv:2511.07483](https://arxiv.org/abs/2511.07483)
- **Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning** — `Adjacent` · [arXiv:2606.29985](https://arxiv.org/abs/2606.29985)
- **MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting** — `Core` · [arXiv:2601.09085](https://arxiv.org/abs/2601.09085)

## 6. Exploration in Specific Scenarios / 6.3 Creative Generation & Open-Ended Tasks

- **Beyond Accuracy: Evaluating Strategy Diversity in LLM Mathematical Reasoning** — `Core` · [arXiv:2605.09292](https://arxiv.org/abs/2605.09292)
- **Policy Split: Incentivizing Dual-Mode Exploration in LLM Reinforcement with Dual-Mode Entropy Regularization** — `Adjacent` · [arXiv:2604.11510](https://arxiv.org/abs/2604.11510)
- **Instructing LLMs to Negotiate using Reinforcement Learning with Verifiable Rewards** — `Core` · [arXiv:2604.09855](https://arxiv.org/abs/2604.09855)
- **cMALC-D: Contextual Multi-Agent LLM-Guided Curriculum Learning with Diversity-Based Context Blending** — `Core` · [arXiv:2508.20818](https://arxiv.org/abs/2508.20818)
- **SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards** — `Core` · [arXiv:2602.21158](https://arxiv.org/abs/2602.21158)
- **Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization** — `Core` · [arXiv:2602.23008](https://arxiv.org/abs/2602.23008)

## 7. The Escape Debate: Can RL Surpass Base Model?

- **What are Key Factors for Updates in RL for LLM Reasoning?** — `Adjacent` · [arXiv:2606.22570](https://arxiv.org/abs/2606.22570)
- **Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning** — `Adjacent` · [arXiv:2511.12344](https://arxiv.org/abs/2511.12344)
- **Exploration Hacking: Can LLMs Learn to Resist RL Training?** — `Adjacent` · [arXiv:2604.28182](https://arxiv.org/abs/2604.28182)
- **On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation** — `Adjacent` · [arXiv:2603.22117](https://arxiv.org/abs/2603.22117)
- **Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward** — `Adjacent` · [arXiv:2512.16912](https://arxiv.org/abs/2512.16912)
  - Systematic analysis of exploration-exploitation trade-off in RLVR from the perspective of clipping, entropy, and reward dynamics.
- **The Debate on RLVR Reasoning Capability Boundary: Shrinkage, Expansion, or Both? A Two-Stage Dynamic View** — `Adjacent` · [arXiv:2510.04028](https://arxiv.org/abs/2510.04028)
  - Two-stage dynamic model showing RLVR can both shrink and expand capability boundaries depending on training phase.
- **Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis** — `Adjacent` · [arXiv:2604.14877](https://arxiv.org/abs/2604.14877)
- **Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training** — `Adjacent` · [arXiv:2602.21189](https://arxiv.org/abs/2602.21189)
- **Understanding Diversity Collapse in RLVR via the Lens of Overtraining** — `Adjacent` · [arXiv:2606.15455](https://arxiv.org/abs/2606.15455)
- **Unlocking Reasoning Capabilities in LLMs via Reinforcement Learning Exploration** — `Adjacent` · [arXiv:2510.03865](https://arxiv.org/abs/2510.03865)
- **LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents** — `Adjacent` · [arXiv:2606.18388](https://arxiv.org/abs/2606.18388)
- **From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space** — `Adjacent` · [arXiv:2604.14142](https://arxiv.org/abs/2604.14142)

## License

This list is licensed under [CC BY 4.0](LICENSE.md).
