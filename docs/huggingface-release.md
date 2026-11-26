# Hugging Face publication verification

Verified on 2026-11-26. Author: Zubair Hussain. Authenticated publisher: `zubairH123`.

## Public artifacts and genuine publication commits

- Dataset: [zubairH123/agentpulse-5g](https://huggingface.co/datasets/zubairH123/agentpulse-5g) | [initial publication commit](https://huggingface.co/datasets/zubairH123/agentpulse-5g/commit/21ef704e77795020646ec0b6edecc4096f14740c).
- Model: [zubairH123/agentpulse-failure-predictor](https://huggingface.co/zubairH123/agentpulse-failure-predictor) | [initial publication commit](https://huggingface.co/zubairH123/agentpulse-failure-predictor/commit/b8b061df2d28aac394f3d2af47de614f8078ee14).
- Space: [zubairH123/agentpulse-risk-demo](https://huggingface.co/spaces/zubairH123/agentpulse-risk-demo) | [initial publication commit](https://huggingface.co/spaces/zubairH123/agentpulse-risk-demo/commit/9d1530c2c2563528ac4f8be6e83412f6c1cc7066).

The Space preserves the project directories; GitHub retains its original history on `prod_core`. Every upload includes `source-revision.json` with its GitHub revision and dataset shard checksums. Hub commit authorship comes from the authenticated publisher; commits describe actual changes.

## Executed checks

- All three Hub cards passed metadata validation.
- Offline release staging and bundled Python inference passed.
- Browser inference matched canonical Python inference on 101 records; invalid records were rejected.
- The publicly downloaded inference bundle produced failure risk `0.1481684489101845`, threshold approximately `0.30`, flagged `false`.
- The public static Space loaded its model and all 16 fields. Example, fewer-errors, and retries-plus-errors presets displayed 14.8%, 1.9%, and 97.8% respectively. An out-of-range ratio was blocked.
- Public Space MP4 playback passed, with no JavaScript errors and no horizontal overflow at 390px width.
- GitHub CI passed Python 3.11, 3.12, and 3.13 plus offline publishing-package checks after adding the browser predictor.

## Platform constraints

Hugging Face rejected creation of a Docker Space with HTTP 402 because compute Spaces currently require a paid plan. The published app uses free static hosting and the same JSON model in the browser. Python API and Docker files remain available for local deployment.

The dataset CSV shards and split metadata are published. The dataset viewer service returned HTTP 503 during verification; its automatic preview is not claimed as verified. The release is a 20,000-row synthetic demo, not a 5 GB upload or a production validation.

## Discoverability additions

The dataset, model, Space, and collection link to one another. Cards include a playable trailer, benchmark graphics, author credit, citation, use examples, and relevant task metadata. GitHub links to the live artifacts. Draft launch copy is in `community/huggingface-launch.md`; no external social posts were sent and no engagement or ranking claims were fabricated.
