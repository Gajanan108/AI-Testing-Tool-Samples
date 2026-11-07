# TextAttack — NLP robustness

## Purpose in the framework

TextAttack is an NLP adversarial-attack and data-augmentation framework. Attack recipes combine a goal function, constraints, transformations and search method to test supported NLP models under text perturbations.

## Assessment method

1. Identify the NLP task, model wrapper, tokenizer, label mapping and baseline dataset.
2. Select a supported attack recipe or define its goal function, transformations, constraints and search method.
3. Set semantic/syntactic constraints and perturbation budget appropriate to the task.
4. Run against a controlled model and bounded dataset; record original/perturbed inputs, predictions and query cost.
5. Manually inspect successful examples for semantic validity and task relevance.
6. Report attack success and robust accuracy only for the stated dataset, wrapper, recipe and budget.

## User configuration

- Model checkpoint/wrapper and tokenizer
- Task type and label mapping
- Dataset and baseline accuracy
- Attack recipe or components
- Perturbation budget and semantic constraints
- Query budget, random seed and compute limits

## Evidence to retain

- Baseline predictions and labels
- Exact recipe and parameters
- Sanitized original/perturbed examples
- Attack success rate and denominator
- Query counts, failed/skipped samples and human validity review

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| NLP-ROB-001 | Run selected adversarial recipe | Attack success rate / robust accuracy | Prediction changes under a valid constrained perturbation |
| NLP-ROB-002 | Measure perturbation cost | Words modified, queries, similarity constraints | Compare attack effectiveness under a defined budget |
| NLP-ROB-003 | Review semantic validity | Human review of successful examples | Exclude invalid or meaning-changing examples from confirmed claims |

## Sample report

See [sample_report.html](sample_report.html). It is a static illustrative report, not an executed assessment or measured result.

## Limitations and interpretation

- Applicability depends on task, wrapper, model outputs and supported tokenizer.
- Successful examples may be semantically invalid or task-changing.
- A failed attack under one recipe/budget does not establish general robustness.
- Small benchmark results do not automatically generalize to production or other languages.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without supporting evidence.

## Official references

- Project: https://github.com/QData/TextAttack
- Documentation: https://textattack.readthedocs.io/

Check upstream documentation for current APIs, supported model interfaces, dependencies and licensing before configuration.
