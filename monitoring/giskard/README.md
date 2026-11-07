# Giskard — AI model and LLM application testing

## Purpose in the framework

Giskard's open-source library supports model and LLM application testing through scenarios, checks, test suites and supported scanning workflows. Current documentation distinguishes open-source library capabilities from Giskard Hub offerings; confirm features and API against the selected release.

## Assessment method

1. Identify the target: classical ML model, chatbot, RAG pipeline or agent; document its interface and expected behaviour.
2. Create a model/client wrapper or agent adapter supported by the selected Giskard version.
3. Define scenarios and checks for correctness, robustness, sensitive-data handling, prompt injection, harmful output or RAG grounding as appropriate.
4. For scanning workflows, select documented vulnerability or quality scan capability and required optional dependencies/provider configuration.
5. Review generated test cases and judge outputs; manually validate failures and rerun deterministic scenarios.
6. Record judge/provider, prompt, dataset, dependency and token/cost assumptions.

## User configuration

- Giskard version and open-source versus Hub scope
- Model/agent adapter and target endpoint
- Scenario definitions and checks
- Scan type and optional extras
- LLM judge/provider and credentials
- Knowledge base/reference documents for RAG checks
- Test budget, timeout and output storage

## Evidence to retain

- Test suite and scenario definitions
- Model/agent version and provider configuration
- Failed scenarios and sanitized conversations
- Judge configuration and rationale
- Manual adjudication and repeatability

## Example test catalogue

| Test ID | Objective | Evidence | Example interpretation |
|---|---|---|---|
| GIS-001 | Evaluate defined behavioural scenarios | Scenario/check pass-fail results | Identify responses violating expected system behaviour |
| GIS-002 | Run supported vulnerability scan | Hostile scenario failures and review | Investigate prompt injection, instruction leakage or policy failures |
| GIS-003 | Evaluate RAG grounding | Answer relevance/faithfulness checks | Identify unsupported or ungrounded answers |

## Sample report

See [sample_report.html](sample_report.html). This is a static illustrative example, not an executed assessment or measured result.

## Limitations and interpretation

- Capabilities differ by version and product offering; verify current documentation.
- LLM-as-judge checks can be inconsistent and may incur provider costs.
- Generated scans are not exhaustive; a clean run is not a security guarantee.
- RAG checks require appropriate reference documents and ground-truth assumptions.

Tool output is an observation. A confirmed finding requires reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without evidence.

## Official references

- Project: https://github.com/Giskard-AI/giskard
- Documentation: https://docs.giskard.ai/oss/
