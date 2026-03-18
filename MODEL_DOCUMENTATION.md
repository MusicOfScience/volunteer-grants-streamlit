# Volunteer Grants Allocation Model  
## Detailed Documentation

## Introduction
This document explains how the Volunteer Grants Allocation Model was developed, why it was built, and how it now functions as a Streamlit application.

It begins with the office’s experience in the 2024–25 round, then explains how those lessons were refined into a more formal model for 2025–26.

---

## 1. Origin of the project

The origin of the model lies in the office’s practical experience administering and reviewing Volunteer Grants in 2024–25.

That earlier experience highlighted a number of recurring issues:
- how to balance small and large requests
- how to avoid very large applications dominating the available budget
- how to think about organisations that had been successful in previous rounds
- how to explain the basis of recommendations clearly
- how to test multiple scenarios without relying on ad hoc spreadsheet adjustments

These issues were not unique to one round. They pointed to a broader need for a structured, transparent, and reusable approach.

The office therefore revisited the prior round not simply to reproduce its outcomes, but to learn from it: to examine what had worked, what had caused confusion, and what would need to be improved if the process were to be made more robust and defensible.

---

## 2. From experience to model concept

The first stage of the work was conceptual rather than technical.

The core design question became:

**How can a fixed Volunteer Grants budget be distributed in a way that is transparent, explainable, and visibly fair, while still allowing the committee to exercise judgement?**

A number of basic principles emerged.

### 2.1 Protect small requests
There was a strong policy intuition that smaller requests should not be squeezed unfairly. This led to the concept of a **protected threshold**, below which requests are funded in full.

### 2.2 Shape larger requests
Larger requests should not be able to dominate the pool simply by virtue of their size. This led to the introduction of a **haircut** or **cap** mechanism.

### 2.3 Consider previous success, but only moderately
Previous Volunteer Grants success should matter, but should not become an exclusion rule. This led to the concept of a **moderate historical penalty**.

### 2.4 Keep the process committee-readable
The model needed to be understandable to non-technical decision-makers. This ruled out opaque or over-engineered approaches.

### 2.5 Support scenario testing
The committee should be able to adjust settings and immediately see how those choices affect the pattern of recommendations.

---

## 3. Building the first working model

The initial technical work focused on building a reusable allocation engine in Python, first tested in Google Colab.

This early work established:
- data cleaning logic
- safe numeric conversion
- duplicate handling
- budget reconciliation
- basic output workbook generation

It also surfaced weaknesses in early drafts, including:
- row duplication after merges
- over-budget outputs
- allocations drifting below intended threshold floors

These issues were valuable. They clarified that the model would need stronger validation, cleaner data handling, and a stricter allocation structure.

---

## 4. Refinement of the allocation logic

The model was progressively refined into a **floor-first** approach.

### 4.1 Protected band
Applications from **$1,000 up to the protected threshold** are funded in full.

### 4.2 Above-threshold floor
Applicants above the threshold should not end up with less than applicants just below the threshold. To prevent this, the model reserves the threshold amount as a floor for all above-threshold applicants before distributing any remaining budget.

### 4.3 Haircut or cap
Above-threshold applicants are then shaped using either:
- a percentage haircut
- or a cap

### 4.4 Historical penalty
Historic Volunteer Grants success is incorporated using:
- recency weighting across years
- scaled position within each year’s award distribution

This means history is treated as a modest, structured influence, not a binary flag.

---

## 5. Historical weighting design

One of the more important refinements was the distinction between two kinds of historical weighting.

### 5.1 Between-year weighting
The committee can decide how much the 2023–24 round matters relative to the 2024–25 round.

This allows the model to reflect the intuition that more recent funding may be more relevant than older funding.

### 5.2 Within-year weighting
Within a given year, the model does not rely only on raw past award values. Instead, it looks at where an applicant’s historical award sat within that year’s distribution.

This was adopted because it reflects relative prior success more effectively than simple dollar totals.

---

## 6. From notebook to Streamlit app

Once the core logic was working reliably, the next step was to make it usable in a web interface.

A Streamlit front end was then built on top of the model engine.

This turned the model into an interactive tool that allows users to:
- upload current and historic files
- set and lock the budget
- adjust live scenario settings
- compare outputs on screen
- export the results

The app was developed iteratively through versioned releases.

---

## 7. Version progression

### v1.0.0
The first working Streamlit deployment.

Included:
- model engine
- diagnostics
- method comparison
- penalty impact
- validation
- duplicate review
- export

### v1.1.0
Added:
- budget lock
- undo controls
- revert functions
- proposed recommendation view
- committee-friendly allocation column names
- export totals and grand total rows
- version labelling

### v1.1.1
Added:
- live recalculation for non-budget controls
- retained budget lock
- styled XLSX exports with:
  - light grey recommended allocation columns
  - pale yellow totals rows

---

## 8. Why Streamlit was chosen

Streamlit was selected because it offered:
- a web-based interface
- fast iteration
- easy scenario testing
- straightforward deployment through GitHub
- accessibility for non-technical users

This allowed the office to move from static spreadsheets and notebooks to a simple browser-based tool.

---

## 9. Current structure of the app

The app currently consists of:
- a **front end** (`streamlit_app.py`)
- a **model engine** (`volunteer_grants_engine.py`)
- deployment and documentation files (`README.md`, `CHANGELOG.md`, etc.)

This separation helps keep:
- the logic cleaner
- maintenance easier
- versioning clearer

---

## 10. How the model currently works

The current version of the model performs the following steps.

### 10.1 Read and clean the data
It reads the historic and current workbooks, standardises names and ABNs, converts dates and numeric values, and removes unusable rows.

### 10.2 Remove duplicate current submissions
Where multiple current submissions exist for the same applicant, it keeps the latest one.

### 10.3 Match history to current applicants
It matches prior-year awards to current applicants using ABN first, then organisation name.

### 10.4 Protect smaller applications
All requests from $1,000 up to the protected threshold are funded in full.

### 10.5 Shape larger applications
Requests above the threshold are adjusted using either the chosen haircut or cap rule.

### 10.6 Apply historical weighting
Historic awards are incorporated using recency and within-year distribution position.

### 10.7 Allocate the remaining budget
The model calculates:
- a Fair allocation
- a Dynamic allocation

### 10.8 Validate and export
It checks totals, prepares review tables, and exports styled workbook outputs.

---

## 11. What the committee should understand

The model is best understood as a structured scenario tool.

It allows the committee to:
- see trade-offs
- test assumptions
- understand why outcomes change
- document the basis of recommendations

It does not eliminate the need for committee oversight.

That is a feature, not a flaw. The aim is transparent support, not false automation.

---

## 12. Why this matters

The development of this model represents a shift from:
- reactive spreadsheet adjustment
to
- structured, documented, and reusable allocation modelling

In that sense, the app is not just a technical tool. It is an administrative and governance improvement built from direct experience of the previous funding round.

It turns the lessons of 2024–25 into a more mature process for 2025–26 and beyond.

---

## 13. Future potential
The current app already provides a strong base. Future enhancements could include:
- improved charts
- enhanced submission exports
- additional diagnostics
- easier committee presets
- more polished documentation within the app itself

But the core work has already been done: the office now has a functioning, transparent, versioned allocation tool built from lived operational experience.
