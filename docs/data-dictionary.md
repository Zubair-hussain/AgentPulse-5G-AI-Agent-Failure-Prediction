# Data dictionary
Each row is a simulated pre-outcome run snapshot. IDs and split are metadata, not model inputs. No time horizon is calibrated to real agents. Ratios are bounded [0,1].

| Column | Meaning | Unit |
|---|---|---|
| run_id | Unique synthetic seed/shard/row identifier | string |
| environment_id | Synthetic cohort, disjoint across splits | integer |
| split | train, validation or test | string |
| elapsed_ms | elapsed time at snapshot | milliseconds |
| input_tokens | consumed input tokens | count |
| output_tokens | emitted output tokens so far | count |
| tool_calls | tool calls so far | count |
| retry_count | observed retries | count |
| queue_ms | queue wait | milliseconds |
| rate_limit_ratio | rate-limited call fraction | ratio |
| tool_error_ratio | tool error fraction | ratio |
| context_utilization | context budget used | ratio |
| cpu_utilization | CPU load | ratio |
| memory_utilization | memory load | ratio |
| retrieval_score | simulated retrieval quality proxy | ratio |
| budget_utilization | execution budget consumed | ratio |
| network_jitter_ms | jitter proxy | milliseconds |
| concurrency | concurrent work proxy | count |
| step_count | completed steps so far | count |
| failed | stochastic eventual failure | binary label |

Ratios and counts are simulated proxies, not measurements from actual LLM providers. See generator for exact distributions.
