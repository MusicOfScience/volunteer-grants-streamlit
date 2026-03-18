# Changelog

## v1.1.2
- Added support for `ID` and `Id` in current workbook ingestion
- Preserved `Last modified time` and made it the first-choice timestamp
- Excluded rows marked `N` / `NO` in `Eligible?` from the live model
- Added onscreen Eligibility & Duplicate Review
- Added XLSX sheets for Included in Model, Excluded by Eligibility, and Duplicate Review
- Improved duplicate handling and audit visibility

## v1.1.1
- Changed non-budget controls to recalculate live
- Retained budget Confirm / Lock behaviour
- Added light grey styling to recommended allocation columns in XLSX export
- Added pale yellow styling to totals rows in XLSX export

## v1.1.0
- Added budget Confirm / Lock behaviour
- Added Undo budget control
- Added revert controls for the other settings
- Added onscreen 2025–26 proposed recommendation view
- Added committee-friendly recommended allocation column names
- Added totals and grand total rows to export views
- Added version label alignment across app, README, code comments, and exports

## v1.0.0
- Initial working Streamlit deployment
- Included model engine, diagnostics, method comparison, penalty impact, validation, duplicate review, and export
