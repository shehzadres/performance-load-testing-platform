# Release Performance Comparison

- Generated: 2026-11-12T06:37:37.594615+00:00
- Baseline: 20261112-113312-baseline
- Candidate: 20261112-113621-baseline-repeat

| Metric | Baseline | Candidate | Change | Assessment |
|---|---:|---:|---:|---|
| Throughput (req/s) | 186.265 | 194.971 | +4.67% | Within 5% |
| Mean response time (ms) | 47.59 | 46.9 | -1.45% | Within 5% |
| p95 response time (ms) | 130.0 | 130.0 | +0.00% | Within 5% |
| p99 response time (ms) | 140.0 | 138.0 | -1.43% | Within 5% |
| Error rate (%) | 0.0 | 0.0 | N/A | N/A |

## Summary
- Regressions detected: 0
- Positive latency/error-rate change is a regression; positive throughput change is generally an improvement.
- Workload, test data, host resources and duration must be controlled for a fair comparison.
