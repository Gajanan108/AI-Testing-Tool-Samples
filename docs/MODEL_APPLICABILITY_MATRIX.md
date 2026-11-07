# Model and application applicability matrix

Use this matrix to select assessment methods before configuration. It is a planning aid, not a compatibility guarantee. Confirm current upstream support, version, adapter, licence and interface requirements.

**Primary** means generally relevant when prerequisites are met. **Conditional** means useful only for a particular component, interface or objective. **Not a direct fit** means do not treat the tool as a direct test of that archetype; it may still test the surrounding application.

## 1. Model archetype coverage

| Model / application archetype | Presidio | AIF360 | TextAttack | Garak | LIME / InterpretML | Giskard | JMeter / Locust | Evidently | Splunk / Elastic |
|---|---|---|---|---|---|---|---|---|---|
| Classical tabular classifier / regressor | Conditional: text fields | **Primary** with labels, predictions and protected attributes | Not a direct fit | Not a direct fit | **Primary** for supported prediction interfaces | Primary/conditional | **Primary** for serving endpoint | **Primary** with reference/current data | Conditional: telemetry |
| Credit / eligibility / decisioning | Conditional: PII fields | **Primary**; define defensible cohorts and outcomes | Not a direct fit | Not a direct fit | **Primary** | Primary/conditional | **Primary** | **Primary** | Conditional: audit trail |
| Text classifier (sentiment, topic, intent) | **Primary** for text PII | Conditional: cohort labels | **Primary** with supported task/model wrapper | Not a direct fit | **Primary** | Primary/conditional | **Primary** | Conditional | Conditional |
| Embedding / semantic search / reranker | Conditional: corpus and output text | Conditional: downstream outcomes | Conditional: supported NLP task only; latent vector changes are not natural-language attacks | Not a direct fit for bare encoder | Conditional: explain downstream score/rank | Conditional: full retrieval workflow | **Primary** | Conditional: meaningful vector/feature baseline | Conditional: query/access logs |
| LLM / chat completion | **Primary** for prompt/response PII checks | Conditional: cohort-based output evaluation | Conditional: task-specific text perturbation only | **Primary** for supported generator/probe/detector | Conditional; generated-output explanations have limits | Primary/conditional | **Primary** for token/latency/concurrency | Conditional: prompt/response metrics need baseline | Primary/conditional |
| RAG application | **Primary** for docs, chunks, prompts, answers | Conditional: defined cohort outcomes | Conditional: supported query/text task | **Primary/conditional** for supported LLM/RAG probes | Conditional: retrieval and answer attribution | **Primary** for supported end-to-end workflow | **Primary** across retrieval/reranking/generation | Primary/conditional: corpus/retrieval drift | **Primary** for retrieval access, tool and audit events |
| OCR / document AI / VLM | Primary/conditional: extracted text; image handling separate | Conditional: cohort labels | Not a direct image-attack tool; text stage only if supported | Conditional: exposed generative component only | Conditional: downstream decisions | Conditional: supported pipeline adapter | **Primary** for upload/OCR/inference service | Conditional: document mix and OCR quality baseline | Conditional: upload/process/export telemetry |
| Image classifier / vision encoder | Conditional: OCR text/metadata | Conditional: labelled cohorts | Not a direct fit | Not a direct fit for bare encoder | Conditional: image-specific methods may be needed | Conditional: supported image adapter | **Primary** | Conditional: image/embedding drift | Conditional |
| Multimodal (text + image/audio/video) | Conditional: text/transcripts | Conditional: modality-specific cohorts | Conditional: supported text path only | Conditional: confirm modality support | Conditional: modality-specific explainers | Conditional: supported modalities only | **Primary** end-to-end | Conditional: modality-aware baselines | Primary/conditional |
| Agent / tool-using assistant | **Primary** for sensitive data in prompts, tool I/O and traces | Conditional: defined outcomes/cohorts | Conditional: supported text component | **Primary** for supported LLM probes; add explicit tool-boundary cases | Conditional: trace interpretation, not causal proof | **Primary** for supported agent scenarios | **Primary** for multi-step flows | Conditional: task/tool metrics need baselines | **Primary** for identity, privilege, tool and data-access telemetry |

## 2. Tool applicability and configuration

