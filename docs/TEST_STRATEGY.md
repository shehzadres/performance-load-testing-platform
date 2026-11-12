# Performance Test Strategy

## Test types

| Type | Goal | Suggested workload |
|---|---|---|
| Smoke | Verify the test path | 2 users, 10 sec |
| Baseline | Normal behavior reference | 10 users, 60 sec |
| Load | Expected traffic | 25 users, 120 sec |
| Stress | Explore saturation | 50 users, 90 sec |
| Spike | Observe sudden arrival | 75 users, short ramp |
| Endurance | Detect resource growth | 15 users, 15 min |

## API coverage

The JMeter journey covers health, product listing, search, variable-cost report generation and checkout. Response assertions should validate expected HTTP status codes and prevent error responses from being counted as successful transactions.

## Measurements

Response-time mean/median/p90/p95/p99; throughput in completed samples/sec; error rate; configured virtual users; in-flight requests; Node process CPU and resident memory.

## Bottleneck signals

Rising latency with flat/falling throughput, growing errors, high in-flight requests, CPU saturation or memory growth. Check the load generator before blaming the application.

## Example acceptance criteria

Illustrative only: p95 below 500ms under agreed load; error rate below 1% at normal load; no sustained throughput collapse; no unbounded memory growth during endurance testing. Agree SLOs with the product owner before treating these as release gates.

Only test authorized systems. Do not point stress profiles at public endpoints.
