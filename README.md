# AI Testing Tool Samples

A companion repository of **small, reproducible demonstrations** for the tools referenced by the AI Security Testing Framework.

This repository is a collection of independent tool workstreams, not a unified scanner. Each demonstration must use the tool's official package, API, and documentation; report actual execution status; and state its limitations.

## Tool catalogue and planned workstreams

| Area | Tool | Official source | Initial demonstration |
|---|---|---|---|
| Privacy | Microsoft Presidio | https://github.com/microsoft/presidio | Detect and anonymise synthetic PII |
| Fairness | AI Fairness 360 | https://github.com/Trusted-AI/AIF360 | Calculate selected fairness metrics on a documented sample dataset |
| NLP robustness | TextAttack | https://github.com/QData/TextAttack | Run a supported text attack against a small NLP model |
| LLM security | Garak | https://github.com/NVIDIA/garak | Run selected probes against an explicitly configured local/test endpoint |
| Explainability | LIME | https://github.com/marcotcr/lime | Explain a prediction from a small tabular/text classifier |
| Explainability | InterpretML | https://github.com/interpretml/interpret | Demonstrate global/local interpretability on a sample dataset |
| Performance | Apache JMeter | https://jmeter.apache.org/ | Run a bounded load test against a local demo endpoint |
| Performance | Locust | https://locust.io/ | Run a bounded Python user-load test against a local demo endpoint |
| Monitoring | Evidently | https://github.com/evidentlyai/evidently | Compare reference and current synthetic data for drift |
| AI testing | Giskard | https://github.com/Giskard-AI/giskard | Run supported tests on a small model or explicitly configured LLM app |
| Incident response | Splunk | https://www.splunk.com/ | Provide sample event ingestion/search workflow; requires an authorised Splunk instance |
| Incident response | Elastic Security | https://github.com/elastic/kibana | Provide sample event ingestion/detection workflow; requires an authorised Elastic instance |

Tool selection and APIs change over time. Before implementation, verify the official documentation and pin tested versions. Do not assume every tool supports every model type.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── IMPLEMENTATION_ROADMAP.md
│   ├── EXECUTION_AND_EVIDENCE_STANDARD.md
│   └── SAFETY.md
├── common/
│   └── result_schema.json
├── templates/
│   ├── TOOL_README_TEMPLATE.md
│   ├── TEST_CASE_TEMPLATE.md
│   └── FINDING_TEMPLATE.md
├── privacy/presidio/
├── fairness/aif360/
├── robustness/textattack/
├── llm_security/garak/
├── explainability/lime/
├── explainability/interpretml/
├── performance/jmeter/
├── performance/locust/
├── monitoring/evidently/
├── monitoring/giskard/
└── incident_response/{splunk,elastic}/
```

Each tool directory will receive its own README, dependency pins, runnable sample, synthetic fixtures, logs and report artefacts as that workstream is implemented. Empty directories are represented by `.gitkeep` files in this starter archive.

## Relationship to the main framework

The main framework defines assurance areas, assessment methodology, risk classification and reporting expectations. This companion repository demonstrates selected tools in isolation. The IBM ART experiments remain in the existing AI-Testing-Framework repository and are not duplicated here.

## Status

**Starter structure and templates only.** No tool integrations or test executions are claimed by this archive. Implementations should be added and validated incrementally.
