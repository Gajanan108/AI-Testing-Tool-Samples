# Tool capability and framework coverage matrix

This matrix describes the intended role of each selected tool. It is a capability map, not a claim that the tools are integrated into one product or executed against a common target.

| Framework workstream | Tool | Example assessment capability | Typical input / target | Main output / evidence |
|---|---|---|---|---|
| Privacy | Presidio | PII detection, custom recognizers, anonymization | Text fields, prompts, responses, documents or logs | Entity spans, confidence scores, anonymized text |
| Fairness | AI Fairness 360 | Group fairness metrics and selected mitigation | Labelled dataset, protected attributes, predictions | Group metrics, mitigation comparison, utility trade-offs |
| NLP robustness | TextAttack | Adversarial text perturbations | Supported NLP model wrapper and labelled examples | Perturbed examples, attack success, robust accuracy |
| LLM security | Garak | Probe-based LLM vulnerability assessment | Supported LLM generator/endpoint | Probe outcomes, detector hits, sanitized transcripts |
| Explainability | LIME | Local model-agnostic explanations | Prediction and prediction function | Local feature weights and surrogate fidelity |
| Explainability | InterpretML | Glassbox models and global/local explanations | Feature matrix, target, supported model | Global and local explanation artefacts |
| Performance | JMeter | Configured load, latency and response validation | Supported service endpoint/protocol | Throughput, latency percentiles, errors, assertions |
| Performance | Locust | Python-defined user load and task flows | Configured service endpoint | Requests/sec, response times, failures |
| Monitoring | Evidently | Data quality and drift | Reference and current datasets | Drift metrics, data-quality tests, reports |
| AI testing | Giskard | Scenario-based model/agent testing and supported scans | Model, chatbot, RAG pipeline or agent adapter | Test suite outcomes and failing scenarios |
| Incident response | Splunk | Search, dashboards and alert workflows | Ingested application/security telemetry | SPL results, alerts, dashboards, investigation records |
| Incident response | Elastic Security | SIEM detection and investigation | Ingested and mapped event data | Detection alerts, rules, timelines and cases |

## Coverage boundaries

- No single tool covers an entire assurance area. Applicability depends on model type, interface, data, deployment and test objective.
- Privacy and fairness tools measure selected data/model behaviours; application context and governance review remain necessary.
- Robustness and LLM security tools exercise selected attack/probe families; coverage is bounded by recipes, probes, adapters, detectors and budgets.
- Explainability tools help interpret model behaviour; explanations are not causal proof or substitutes for fairness, robustness or security testing.
- Performance tools measure configured workloads; they do not establish model correctness or security.
- Monitoring tools surface distribution and data-quality signals; drift alone does not prove degraded model quality.
- SIEM platforms require telemetry ingestion, normalization, detection logic and operational response. They are not model vulnerability scanners by themselves.

## Assessment maturity

1. **Documented method** — capability, applicability and procedure are described.
2. **Illustrative sample** — static report shows how evidence could be presented; values are fictional.
3. **Runnable reference** — optional configuration or starter code is supplied; execution is not implied.
4. **Executed demonstration** — intended tool operation has actually run and inspectable evidence is retained.
5. **Validated assessment** — authorized target, reproducible evidence, impact analysis and reviewer validation support a finding.

Do not infer a higher maturity level from the presence of a README, script or sample report.
