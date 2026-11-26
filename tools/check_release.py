"""Offline sanity checks for staged platform metadata and local inference."""
import argparse,json,subprocess,sys
from pathlib import Path

def check(root):
    root=Path(root)
    for p in root.rglob('README.md'): assert '__HF_OWNER__' not in p.read_text()
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
