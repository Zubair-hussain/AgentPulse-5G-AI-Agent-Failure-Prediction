"""Offline sanity checks for staged platform metadata and local inference."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path

def check(root):
    root=Path(root)
    for name in ('hf-dataset','hf-model','hf-space'):
        folder=root/name
        assert '__HF_OWNER__' not in (folder/'README.md').read_text(encoding='utf-8')
        source=json.loads((folder/'source-revision.json').read_text(encoding='utf-8'))
        assert len(source['source_commit'])==40 and source['source_branch']=='prod_core'
        assert (folder/'assets/intro-saas.mp4').stat().st_size>0
    # Keep canonical source templates intact inside the Space snapshot.
    for name in ('agentpulse','data/demo','docs','models','tests','tools','publishing'):
        assert (root/'hf-space'/name).is_dir()
    hashes={hashlib.sha256((root/name/'assets/intro-saas.mp4').read_bytes()).hexdigest() for name in ('hf-dataset','hf-model','hf-space')}
    assert len(hashes)==1
    ds=root/'hf-dataset'; m=json.loads((ds/'manifest.json').read_text())
    for s in m['shards']: assert (ds/'data'/s['file']).stat().st_size==s['bytes']
    kd=root/'kaggle-dataset'; meta=json.loads((kd/'dataset-metadata.json').read_text()); assert '__KAGGLE_OWNER__' not in meta['id'] and meta['licenses']==[{'name':'other'}]
    assert all((kd/s['file']).stat().st_size==s['bytes'] for s in m['shards'])
    kn=root/'kaggle-notebook'; km=json.loads((kn/'kernel-metadata.json').read_text()); assert km['dataset_sources']==[meta['id']]
    assert json.loads((kn/km['code_file']).read_text())['nbformat']==4
    model=root/'hf-model'; subprocess.run([sys.executable,'predict.py','telemetry.json','--model','logistic.json'],cwd=model,check=True)
    print('Offline Hugging Face / Kaggle staging checks passed.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='release');check(p.parse_args().root)
