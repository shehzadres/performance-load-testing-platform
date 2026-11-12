# QA / Build Verification Report

## Automated and static checks

| Check | Result |
|---|---|
| Python analyzer and comparison syntax | PASS |
| Python unit / CLI / JMeter-plan tests | PASS: 8 tests |
| Node.js API contract tests | PASS: 7 tests |
| Grafana dashboard JSON parse | PASS |
| JMeter XML parse | PASS |
| JMeter HTTP samplers | PASS: 5 |
| JMeter response-code assertions | PASS: 5 |
| Docker Compose configuration | PASS |
| npm lockfile and clean install | PASS |
| Git secret-pattern scan | PASS: no high-confidence token/private-key patterns |

## Local runtime verification

- Docker Engine 29.5.3 and Compose v5.1.4 are running.
- API health endpoint passed on host port 18080.
- Prometheus API target performance-lab-api reported UP.
- Grafana provisioned dashboard loaded successfully.
- Dashboard API confirmed seven panels, including API process CPU and memory.
- Containerized JMeter 5.6.3 smoke, baseline and stress profiles completed.
- Five HTTP routes were exercised, including checkout POST with expected HTTP 201 assertion.
- The analyzer separates transaction-controller rows from HTTP request statistics.

## Measured local runs

| Scenario | Users | Duration | Request samples | Throughput | p95 | Errors |
|---|---:|---:|---:|---:|---:|---:|
| Smoke | 2 | 10 sec | 403 | 40.312 req/s | 127 ms | 0% |
| Baseline | 10 | 60 sec | 11,191 | 186.265 req/s | 130 ms | 0% |
| Stress | 50 | 90 sec | 59,533 | 659.331 req/s | 183 ms | 0% |
| Baseline repeat | 10 | 60 sec | 11,701 | 194.971 req/s | 130 ms | 0% |

The repeated baseline comparison showed all measured changes within 5%. See docs/EXECUTION_LOG.md and docs/BOTTLENECK_ANALYSIS.md.

## GitHub verification

- Public repository created and pushed.
- GitHub Actions first integration run completed successfully, including Docker, Prometheus, Grafana and a real JMeter smoke workload.
- GitHub Pages recruiter showcase deployed and returned HTTP 200.
- A subsequent commit added JMeter plan regression tests and its workflow completed successfully.

A final workflow run is required after the latest analyzer/JMeter/dashboard changes are pushed. Its result and updated CI evidence will be recorded separately.

## Remaining publication checks

- Verify the latest GitHub Actions run after the final code changes.
- Verify the Pages showcase refreshes with the corrected JMeter transaction-aware summary.
- No production deployment or public-target stress test is claimed.
