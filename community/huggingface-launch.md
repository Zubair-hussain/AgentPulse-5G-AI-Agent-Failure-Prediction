# Hugging Face launch copy

## Short announcement

Can telemetry warn us before an AI agent fails?

I built AgentPulse-5G: an open synthetic benchmark with 20,000 runs, 16 telemetry features, a portable CPU predictor, and a live demo. The logistic baseline reaches 0.7652 ROC-AUC on 2,000 held-out synthetic runs. No paid inference API is needed.

Try the demo, raise retries or tool errors, and compare the risk estimate:
https://huggingface.co/spaces/zubairH123/agentpulse-risk-demo

Dataset: https://huggingface.co/datasets/zubairH123/agentpulse-5g
Model: https://huggingface.co/zubairH123/agentpulse-failure-predictor
Code: https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction

This is synthetic research, not production validation. The full 5 GB edition is generated separately. Which real telemetry signals would you test next?

## Suggested demo sequence

1. Play the 30-second trailer.
2. Score the supplied example telemetry.
3. Increase `tool_error_ratio`, `rate_limit_ratio`, and `retry_count`.
4. Compare the risk estimates and explain the synthetic-data limitation.
5. Invite one concrete calibration or transfer experiment through GitHub issues.

This is ready-to-review copy, not an announcement that has already been posted. Share it with relevant communities when their rules permit. Track actual demo visits, dataset downloads, useful feedback, and reproducible experiments. Likes, downloads, or viral reach are not guaranteed.
