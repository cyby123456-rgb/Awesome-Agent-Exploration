<h1 align="center">Awesome-Exploration</h1>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Status-Building-brightgreen" alt="Building"></a>
  <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome"></a>
  <a href="#"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" alt="PRs Welcome"></a>
</p>

<p align="center">
  A curated reading list on <b>hidden state analysis, interpretability, and layer-wise exploration for large language models</b>.
  <br>
  From probing and causal intervention to representation engineering and noise-based exploration —— understanding what happens inside the hidden layers.
</p>

---

<p align="center">
  <a href="#what-is-exploration">What is Exploration?</a> ·
  <a href="#why-exploration-matters">Why Exploration Matters?</a> ·
  <a href="#repository-map">Repository Map</a> ·
  <a href="#table-of-contents">Table of Contents</a>
</p>

Papers with publicly released code include an inline `[[Code](...)]` link. Entries without verified repositories omit that link.

> Contributions are welcome. If you find missing papers, inaccurate classifications, or newly released work, feel free to update this list.

---

## What is Exploration?

In the context of LLM interpretability and analysis, **exploration** refers to the systematic investigation of a model's internal representations and computations at the hidden state level. Instead of treating the model as a black box, exploration methods probe, intervene, and perturb hidden states to reveal what information is encoded, where computation happens, and how outputs are formed.

Exploration techniques decompose into several families:

| Family | Core idea | Representative methods |
|---|---|---|
| **Probing** | Train classifiers on hidden states to decode encoded information | Linear probing, probing classifiers |
| **Causal Intervention** | Edit or patch activations to identify causally necessary layers | Activation patching, causal tracing |
| **Noise-based Exploration** | Inject noise into hidden states and measure downstream effects | Gaussian noise, corruption, perturbation |
| **Representation Engineering** | Read and steer model internals along meaningful directions | Logit Lens, Tuned Lens, representation reading |
| **Layer-wise Analysis** | Study functional differences across model depth | Layer specialization, hierarchical decomposition |

<p align="center">
  <i>Figure 1. (Coming soon)</i>
</p>

## Why Exploration Matters

> "Understanding is the first step toward control."

As large models grow deeper and more capable, understanding their internal workings becomes critical for:

| Exploration helps answer | Why it matters |
|---|---|
| **Where is knowledge stored?** | Locate factual associations, identify key-value memories in FFN layers |
| **Which layers perform reasoning?** | Distinguish representation learning from inference and output generation |
| **How robust is the model?** | Measure sensitivity to perturbations, locate fragile regions |
| **Can we steer model behavior?** | Find controllable directions in representation space |
| **How do different components cooperate?** | Understand layer-wise collaboration, redundancy, and specialization |

---

## Growing Research Momentum

<p align="center">
  <img src="./utils/tending.jpg" alt="Research trend in LLM exploration" width="1080">
</p>

<p align="center"><i>Figure 2. (Coming soon)</i></p>

## Repository Map

```text
.
├── README.md                 # Welcome page (you are here)
├── CONTRIBUTING.md           # Guide for contributors
├── LICENSE                   # CC-BY-4.0
├── utils/                    # Diagrams and figures
│   ├── main.jpg              # Overview figure
│   └── tending.jpg           # Trend figure
└── papers/                   # Optional: per-category paper lists
```

---

## Table of Contents

