# AGENTS.md: Working Rules for AI Agents in the EA and HERM Adoption Survey

This file is the **single place** where project context, rules and agent roles are maintained. `CLAUDE.md` only points here.

**Last updated:** 2026-10-08

---

## 1. Project in one paragraph

The EUNIS Enterprise Architecture Special Interest Group (EA SIG) runs an online survey on the adoption of Enterprise Architecture (EA) and the Higher Education Reference Model (HERM) in higher education. The survey is distributed via national higher education IT networks in Europe and EUNIS channels, implemented in LamaPoll, and analysed by SemaLogic for the community. Results are discussed in the EA SIG first and then published, including a de-identified dataset on Zenodo under CC BY-NC-SA 4.0. Follow-up interviews, workshops and case studies build on the survey.

Status on 2026-10-08: questionnaire implemented, pretest completed in September 2026, field phase not yet started.

---

## 2. Document map and source of truth

| File | Role | Status |
|---|---|---|
| `Adoption_of_EA_in_HE.md` | Proposal to the EUNIS Board: scope, governance, budget, deliverables | Sponsor-facing; must stay consistent with the Blueprint |
| `Blueprint.md` | Questionnaire, routing, data rules, decided open items (OI-1 to OI-14) | **Source of truth for the instrument** |
| `Analysis-Matrix.md` | Research questions, derived variables, checks, reporting language | **Source of truth for the analysis** |
| `LamaPoll_Realisation.pdf`, `LamaPoll_Codebook.pdf` | Implemented survey; LamaPoll numbering (Frage 1–48, V1–V185) | Must match the Blueprint |
| `Introduction-text.md` | Welcome and GDPR text of the survey | Must match Blueprint OI-13 |
| `Distribution.md` | Channel links with LamaPoll attributes | Working document |
| `National_Higher_Education_IT_Networks_Europe.md` | Inventory of national networks with membership counts | Basis for channels and reach estimates |
| `Countries.md` | Country list used in question 1.2 | Must match LamaPoll |
| `Letter to the board.md` | Request for the Board's endorsement message | Sent; do not edit |
| `Survey_Invitation.md` | Invitation to national organisations, master texts for members, internal reminder template | Working document for distribution |
| `README.md`, `.instructions.md` | Earlier case-study framing of the project | Outdated; do not use as reference |
| `qa/` | Synthetic data and routing tests for the Blueprint of 2026-09-01 | Outdated numbering |
| `data/` | Raw LamaPoll exports | Contains personal data; see section 3 |

If documents disagree, the Blueprint wins for the instrument and the Analysis Matrix wins for the analysis. Report every disagreement instead of silently resolving it.

---

## 3. Mandatory rules

### Access and privacy

- **Never read, index or cite** `no_agent_access/` and `.logs/`. They hold outdated drafts, reviews and session logs. If a finding would depend on them, say that they were not checked.
- Raw files in `data/` contain personal data (e-mail, name, institution, free text, technical metadata). Only compute aggregates or inspect column headers; never print individual responses, e-mail addresses or names.
- Before any data leaves the controlled environment, apply Blueprint data rule 12 (remove identifiers and technical metadata) and rule 13 (exclude Preview and Leave responses).
- Pretest durations from September 2026 include the time testers spent writing feedback. Do not use them to estimate completion time.

### Language

- Survey and project documents: English, British spelling.
- Communication with the project team: German.

### Analysis and reporting

- Follow the reporting language of Analysis Matrix section G: "Among participating institutions…", never "X % of European universities…".
- Do not use the term "EA maturity" and do not build maturity scores; report an "EA status and coverage profile" (Blueprint OI-11, Analysis Matrix E4).
- HERM adoption starts with pilot use (Blueprint OI-5). Always state which indicator is used: adoption, operational adoption, or engagement.
- Report barriers (Section 5) separately for non-users and for evaluators / pilot users.
- Country comparisons only for country groups with at least 5 participating institutions; smaller countries form "Other countries" (Analysis Matrix E1).
- Give evidence weight for every finding ("7 of 12 institutions", "mentioned by half"). For qualitative patterns, require at least 3 independent responses.
- Separate "what happened" from "why it happened", and separate respondent-level from institution-level statements.
- Highlight successes and realistic challenges; HE institutions are diverse, avoid one-size-fits-all conclusions.
- Frameworks must emerge from the data, be actionable for practitioners, and be tested against the existing responses and cases before they are finalised.

### Findings format

- **Finding:** clear statement
- **Evidence:** questions, variables and number of cases
- **Strength:** universal / common / emerging
- **Implications:** what it means for practitioners in HE

---

## 4. Agent roles

Agents are invoked by naming the role and the task, e.g. "Act as the Consistency Reviewer and check Blueprint against the LamaPoll codebook." Each role follows section 3.

### 4.1 Consistency Reviewer
Checks that proposal, Blueprint, Analysis Matrix, LamaPoll realisation, introduction text and distribution plan agree.
**Input:** the documents in section 2. **Output:** list of contradictions, redundancies and gaps, each with file and location, ranked by impact on the field phase.

### 4.2 Distribution Coordinator
Maintains channel links and the distribution plan.
**Input:** `Distribution.md`, network inventory, Board decisions. **Output:** checked links with uniform attribute syntax (`Distribution_<NAME>=1`), ISO country codes matching `Countries.md`, field dates, reminders, owners per channel, templates for national networks.

### 4.3 Data Steward
Prepares raw exports for analysis and publication.
**Input:** LamaPoll export, Blueprint data rules. **Output:** cleaned research dataset, separate restricted contact list, documented derived variables (Analysis Matrix B), results of all checks in Analysis Matrix F and F1, disclosure-control notes for publication.

### 4.4 Quantitative Analyst
Answers RQ1–RQ31 with the variables and analyses defined in the Analysis Matrix.
**Input:** cleaned dataset. **Output:** frequencies, cross-tabulations with cell sizes, sensitivity analyses (respondent vs. institution level, knowledge level 1.8), in the reporting language of section G.

### 4.5 Qualitative Coder
Codes open answers (4.5, 4.8, 4.9, 4.11, 5.5, 6.1, 6.2, 9.1).
**Input:** de-identified free text. **Output:** codebook with definitions, assigned codes per response, coder and coding version, memos, theme frequencies and representative quotes without identifying details.

### 4.6 Case and Follow-up Screener
Identifies candidates for case studies, interviews and peer matching.
**Input:** cleaned dataset plus restricted contact list. **Output:** candidate list using `CASE_CANDIDATE` (Blueprint OI-8 criteria) and `PEER_MATCH_PROFILE`; kept outside the research dataset.

### 4.7 Interview Analyst
Analyses follow-up interviews and case material.
**Input:** transcripts or notes. **Output:** motivation, implementation and outcome per case, contingency factors (size, EA status, leadership support), quotes, open questions.

### 4.8 Report Writer
Turns findings into reports for the EA SIG, the EUNIS Board and the community.
**Input:** results of 4.4–4.7. **Output:** text structured around practitioner questions ("Why adopt?", "How to start?", "What is realistic?"), with evidence weight and limitations, connected to HERM where relevant.

---

## 5. Requesting a new role

Describe the analytical task, the input data, the desired output and how it supports the study goals in Blueprint section 1. Add the role to section 4 of this file.
