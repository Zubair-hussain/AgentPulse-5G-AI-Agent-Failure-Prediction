# Initial issue drafts (not filed remotely)
1. **Validate full 5 GB Parquet release** — Generate, hash and validate all shards; record measured size and viewer status. Acceptance: reproducible manifest and split checks.
2. **Evaluate real-world transfer** — Design opt-in anonymized telemetry evaluation. Acceptance: rights documented, separate real test metrics, limitations.
3. **Probability calibration** — Reliability diagram, calibration error and confidence intervals across seeds. Acceptance: report on untouched test split.
4. **Compare fault-localization features** — Explore additional simulated signals, no leakage. Acceptance: ablation table and tests.
5. **Hugging Face Space smoke test** — Deploy privately and verify health, predict and invalid input. Acceptance: recorded status and release hash.
6. **Kaggle notebook reproducibility** — Run offline notebook against public release. Acceptance: output metrics and runtime.
7. **Publish dataset and model version linkage** — Add verified links, release tags and citation. Acceptance: no broken links.
8. **Add drift monitoring example** — Simulated shifts with reported false alarm rates. Acceptance: standalone example and tests.
