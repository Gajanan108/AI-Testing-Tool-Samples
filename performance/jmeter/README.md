# Apache JMeter — Performance and resilience

## Purpose in the framework

JMeter models request flows using test plans, thread groups, samplers, controllers, timers, assertions, configuration elements and listeners. It can measure throughput, response times, errors and behaviour under configured concurrency for supported protocols.

## Assessment method

1. Obtain authorization and define target environment, test window and safe load ceiling.
2. Build a test plan with thread groups, samplers, controllers, timers and assertions representing request flows.
3. Parameterize host, paths, payloads, credentials and test data; keep secrets out of JMX files.
4. Define ramp-up, concurrency, duration, pacing and stop conditions; establish a low-load baseline.
5. Increase load in controlled stages while observing latency percentiles, throughput, errors and infrastructure saturation.
6. Stop at approved thresholds and document workload model, environment and limitations.

## User configuration

- Target host/base URL and request paths
- Threads, ramp-up, duration/loops
- Pacing/timers and request mix
- Payload sizes, test data and authentication
- Assertions and response validation
- Listeners/result format and stop thresholds

## Evidence to retain

- JMX plan and tool version
- Workload profile and environment
- Throughput and p50/p90/p95/p99 latency
- Error rate, assertion failures and response codes
- Resource saturation and stop reason

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| PERF-JM-001 | Baseline request latency | p50/p95/p99 response time | Establish low-concurrency baseline |
| PERF-JM-002 | Step-load concurrency | Throughput, latency and error rate | Identify capacity knee under defined workload |
| PERF-JM-003 | Validate response correctness under load | Assertions and functional error rate | Detect degraded or incorrect responses |

## Sample report

See [sample_report.html](sample_report.html). Static illustrative example only; no execution or measured result is implied.

## Limitations and interpretation

- Results depend on generator capacity, network, environment and workload realism.
- Do not test production or third-party targets without explicit authorization and limits.
- A successful HTTP status does not prove semantic correctness; use assertions.
- Client bottlenecks can distort results; distributed load needs coordinated setup.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in context. Keep execution status separate from finding status. Do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://jmeter.apache.org/
- Documentation: https://jmeter.apache.org/usermanual/
