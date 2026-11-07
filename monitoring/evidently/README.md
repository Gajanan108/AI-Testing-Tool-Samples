# Evidently — Data quality, drift and monitoring

## Purpose in the framework

Evidently supports evaluation and monitoring of data quality, data drift, target/prediction drift and selected model quality metrics through reports and tests. It compares reference and current datasets using configured column mappings, metrics and statistical methods.

## Assessment method

1. Define monitored data boundary and distinguish reference/baseline data from current data.
2. Map feature, prediction, target and timestamp columns; document data types.
3. Select drift and data-quality metrics appropriate to volume and distribution.
4. Generate a report comparing reference/current data; optionally define tests and thresholds.
5. Investigate changed distributions, missing values, schema changes and prediction shifts.
6. Determine whether drift is actionable through model validation; drift alone is not proof of model failure.

## User configuration

- Reference and current datasets
- Column mapping and target/prediction columns
- Data types and feature selection
- Drift methods and thresholds
- Minimum sample sizes and test suite
- Report output and monitoring cadence

## Evidence to retain

- Dataset windows/provenance and row counts
- Column mapping and metric configuration
- Drift/data-quality report and test outcomes
- Affected columns and distribution summaries
- Follow-up validation and retraining decision

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| MON-EVI-001 | Compare feature distributions | Drift metric by feature | Flag material distribution changes |
| MON-EVI-002 | Check data quality | Missingness, type and value checks | Identify schema and quality regressions |
| MON-EVI-003 | Evaluate prediction drift | Prediction distribution comparison | Investigate changes in model output distribution |

## Sample report

See [sample_report.html](sample_report.html). Static illustrative example only; no execution or measured result is implied.

## Limitations and interpretation

- Drift indicates distributional change, not necessarily degraded model performance.
- Results depend on reference-window selection, sample size, feature types and thresholds.
- Without labels, predictive performance may not be measurable.
- Monitoring data may contain sensitive information; minimize and govern ingestion.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in context. Keep execution status separate from finding status. Do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://github.com/evidentlyai/evidently
- Documentation: https://docs.evidentlyai.com/
