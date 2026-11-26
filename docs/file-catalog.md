# File catalog and initial Git commit messages
Each tracked file has one initial commit. These are real creation commits in one build session, not fabricated contribution dates. Full-scale generated files are cataloged by their manifest and per-shard commit message.

| File | Description | Commit message |
|---|---|---|
| `.gitattributes` | Git file type handling | `chore: add .gitattributes` |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Issue template for bug_report | `docs: add .github/ISSUE_TEMPLATE/bug_report.md` |
| `.github/ISSUE_TEMPLATE/research.md` | Issue template for research | `docs: add .github/ISSUE_TEMPLATE/research.md` |
| `.github/PULL_REQUEST_TEMPLATE.md` | Pull request review checklist | `docs: add .github/PULL_REQUEST_TEMPLATE.md` |
| `.github/workflows/ci.yml` | GitHub Actions ci workflow | `ci: add .github/workflows/ci.yml` |
| `.github/workflows/release-check.yml` | GitHub Actions release-check workflow | `ci: add .github/workflows/release-check.yml` |
| `.gitignore` | Exclude secrets, caches and full local data | `chore: add .gitignore` |
| `.gitlab-ci.yml` | GitLab CI validation pipeline | `ci: add .gitlab-ci.yml` |
| `.gitlab/issue_templates/Bug.md` | Issue template for Bug | `docs: add .gitlab/issue_templates/Bug.md` |
| `.gitlab/issue_templates/Research.md` | Issue template for Research | `docs: add .gitlab/issue_templates/Research.md` |
| `CHANGELOG.md` | Version and release scope | `docs: add CHANGELOG.md` |
| `CITATION.cff` | Machine-readable project citation | `docs: add CITATION.cff` |
| `CONTRIBUTING.md` | Contribution and data provenance rules | `docs: add CONTRIBUTING.md` |
| `Dockerfile` | Non-root FastAPI container for local and HF Space deployment | `chore: add Dockerfile` |
| `LICENSE` | MIT license notice for original project | `chore: add LICENSE` |
| `Makefile` | Common development commands | `chore: add Makefile` |
| `README.md` | Main project overview, introduction video, measured benchmark, quick start and publication guidance | `docs: add README.md` |
| `SECURITY.md` | Security disclosure and demo limitations | `docs: add SECURITY.md` |
| `agentpulse/__init__.py` | Python package and version | `feat: add agentpulse/__init__.py` |
| `agentpulse/api.py` | FastAPI and HTML scoring interface | `feat: add agentpulse/api.py` |
| `agentpulse/generate.py` | Seeded dataset generation and optional per-shard commits | `feat: add agentpulse/generate.py` |
| `agentpulse/predict.py` | Safe dependency-free model inference | `feat: add agentpulse/predict.py` |
| `agentpulse/schema.py` | Ordered model features, target and range constraints | `feat: add agentpulse/schema.py` |
| `agentpulse/stream_train.py` | Bounded-memory full-train SGD with JSON export | `feat: add agentpulse/stream_train.py` |
| `agentpulse/train.py` | Three baseline models and held-out evaluation | `feat: add agentpulse/train.py` |
| `assets/benchmark.svg` | Measured benchmark visualization | `chore: add assets/benchmark.svg` |
| `assets/cover.png` | Original 1280x720 research cover | `chore: add assets/cover.png` |
| `assets/intro.vtt` | Video captions and narration transcript | `chore: add assets/intro.vtt` |
| `assets/intro.webm` | Rendered 30-second narrated WebM | `chore: add assets/intro.webm` |
| `community/discussion.md` | Ready-to-review discussion draft | `docs: add community/discussion.md` |
| `community/launch-copy.md` | Cross-platform launch copy | `docs: add community/launch-copy.md` |
| `community/roadmap.md` | Eight issue drafts with acceptance criteria | `docs: add community/roadmap.md` |
| `data/demo/manifest.json` | Data shard metadata, counts and SHA-256 checksums | `data: add data/demo/manifest.json` |
| `data/demo/test-0000.csv` | Original synthetic test telemetry shard 0000 (1,000 rows) | `data: add data/demo/test-0000.csv` |
| `data/demo/test-0010.csv` | Original synthetic test telemetry shard 0010 (1,000 rows) | `data: add data/demo/test-0010.csv` |
| `data/demo/train-0002.csv` | Original synthetic train telemetry shard 0002 (1,000 rows) | `data: add data/demo/train-0002.csv` |
| `data/demo/train-0003.csv` | Original synthetic train telemetry shard 0003 (1,000 rows) | `data: add data/demo/train-0003.csv` |
| `data/demo/train-0004.csv` | Original synthetic train telemetry shard 0004 (1,000 rows) | `data: add data/demo/train-0004.csv` |
| `data/demo/train-0005.csv` | Original synthetic train telemetry shard 0005 (1,000 rows) | `data: add data/demo/train-0005.csv` |
| `data/demo/train-0006.csv` | Original synthetic train telemetry shard 0006 (1,000 rows) | `data: add data/demo/train-0006.csv` |
| `data/demo/train-0007.csv` | Original synthetic train telemetry shard 0007 (1,000 rows) | `data: add data/demo/train-0007.csv` |
| `data/demo/train-0008.csv` | Original synthetic train telemetry shard 0008 (1,000 rows) | `data: add data/demo/train-0008.csv` |
| `data/demo/train-0009.csv` | Original synthetic train telemetry shard 0009 (1,000 rows) | `data: add data/demo/train-0009.csv` |
| `data/demo/train-0012.csv` | Original synthetic train telemetry shard 0012 (1,000 rows) | `data: add data/demo/train-0012.csv` |
| `data/demo/train-0013.csv` | Original synthetic train telemetry shard 0013 (1,000 rows) | `data: add data/demo/train-0013.csv` |
| `data/demo/train-0014.csv` | Original synthetic train telemetry shard 0014 (1,000 rows) | `data: add data/demo/train-0014.csv` |
| `data/demo/train-0015.csv` | Original synthetic train telemetry shard 0015 (1,000 rows) | `data: add data/demo/train-0015.csv` |
| `data/demo/train-0016.csv` | Original synthetic train telemetry shard 0016 (1,000 rows) | `data: add data/demo/train-0016.csv` |
| `data/demo/train-0017.csv` | Original synthetic train telemetry shard 0017 (1,000 rows) | `data: add data/demo/train-0017.csv` |
| `data/demo/train-0018.csv` | Original synthetic train telemetry shard 0018 (1,000 rows) | `data: add data/demo/train-0018.csv` |
| `data/demo/train-0019.csv` | Original synthetic train telemetry shard 0019 (1,000 rows) | `data: add data/demo/train-0019.csv` |
| `data/demo/validation-0001.csv` | Original synthetic validation telemetry shard 0001 (1,000 rows) | `data: add data/demo/validation-0001.csv` |
| `data/demo/validation-0011.csv` | Original synthetic validation telemetry shard 0011 (1,000 rows) | `data: add data/demo/validation-0011.csv` |
| `docs/data-dictionary.md` | Complete column semantics and units | `docs: add docs/data-dictionary.md` |
| `docs/discoverability.md` | Search metadata, community and launch strategy | `docs: add docs/discoverability.md` |
| `docs/file-catalog.md` | Every project file description and initial commit message | `docs: add docs/file-catalog.md` |
| `docs/full-scale.md` | 5 GB generation, memory and commit instructions | `docs: add docs/full-scale.md` |
| `docs/index.html` | SEO-ready static portfolio landing page | `chore: add docs/index.html` |
| `docs/methodology.md` | Simulation, evaluation protocol and limitations | `docs: add docs/methodology.md` |
| `docs/publish.md` | Platform-specific manual publication instructions | `docs: add docs/publish.md` |
| `docs/references.md` | Research and official platform references | `docs: add docs/references.md` |
| `examples/prediction.json` | Actual portable inference output | `chore: add examples/prediction.json` |
| `examples/telemetry.json` | Example 16-feature payload | `chore: add examples/telemetry.json` |
| `hyperframer/README.md` | Framework-neutral motion source scope and rendering instructions | `docs: add hyperframer/README.md` |
| `hyperframer/components/metric-card.html` | Editable metric component | `chore: add hyperframer/components/metric-card.html` |
| `hyperframer/components/pulse.svg` | Original vector pulse component | `chore: add hyperframer/components/pulse.svg` |
| `hyperframer/layouts/intro.json` | Scene timings and visual layout | `chore: add hyperframer/layouts/intro.json` |
| `hyperframer/storyboard.md` | Six-scene intro storyboard | `docs: add hyperframer/storyboard.md` |
| `hyperframer/tokens/theme.json` | Intro color and layout tokens | `chore: add hyperframer/tokens/theme.json` |
| `models/logistic.json` | Actual fitted demo logistic coefficients and scaler | `chore: add models/logistic.json` |
| `models/sgd.json` | Actual fitted streaming SGD coefficients and scaler | `chore: add models/sgd.json` |
| `notebooks/baseline.ipynb` | Runnable offline Kaggle baseline notebook | `chore: add notebooks/baseline.ipynb` |
| `publishing/hf-dataset/README.md` | Platform-specific hf-dataset card template | `docs: add publishing/hf-dataset/README.md` |
| `publishing/hf-model/README.md` | Platform-specific hf-model card template | `docs: add publishing/hf-model/README.md` |
| `publishing/hf-space/README.md` | Platform-specific hf-space card template | `docs: add publishing/hf-space/README.md` |
| `publishing/kaggle/dataset-metadata.json` | Platform-specific kaggle dataset-metadata.json template | `chore: add publishing/kaggle/dataset-metadata.json` |
| `publishing/kaggle/kernel-metadata.json` | Platform-specific kaggle kernel-metadata.json template | `chore: add publishing/kaggle/kernel-metadata.json` |
| `reports/benchmark.json` | Measured three-model demo benchmark | `chore: add reports/benchmark.json` |
| `reports/build-verification.md` | Executed and unexecuted checks | `docs: add reports/build-verification.md` |
| `reports/sgd.json` | Measured streaming SGD evaluation | `chore: add reports/sgd.json` |
| `reports/test-results.txt` | Actual local pytest results | `chore: add reports/test-results.txt` |
| `requirements-api.txt` | API dependencies | `chore: add requirements-api.txt` |
| `requirements-publish.txt` | Optional platform and Parquet dependencies | `chore: add requirements-publish.txt` |
| `requirements.txt` | Pinned tested numerical and ML dependencies | `chore: add requirements.txt` |
| `tests/test_data.py` | Dataset integrity, determinism and leakage tests | `test: add tests/test_data.py` |
| `tests/test_model.py` | Inference and metrics regression tests | `test: add tests/test_model.py` |
| `tests/test_training.py` | Retraining and streaming smoke tests | `test: add tests/test_training.py` |
| `tools/check_release.py` | Offline staged artifact checks | `feat: add tools/check_release.py` |
| `tools/make_intro.py` | Reproducible narrated video renderer | `feat: add tools/make_intro.py` |
| `tools/stage_release.py` | Offline platform release folder builder | `feat: add tools/stage_release.py` |
| `tools/validate_data.py` | Manifest integrity and schema checks | `feat: add tools/validate_data.py` |

## Launch trailer update

| File | Description | Change |
|---|---|---|
| `assets/intro-saas.mp4` | Supplied 30-second text-led SaaS launch trailer, H.264/AAC | Added alongside the original narrated media |
