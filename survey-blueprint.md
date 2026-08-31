# HERM Adoption Survey — Blueprint

**Status:** Draft  
**Audience:** EA practitioners at HE institutions  
**Distribution:** EUNIS to national organizations asking to distribute via member channels
**Last updated:** 2026-06-02

---

## Goals

1. Map who is using HERM and which artifacts, and for what problems
2. Identify transfer-worthy case studies for community sharing
3. Capture open questions practitioners have about HERM (future content direction)

---

## Question Flow (Branching Logic)

```
Section 1: Profile (everyone)
Section 2: Two independent screener questions (everyone)
  Q2.1: Practice EAM?  (Yes / Exploring / No)
  Q2.2: Use HERM?      (Yes / Exploring / No / Not familiar)

Derived routing based on answers:

  Q2.2 = Yes or Exploring                          → Section 3 (HERM Details)
    + Q2.1 = Yes or Exploring                      → Section 3, Q3.x includes EAM context questions
    + Q2.1 = No                                    → Section 3, skip EAM context questions
  → then Section 4 (Sharing) → END

  Q2.2 = No/Unfamiliar AND Q2.1 = Yes/Exploring   → Section 3b (Alternative Framework)
  → then Section 5 (Open Questions) → END

  Q2.2 = No/Unfamiliar AND Q2.1 = No              → Section 5 (Open Questions) → END
```

---

## Section 1: Profile
*Everyone answers — keep short*

| #   | Question                            | Type            | Notes                                                                    |
| --- | ----------------------------------- | --------------- | ------------------------------------------------------------------------ |
| 1.1 | Institution name                    | Text (optional) | Add: "Or describe anonymously (e.g. 'mid-size German university')"       |
| 1.2 | Country                             | Dropdown / Text | ISO country list or free text                                            |
| 1.3 | Institution type                    | Single select   | University / University of Applied Sciences / Research Institute / Other |
| 1.4 | Institution size (approx. students) | Single select   | <5k / 5–15k / 15–30k / >30k / n.a.                                       |
| 1.5 | Staff size (approx. headcount)      | Single select   | <500 / 500–1.5k / 1.5–5.0k / >5k / n.a.                                  |
| 1.6 | Your role                           | Multi select    | EA Architect / IT Strategist / CIO/IT Director / IT Project Lead / Other |
- [ ] check for good boundaries in student size and staff headcount
- [ ] follow-up topics
	- [ ] medical faculty or not
	- [ ] how broad is the spectrum of subjects -> double check importance of TU/full university vs university // school of arts or music
	- [ ] background of person
	- [ ] more details about the type of institution

---

## Section 2: Screener — EAM & HERM Practice
*Two independent questions — answer both is required*

| #   | Question                                                      | Type          | Options                                                                                    |
| --- | ------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------ |
| 2.1 | Does your institution practice Enterprise Architecture (EAM)? | Single select | Yes, established practice / We are exploring or just starting / No / Not familiar with EAM |
| 2.2 | Does your institution use HERM?                               | Single select | Yes, actively / We are exploring or piloting / No / Not familiar with HERM                 |
- [ ] add optional text field to specify exactly.
*Routing is derived from the combination of both answers — see flow diagram above.*
*Based on the answers in 2.1 and 2.2 we set the VAR to "HERM" / "EAM & HERM" / "EAM"*

---

## Section 3: EAM/HERM Usage Details
*For anyone who answered more than "Yes" or "Exploring" to Q2.2 (HERM use)*

| #       | Question                                                                           | Type                 | Condition                    | Notes                                                                                               |
| ------- | ---------------------------------------------------------------------------------- | -------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------- |
| 3.1     | Which EAM & HERM artifacts do you use?                                             | Multi-select         | Always, randomized order     | ARM / BRM / TRM / DRM / Business Model Canvas / SRM / Process Models / Value Streams / other (text) |
| 3.2 (C) | Primary Business Capability area of EAM & HERM adoption (if known)                 | Text                 | Only, if Q3.1 is not empty   | e.g. BC number or name — helps cross-reference HERM structure. Only if 3.1                          |
| 3.3     | What problem(s) are you solving with EAM & HERM?                                   | Multi-select + Other | Always, randomized order     | See options below                                                                                   |
| 3.4 (C) | Describe one successful solution scenario of the previous question in more detail. | Text                 | Only, if Q3.3 is not empty   |                                                                                                     |
| 3.5     | When did your institution start using EAM & HERM?                                  | Year (number)        | Always                       | Rough estimate is fine                                                                              |
| 3.6     | Current EAM & HERM adoption maturity                                               | Single select        | Always                       | Exploring / Pilot / Actively used / Embedded in governance / n.a.                                   |
| 3.7     | Is HERM embedded in your broader EAM practice?                                     | Single select        | Only if Q2.1 = Yes/Exploring | Yes, central to it / Partly / No, used standalone                                                   |
| 3.8     | What has worked well?                                                              | Text                 | Always                       | Optional but valuable                                                                               |
| 3.9     | What has been difficult or is missing?                                             | Text                 | Always                       | Optional but valuable                                                                               |
- [ ]  more generic on EA not HERM
- [ ] follow-up: Planing horizon

