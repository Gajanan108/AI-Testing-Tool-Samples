# Safe use

- Test only systems, models, data and endpoints you own or are explicitly authorised to assess.
- Prefer synthetic fixtures and local test services.
- Keep load tests bounded and use only approved test systems.
- Do not run Garak, TextAttack or other adversarial tests against third-party production services without written authorisation.
- Never commit API keys, access tokens, passwords, customer data, private prompts or proprietary model artefacts.
- Redact sensitive values from logs and reports.
- Use local labs or authorised tenants and synthetic events for Splunk and Elastic demonstrations.
- Document destructive, expensive, rate-limited or externally visible behaviour before execution.
