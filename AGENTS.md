# Codex instructions — Mobile Antenna Align (MAA)

Read `docs/PROJECT_CONTEXT.md` before making architectural or product decisions.

## Mission
Make LTE/5G reception optimization accessible to people without specialist mobile-network or radio knowledge. Analyze **reception/radio metrics**, not the hardware itself, and translate them into understandable feedback and practical guidance.

## Current scope
- Home Assistant custom integration: `custom_components/mobile_antenna_align/`.
- The current router source is AVM FRITZ!Box via TR-064 / fritzconnection.
- The long-term design goal is vendor-independent; **do not claim that additional vendors are implemented**.
- Use `RadioMetrics` in `core/models/radio_metrics.py` as the common data model.
- Keep vendor-specific collection/parsing separate from generic analysis. Keep reusable analysis code independent of Home Assistant where practical.

## Working rules
- Work on `development`, not `main`; propose changes in small reviewable commits/PRs. Do not merge or create releases without explicit approval.
- Preserve existing functioning entities, unique IDs, configuration flows, and API behavior unless the change is expressly requested.
- Avoid editing the archived/legacy `fritz_5g` integration; it has been removed from the active repository.
- Never commit router passwords, credentials, serial numbers, or location-specific private data.
- Before changing code, inspect the actual repository files. Do not assume that proposed modules or features already exist.
- Run the available validation (Ruff, Python compile, hassfest/GitHub Actions) and add tests for new analysis algorithms.
- Treat missing radio metrics as missing data, not as zero; avoid misleading signal scores or throughput guarantees.
- Prefer one step and one terminal command at a time when guiding the project owner. Clearly identify whether an action belongs in Codespaces, GitHub, or Home Assistant.
- Distinguish **implemented**, **planned**, and **experimental** features in documentation.

## Product direction
- Planned: interpretable Signal Quality Score (SQS), reception ratings and explanations, actionable recommendations, guided antenna alignment, performance estimates, and later multi-vendor support.
- Do not infer antenna rotation direction, exact speeds, or geographic context from RSRP/RSRQ alone.
- Keep UX approachable: prioritize the next useful action over raw jargon.

## Project references
See `docs/PROJECT_CONTEXT.md` for mission wording, history, architecture, roadmap, and open questions.
