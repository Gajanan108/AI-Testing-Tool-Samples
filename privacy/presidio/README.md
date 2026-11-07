# Microsoft Presidio — PII detection and anonymization sample

This workstream demonstrates **real execution** of the official Presidio Python packages against synthetic text fixtures. It calls Presidio's `AnalyzerEngine` to detect PII and `AnonymizerEngine` to anonymize the detected spans.

## Scope

- Text PII detection for email addresses, phone numbers, and credit-card numbers.
- Anonymization of spans returned by the analyzer.
- Comparison of detected entity types against explicitly declared synthetic fixture expectations.
- HTML report and execution log.

This is a reproducible starter assessment, not a certification of privacy compliance or a complete PII benchmark. A missed expected entity is classified as a **potential** privacy finding; it is not automatically promoted to a confirmed production vulnerability. Unexpected entity types are marked as fixture-level false-positive candidates. Review the source text, recognizer configuration, language, and business context before making a production risk decision.

## Requirements

- Python 3.11 or newer (the upstream installation guide currently lists supported Python versions).
- A virtual environment.
- Presidio Analyzer, Presidio Anonymizer, spaCy, and the English spaCy model.

## Install

From this directory:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

## Run

```bash
python run_presidio.py
```

The script reads `sample_cases.json` and writes exactly two generated artifacts into `output/`:

- `presidio_report.html`
- `presidio_run.log`

Choose another output directory with:

```bash
python run_presidio.py --output-dir ./artifacts
```

The log intentionally excludes raw fixture text and detected values. The HTML report shows anonymized text, entity types, confidence scores, fixture comparisons, execution status, and limitations.

## Interpretation

| Result | Meaning |
|---|---|
| `EXECUTED` | Presidio analysis and anonymization completed for all fixtures. |
| `FAILED` | The tool could not complete the run; inspect the log. |
| `POTENTIAL` | At least one expected entity type was not detected in a synthetic fixture. |
| `FALSE_POSITIVE` | Presidio returned an entity type not declared in the fixture's expected set. |
| `OBSERVATION` | Detected entity types matched the fixture expectations. |

The report's risky-behavior field is set to true only when an expected fixture entity type is missed. This is a test signal, not proof of exploitability or production exposure. Severity remains unassessed. OWASP mapping is left empty because this standalone PII detector test does not, by itself, establish an application or LLM vulnerability.

## Limitations

- The fixtures are synthetic and intentionally small; they do not measure production precision or recall.
- Entity-type matching is evaluated at the fixture level, not as a full span-level benchmark.
- Presidio's results depend on recognizers, NLP model, language, context, and configuration.
- A successful run does not prove that all sensitive data will be detected. Add domain-specific recognizers and representative, approved test data before relying on it operationally.
- No network service or external API is required by this sample; the Python packages run locally.

## Official upstream references

- [Presidio project](https://github.com/data-privacy-stack/presidio)
- [Installation guide](https://microsoft.github.io/presidio/installation/)
- [Analyzer documentation](https://microsoft.github.io/presidio/analyzer/)
- [Text de-identification quickstart](https://presidio.dataprivacystack.org/getting_started/getting_started_text/)
