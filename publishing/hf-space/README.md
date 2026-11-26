---
title: AgentPulse - AI Agent Failure Risk
emoji: "📈"
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
license: mit
short_description: Score synthetic agent telemetry with a local CPU model.
tags:
- ai-agents
- failure-prediction
- observability
- synthetic-data
- mlops
models:
- __HF_OWNER__/agentpulse-failure-predictor
datasets:
- __HF_OWNER__/agentpulse-5g
---
# Can you spot an agent failure before it happens?

Change the telemetry fields and click **Score telemetry** to explore a synthetic-trained agent failure-risk model. Try raising `tool_error_ratio`, `rate_limit_ratio`, or `retry_count` and compare the output. No prompts or paid inference APIs are involved.

[Try the live demo](https://huggingface.co/spaces/__HF_OWNER__/agentpulse-risk-demo) | [Dataset](https://huggingface.co/datasets/__HF_OWNER__/agentpulse-5g) | [Model](https://huggingface.co/__HF_OWNER__/agentpulse-failure-predictor) | [Code and issues](https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction)

<video controls preload="metadata" src="assets/intro-saas.mp4" poster="assets/cover.png"></video>

[Watch or download the 30-second trailer](assets/intro-saas.mp4). The dashboard in the trailer is illustrative; the benchmark below is measured on synthetic data.

## What the demo shows

- A standard-library CPU predictor with a fitted logistic regression and validation-selected threshold.
- Sixteen numerical telemetry inputs, including retries, tool errors, resource use, and queue time.
- The measured baseline: **0.7652 ROC-AUC** and **0.5637 F1** on 2,000 held-out synthetic runs.
- FastAPI endpoints: `/health`, `/predict`, and interactive API documentation at `/docs`.

This is a synthetic research demo. The score is not calibrated or validated for real production agents, and the trailer dashboard is illustrative.

## Source, directories, and commits

The original project directories are preserved here: `agentpulse/`, `assets/`, `data/demo/`, `docs/`, `examples/`, `models/`, `notebooks/`, `publishing/`, `reports/`, `tests/`, `tools/`, and collaboration/media source directories. The Space root README provides the Docker configuration. GitHub remains the canonical development repository on `prod_core`; `source-revision.json` pins the source revision used for this upload. Existing GitHub commit history is preserved on GitHub; new Hub changes have their own descriptive commits.

The app listens on port 7860 and runs as a non-root user. It uses the bundled JSON model and FastAPI without external inference calls.

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