**Options for Q3.3 — Problems solved with HERM:**
- Structuring the application landscape (ARM)
- Defining / communicating business capabilities (BRM)
- Standardizing technology choices (TRM)
- Data governance / data architecture (DRM)
- Strategic planning / business model clarity (BMC)
- Service architecture / user focused design (SRM)
- Benchmarking against peer institutions
- Supporting merger / consolidation decisions
- Planing of change / risk scenarios (ISO27000)
- Communicating IT to non-IT stakeholders (Value Proposition)
- Accreditation / compliance documentation
- Structuring workflow / define responsibilities (Process Models) 
- Other (free text)

---
## Section 3a: Alternative EA Framework
*Only for respondents who indicate EA practice (2.1 either "Yes" or "Exploring")*

| #    | Question                                                            | Type                 | Notes                                                        |
| ---- | ------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------ |
| 3a.1 | Which EA framework(s) does your institution use?                    | Multi-select + Other | See options below                                            |
| 3a.2 | How long have you been using this framework?                        | Single select        | Less than 1 year / 1–3 years / 4–7 years / More than 7 years |
| 3a.3 | To which business unit / function is your EAM practice coupled most | Multi-select + Other | See options below                                            |

**Options for Q3a.1 — Frameworks in use:**
- TOGAF
- Zachman Framework
- ArchiMate (as modelling language)
- Custom / in-house framework
- No formal framework, ad hoc EA practice
- Other

**Options for Q3a.3 — EAM Coupling:**
- CIO
- dedicated EA Team
- Person on VP-level
- HR
- Finance
- Central IT
- CDO / Digital Office
- Other
## Section 3b: Why not (yet) HERM?
*Only for respondents who practice EA but do not use HERM (2.2 either "No" or "Not familiar with HERM")*

| #        | Question                                                       | Type                                                | Notes                                                                                                                  |
| -------- | -------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 3b.1     | Are you aware of HERM?                                         | Single select                                       | Yes, familiar / Heard of it / No                                                                                       |
| 3b.2     | What is the main reason you are not using HERM?                | Multi-select + Other                                | See options below                                                                                                      |
| 3b.3     | Would you consider adopting HERM?                              | Single select                                       | Yes, interested / Maybe, need more info / Unlikely / Definitely not. Better -> co pement or replace or ... as answers. |
| 3b.4 (C) | Would HERM act as...                                           | Single-select + Other (Only if 3b.3 is = Yes/Maybe) | complement / replacement / other (specify)                                                                             |
| 3b.5     | What would HERM need to offer for you to consider adopting it? | Text                                                | Optional — high value for roadmap/community content                                                                    |

**Options for Q3b.2 — Reasons for not using HERM:**
- Not aware of it until now
- Our current framework already meets our needs
- HERM is too complex / specific / doesn't fit our context
- Lack of tooling support for HERM
- No community or peer examples to learn from
- Switching cost too high
- Other

---

## Section 4: Knowledge Sharing
*Only for active users — "Exploring" respondents skip this*

| #   | Question                                                                   | Type             | Notes                                                 |
| --- | -------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------- |
| 4.1 | How transferable do you think your experience is to other HE institutions? | Single select    | High / Medium / Low / Uncertain                       |
| 4.2 | Are you interested in sharing knowledge with the community?                | Single select    | Yes / Maybe / No                                      |
| 4.3 | Contact email                                                              | Email (optional) | Only shown if 4.2 = Yes or Maybe                      |
| 4.4 | For which purpose would you like to be contacted                           | Multi select     | Only shown if 4.2 = Yes or Maybe, see selection below |
- [ ]  make a choice, for what reason to contact.
- [ ] later: tooling questions
*Note:* Respondents who rate transferability "High, medium" AND agree to share → flag for follow-up contact / activity.

**Options for Q4.4 — Reasons for providing contact:**
- Get to know the results of this survey
- Explain your EA tooling
- Provide more details about your use cases and scenarios
- Join a community workgroup on EAM / HERM
- Other

---

## Section 5: Open Questions & Barriers
*Everyone who is not actively using HERM*

| #   | Question                                                       | Type                 | Notes                                              |
| --- | -------------------------------------------------------------- | -------------------- | -------------------------------------------------- |
| 5.1 | What are your biggest open questions about EAM?                | Text                 | Core data for "what do practitioners need to know" |
| 5.2 | What is the main barrier to adopting HERM at your institution? | Multi-select + Other | Options below                                      |
| 5.3 | What would most help you move forward?                         | Text                 | Optional                                           |
- [ ] more generic EA not only HERM
**Options for Q5.2 — Barriers:**
- Lack of awareness / don't know HERM well enough
- No leadership support
- No EA practice at our institution yet
- Lack of time / capacity
- Unclear benefit vs. effort
- Lack of visibility of community 
- Lack of peer examples to learn from
- Other

---

## Design Decisions & Open Items

- [ ] Decide distribution tool (Google Forms / [LamaPoll](https://www.lamapoll.de/) / LimeSurvey / SurveyMonkey / Typeform / paper)
- [x] Confirm the 5 artifact names match current HERM documentation exactly ✅ 2026-06-02
- [x] Add SRM to artifact list once released — placeholder added in Q3.1
- [x] Decide whether institution name is truly optional (anonymization vs. case study richness tradeoff), yes, optional as much as possible ✅ 2026-06-02
- [ ] Add introduction and ethics/consent statement at the top
- [ ] Consider a short version (Sections 1–2–4 only, ~5 min) for conference distribution

---

## Estimated Completion Time

- Active HERM user: ~8–10 min
- Explorer: ~6–8 min
- Non-user: ~3–4 min
