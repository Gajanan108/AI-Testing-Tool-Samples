# InterpretML — Explainability

## Purpose in the framework

InterpretML provides glassbox interpretable models and blackbox explanation methods. Explainable Boosting Machines (EBMs) support interpretable additive modelling; global and local explanation interfaces can also inspect supported blackbox models.

## Assessment method

1. Decide whether the objective is interpretable modelling or explanation of an existing blackbox.
2. Prepare documented features, target, train/test split and preprocessing.
3. For glassbox assessment, configure an EBM or another supported estimator; for blackbox analysis, select a supported explainer.
4. Generate global explanations for feature importance/shape and local explanations for selected predictions.
5. Inspect interactions, missingness and sensitive/proxy attributes where relevant.
6. Compare explanations with domain expectations and independent performance/fairness evidence.

## User configuration

- Estimator or blackbox model interface
- Feature matrix, target and feature names
- Train/test split and preprocessing
- Global/local explainer selection
- Model parameters and random seed
- Instances and subgroups to inspect

## Evidence to retain

- Model and dataset versions
- Global feature importance and shape plots
- Local explanations for selected records
- Performance metrics and calibration where relevant
- Reviewer interpretation and limitations

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| XAI-INT-001 | Review global model drivers | Global feature importance/shape | Identify dominant or unexpected feature dependencies |
| XAI-INT-002 | Explain individual decisions | Local feature contributions | Assess whether selected outcomes are interpretable |
| XAI-INT-003 | Compare group explanations | Group-level feature patterns | Investigate differences; do not treat them alone as proof of bias |

## Sample report

See [sample_report.html](sample_report.html). Static illustrative example only; no execution or measured result is implied.

## Limitations and interpretation

- Glassbox model explanations differ from post-hoc blackbox approximations.
- Feature importance is not causal evidence or proof of fairness.
- Correlated variables and data leakage can distort interpretation.
- Explanations are bounded by training data, preprocessing and selected model.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in context. Keep execution status separate from finding status. Do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://github.com/interpretml/interpret
- Documentation: https://interpret.ml/docs/
