from agentpulse.train import run
from agentpulse.stream_train import run as stream

def test_retrain(tmp_path):
    r=run('data/demo',tmp_path/'model.json',tmp_path/'metrics.json',150)
    assert r['rows']['test']==300 and r['models']['logistic']['test']['roc_auc']>.5

def test_stream(tmp_path):
    r=stream('data/demo',tmp_path/'model.json',tmp_path/'metrics.json',1,150)
    assert r['training_rows']==16000 and r['test']['roc_auc']>.5
