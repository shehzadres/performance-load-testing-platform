# Performance Evidence

## Local execution evidence

The local-runs/ folders contain raw JMeter JTL files, analyzer JSON summaries and Markdown reports generated on the Dell Latitude 7420 test machine on 12 November 2026.

- Smoke: 2 virtual users / 10 seconds.
- Baseline: 10 virtual users / 60 seconds.
- Stress: 50 virtual users / 90 seconds.
- Baseline repeat: 10 virtual users / 60 seconds.
- comparisons/ contains the same-workload repeatability comparison.

These are measurements of the synthetic local API on the recorded host. They are not production capacity guarantees.

## CI evidence

The GitHub Actions integration workflow runs a separate short smoke test on a hosted runner and uploads its raw JTL, JSON and Markdown report as a workflow artifact. CI-runner measurements must not be mixed with local laptop measurements.
