# HERM Adoption Survey — Blueprint

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

Section 3 ("HERM Usage Details") and Section 4 ("Why not (yet) HERM?") are now genuinely separate, mutually exclusive top-level sections — restructured 2026-09-01, see rationale below.

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
       (moved here from the old "Other Framework Details" group 2026-09-01 —
       see rationale below)

Section 3: HERM Usage Details                                              — 3.1–3.9
  Shown if HERM ∈ 2.3 selection

Section 4: Why not (yet) HERM?                                             — 4.1–4.4
  Shown if HERM ∉ 2.3 selection AND (2.1 = Yes/Exploring OR 2.2 = Yes/Exploring)
  (mutually exclusive with Section 3 by construction — a respondent sees
  exactly one of the two)

Section 5: Sharing & Contact — two independently-gated groups              — 5.1–5.5
  5.1       (naming consent)    → everyone who gave an institution name in 1.1
  5.2–5.5   (follow-up contact) → gated on an engagement flag (3.6 / 4.2
                                   signals), not on which of Section 3/4 fired

Section 6: Open Questions & Barriers                                       — 6.1–6.3
  → everyone who did NOT trigger the 5.2–5.5 engagement flag
    (i.e. limited or no active EA/HERM engagement) — catch-all wrap-up
  → 6.2 specifically is suppressed for anyone who saw Section 4
    (4.1 already covers "reasons for not using HERM"); 6.1/6.3 still apply

