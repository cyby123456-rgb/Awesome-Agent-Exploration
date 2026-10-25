# Research Directions

## Memory x Exploration

Memory conditions an exploration policy by changing which experience is
available for action selection, what should be revisited, and what remains
unknown. It is a cross-cutting lens across agentic interaction and policy
learning, not a sixth primary category.

| Direction | Current bottleneck | Research opportunity |
|---|---|---|
| **Memory-guided exploration** | Retrieval can be stale, overly similar, or detached from the agent's current uncertainty and environment state. | Learn when to recall, when to verify, and when to explore a new state instead of following remembered trajectories. |
| **Exploration-driven memory** | Most systems passively append experiences, retaining redundant traces and outdated rules. | Treat write, merge, compression, and forgetting as utility-aware decisions that preserve experiences which expand future coverage. |
| **Failure memory and recovery** | Failure traces are often stored as unstructured text and can transfer brittle or incorrect lessons. | Learn causal, context-sensitive failure representations that support safe backtracking without suppressing useful risk-taking. |
| **Memory-augmented training** | Replayed experience is correlated, non-stationary, and may reinforce reward-hacked behavior. | Optimize which trajectories to retain and replay so memory improves policy learning, task diversity, and long-horizon generalization. |

Related catalog paths: [Knowledge & Memory-Guided Exploration](../README.md#category-3-knowledge-memory) · [Planning & Interactive Search](../README.md#category-3-planning-interaction) · [Memory-Augmented Agent Training](../README.md#category-4-knowledge-memory) · [Replay, Population & Self-Improvement](../README.md#category-2-replay-population).

## October evidence to compare

[DAEDALUS](https://arxiv.org/abs/2610.08048) constructs procedural memory from
self-generated practice, solver failures, and repeated successful retries.
[RSIAgent](https://arxiv.org/abs/2609.15364) uses broad-then-deep environment
exploration and a verifier to retain reusable procedures and constraints. Both
freeze the resulting memory for evaluation. Compare exploration cost, task
conditioning, verification quality, and cross-task reuse before treating
either as evidence for continual online memory improvement.

[MemAct](https://arxiv.org/abs/2610.17640) provides a complementary loop: choose
between historical evidence, a new view, and stopping to answer. It motivates
cost-aware tests of when memory reduces redundant actions and when fresh
observations are more informative than retrieval.

[Inquiry Learning](https://arxiv.org/abs/2610.21604) evaluates variable
manipulation, observations, and hypothesis changes. Its process annotations
suggest an evaluation lens for memory systems: measure whether retained rules
improve later experimental choices and hypothesis revision, alongside final
task success. This extension is a research proposal, not a result established
by the cited paper.
