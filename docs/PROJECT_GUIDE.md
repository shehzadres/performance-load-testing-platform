# Project Guide

## Objective
Demonstrate the complete performance-engineering workflow: plan, execute, observe, analyze, diagnose and compare.

## System under test
- GET /health: readiness.
- GET /api/products: product listing.
- GET /api/search: configurable I/O delay.
- GET /api/report: configurable delay plus bounded CPU work.
- POST /api/checkout: JSON request handling.
- GET /metrics: Prometheus exposition endpoint.

## Observability
Prometheus scrapes every five seconds. Grafana provisions Prometheus as its default datasource and imports the API health dashboard. Dashboard panels include request rate, p95 latency, 5xx rate, in-flight requests, process memory and route traffic.

## Bottleneck method
1. Capture a baseline with a documented workload.
2. Increase virtual users gradually.
3. Correlate p95/p99 latency, throughput, errors, in-flight requests and process CPU/memory.
4. Rule out load-generator, network and Docker-host saturation.
5. Identify the slowest sampler/route and form a hypothesis.
6. Change one variable, repeat and compare.

## Portfolio evidence
Preserve raw JTL, JSON summary, Markdown report, Grafana screenshots and a measured root-cause analysis. Never invent performance findings.
