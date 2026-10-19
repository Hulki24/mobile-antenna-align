# Mobile Antenna Align (MAA) — Project Context

## Official mission statement
> Mobile Antenna Align (MAA) is designed to help everyone achieve the best possible LTE and 5G mobile signal, even without in-depth knowledge of mobile networks or radio technology. It transforms complex radio metrics into easy-to-understand insights and practical recommendations.

This wording was explicitly agreed upon. The goal is **good reception without requiring deep mobile-radio expertise**.

## Project description and philosophy
MAA aims to be a vendor-independent Home Assistant integration that analyzes LTE and 5G **radio/reception metrics** and ultimately helps users optimize reception according to their equipment and location. It does **not** analyze the devices themselves. Equipment and location are potential context for recommendations, not substitutes for actual measured reception data.

Design principle: Turn reception data into actionable, understandable advice. Explanations should be transparent and useful to non-specialists.

## Confirmed history
- Started as an AVM FRITZ!Box LTE/5G Home Assistant integration using TR-064 and `fritzconnection`.
- Created `custom_components/mobile_antenna_align` as a separate integration, initially copied from `fritz_5g`, while preserving a functioning fallback in the Home Assistant installation (`fritz_5g_safe`).
- Moved the data pipeline toward a manufacturer-independent `RadioMetrics` dataclass.
- Corrected the LTE PCI field to `lte_pci`.
- Fixed integration issues and achieved a functioning MAA setup in Home Assistant, according to project-owner tests.
- Removed legacy `custom_components/fritz_5g` from the active repository.
- Updated GitHub Actions validation (hassfest, Ruff, compileall); project owner reported the workflow green.
- Renamed GitHub repository from `Hulki24/ha-fritzbox-mobile` to `Hulki24/mobile-antenna-align`.
- Merged `development` into `main` through a passing PR, then fast-forwarded local `development` to `main`.
- Development workflow: `development` for ongoing work, `main` for stable reviewed work; use PRs and passing CI.
- Historical tags include `v0.1.0a2` and `v0.1.0a3`. Verify the current manifest and tags before publishing a release.

## Current architecture (verify against code)
```text
FRITZ!Box TR-064
    -> AVM-specific API/parser
    -> RadioMetrics
    -> DataUpdateCoordinator
    -> Home Assistant sensor entities

Future:
    RadioMetrics -> generic analysis engine -> SQS/explanations/recommendations
```

Key repository paths:
- `custom_components/mobile_antenna_align/api.py`
- `custom_components/mobile_antenna_align/coordinator.py`
- `custom_components/mobile_antenna_align/sensor.py`
- `custom_components/mobile_antenna_align/core/models/radio_metrics.py`
- `custom_components/mobile_antenna_align/manifest.json`
- `.github/workflows/validate.yml`

`RadioMetrics` includes LTE/NR RSRP, RSRQ, RSSI, cell IDs and other optional fields. Inspect its current definition for exact field names and types.

## Roadmap — proposed, not yet delivered
1. **Analysis Engine:** SQS (0–100) and human-readable ratings, explainable component evaluations. Start with measured metrics that exist; missing values must not silently inflate scores.
2. **Recommendation Engine:** Plain-language improvement guidance grounded in measured changes; avoid pretending one snapshot reveals which direction to rotate.
3. **Live Alignment:** Interactive measurement/position comparison, trends, and feedback during antenna adjustment.
4. **Performance:** Investigate upload/download/latency estimates, clearly labeled as estimates with uncertainty; do not present radio values as reliable speed predictions.
5. **Equipment/location context and multi-vendor adapters:** Future enhancements, not currently supported by the initial AVM adapter.
6. **Other clients:** Potential future Android, iOS, web or desktop uses of reusable analysis logic.

Proposed modular structure (check existence before creating):
```text
core/analysis/
    __init__.py
    signal_quality.py
    scoring.py
    weights.py
```
This is a plan, not proof these modules have been implemented.

## SQS design decisions still open
- Which metrics are available for each LTE/5G technology and router?
- How should missing values affect confidence and score?
- How should LTE and 5G NSA be combined without double-counting?
- How to calibrate scoring thresholds and weights empirically?
- Should stability be measured over a time window?
- Which recommendations can be justified from data alone?

Previous numerical weights and scoring examples were **illustrative proposals**, not validated scientific thresholds or approved final specifications.

## Collaboration preferences
- Give the owner **one copyable terminal command per message/step**.
- Always state the environment: **Codespaces**, **GitHub**, or **Home Assistant**.
- Prefer complete files for larger edits, minimize manual patching, and verify each stage before proceeding.
- Protect the working Home Assistant installation and existing sensors.
- Keep user-facing explanations in German when collaborating with the owner; project-facing documentation and code may be in English.

## Documentation accuracy
Do not describe SQS, recommendation engine, speed predictions, antenna guidance, or multi-vendor support as already shipped until confirmed in code and tested. The mission is a product goal, not a claim that all functions already exist.
