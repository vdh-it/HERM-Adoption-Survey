# EA and HERM Adoption Survey of Higher Education in Europe — Blueprint

**Status:** Revised Draft  
**Audience:** EA practitioners and related decision-makers at higher education institutions  
**Distribution:** EUNIS and national organisations via member channels  
**Last updated:** 2026-10-08

---

## 1. Study Goals

1. Describe the use of Enterprise Architecture (EA) and HERM among participating higher education institutions.
2. Identify which EA frameworks, reference models, modelling languages, and in-house approaches are used.
3. Understand how HERM is used, including artefacts, application areas, adoption stage, and organisational embedding.
4. Identify barriers and enabling conditions for HERM adoption.
5. Identify concrete HERM use cases that may be suitable for community sharing or follow-up case studies.
6. Capture open questions and support needs related to EA and HERM.

---

## 2. Unit of Analysis and Response Perspective

The primary unit of analysis is the **institution**.

Respondents answer on behalf of their institution to the best of their knowledge. Where institutional knowledge cannot reasonably be assumed, a **Don't know / Cannot assess** option is provided.

Respondent-level variables such as role, organisational unit, and familiarity with HERM are treated separately from institution-level variables.

If multiple responses are received from the same institution, they must be identifiable where possible and handled during data cleaning and analysis.

---

## 3. Question Flow

```text
Section 0: Introduction, GDPR, How to proceed?    everyone

If 0.1 = Leave
    -> Section 9

Section 1: Respondent & Institution Profile        everyone
Section 2: EA Practice                             everyone, partly conditional

If EA status (2.1) = Established / Early operational
    -> 2.2–2.6: EA coverage, age, approaches, home, lead
If EA status (2.1) = Exploring or planning
    -> 2.2, 2.4–2.6: EA coverage, approaches, home, lead
Else
    -> Section 3

Section 3: HERM Awareness & Adoption               everyone

If HERM status (3.2) = Evaluating / Pilot / Active / Embedded
    -> Section 4: HERM Usage Details
Else
    -> Section 5: HERM Non-Adoption & Barriers

After Section 4:
If HERM status (3.2) = Active / Embedded
    -> Section 6
If HERM status (3.2) = Evaluating / Pilot
    -> Section 5, reduced: 5.1 (without "discontinued") and 5.2 only

Section 6: Open Questions & Support Needs          everyone
Section 7: Knowledge Sharing & Follow-up           everyone, partly conditional
Section 8: Naming & Contact Consent                conditional
Section 9: Closing & Feedback                      everyone
```

---

# Section 0: Introduction, GDPR, How to proceed?

Introduction text see [[Introduction-text]]

## 0.1 How would you like to proceed?

**Type:** Single select, mandatory

> Please select one option:

- Leave the survey without participating. You may optionally tell us why on the final page.
- Preview the questionnaire only. My responses will not be included in the study.
- Participate in the survey. I have read the information above and voluntarily consent to the processing of my survey responses for the purposes described.

**Routing:**

- Preview -> Section 1 (responses are excluded from the study; see data rule 13)
- Participate -> Section 1
- Leave -> Section 9

---

# Section 1: Respondent & Institution Profile

## 1.1 Institution name

**Type:** Text, optional

> Institution name

Optional. If you prefer not to identify your institution, leave this field blank.

---

## 1.2 Country

**Type:** Single select as dropdown

> Which country is your institution based in?

- European country list
- Other (please specify below)

If **Other**: follow-up text question "Specific Country" — "Please state the country in which your institution is based."

---

## 1.3 Institution type

**Type:** Single select, randomised

- University
- University of Applied Sciences / Polytechnic
- Specialised higher education institution
- Arts or Music institution
- Research institution
- Don't know / Cannot assess
- Other + Text

---

## 1.4 Approximate number of students

**Type:** Single select

> Report head count.

- Fewer than 1,000
- 1,000–4,999
- 5,000–9,999
- 10,000–19,999
- 20,000–39,999
- 40,000–79,999
- 80,000 or more
- Not applicable
- Don't know

---

## 1.5 Approximate staff headcount

**Type:** Single select

