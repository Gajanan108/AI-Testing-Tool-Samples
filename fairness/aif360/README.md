# AI Fairness 360 — Fairness and bias assessment

## Purpose in the framework

AIF360 provides datasets, group fairness metrics, explainers and selected bias-mitigation algorithms. It helps measure differences in model outcomes across defined protected and comparison groups, and compare selected pre-, in- and post-processing mitigation approaches.

## Assessment method

1. Define the decision use case, population, protected attributes and comparison groups.
2. Select a labelled dataset; document provenance, sampling, missingness and label quality.
3. Define favourable outcome and privileged/unprivileged group values before metric calculation.
4. Calculate suitable baseline metrics such as statistical parity difference, disparate impact, equal opportunity difference and average odds difference, as supported by the selected metric API.
5. If mitigation is in scope, select a compatible algorithm and compare fairness and utility metrics on held-out data.
6. Review group sizes, uncertainty, intersectional effects and domain/legal context before conclusions.

## User configuration

- Dataset, feature and label columns
- Protected attribute(s), group definitions and favourable label
- Train/validation/test split and random seed
- Selected fairness metrics and justified thresholds
- Model predictions or scores
- Mitigation algorithm and parameters, if used

## Evidence to retain

- Group counts and data-quality checks
- Baseline and post-mitigation fairness metrics
- Overall and subgroup utility metrics
- Mitigation configuration and model version
- Threshold rationale and reviewer decision

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| FAIR-001 | Compare group selection rates | Statistical parity difference / disparate impact | Assess outcome-rate differences against pre-defined criteria |
| FAIR-002 | Compare true-positive rates | Equal opportunity difference | Investigate group opportunity gaps and label quality |
| FAIR-003 | Compare mitigation trade-offs | Before/after fairness and utility metrics | Check whether mitigation improves selected metrics without unacceptable utility loss |

## Sample report

See [sample_report.html](sample_report.html). It is a static illustrative report, not an executed assessment or measured result.

## Limitations and interpretation

- Fairness metrics encode different normative definitions and may conflict.
- Results depend on group definitions, data quality, label bias and subgroup sample sizes.
- AIF360 does not determine applicable legal standards or which attributes should be protected.
- Mitigation may change utility, calibration or other subgroup outcomes.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without supporting evidence.

## Official references

- Project: https://github.com/Trusted-AI/AIF360
- Documentation: https://aif360.readthedocs.io/

Check upstream documentation for current APIs, supported model interfaces, dependencies and licensing before configuration.
