"""Reproducible held-out benchmark and portable JSON logistic model."""
import argparse,json,time,platform
from pathlib import Path
import numpy as np
import pandas as pd
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, average_precision_score, brier_score_loss, confusion_matrix
from .schema import FEATURES


def read_split(root,split,cap):
    files=sorted([*Path(root).glob(f'{split}-*.csv'),*Path(root).glob(f'{split}-*.parquet')]); frames=[]
    if not files: raise ValueError(f'missing {split} shards')
    for i,f in enumerate(files):
        df=pd.read_csv(f) if f.suffix=='.csv' else pd.read_parquet(f)
        if cap and len(df)>cap: df=df.sample(cap,random_state=2026+i)
        frames.append(df)
    return pd.concat(frames,ignore_index=True)


def scores(y,p,t):
    pred=p>=t
    return dict(accuracy=accuracy_score(y,pred),f1=f1_score(y,pred,zero_division=0),precision=precision_score(y,pred,zero_division=0),recall=recall_score(y,pred,zero_division=0),roc_auc=roc_auc_score(y,p),pr_auc=average_precision_score(y,p),brier=brier_score_loss(y,p),confusion_matrix=confusion_matrix(y,pred,labels=[0,1]).tolist(),threshold=float(t))


def run(data,out,report,cap=1000):
    train,val,test=[read_split(data,s,cap) for s in ('train','validation','test')]
    assert not set(train.environment_id)&set(test.environment_id)
    assert not set(train.environment_id)&set(val.environment_id)
    assert not set(test.environment_id)&set(val.environment_id)
    scaler=StandardScaler().fit(train[FEATURES]); x,v,t=[scaler.transform(d[FEATURES]) for d in (train,val,test)]
    models={'prior':DummyClassifier(strategy='prior'),'logistic':LogisticRegression(max_iter=300,random_state=2026),'hist_gradient_boosting':HistGradientBoostingClassifier(max_iter=90,random_state=2026)}
    result={'source':str(data),'synthetic':True,'seed':2026,'max_rows_per_shard':cap,'rows':{s:len(d) for s,d in zip(('train','validation','test'),(train,val,test))},'positive_rate':{s:float(d.failed.mean()) for s,d in zip(('train','validation','test'),(train,val,test))},'versions':{'python':platform.python_version(),'sklearn':sklearn.__version__,'numpy':np.__version__,'pandas':pd.__version__},'models':{}}
    for name,m in models.items():
        start=time.perf_counter(); m.fit(x,train.failed); elapsed=time.perf_counter()-start
        pv=m.predict_proba(v)[:,1]; pt=m.predict_proba(t)[:,1]
        th=max(np.arange(.1,.81,.025),key=lambda a:f1_score(val.failed,pv>=a,zero_division=0))
        result['models'][name]={'validation':scores(val.failed,pv,th),'test':scores(test.failed,pt,th),'fit_seconds':elapsed}
    m=models['logistic']; model={'format':'agentpulse-logistic-v1','features':FEATURES,'mean':scaler.mean_.tolist(),'scale':scaler.scale_.tolist(),'coef':m.coef_[0].tolist(),'intercept':float(m.intercept_[0]),'threshold':result['models']['logistic']['test']['threshold']}
    for path,obj in [(Path(out),model),(Path(report),result)]: path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,indent=2)+'\n')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--data',default='data/demo'); p.add_argument('--out',default='models/logistic.json'); p.add_argument('--report',default='reports/benchmark.json'); p.add_argument('--max-per-shard',type=int,default=1000,help='0 loads every row (requires sufficient RAM)'); a=p.parse_args(); print(json.dumps(run(a.data,a.out,a.report,a.max_per_shard),indent=2))