- Fewer than 250
- 250–999
- 1,000–2,499
- 2,500–4,999
- 5,000–9,999
- 10,000 or more
- Don't know

---

## 1.6 Your role

**Type:** Multi-select

- Enterprise / Business / Solution / IT Architect
- IT Strategy / Digital Strategy
- CIO / IT Director / Head of IT
- CDO / Digital Office
- IT or Digital Project / Programme Management
- Academic / Researcher with EA context
- Educator / Lecturer with EA context
- Other + Text

---

## 1.7 Your organisational unit

**Type:** Multi-select

> In which part of your institution do you mainly work?

- Central IT
- Central administration or services outside IT (incl. executive or strategy office)
- Decentralised IT in a faculty, department or institute
- Faculty, department or institute (outside IT)
- External to the institution (e.g. consultant)
- Other + Text

**Implementation note:** Respondent-level variable. The first four options mirror the rows of 2.2 so that the respondent's vantage point can be compared with the reported EA coverage (see OI-2).

---

## 1.8 Your knowledge of your institution's EA practice

**Type:** Single select

- I am directly responsible for or actively involved in it
- I work closely with the EA practice
- I have general knowledge of it
- I have limited knowledge of it

---

# Section 2: Enterprise Architecture Practice

## 2.1 Current status of Enterprise Architecture at your institution

**Type:** Single select

> To the best of your knowledge, what is the current status of Enterprise Architecture at your institution?
>
> _If the status differs between parts of your institution (e.g. central units vs. faculties), please answer for the most advanced part._

- Established operational practice
- Early operational practice / currently being established
- Exploring or planning EA
- No EA practice
- Don't know / Cannot assess

**Routing:**

- Established operational practice -> 2.2
- Early operational practice / currently being established -> 2.2
- Exploring or planning EA -> 2.2 (2.3 is skipped)
- All other responses -> Section 3

---

## 2.2 Coverage of EA across organisational areas

**Type:** Matrix, one answer per row, fixed order, optional

> In higher education, EA often covers some parts of the institution more than others.
> For each of the following areas, what is the current status of EA?

| Area                                                                                         | Established | Early operational | Exploring or planning | No EA | Don't know / n.a. |
| -------------------------------------------------------------------------------------------- | ----------- | ----------------- | --------------------- | ----- | ----------------- |
| Central IT (e.g. IT services, infrastructure, IT governance)                                  | ○           | ○                 | ○                     | ○     | ○                 |
| Central administration and services outside IT (e.g. student administration, finance, HR)     | ○           | ○                 | ○                     | ○     | ○                 |
| Decentralised IT in faculties, departments or institutes                                      | ○           | ○                 | ○                     | ○     | ○                 |
| Faculties, departments, institutes (organisation of teaching and research, local processes)   | ○           | ○                 | ○                     | ○     | ○                 |
| Other (please name)                                                                           | ○           | ○                 | ○                     | ○     | ○                 |

**Implementation note:** Store each row as a separate ordinal variable, using the LamaPoll coding by column position: 1 = Established, 2 = Early operational, 3 = Exploring or planning, 4 = No EA, 5 = Don't know / n.a. (treated as missing in analysis). Lower codes therefore mean a more advanced EA status; the codes 1–5 are identical to those of 2.1. Because of the "most advanced part" instruction in 2.1, the lowest substantive row code (1–4) is expected to match the code of 2.1 (consistency check). The "Other" row has a free-text field for the area name; it is coded separately and not part of the four-area coverage typology.

---

## 2.3 Organisational age of the EA practice

**Condition:** Show if 2.1 = Established / Early operational practice

**Type:** Single select

> Approximately how long has your institution had an operational EA practice?

- Less than 1 year
- 1–3 years
- 4–7 years
- More than 7 years
- Don't know

---

## 2.4 EA approaches currently used

**Type:** Multi-select, randomised

> Which of the following frameworks/methods/etc. does your institution currently use, pilot, or actively evaluate for Enterprise Architecture?
> For the following questions, you can select more than one option.

### EA frameworks / methods

- TOGAF
- Zachman Framework
- Don't know / Cannot assess
- Other EA framework or method

### Higher-education reference models / architectures

