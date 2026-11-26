FEATURES = ['elapsed_ms','input_tokens','output_tokens','tool_calls','retry_count','queue_ms','rate_limit_ratio','tool_error_ratio','context_utilization','cpu_utilization','memory_utilization','retrieval_score','budget_utilization','network_jitter_ms','concurrency','step_count']
TARGET = 'failed'
SPLITS = {'train': 0, 'validation': 1, 'test': 2}
RANGES = {k:(0,None) for k in FEATURES}
for k in ['rate_limit_ratio','tool_error_ratio','context_utilization','cpu_utilization','memory_utilization','retrieval_score','budget_utilization']: RANGES[k]=(0,1)
