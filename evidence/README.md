# Performance Evidence

## Local execution evidence

The local-runs/ folders contain raw JMeter JTL files, analyzer JSON summaries and Markdown reports generated on the Dell Latitude 7420 test machine on 12 November 2026.

- Smoke: 2 virtual users / 10 seconds.
- Baseline: 10 virtual users / 60 seconds.
- Stress: 50 virtual users / 90 seconds.
- Baseline repeat: 10 virtual users / 60 seconds.
- comparisons/ contains the same-workload repeatability comparison.

These are measurements of the synthetic local API on the recorded host. They are not production capacity guarantees.

## GitHub Actions evidence

Workflow run 43169817342 on the GitHub-hosted runner completed a real 2-user, 10-second JMeter smoke test:

- 434 HTTP request samples.
- 42.970 requests/second.
- p95 request latency: 123 ms.
- Request error rate: 0%.
- 86 transaction samples reported separately.

The raw JTL, JSON summary and Markdown report are stored in ci-smoke/. CI-runner measurements must not be mixed with local laptop measurements.
