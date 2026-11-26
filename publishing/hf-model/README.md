---
license: mit
language:
- en
library_name: sklearn
pipeline_tag: tabular-classification
datasets:
- __HF_OWNER__/agentpulse-5g
metrics:
- roc_auc
- f1
- accuracy
tags:
- ai-agents
- observability
- failure-prediction
- synthetic-data
- logistic-regression
- cpu
- mlops
model-index:
- name: AgentPulse portable logistic regression
  results:
  - task:
      type: tabular-classification
      name: Agent failure prediction
    dataset:
      type: __HF_OWNER__/agentpulse-5g
      name: AgentPulse-5G synthetic demo
      split: test
    metrics:
    - type: roc_auc
      name: ROC-AUC
      value: 0.7652
    - type: f1
      name: F1
      value: 0.5637
    - type: accuracy
      name: Accuracy
      value: 0.7190
---
# AgentPulse: local failure-risk scoring, no prompts required

A small **CPU-only logistic regression** that maps 16 numerical agent telemetry signals to a failure-risk estimate. The JSON weights, scaler, schema, example, and standard-library predictor are included. Runtime inference needs no API key, language model, scikit-learn installation, or executable pickle.

[Try the live demo](https://huggingface.co/spaces/__HF_OWNER__/agentpulse-risk-demo) | [Dataset](https://huggingface.co/datasets/__HF_OWNER__/agentpulse-5g) | [Model](https://huggingface.co/__HF_OWNER__/agentpulse-failure-predictor) | [Code and issues](https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction)

<video controls preload="metadata" src="assets/intro-saas.mp4" poster="assets/cover.png"></video>

[Watch or download the 30-second trailer](assets/intro-saas.mp4). The dashboard in the trailer is illustrative; the benchmark below is measured on synthetic data.

## Try it locally

Download the repository files, then run from that directory:

```bash
python predict.py telemetry.json --model logistic.json
```

Expected risk for the supplied example: approximately **0.148168**, below the validation-selected threshold of **0.30**.

Or download the small inference bundle with the Hub client:

```python
from huggingface_hub import snapshot_download
import subprocess
import sys

folder = snapshot_download(
    repo_id="__HF_OWNER__/agentpulse-failure-predictor",
    allow_patterns=["predict.py", "schema.py", "logistic.json", "telemetry.json"],
)
subprocess.run(
    [sys.executable, "predict.py", "telemetry.json", "--model", "logistic.json"],
    cwd=folder, check=True,
)
```

## Measured held-out results

![Baseline benchmark](assets/benchmark.svg)

| Metric | Logistic regression |
|---|---:|
| ROC-AUC | 0.7652 |
| PR-AUC | 0.5859 |
| F1 | 0.5637 |
| Accuracy | 0.7190 |
| Recall | 0.6436 |

Training uses 16,000 synthetic runs. Validation uses 2,000 independent runs to select the threshold; test uses another 2,000 runs from disjoint environment IDs. See [benchmark.json](benchmark.json) for the full three-model comparison. The GitHub project includes the training implementation and pinned dependencies.

## Intended use and limitations

Use for synthetic reliability experiments, local inference examples, and reproducible baselines. The output is a model estimate, not a guaranteed future failure. Synthetic signals may not transfer to real agents; probability calibration and external validation remain open.

Weights are exported from scikit-learn to a custom portable JSON format. This repository does not configure the Hub's hosted inference widget; use the linked static Space for interactive scoring.

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
