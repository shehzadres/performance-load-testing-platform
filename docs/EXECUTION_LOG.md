# Execution Log

All figures below are genuine JMeter executions against the local demo API. Transaction Controller rows are reported separately and excluded from HTTP request throughput, request error rate and request latency percentiles.

## Environment

- Date: 12 November 2026
- Device: Dell Latitude 7420
- CPU: Intel Core i7-1185G7, 4 cores / 8 logical processors
- RAM: 15.73 GiB
- OS: Windows 11 Pro 10.0.26300
- Docker Engine: 29.5.3
- Docker Compose: v5.1.4
- JMeter: 5.6.3 (alpine/jmeter:5.6.3)

## Local runs

| Run ID | Scenario | Users | Duration | Request samples | Throughput | p95 | Error rate |
|---|---|---:|---:|---:|---:|---:|---:|
| 20261112-113231-smoke-verified | Smoke | 2 | 10 sec | 403 | 40.312 req/s | 127 ms | 0% |
| 20261112-113312-baseline | Baseline | 10 | 60 sec | 11,191 | 186.265 req/s | 130 ms | 0% |
| 20261112-113430-stress | Stress | 50 | 90 sec | 59,533 | 659.331 req/s | 183 ms | 0% |
| 20261112-113621-baseline-repeat | Baseline repeat | 10 | 60 sec | 11,701 | 194.971 req/s | 130 ms | 0% |

## Repeatability check

The baseline and baseline-repeat used the same 10-user, 60-second profile on the same machine and build.

| Metric | Baseline | Repeat | Change |
|---|---:|---:|---:|
| Throughput | 186.265 req/s | 194.971 req/s | +4.67% |
| Mean latency | 47.59 ms | 46.90 ms | -1.45% |
| p95 latency | 130 ms | 130 ms | 0.00% |
| p99 latency | 140 ms | 138 ms | -1.43% |
| Error rate | 0% | 0% | unchanged |

All measured changes were within the comparator's 5% tolerance. This is a repeatability check between two runs of the same build, not a claim of a software release improvement.

## Stress observations

At 50 virtual users, measured request throughput was 659.331 req/s and request p95 was 183 ms, compared with 186.265 req/s and 130 ms at baseline. No failed HTTP samples were recorded.

The /api/report sampler had the highest stress p95 at 221 ms (baseline 140 ms). A Prometheus CPU query during the stress run returned approximately 0.727 CPU cores in use at that instant. This single sample does not establish CPU saturation.

See BOTTLENECK_ANALYSIS.md for the measured observation and remediation hypothesis.

## Hosted CI smoke

- Workflow run: 43169817342
- Commit: bf83d66
- Environment: GitHub-hosted Actions runner
- Workload: 2 virtual users, 10 seconds
- HTTP request samples: 434
- Transaction samples: 86 (reported separately)
- Throughput: 42.970 req/s
- p95 request latency: 123 ms
- Request error rate: 0%

This hosted-runner measurement is separate from the Dell Latitude local runs and must not be compared directly with them.

## Evidence files

Each local run folder under evidence/local-runs/ contains its raw JTL, JSON summary and Markdown report. The comparison report is stored in evidence/local-runs/comparisons/.

Do not compare unlike workloads as if they were controlled release comparisons. Record the workload, environment and host resource conditions with every benchmark.
