# Locust — Performance and resilience

## Purpose in the framework

Locust is a Python-based load-testing framework. User classes and task definitions model client behaviour; wait times, task weights and load shapes control request patterns. It reports request counts, response times, failures and throughput.

## Assessment method

1. Define representative user journeys and the authorized target environment/load envelope.
2. Model user classes, tasks, request headers/payloads and wait-time behaviour.
3. Parameterize host, credentials, test data and concurrency; store secrets outside source files.
4. Choose user count, spawn rate, duration and optional load shape; establish baseline.
5. Increase load in controlled stages and observe response-time percentiles, throughput and failures.
6. Stop at approved limits and preserve configuration and statistics.

## User configuration

- Host/base URL and request paths
- User classes, task mix and weights
- Wait-time distribution and load shape
- Users, spawn rate and duration
- Authentication, test data and payloads
- Failure classification and stop thresholds

## Evidence to retain

- Locustfile and tool version
- User/task mix and load profile
- Requests per second and response-time percentiles
- Failure count/rate and details
- Environment metrics and stop reason

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| PERF-LOC-001 | Simulate representative user journeys | Requests/sec and response-time percentiles | Measure baseline user experience |
| PERF-LOC-002 | Apply controlled ramp-up | Latency, throughput and failures by load step | Identify saturation/degradation point |
| PERF-LOC-003 | Exercise error handling | Expected versus unexpected failures | Check graceful behaviour and recovery |

## Sample report

See [sample_report.html](sample_report.html). Static illustrative example only; no execution or measured result is implied.

## Limitations and interpretation

- Workload realism depends on task modelling.
- Generator CPU/network limits can distort results.
- Do not stress production or external systems without authorization.
- Application response validation is needed; request success alone is insufficient.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in context. Keep execution status separate from finding status. Do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://github.com/locustio/locust
- Documentation: https://docs.locust.io/
