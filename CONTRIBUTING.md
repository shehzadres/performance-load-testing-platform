# Contributing

## Local setup

1. Install Docker Desktop / Docker Engine and Python 3.10+.
2. Clone the repository.
3. Start the local stack with `scripts/start-platform.ps1`.
4. Run the smoke profile before changing the JMeter plan.

## Quality expectations

- Keep test targets limited to the local demo API unless written authorization exists.
- Add or update API tests when routes or response contracts change.
- Keep JMeter assertions aligned with the API contract.
- Never commit credentials, environment files, generated JTL files or fabricated benchmark results.
- Record actual execution settings and machine context when publishing measurements.
- Run Python tests and Docker Compose validation before opening a pull request.

## Pull requests

Include a concise problem statement, implementation summary, verification commands and any relevant screenshots or report artifacts.
