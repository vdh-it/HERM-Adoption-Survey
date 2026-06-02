# HERM Adoption Survey — Blueprint

**Status:** Draft  
**Audience:** EA practitioners at HE institutions  
**Distribution:** TBD  
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
| 1.4 | Institution size (approx. students) | Single select   | <5k / 5–15k / 15–30k / >30k / N/A                                        |
| 1.5 | Your role                           | Single select   | EA Architect / IT Strategist / CIO/IT Director / IT Project Lead / Other |

---

## Section 2: Screener — EAM & HERM Practice
*Two independent questions — answer both*

| #   | Question                                               | Type          | Options                                                                 |
| --- | ------------------------------------------------------ | ------------- | ----------------------------------------------------------------------- |
| 2.1 | Does your institution practice Enterprise Architecture (EAM)? | Single select | Yes, established practice / We are exploring or just starting / No     |
| 2.2 | Does your institution use HERM?                        | Single select | Yes, actively / We are exploring or piloting / No / Not familiar with HERM |

*Routing is derived from the combination of both answers — see flow diagram above.*

---

## Section 3: HERM Usage Details
*For anyone who answered "Yes" or "Exploring" to Q2.2 (HERM use)*

| #   | Question                                              | Type                 | Condition         | Notes                                                         |
| --- | ----------------------------------------------------- | -------------------- | ----------------- | ------------------------------------------------------------- |
| 3.1 | Which HERM artifacts do you use?                      | Multi-select         | Always            | ARM / BRM / TRM / DRM / Business Model Canvas / SRM (planned) |
| 3.2 | Primary Business Capability area (if known)           | Text (optional)      | Always            | e.g. BC number or name — helps cross-reference HERM structure |
| 3.3 | What problem(s) are you solving with HERM?            | Multi-select + Other | Always            | See options below                                             |
| 3.4 | When did your institution start using HERM?           | Year (number)        | Always            | Rough estimate is fine                                        |
| 3.5 | Current HERM adoption maturity                        | Single select        | Always            | Exploring / Pilot / Actively used / Embedded in governance    |
| 3.6 | Is HERM embedded in your broader EAM practice?        | Single select        | Only if Q2.1 = Yes/Exploring | Yes, central to it / Partly / No, used standalone  |
| 3.7 | What has worked well?                                 | Text (free)          | Always            | Optional but valuable                                         |
| 3.8 | What has been difficult or is missing?                | Text (free)          | Always            | Optional but valuable                                         |

**Options for Q3.3 — Problems solved with HERM:**
- Structuring the application landscape (ARM)
- Defining / communicating business capabilities (BRM)
- Standardizing technology choices (TRM)
- Data governance / data architecture (DRM)
- Strategic planning / business model clarity (BMC)
- Benchmarking against peer institutions
- Supporting merger / consolidation decisions
- Communicating IT to non-IT stakeholders
- Accreditation / compliance documentation
- Other (free text)

---

## Section 3b: Alternative EA Framework
*Only for respondents who practice EA but do not use HERM*

| #    | Question                                                         | Type                 | Notes                                                                  |
| ---- | ---------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------- |
| 3b.1 | Which EA framework(s) does your institution use?                 | Multi-select + Other | See options below                                                      |
| 3b.2 | How long have you been using this framework?                     | Single select        | Less than 1 year / 1–3 years / 4–7 years / More than 7 years          |
| 3b.3 | Are you aware of HERM?                                          | Single select        | Yes, familiar / Heard of it / No                                       |
| 3b.4 | What is the main reason you are not using HERM?                 | Multi-select + Other | See options below                                                       |
| 3b.5 | Would you consider HERM as a complement or replacement?         | Single select        | Yes, interested / Maybe, need more info / Unlikely / Definitely not    |
| 3b.6 | What would HERM need to offer for you to consider adopting it?  | Text (free)          | Optional — high value for roadmap/community content                    |

**Options for Q3b.1 — Frameworks in use:**
- TOGAF
- Zachman Framework
- ArchiMate (as modelling language)
- Custom / in-house framework
- No formal framework, ad hoc EA practice
- Other

**Options for Q3b.4 — Reasons for not using HERM:**
- Not aware of it until now
- Our current framework already meets our needs
- HERM is too HE-specific / doesn't fit our context
- Lack of tooling support for HERM
- No community or peer examples to learn from
- Switching cost too high
- Other

---

## Section 4: Knowledge Sharing
*Only for active users — "Exploring" respondents skip this*

| #   | Question                                                                   | Type             | Notes                            |
| --- | -------------------------------------------------------------------------- | ---------------- | -------------------------------- |
| 4.1 | How transferable do you think your experience is to other HE institutions? | Single select    | High / Medium / Low / Uncertain  |
| 4.2 | Would you be willing to share more about your case for the community?      | Single select    | Yes / Maybe / No                 |
| 4.3 | If yes: contact email                                                      | Email (optional) | Only shown if 4.2 = Yes or Maybe |

*Note:* Respondents who rate transferability "High" AND agree to share → flag for follow-up interview.

---

## Section 5: Open Questions & Barriers
*Everyone who is not actively using HERM*

| #   | Question                                                       | Type                 | Notes                                              |
| --- | -------------------------------------------------------------- | -------------------- | -------------------------------------------------- |
| 5.1 | What are your biggest open questions about HERM?               | Text (free)          | Core data for "what do practitioners need to know" |
| 5.2 | What is the main barrier to adopting HERM at your institution? | Multi-select + Other | Options below                                      |
| 5.3 | What would most help you move forward?                         | Text (free)          | Optional                                           |

**Options for Q5.2 — Barriers:**
- Lack of awareness / don't know HERM well enough
- No internal champion or leadership support
- No EA practice at our institution yet
- Lack of time / capacity
- Unclear benefit vs. effort
- No community or peer examples to learn from
- Other

---

## Design Decisions & Open Items

- [ ] Decide distribution tool (Google Forms / LimeSurvey / Typeform / paper)
- [ ] Confirm the 5 artifact names match current HERM documentation exactly
- [ ] Add SRM to artifact list once released — placeholder added in Q3.1
- [ ] Decide whether institution name is truly optional (anonymization vs. case study richness tradeoff)
- [ ] Add ethics/consent statement at the top if submitting to any academic venue
- [ ] Consider a short version (Sections 1–2–4 only, ~5 min) for conference distribution

---

## Estimated Completion Time

- Active HERM user: ~8–10 min
- Explorer: ~6–8 min
- Non-user: ~3–4 min