- HERM
- HORA / HOSA
- Don't know / Cannot assess
- Other higher-education reference model

### Modelling languages / standards

- ArchiMate
- BPMN
- Don't know / Cannot assess
- Other modelling language or notation

### Institution-specific approach

- Custom / in-house EA framework
- Just EA standards without customisation
- No formal framework; pragmatic or ad hoc EA practice
- Other
- Don't know / Cannot assess

**Implementation note:** Store each option as a separate binary variable and retain the category grouping above.

---

## 2.5 Organisational home of the EA practice

**Type:** Multi-select, randomised

> Where is the EA practice organisationally located or formally anchored?

- Dedicated Enterprise Architecture team
- Central IT
- CIO office / IT leadership
- CDO / Digital Office
- Central administration outside IT
- Academic / teaching organisation
- Research organisation
- Cross-institutional / distributed model
- Undefined
- Don't know / Cannot assess
- Other + Text

---

## 2.6 Executive or organisational lead for EA

**Type:** Single select, randomised

> Who has primary organisational responsibility for Enterprise Architecture?

- CIO
- IT Director / Head of IT
- CDO / Head of Digital Transformation
- Dedicated Head of Enterprise Architecture / Chief Architect
- Vice-President / Vice-Rector / Executive Board member
- Central administration leader outside IT
- Distributed / shared responsibility without one formal lead
- Undefined
- Don't know / Cannot assess
- Other + Text

---

# Section 3: HERM Awareness & Adoption

## 3.1 Respondent awareness of HERM

**Type:** Single select

> Before starting this survey, how familiar were you personally with HERM?

- I know HERM well
- I know the basic concept
- I had heard of HERM but knew little about it
- I was not familiar with HERM before this survey

---

## 3.2 Institutional HERM adoption status

**Type:** Single select

> To the best of your knowledge, what is the highest current level of HERM adoption at your institution?

- Not considered
- Being evaluated / considered
- Pilot or experimental use
- Active operational use
- Embedded in governance or standard EA processes
- Previously used, but no longer in use
- Don't know / Cannot assess

**Routing:**

- Being evaluated / considered -> Section 4
- Pilot or experimental use -> Section 4
- Active operational use -> Section 4
- Embedded in governance or standard EA processes -> Section 4
- All other responses -> Section 5

**Routing after Section 4:**

- Active operational use / Embedded in governance or standard EA processes -> Section 6
- Being evaluated / considered / Pilot or experimental use -> Section 5 (5.1 and 5.2 only; 5.3–5.5 hidden)

---

# Section 4: HERM Usage Details

## 4.1 Duration of HERM engagement

**Condition:** Show if 3.2 is selected as other than "not considered" or "Don't know" or if 3.1 is selected as "basic concept" or "well known".

**Type:** Single select

> Approximately how long has your institution been actively evaluating or using HERM?

- Less than 1 year
- 1–3 years
- 4–7 years
- More than 7 years
- Don't know

**Implementation note:** Same categories as 2.3, so that the duration of HERM engagement and the age of the EA practice can be compared directly.

---

## 4.2 HERM application area

**Type:** Multi-select, randomised

> In which areas of your organisation are HERM artefacts used?

- Institution-wide / cross-domain
- Teaching and learning (as topic)
- Research (as topic)
- Student lifecycle / student administration
- Finance and controlling
- Human resources
- IT management
- Facilities / infrastructure
- Governance / strategy
- Don't know / Cannot assess
- Other + Text

---

## 4.3 HERM artefacts used or evaluated

**Type:** Matrix, one answer per row, random order

> Which HERM artefacts does your institution currently use, pilot, or actively evaluate?

| Artefact                          | Operational | Pilot | Evaluating | Not used | Don't know / n.a. |
| --------------------------------- | ----------- | ----- | ---------- | -------- | ----------------- |
| Business Reference Model (BRM)    | ○           | ○     | ○          | ○        | ○                 |
| Data Reference Model (DRM)        | ○           | ○     | ○          | ○        | ○                 |
| Application Reference Model (ARM) | ○           | ○     | ○          | ○        | ○                 |
| Technology Reference Model (TRM)  | ○           | ○     | ○          | ○        | ○                 |
| Service Reference Model (SRM)     | ○           | ○     | ○          | ○        | ○                 |

