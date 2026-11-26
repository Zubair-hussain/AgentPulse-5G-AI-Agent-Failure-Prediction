"""Generate original synthetic, pre-outcome telemetry; never accesses real logs."""
import argparse, hashlib, json, math, subprocess
from pathlib import Path
import numpy as np
import pandas as pd
from .schema import FEATURES, SPLITS


def generate_shard(n, shard, seed=2026):
    # Separate generator streams and environment cohorts by split; one row per run.
    split = ('test' if shard%10==0 else 'validation' if shard%10==1 else 'train')
    r=np.random.default_rng(np.random.SeedSequence([seed, shard]))
    env=r.integers(0,12,n)+12*SPLITS[split]
    load=r.beta(2,3,n); complexity=r.gamma(2,1,n); instability=r.beta(1.4,5,n)
    shift={'train':0.,'validation':.05,'test':.12}[split]
    clip=lambda a: np.clip(a,0,1)
    d={
      'elapsed_ms': r.lognormal(6.4+.65*load+.13*complexity,.55,n),
      'input_tokens': r.lognormal(7.1+.19*complexity,.7,n).astype(int),
      'output_tokens': r.lognormal(5.3+.12*complexity,.6,n).astype(int),
      'tool_calls':r.poisson(1.5+complexity),
      'retry_count':r.poisson(.15+1.5*instability+load*.4),
      'queue_ms':r.lognormal(3.4+2*load,.7,n),
      'rate_limit_ratio':clip(.55*load+.4*instability+r.normal(0,.12,n)+shift),
      'tool_error_ratio':clip(.75*instability+r.normal(0,.10,n)),
      'context_utilization':clip(.17+.16*complexity+r.normal(0,.16,n)),
      'cpu_utilization':clip(.15+.8*load+r.normal(0,.12,n)),
      'memory_utilization':clip(.18+.4*load+.09*complexity+r.normal(0,.11,n)),
      'retrieval_score':clip(.89-.37*instability-.05*complexity+r.normal(0,.15,n)),
      'budget_utilization':clip(.12+.14*complexity+.27*load+r.normal(0,.12,n)),
      'network_jitter_ms':r.lognormal(2.5+2*instability,.6,n),
      'concurrency':r.poisson(2+16*load),
      'step_count':r.poisson(2+complexity*1.5)}
    # No outcome columns appear in inputs; hidden noise and cohort shift keep the task stochastic.
    z=(-3.5+2.4*d['rate_limit_ratio']+2.8*d['tool_error_ratio']+1.4*d['context_utilization']
       +.32*d['retry_count']+1.1*d['budget_utilization']-1.45*d['retrieval_score']
       +2.2*(d['cpu_utilization']>.75)*(d['rate_limit_ratio']>.5)+.55*instability
       +r.normal(0,.55,n)+shift)
    y=r.binomial(1,1/(1+np.exp(-z)))
    frame=pd.DataFrame(d)[FEATURES].round(5)
    frame.insert(0,'run_id',[f'{seed}-{shard:05d}-{i:07d}' for i in range(n)])
    frame.insert(1,'environment_id',env); frame.insert(2,'split',split)
    frame['failed']=y
    return frame


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',default='data/demo'); p.add_argument('--shards',type=int,default=20)
    p.add_argument('--rows-per-shard',type=int,default=1000); p.add_argument('--seed',type=int,default=2026)
    p.add_argument('--target-gb',type=float,default=None,help='Calibrate fixed shard count to approximate decimal GB on disk')
    p.add_argument('--format',choices=['csv','parquet'],default='csv'); p.add_argument('--git-commit',action='store_true')
    a=p.parse_args(); out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    if a.shards<10 or a.rows_per_shard<1 or (a.target_gb is not None and a.target_gb<=0): p.error('need >=10 shards, positive rows and target')
    if any(out.iterdir()): p.error('output directory must be empty; use a new release directory')
    def write(frame,path):
        if a.format=='csv': frame.to_csv(path,index=False)
        else: frame.to_parquet(path,index=False,compression='zstd')
    n=a.rows_per_shard
    if a.target_gb:
        pilot=out/f'.pilot.{a.format}'; write(generate_shard(10000,2,a.seed),pilot)
        n=max(1,round(a.target_gb*1e9/a.shards/(pilot.stat().st_size/10000))); pilot.unlink()
    manifest=[]
    for s in range(a.shards):
        frame=generate_shard(n,s,a.seed); split=frame['split'].iat[0]
        path=out/f'{split}-{s:04d}.{a.format}'; write(frame,path)
        manifest.append(dict(file=path.name,split=split,rows=n,bytes=path.stat().st_size,sha256=hashlib.file_digest(path.open('rb'),'sha256').hexdigest(),positive=int(frame.failed.sum())))
        if a.git_commit:
            subprocess.run(['git','add','-f','--',str(path)],check=True); subprocess.run(['git','commit','-m',f'data: add {split} telemetry shard {s:04d}'],check=True)
    result={'synthetic':True,'seed':a.seed,'format':a.format,'rows':sum(x['rows'] for x in manifest),'bytes':sum(x['bytes'] for x in manifest),'shards':manifest}
    path=out/'manifest.json'; path.write_text(json.dumps(result,indent=2)+'\n')
    if a.git_commit:
        subprocess.run(['git','add','-f','--',str(path)],check=True); subprocess.run(['git','commit','-m','data: record generated release manifest'],check=True)
    print(json.dumps({k:v for k,v in result.items() if k!='shards'},indent=2))
if __name__=='__main__': main()
