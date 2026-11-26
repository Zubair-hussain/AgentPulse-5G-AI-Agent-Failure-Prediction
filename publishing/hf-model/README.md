---
license: mit
library_name: sklearn
pipeline_tag: tabular-classification
datasets:
- __HF_OWNER__/agentpulse-5g
tags:
- ai-agents
- observability
- failure-prediction
- synthetic-data
- logistic-regression
---
# AgentPulse failure predictor
Author: Zubair Hussain | [Portfolio](https://zubairhussain.xyz)

A portable, CPU-only logistic regression trained on 16,000 synthetic telemetry rows. The 2,000-row validation split selects the threshold and the separate 2,000-row test split evaluates the model. See benchmark.json for measured values. No paid API or language-model prompt required.

Test ROC-AUC: **0.7652**; F1: **0.5637**; accuracy: **0.719**. Not production validated; synthetic correlations may not transfer. A probability estimate is not a guarantee of failure. Model is JSON, not executable pickle. The Hub's hosted inference widget is not configured for this custom format.

```bash
python predict.py telemetry.json --model logistic.json
```
Dataset: [AgentPulse-5G](https://huggingface.co/datasets/__HF_OWNER__/agentpulse-5g) (after publication). The JSON model and accompanying schema/predictor can run locally with standard Python. MIT license.
