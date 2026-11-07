# Garak — LLM security and red teaming

## Purpose in the framework

Garak is an LLM vulnerability scanner built around generators, probes, detectors, harnesses and evaluators. Depending on installed plugins and target support, it can probe for prompt injection, jailbreaks, data leakage, hallucination, misinformation and unsafe content generation.

## Assessment method

1. Define target boundary and written authorization; use a dedicated test endpoint and non-production credentials.
2. Select a supported generator/target adapter and confirm model/API compatibility.
3. Choose probes and detectors mapped to the threat model; record plugin names and versions.
4. Run bounded probe sets; preserve hit logs and sanitized transcripts.
5. Manually review detector hits against explicit security requirements and expected refusal behaviour.
6. Map validated behaviours to framework taxonomy and OWASP LLM risks only when evidence supports it.

## User configuration

- Generator/target type and model identifier
- Endpoint and authentication via secure configuration
- Probe and detector selection
- Harness and generation parameters
- Rate limits, timeouts and concurrency
- Test policy and synthetic canary values
- Output/hit-log handling

## Evidence to retain

- Garak version and plugin inventory
- Target configuration with secrets removed
- Probe/detector names and parameters
- Attempts, detector hits and sanitized transcripts
- Manual validation and limitations

## Example test catalogue

| Test ID | Objective | Evidence / metric | Example interpretation |
|---|---|---|---|
| LLM-RED-001 | Probe prompt-injection resistance | Probe hits and sanitized transcript | Untrusted content crosses an instruction boundary |
| LLM-RED-002 | Probe sensitive-data disclosure | Canary exposure and detector result | Protected test data is disclosed to an unauthorized context |
| LLM-RED-003 | Probe jailbreak/unsafe completion | Detector hit and reviewer decision | Output violates the defined safety/security policy |

## Sample report

See [sample_report.html](sample_report.html). It is a static illustrative report, not an executed assessment or measured result.

## Limitations and interpretation

- Coverage is plugin- and target-dependent, not exhaustive.
- Detectors can produce false positives/negatives and require adjudication.
- A hit is an observation, not automatically a confirmed vulnerability.
- Provider/model changes and application orchestration affect results.

Tool output is an observation. Confirmed findings require reproducible evidence of impact in the assessed context. Keep execution status separate from finding status; do not assign severity or OWASP mapping without supporting evidence.

## Official references

- Project: https://github.com/NVIDIA/garak
- Documentation: https://reference.garak.ai/

Check upstream documentation for current APIs, supported model interfaces, dependencies and licensing before configuration.
