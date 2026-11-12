# Bottleneck Analysis

## Test context

The local demo API was exercised with the same five-request JMeter journey at 10 virtual users (baseline) and 50 virtual users (stress). Both runs used the same build and host.

| Measurement | Baseline | Stress |
|---|---:|---:|
| Virtual users | 10 | 50 |
| Duration | 60 sec | 90 sec |
| Request throughput | 186.265 req/s | 659.331 req/s |
| Overall request p95 | 130 ms | 183 ms |
| Request error rate | 0% | 0% |
| /api/report p95 | 140 ms | 221 ms |
| /api/checkout p95 | 64 ms | 151 ms |

## Finding

The report route was the slowest request sampler under both workloads. Its p95 increased by 57.9% from baseline to stress. Checkout p95 also increased under concurrency. The API continued to return successful responses, so this workload showed latency degradation rather than an error-rate failure.

A Prometheus CPU query during the stress run returned approximately 0.727 CPU cores in use at one instant. That is not evidence of sustained CPU saturation. Queueing, concurrency and the deliberately configured I/O/CPU work in the report route are plausible contributors, but the available sample does not prove a single root cause.

## Candidate remediation

For a production-like CPU-bound route, move expensive report computation to a worker-thread pool or background job queue, bound concurrency, and return an operation identifier for longer work. Preserve the current synthetic delay/work controls in this lab so the workload remains repeatable.

## How to validate a remediation

1. Change one implementation variable at a time.
2. Run the same 50-user workload, ramp-up, duration and test data on the same host.
3. Compare per-sampler p95/p99, throughput, error rate and process CPU/memory.
4. Confirm the load generator is not saturated.
5. Accept the remediation only if repeated runs show a consistent improvement without new errors.

No remediation is claimed as implemented or measured in this report. This is a measured bottleneck observation with a proposed next experiment.
