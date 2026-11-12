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
- Containerized JMeter 5.6.3 smoke, baseline, stress and baseline-repeat profiles completed.
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

- Public repository: https://github.com/shehzadres/performance-load-testing-platform
- Final showcase commit: 1a5f432
- GitHub Actions run 43170474335: SUCCESS.
- All five jobs passed: Python analysis tests, API contract tests, Compose configuration, Docker/Prometheus/Grafana/JMeter integration, and recruiter showcase deployment.
- Hosted CI smoke: 437 request samples, 43.556 req/s, p95 123 ms, 0% errors; 87 transaction samples reported separately.
- GitHub Pages recruiter showcase returned HTTP 200 and displays the corrected CI smoke summary: https://shehzadres.github.io/performance-load-testing-platform/
- CI raw JTL, JSON and Markdown report are preserved in evidence/ci-smoke/.

## Scope limitations

This is a local performance-engineering lab using a synthetic API. Results describe the recorded test plan and host only. No production deployment, production capacity guarantee or public-target stress test is claimed.
