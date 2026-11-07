# Tool integration method

## Purpose

This repository demonstrates how external tools can support the AI Security Testing Framework. It is designed to communicate achievable assessment coverage and provide a starting point for users to configure their own tests. It is not intended to be a preconfigured universal scanner.

## Standard workstream structure

Each tool's directory should document:

1. **Purpose and assurance area** — which framework objective the tool supports.
2. **Capabilities** — concrete test activities the upstream tool can perform.
3. **Applicability** — supported model types, interfaces, data formats, deployment assumptions and exclusions.
4. **Method** — test objective, threat assumptions, baseline, procedure and expected observations.
5. **Configuration** — user-supplied model/system identifier, endpoint or local model path, credentials via environment variables or secret manager, dataset, language, thresholds, attack/probe selection, rate limits and output location.
6. **Sample fixtures** — synthetic or explicitly authorised inputs with expected behaviour.
7. **Evidence** — tool/version, configuration, invocation, timestamps, output references, logs, exceptions and reproducibility notes.
8. **Sample report** — a clearly labelled illustrative report showing the fields and presentation users can populate with their own results.
9. **Limitations and safety** — false positives/negatives, unsupported cases, resource cost, data handling and safe execution boundaries.
10. **Official references** — upstream repository and current documentation.

Not every tool supports every configuration item. Document only the options actually exposed by that tool.

## User configuration pattern

A user adapting a workstream should identify:

- Target model or system and version.
- Model interface: local Python object, file, REST API, hosted endpoint, or application workflow.
- Authentication and secret handling.
- Input/output schema and preprocessing requirements.
- Dataset provenance, labels and expected outcomes.
- Test categories and supported test selection.
- Runtime constraints: timeout, request rate, concurrency, compute and budget.
- Baseline and comparison criteria.
- Evidence retention and report destination.

Keep secrets outside source code and sample configuration files. Use environment variables or an approved secrets manager. Use synthetic data by default and obtain authorisation before testing external systems.

## Reporting contract

Use the shared `common/result_schema.json` and finding template where applicable. At minimum, report:

- Tool and version.
- Model/system and version.
- Test ID and objective.
- Execution status.
- Finding status.
- Category and severity (or `UNASSESSED`).
- Risky behaviour (true, false, or unknown).
- OWASP mapping only where evidence supports a defensible mapping.
- Summary, evidence, limitations, timestamp and exception.

Execution and finding are independent dimensions:

| Example | Execution status | Finding status |
|---|---|---|
| Example report only; no tool run | PLANNED | NONE |
| Tool ran and returned a metric | EXECUTED | OBSERVATION |
| Tool ran and produced a suspicious result requiring validation | EXECUTED | POTENTIAL |
| Reproducible security impact established | EXECUTED | CONFIRMED |
| Review determined the alert was benign | EXECUTED | FALSE_POSITIVE |
| Tool could not run due to dependency/configuration error | FAILED | NONE |

Do not mark an illustrative report as `EXECUTED`. Do not infer a vulnerability merely because a tool reports a score, alert, drift signal, or model behaviour.

## Sample report convention

Every sample report must visibly state **ILLUSTRATIVE EXAMPLE — NOT AN EXECUTED ASSESSMENT**. Use fictional fixture identifiers and placeholder results. Explain which fields users replace and which values must come from their own tool output. Sample numbers must never be represented as measured framework performance.

## Validation levels

- **Documented method:** capability and procedure described; no execution claim.
- **Illustrative sample:** report layout populated with fictional example values.
- **Runnable reference:** code or configuration supplied; execution may remain unverified.
- **Executed demonstration:** tool actually run against the stated target and evidence retained.
- **Assessment evidence:** authorised target, reproducible test, reviewed evidence and validated finding.

State the achieved level for each workstream. Progression between levels requires evidence, not assumptions.
