# Microsoft Presidio — PII detection and anonymization

## Purpose in the framework

Presidio supports the **privacy and sensitive-data handling** workstream. It can identify configured entities in text, return spans and confidence scores, and anonymize or replace detected values. It is useful for demonstrating PII discovery and de-identification workflows around text inputs and outputs.

Presidio is not a complete privacy assessment by itself. It does not prove that an application stores, exposes, or mishandles personal data; that conclusion requires application context and evidence.

## What can be demonstrated

- Identify supported PII entity types such as email addresses, phone numbers and payment-card numbers.
- Inspect entity type, text span and recognizer confidence.
- Apply anonymization operators to detected spans.
- Configure recognizers, supported languages and NLP models.
- Add custom recognizers for domain-specific identifiers.
- Compare detected entities with labelled synthetic fixtures to illustrate expected-versus-observed coverage.

## Method

1. Define the data boundary: user prompts, model inputs, model outputs, retrieved documents, logs, or another text surface.
2. Select synthetic or approved test fixtures and label expected entity types.
3. Configure Presidio's analyzer, language, NLP engine and recognizers for the target data.
4. Run analysis and capture entity type, span and score.
5. Apply the selected anonymization operator and inspect the transformed output.
6. Compare results against fixture expectations; investigate missed and unexpected detections.
7. Record limitations and decide whether any application-level risk is established.

## User configuration

| Configuration | What the assessor supplies |
|---|---|
| Input source | Text fixture, approved dataset, application adapter or controlled endpoint |
| Language | Language supported by the configured NLP engine and recognizers |
| Entity types | Entity classes relevant to the assessment objective |
| Recognizers | Built-in recognizers plus optional custom patterns/context |
| NLP model | Installed model compatible with the Presidio NLP engine |
| Thresholds | Confidence threshold appropriate to the use case |
| Anonymization | Operator and replacement policy for each entity type |
| Evaluation | Expected entity labels and acceptance criteria |

Use the official Presidio documentation to confirm the current API and supported configuration. The optional `run_presidio.py` file is a starter example for synthetic local fixtures; adapt it to the target architecture rather than assuming it fits every deployment.

## Sample assets

- `sample_cases.json`: fictional fixture examples; change or extend the text and expected entity labels.
- `sample_report.html`: **illustrative only** report layout with fictional values. It is not generated from an actual execution.
- `run_presidio.py`: optional reference script; its presence does not mean it has been executed or validated in your environment.

### Machine-readable orchestration output

The runner also supports an opt-in, redacted evidence summary on stdout:

```bash
python run_presidio.py --fixtures sample_cases.json --output-dir ./output --emit-evidence-summary
```

The summary is emitted as one `PRESIDIO_EVIDENCE_SUMMARY=` JSON line. It contains fixture IDs, expected/detected entity types, misses, unexpected types and confidence scores; it does not include input text, detected values or anonymized text. It creates no additional file, so the runner continues to write only `presidio_report.html` and `presidio_run.log`. The framework orchestrator consumes this line to create its separate normalized evidence record and SHA-256 artifact references.

## Report interpretation

A missed expected entity is a test observation that may indicate a potential privacy-control weakness. An unexpected detection may be a false-positive candidate. Neither should be promoted to a confirmed finding without review of the actual data surface, application behaviour and impact.

Keep the following separate:
- Execution status: whether the configured Presidio operation actually ran.
- Finding status: whether the observed behaviour has security significance.
- Risky behaviour: whether the observed behaviour creates a demonstrated risk in the assessed system.
- Severity: assigned only after impact and context are assessed.
- OWASP mapping: include only if the broader application evidence supports a relevant mapping.

## Limitations

- Recognition depends on language, NLP model, recognizer coverage, context and configuration.
- A detector can miss sensitive values or produce false positives.
- A small synthetic fixture set is not a representative precision/recall benchmark.
- Anonymization of detected spans does not guarantee complete de-identification.
- Production deployment requires data-flow analysis, custom recognizers where appropriate, privacy review and security controls beyond the detector.

## Official references

- [Presidio upstream repository](https://github.com/microsoft/presidio)
- [Installation guide](https://microsoft.github.io/presidio/installation/)
- [Analyzer documentation](https://microsoft.github.io/presidio/analyzer/)
- [Text de-identification quickstart](https://microsoft.github.io/presidio/getting_started/quickstart/)
