# HERM Adoption Survey — Blueprint

**Status:** Draft  
**Audience:** EA practitioners at HE institutions  
**Distribution:** EUNIS to national organizations asking to distribute via member channels
**Last updated:** 2026-08-31

---

## Goals

1. Map who is using HERM and which artifacts, and for what problems
2. Identify transfer-worthy case studies for community sharing
3. Capture open questions practitioners have about HERM (future content direction)

---

## Question Flow (Branching Logic)

Two core research questions must be answerable **independently, including in combination** — an institution can use HERM *and* another framework at the same time (e.g. HERM as content model, ArchiMate as notation):

1. How is HERM used? → Section 3
2. Which other/alternative EA framework(s) are used? → Section 3a

Routing into Sections 3 / 3a / 3b is driven by **set membership** in Q2.3 (which framework(s) are in use), not by mutually exclusive branches. This replaces the earlier either/or tree, which could not represent a HERM+TOGAF respondent at all.

```
Section 1: Profile (everyone)
Section 2: Screener (everyone)
  Q2.1  Practice EAM?                     (Yes / Exploring / No / Not familiar)
  Q2.2  Use HERM?                         (Yes / Exploring / No / Not familiar)
        — kept as a universal question purely for the HERM-awareness headline
          metric across ALL respondents; it does NOT drive routing.
  Q2.3  Which EA framework(s) are in use?  Multi-select, includes HERM as an
        option; shown if Q2.1 = Yes/Exploring — this drives the routing below.

Routing (independent conditions — several can be true at once):

  HERM ∈ Q2.3 selection                          → Section 3  (HERM Usage Details)
  (Q2.3 selection \ {HERM}) is non-empty          → Section 3a (Other Framework Details)
  HERM ∉ Q2.3 selection AND Q2.1 = Yes/Exploring  → Section 3b (Why not (yet) HERM?)

Section 4: Sharing — internally split, see Section 4 below:
  Part A (naming consent)   → everyone who gave an institution name in Q1.1
  Part B (follow-up contact) → gated on an engagement flag (Section 3/3a/3b
                                 signals), not on which branch was taken

Section 5: Open Questions & Barriers
  → everyone who did NOT trigger the Section 4 Part B engagement flag
    (i.e. limited or no active EA/HERM engagement) — catch-all wrap-up
  → Q5.2 specifically is suppressed for anyone who saw Section 3b
    (3b.1 already covers "reasons for not using HERM"); 5.1/5.3 still apply

→ END
```

A respondent using HERM *and* TOGAF sees both Section 3 and Section 3a — this is intentional and is exactly how co-occurrence gets captured, which the previous exclusive-branch design could not do.

**Trade-off, deliberately accepted:** this has more conditional logic than the previous exclusive-branch tree (independent set-membership checks instead of four fixed paths). The payoff is that core question 2 (which frameworks, including alongside HERM) becomes answerable at all, and no EA-practicing/non-HERM respondent is silently dropped from Section 4. Confirm the chosen survey tool can express multi-select-driven branching and a flag combining answers from three different sections (see Design Decisions below).

---

## Section 1: Profile
*Everyone answers — keep short*

| #   | Question                            | Type            | Notes                                                                    |
| --- | ----------------------------------- | --------------- | ------------------------------------------------------------------------ |
| 1.1 | Institution name                    | Text (optional) | Add: "Or describe anonymously (e.g. 'mid-size German university')"       |
| 1.2 | Country                             | Dropdown / Text | ISO country list or free text                                            |
| 1.3 | Institution type                    | Single select   | University / University of Applied Sciences / Research Institute / Other |
| 1.4 | Institution size (approx. students) | Single select   | <2k / 2–10k / 10–30k / >30k / n.a.                                       |
| 1.5 | Staff size (approx. headcount)      | Single select   | <200 / 200–1k / 1–3k / >3k / n.a.                                        |
| 1.6 | Your role                           | Multi select    | EA Architect / IT Strategist / CIO/IT Director / IT Project Lead / Other |
- [ ] check for good boundaries in student size and staff headcount

---

## Section 2: Screener — EAM & HERM Practice
*Q2.1 and Q2.2 are always required; Q2.3 is required if Q2.1 = Yes/Exploring*

| #   | Question                                                      | Type          | Options                                                                                                                                                            |
| --- | -------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1 | Does your institution practice Enterprise Architecture (EAM)? | Single select | Yes, established practice / We are exploring or just starting / No / Not familiar with EAM                                                                       |
| 2.2 | Does your institution use HERM?                               | Single select | Yes, actively / We are exploring or piloting / No / Not familiar with HERM                                                                                        |
| 2.3 | Which EA framework(s) does your institution use or pilot?     | Multi-select  | HERM / TOGAF / Zachman Framework / ArchiMate (as modelling language) / Custom / in-house framework / No formal framework, ad hoc EA practice / Other (text). Shown only if Q2.1 = Yes/Exploring |

- [x] add optional text field to specify exactly — covered by "Other" free text on Q2.3 ✅ 2026-08-31

