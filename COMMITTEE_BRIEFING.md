# Volunteer Grants Allocation Model  
## Committee Briefing Note

**Purpose**  
This briefing note explains the purpose, logic, and use of the Volunteer Grants Allocation Model developed for the 2025–26 round. The model is intended to support transparent, consistent, and testable allocation scenarios within the available budget. It is not a substitute for committee judgement, but a structured tool to assist decision-making.

**Background**  
The model was developed in response to lessons from the previous Volunteer Grants round. In 2024–25, the office and committee worked through a range of issues common to small discretionary grants programs, including balancing smaller and larger requests, considering the effect of prior grant success, and explaining the basis on which different funding patterns might emerge.

That experience made clear that a more formal and transparent modelling tool would be useful. The current Streamlit app builds on that experience. It takes the previous round’s practical issues and turns them into a structured, repeatable system for scenario testing.

**What the model does**  
The model reads:
- the current 2025–26 applicant workbook
- the historic Volunteer Grants workbook containing prior-year award amounts

It then:
1. cleans and standardises the data
2. removes duplicate current submissions by retaining the latest valid version
3. matches current applicants to historic Volunteer Grants data
4. protects smaller requests up to a chosen threshold
5. shapes larger requests using either a percentage haircut or a cap
6. applies a moderate historical weighting based on prior Volunteer Grants success
7. distributes the budget using two alternative allocation methods
8. presents the results on screen and through exportable workbooks

**Core policy logic**  
The model is designed around five principles:

1. **Stay within the available budget**  
   The total recommendations must reconcile to the budget set by the office or committee.

2. **Protect smaller requests**  
   Requests from $1,000 up to the chosen protected threshold are funded in full.

3. **Prevent larger requests from dominating the pool**  
   Requests above the threshold are shaped using either a percentage haircut or a cap.

4. **Recognise prior Volunteer Grants support without excluding applicants**  
   The model applies a moderate penalty where an organisation has received relatively strong prior Volunteer Grants support, especially in the more recent round.

5. **Produce recommendations that can be explained clearly**  
   The purpose is not to generate a perfect mathematical answer, but to produce outcomes that are defensible, testable, and transparent.

**Historical weighting**  
Historic Volunteer Grants funding is included as a moderate weighting factor only.

Two prior rounds are considered:
- 2023–24
- 2024–25

The committee can adjust how much each year matters. Within each year, the model does not simply use raw dollar values. Instead, it considers where an organisation’s historic award sat within that year’s overall distribution. This means an organisation that received a relatively high award in a historical round carries more historical weight than one that received a relatively low award in that round.

**Allocation methods**  
The model provides two methods:

**Fair**  
A flatter and more even distribution of the available money above the threshold floor.

**Dynamic**  
A more directly weighted distribution based on adjusted request size and historical weighting.

The app allows the committee to compare these two views and see where they produce similar or different recommendations.

**Controls available in the app**  
The committee can test scenarios by adjusting:
- total budget
- protected threshold
- minimum application
- haircut mode
- haircut rate
- cap level
- penalty weight
- 2023–24 weight
- 2024–25 weight

The budget itself is locked through a confirm mechanism, while the non-budget settings can be adjusted live for scenario testing.

**Why this is useful**  
The model gives the committee a practical way to:
- explore trade-offs openly
- understand how settings influence recommendations
- compare alternative allocation patterns
- document and explain the basis for recommendations

**Limitations**  
The model does not replace committee judgement. It does not independently decide:
- legal eligibility
- organisational merit
- policy desirability
- local strategic priorities
- whether exceptional circumstances justify overriding the model

It should be understood as a decision-support and transparency tool.

**Recommended use**  
The model should be used to test and discuss allocation scenarios, not to treat one output as automatically final. The committee should use it alongside qualitative judgement, known local context, and any administrative screening decisions.
