"""Bounded-memory SGD training over every training shard; validation/test sampled."""
import argparse,json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score
from .schema import FEATURES
from .train import read_split,scores

def batches(root):
    for p in sorted([*Path(root).glob('train-*.csv'),*Path(root).glob('train-*.parquet')]):
        if p.suffix=='.csv': yield from pd.read_csv(p,chunksize=25000)
        else:
            import pyarrow.parquet as pq
            for batch in pq.ParquetFile(p).iter_batches(batch_size=25000): yield batch.to_pandas()

def run(root,out,report,epochs=2,cap=1000):
    scaler=StandardScaler(); n=0
    for d in batches(root): scaler.partial_fit(d[FEATURES]); n+=len(d)
    if not n: raise ValueError('No training data')
    m=SGDClassifier(loss='log_loss',random_state=2026,average=True)
    for _ in range(epochs):
        for d in batches(root): m.partial_fit(scaler.transform(d[FEATURES]),d.failed,classes=[0,1])
    v,t=[read_split(root,s,cap) for s in ('validation','test')]; pv,pt=[m.predict_proba(scaler.transform(d[FEATURES]))[:,1] for d in (v,t)]
    th=max(np.arange(.1,.81,.025),key=lambda a:f1_score(v.failed,pv>=a,zero_division=0))
    result={'synthetic':True,'training_rows':n,'epochs':epochs,'max_eval_rows_per_shard':cap,'validation':scores(v.failed,pv,th),'test':scores(t.failed,pt,th)}
    model=dict(format='agentpulse-logistic-v1',features=FEATURES,mean=scaler.mean_.tolist(),scale=scaler.scale_.tolist(),coef=m.coef_[0].tolist(),intercept=float(m.intercept_[0]),threshold=float(th))
    for path,obj in [(Path(out),model),(Path(report),result)]: path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2)+'\n')
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--data',default='data/demo'); p.add_argument('--out',default='models/sgd.json'); p.add_argument('--report',default='reports/sgd.json'); p.add_argument('--epochs',type=int,default=2); p.add_argument('--max-eval-per-shard',type=int,default=1000); a=p.parse_args(); print(json.dumps(run(a.data,a.out,a.report,a.epochs,a.max_eval_per_shard),indent=2))
