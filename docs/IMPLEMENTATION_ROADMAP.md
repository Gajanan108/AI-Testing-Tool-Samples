# Implementation roadmap

Use official upstream packages and APIs. Pin dependencies and runtime versions. Use synthetic or authorised data and targets. Record model/system, dataset, threat model, exact invocation, execution status, evidence, exceptions and limitations. Never claim a test executed unless the intended tool operation ran and produced inspectable output.

## Phases
1. Foundation: shared result schema, templates and logging conventions.
2. Privacy and fairness: Presidio, AI Fairness 360 and TextAttack.
3. LLM security: Garak and Giskard against controlled local or authorised targets.
4. Explainability: LIME and InterpretML.
5. Performance: bounded JMeter and Locust tests against local demo endpoints.
6. Monitoring: Evidently and Giskard.
7. Incident response: Splunk and Elastic Security with synthetic events in an authorised lab.

## Acceptance checklist
- [ ] Official upstream references and pinned versions.
- [ ] Model/system and dataset provenance documented.
- [ ] Synthetic fixture or authorised target provided.
- [ ] Exact run instructions and prerequisites documented.
- [ ] Baseline, output, logs and exceptions retained.
- [ ] Limitations and threat-model assumptions documented.
- [ ] Clean-environment run verified before claiming reproducibility.
