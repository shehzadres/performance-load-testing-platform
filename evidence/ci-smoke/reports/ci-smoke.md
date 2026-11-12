# Performance Test Report: ci-smoke

- Environment: github-actions
- Generated: 2026-11-12T06:41:45.689129+00:00
- Request samples: 434
- Transaction samples: 86
- Successful requests: 434
- Failed requests: 0
- Request error rate: 0.0%
- Request throughput: 42.97 req/s
- Wall time: 10.1 sec

## Request response time (ms)

| Metric | Value |
|---|---:|
| min | 0 |
| mean | 44.59 |
| median | 36.0 |
| p90 | 123.0 |
| p95 | 123.0 |
| p99 | 124.0 |
| max | 127 |

## Transaction response time (ms)

| Metric | Value |
|---|---:|
| min | 219 |
| mean | 222.98 |
| median | 222.0 |
| p90 | 225.0 |
| p95 | 225.0 |
| p99 | 234.35 |
| max | 276 |

## Request sampler breakdown

| Sampler | Samples | Errors | Mean ms | p95 ms |
|---|---:|---:|---:|---:|
| Checkout | 86 | 0 | 46.62 | 47.75 |
| Health Check | 87 | 0 | 1.29 | 1.0 |
| List Products | 87 | 0 | 15.93 | 17.0 |
| Search | 87 | 0 | 36.24 | 38.0 |
| Variable Cost Report | 87 | 0 | 122.92 | 124.0 |

## Investigation notes
- Transaction Controller rows are reported separately and excluded from request throughput to avoid double-counting.
- Correlate slow samplers with Grafana route latency and process metrics.
- Verify the JMeter generator and Docker host are not saturated.
- Treat these results as valid only for the recorded workload and environment.