→ END
```

A respondent using HERM *and* TOGAF answers 2.3 (both), 2.4/2.5 once (general, covering the whole picture), then goes straight into Section 3 — no more detour through a "other framework" sub-block sitting inside the HERM section.

**Why the restructure (2026-09-01):** 2.4/2.5 ("Other EA Framework Details") used to live inside Section 3, conditional on having a *real* non-HERM framework, and its stem read "the framework(s) selected above" — which only worked because it was the very next question after 2.3, with nothing else selected-from-2.3 in between. Splitting Section 3 into a HERM-only Section 3 and a genuinely separate Section 4 removed the reason for that conditional sub-block to live where it did; moving 2.4/2.5 to immediately follow 2.3 makes "selected above" resolve exactly as intended (covering everything checked in 2.3, HERM included), and removes the old "does 'No formal framework' count as a real other framework" distinction entirely, since 2.4/2.5 are now asked unconditionally whenever 2.3 fires, regardless of which framework(s) were picked.

**Consequence, deliberately accepted, open item:** the old engagement flag included "2.4 (formerly 3.10) was answered" as a proxy for "a real other-framework user, worth recruiting even without HERM interest." Since 2.4/2.5 are now general and (almost) always answered whenever 2.3 fires, that proxy no longer distinguishes anything and has been dropped from the flag (see Section 5 below). This means a long-time TOGAF-only user with no HERM adoption interest no longer automatically reaches the follow-up-contact funnel. Whether 2.4's duration answer itself (e.g. ≥ 4 years) should re-enter the flag as a recruitment signal is an open decision — see Design Decisions.

**Trade-off, deliberately accepted:** Section 2 grows to 5 questions (still light — two of the five are single/multi-select) and Sections 4–6 numbering shifted down by one relative to the earlier revision, requiring a full renumbering pass (done here) and a rewrite of `qa/eval_survey_flow.py`'s routing logic (also done). Payoff: Section 3 and Section 4 now map exactly onto the two core research questions, HERM co-occurrence with another framework no longer produces an in-section detour, and the NOFORMAL-exclusion special case is gone rather than merely fixed.

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

| #   | Question                                                            | Type                 | Options / Notes                                                                                                                                                   |
| --- | ---------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1 | Does your institution practice Enterprise Architecture (EAM)?         | Single select         | Yes, established practice / We are exploring or just starting / No / Not familiar with EAM                                                                       |
| 2.2 | Does your institution use HERM?                                       | Single select         | Yes, actively / We are exploring or piloting / No / Not familiar with HERM                                                                                        |
| 2.3 | Which EA framework(s) does your institution use or pilot?             | Multi-select          | HERM / TOGAF / Zachman Framework / ArchiMate (as modelling language) / Custom / in-house framework / No formal framework, ad hoc EA practice / Other (text). Shown if 2.1 = Yes/Exploring OR 2.2 = Yes/Exploring |
| 2.4 | How long have you been using the framework(s) selected above?         | Single select         | Less than 1 year / 1–3 years / 4–7 years / More than 7 years. Same condition as 2.3. General — covers everything picked in 2.3, HERM included; independent of 3.5 (HERM's own start year) |
| 2.5 | To which business unit / function is your EAM practice coupled most?  | Multi-select + Other  | See options below. Same condition as 2.3/2.4                                                                                                                       |

- [x] add optional text field to specify exactly — covered by "Other" free text on 2.3 ✅ 2026-08-31
- [x] Bug fix (2026-09-01): 2.3 was gated on 2.1 alone, so a respondent reporting HERM use in 2.2 without formal "EAM practice" (2.1 = No/Not familiar) never reached HERM detail questions at all — contradicting Goal 1. Broadened the gate to 2.1 = Yes/Exploring **OR** 2.2 = Yes/Exploring. Found via the scenario walkthrough in `qa/eval_survey_flow.py` (checks `HERM_DISAGREEMENT_2.2_says_yes_but_no_3.1-3.9`) ✅
- [x] Bug fix (2026-09-01, superseded by the 2026-09-01 restructure below): "No formal framework, ad hoc EA practice" used to count as a non-HERM framework and incorrectly trigger the old conditional "Other Framework Details" group and, through it, the engagement flag. That whole conditional distinction is now moot — 2.4/2.5 are asked unconditionally whenever 2.3 fires, regardless of which framework(s) were selected ✅
- [x] Restructure (2026-09-01): moved duration/coupling (old 3.10–3.11) up to 2.4–2.5, immediately after 2.3, and made them general/unconditional on framework type rather than "real other framework only". Resolves the "selected above" anaphora cleanly (see Question Flow rationale) and removes 3.11's old awkward split from 3.7 (both are "how is this embedded organizationally" questions — 2.5 is now the general anchor, 3.7 the HERM-specific refinement of it) ✅

**Options for 2.5 — EAM Coupling:**
- CIO
- dedicated EA Team
- Person on VP-level
- HR
- Finance
- Central IT
- CDO / Digital Office
- Other

*2.2 is kept purely for the HERM-awareness metric across all respondents, including those without EA practice — it is not itself a routing condition, but it co-determines (together with 2.1) whether 2.3–2.5 are shown.*
*Routing into Section 3 vs. Section 4 is derived from 2.3's HERM membership combined with 2.1/2.2 — see flow diagram above.*
*Based on the combination of 2.1 / 2.2 / 2.3 we set the VAR to "HERM" / "EAM & HERM" / "EAM"*
*Residual risk:* 2.2 and 2.3 are still two independently-answered questions, so a respondent can in principle self-report a contradiction (e.g. 2.2 = "No" but still ticks HERM in 2.3, which is shown because 2.1 = Yes). No routing condition can prevent this — it's a data-quality property of self-report surveys, not a branching bug. Re-run the `HERM_DISAGREEMENT_*` checks in `qa/eval_survey_flow.py` against real submissions to catch and review these cases during cleaning.

---

## Section 3: HERM Usage Details
*Shown if HERM is among the frameworks selected in 2.3*

| #    | Question                                                                           | Type                 | Condition                    | Notes                                                                                               |
| ---- | ------------------------------------------------------------------------------------ | -------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------ |
| 3.1  | Which HERM artifacts do you use?                                                    | Multi-select         | Always, randomized order      | ARM / BRM / TRM / DRM / Business Model Canvas / SRM / Process Models / Value Streams / other (text) |
| 3.2 (C) | Primary Business Capability area of HERM adoption (if known)                     | Text                 | Only if 3.1 is not empty      | e.g. BC number or name — helps cross-reference HERM structure                                        |
| 3.3  | What problem(s) are you solving with HERM?                                          | Multi-select + Other | Always, randomized order      | See options below                                                                                     |
| 3.4 (C) | Describe one successful solution scenario of the previous question in more detail. | Text                 | Only if 3.3 is not empty      |                                                                                                        |
| 3.5  | When did your institution start using HERM?                                         | Year (number)        | Always                        | Rough estimate is fine. Independent of 2.4's general duration question                               |
| 3.6  | Current HERM adoption maturity                                                      | Single select        | Always                        | Exploring / Pilot / Actively used / Embedded in governance / n.a.                                    |
| 3.7  | Is HERM embedded in your broader EAM practice?                                      | Single select        | Only if 2.1 = Yes/Exploring   | Yes, central to it / Partly / No, used standalone. Refines 2.5's general coupling answer for HERM specifically |
| 3.8(\*) | What has worked well?                                                             | Text                 | Always                        | Optional but valuable                                                                                |
| 3.9  | What has been difficult or is missing?                                              | Text                 | Always                        | Optional but valuable                                                                                |

(\*) maybe, we leave this out after pretest.

- [x] more generic on EA not HERM — resolved by keeping Section 3 strictly HERM-scoped and giving general-EA content its own place, first in Section 2 (2.4–2.5) and second in Section 4 (why not HERM) ✅ 2026-08-31, updated 2026-09-01

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

| #    | Question                                                       | Type                                                 | Notes                                                                |
| ---- | ------------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------------ |
| 4.1  | What is the main reason you are not using HERM?                    | Multi-select + Other                                     | See options below                                                        |
| 4.2  | Would you consider adopting HERM?                                   | Single select                                            | Yes, interested / Maybe, need more info / Unlikely / Definitely not     |
| 4.3 (C) | Would HERM act as...                                             | Single-select + Other (Only if 4.2 is = Yes/Maybe)       | complement / replacement / other (specify)                              |
| 4.4  | What would HERM need to offer for you to consider adopting it?      | Text                                                     | Optional — high value for roadmap/community content                     |

*Dropped the earlier "Are you aware of HERM?" question here — 2.2 already captures HERM awareness across all respondents, and its "Not familiar" state combined with the 2.3 routing already determines that this section applies.*

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

| #   | Question                                                  | Type          | Notes                                                        |
| --- | ------------------------------------------------------------ | ------------- | ----------------------------------------------------------------- |
| 5.1 | May your institution be named in the published dataset?      | Single select | Yes, may be named / No, anonymize or aggregate only               |

### 5.2–5.5 — Follow-up Contact
*Shown if the "engagement flag" is set — i.e. either of the following holds, regardless of whether Section 3 or Section 4 fired:*
- 3.6 (HERM maturity) ∈ {Pilot, Actively used, Embedded in governance}, or
- 4.2 (adoption interest) ∈ {Yes interested, Maybe}

*(The old third trigger — "a real other-framework in active use" — was dropped in the 2026-09-01 restructure, since duration/coupling moved to Section 2 and are no longer a distinguishing signal there. See Question Flow's "Consequence, deliberately accepted, open item" and Design Decisions for whether it should be reinstated based on 2.4's duration value.)*

| #   | Question                                                                   | Type             | Notes                                                 |
| --- | ---------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------- |
| 5.2 | How transferable do you think your experience is to other HE institutions? | Single select    | High / Medium / Low / Uncertain                       |
| 5.3 | Are you interested in sharing knowledge with the community?                 | Single select    | Yes / Maybe / No                                       |
| 5.4 | Contact email                                                                | Email (optional) | Only shown if 5.3 = Yes or Maybe                       |
| 5.5 | For which purpose would you like to be contacted                            | Multi select     | Only shown if 5.3 = Yes or Maybe, see selection below  |

- [ ]  make a choice, for what reason to contact.

*Note:* Respondents who rate transferability "High, Medium" AND agree to share → flag for follow-up contact / activity. Gating 5.2–5.5 on the engagement flag rather than on the HERM/non-HERM branch ensures EA-practicing institutions without HERM are not silently dropped from the recruitment funnel described in `Draft-Letter2EUNISBoard.md` (deliverables 3–7: follow-up interviews, workshops).

**Options for 5.5 — Reasons for providing contact:**
- Get to know the results of this survey
- Explain your EA tooling
- Provide more details about your use cases and scenarios
- Join a community workgroup on EAM / HERM
- Other

---

## Section 6: Open Questions & Barriers
*Everyone who did NOT trigger the 5.2–5.5 engagement flag — i.e. limited or no active EA/HERM engagement; this is the catch-all wrap-up*

| #   | Question                                                       | Type                 | Condition                              | Notes                                                    |
| --- | ------------------------------------------------------------------ | -------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| 6.1 | What are your biggest open questions about EAM?                    | Text                 | Always                                      | Core data for "what do practitioners need to know"            |
| 6.2 | What is the main barrier to adopting HERM at your institution?     | Multi-select + Other | Only if Section 4 was NOT shown             | Skip for respondents who already answered 4.1 with the same ground — asking again is redundant |
| 6.3 | What would most help you move forward?                             | Text                 | Always                                      | Optional                                                       |

- [x] more generic EA not only HERM — 6.1 already asks about EAM broadly, not HERM specifically ✅ 2026-08-31
- [x] Section 6 / Section 4 overlap — respondents who complete Section 4 (EA practice, no HERM) but land in Section 6 anyway (no engagement flag, e.g. 4.2 = Unlikely/Definitely not) were being re-asked "main barrier to adopting HERM" right after 4.1 covered the same ground. 6.2 is now suppressed for anyone who saw Section 4; 6.1 and 6.3 still apply to everyone ✅ 2026-08-31, renumbered 2026-09-01

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

- [x] Decide distribution tool (Google Forms / [LamaPoll](https://www.lamapoll.de/) / LimeSurvey / SurveyMonkey / Typeform / paper) ✅ 2026-08-31
> --> LamaPoll will be used.
- [x] Confirm the 5 artifact names match current HERM documentation exactly ✅ 2026-06-02
- [x] Add SRM to artifact list once released — placeholder added in 3.1
- [x] Decide whether institution name is truly optional (anonymization vs. case study richness tradeoff), yes, optional as much as possible ✅ 2026-06-02
- [x] Resolve HERM-vs-other-framework overlap: 2.3 (universal multi-select, includes HERM) drives Section 3 vs. Section 4 via HERM set-membership instead of mutually exclusive branching, so HERM + another framework can be recorded together ✅ 2026-08-31
- [x] Numbering cleanup: dropped lettered sub-sections (3a/3b) and lettered parts (Part A/B) in favor of one running number per top-level section ✅ 2026-08-31
- [x] Fixed two routing bugs found by the `qa/eval_survey_flow.py` scenario walkthrough: 2.3's visibility gate broadened to 2.1 = Yes/Exploring OR 2.2 = Yes/Exploring; "No formal framework" excluded from counting as a real other framework ✅ 2026-09-01
- [x] Restructure: moved duration/coupling (old 3.10–3.11) to Section 2 as general questions (2.4–2.5); split Section 3 into a pure-HERM Section 3 and a genuinely separate Section 4 ("Why not (yet) HERM?"); renumbered old Section 4 → 5, old Section 5 → 6 ✅ 2026-09-01
- [ ] **Open:** should 2.4's duration answer (e.g. ≥ 4 years) re-enter the Section 5 engagement flag, so a long-time non-HERM framework user is still recruited for follow-up contact even without HERM adoption interest? Dropped in the 2026-09-01 restructure because 2.4 stopped being a distinguishing signal (see Question Flow) — needs a decision, not a default
- [ ] Add introduction and full ethics/consent statement at the top — naming-consent question added as 5.1; purpose/GDPR intro text still needed
- [ ] Consider a short version (Sections 1–2 + naming consent only, ~5 min) for conference distribution
- [ ] Re-confirm the chosen survey tool (LamaPoll) can implement: (a) 2.3 gating 2.4–2.5, (b) Section 3 vs. Section 4 as mutually exclusive on HERM membership, (c) the 5.2–5.5 flag combining 3.6 and 4.2 across two different sections — superseded by the 2026-09-01 restructure, previous confirmation (2026-08-31) no longer applies as-is

---

## Estimated Completion Time

- Active HERM user (incl. combined with another framework): ~8–10 min
- Explorer: ~6–8 min
- Non-user: ~3–4 min
