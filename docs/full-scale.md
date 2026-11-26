# Generate the approximately 5 GB edition
Use Python 3.11–3.13, at least 12 GB free for generation and preferably 25 GB for staging copies. The ZIP contains the tested 20,000-row demo, not 5 GB of generated data. The size target is decimal 5,000,000,000 bytes before ZIP compression. Calibration writes a pilot shard and estimates rows per shard; actual total may differ. Choose a fresh folder every run.

```bash
pip install -r requirements-publish.txt
python -m agentpulse.generate --out data/full-5gb --shards 1000 --target-gb 5 --format parquet
python -m tools.validate_data data/full-5gb
python -m agentpulse.stream_train --data data/full-5gb --out models/full-sgd.json --report reports/full-sgd.json
```
CSV alternative: `--format csv`. Parquet requires pyarrow; it could not be installed in the offline build environment and this path has not been run here. Full-scale output is untested. Do not confuse the demo scores with the full-scale results. Run validation before release. For a full dataset with real one-file commits, create a dedicated data branch/repository and configure Git LFS for CSV/Parquet first, then add `--git-commit` to generation. Each generated shard and manifest receives one actual commit; do not push 5 GB of raw Git blobs to GitHub. 1,000 shards plus manifest produce 1,001 new commits. Prefer platform-native large-file upload for public datasets. Do not manufacture empty commits or imply prolonged human activity. Git LFS and cloud platform limits must be checked before pushing.