*Q2.2 is kept purely for the HERM-awareness metric across all respondents, including those without EA practice — it is not a routing condition.*
*Routing into Sections 3 / 3a / 3b is derived from Q2.3 membership combined with Q2.1 — see flow diagram above.*
*Based on the combination of Q2.1 / Q2.2 / Q2.3 we set the VAR to "HERM" / "EAM & HERM" / "EAM"*

---

## Section 3: HERM Usage Details
*Shown if HERM is among the frameworks selected in Q2.3*

| #       | Question                                                                           | Type                 | Condition                    | Notes                                                                                               |
| ------- | ---------------------------------------------------------------------------------- | -------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------- |
| 3.1     | Which HERM artifacts do you use?                                                   | Multi-select         | Always, randomized order     | ARM / BRM / TRM / DRM / Business Model Canvas / SRM / Process Models / Value Streams / other (text) |
| 3.2 (C) | Primary Business Capability area of HERM adoption (if known)                       | Text                 | Only if Q3.1 is not empty    | e.g. BC number or name — helps cross-reference HERM structure                                       |
| 3.3     | What problem(s) are you solving with HERM?                                         | Multi-select + Other | Always, randomized order     | See options below                                                                                   |
| 3.4 (C) | Describe one successful solution scenario of the previous question in more detail. | Text                 | Only if Q3.3 is not empty    |                                                                                                     |
| 3.5     | When did your institution start using HERM?                                        | Year (number)        | Always                       | Rough estimate is fine                                                                              |
| 3.6     | Current HERM adoption maturity                                                     | Single select        | Always                       | Exploring / Pilot / Actively used / Embedded in governance / n.a.                                   |
| 3.7     | Is HERM embedded in your broader EAM practice?                                     | Single select        | Only if Q2.1 = Yes/Exploring | Yes, central to it / Partly / No, used standalone                                                   |
| 3.8(\*) | What has worked well?                                                              | Text                 | Always                       | Optional but valuable                                                                               |
| 3.9     | What has been difficult or is missing?                                             | Text                 | Always                       | Optional but valuable                                                                               |

(\*) maybe, we leave this out after pretest.

- [x] more generic on EA not HERM — resolved by keeping this section strictly HERM-scoped and giving general-EA content its own module (Section 3a), instead of merging the labels ✅ 2026-08-31

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
## Section 3a: Other EA Framework Details
*Shown if at least one non-HERM framework was selected in Q2.3 — independent of Section 3, so it can co-occur with it (HERM + another framework case)*

| #    | Question                                                              | Type                 | Notes                                                          |
| ---- | ------------------------------------------------------------------------ | -------------------- | ----------------------------------------------------------------- |
| 3a.1 | How long have you been using the framework(s) selected above?            | Single select        | Less than 1 year / 1–3 years / 4–7 years / More than 7 years    |
| 3a.2 | To which business unit / function is your EAM practice coupled most?     | Multi-select + Other | See options below                                                |

*Which framework(s) are in use is already captured in Q2.3 — this section only adds detail and deliberately does not re-ask the framework list.*

**Options for Q3a.2 — EAM Coupling:**
- CIO
- dedicated EA Team
- Person on VP-level
- HR
- Finance
- Central IT
- CDO / Digital Office
- Other

## Section 3b: Why not (yet) HERM?
*Shown if HERM was NOT selected in Q2.3, AND Q2.1 = Yes/Exploring*

| #        | Question                                                       | Type                                                 | Notes                                                                |
| -------- | ------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------ |
| 3b.1     | What is the main reason you are not using HERM?                    | Multi-select + Other                                     | See options below                                                        |
| 3b.2     | Would you consider adopting HERM?                                   | Single select                                            | Yes, interested / Maybe, need more info / Unlikely / Definitely not     |
| 3b.3 (C) | Would HERM act as...                                                | Single-select + Other (Only if 3b.2 is = Yes/Maybe)      | complement / replacement / other (specify)                              |
| 3b.4     | What would HERM need to offer for you to consider adopting it?      | Text                                                     | Optional — high value for roadmap/community content                     |

*Dropped the earlier "Are you aware of HERM?" question here — Q2.2 already captures HERM awareness across all respondents, and its "Not familiar" state combined with the Q2.3 routing already determines that this section applies.*

**Options for Q3b.1 — Reasons for not using HERM:**
- Not aware of it until now
- Our current framework already meets our needs
- HERM is too complex / specific / doesn't fit our context
- Lack of tooling support for HERM
- No community or peer examples to learn from
- Switching cost too high
- Other

---

## Section 4: Knowledge Sharing & Contact
*Split into two independently-gated parts — see rationale below*

**Part A — Naming consent**
*Shown to everyone who provided an institution name in Q1.1 — ungated, required for GDPR-compliant publication regardless of branch (see `Draft-Letter2EUNISBoard.md`, which commits to asking this)*

| #   | Question                                                  | Type          | Notes                                                        |
| --- | ------------------------------------------------------------ | ------------- | ----------------------------------------------------------------- |
| 4.1 | May your institution be named in the published dataset?      | Single select | Yes, may be named / No, anonymize or aggregate only               |

