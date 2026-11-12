# CI Integration

The GitHub Actions workflow validates source and configuration, then performs a containerized integration smoke test.

## Automated checks

1. Compile Python modules and run analyzer unit tests.
2. Install locked Node dependencies and run API contract tests.
3. Validate Docker Compose configuration.
4. Build and start the API, Prometheus and Grafana services.
5. Verify API health, Prometheus scrape target and provisioned Grafana dashboard.
6. Run a short JMeter workload against the local demo API.
7. Analyze the real JTL file and upload raw results, JSON summary and Markdown report as a workflow artifact.
8. On successful pushes to `main`, publish the recruiter showcase to GitHub Pages with the CI smoke summary.

## Why only a smoke test?

Long stress and endurance runs are not suitable for every pull request. Shared CI runners have variable CPU and memory. Keep longer profiles manual or scheduled and record runner context for fair comparisons.

## Local equivalent

```powershell
python -m unittest discover -s analysis/tests -v
npm --prefix app ci
npm --prefix app test
docker compose config --quiet
.\scripts\start-platform.ps1
.\scripts\run-test.ps1 -Users 2 -RampUp 1 -Duration 10 -Label smoke
```

## Published evidence

The GitHub Actions artifact contains the raw JTL, JSON summary and Markdown report. The Pages showcase displays the measured CI smoke summary and identifies its environment as GitHub Actions. It is not a substitute for a local baseline or stress benchmark.
