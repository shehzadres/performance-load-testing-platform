# Performance Test Report: ci-smoke

- Environment: github-actions
- Generated: 2026-11-12T06:47:21.473236+00:00
- Request samples: 437
- Transaction samples: 87
- Successful requests: 437
- Failed requests: 0
- Request error rate: 0.0%
- Request throughput: 43.556 req/s
- Wall time: 10.033 sec

## Request response time (ms)

| Metric | Value |
|---|---:|
| min | 0 |
| mean | 44.16 |
| median | 36.0 |
| p90 | 122.0 |
| p95 | 123.0 |
| p99 | 123.0 |
| max | 129 |

## Transaction response time (ms)

| Metric | Value |
|---|---:|
| min | 217 |
| mean | 221.62 |
| median | 221.0 |
| p90 | 223.0 |
| p95 | 224.0 |
| p99 | 234.82 |
| max | 289 |

## Request sampler breakdown

| Sampler | Samples | Errors | Mean ms | p95 ms |
|---|---:|---:|---:|---:|
| Checkout | 87 | 0 | 46.4 | 47.0 |
| Health Check | 88 | 0 | 1.28 | 1.0 |
| List Products | 88 | 0 | 15.72 | 17.0 |
| Search | 87 | 0 | 35.82 | 37.0 |
| Variable Cost Report | 87 | 0 | 122.4 | 123.0 |

## Investigation notes
- Transaction Controller rows are reported separately and excluded from request throughput to avoid double-counting.
- Correlate slow samplers with Grafana route latency and process metrics.
- Verify the JMeter generator and Docker host are not saturated.
- Treat these results as valid only for the recorded workload and environment.