**Implementation note:** Rows in random order, columns in fixed order (same direction as 2.2). Store each row as a separate ordinal variable, using the LamaPoll coding by column position: 1 = Operational, 2 = Pilot, 3 = Evaluating, 4 = Not used, 5 = Don't know / n.a. (treated as missing in analysis).

---

## 4.4 Additional artefacts used

**Type:** Multi-select, randomised

> Which EAM and HERM-related/supporting artefacts and approaches are in use?

- Business Model Canvas
- Recipe Cards
- Process Models
- Value Streams
- Don't know / Cannot assess
- Other

---

## 4.5 Primary HERM application area

**Condition:** Show if 4.2 ≠ "Don't know / Cannot assess"

**Type:** Text, optional

> Which is currently the primary area? Provide HERM Business Capability name or other HERM identifier, if known.

---

## 4.6 Problems and tasks addressed with HERM

**Type:** Multi-select, randomised

> For which tasks is HERM currently used or evaluated at your institution?

- Structuring or documenting the application landscape
- Structuring or communicating business capabilities
- Technology standardisation or technology lifecycle management
- Data governance or data architecture
- Service design or service architecture
- Strategic or transformation planning
- Impact analysis and future-state planning for major change initiatives
- Risk, security, or compliance analysis
- Process or responsibility modelling
- Communication between IT and non-IT stakeholders
- Benchmarking or comparison with peer institutions
- Consolidation, merger, or shared-service planning
- Investment or project portfolio planning and prioritisation
- Don't know / Cannot assess
- Other

---

## 4.7 Value received from using HERM

**Type:** Multi-select, randomised

> What specific value can you now offer your organisation?

- No tangible outcome yet
- Shared terminology
- Improved landscape transparency
- Better decision support
- Accelerated project or analysis
- Improved stakeholder communication
- Reusable architecture artefact
- Cost or effort reduction
- Don't know / Cannot assess
- Other

---

## 4.8 Concrete HERM use case

**Type:** Text, optional

> **Please describe one specific HERM use case at your institution that you know particularly well. Please focus on what was actually done rather than on HERM in general.**  
>  
> You may use the following points as guidance:
> 
> - **Use case:** What was the problem, task, or decision?
> - **Actors:** Who was involved?
> - **HERM use:** Which HERM artefact(s) were used, and how were they applied?
> - **Outcome:** What was produced, decided, or changed?
> - **Benefit:** Who benefited from the result, and in what way?
> 
> _A concise description is sufficient; you do not need to address every point._

Prompt: "Your HERM use-case-description..."

---

## 4.9 What has worked well?

**Type:** Text, optional

> What aspects of using HERM have worked particularly well at your institution?

Prompt: "Please provide details how you applied HERM and why this was a success..."

---

## 4.10 Enabling factors

**Type:** Multi-select, randomised

> What factors enabled the implementation of HERM at your institution?

- Strong EA capability
- Executive sponsorship
- Active practitioner community
- Good documentation
- Concrete institutional use case
- Tool support
- Availability of reusable examples
- Alignment with existing EA models
- National / community support
- Individual champion or internal advocate
- Don't know / Cannot assess
- Other

---

## 4.11 What has been difficult or missing?

**Type:** Text, optional

> What aspects of using HERM have been difficult, insufficient, or missing?

Prompt: "Provide details on road blocks concerning HERM..."

---

## 4.12 Integration of HERM into broader EA practice

**Condition:** Show if 2.1 = Established / Early operational / Exploring

**Type:** Single select

> What role does HERM play in your institution's broader EA practice?

- Central foundation of the EA approach
- Integrated component of the EA approach
- Selectively connected for specific use cases
- Used independently of the broader EA practice
- No relationship established yet
- Don't know / Cannot assess

---

## 4.13 Adapted, extended or mapped HERM

**Type:** Multi-select, randomised

> Have you adapted, extended or mapped HERM in a way that might be useful to other institutions?

