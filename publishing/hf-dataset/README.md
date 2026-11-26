---
license: mit
task_categories:
- tabular-classification
tags:
- synthetic-data
- ai-agents
- observability
- failure-prediction
- reliability
- mlops
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
# AgentPulse-5G | AI Agent Reliability Dataset
By Zubair Hussain · [Portfolio](https://zubairhussain.xyz)

**Synthetic research data, not production logs.** This release contains __ROWS__ rows and __BYTES__ bytes of data files. Each row describes a simulated agent run before its binary failure outcome. The 5G name indicates the target edition, not the size of every release.

## Data and use
16 numeric telemetry predictors, run ID, environment ID, split, failed (0 or 1). Environment cohorts are disjoint; validation selects the decision threshold and test is held out. Data was generated from an original stochastic simulator, not scraped from proprietary sources. No private logs, prompts, user identities or provider-specific traces.

```python
from datasets import load_dataset
ds = load_dataset("__HF_OWNER__/agentpulse-5g", streaming=True)
print(next(iter(ds["train"])))
```
See [data dictionary](data-dictionary.md), manifest and [model repository](https://huggingface.co/__HF_OWNER__/agentpulse-failure-predictor) after publication. The included benchmark concerns the 20,000-row demo only. Real-world validity is not established. MIT license; cite Zubair Hussain, AgentPulse-5G, 2026.
