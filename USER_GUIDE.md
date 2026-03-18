# Volunteer Grants Allocation Model  
## One-Page User Guide

**What this app does**  
This app helps you test how a fixed Volunteer Grants budget could be distributed across eligible applicants.

It uses:
- current 2025–26 application data
- historic Volunteer Grants award data

It shows how different settings change the recommended amounts.

---

## Step 1 — Upload the files
Upload:
- the historic Volunteer Grants workbook
- the current applicants workbook

---

## Step 2 — Set and lock the budget
Enter the total available budget.

Click **Confirm / Lock budget**.

This is a safety feature. The app will not run the working scenario until the budget is confirmed.

---

## Step 3 — Adjust the model settings

### Protected threshold
Applications from **$1,000 up to this threshold** are funded in full.

### Haircut mode
Choose how to reduce larger requests:
- **Percentage** = reduce by a chosen %
- **Cap** = limit larger requests to a chosen ceiling

### Haircut rate
Only used with **Percentage** mode.

### Soft cap
Only used with **Cap** mode.

### Penalty weight
Controls how strongly prior Volunteer Grants success affects current priority.

### 2023–24 and 2024–25 weights
Control how much each prior year matters in the history weighting.

---

## Step 4 — Watch the results update
The app shows:
- a proposed 2025–26 recommendation view
- diagnostics
- comparison of Fair and Dynamic methods
- penalty impact
- validation checks

---

## What the two methods mean

### Fair
A flatter and more even distribution above the threshold floor.

### Dynamic
A more directly weighted distribution based on adjusted request size and historical weighting.

---

## Undo and revert tools

### Undo budget
Returns budget to the last confirmed amount.

### Undo other settings
Returns the other settings to the last confirmed values.

### Revert all to last confirmed scenario
Resets both budget and non-budget settings to the last confirmed state.

---

## What to look at first
Start with:
- **Proposed recommendation view**
- **Diagnostics**
- **Method Comparison**

These show the main effect of your changes.

---

## Good way to test scenarios
Change **one setting at a time**, for example:
- raise the protected threshold
- increase haircut rate
- increase the 2024–25 historic weighting

Then watch what changes.

---

## Exports
You can download:
- an XLSX workbook
- a CSV file

The XLSX export highlights:
- recommended allocation columns in light grey
- totals rows in pale yellow