- Translation
- Capability extensions
- HORA mapping
- Application mapping
- Service catalogue
- Data mapping
- Tool implementation
- Governance model
- Visualisation
- Don't know / Cannot assess
- Other

---

# Section 5: HERM Non-Adoption & Barriers

## 5.1 Reasons HERM is not currently in operational use

**Type:** Multi-select, randomised

> Which factors currently contribute to HERM not being used operationally at your institution?

- HERM is not sufficiently known at our institution
- No current need for an additional reference model
- Existing EA approaches already meet our needs
- HERM appears too complex for our current needs
- HERM appears too specific for our context
- HERM does not appear to fit our institutional context
- Insufficient tooling support
- Insufficient documentation or guidance
- Lack of implementation examples / peer cases
- Insufficient internal EA capacity
- Lack of leadership or organisational support
- Switching or adoption effort is too high
- Benefits are unclear compared with the required effort
- EA/HERM knowledge depends on too few individuals
- HERM was previously used but discontinued
- Don't know / Cannot assess
- Other

**Implementation note:** Shown to all respondents in Section 5, including HERM evaluators and pilot users (3.2 = Being evaluated / considered, Pilot or experimental use) after Section 4. For these two groups, hide the option "HERM was previously used but discontinued". Report results separately by 3.2 status.

---

## 5.2 Primary barrier

**Condition:** Show if at least one substantive option selected in 5.1

**Type:** Single select, piped from selected responses in 5.1, randomised; added options anchored at the end

> Of the factors you selected, which is currently the most important barrier?

Added options:
- Other (meaning the item you provided above)
- None of the above
- Don't know / Cannot assess

**Implementation note:** No change needed for evaluators and pilot users; because the options are piped from 5.1, "discontinued" is absent when it was hidden there.

---

## 5.3 Future consideration of HERM

**Condition:** Hide if 3.2 = Being evaluated / considered or Pilot or experimental use

**Type:** Single select

> Is there currently an intention or plan to evaluate or pilot HERM within the next two years?

- Yes
- Under discussion
- No
- Don't know / Cannot assess

---

## 5.4 Potential role of HERM

**Condition:** Show if 5.3 = Yes / under discussion (therefore hidden for evaluators and pilot users, who do not see 5.3)

**Type:** Single select

> If your institution adopted HERM, what role would it most likely play?

- Foundation for the overall EA approach
- Complement to an existing EA framework or method
- Reference model for selected domains or use cases
- Primarily a benchmarking / comparison reference
- Don't know / Cannot assess
- Other

---

## 5.5 Requirements for future adoption

**Condition:** Hide if 3.2 = Being evaluated / considered or Pilot or experimental use (they already answered 4.11)

**Type:** Text, optional

> What would HERM need to offer, or what would need to change at your institution, for adoption to become more attractive?

---

# Section 6: Open Questions & Support Needs

## 6.1 Open questions about Enterprise Architecture

**Type:** Text, optional

> What are the most important unresolved questions about Enterprise Architecture at your institution?

---

## 6.2 Open questions about HERM

**Type:** Text, optional

> What questions about HERM would you most like the HERM community to address?

---

## 6.3 Support needs

**Type:** Multi-select, randomised

> What support from the EA and HERM community would help your institution advance EA?

- None currently
- Introductory guidance
- Implementation guide / playbook
- Concrete use cases and examples
- Reference architectures / reusable patterns
- Tooling support
- Training or workshops
- Peer exchange with other institutions
- Benchmarking data
- Governance and organisational guidance
- Mapping to other EA frameworks or standards
- Don't know / Cannot assess
- Other

---

## 6.4 Most important support need

**Condition:** Show if at least one substantive option selected in 6.3

**Type:** Single select, piped from 6.3, randomised; added options anchored at the end

> Which of these would be most valuable to your institution?

Added options:
- Other (meaning the item you provided above)
- None of the above
- Don't know / Cannot assess

---

# Section 7: Knowledge Sharing & Follow-up

## 7.1 Potential value of the institution's experience

**Type:** Single select

> Do you believe your institution has an EA or HERM experience that could be useful for other higher education institutions?

- Yes
- Possibly
- Unlikely
- No
- Don't know / Cannot assess

---

