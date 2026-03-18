# Volunteer Grants Allocation Model

Current version: **v1.1.0**

A Streamlit web app for testing Volunteer Grants allocation scenarios.

## Main additions in v1.1.0

- Budget **Confirm / Lock** control
- Undo budget control
- Undo / revert controls for the other settings
- Onscreen **2025–26 proposed recommendation view**
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

Use this entrypoint:

```text
streamlit_app.py
```
