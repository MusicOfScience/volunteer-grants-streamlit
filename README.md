# Volunteer Grants Allocation Model

Current version: **v1.1.2**

A Streamlit web app for testing Volunteer Grants allocation scenarios.

## Main additions in v1.1.2

- Supports `ID` and `Id` in the current workbook
- Preserves `Last modified time` and uses it as the first-choice timestamp
- Excludes rows marked `N` / `NO` in `Eligible?` from the live model
- Adds onscreen **Eligibility & Duplicate Review**
- Adds XLSX export sheets for:
  - Included in Model
  - Excluded by Eligibility
  - Duplicate Review

## Previous additions

### v1.1.1
- Non-budget controls recalculate live
- Budget lock retained
- XLSX export styles recommended allocation columns in light grey
- XLSX export styles totals rows in pale yellow

### v1.1.0
- Budget Confirm / Lock control
- Undo budget control
- Undo / revert controls for other settings
- Onscreen 2025–26 proposed recommendation view
- Committee-friendly allocation column names
- Export totals and grand total rows
- Version labelling aligned across the app and exports

## Files

- `streamlit_app.py` — Streamlit front end
- `volunteer_grants_engine.py` — model engine
- `requirements.txt` — dependencies
- `CHANGELOG.md` — version history
- documentation Markdown files as needed

## Deploy on Streamlit Community Cloud

Use this entrypoint:

```text
streamlit_app.py
```
