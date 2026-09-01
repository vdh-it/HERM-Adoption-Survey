# EA and HERM Adoption Survey of Higher Education in Europe — Blueprint

**Status:** Draft  
**Audience:** EA practitioners at HE institutions  
**Distribution:** EUNIS to national organizations asking to distribute via member channels
**Last updated:** 2026-09-01

---

## Goals

1. Map who is using HERM and which artifacts, and for what problems
2. Identify transfer-worthy case studies for community sharing
3. Capture open questions practitioners have about HERM (future content direction)

---

## Question Flow (Branching Logic)

Two core research questions must be answerable **independently, including in combination** — an institution can use HERM *and* another framework at the same time (e.g. HERM as content model, ArchiMate as notation):

1. How is HERM used? → Section 3
2. Which other/alternative EA framework(s) are used? → 2.3 (which) + 2.4–2.5 (duration/coupling, general — see below)

Section 3 ("HERM Usage Details") and Section 4 ("Why not (yet) HERM?") are separate, mutually exclusive top-level sections.

```
Section 1: Profile (everyone)                                              — 1.1–1.6

Section 2: Screener (everyone)                                             — 2.1–2.5
  2.1  Practice EAM?                     (Yes / Exploring / No / Not familiar)
  2.2  Use HERM?                         (Yes / Exploring / No / Not familiar)
       — kept as a universal question purely for the HERM-awareness headline
         metric across ALL respondents; it does NOT drive routing.
  2.3  Which EA framework(s) are in use?  Multi-select, includes HERM as an
       option; shown if 2.1 = Yes/Exploring OR 2.2 = Yes/Exploring.
  2.4  How long have you been using the framework(s) selected above?
       General duration, covering everything selected in 2.3 (HERM included)
       — independent of 3.5, which still asks HERM's own specific start year.
       Shown under the same condition as 2.3.
  2.5  To which business unit/function is your EAM practice coupled most?
       General organizational-coupling question, same condition as 2.3/2.4.
       
Section 3: HERM Usage Details                                              — 3.1–3.9
  Shown if HERM ∈ 2.3 selection
  Jump to section 5 afterwards.

Section 4: Why not (yet) HERM?                                             — 4.1–4.4
  Shown if HERM ∉ 2.3 selection AND (2.1 = Yes/Exploring OR 2.2 = Yes/Exploring)
  (mutually exclusive with Section 3 by construction — a respondent sees
  exactly one of the two)

Section 5: Sharing & Contact — two independently-gated groups              — 5.1–5.5
  5.1       (naming consent)    → everyone who gave an institution name in 1.1
  5.2–5.5   (follow-up contact) → gated on an engagement flag: 3.6 maturity,
                                   OR 4.2 adoption interest, OR (Section 4 AND
                                   2.4 duration ∈ {4-7y, >7y}) — long-time EA
                                   adopters without current HERM intent still
                                   count

Section 6: Open Questions & Barriers                                       — 6.1–6.3
  → everyone who did NOT trigger the 5.2–5.5 engagement flag
    (i.e. limited or no active EA/HERM engagement) — catch-all wrap-up
  → 6.2 specifically is suppressed for anyone who saw Section 4
    (4.1 already covers "reasons for not using HERM"); 6.1/6.3 still apply

→ END
```

A respondent using HERM *and* TOGAF answers 2.3 (both), 2.4/2.5 once (general, covering the whole picture), then goes straight into Section 3 — no more detour through a "other framework" sub-block sitting inside the HERM section.

---

## Section 1: Profile
*Everyone answers — keep short*

| #   | Question                            | Type            | Notes                                                                    |
| --- | ------------------------------------ | --------------- | -------------------------------------------------------------------------- |
| 1.1 | Institution name                    | Text (optional) | Add: "Or describe anonymously (e.g. 'mid-size German university')"       |
| 1.2 | Country                             | Dropdown / Text | ISO country list or free text                                            |
| 1.3 | Institution type                    | Single select   | University / University of Applied Sciences / Research Institute / Other |
| 1.4 | Institution size (approx. students) | Single select   | <2k / 2–10k / 10–30k / >30k / n.a.                                       |
| 1.5 | Staff size (approx. headcount)      | Single select   | <200 / 200–1k / 1–3k / >3k / n.a.                                        |
| 1.6 | Your role                           | Multi select    | EA Architect / IT Strategist / CIO/IT Director / IT Project Lead / Other |
- [ ] check for good boundaries in student size and staff headcount

---

