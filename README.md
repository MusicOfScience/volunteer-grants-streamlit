# Volunteer Grants Allocation Model

Current version: **v1.1.1**

A Streamlit web app for testing Volunteer Grants allocation scenarios.

## Main additions in v1.1.1

- Non-budget controls now recalculate live
- Budget lock / confirm retained
- Excel export now styles recommended allocation columns in light grey
- Excel export now styles totals rows in pale yellow

## Main additions already present from v1.1.0

- Budget Confirm / Lock control
- Undo budget control
- Undo / revert controls for the other settings
- Onscreen 2025–26 proposed recommendation view
- Committee-friendly allocation column names:
  - `RecommendedAllocation_Fair`
  - `RecommendedAllocation_Dynamic`
- Export totals and grand total rows
- Version labelling aligned across the app and exports

## Files

- `streamlit_app.py` — Streamlit front end
- `volunteer_grants_engine.py` — model engine
- `requirements.txt` — dependencies
- `CHANGELOG.md` — version history

## Deploy on Streamlit Community Cloud

## Documentation maintenance

When the app is updated, the documentation should be reviewed for consistency.

At minimum, update:
- CHANGELOG.md
- README.md

Where user-facing behaviour changes, also review:
- USER_GUIDE.md
- COMMITTEE_BRIEFING.md
- MODEL_DOCUMENTATION.md

Use this entrypoint:

```text
streamlit_app.py
```
