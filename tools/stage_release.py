"""Prepare isolated, upload-ready folders; never uploads or needs credentials."""
import argparse,json,shutil,re,subprocess
from pathlib import Path
from agentpulse.schema import FEATURES,RANGES
ROOT=Path(__file__).resolve().parents[1]
def stage(data,out,hf,kaggle):
    data=Path(data); out=Path(out); m=json.loads((data/'manifest.json').read_text())
    for owner in (hf,kaggle):
        if not re.fullmatch(r'[A-Za-z0-9_-]+',owner): raise ValueError('invalid owner slug')
    if out.exists() and any(out.iterdir()): raise ValueError('choose a fresh output folder')
    for name in ('hf-dataset','hf-model','hf-space','kaggle-dataset','kaggle-notebook'): (out/name).mkdir(parents=True,exist_ok=True)
    def copy(src,dst): shutil.copy2(ROOT/src,dst)
    def template(src,dst):
        text=(ROOT/src).read_text(encoding='utf-8')
        for key,value in {'__HF_OWNER__':hf,'__KAGGLE_OWNER__':kaggle,'__ROWS__':f"{m['rows']:,}",'__BYTES__':f"{m['bytes']:,}",'__FORMAT__':m['format']}.items(): text=text.replace(key,value)
        dst.write_text(text,encoding='utf-8')
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
    (model/'predict.py').write_text((ROOT/'agentpulse/predict.py').read_text(encoding='utf-8').replace('from .schema','from schema'),encoding='utf-8')
    space=out/'hf-space'
    # Keep the original project directories; the Space gets its own metadata card.
    for name in ('agentpulse','assets','community','docs','examples','hyperframer','models','notebooks','publishing','reports','tests','tools','.github','.gitlab'):
        shutil.copytree(ROOT/name,space/name,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache'))
    (space/'data').mkdir(); shutil.copytree(data,space/'data/demo')
    for name in ('.gitattributes','.gitignore','.gitlab-ci.yml','CHANGELOG.md','CITATION.cff','CONTRIBUTING.md','Dockerfile','LICENSE','Makefile','SECURITY.md','requirements.txt','requirements-api.txt','requirements-publish.txt'):
        copy(name,space/name)
    copy('README.md',space/'docs/github-readme.md')
    template('publishing/hf-space/README.md',space/'README.md')
    for name in ('index.html','predict.mjs'):
        copy('publishing/hf-space/'+name,space/name)
    (space/'schema.json').write_text(json.dumps({'features':FEATURES,'ranges':RANGES},indent=2)+'\n',encoding='utf-8')
    for folder in (ds,model):
        (folder/'assets').mkdir()
        for name in ('cover.png','benchmark.svg','intro-saas.mp4'):
            copy('assets/'+name,folder/'assets'/name)
        copy('CITATION.cff',folder/'CITATION.cff')
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    provenance={'source_repository':'https://github.com/Zubair-hussain/AgentPulse-5G-AI-Agent-Failure-Prediction','source_branch':'prod_core','source_commit':revision,'dataset_sha256':{s['file']:s['sha256'] for s in m['shards']}}
    for folder in (ds,model,space):
        (folder/'source-revision.json').write_text(json.dumps(provenance,indent=2)+'\n',encoding='utf-8')
    notebook=out/'kaggle-notebook'; template('publishing/kaggle/kernel-metadata.json',notebook/'kernel-metadata.json'); copy('notebooks/baseline.ipynb',notebook/'baseline.ipynb')
    print('Prepared:',out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',default='data/demo');p.add_argument('--out',default='release');p.add_argument('--hf-owner',required=True);p.add_argument('--kaggle-owner',required=True);a=p.parse_args();stage(a.data,a.out,a.hf_owner,a.kaggle_owner)
