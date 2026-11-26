# Publishing checklist
Verify author name, real Git email, account names, repository slugs and license before any push. No public uploads have been performed. Use your own tokens with least privileges; do not commit credentials. The HF owner inferred from the existing dataset is zubairH123; Kaggle and GitLab handles are not verified. Replace YOUR_KAGGLE_HANDLE.

```bash
pip install -r requirements-publish.txt
python -m tools.stage_release --hf-owner zubairH123 --kaggle-owner YOUR_KAGGLE_HANDLE
python -m tools.check_release release
hf auth login
hf repo create zubairH123/agentpulse-5g --repo-type dataset
hf upload zubairH123/agentpulse-5g release/hf-dataset --repo-type dataset
hf repo create zubairH123/agentpulse-failure-predictor --repo-type model
hf upload zubairH123/agentpulse-failure-predictor release/hf-model --repo-type model
```
Create a Docker Space in HF UI named `agentpulse-risk-demo`, then `hf upload zubairH123/agentpulse-risk-demo release/hf-space --repo-type space`. Check dataset viewer splits, test model code locally and check Space `/health`, `/docs`, `/`. HF does not execute GitHub CI; the Docker Space build is its native deployment check. Use Kaggle API authentication per official CLI docs, then:

```bash
kaggle datasets create -p release/kaggle-dataset --keep-tabular
kaggle kernels push -p release/kaggle-notebook
```
Initial Kaggle upload and notebook are private by default/metadata; review then publish in UI. Kaggle dataset API currently does not list MIT, so metadata uses `other` with explicit MIT text and LICENSE file. Verify acceptance in UI. Kaggle notebook execution/status is its remote test, not GitHub Actions. The included workflow checks platform packages offline; it has not run in a hosted CI. For a full release stage using `--data data/full-5gb --out release-full`; note this duplicates the data for two platforms. The model staged remains the demo logistic model unless explicitly replaced with documented full-training weights and updated cards. Check `hf --help` and `kaggle --help` if installed CLI version differs.

GitHub/GitLab: extract ZIP including `.git`, configure your actual verified commit email for subsequent work, create empty remote repositories, and set `git remote add origin <your-github-url>`; `git push -u origin main`. For GitLab use a second remote `git remote add gitlab <your-gitlab-url>` then `git push -u gitlab main`. The archive contains genuine per-file creation commits generated in one session using a local placeholder noreply address; it does not claim a thousand days of development or guaranteed contribution credit. If desired, regenerate history with your verified email before first publication. Never force push without checking remote history.