**Part B — Follow-up contact**
*Shown if the "engagement flag" is set — i.e. any of the following holds, regardless of which branch produced it:*
- Q3.6 (HERM maturity) ∈ {Pilot, Actively used, Embedded in governance}, or
- Q3a.1 was answered (an other-framework is in active use), or
- Q3b.2 (adoption interest) ∈ {Yes interested, Maybe}

| #   | Question                                                                   | Type             | Notes                                                 |
| --- | ---------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| 4.2 | How transferable do you think your experience is to other HE institutions? | Single select    | High / Medium / Low / Uncertain                       |
| 4.3 | Are you interested in sharing knowledge with the community?                 | Single select    | Yes / Maybe / No                                       |
| 4.4 | Contact email                                                                | Email (optional) | Only shown if 4.3 = Yes or Maybe                       |
| 4.5 | For which purpose would you like to be contacted                            | Multi select     | Only shown if 4.3 = Yes or Maybe, see selection below  |

- [ ]  make a choice, for what reason to contact.

*Note:* Respondents who rate transferability "High, Medium" AND agree to share → flag for follow-up contact / activity. Gating Part B on the engagement flag rather than on the HERM/non-HERM branch ensures EA-practicing institutions without HERM are not silently dropped from the recruitment funnel described in `Draft-Letter2EUNISBoard.md` (deliverables 3–7: follow-up interviews, workshops).

**Options for Q4.5 — Reasons for providing contact:**
- Get to know the results of this survey
- Explain your EA tooling
- Provide more details about your use cases and scenarios
- Join a community workgroup on EAM / HERM
- Other

---

## Section 5: Open Questions & Barriers
*Everyone who did NOT trigger the Section 4 Part B engagement flag — i.e. limited or no active EA/HERM engagement; this is the catch-all wrap-up*

| #   | Question                                                       | Type                 | Condition                              | Notes                                                    |
| --- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| 5.1 | What are your biggest open questions about EAM?                    | Text                 | Always                                      | Core data for "what do practitioners need to know"            |
| 5.2 | What is the main barrier to adopting HERM at your institution?     | Multi-select + Other | Only if Section 3b was NOT shown            | Skip for respondents who already answered 3b.1 with the same ground — asking again is redundant |
| 5.3 | What would most help you move forward?                             | Text                 | Always                                      | Optional                                                       |

- [x] more generic EA not only HERM — Q5.1 already asks about EAM broadly, not HERM specifically ✅ 2026-08-31
- [x] Section 5 / Section 3b overlap — respondents who complete 3b (EA practice, no HERM) but land in Section 5 anyway (no engagement flag, e.g. 3b.2 = Unlikely/Definitely not) were being re-asked "main barrier to adopting HERM" right after 3b.1 covered the same ground. Q5.2 is now suppressed for anyone who saw Section 3b; 5.1 and 5.3 still apply to everyone ✅ 2026-08-31

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

## Deferred to Follow-up Wave

These came out of the EA-SIG discussion at EUNIS 2026 but go beyond a first short landscape survey — they add case-study depth or roadmap detail rather than serving the core "who uses HERM / which frameworks / why (not)" questions. `Draft-Letter2EUNISBoard.md` already commits to a follow-up wave (deliverable 7: "recommendations for follow-up activities, including possible more detailed surveys, interviews, or workshops") — that is where these belong, not in this instrument.

- Medical faculty present or not
- Breadth of subjects offered (TU/full university vs. university vs. school of arts or music)
- Respondent's professional background
- More detail on institution type
- Planning horizon for EAM/HERM adoption
- Tooling questions (which EA tools are used) — explicitly marked "later" in the source discussion notes

---

## Design Decisions & Open Items

- [x] Decide distribution tool (Google Forms / [LamaPoll](https://www.lamapoll.de/) / LimeSurvey / SurveyMonkey / Typeform / paper) ✅ 2026-08-31
> --> LamaPoll will be used.
- [x] Confirm the 5 artifact names match current HERM documentation exactly ✅ 2026-06-02
- [x] Add SRM to artifact list once released — placeholder added in Q3.1
- [x] Decide whether institution name is truly optional (anonymization vs. case study richness tradeoff), yes, optional as much as possible ✅ 2026-06-02
- [x] Resolve HERM-vs-other-framework overlap: Q2.3 (universal multi-select, includes HERM) now drives Sections 3 / 3a / 3b via independent set-membership conditions instead of mutually exclusive branching, so HERM + another framework can be recorded together ✅ 2026-08-31
- [ ] Add introduction and full ethics/consent statement at the top — naming-consent question added as Section 4 Part A; purpose/GDPR intro text still needed
- [ ] Consider a short version (Sections 1–2–4 only, ~5 min) for conference distribution
- [x] Confirm the chosen survey tool (LamaPoll / LimeSurvey / etc.) can implement: (a) branching on multi-select membership for Sections 3/3a/3b, (b) the Section 4 Part B flag combining answers from three different sections ✅ 2026-08-31

---

## Estimated Completion Time

- Active HERM user (incl. combined with another framework): ~8–10 min
- Explorer: ~6–8 min
- Non-user: ~3–4 min
