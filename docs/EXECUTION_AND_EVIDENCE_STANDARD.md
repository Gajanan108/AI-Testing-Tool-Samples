# Execution and evidence standard

## Execution states
- **PLANNED:** included in roadmap, not started.
- **NOT_APPLICABLE:** model/interface or prerequisites do not support it.
- **SKIPPED:** deliberately not run; reason recorded.
- **ATTEMPTED:** execution was initiated.
- **EXECUTED:** intended tool operation ran and produced inspectable output.
- **FAILED:** execution failed; preserve exception and do not claim success.

A listed test is not an executed test. A successful process exit alone is insufficient if the intended operation did not occur.

## Finding states
- **Observation:** raw behaviour or metric recorded.
- **Potential finding:** possible security significance; validation remains.
- **Confirmed finding:** reproducible evidence demonstrates security impact within the threat model.
- **False positive:** investigation found insufficient evidence.
- **Not a finding:** expected behaviour or outside scope.

Keep execution status separate from finding status; do not force true/false before validation.

## Minimum evidence
Record tool/version, model/system/version, fixture identifier, timestamp, configuration, test ID, invocation, execution state, output and log locations, exceptions, baseline and test observations, repeatability, limitations and reviewer. Never publish credentials, personal data, confidential prompts, customer payloads or proprietary weights.
