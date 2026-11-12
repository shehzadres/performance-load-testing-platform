# Architecture

## Components

| Component | Responsibility |
|---|---|
| Node.js / Express | Deterministic demo API with bounded latency and CPU-work controls |
| prom-client | HTTP request counter, latency histogram, in-flight gauge and process metrics |
| Apache JMeter | Concurrent virtual-user request journey and raw CSV JTL output |
| Prometheus | Five-second scrape interval and alert evaluation |
| Grafana | Provisioned Prometheus datasource and performance dashboard |
| Python analyzer | Percentiles, throughput, error rate and sampler breakdown |
| PowerShell scripts | Repeatable lifecycle, workload, analysis and comparison commands |

## Data flow

1. JMeter sends a parameterized workload to the local API over the Docker network.
2. The API records request count, duration and in-flight concurrency.
3. Prometheus scrapes the API's `/metrics` endpoint.
4. Grafana queries Prometheus for latency, throughput, error and process metrics.
5. JMeter writes sample-level results to a CSV JTL file.
6. Python converts the JTL into a JSON summary and Markdown report.
7. The comparison tool evaluates two runs across throughput, mean, p95, p99 and error rate.

The JMeter plan wraps the five HTTP samplers in a Transaction Controller named `Transaction: API Journey`. The analyzer reports those journey timings separately and excludes transaction rows from request throughput, request error rate and request percentiles so the same journey is not counted twice.

## Reliability boundaries

- The API is a synthetic system under test, not a real commerce service.
- JMeter virtual users are not equivalent to real human sessions unless think time, state and realistic journeys are modeled.
- Load-generator and Docker-host saturation can distort results.
- Comparisons require equivalent workload, duration, data, host resources and environment.
- Grafana credentials and ports are for local development. Do not expose this configuration publicly without hardening.
