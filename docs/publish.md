# Publishing AgentPulse

GitHub is the canonical development repository; its default branch is `prod_core`.

## Hugging Face packages

- Dataset: https://huggingface.co/datasets/zubairH123/agentpulse-5g
- Portable model: https://huggingface.co/zubairH123/agentpulse-failure-predictor
- Static browser Space: https://huggingface.co/spaces/zubairH123/agentpulse-risk-demo

Stage a fresh snapshot from the repository root:

```bash
python -m tools.stage_release --out release/huggingface-launch --hf-owner zubairH123 --kaggle-owner zubairhussain786
python -m tools.check_release release/huggingface-launch
```

The dataset preserves its CSV shard filenames under `data/`, with explicit split patterns in the card. The model package includes portable weights, schema, example telemetry, and a standard-library inference script. The Space preserves the project directories, including demo data, tests, documentation, and media; its root README supplies static-app metadata. All three packages carry `source-revision.json`, pinning the GitHub commit and dataset checksums, and include the launch trailer and cover.

Hugging Face has its own Git history. Use descriptive messages for actual upload changes; the original history remains on GitHub. Do not fabricate commits, rewrite historical authors, or force-push over remote work.

Authenticate locally with `hf auth login`; never commit tokens. To upload an existing package:

```bash
hf upload zubairH123/agentpulse-5g release/huggingface-launch/hf-dataset --repo-type dataset --commit-message "data: publish reproducible synthetic agent telemetry"
hf upload zubairH123/agentpulse-failure-predictor release/huggingface-launch/hf-model --repo-type model --commit-message "model: publish portable CPU failure predictor"
hf upload zubairH123/agentpulse-risk-demo release/huggingface-launch/hf-space --repo-type space --commit-message "feat: deploy AgentPulse risk demo with project sources"
```

Before updating an existing Hub repository, inspect its current revision and files. Preserve remote changes and do not delete unrelated files. Verify the public cards, dataset viewer splits, downloaded model inference, Space asset loading, browser/Python prediction parity, and invalid-input handling after upload. The Space uses free static hosting; Docker/Gradio compute Spaces currently require a paid plan. No paid upgrade was requested.

## Checks and release scope

GitHub Actions validates Python 3.11-3.13, dataset integrity, inference, tests, and offline publishing packages. Hugging Face independently serves the static Space. The preserved Dockerfile remains available for local API deployment. Dataset viewer preparation and Space startup may take time after upload.

This release is the 20,000-row synthetic demo. The 5 GB edition must be generated and validated separately. Do not label the demo as a 5 GB upload or present synthetic results as real-world performance.

## Optional platform publishing

Kaggle dataset and notebook packages are staged for review but are not uploaded by this workflow. Use your verified Kaggle account and review metadata before publishing. Hugging Face publication does not authorize posting announcements to external social accounts.

## Published collection

https://huggingface.co/collections/zubairH123/agentpulse-ai-agent-reliability-6b0831bec625b7f351986bd8

Publication commits and verification are recorded in [the release report](huggingface-release.md).
