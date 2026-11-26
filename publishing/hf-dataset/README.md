---
license: mit
language:
- en
task_categories:
- tabular-classification
size_categories:
- 10K<n<100K
tags:
- synthetic-data
- ai-agents
- observability
- failure-prediction
- reliability
- mlops
- llmops
pretty_name: AgentPulse-5G Synthetic Agent Telemetry
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.__FORMAT__
  - split: validation
    path: data/validation-*.__FORMAT__
  - split: test
    path: data/test-*.__FORMAT__
---
# Can telemetry predict when an AI agent will fail?

**AgentPulse-5G** is an open, reproducible synthetic benchmark for AI agent failure prediction. Explore **20,000 simulated runs**, **16 numeric predictors**, and a portable CPU model, then try changing the telemetry in the live demo.

[Try the live demo](https://huggingface.co/spaces/__HF_OWNER__/agentpulse-risk-demo) | [Dataset](https://huggingface.co/datasets/__HF_OWNER__/agentpulse-5g) | [Model](https://huggingface.co/__HF_OWNER__/agentpulse-failure-predictor) | [Code and issues](https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction)

<video controls preload="metadata" src="assets/intro-saas.mp4" poster="assets/cover.png"></video>

[Watch or download the 30-second trailer](assets/intro-saas.mp4). The dashboard in the trailer is illustrative; the benchmark below is measured on synthetic data.

## What is in this release?

| Split | Rows | Purpose |
|---|---:|---|
| Train | 16,000 | Fit model and scaler |
| Validation | 2,000 | Choose decision threshold |
| Test | 2,000 | Held-out evaluation |

This upload contains **__ROWS__ rows** across 20 CSV shards, totaling **__BYTES__ bytes of data files**. The name refers to a generator targeting a separate 5 GB edition; this upload is the demo edition.

Each record contains run ID, environment ID, split, 16 numerical telemetry features, and a binary `failed` outcome. Features include retries, tool error ratio, context use, queue time, resource use, and rate limiting. Environment IDs are disjoint across splits. See the [data dictionary](data-dictionary.md) and [integrity manifest](manifest.json).

## Load in Python

```bash
pip install datasets
```

```python
from datasets import load_dataset

runs = load_dataset("__HF_OWNER__/agentpulse-5g")
print(runs)
print(runs["train"][0])

# For sequential access without downloading the full dataset first:
stream = load_dataset("__HF_OWNER__/agentpulse-5g", streaming=True)
print(next(iter(stream["train"])))
```

## Measured baseline

![Held-out baseline comparison](assets/benchmark.svg)

The shipped logistic regression scores **0.7652 ROC-AUC**, **0.5859 PR-AUC**, and **0.5637 F1** on 2,000 held-out synthetic runs. Validation selects the F1 threshold. These are synthetic benchmark results, not real-world accuracy claims.

## Generation and limitations

An original seeded stochastic simulator generates pre-outcome telemetry and failure labels. It uses no proprietary logs, prompts, user identities, or provider-specific traces. The source repository includes generation and retraining commands, leakage tests, checksums, and split checks.

Synthetic correlations can differ from real deployments. This dataset is useful for reproducibility, evaluation tooling, and research prototypes; operational decisions require external validation. Calibration, confidence intervals, and transfer to real agent workloads remain open research tasks.

## Reproduce, contribute, and cite

Created by **Zubair Hussain** | [Portfolio](https://zubairhussain.xyz). Original code and synthetic data are MIT licensed. `source-revision.json` records the GitHub source commit and dataset shard hashes; Hugging Face commits record actual publication changes.

[Report a problem or propose an experiment](https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction/issues). Useful next experiments include probability calibration, feature ablations, and real-world transfer with appropriately sourced telemetry. If this helps your work, a like or a citation helps others discover it.

```bibtex
@software{hussain2026agentpulse,
  author = {Hussain, Zubair},
  title = {AgentPulse-5G: AI Agent Failure Prediction},
  year = {2026},
  url = {https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction}
}
```
