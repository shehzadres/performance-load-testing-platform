# Project Roadmap

## Phase 1: Core implementation
- [x] Instrumented demo API
- [x] Docker Compose stack
- [x] JMeter test plan
- [x] JMeter response-code assertions and checkout POST journey
- [x] Prometheus scrape config and alert rules
- [x] Grafana provisioned dashboard
- [x] JTL analyzer and release comparison
- [x] PowerShell operator scripts
- [x] Architecture and project documentation
- [x] API contract tests
- [x] Python analyzer unit tests
- [x] GitHub Actions quality workflow
- [x] Recruiter-facing visual showcase
- [x] Static validation

## Phase 2: Runtime verification
- [ ] Finish Docker image downloads and start services
- [ ] Verify API health and all API routes in Compose
- [ ] Verify Prometheus target is UP
- [ ] Verify Grafana datasource and provisioned dashboard
- [ ] Run a containerized JMeter smoke test
- [ ] Run baseline and stress profiles
- [ ] Inspect generated JTL, JSON and Markdown artifacts
- [ ] Verify showcase loads a real run summary

## Phase 3: Portfolio evidence and publication
- [ ] Capture baseline and stress Grafana screenshots
- [ ] Record actual metrics in docs/EXECUTION_LOG.md
- [ ] Run a controlled release comparison
- [ ] Document one measured bottleneck and remediation
- [ ] Verify GitHub Actions on the published repository
- [ ] Create and publish the GitHub repository
- [ ] Verify README rendering and showcase links
