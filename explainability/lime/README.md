# LIME — Explainability

## Purpose in the framework

LIME (Local Interpretable Model-agnostic Explanations) approximates a model locally around an individual prediction with an interpretable surrogate. Depending on explainer type, it can explain tabular, text or image predictions.

## Assessment method

1. Select a prediction and preserve exact input, preprocessing and model version.
2. Choose tabular, text or image explainer and define feature representation and perturbation behaviour.
3. Configure prediction function, class names, sample count and relevant explainer settings.
4. Generate local perturbations, obtain black-box predictions and fit the local surrogate.
5. Inspect feature contributions and surrogate fidelity; repeat with different seeds/settings to assess stability.
6. Treat the explanation as a diagnostic aid, not causal reasoning or proof of correctness.

## User configuration

- Model prediction function and output shape
- Input schema, feature names and preprocessing
- Explainer type and feature representation
- Perturbation sample count and kernel settings
- Class labels and random seed
- Selected instance(s)

## Evidence to retain

- Target instance and model version
- Positive/negative local feature contributions
- Local surrogate fidelity
- Explainer configuration
- Stability checks and analyst interpretation

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| XAI-LIME-001 | Explain a selected prediction | Local feature weights and fidelity | Identify features driving the local approximation |
| XAI-LIME-002 | Check explanation stability | Repeated runs across seeds/settings | Material variation requires investigation |
| XAI-LIME-003 | Inspect sensitive/proxy features | Attribution of protected or proxy features | Potential dependence signal; validate with fairness analysis |

## Sample report

See [sample_report.html](sample_report.html). It is a static illustrative report, not an executed assessment or measured result.

## Limitations and interpretation

- Explanations are local approximations and may be unstable.
- Feature attribution is not causal evidence.
- Correlated features and unrealistic perturbations can mislead.
- An individual explanation does not describe global model behaviour.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without supporting evidence.

## Official references

- Project: https://github.com/marcotcr/lime
- Documentation: https://lime-ml.readthedocs.io/

Check upstream documentation for current APIs, supported model interfaces, dependencies and licensing before configuration.
