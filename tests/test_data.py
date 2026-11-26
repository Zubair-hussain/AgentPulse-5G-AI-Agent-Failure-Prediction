import pandas as pd
from agentpulse.generate import generate_shard
from agentpulse.schema import FEATURES
from tools.validate_data import validate

def test_manifest(): validate('data/demo')
def test_deterministic(): pd.testing.assert_frame_equal(generate_shard(32,3),generate_shard(32,3))
def test_disjoint_cohorts():
    groups=[set(generate_shard(100,s).environment_id) for s in [0,1,2]]
    assert all(not a&b for i,a in enumerate(groups) for b in groups[i+1:])
def test_no_target_leakage(): assert not {'failed','run_id','environment_id','split'}&set(FEATURES)
