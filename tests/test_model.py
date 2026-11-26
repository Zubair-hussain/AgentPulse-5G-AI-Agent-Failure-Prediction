import json,math
from pathlib import Path
import pytest
from agentpulse.predict import predict
from agentpulse.schema import FEATURES
M=json.loads(Path('models/logistic.json').read_text())
R=json.loads(Path('examples/telemetry.json').read_text())

def test_score():
    p=predict(R,M); assert 0<=p['failure_risk']<=1 and p['flagged']==(p['failure_risk']>=p['threshold'])
def test_missing():
    with pytest.raises(ValueError): predict({},M)
@pytest.mark.parametrize('bad',[-1,float('nan'),float('inf'),True,'1'])
def test_invalid(bad):
    with pytest.raises(ValueError): predict({**R,'elapsed_ms':bad},M)
def test_invalid_ratio():
    with pytest.raises(ValueError): predict({**R,'cpu_utilization':1.2},M)
def test_known_risk_order():
    low={**R,'rate_limit_ratio':0.01,'tool_error_ratio':0.01,'retry_count':0}
    high={**R,'rate_limit_ratio':.95,'tool_error_ratio':.9,'retry_count':8}
    assert predict(high,M)['failure_risk']>predict(low,M)['failure_risk']
def test_metrics():
    r=json.loads(Path('reports/benchmark.json').read_text()); assert r['synthetic'] and r['models']['logistic']['test']['roc_auc']>.5
