# Continuation Context

Project: 04 - Performance & Load Testing Platform
Location: D:\SQA-Portfolio\04-Performance-Load-Testing-Platform
GitHub: https://github.com/shehzadres/performance-load-testing-platform
Recruiter showcase: https://shehzadres.github.io/performance-load-testing-platform/

## Stack
Node.js 22 + Express + prom-client; Apache JMeter 5.6.3 (alpine/jmeter:5.6.3); Docker Compose; Prometheus 3.1.0; Grafana 11.4.0; Python analyzer; PowerShell scripts.

## Completed
- Public GitHub repository created and pushed; Pages enabled.
- Local API, Prometheus target and Grafana dashboard verified.
- API host port is 18080 because port 8080 was already occupied; container API port remains 8080.
- JMeter plan has five HTTP samplers and five response-code assertions, including checkout POST.
- Transaction Controller is named Transaction: API Journey; analyzer separates transaction rows from HTTP request statistics.
- Grafana dashboard has seven panels including CPU and memory.
- Seven Node API contract tests and eight Python/JMeter regression tests pass.
- Local JMeter smoke, baseline, stress and baseline-repeat runs completed with zero failed request samples.
- Local evidence copied to evidence/local-runs/.
- CI integration and Pages deployment succeeded on the first public push; a subsequent test-only commit also passed.

## Local results
- Smoke: 2 users / 10 sec, 403 requests, 40.312 req/s, p95 127 ms, 0% errors.
- Baseline: 10 users / 60 sec, 11,191 requests, 186.265 req/s, p95 130 ms, 0% errors.
- Stress: 50 users / 90 sec, 59,533 requests, 659.331 req/s, p95 183 ms, 0% errors.
- Baseline repeat: 10 users / 60 sec, 11,701 requests, 194.971 req/s, p95 130 ms, 0% errors.
- Same-workload baseline repeat deltas all within 5%.
- See docs/BOTTLENECK_ANALYSIS.md for the measured report-route degradation and remediation hypothesis.

## Remaining
1. Commit and push the final JMeter/analyzer/dashboard/docs/evidence changes.
2. Verify the latest GitHub Actions integration and Pages deployment.
3. Download the latest CI smoke artifact into evidence/ci-smoke/.
4. Confirm the live showcase displays the latest corrected CI smoke summary.
5. Update QA_REPORT and ROADMAP with final workflow outcome.
