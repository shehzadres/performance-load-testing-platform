# Continuation Context

Project: 04 - Performance & Load Testing Platform
Location: D:\SQA-Portfolio\04-Performance-Load-Testing-Platform
GitHub: https://github.com/shehzadres/performance-load-testing-platform
Recruiter showcase: https://shehzadres.github.io/performance-load-testing-platform/

## Stack
Node.js 22 + Express + prom-client; Apache JMeter 5.6.3 (alpine/jmeter:5.6.3); Docker Compose; Prometheus 3.1.0; Grafana 11.4.0; Python analyzer; PowerShell scripts.

## Completed
- Public GitHub repository created and pushed.
- GitHub Pages enabled and recruiter showcase deployed with latest CI smoke metrics and local baseline/stress comparison visuals.
- Final GitHub Actions run 43169817342 passed all five jobs.
- Pages URL returned HTTP 200 and displayed the latest CI smoke summary.
- Local API, Prometheus target and Grafana dashboard verified.
- API host port is 18080 because port 8080 was already occupied; container API port remains 8080.
- JMeter plan has five HTTP samplers and five response-code assertions, including checkout POST.
- Transaction Controller is named Transaction: API Journey; analyzer separates transaction rows from HTTP request statistics.
- Grafana dashboard has seven panels including CPU and memory.
- Seven Node API contract tests and eight Python/JMeter regression tests pass.
- Local JMeter smoke, baseline, stress and baseline-repeat runs completed with zero failed request samples.
- Local evidence is stored in evidence/local-runs/.
- Hosted CI smoke evidence is stored in evidence/ci-smoke/.

## Local results
- Smoke: 2 users / 10 sec, 403 requests, 40.312 req/s, p95 127 ms, 0% errors.
- Baseline: 10 users / 60 sec, 11,191 requests, 186.265 req/s, p95 130 ms, 0% errors.
- Stress: 50 users / 90 sec, 59,533 requests, 659.331 req/s, p95 183 ms, 0% errors.
- Baseline repeat: 10 users / 60 sec, 11,701 requests, 194.971 req/s, p95 130 ms, 0% errors.
- Same-workload baseline repeat deltas all within 5%.
- See docs/BOTTLENECK_ANALYSIS.md for the measured report-route degradation and remediation hypothesis.

## Final status
Project 04 has been published and verified. Future work can focus on an actual worker-thread remediation experiment and longer endurance testing, rather than repository-readiness blockers.
