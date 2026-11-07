# Splunk — Security analytics and incident response

## Purpose in the framework

Splunk Enterprise and Splunk Cloud Platform provide search, analysis, dashboards and alerting over ingested machine data. For AI security monitoring, an authorized deployment can ingest model gateway, API, identity, application, safety-filter and infrastructure events and correlate them using SPL.

## Assessment method

1. Define telemetry sources and event schema for AI components, including model/API identity, request correlation ID, policy decision, latency, token usage and error category where appropriate.
2. Use synthetic events or authorized sanitized telemetry; do not ingest secrets or raw sensitive prompts by default.
3. Confirm indexes, sourcetypes, timestamps, field extraction and retention policy.
4. Develop SPL searches for suspicious patterns such as repeated policy denials, anomalous request volume, unusual model access or sensitive-data detector events.
5. Build dashboards and alert conditions with suppression, thresholds and routing to an approved response process.
6. Validate searches against known-positive and known-negative synthetic events; document gaps and ownership.

## User configuration

- Splunk deployment and authorized access
- Data inputs, index, sourcetype and field schema
- Timestamp and correlation fields
- SPL search and time window
- Alert schedule, threshold, suppression and action
- Retention, access control and masking policy

## Evidence to retain

- Synthetic event schema and sample events
- SPL query and search time range
- Search results and alert configuration
- Dashboard panels and correlation logic
- Data source coverage, retention and access-control notes

## Example test catalogue

| Test ID | Objective | Evidence | Example interpretation |
|---|---|---|---|
| SIEM-SPL-001 | Detect repeated blocked prompt-injection events | SPL results grouped by identity/time | Identify repeated policy-trigger patterns |
| SIEM-SPL-002 | Detect unusual API/model access | Identity, source and time-window correlation | Flag access outside expected baseline |
| SIEM-SPL-003 | Correlate sensitive-data alerts with model requests | Correlation ID and event sequence | Support incident timeline and triage |

## Sample report

See [sample_report.html](sample_report.html). This is a static illustrative example, not an executed assessment or measured result.

## Limitations and interpretation

- Splunk is an analytics/monitoring platform, not an AI model scanner by itself.
- Detection depends on telemetry completeness, normalization, search logic and tuning.
- Sensitive prompts/outputs require minimization, redaction and governance.
- An alert is an investigation lead, not proof of malicious activity.

Tool output is an observation. A confirmed finding requires reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://www.splunk.com/
- Documentation: https://docs.splunk.com/