## 7.2 Interest in community exchange

**Type:** Multi-select, randomised

> Would you or your institution be interested in any of the following?

- Receiving the results of this survey
- Sharing a use case or practical experience
- Presenting and discussing your EA / HERM work
- Joining a community workgroup on EA / HERM
- Participating in a follow-up interview
- Participating in a more detailed follow-up survey
- Being connected with peer institutions that have a similar EA setup (peer matching)
- None of these

---

# Section 8: Naming & Contact Consent

## 8.1 Contact e-mail

**Condition:** Show if at least one follow-up option other than "None" was selected in 7.2

**Type:** Email, optional

> By providing your contact details, you consent to the purpose(s) provided in the previous question.
> Please note that your response will not be included in the publication of the dataset. It will only be processed internally by SemaLogic and the EUNIS EA SIG. If you selected peer matching, your contact details will be shared only with peer institutions that have also selected peer matching.

Prompt: "Your e-mail address"

**Implementation note:** Peer matching only connects respondents who both selected peer matching in 7.2 and provided an e-mail address here.

---

## 8.2 Permission to name institution

**Condition:** Show if institution name provided in 1.1

**Type:** Single select, randomised

> You had provided the name of your institution at the beginning of this survey. This may in connection with your role lead reveal your identity.
> May your institution be named in publications or datasets resulting from this survey?

- Yes, the institution may be named, and I understand that this may identify me
- No, do not name the institution; publish my responses only in de-identified or aggregated form

---

# Section 9: Closing & Feedback

> Thank you for your time.
> We will evaluate, discuss and publish the results as soon as possible.

## 9.1 Feedback

**Type:** Text, optional

> Do you have any final comments about the survey itself? If you chose not to participate, we would appreciate a short note on why.

Closing text: "Thank you again for your personal support of the global HERM community!"

---

# Data Quality and Implementation Rules

