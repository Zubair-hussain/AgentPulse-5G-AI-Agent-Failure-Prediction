"""Dependency-free, non-executable JSON inference. No prompts or network."""
import argparse,json,math
from pathlib import Path
from .schema import FEATURES,RANGES

def predict(record,model):
    if model['features']!=FEATURES: raise ValueError('model schema mismatch')
    if set(record)!=set(FEATURES): raise ValueError('exactly the documented features are required')
    x=[]
    for k in FEATURES:
        a=record[k]; lo,hi=RANGES[k]
        if isinstance(a,bool) or not isinstance(a,(int,float)) or not math.isfinite(a) or a<lo or (hi is not None and a>hi): raise ValueError(f'invalid {k}')
        x.append(a)
    z=model['intercept']+sum(c*(a-m)/s for a,m,s,c in zip(x,model['mean'],model['scale'],model['coef']))
    p=1/(1+math.exp(-max(-700,min(700,z))))
    return {'failure_risk':p,'threshold':model['threshold'],'flagged':p>=model['threshold']}

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('input'); p.add_argument('--model',default='models/logistic.json'); a=p.parse_args(); print(json.dumps(predict(json.loads(Path(a.input).read_text()),json.loads(Path(a.model).read_text())),indent=2))