| Tool | Best fit | Minimum inputs | Key configuration choices | Do not claim |
|---|---|---|---|---|
| Microsoft Presidio | Text-bearing systems and document pipelines | Text, language, expected PII categories | Built-in/custom recognizers, thresholds, anonymizers, field scope | Complete privacy compliance or detection of all sensitive data |
| AI Fairness 360 | Supervised classification/regression | Labels, predictions, protected attributes, favourable outcome | Cohort definitions, metric, threshold, mitigation and utility trade-off | Universal fairness verdict; metrics are context-dependent |
| TextAttack | Supported NLP classification/sequence tasks | Model wrapper, tokenizer, labelled examples, task metric | Recipe, constraints, query budget, sample size, seed | Vision robustness or arbitrary LLM security |
| Garak | Supported LLM generator interfaces | Generator/endpoint, credentials, probe/detector selection | Safe target, rate limits, probe families, timeouts, output sanitization | Exhaustive LLM security coverage or vulnerability confirmation from one hit |
| LIME | Supported tabular/text/image prediction functions | Instance, prediction function, feature representation | Samples, feature mapping, kernel/segmentation settings | Causality or global fidelity from a local surrogate |
| InterpretML | Supported tabular models | Feature matrix, target, model/estimator | Glassbox vs blackbox explainer, feature handling, evaluation split | Causal attribution or support for arbitrary modalities |
| Apache JMeter | HTTP and supported service protocols | Endpoint, request template, test data, assertions | Users/threads, ramp-up, duration, pacing, timeout | Model quality or capacity beyond tested workload |
| Locust | Programmable service user journeys | Host, user tasks, test data | User classes, wait time, spawn rate, duration, task mix | Production capacity from unrepresentative workload |
| Evidently | Data and model monitoring | Reference/current datasets or supported prediction data | Column mapping, target/prediction fields, tests, thresholds | Model failure from drift alone |
| Giskard | Supported ML, LLM and application workflows | Model/app adapter, representative data/scenarios | Scan/test selection, metadata, task config, thresholds | Complete security coverage or confirmed vulnerability without validation |
| Splunk | Log/event analytics and alerting | Approved telemetry and field mapping | Ingestion, parsing, SPL, thresholds, retention, RBAC | Detection capability before data and rules are tested |
| Elastic Security | SIEM detection and investigation | Data sources and normalized event fields | Integrations, ECS mapping, rules, exceptions, cases | Effective detection without validated ingestion and response |

## 3. Choose by assessment question

| Question | Start with | Add where appropriate | Evidence |
|---|---|---|---|
| Is PII exposed or transformed unexpectedly? | Presidio on scoped text surfaces | Data-flow review, access logs, synthetic canaries | Redacted I/O, recognizer/version, entity spans, disposition |
| Do outcomes differ across defined groups? | AIF360 | Giskard/custom evaluation and domain review | Provenance, cohort counts, metric definition, uncertainty, utility trade-off |
| Is supported NLP behaviour sensitive to adversarial text? | TextAttack | Application-level reproduction | Model/tokenizer, recipe, constraints, budgets, examples, baseline |
| Does an LLM fail selected safety/security probes? | Garak | Giskard and application abuse cases | Generator config, probe/detector, sanitized transcript, reproduction |
| Can the endpoint handle expected load? | JMeter or Locust | Tracing and resource monitoring | Workload, environment, latency percentiles, throughput, errors |
| Is production data/behaviour drifting? | Evidently | Model-quality evaluation and alerting | Reference/current windows, schema, drift tests, downstream quality |
| Can SOC detect suspicious AI activity? | Splunk or Elastic | Application audit instrumentation and playbooks | Event source, field mapping, rule, test event, alert, investigation |

## 4. IBM ART applicability in the main framework

IBM Adversarial Robustness Toolbox (ART) is maintained separately in the [main framework](https://github.com/Gajanan108/AI-Testing-Framework), not as one of the 12 companion catalogue tools. Applicability depends on estimator interface, task, input representation, output semantics and attack prerequisites. A working adapter does not make every attack meaningful.

| Component | Potential ART path | Required checks / limitations |
|---|---|---|
| Image classifier | ART image-classifier estimator and compatible image attacks | Validate range, channel order, preprocessing, differentiability/query access, labels/probabilities and attack constraints |
| Vision encoder | Justified differentiable wrapper or downstream decision proxy | Define objective/output semantics. Embedding movement alone is not security impact; assess ranking/retrieval degradation against a baseline |
| OCR/document pipeline | Test separable image/layout/text components with suitable adapters | Layout-class scores do not test OCR recognition, boxes, parsing or the complete document pipeline |
| Text embedding/reranker | Justified tensor wrapper or downstream ranking objective | Embedding perturbation is latent-space robustness, not natural-language adversarial robustness |
| Generative LLM | Appropriate differentiable or query-based interface and generation objective | Classifier attacks cannot be assumed applicable to token generation; use suitable LLM/application probes |

**ART execution gate:** record estimator type, input/output shape, preprocessing, output range/semantics, objective, attack prerequisites, perturbation norm/budget, query/iteration budget and success criterion. Mark unsupported attacks as NOT APPLICABLE with a reason; never silently substitute another method.

## 5. Selection workflow

1. Identify the boundary: model, API, RAG, document pipeline, agent or full application.
2. Decompose composite systems into testable components and data flows.
3. Define the assessment question and threat assumptions before selecting tools.
4. Verify official support for the exact model interface and task.
5. Define baseline, success criteria, sample size, budget and safety limits.
6. Configure supported parameters; keep secrets outside source control.
7. Retain raw evidence, versions, configuration, invocation, logs and exceptions.
8. Reproduce relevant observations and determine impact.
9. Assign finding status and severity only after validation.

## 6. Official references

[Presidio](https://github.com/microsoft/presidio) · [AIF360](https://github.com/Trusted-AI/AIF360) · [TextAttack](https://github.com/QData/TextAttack) · [Garak](https://github.com/NVIDIA/garak) · [LIME](https://github.com/marcotcr/lime) · [InterpretML](https://github.com/interpretml/interpret) · [JMeter](https://jmeter.apache.org/) · [Locust](https://locust.io/) · [Evidently](https://github.com/evidentlyai/evidently) · [Giskard](https://github.com/Giskard-AI/giskard) · [Splunk](https://www.splunk.com/) · [Elastic Security](https://github.com/elastic/kibana) · [IBM ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox).

Check upstream documentation for current support, APIs, installation and licence terms before execution.
