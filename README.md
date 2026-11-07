# AI Testing Tool Samples

A companion repository that **re-establishes the practical scope and capabilities** of the AI Security Testing Framework through tool-specific methods, configuration guidance, illustrative test cases, and sample reports.

This repository is a reference catalogue and starter kit—not a unified scanner, a claim that every tool has been executed, or a claim that sample results are real. Its purpose is to help assessors understand **what can be tested, which tool can help, what needs to be configured, what evidence to collect, and how results can be reported**.

## Framework coverage and integration guidance

- [Tool capability matrix](docs/TOOL_CAPABILITY_MATRIX.md) — coverage, inputs and evidence across all selected tools.
- [Tool integration method](docs/TOOL_INTEGRATION_METHOD.md) — a repeatable method for documenting and configuring each workstream.
- [Execution and evidence standard](docs/EXECUTION_AND_EVIDENCE_STANDARD.md) — distinguishes planned, executed and validated work.

## How to use this repository

1. Select an assurance area and review the tool's capability and limitations.
2. Read the method and configuration guidance.
3. Adapt the sample configuration, model/system endpoint, dataset, test cases, and thresholds to an authorised assessment.
4. Run the upstream tool in the user's own controlled environment when ready.
5. Capture actual outputs, logs, versions, and exceptions.
6. Convert observations into findings only after validation against the assessment threat model.
7. Use the shared result schema and report templates for consistent evidence.

**Sample reports are illustrative only.** Any example metrics, findings, outputs, or severities are fictional placeholders for demonstrating report structure. They must not be presented as evidence of a real assessment.

## Tool catalogue and achievable coverage

| Assurance area | Tool | What it can help demonstrate |
|---|---|---|
| Privacy | [Microsoft Presidio](https://github.com/microsoft/presidio) | PII discovery, entity recognition, anonymization and custom recognizers |
| Fairness | [AI Fairness 360](https://github.com/Trusted-AI/AIF360) | Group fairness metrics, bias measurement and selected mitigation approaches |
| NLP robustness | [TextAttack](https://github.com/QData/TextAttack) | Text perturbations, adversarial examples and model performance under attack |
| LLM security | [Garak](https://github.com/NVIDIA/garak) | Probe-based assessment of selected LLM behaviours and security weaknesses |
| Explainability | [LIME](https://github.com/marcotcr/lime) | Local explanations for individual predictions |
| Explainability | [InterpretML](https://github.com/interpretml/interpret) | Global and local model interpretability |
| Performance | [Apache JMeter](https://jmeter.apache.org/) | Repeatable load and response-time tests against configured endpoints |
| Performance | [Locust](https://locust.io/) | Programmable user-load and throughput tests |
| Monitoring | [Evidently](https://github.com/evidentlyai/evidently) | Data quality, drift and model-monitoring signals |
| AI testing | [Giskard](https://github.com/Giskard-AI/giskard) | Selected model and LLM application quality/security tests |
| Incident response | [Splunk](https://www.splunk.com/) | Security-event ingestion, searches, dashboards and alert workflows |
| Incident response | [Elastic Security](https://github.com/elastic/kibana) | Security-event ingestion, detection rules, investigation and response workflows |

The tools are not interchangeable and do not cover every model or interface. Suitability depends on model type, access method, data, deployment architecture, licensing, and assessment objective. Use official upstream documentation to confirm current features and compatibility before configuring a test.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── IMPLEMENTATION_ROADMAP.md
│   ├── EXECUTION_AND_EVIDENCE_STANDARD.md
│   ├── SAFETY.md
│   └── TOOL_INTEGRATION_METHOD.md
├── common/result_schema.json
├── templates/
│   ├── TOOL_README_TEMPLATE.md
│   ├── TEST_CASE_TEMPLATE.md
│   └── FINDING_TEMPLATE.md
├── privacy/presidio/
│   ├── README.md
│   ├── requirements.txt
│   ├── sample_cases.json
│   ├── run_presidio.py
│   └── sample_report.html
├── fairness/aif360/
├── robustness/textattack/
├── llm_security/garak/
├── explainability/{lime,interpretml}/
├── performance/{jmeter,locust}/
├── monitoring/{evidently,giskard}/
└── incident_response/{splunk,elastic}/
```

Each tool workstream should include, as appropriate: capability overview, method, prerequisites, configurable inputs, example test cases, expected evidence, limitations, official references, and an illustrative report. A runnable reference script is optional and should never be confused with proof that a test was run.

## Relationship to the main framework

The main [AI Testing Framework](https://github.com/Gajanan108/AI-Testing-Framework) defines the assessment lifecycle, assurance areas, methodology, risk rating, finding taxonomy, and reporting expectations. This repository explains how selected external tools can support those workstreams. The IBM ART experiments remain in the main repository.

## Status and evidence discipline

- Tool catalogue, capability matrix and integration guidance: documented.
- Presidio: reference method, configuration example, optional script, synthetic fixtures and illustrative report.
- Other 11 tool workstreams: method guides and illustrative HTML reports are documented.
- No actual assessment execution or tool result is claimed by the presence of sample files.

Keep **execution status** separate from **finding status**. A planned or illustrative test is not an executed test; a tool observation is not automatically a confirmed vulnerability.
