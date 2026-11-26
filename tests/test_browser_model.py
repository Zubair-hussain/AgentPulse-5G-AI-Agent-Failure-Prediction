"""Check the hosted browser predictor against canonical Python inference."""
import json
from pathlib import Path
import random
import shutil
import subprocess

import pytest

from agentpulse.predict import predict
from agentpulse.schema import FEATURES, RANGES


def test_browser_inference_parity():
    if not shutil.which('node'):
        pytest.skip('Node.js is needed to check browser inference')
    model = json.loads(Path('models/logistic.json').read_text())
    example = json.loads(Path('examples/telemetry.json').read_text())
    rng = random.Random(2026)
    records = [example]
    for _ in range(100):
        records.append({key: rng.uniform(0, 1 if RANGES[key][1] else max(1, example[key] * 4)) for key in FEATURES})
    invalid = [{}, {**example, 'retry_count': -1}, {**example, 'tool_error_ratio': 1.1},
               {**example, 'elapsed_ms': True}, {**example, 'elapsed_ms': '1'},
               {**example, 'extra': 1}]
    script = '''
import {predict} from './publishing/hf-space/predict.mjs';
import fs from 'node:fs';
const {records, invalid, model, schema} = JSON.parse(fs.readFileSync(0, 'utf8'));
const scores = records.map(record => predict(record, model, schema));
const rejected = invalid.map(record => {try {predict(record, model, schema); return false;} catch {return true;}});
console.log(JSON.stringify({scores,rejected}));
'''
    result = subprocess.run(['node', '--input-type=module', '-e', script],
                            input=json.dumps({'records': records, 'invalid': invalid, 'model': model,
                                              'schema': {'features': FEATURES, 'ranges': RANGES}}),
                            text=True, capture_output=True, check=True)
    actual = json.loads(result.stdout)
    for record, score in zip(records, actual['scores']):
        expected = predict(record, model)
        assert score['failure_risk'] == pytest.approx(expected['failure_risk'], abs=1e-12)
        assert score['flagged'] == expected['flagged']
    assert all(actual['rejected'])