## Section 2: Screener — EAM & HERM Practice
*2.1 and 2.2 are always required; 2.3–2.5 are required if 2.1 = Yes/Exploring OR 2.2 = Yes/Exploring*

| #   | Question                                                             | Type                 | Options / Notes                                                                                                                                                                                                                |
| --- | -------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2.1 | Does your institution practice Enterprise Architecture (EAM)?        | Single select        | Yes, established practice / We are exploring or just starting / No / Not familiar with EAM                                                                                                                                     |
| 2.2 | Does your institution use HERM?                                      | Single select        | Yes, actively / We are exploring or piloting / No / Not familiar with HERM                                                                                                                                                     |
| 2.3 | Which EA framework(s) does your institution use or pilot?            | Multi-select         | HERM / TOGAF / Zachman Framework / HORA,  HOSA / ArchiMate (as modelling language) / Custom / in-house framework / No formal framework, ad hoc EA practice / Other (text). Shown if 2.1 = Yes/Exploring OR 2.2 = Yes/Exploring |
| 2.4 | How long have you been using the framework(s) selected above?        | Single select        | Less than 1 year / 1–3 years / 4–7 years / More than 7 years. Same condition as 2.3. General — covers everything picked in 2.3, HERM included; independent of 3.5 (HERM's own start year)                                      |
| 2.5 | To which business unit / function is your EAM practice coupled most? | Multi-select + Other | See options below. Same condition as 2.3/2.4                                                                                                                                                                                   |

**Options for 2.5 — EAM Coupling:**
- CIO
- dedicated EA Team
- Person on VP-level
- HR
- Finance
- Central IT
- CDO / Digital Office
- Other

*2.2 does not itself route to Section 3 vs. Section 4 (that's driven by 2.3's HERM membership); together with 2.1 it gates whether 2.3–2.5 are shown.*
*Based on the combination of 2.1 / 2.2 / 2.3 we set the VAR to "HERM" / "EAM & HERM" / "EAM"*
*Residual risk:* 2.2 and 2.3 are still two independently-answered questions, so a respondent can in principle self-report a contradiction (e.g. 2.2 = "No" but still ticks HERM in 2.3, which is shown because 2.1 = Yes). No routing condition can prevent this — it's a data-quality property of self-report surveys, not a branching bug. Re-run the `HERM_DISAGREEMENT_*` checks in `qa/eval_survey_flow.py` against real submissions to catch and review these cases during cleaning.

---

## Section 3: HERM Usage Details
*Shown if HERM is among the frameworks selected in 2.3*

| #       | Question                                                                           | Type                 | Condition                   | Notes                                                                                                          |
| ------- | ---------------------------------------------------------------------------------- | -------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 3.1     | Which HERM artifacts do you use?                                                   | Multi-select         | Always, randomized order    | ARM / BRM / TRM / DRM / Business Model Canvas / SRM / Process Models / Value Streams / other (text)            |
| 3.2 (C) | Primary Business Capability area of HERM adoption (if known)                       | Text                 | Only if 3.1 is not empty    | e.g. BC number or name — helps cross-reference HERM structure                                                  |
| 3.3     | What problem(s) are you solving with HERM?                                         | Multi-select + Other | Always, randomized order    | See options below                                                                                              |
| 3.4 (C) | Describe one successful solution scenario of the previous question in more detail. | Text                 | Only if 3.3 is not empty    |                                                                                                                |
| 3.5     | When did your institution start using HERM?                                        | Year (number)        | Always                      | Rough estimate is fine. Independent of 2.4's general duration question                                         |
| 3.6     | Current HERM adoption maturity                                                     | Single select        | Always                      | Exploring / Pilot / Actively used / Embedded in governance / n.a.                                              |
| 3.7     | Is HERM embedded in your broader EAM practice?                                     | Single select        | Only if 2.1 = Yes/Exploring | Yes, central to it / Partly / No, used standalone. Refines 2.5's general coupling answer for HERM specifically |
| 3.8(\*) | What has worked well?                                                              | Text                 | Always                      | Optional but valuable                                                                                          |
| 3.9     | What has been difficult or is missing?                                             | Text                 | Always                      | Optional but valuable                                                                                          |

(\*) maybe, we leave this out after pretest.

**Options for 3.3 — Problems solved with HERM:**
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

## Section 4: Why not (yet) HERM?
*Shown if HERM was NOT selected in 2.3, AND (2.1 = Yes/Exploring OR 2.2 = Yes/Exploring). Mutually exclusive with Section 3 — a respondent sees exactly one of the two.*

| #       | Question                                                       | Type                                               | Notes                                                               |
| ------- | -------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| 4.1     | What is the main reason you are not using HERM?                | Multi-select + Other                               | See options below                                                   |
| 4.2     | Would you consider adopting HERM?                              | Single select                                      | Yes, interested / Maybe, need more info / Unlikely / Definitely not |
| 4.3 (C) | Would HERM act as...                                           | Single-select + Other (Only if 4.2 is = Yes/Maybe) | complement / replacement / other (specify)                          |
| 4.4     | What would HERM need to offer for you to consider adopting it? | Text                                               | Optional — high value for roadmap/community content                 |

**Options for 4.1 — Reasons for not using HERM:**
- Not aware of it until now
- Our current framework already meets our needs
- HERM is too complex / specific / doesn't fit our context
- Lack of tooling support for HERM
- No community or peer examples to learn from
- Switching cost too high
- Other

---

## Section 5: Knowledge Sharing & Contact

### 5.1 — Naming Consent
*Shown to everyone who provided an institution name in 1.1 — ungated, required for GDPR-compliant publication regardless of which of Section 3/4 fired (see `Draft-Letter2EUNISBoard.md`, which commits to asking this)*

| #   | Question                                                | Type          | Notes                                               |
| --- | ------------------------------------------------------- | ------------- | --------------------------------------------------- |
| 5.1 | May your institution be named in the published dataset? | Single select | Yes, may be named / No, anonymize or aggregate only |

### 5.2–5.5 — Follow-up Contact
*Shown if the "engagement flag" is set — i.e. any of the following holds:*
- 3.6 (HERM maturity) ∈ {Pilot, Actively used, Embedded in governance}, or
- 4.2 (adoption interest) ∈ {Yes interested, Maybe}, or
- Section 4 fired AND 2.4 (duration) ∈ {4–7 years, More than 7 years} — a long-time EA adopter still counts as worth recruiting even without current HERM intent

| #   | Question                                                                   | Type             | Notes                                                 |
| --- | -------------------------------------------------------------------------- | ---------------- | ----------------------------------------------------- |
| 5.2 | How transferable do you think your experience is to other HE institutions? | Single select    | High / Medium / Low / Uncertain                       |
| 5.3 | Are you interested in sharing knowledge with the community?                | Single select    | Yes / Maybe / No                                      |
| 5.4 | Contact email                                                              | Email (optional) | Only shown if 5.3 = Yes or Maybe                      |
| 5.5 | For which purpose would you like to be contacted                           | Multi select     | Only shown if 5.3 = Yes or Maybe, see selection below |

- [ ]  make a choice, for what reason to contact.

*Note:* Respondents who rate transferability "High, Medium" AND agree to share → flag for follow-up contact / activity.

**Options for 5.5 — Reasons for providing contact:**
- Get to know the results of this survey
- Explain your EA tooling
- Provide more details about your use cases and scenarios
- Join a community workgroup on EAM / HERM
- Other

---

## Section 6: Open Questions & Barriers
*Everyone who did NOT trigger the 5.2–5.5 engagement flag — i.e. limited or no active EA/HERM engagement; this is the catch-all wrap-up*

| #   | Question                                                       | Type                 | Condition                       | Notes                                                                                          |
| --- | -------------------------------------------------------------- | -------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------- |
| 6.1 | What are your biggest open questions about EAM?                | Text                 | Always                          | Core data for "what do practitioners need to know"                                             |
| 6.2 | What is the main barrier to adopting HERM at your institution? | Multi-select + Other | Only if Section 4 was NOT shown | Skip for respondents who already answered 4.1 with the same ground — asking again is redundant |
| 6.3 | What would most help you move forward?                         | Text                 | Always                          | Optional                                                                                       |

**Options for 6.2 — Barriers:**
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

- [x] Distribution tool: LamaPoll
- [x] Long-time non-HERM framework users included in the Section 5 engagement flag (2.4 duration ∈ {4–7y, >7y} AND Section 4 fired)
- [ ] Add introduction and full ethics/consent statement at the top — naming-consent question added as 5.1; purpose/GDPR intro text still needed
- [ ] Consider a short version (Sections 1–2 + naming consent only, ~5 min) for conference distribution
- [ ] Confirm LamaPoll can implement: (a) 2.3 gating 2.4–2.5, (b) Section 3 vs. Section 4 as mutually exclusive on HERM membership, (c) the 5.2–5.5 engagement flag combining 3.6, 4.2, and 2.4 across three points in the flow

---

## Estimated Completion Time

- Active HERM user (incl. combined with another framework): ~8–10 min
- Explorer: ~6–8 min
- Non-user: ~3–4 min