1. Do not force institution-level answers where respondents may reasonably lack knowledge; provide **Don't know / Cannot assess**.
2. Store multi-select responses as separate binary variables.
3. Randomise unordered option lists where supported by the survey platform; keep ordinal scales (2.1, 2.2, 3.1, 3.2, 4.12, 5.3, 5.4, 7.1) in fixed order.
4. Keep "Other" as a separate binary variable plus free-text field.
5. Keep "None" and "Don't know" mutually exclusive with substantive options.
6. Use identical duration categories for 2.3 and 4.1.
7. Retain respondent-level and institution-level variables separately.
8. Flag duplicate institution responses during data cleaning where institution identity is available.
9. Do not automatically merge conflicting responses from the same institution; define a reconciliation rule before analysis.
10. Preserve the exact survey version used for every response. We restart survey responses after pre-testing.
11. Store each row of matrix items (2.2, 4.3) as a separate ordinal variable, keeping the LamaPoll column coding (1 = most advanced stage … 4 = none; 5 = Don't know / n.a., treated as missing).
12. Remove direct identifiers and technical metadata from the research dataset before any sharing, including sharing within the EA SIG. This covers the contact e-mail (8.1), the LamaPoll participant fields "E-Mail" and "Name", all timestamps ("Datum", "Startzeit", "Endzeit"), device, operating system, browser and referrer. Keep contact details in a separate contact list with restricted access. Before removing timestamps, derive the coarse variable `FIELD_WEEK` (see Analysis Matrix B); keep durations only internally for data-quality checks and drop them before publication. Keep the distribution attributes (channel, reminder) in the research dataset.
13. Exclude responses with 0.1 = Preview or Leave from the research dataset; keep any feedback given in 9.1 for survey improvement only.

---

# Open Items

The following design decisions require clarification of the study's intended claims or use of the results.

## OI-1 — Population claim and sampling strategy

What should the final study claim?

1. Descriptive results for participating institutions / respondents only
2. Approximate landscape of the EUNIS community
3. Estimates intended to describe European higher education institutions more broadly

The third objective would require a substantially more explicit sampling frame, recruitment strategy, and treatment of non-response.

> Options 1 and 2, definitely not 3, since we do not have a good distribution channel beyond EUNIS.
> Distribution will be done via the national bodies registered in EUNIS. We have 15 organisations named on eunis.org/eunis-members (section "Partners", list "Member Organisations of EUNIS").

## OI-2 — One response per institution vs. multiple expert responses

Should the study aim for:

1. one authoritative institutional response,
2. multiple expert responses that are analysed independently, or
3. multiple responses that are reconciled into one institutional record?

This determines recruitment wording, duplicate handling, and the unit used in inferential analyses.

> Option 2 is key. However, we will often get only one answer per institution and treat it as option 1.

> Decided: Item 1.7 records the respondent's organisational unit, mirroring the rows of 2.2. If several experts from the same institution respond, differing answers (e.g. in 2.1 or 2.2) can then be interpreted as different vantage points (e.g. central IT vs. faculty) instead of being treated as inconsistencies. Responses are not merged. Respondent-level analysis is primary; institution-level counts use one response per institution, selected by a predefined rule (highest knowledge in 1.8), and are reported as a sensitivity analysis (see Analysis Matrix E3).

## OI-3 — Scope of "Higher Education Institution"

Should research institutes and other non-teaching organisations remain part of the target population, or should the survey focus strictly on higher education institutions?

> Yes. Keep this. Just to see the differences.

## OI-4 — Required depth of framework comparison

Is it sufficient to know which frameworks / reference models / modelling languages are used, or should the study compare for each selected approach:

- adoption status,
- start year,
- organisational scope,
- purpose of use?

A framework-by-framework comparison would require a repeated question block or matrix.

> Decided: No framework-by-framework comparison in this wave. 2.4 records which frameworks, reference models, modelling languages and in-house approaches are used, piloted or evaluated (one binary variable per option). Adoption status, start year, scope and purpose per framework are reserved for follow-up research (OI-12). For HERM, status (3.2), duration (4.1), artefact stage (4.3) and application areas (4.2) are captured in detail.

## OI-5 — Meaning of HERM adoption

Should "adoption" require operational use, or should active evaluation and pilots also count as adoption in headline reporting?

A reporting definition should be fixed before fieldwork.

> Decided: Adoption starts with pilot use. Labels follow the answer options of 3.2.

| 3.2 answer option                                | Is adoption  | Reporting category         |
| ------------------------------------------------ | -----------: | -------------------------- |
| Not considered                                   |           no | non-adoption               |
| Being evaluated / considered                     |           no | considering adoption       |
| Pilot or experimental use                        |          yes | early / pilot adoption     |
| Active operational use                           |          yes | operational adoption       |
| Embedded in governance or standard EA processes  |          yes | institutionalised adoption |
| Previously used, but no longer in use            | formerly yes | discontinued adoption      |
| Don't know / Cannot assess                       |            — | excluded (unknown)         |

> Note: Routing after 3.2 does not follow this definition one-to-one. "Being evaluated / considered" is routed to Section 4 (usage details) although it does not count as adoption, and "Previously used" is routed to Section 5. Reports on Section 4 must therefore distinguish evaluators from adopters. Evaluators and pilot users additionally answer 5.1 and 5.2 after Section 4, so barrier results must be reported separately by 3.2 status.

## OI-6 — HERM artefact taxonomy

Which artefacts are officially considered part of HERM for this study, and which are related artefacts or methods used alongside HERM?

The final answer options should use one agreed taxonomy and naming convention.

> Decided: The HERM reference models in 4.3 are BRM, DRM, ARM, TRM and SRM. The SRM is scheduled for HERM 4.0 but is already included in HERM 3.2 as an alpha version for community feedback; "Don't know / n.a." in 4.3 covers institutions using a version without SRM. Related artefacts and approaches used alongside HERM (Business Model Canvas, Recipe Cards, Process Models, Value Streams) are captured separately in 4.4.

## OI-7 — Desired granularity of institutional application areas

Is a broad functional classification sufficient, or should HERM Business Capabilities be captured using a formal HERM capability hierarchy?

If formal capability-level analysis is intended, a controlled selection should replace optional free text.

> Decided: A broad functional classification (4.2) is sufficient for this wave. The primary area can be specified as an optional HERM Business Capability name or identifier (4.5, free text); these answers are coded qualitatively where possible. Formal capability-level analysis is not intended.

## OI-8 — Case-study selection criteria

What makes a case "transfer-worthy" for the purposes of the study?

Possible criteria include:

- demonstrated outcome, -> yes
- reuse potential, -> yes
- documentation quality, -> no
- cross-institutional relevance, -> yes
- maturity, -> yes
- novelty, -> no
- willingness to share. -> yes

The criteria should be defined before using survey responses to rank cases.

> See "-> yes/no" entries.

## OI-9 — Intended analysis of institutional size

Will student and staff size be used only descriptively, or should they support statistical comparisons between institution-size groups?

If comparative analysis is planned, the final category boundaries should be aligned with expected sample sizes and relevant European higher-education classifications.

> Head-count categories are adapted, and we will use them to compare groups of institutions.

## OI-10 — Country-level analysis

Are country comparisons an intended output?

If yes, minimum case counts per country, treatment of uneven national recruitment, and aggregation rules should be specified before fieldwork.

> We have a few countries where fewer than 10 universities exist. Grouping them into one class might be an option for group-wise comparison.

> Decided (2026-10-08): The minimum size of a country group is 5 participating institutions. All countries with fewer institutions are pooled into one group, "Other countries". This rule is to be re-assessed after the field phase (see Analysis Matrix E1).

## OI-11 — EA maturity beyond HERM status

Is the study intended to compare overall EA maturity between institutions?

If yes, the current EA status item is insufficient; a separate multi-item EA maturity construct would be required.

> Decided: No validated maturity construct in this wave. 2.1 (highest EA status), 2.2 (coverage across organisational areas), 2.3 (age), 2.5/2.6 (anchoring) and 3.2 (HERM status) are reported together as an "EA status and coverage profile", not as "EA maturity". A multi-dimensional maturity assessment remains a candidate for follow-up research (OI-12).

## OI-12 — Relationship to follow-up research

Which topics must be answered quantitatively in this first wave, and which are explicitly reserved for interviews, workshops, or a second survey?

Candidate follow-up topics include:

- detailed EA tooling,
- professional background of respondents,
- planning horizons,
- detailed governance arrangements,
- detailed maturity dimensions,
- implementation costs and resources,
- failure cases,
- detailed mappings between HERM and other frameworks.

> Decided: All candidate topics above are reserved for follow-up interviews, workshops or a second survey, together with framework-by-framework comparison (OI-4) and a multi-dimensional maturity assessment (OI-11). This wave answers quantitatively: EA status, coverage, age, approaches and anchoring (Section 2), HERM status and usage (Sections 3–4), barriers (Section 5), and support needs (Section 6). Respondents willing to take part in follow-up activities are identified via 7.2.

## OI-13 — Publication and data-sharing model

Will the published output contain:

- aggregated statistics only,
- anonymised respondent-level data,
- named institution-level data with consent,
- or a public case-study directory?

The final consent and privacy wording depends on this decision.

> Decided (see [[Introduction-text]]): a pseudonymised respondent-level dataset is published for long-term access via the Zenodo community "Research on Digital Transformation and Information Technology in Higher Education in Europe" under CC-BY-NC-SA 4.0. Contact details and other direct identifiers are excluded (data rule 12). Institutions are named only with permission in 8.2.

## OI-14 — Survey language

Will the survey be English-only or translated into national languages?

If translated, a translation and reconciliation procedure should be defined to preserve measurement equivalence across language versions.

> Decided: English only, using British spelling, as institutions from all over Europe are invited. No translation procedure is required.

---

# Estimated Completion Time

- HERM operational user: approximately 8–10 minutes
- HERM evaluator / pilot: approximately 7–9 minutes
- HERM non-user with EA practice: approximately 5–7 minutes
- Respondent without active EA practice: approximately 4–5 minutes

> Update 2026-10-08: The estimates above are the original design targets. The project team now expects about 20 minutes on average, varying strongly with the institution's EA and HERM experience and the length of free-text answers. Communication to respondents and distribution partners uses "about 20 minutes on average" (see `Survey_Invitation.md`). Replace the per-path estimates with medians from the first field responses.

