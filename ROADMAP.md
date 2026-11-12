# Project Roadmap

## Phase 1: Core implementation
- [x] Instrumented demo API
- [x] Docker Compose stack
- [x] JMeter test plan with five HTTP samplers
- [x] Checkout POST and response-code assertions
- [x] Prometheus scrape config and alert rules
- [x] Grafana provisioned dashboard with CPU and memory panels
- [x] JTL analyzer and release comparison
- [x] Transaction samples separated from request throughput
- [x] PowerShell operator scripts
- [x] Architecture, project and interview documentation
- [x] API contract tests
- [x] Python analyzer and JMeter-plan regression tests
- [x] GitHub Actions workflow
- [x] Recruiter-facing showcase and GitHub Pages deployment
- [x] Static validation

## Phase 2: Runtime verification
- [x] Docker Compose services started and health-checked
- [x] Verify API health and all API routes
- [x] Verify Prometheus target is UP
- [x] Verify Grafana datasource and provisioned dashboard
- [x] Run a containerized JMeter smoke test
- [x] Run baseline and stress profiles
- [x] Inspect generated JTL, JSON and Markdown artifacts
- [x] Verify showcase consumes generated run summaries

## Phase 3: Portfolio evidence and publication
- [x] Preserve raw JTL, JSON and Markdown run evidence
- [x] Record real metrics in docs/EXECUTION_LOG.md
- [x] Run a same-workload baseline repeatability comparison
- [x] Document measured stress degradation and a remediation hypothesis
- [x] Create and publish the GitHub repository
- [x] Publish the recruiter showcase through GitHub Pages
- [ ] Verify the latest CI run after final analyzer/JMeter/dashboard updates
