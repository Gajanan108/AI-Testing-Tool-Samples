# Elastic Security — Security analytics and incident response

## Purpose in the framework

Elastic Security provides SIEM detection and investigation workflows over data ingested into Elasticsearch. It supports prebuilt and custom detection rules, alerts, timelines, cases and integrations. AI environments can correlate gateway, identity, application and infrastructure events when collected and normalized.

## Assessment method

1. Define AI service telemetry and threat scenarios; identify required event fields and data sources.
2. Ingest synthetic or authorized sanitized events using suitable Elastic integrations or pipelines.
3. Map events to applicable schemas/fields and verify timestamps, identity and correlation identifiers.
4. Review relevant prebuilt rules and create environment-specific detection rules for AI-service threats.
5. Validate rule logic against historical or synthetic known-positive/negative events before enabling production alerting.
6. Tune exceptions, suppression, schedules, severity and response ownership; use Timeline/Cases for investigation.

## User configuration

- Elastic deployment/version and enabled Security features
- Data sources, integrations and event schema
- Index/data stream and field mappings
- Prebuilt/custom rule selection and query logic
- Rule schedule, threshold, severity and exceptions
- Alert routing, cases and retention/access controls

## Evidence to retain

- Ingested synthetic event examples and source list
- Rule identifiers, query logic and configuration
- Validation results and generated alerts
- Timeline/case references and investigation notes
- Rule execution health, tuning and coverage gaps

## Example test catalogue

| Test ID | Objective | Evidence | Example interpretation |
|---|---|---|---|
| SIEM-EL-001 | Detect anomalous model/API access | Rule match and generated alert | Identify access inconsistent with defined baseline |
| SIEM-EL-002 | Detect repeated AI policy violations | Event correlation and alert | Surface repeated policy-trigger events for investigation |
| SIEM-EL-003 | Validate incident workflow | Timeline and case evidence | Demonstrate alert triage, ownership and resolution recording |

## Sample report

See [sample_report.html](sample_report.html). This is a static illustrative example, not an executed assessment or measured result.

## Limitations and interpretation

- Detection requires relevant telemetry to be ingested and correctly mapped.
- Prebuilt rules may require integration-specific fields and tuning.
- An alert indicates a rule condition, not confirmed compromise or AI-specific vulnerability.
- Features vary by deployment, license and version; verify applicability.

Tool output is an observation. A confirmed finding requires reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://github.com/elastic/kibana
- Documentation: https://www.elastic.co/docs/solutions/security
