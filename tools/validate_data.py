"""Verify manifest, hashes, schema, split and range constraints one shard at a time."""
import argparse,hashlib,json
from pathlib import Path
import pandas as pd
from agentpulse.schema import FEATURES,RANGES,SPLITS

def validate(root):
    root=Path(root); m=json.loads((root/'manifest.json').read_text()); total=0; size=0
    assert m['synthetic'] is True
    assert len({s['file'] for s in m['shards']})==len(m['shards'])
    for s in m['shards']:
        p=root/s['file']; assert p.is_file() and p.stat().st_size==s['bytes']
        with p.open('rb') as f: assert hashlib.file_digest(f,'sha256').hexdigest()==s['sha256']
        d=pd.read_csv(p) if p.suffix=='.csv' else pd.read_parquet(p)
        assert list(d)==['run_id','environment_id','split',*FEATURES,'failed']
        assert len(d)==s['rows'] and d.run_id.is_unique and not d.isna().any().any()
        shard=int(p.stem.rsplit('-',1)[1]); assert d.run_id.str.startswith(f"{m['seed']}-{shard:05d}-").all()
        assert set(d.split)=={s['split']} and set(d.failed)<= {0,1} and d.failed.sum()==s['positive']
        assert set(d.environment_id//12)=={SPLITS[s['split']]}
        for k,(lo,hi) in RANGES.items():
            assert d[k].ge(lo).all()
            if hi is not None: assert d[k].le(hi).all()
        total+=len(d); size+=p.stat().st_size
    assert total==m['rows'] and size==m['bytes']
    print(f'Validated {total:,} rows across {len(m["shards"])} shards, {size:,} bytes')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('root',nargs='?',default='data/demo');validate(p.parse_args().root)
