# Implementation roadmap

The roadmap is capability-led. The immediate objective is to document what each selected tool can achieve, how assessors configure it, and how outputs fit the framework. Tool execution is optional for the documentation and illustrative-report stages.

## Phases

1. **Framework re-establishment:** align tool workstreams to the main framework's assurance areas, taxonomy, evidence standard and report structure.
2. **Privacy and fairness:** document Presidio and AI Fairness 360 methods, configuration points, synthetic cases and illustrative reports.
3. **Robustness and LLM security:** document TextAttack and Garak capabilities, applicability, safe target configuration and sample result formats.
4. **Explainability:** document LIME and InterpretML workflows, inputs, interpretation boundaries and sample outputs.
5. **Performance:** document JMeter and Locust test plans, workload configuration, safe limits and sample performance reports.
6. **Monitoring and AI testing:** document Evidently and Giskard drift, quality and security testing workflows.
7. **Incident response:** document Splunk and Elastic Security ingestion, detection and investigation examples using synthetic events.
8. **Optional runnable demonstrations:** add reference scripts or configurations where they materially help users. Execute and validate them only when a separate demonstration is planned.

## Acceptance checklist for a documented workstream

- [ ] Assurance objective and tool capability are explicit.
- [ ] Official upstream source and documentation are linked.
- [ ] Applicability and unsupported cases are documented.
- [ ] Method, prerequisites and user configuration points are explained.
- [ ] Synthetic sample cases or a safe example workflow are provided.
- [ ] Illustrative report is clearly marked as non-executed.
- [ ] Expected evidence, limitations and safety constraints are stated.
- [ ] Execution and finding status are not conflated.

## Additional acceptance checklist for an executed demonstration

- [ ] Dependencies and tool versions are recorded.
- [ ] Exact target, configuration and invocation are retained.
- [ ] Intended tool operation actually ran.
- [ ] Output and logs are inspectable.
- [ ] Exceptions and deviations are recorded.
- [ ] Results are reviewed before findings are confirmed.
