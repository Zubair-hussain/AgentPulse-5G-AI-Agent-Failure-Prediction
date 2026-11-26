"""Prepare isolated, upload-ready folders; never uploads or needs credentials."""
import argparse,json,shutil,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def stage(data,out,hf,kaggle):
    data=Path(data); out=Path(out); m=json.loads((data/'manifest.json').read_text())
    for owner in (hf,kaggle):
        if not re.fullmatch(r'[A-Za-z0-9_-]+',owner): raise ValueError('invalid owner slug')
    if out.exists() and any(out.iterdir()): raise ValueError('choose a fresh output folder')
    for name in ('hf-dataset','hf-model','hf-space','kaggle-dataset','kaggle-notebook'): (out/name).mkdir(parents=True,exist_ok=True)
    def copy(src,dst): shutil.copy2(ROOT/src,dst)
    def template(src,dst):
        text=(ROOT/src).read_text()
        for key,value in {'__HF_OWNER__':hf,'__KAGGLE_OWNER__':kaggle,'__ROWS__':f"{m['rows']:,}",'__BYTES__':f"{m['bytes']:,}",'__FORMAT__':m['format']}.items(): text=text.replace(key,value)
        dst.write_text(text)
    ds=out/'hf-dataset'; kd=out/'kaggle-dataset'; (ds/'data').mkdir()
    template('publishing/hf-dataset/README.md',ds/'README.md')
    template('publishing/kaggle/dataset-metadata.json',kd/'dataset-metadata.json')
    for folder in (ds,kd):
        copy('LICENSE',folder/'LICENSE'); copy('docs/data-dictionary.md',folder/'data-dictionary.md'); shutil.copy2(data/'manifest.json',folder/'manifest.json')
    for s in m['shards']:
        p=data/s['file']; shutil.copy2(p,ds/'data'/p.name); shutil.copy2(p,kd/p.name)
    copy('assets/cover.png',kd/'dataset-cover-image.png')
    model=out/'hf-model'; template('publishing/hf-model/README.md',model/'README.md')
    for src in ['LICENSE','models/logistic.json','reports/benchmark.json','examples/telemetry.json','agentpulse/schema.py']: copy(src,model/Path(src).name)
    (model/'predict.py').write_text((ROOT/'agentpulse/predict.py').read_text().replace('from .schema','from schema'))
    space=out/'hf-space'; copy('publishing/hf-space/README.md',space/'README.md'); copy('Dockerfile',space/'Dockerfile'); copy('requirements-api.txt',space/'requirements-api.txt'); copy('LICENSE',space/'LICENSE')
    shutil.copytree(ROOT/'agentpulse',space/'agentpulse',ignore=shutil.ignore_patterns('__pycache__')); (space/'models').mkdir(); copy('models/logistic.json',space/'models/logistic.json')
    notebook=out/'kaggle-notebook'; template('publishing/kaggle/kernel-metadata.json',notebook/'kernel-metadata.json'); copy('notebooks/baseline.ipynb',notebook/'baseline.ipynb')
    print('Prepared:',out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',default='data/demo');p.add_argument('--out',default='release');p.add_argument('--hf-owner',required=True);p.add_argument('--kaggle-owner',required=True);a=p.parse_args();stage(a.data,a.out,a.hf_owner,a.kaggle_owner)
