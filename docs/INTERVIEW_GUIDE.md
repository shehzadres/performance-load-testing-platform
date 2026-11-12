# Interview Guide

**Load vs stress:** Load testing measures expected/peak traffic; stress testing pushes beyond capacity to find saturation, failure behavior and recovery.

**Virtual user:** A simulated thread executing a request journey. It is not automatically equivalent to a real human user; think time, sessions and request mix matter.

**Why p95?** Average latency hides slow-tail behavior. p95 means 95% of samples completed at or below that latency.

**Throughput:** Completed requests per unit time. Interpret with latency and errors; high throughput with high failure rate is not success.

**Bottleneck diagnosis:** Correlate latency, throughput, errors, concurrency and resources. Rule out load-generator and host saturation.

**Release comparison:** Control workload shape, data, duration, host resources and environment to reduce confounding variables.

**Prometheus/Grafana:** Prometheus scrapes and stores time-series metrics; Grafana queries and visualizes dashboards and alerts.

**JTL:** JMeter result file containing sample-level timestamps, elapsed time, labels, response codes and success status.