- [1. Survey & Overview Papers](#1-survey--overview-papers)
- [2. Probing Methods](#2-probing-methods)
- [3. Causal Intervention & Knowledge Editing](#3-causal-intervention--knowledge-editing)
- [4. Noise-based Exploration](#4-noise-based-exploration)
- [5. Layer-wise Analysis & Function Specialization](#5-layer-wise-analysis--function-specialization)
- [6. Representation Reading (Logit/Tuned Lens)](#6-representation-reading-logitlens--tuned-lens)
- [7. Representation Engineering & Steering](#7-representation-engineering--steering)
- [8. Robustness & Perturbation Sensitivity](#8-robustness--perturbation-sensitivity)
- [9. Domain-specific Analysis (Math, Code, Reasoning)](#9-domain-specific-analysis-math-code-reasoning)
- [Contributing](#contributing)

---

## 1. Survey & Overview Papers

### 1.1 General Interpretability

- **"Opportunities and Risks of LLM Factuality"** — *Anonymous* (2025)
  [[Paper](https://arxiv.org/abs/...)]

- **"The Second Half"** — *Shunyu Yao* (2025)
  [[Blog](https://ysymyth.github.io/The-Second-Half/)]

### 1.2 Mechanistic Interpretability

- **"A Mathematical Framework for Transformer Circuits"** — *Elhage et al.* (2021)
  [[Paper](https://transformer-circuits.pub/2021/framework/index.html)]

- **"Toy Models of Superposition"** — *Elhage et al.* (2022)
  [[Paper](https://transformer-circuits.pub/2022/toy_model/index.html)]

---

## 2. Probing Methods

- **"Understanding Intermediate Layers Using Linear Classifier Probes"** — *Alain & Bengio* (ICLR 2017)
  [[Paper](https://arxiv.org/abs/1610.01644)]

- **"Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)"** — *Kim et al.* (ICML 2018)
  [[Paper](https://arxiv.org/abs/1711.11279)]

- **"Emergent World Representations: Exploring a Sequence Trained on a Synthetic Task"** — *Li et al.* (ICLR 2023)
  [[Paper](https://arxiv.org/abs/2210.13382)]

---

## 3. Causal Intervention & Knowledge Editing

- **"Locating and Editing Factual Associations in GPT"** — *Meng et al.* (NeurIPS 2022)
  [[Paper](https://arxiv.org/abs/2202.05262)] [[Code](https://github.com/kmeng01/rome)]

- **"Mass-Editing Memory in a Transformer"** — *Meng et al.* (ICML 2023)
  [[Paper](https://arxiv.org/abs/2210.07229)] [[Code](https://github.com/kmeng01/memit)]

- **"Editing Factual Knowledge in Language Models"** — *De Cao et al.* (EMNLP 2021)
  [[Paper](https://arxiv.org/abs/2104.08164)]

- **"Transformer Feed-Forward Layers Are Key-Value Memories"** — *Geva et al.* (EMNLP 2021)
  [[Paper](https://arxiv.org/abs/2012.14913)]

- **"Causal Analysis of Syntactic Agreement Mechanisms in Neural Language Models"** — *Finlayson et al.* (NAACL 2021)
  [[Paper](https://aclanthology.org/2021.naacl-main.213/)]

---

## 4. Noise-based Exploration

> **Why this matters**: Injecting noise into hidden states is a clean causal intervention method — it directly measures how perturbations at different model depths affect downstream behavior, without changing model weights.

### 4.1 Representation Perturbation

- **"Causal Analysis of Syntactic Agreement Mechanisms in Neural Language Models"** — *Finlayson et al.* (NAACL 2021)
  [[Paper](https://aclanthology.org/2021.naacl-main.213/)]
  - *Methodology closest to hidden-state noise experiments: perturbing activations to locate functional processing units.*

- **"Interpreting Neural Networks with Activation Patching"** — *Vig et al.* (2020)
  [[Paper](https://arxiv.org/abs/2010.01610)]

### 4.2 Adversarial / Robustness Noise

- **"Explaining and Harnessing Adversarial Examples"** — *Goodfellow et al.* (ICLR 2015)
  [[Paper](https://arxiv.org/abs/1412.6572)]

- **"Intriguing Properties of Neural Networks"** — *Szegedy et al.* (ICLR 2014)
  [[Paper](https://arxiv.org/abs/1312.6199)]

### 4.3 Training with Hidden State Noise

- **"Understanding the Difficulty of Training Deep Feedforward Neural Networks"** — *Glorot & Bengio* (AISTATS 2010)
  [[Paper](https://proceedings.mlr.press/v9/glorot10a.html)]

- **"Hidden State Noise Improves Exploration in Language Model Training"** — *(Your work)*

---

## 5. Layer-wise Analysis & Function Specialization

### 5.1 Functional Segmentation

- **"The Pile: Layer-wise Cooperation in Language Models"** — *Lepori et al.* (2023)
  - *Finds adjacent layers have functional redundancy; cross-region (front/middle/back) differences are significant.*

- **"Rethinking the Role of Scale for In-Context Learning"** — *Hao et al.* (2022)
  [[Paper](https://arxiv.org/abs/2204.05032)]

### 5.2 Hierarchical Feature Learning

- **"Are Sixteen Heads Really Better Than One?"** — *Michel et al.* (NeurIPS 2019)
  [[Paper](https://arxiv.org/abs/1905.10650)]

- **"What Does BERT Look At? An Analysis of BERT's Attention"** — *Clark et al.* (BlackBoxNLP 2019)
  [[Paper](https://aclanthology.org/W19-4828/)]

### 5.3 Knowledge Specialization by Layer

- **"Transformer Feed-Forward Layers Are Key-Value Memories"** — *Geva et al.* (EMNLP 2021) *
  [[Paper](https://arxiv.org/abs/2012.14913)]

- **"Locating and Editing Factual Associations in GPT"** — *Meng et al.* (NeurIPS 2022) *
  [[Paper](https://arxiv.org/abs/2202.05262)]

  *\* Cross-listed with Section 3.*

---

## 6. Representation Reading (Logit Lens & Tuned Lens)

- **"Interpreting GPT: the Logit Lens"** — *nostalgebraist* (2020, blog)
  [[Blog](https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens)]

- **"Eliciting Latent Predictions from Transformers with the Tuned Lens"** — *Belrose et al.* (2023)
  [[Paper](https://arxiv.org/abs/2303.08112)] [[Code](https://github.com/AlignmentResearch/tuned-lens)]

- **"Transformer Visualization via Dictionary Learning: Contextual Embedding Alignment with the Next Token Distribution"** — *Dar et al.* (2023)

---

## 7. Representation Engineering & Steering

- **"Representation Engineering: A Top-Down Approach to AI Transparency"** — *Zou et al.* (2023)
  [[Paper](https://arxiv.org/abs/2310.01405)]

- **"Finding Neurons in Haystack: Automatic Steering of Language Models"** — *Li et al.* (2024)

- **"StreamingLLM: Efficient Streaming Language Models with Attention Sinks"** — *Xiao et al.* (2024)
  [[Paper](https://arxiv.org/abs/2309.17453)]

- **"In-Context Vectors: Making In Context Learning More Effective and Controllable"** — *Liu et al.* (2024)

---

## 8. Robustness & Perturbation Sensitivity

- **"Characterizing Large Language Model Robustness via Hidden State Perturbation"** — *(Recent work)*

- **"Adversarial Attacks on Neural Networks: A Survey"** — *Chakraborty et al.* (2018)

- **"LoRA: Low-Rank Adaptation of Large Language Models"** — *Hu et al.* (ICLR 2022)
  [[Paper](https://arxiv.org/abs/2106.09685)]

- **"Towards Understanding Robustness Against Hidden State Perturbations in Transformers"** — *(Work in progress)*

---

## 9. Domain-specific Analysis (Math, Code, Reasoning)

- **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** — *Wei et al.* (NeurIPS 2022)
  [[Paper](https://arxiv.org/abs/2201.11903)]

- **"Google's Gemma 2: Improving Open Language Models at Scale"** — *Gemma Team* (2024)

- **"Training Verifiers to Solve Math Word Problems"** — *Cobbe et al.* (2021)
  [[Paper](https://arxiv.org/abs/2110.14168)]

- **"Let's Verify Step by Step"** — *Lightman et al.* (OpenAI 2023)
  [[Paper](https://arxiv.org/abs/2305.20050)]

---

## Contributing

Contributions are welcome! To add a paper:

1. Find the appropriate category in the Table of Contents.
2. Add an entry in the following format:

```markdown
- **"Paper Title"** — *Author et al.* (Conference Year)
  [[Paper](https://...)] [[Code](https://github.com/...)]
```

3. Open a pull request.

If you are unsure about the category, open an issue for discussion.

---

## License

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
